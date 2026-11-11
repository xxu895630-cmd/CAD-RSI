import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 2.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-15.0, 9.0)
    .lineTo(-15.0, -9.0)
    .lineTo(-14.0, -10.0)
    .lineTo(14.0, -10.0)
    .lineTo(15.0, -9.0)
    .lineTo(15.0, 9.0)
    .lineTo(14.0, 10.0)
    .lineTo(-14.0, 10.0)
    .lineTo(-15.0, 9.0)
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(4.0, 1.2499999999999865)
    .threePointArc((5.249999999999988, 0.0), (4.0, -1.249999999999988))
    .threePointArc((2.750000000000013, 0.0), (4.0, 1.2499999999999862))
    .close().val())

opening_2 = (cq.Workplane(profile_plane).moveTo(-4.0, 1.2499999999999865)
    .threePointArc((-2.750000000000013, 0.0), (-4.0, -1.249999999999988))
    .threePointArc((-5.249999999999988, 0.0), (-4.0, 1.2499999999999862))
    .close().val())

opening_3 = (cq.Workplane(profile_plane).moveTo(-11.500000000000005, -4.750000000000018)
    .threePointArc((-10.250000000000018, -6.0), (-11.500000000000005, -7.249999999999993))
    .threePointArc((-12.749999999999993, -6.0), (-11.500000000000005, -4.750000000000018))
    .close().val())

opening_4 = (cq.Workplane(profile_plane).moveTo(11.500000000000005, 7.24999999999999)
    .threePointArc((12.749999999999993, 6.0), (11.500000000000005, 4.750000000000016))
    .threePointArc((10.250000000000018, 6.0), (11.500000000000005, 7.249999999999989))
    .close().val())

extrusion_vector = (0.0, -2.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2, opening_3, opening_4], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
