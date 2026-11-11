import cadquery as cq

profile_plane = cq.Plane(origin=(29.3972838447065, 24.2266889438809, -0.430061978368164), xDir=(1.0, 0.0, 0.0), normal=(0.0, -1.577926534622511e-05, 0.9999999998755075))

outer_profile = (cq.Workplane(profile_plane).moveTo(-7.620000000000001, 0.0)
    .lineTo(0.0, 0.0)
    .lineTo(0.0, 8.750000000000007)
    .lineTo(-7.620000000000001, 8.750000000000036)
    .lineTo(-7.620000000000001, 0.0)
    .close().val())

extrusion_vector = (0.0, 7.889632673112588e-06, -0.49999999993775573)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
