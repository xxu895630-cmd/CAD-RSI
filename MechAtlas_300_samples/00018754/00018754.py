import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 6.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-13.0, 17.500000000000007)
    .lineTo(-13.0, -17.499999999999996)
    .lineTo(-12.499999999999998, -18.0)
    .lineTo(12.500000000000007, -18.0)
    .lineTo(13.0, -17.500000000000007)
    .lineTo(13.0, 17.49999999999999)
    .lineTo(12.499999999999977, 18.0)
    .lineTo(-12.500000000000009, 18.0)
    .lineTo(-13.0, 17.500000000000007)
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(8.5, 11.4)
    .threePointArc((6.399999999999999, 13.500000000000002), (8.5, 15.600000000000003))
    .threePointArc((10.600000000000001, 13.500000000000002), (8.5, 11.4))
    .close().val())

opening_2 = (cq.Workplane(profile_plane).moveTo(8.499999999999996, -15.6)
    .threePointArc((6.399999999999995, -13.499999999999998), (8.499999999999996, -11.399999999999997))
    .threePointArc((10.599999999999998, -13.499999999999998), (8.499999999999996, -15.6))
    .close().val())

opening_3 = (cq.Workplane(profile_plane).moveTo(-6.0, 4.500000000000005)
    .threePointArc((-8.5, 7.0), (-6.0, 9.5))
    .threePointArc((-3.5000000000000058, 7.0), (-6.0, 4.500000000000005))
    .close().val())

opening_4 = (cq.Workplane(profile_plane).moveTo(-6.0, -6.499999999999992)
    .threePointArc((-8.5, -4.0), (-6.0, -1.4999999999999978))
    .threePointArc((-3.5000000000000058, -4.0), (-6.0, -6.499999999999991))
    .close().val())

extrusion_vector = (0.0, -6.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2, opening_3, opening_4], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
