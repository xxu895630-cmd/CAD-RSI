import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, -1.1657341758564144e-12, 6.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(0.0, 2047.6000000000013)
    .lineTo(0.0, 0.0)
    .lineTo(60.0, 0.0)
    .lineTo(60.0, 2047.6000000000013)
    .lineTo(0.0, 2047.6000000000013)
    .close().val())

extrusion_vector = (0.0, 0.0, -6.00000000000156)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
