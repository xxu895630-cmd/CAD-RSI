import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-10.0, 9.500000000000002)
    .lineTo(-10.0, -9.500000000000002)
    .threePointArc((-9.121320343559642, -11.621320343559644), (-7.0, -12.500000000000002))
    .lineTo(7.0, -12.5)
    .threePointArc((9.121320343559644, -11.621320343559645), (10.0, -9.500000000000002))
    .lineTo(10.0, 9.5)
    .threePointArc((9.121320343559642, 11.621320343559644), (7.0, 12.5))
    .lineTo(-7.0, 12.5)
    .threePointArc((-9.121320343559642, 11.621320343559644), (-10.0, 9.500000000000002))
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(5.0, 8.2)
    .threePointArc((6.699999999999998, 6.500000000000001), (5.0, 4.8000000000000025))
    .threePointArc((3.3000000000000016, 6.500000000000001), (5.0, 8.2))
    .close().val())

opening_2 = (cq.Workplane(profile_plane).moveTo(5.0, -4.8000000000000025)
    .threePointArc((6.699999999999997, -6.500000000000001), (5.0, -8.2))
    .threePointArc((3.3, -6.500000000000001), (5.0, -4.8000000000000025))
    .close().val())

extrusion_vector = (0.0, -1.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
