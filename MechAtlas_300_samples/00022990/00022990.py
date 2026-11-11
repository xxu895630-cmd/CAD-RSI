import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, -1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(160.0, 0.0)
    .lineTo(10.0, 0.0)
    .lineTo(0.0, -10.0)
    .lineTo(0.0, -160.0)
    .lineTo(10.0, -170.0)
    .lineTo(160.0, -170.0)
    .lineTo(170.0, -160.0)
    .lineTo(170.0, -10.0)
    .lineTo(160.0, 0.0)
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(79.50000000000003, -150.0)
    .threePointArc((75.0, -154.50000000000003), (70.50000000000003, -150.0))
    .threePointArc((75.0, -145.50000000000003), (79.50000000000003, -150.0))
    .close().val())

opening_2 = (cq.Workplane(profile_plane).moveTo(159.50000000000003, -150.0)
    .threePointArc((155.0, -154.50000000000003), (150.50000000000003, -150.0))
    .threePointArc((155.0, -145.50000000000003), (159.50000000000003, -150.0))
    .close().val())

opening_3 = (cq.Workplane(profile_plane).moveTo(24.499999999999982, -95.0)
    .threePointArc((20.0, -99.49999999999999), (15.499999999999982, -95.0))
    .threePointArc((20.0, -90.49999999999999), (24.499999999999982, -95.0))
    .close().val())

opening_4 = (cq.Workplane(profile_plane).moveTo(24.49999999999999, -15.0)
    .threePointArc((20.0, -19.5), (15.49999999999999, -15.0))
    .threePointArc((20.0, -10.5), (24.49999999999999, -15.0))
    .close().val())

opening_5 = (cq.Workplane(profile_plane).moveTo(163.89999999999998, -72.5)
    .threePointArc((160.5, -75.89999999999999), (157.10000000000002, -72.5))
    .threePointArc((160.5, -69.10000000000001), (163.89999999999998, -72.5))
    .close().val())

opening_6 = (cq.Workplane(profile_plane).moveTo(100.9, -72.5)
    .threePointArc((97.5, -75.9), (94.1, -72.5))
    .threePointArc((97.5, -69.1), (100.9, -72.5))
    .close().val())

opening_7 = (cq.Workplane(profile_plane).moveTo(100.9, -9.5)
    .threePointArc((97.5, -12.9), (94.1, -9.5))
    .threePointArc((97.5, -6.1), (100.9, -9.5))
    .close().val())

opening_8 = (cq.Workplane(profile_plane).moveTo(163.89999999999998, -9.5)
    .threePointArc((160.5, -12.899999999999986), (157.10000000000002, -9.5))
    .threePointArc((160.5, -6.100000000000014), (163.89999999999998, -9.5))
    .close().val())

opening_9 = (cq.Workplane(profile_plane).moveTo(57.0, -120.0)
    .threePointArc((50.0, -127.0), (43.0, -120.0))
    .threePointArc((50.0, -113.0), (57.0, -120.0))
    .close().val())

extrusion_vector = (0.0, 0.0, 10.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2, opening_3, opening_4, opening_5, opening_6, opening_7, opening_8, opening_9], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
