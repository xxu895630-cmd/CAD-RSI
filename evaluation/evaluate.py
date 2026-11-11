"""Evaluate generated STEP files against ground truth using IoU, SIoU, CD, and VAGF."""
import argparse
import hashlib
import importlib.metadata
import importlib.util
import json
import math
import os
from pathlib import Path
import signal
import statistics
import subprocess
import sys
import tempfile

SURFACE_SAMPLES = 8192
OCCUPANCY_SAMPLES = 500000
SEED_NAMESPACE = "bench300_paper_formulas_v1"
TAU_MIN, TAU_MAX = 1e-5, 1e-1
DEPENDENCIES = ("cadquery", "numpy", "scipy", "open3d")


def load_geometry_dependencies():
    global np, cq, BRepGProp, GProp_GProps, gp_Trsf
    global BRepBuilderAPI_Transform, BRepMesh_IncrementalMesh, BRepTools
    import numpy as np
    import cadquery as cq
    from OCP.BRepGProp import BRepGProp
    from OCP.GProp import GProp_GProps
    from OCP.gp import gp_Trsf
    from OCP.BRepBuilderAPI import BRepBuilderAPI_Transform
    from OCP.BRepMesh import BRepMesh_IncrementalMesh
    from OCP.BRepTools import BRepTools


def write_json(path, value):
    path = Path(path)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def seed_for(part_id, role):
    text = f"{part_id}|{role}|{SEED_NAMESPACE}"
    return int.from_bytes(hashlib.sha256(text.encode("utf-8")).digest()[:8], "big")


def load_shape(path):
    obj = cq.importers.importStep(str(path))
    shapes = obj.vals()
    if not shapes:
        raise ValueError("Empty STEP")
    return shapes[0] if len(shapes) == 1 else cq.Compound.makeCompound(shapes)


def properties(shape):
    bbox = shape.BoundingBox()
    lo = np.array([bbox.xmin, bbox.ymin, bbox.zmin], dtype=float)
    hi = np.array([bbox.xmax, bbox.ymax, bbox.zmax], dtype=float)
    extent = hi - lo
    if not np.isfinite(np.r_[lo, hi]).all() or max(extent) <= 0:
        raise ValueError("Invalid bounding box")
    faces = shape.Faces()
    solid_faces = {f.hashCode() for s in shape.Solids() for f in s.Faces()}
    all_faces = {f.hashCode() for f in faces}
    # Closed-shell volume is meaningful only when actual Solid objects own every face.
    complete_solid = bool(shape.Solids()) and solid_faces == all_faces
    vp = GProp_GProps()
    if complete_solid:
        BRepGProp.VolumeProperties_s(shape.wrapped, vp)
    volume = float(vp.Mass()) if complete_solid else 0.0
    volume_eps = max(float(max(extent)) ** 3 * 1e-12, 1e-18)
    solid = complete_solid and math.isfinite(volume) and volume > volume_eps
    ap = GProp_GProps()
    BRepGProp.SurfaceProperties_s(shape.wrapped, ap)
    area = float(ap.Mass())
    props = vp if solid else ap
    com = props.CentreOfMass()
    center = np.array([com.X(), com.Y(), com.Z()])
    matrix = props.MatrixOfInertia()
    inertia = np.array([[matrix.Value(i, j) for j in range(1, 4)] for i in range(1, 4)])
    mass = float(props.Mass())
    radius = math.sqrt(float(np.trace(inertia)) / (2 * mass)) if mass > 0 else float("nan")
    eigenvalues, basis = np.linalg.eigh(inertia)
    # Proper frames ensure each of the four sign combinations lies in SO(3).
    if np.linalg.det(basis) < 0:
        basis[:, -1] *= -1
    valid = bool(shape.isValid() and len(faces) and math.isfinite(area) and area > 0 and
                 np.isfinite(center).all() and math.isfinite(radius) and radius > 0)
    return {"valid": valid, "solid": bool(solid), "volume": volume, "area": area,
            "lo": lo, "hi": hi, "extent": extent, "center": center,
            "inertia": inertia, "radius": radius, "basis": basis,
            "eigenvalues": eigenvalues}


def sample_surface(shape, props, part_id, role, n):
    tol = float(max(props["extent"])) * 2e-4
    BRepTools.Clean_s(shape.wrapped)
    BRepMesh_IncrementalMesh(shape.wrapped, tol, False, 0.05, False).Perform()
    vertices, faces = shape.tessellate(tol, angularTolerance=0.05)
    v = np.asarray([p.toTuple() for p in vertices], dtype=float)
    f = np.asarray(faces, dtype=np.int64)
    if v.size == 0 or f.size == 0:
        raise ValueError("No tessellated surface")
    tri = v[f]
    areas = np.linalg.norm(np.cross(tri[:, 1] - tri[:, 0], tri[:, 2] - tri[:, 0]), axis=1) / 2
    keep = np.isfinite(areas) & (areas > 0)
    tri, areas = tri[keep], areas[keep]
    if not len(areas) or not np.isfinite(tri).all():
        raise ValueError("Invalid surface tessellation")
    rng = np.random.default_rng(seed_for(part_id, role))
    selected = tri[rng.choice(len(tri), n, p=areas / areas.sum())]
    a = np.sqrt(rng.random(n))[:, None]
    b = rng.random(n)[:, None]
    points = (1-a)*selected[:, 0] + a*(1-b)*selected[:, 1] + a*b*selected[:, 2]
    return points, {"vertices": len(v), "triangles": len(tri), "deflection": tol,
                    "seed": seed_for(part_id, role)}


def transformed_shape(shape, scale, rotation, translation):
    # Matrix->gp_Trsf preserves analytic faces for rigid and uniform-scale transforms.
    values = np.column_stack([scale * rotation, translation]).ravel().tolist()
    t = gp_Trsf()
    t.SetValues(*values)
    return cq.Shape.cast(BRepBuilderAPI_Transform(shape.wrapped, t, True).Shape())


def volume_of(shape):
    gp = GProp_GProps()
    BRepGProp.VolumeProperties_s(shape.wrapped, gp)
    return float(gp.Mass())


def exact_iou(pred, gt, vp, vg):
    common = pred.intersect(gt)
    if not common.isValid():
        raise ValueError("Invalid boolean common shape")
    overlap = volume_of(common)
    if not math.isfinite(overlap) or overlap < 0 or overlap > min(vp, vg):
        raise ValueError("Invalid boolean intersection volume")
    union = vp + vg - overlap
    if union <= 0:
        raise ValueError("Undefined IoU union")
    return float(overlap / union)


def boolean_failure_category(exc):
    value = str(exc)
    if "Invalid boolean intersection volume" in value:
        return "intersection_volume_out_of_bounds"
    if "Invalid boolean common shape" in value:
        return "invalid_boolean_common_shape"
    if "Null TopoDS_Shape" in value or "Null shape" in value:
        return "null_boolean_shape"
    if "Undefined IoU union" in value:
        return "nonpositive_union_volume"
    return "boolean_backend_exception"


def rotations(g, p):
    signs = [(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)]
    return [g["basis"] @ np.diag(s) @ p["basis"].T for s in signs]


def point_metrics(predicted, target, threshold):
    from scipy.spatial import cKDTree
    d_pt = cKDTree(target).query(predicted, k=1)[0]
    d_tp = cKDTree(predicted).query(target, k=1)[0]
    return {
        "cd": float(np.mean(d_pt ** 2) + np.mean(d_tp ** 2)),
        "siou": float((np.mean(d_pt < threshold) + np.mean(d_tp < threshold)) / 2),
    }


def vagf_score(valid, cd):
    if not valid or cd is None or not math.isfinite(cd) or cd < 0:
        return 0.0
    value = math.log(TAU_MAX / max(cd, TAU_MIN)) / math.log(TAU_MAX / TAU_MIN)
    return min(1.0, max(0.0, value)) ** 2


def solid_meshes(shape, props):
    meshes = []
    for solid in shape.Solids():
        vertices, faces = solid.tessellate(float(max(props["extent"])) * 2e-4,
                                         angularTolerance=0.05)
        vertices = np.asarray([p.toTuple() for p in vertices], dtype=float)
        faces = np.asarray(faces, dtype=np.int64)
        if not len(vertices) or not len(faces) or not np.isfinite(vertices).all():
            raise ValueError("Invalid occupancy triangulation")
        meshes.append((vertices, faces))
    if not meshes:
        raise ValueError("No solids for occupancy evaluation")
    return meshes


def occupancy_iou(pred_meshes, gt_meshes, job):
    import open3d as o3d
    rotation = np.asarray(job["rotation"])
    translation = np.asarray(job["translation"])
    pred_meshes = [(v @ rotation.T * job["scale"] + translation, f)
                   for v, f in pred_meshes]
    all_vertices = np.concatenate([v for v, _ in pred_meshes + gt_meshes])
    lo, hi = all_vertices.min(axis=0), all_vertices.max(axis=0)
    center, length = (lo + hi) / 2, float(max(hi - lo))
    if not math.isfinite(length) or length <= 0:
        raise ValueError("Invalid occupancy bounds")

    def scenes(meshes):
        result = []
        for vertices, faces in meshes:
            mesh = o3d.t.geometry.TriangleMesh(
                o3d.core.Tensor(((vertices - center) / length).astype(np.float32)),
                o3d.core.Tensor(faces.astype(np.uint32)))
            scene = o3d.t.geometry.RaycastingScene(nthreads=1)
            scene.add_triangles(mesh)
            result.append(scene)
        return result

    def occupied(scene_list, points):
        inside = np.zeros(len(points), dtype=bool)
        tensor = o3d.core.Tensor(points.astype(np.float32))
        for scene in scene_list:
            inside |= scene.compute_occupancy(tensor, nthreads=1, nsamples=3).numpy() > 0.5
        return inside

    rng = np.random.Generator(np.random.PCG64(job["seed"]))
    points = (rng.uniform(lo, hi, size=(OCCUPANCY_SAMPLES, 3)) - center) / length
    pred_inside = occupied(scenes(pred_meshes), points)
    gt_inside = occupied(scenes(gt_meshes), points)
    union = int(np.count_nonzero(pred_inside | gt_inside))
    if union == 0:
        raise ValueError("No occupied samples in the Monte Carlo union")
    return float(np.count_nonzero(pred_inside & gt_inside) / union)


def run_exact_worker(request):
    prediction = load_shape(request["prediction"])
    target = load_shape(request["ground_truth"])
    results = {}
    for job in request["jobs"]:
        try:
            transformed = transformed_shape(prediction, job["scale"],
                                            np.asarray(job["rotation"]),
                                            np.asarray(job["translation"]))
            iou = exact_iou(transformed, target, job["prediction_volume"],
                            job["target_volume"])
            results[str(job["index"])] = {"iou": iou, "fallback_reason": None}
        except Exception as exc:
            results[str(job["index"])] = {
                "iou": None, "fallback_reason": boolean_failure_category(exc)}
        # Retain completed candidates if a later Boolean operation times out.
        write_json(request["output"], results)


def exact_candidates(request, jobs, work):
    output = work / "exact.json"
    request_path = work / "exact_request.json"
    write_json(request_path, {**request, "jobs": jobs, "output": str(output)})
    reason = "exact_worker_failure"
    with (work / "exact.log").open("wb") as log:
        try:
            subprocess.run([sys.executable, "-B", str(Path(__file__).resolve()),
                            "--worker", "exact", str(request_path)],
                           stdout=log, stderr=log, timeout=request["boolean_timeout"],
                           check=False)
        except subprocess.TimeoutExpired:
            reason = "exact_stage_timeout"
    results = json.loads(output.read_text(encoding="utf-8")) if output.exists() else {}
    for job in jobs:
        results.setdefault(str(job["index"]), {"iou": None, "fallback_reason": reason})
    return results


def empty_record(part_id):
    return {"id": part_id, "status": "not_evaluated", "valid": None,
            "iou_eligible": None, "iou": None, "siou": None, "cd": None,
            "vagf": 0.0, "error": None}


def evaluate_pair(request, work):
    row = empty_record(request["id"])
    state = work / "result.json"
    try:
        target = load_shape(request["ground_truth"])
        gp = properties(target)
        if not gp["valid"]:
            raise ValueError("Ground-truth geometry is invalid")
        row["iou_eligible"] = gp["solid"]
    except Exception as exc:
        row.update(status="ground_truth_error", error=str(exc))
        write_json(state, row)
        return
    if request["prediction"] is None or not Path(request["prediction"]).exists():
        row.update(status="missing_prediction", valid=False)
        write_json(state, row)
        return
    try:
        prediction = load_shape(request["prediction"])
        pp = properties(prediction)
        if not pp["valid"] or (gp["solid"] and not pp["solid"]):
            raise ValueError("Prediction does not satisfy the target's geometry validity requirements")
    except Exception as exc:
        row.update(status="invalid_prediction", valid=False, error=str(exc))
        write_json(state, row)
        return
    row.update(status="computing_metrics", valid=True)
    write_json(state, row)
    try:
        target_points, _ = sample_surface(target, gp, request["id"], "target", request["samples"])
        predicted_points, _ = sample_surface(prediction, pp, request["id"], "prediction", request["samples"])
        length = float(max(gp["extent"]))
        origin = (gp["hi"] + gp["lo"]) / 2
        target_points = (target_points - origin) / length
        threshold = 0.01 * float(np.linalg.norm(gp["extent"])) / length
        scale = gp["radius"] / pp["radius"] if request["alignment"] == "similarity" else 1.0
        track = "paper_similarity" if request["alignment"] == "similarity" else "physical_rigid"
        jobs, candidates = [], []
        for index, rotation in enumerate(rotations(gp, pp)):
            native_shift = gp["center"] - scale * rotation @ pp["center"]
            shift = (gp["center"] - origin - scale * rotation @ pp["center"]) / length
            points = (predicted_points @ rotation.T) * scale / length + shift
            candidates.append({"index": index, "iou": None,
                               **point_metrics(points, target_points, threshold)})
            seed_text = f"{request['id']}|{track}|{index}|bench300_iou_mc500k_v2"
            jobs.append({"index": index, "scale": scale, "rotation": rotation.tolist(),
                         "translation": native_shift.tolist(),
                         "prediction_volume": pp["volume"] * scale ** 3,
                         "target_volume": gp["volume"],
                         "seed": int.from_bytes(hashlib.sha256(seed_text.encode()).digest()[:8], "big")})
        methods = []
        if gp["solid"]:
            exact = exact_candidates(request, jobs, work)
            pred_meshes = gt_meshes = None
            for candidate, job in zip(candidates, jobs):
                result = exact[str(job["index"])]
                reason = result["fallback_reason"]
                if reason:
                    if pred_meshes is None:
                        pred_meshes = solid_meshes(prediction, pp)
                        gt_meshes = solid_meshes(target, gp)
                    candidate["iou"] = occupancy_iou(pred_meshes, gt_meshes, job)
                else:
                    candidate["iou"] = result["iou"]
                methods.append({"rotation_index": job["index"],
                                "method": "occupancy_mc" if reason else "exact_brep",
                                "fallback_reason": reason})
            chosen = max(candidates, key=lambda item: item["iou"])
        else:
            chosen = min(candidates, key=lambda item: item["cd"])
        row.update({key: chosen[key] for key in ("iou", "siou", "cd")})
        row.update(status="success", vagf=vagf_score(True, row["cd"]),
                   selected_rotation=chosen["index"], iou_methods=methods)
    except Exception as exc:
        row.update(status="metric_error", error=str(exc), iou=None, siou=None, cd=None, vagf=0.0)
    write_json(state, row)


def summarize(rows):
    valid = [row for row in rows if row["valid"] is True]
    invalid = sum(row["valid"] is False for row in rows)
    complete = all(row["status"] in ("success", "invalid_prediction", "missing_prediction") for row in rows)
    ious = [row["iou"] for row in valid if row["iou_eligible"]]
    sious, cds = [row["siou"] for row in valid], [row["cd"] for row in valid]

    def mean(values):
        return statistics.fmean(values) if complete and values else None

    return {"complete": complete, "total_count": len(rows), "valid_count": len(valid),
            "invalid_count": invalid, "unknown_validity_count": len(rows) - len(valid) - invalid,
            "iou_count": len(ious), "siou_count": len(sious), "cd_count": len(cds),
            "vagf_count": len(rows), "iou_mean": mean(ious), "siou_mean": mean(sious),
            "cd_mean": mean(cds),
            "cd_median": statistics.median(cds) if complete and cds else None,
            "vagf": statistics.fmean(row["vagf"] for row in rows) if complete else None}


def index_steps(directory):
    indexed, normalized = {}, {}
    for path in sorted(directory.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in (".step", ".stp"):
            continue
        key = path.stem
        if key.casefold() in normalized:
            raise ValueError(f"Ambiguous STEP ID '{key}': {normalized[key.casefold()]} and {path}")
        normalized[key.casefold()] = path
        indexed[key] = path.resolve()
    return indexed


def input_pairs(prediction, target, part_id):
    if target.is_file():
        if target.suffix.lower() not in (".step", ".stp"):
            raise ValueError("Ground truth must be a .step or .stp file")
        if prediction.is_dir() or prediction.suffix.lower() not in (".step", ".stp"):
            raise ValueError("Pair mode requires a prediction STEP path (which may be missing)")
        return [(part_id or target.stem, prediction, target)]
    if not target.is_dir() or not prediction.is_dir():
        raise ValueError("Batch mode requires existing prediction and ground-truth directories")
    if part_id is not None:
        raise ValueError("--id is only available in pair mode")
    gt, pred = index_steps(target), index_steps(prediction)
    if not gt:
        raise ValueError("No ground-truth STEP files found")
    extra = sorted(set(pred) - set(gt))
    if extra:
        raise ValueError("Prediction IDs absent from ground truth: " + ", ".join(extra[:10]))
    return [(key, pred.get(key), gt[key]) for key in sorted(gt)]


def run_pair(request, work):
    request_path, result_path = work / "request.json", work / "result.json"
    write_json(request_path, request)
    failure = None
    with (work / "worker.log").open("wb") as log:
        process = subprocess.Popen(
            [sys.executable, "-B", str(Path(__file__).resolve()), "--worker", "pair", str(request_path)],
            stdout=log, stderr=log, start_new_session=(os.name != "nt"))
        try:
            returncode = process.wait(timeout=request["timeout"])
            if returncode != 0:
                failure = f"Evaluation worker exited with code {returncode}"
        except subprocess.TimeoutExpired:
            failure = f"Evaluation exceeded {request['timeout']} seconds"
            stop_worker_tree(process)
        except BaseException:
            stop_worker_tree(process)
            raise
    row = json.loads(result_path.read_text(encoding="utf-8")) if result_path.exists() else empty_record(request["id"])
    if failure or row["status"] in ("not_evaluated", "computing_metrics"):
        row.update(status="metric_error" if row["valid"] is True else "evaluation_error",
                   error=failure or "Evaluation worker did not finish",
                   iou=None, siou=None, cd=None, vagf=0.0)
        diagnostics = (work / "worker.log").read_text(encoding="utf-8", errors="replace").strip()
        if diagnostics:
            row["error"] += ": " + diagnostics[-1500:]
    return row


def stop_worker_tree(process):
    # The pair worker may own a running Boolean worker. Stop both before cleanup.
    if os.name == "nt":
        subprocess.run(["taskkill", "/PID", str(process.pid), "/T", "/F"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    else:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
    if process.poll() is None:
        process.kill()
    process.wait()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prediction", required=True, type=Path, help="Prediction STEP file or directory")
    parser.add_argument("--ground-truth", required=True, type=Path, help="Ground-truth STEP file or directory")
    parser.add_argument("--id", help="Pair ID used for sampling seeds; defaults to the ground-truth stem")
    parser.add_argument("--samples", type=int, default=SURFACE_SAMPLES, help="Surface points per shape (default: 8192)")
    parser.add_argument("--alignment", choices=("similarity", "rigid"), default="similarity")
    parser.add_argument("--output", type=Path, help="Save JSON here; otherwise write it to standard output")
    parser.add_argument("--timeout", type=float, default=900, help="Maximum seconds per pair (default: 900)")
    parser.add_argument("--boolean-timeout", type=float, default=120, help="Seconds for exact IoU candidates before fallback")
    args = parser.parse_args()
    if args.samples < 1:
        parser.error("--samples must be positive")
    if not all(math.isfinite(t) and t > 0 for t in (args.timeout, args.boolean_timeout)):
        parser.error("Timeouts must be finite and positive")
    # Keep the outer deadline beyond the isolated Boolean deadline.
    if args.timeout <= args.boolean_timeout + 30:
        parser.error("--timeout must exceed --boolean-timeout by more than 30 seconds")
    try:
        pairs = input_pairs(args.prediction.resolve(), args.ground_truth.resolve(), args.id)
        missing = [name for name in DEPENDENCIES if importlib.util.find_spec(name) is None]
        if missing:
            raise ValueError("Missing dependencies: " + ", ".join(missing) + "; install evaluation/requirements.txt")
        if args.output:
            output = args.output.resolve()
            inputs = {p for _, pred, gt in pairs for p in (pred, gt) if p is not None}
            if output in inputs or output == Path(__file__).resolve() or output.suffix.lower() != ".json":
                raise ValueError("--output must be a .json path that does not overwrite an input or the script")
            if not output.parent.is_dir():
                raise ValueError("The output parent directory must already exist")
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    rows = []
    for index, (part_id, prediction, target) in enumerate(pairs, 1):
        request = {"id": part_id, "prediction": str(prediction) if prediction else None,
                   "ground_truth": str(target), "samples": args.samples,
                   "alignment": args.alignment, "timeout": args.timeout,
                   "boolean_timeout": args.boolean_timeout}
        with tempfile.TemporaryDirectory(prefix="cad_rsi_eval_") as directory:
            row = run_pair(request, Path(directory))
        rows.append(row)
        print(f"[{index}/{len(pairs)}] {part_id}: {row['status']}", file=sys.stderr, flush=True)
    report = {"settings": {"surface_samples_per_shape": args.samples,
                           "surface_seed_namespace": SEED_NAMESPACE,
                           "alignment": args.alignment,
                           "cd_definition": "sum of two mean squared nearest-neighbor distances",
                           "cd_display_multiplier": 1000,
                           "siou_distance_threshold": "0.01 * ground-truth bounding-box diagonal",
                           "iou_fallback_samples": OCCUPANCY_SAMPLES,
                           "tau_min": TAU_MIN, "tau_max": TAU_MAX,
                           "pair_timeout_seconds": args.timeout,
                           "boolean_timeout_seconds": args.boolean_timeout,
                           "python_version": sys.version.split()[0],
                           "versions": {name: importlib.metadata.version(name)
                                        for name in (*DEPENDENCIES, "cadquery-ocp")}},
              "summary": summarize(rows), "per_sample": rows}
    if args.output:
        write_json(args.output.resolve(), report)
        print(f"Saved evaluation to {args.output}", file=sys.stderr)
    else:
        print(json.dumps(report, indent=2, allow_nan=False))
    return 0 if report["summary"]["complete"] else 1


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "--worker":
        # Internal subprocess entry points; all intermediate files are temporary.
        load_geometry_dependencies()
        request_path = Path(sys.argv[3])
        request = json.loads(request_path.read_text(encoding="utf-8"))
        if sys.argv[2] == "exact":
            run_exact_worker(request)
        elif sys.argv[2] == "pair":
            evaluate_pair(request, request_path.parent)
        else:
            raise ValueError("Unknown worker mode")
    else:
        raise SystemExit(main())


