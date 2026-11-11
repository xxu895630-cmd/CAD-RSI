# STEP evaluation

Evaluate generated STEP files against ground-truth STEP files using IoU, SIoU,
Chamfer Distance (CD), and Validity-Aware Geometric Fidelity (VAGF).
The evaluator only reads STEP geometry; it does not execute reconstruction code.

## Installation

Use Python 3.9-3.11 in a dedicated environment. From the repository root:

```bash
python -m venv .venv
# Activate the environment before installing dependencies.
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -r evaluation/requirements.txt
```

## Usage

Evaluate one pair (filenames may differ):

```bash
python evaluation/evaluate.py --prediction generated.step --ground-truth reference.step
```

Evaluate a dataset and save one JSON report:

```bash
python evaluation/evaluate.py --prediction predictions --ground-truth MechAtlas_300_samples --output scores.json
```

Batch mode recursively matches `.step` and `.stp` files by their **case-sensitive
filename stem**. For example, `predictions/00000117.step` matches
`MechAtlas_300_samples/00000117/00000117.step`. Preserve leading zeros.
Duplicate IDs, including case-only collisions, and prediction IDs absent from
ground truth are rejected. Ground truth defines the complete evaluation set;
missing predictions are included as invalid outputs. An empty prediction directory
is allowed. In pair mode, `--id` optionally sets the ID used to derive sampling seeds.

Defaults: `--samples 8192`, `--alignment similarity`, `--timeout 900`, and
`--boolean-timeout 120` (seconds). Use `--alignment rigid` to disable scale fitting.
Keep the same alignment and sample count across methods. Changing sample count
changes CD, SIoU, and consequently VAGF. A report records the settings and dependency
versions used.

Without `--output`, JSON goes to standard output; progress goes to standard error.
Temporary worker files are removed automatically. Exit codes are 0 for a complete
evaluation (including invalid predictions), 1 for incomplete evaluation, and 2 for
invalid arguments or missing dependencies.

## Metric definitions

Each shape uses **8,192 surface samples by default**. Tessellation uses absolute
linear deflection `2e-4 * longest bounding-box edge` and angular deflection `0.05`
radians. Triangles are selected in proportion to area, with uniform barycentric
sampling within each triangle. Independent deterministic PCG64 generators use
the first eight big-endian bytes of SHA256 of
`ID|ROLE|bench300_paper_formulas_v1`; `ROLE` is `target` or `prediction`.
Even identical surfaces can therefore have a small positive sampled CD.

Similarity alignment matches centroids, fits uniform scale using
`sqrt(trace(inertia) / (2 * mass))`, and tests the four proper principal-axis sign
rotations `+++`, `+--`, `-+-`, and `--+`. Solid targets select the highest-IoU
candidate; exact ties retain the first candidate. There is no ICP or reflection.
Surface-only targets use area properties and select the lowest-CD candidate.
The common ground-truth bounding-box center and longest edge normalize both point
sets so that the ground-truth longest edge equals one.

Let `P` and `G` be the aligned, normalized sampled surfaces and `d(p, G)` the
Euclidean distance to the nearest sampled point in `G`.

| Metric | Definition |
| --- | --- |
| IoU | Intersection volume divided by union volume, in `[0, 1]`. |
| SIoU | `0.5 * (mean(d(P,G) < t) + mean(d(G,P) < t))`, where `t` is 1% of the normalized ground-truth bounding-box diagonal. |
| CD | `mean(d(P,G)^2) + mean(d(G,P)^2)`. No square root or factor of one half. |
| VAGF | Mean over all expected samples of `clip(log(tau_max / max(CD, tau_min)) / log(tau_max / tau_min), 0, 1)^2`, with `tau_min = 1e-5` and `tau_max = 1e-1`. Invalid predictions contribute zero. |

JSON reports raw CD. Multiply it by **1,000** only to reproduce the paper's CD
display units; VAGF always uses raw CD. IoU and SIoU are fractions; multiply by 100
for percentages. Per-sample VAGF entries are contributions to the dataset average.

IoU uses native-coordinate BRep intersections. Failed or invalid Boolean results,
out-of-range intersection volumes, or Boolean timeouts trigger a deterministic
500,000-query occupancy estimate on the original tessellated solids. Each solid
is tested separately and occupancies are unioned. Open3D uses CPU ray casting,
three rays per query, and one thread. The PCG64 seed derives from
`ID|TRACK|ROTATION_INDEX|bench300_iou_mc500k_v2`, where `TRACK` is
`paper_similarity` or `physical_rigid`, using the same SHA256 truncation above.
All exact candidates share the Boolean deadline. Low IoU alone does not trigger
fallback. The report records each candidate's backend and fallback reason.
No mesh repair is applied. Occupancy is approximate, especially for thin parts.
For internally overlapping multi-solid compounds, BRep mass properties sum solid
contributions while occupancy uses their union; the two backends need not agree.
Kernel and library versions can also affect numerical results.

## Validity and aggregation

A valid prediction must import as nonempty, finite, valid geometry with positive
area. For solid ground truth, every prediction face must belong to a solid, and
volume must exceed `max(longest_edge^3 * 1e-12, 1e-18)`. Surface-only ground truth
accepts valid positive-area surfaces; its IoU is undefined (`null`).

IoU means include only valid, volume-eligible pairs. SIoU means and CD mean/median
include only valid pairs. VAGF includes **all ground-truth IDs**, including invalid
and missing predictions. When no prediction is valid, geometric aggregates are
`null` and VAGF is zero.

Ground-truth errors, timeouts, and metric backend failures are distinct from
invalid predictions. Failed samples have a zero provisional VAGF contribution,
but any such evaluation error marks the report incomplete and suppresses all
aggregate metrics (`null`). Fix the error and rerun before reporting scores.
