import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 5.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-25.0, 0.0)
    .threePointArc((0.0, -25.0), (25.0, 0.0))
    .threePointArc((0.0, 25.0), (-25.0, 0.0))
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(17.25, 0.0)
    .threePointArc((19.5, 2.2499999999999316), (21.75, 0.0))
    .threePointArc((19.5, -2.2500000000000675), (17.25, 0.0))
    .close().val())

opening_2 = (cq.Workplane(profile_plane).moveTo(-2.2499999999999996, -19.5)
    .threePointArc((0.0, -17.25), (2.2499999999999996, -19.5))
    .threePointArc((0.0, -21.75), (-2.2499999999999996, -19.5))
    .close().val())

opening_3 = (cq.Workplane(profile_plane).moveTo(-21.75, 0.0)
    .threePointArc((-19.5, 2.250000000000204), (-17.25, 0.0))
    .threePointArc((-19.5, -2.2499999999997953), (-21.75, 0.0))
    .close().val())

opening_4 = (cq.Workplane(profile_plane).moveTo(-2.2499999999999996, 19.5)
    .threePointArc((0.0, 21.75), (2.2499999999999996, 19.5))
    .threePointArc((0.0, 17.25), (-2.2499999999999996, 19.5))
    .close().val())

extrusion_vector = (0.0, 0.0, -5.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2, opening_3, opening_4], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
