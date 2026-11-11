import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 1.0, 2.5), xDir=(1.0, 0.0, 0.0), normal=(0.0, 1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-2.750000000000001, -7.5)
    .threePointArc((0.0, -10.25), (2.75, -7.5))
    .lineTo(2.7499999999999982, 12.5)
    .threePointArc((0.0, 15.25), (-2.75, 12.5))
    .lineTo(-2.7500000000000004, -7.5)
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(1.699999999999999, 12.5)
    .lineTo(1.7000000000000006, -7.5)
    .threePointArc((0.0, -9.2), (-1.7, -7.5))
    .lineTo(-1.7000000000000024, 12.5)
    .threePointArc((0.0, 14.2), (1.7, 12.5))
    .close().val())

extrusion_vector = (0.0, -1.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
