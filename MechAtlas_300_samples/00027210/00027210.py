import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 10.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(152.50000000000003, -8.0)
    .lineTo(152.50000000000003, 2.475062189439541)
    .threePointArc((151.20726266775944, 5.830088793244263), (147.99751859510505, 7.450248140489483))
    .lineTo(122.499999999999, 10.0)
    .lineTo(-150.49999999999991, 10.0)
    .lineTo(-152.5, 8.0)
    .lineTo(-152.49999999999997, -8.0)
    .lineTo(-150.49999999999997, -10.0)
    .lineTo(150.49999999999997, -10.0)
    .lineTo(152.50000000000006, -8.0)
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(-6.0, 1.4999999999999991)
    .threePointArc((-2.49999999999996, 5.0), (1.0, 1.5000000000000002))
    .lineTo(1.0, -1.5)
    .threePointArc((-0.025126265847041918, -3.974873734152918), (-2.4999999999999605, -5.0))
    .threePointArc((-4.9748737341528795, -3.9748737341529177), (-6.0, -1.499999999999999))
    .lineTo(-6.0, 1.4999999999999991)
    .close().val())

opening_2 = (cq.Workplane(profile_plane).moveTo(104.0, 1.4999999999999991)
    .threePointArc((107.50000000000004, 5.0), (111.0, 1.5000000000000002))
    .lineTo(111.0, -1.5)
    .threePointArc((109.97487373415296, -3.974873734152918), (107.50000000000004, -5.0))
    .threePointArc((105.02512626584712, -3.9748737341529177), (104.0, -1.499999999999999))
    .lineTo(104.0, 1.4999999999999991)
    .close().val())

opening_3 = (cq.Workplane(profile_plane).moveTo(-116.0, 1.4999999999999991)
    .threePointArc((-112.49999999999996, 5.0), (-109.0, 1.5000000000000002))
    .lineTo(-109.0, -1.5)
    .threePointArc((-110.02512626584704, -3.974873734152918), (-112.49999999999996, -5.0))
    .threePointArc((-114.97487373415288, -3.9748737341529177), (-116.0, -1.499999999999999))
    .lineTo(-116.0, 1.4999999999999991)
    .close().val())

extrusion_vector = (0.0, -10.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2, opening_3], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
