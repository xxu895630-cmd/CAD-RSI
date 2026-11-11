import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 5.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-50.0, 58.0)
    .lineTo(-50.0, -58.0)
    .lineTo(-48.0, -60.0)
    .lineTo(48.0, -60.0)
    .lineTo(50.0, -58.0)
    .lineTo(50.0, 58.0)
    .lineTo(48.0, 60.0)
    .lineTo(-48.0, 60.0)
    .lineTo(-50.0, 58.0)
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(-20.026800000000044, 48.0)
    .threePointArc((-16.776800000000044, 51.249999999999915), (-13.526800000000044, 48.0))
    .threePointArc((-16.776800000000044, 44.749999999999915), (-20.026800000000044, 48.0))
    .close().val())

opening_2 = (cq.Workplane(profile_plane).moveTo(-38.52680000000003, 48.0)
    .threePointArc((-35.27680000000003, 51.24999999999991), (-32.02680000000004, 48.0))
    .threePointArc((-35.27680000000003, 44.74999999999992), (-38.52680000000002, 48.0))
    .close().val())

opening_3 = (cq.Workplane(profile_plane).moveTo(38.34999999999996, -52.0)
    .threePointArc((40.0, -50.34999999999995), (41.649999999999956, -52.0))
    .threePointArc((40.0, -53.64999999999995), (38.34999999999996, -52.0))
    .close().val())

opening_4 = (cq.Workplane(profile_plane).moveTo(-41.65000000000004, -52.0)
    .threePointArc((-40.0, -50.34999999999998), (-38.350000000000044, -52.0))
    .threePointArc((-40.0, -53.64999999999998), (-41.65000000000004, -52.0))
    .close().val())

opening_5 = (cq.Workplane(profile_plane).moveTo(38.34999999999994, 23.0)
    .threePointArc((40.0, 24.65000000000005), (41.649999999999935, 23.0))
    .threePointArc((40.0, 21.35000000000005), (38.34999999999994, 23.0))
    .close().val())

opening_6 = (cq.Workplane(profile_plane).moveTo(-41.65000000000006, 23.0)
    .threePointArc((-40.0, 24.65000000000002), (-38.350000000000065, 23.0))
    .threePointArc((-40.0, 21.350000000000023), (-41.65000000000006, 23.0))
    .close().val())

extrusion_vector = (0.0, 0.0, -5.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2, opening_3, opening_4, opening_5, opening_6], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
