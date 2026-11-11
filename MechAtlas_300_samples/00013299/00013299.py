import cadquery as cq

profile_plane = cq.Plane(origin=(5.0, 0.0, 2.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(0.0, -3.4999999999999996)
    .threePointArc((3.5, 0.0), (0.0, 3.5000000000000004))
    .lineTo(-10.0, 3.4999999999999964)
    .threePointArc((-12.474873734152917, 2.474873734152912), (-13.5, 0.0))
    .threePointArc((-12.474873734152917, -2.474873734152919), (-10.0, -3.5000000000000027))
    .lineTo(0.0, -3.4999999999999996)
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(-11.7, 0.0)
    .threePointArc((-10.0, 1.6999999999999964), (-8.3, 0.0))
    .threePointArc((-10.0, -1.7000000000000022), (-11.7, 0.0))
    .close().val())

opening_2 = (cq.Workplane(profile_plane).moveTo(-1.6999999999999993, 0.0)
    .threePointArc((0.0, 1.6999999999999993), (1.6999999999999993, 0.0))
    .threePointArc((0.0, -1.6999999999999993), (-1.6999999999999993, 0.0))
    .close().val())

extrusion_vector = (0.0, 0.0, -2.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
