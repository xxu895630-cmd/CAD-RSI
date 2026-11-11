import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, -1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(81.0, -12.5)
    .lineTo(81.0, 8.499999999999984)
    .lineTo(77.0, 12.499999999999986)
    .lineTo(-77.0, 12.5)
    .lineTo(-81.0, 8.499999999999957)
    .lineTo(-81.0, -12.5)
    .lineTo(81.0, -12.5)
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(3.0, -7.249999999999996)
    .threePointArc((0.7500000000000067, -5.0), (3.0, -2.750000000000003))
    .threePointArc((5.249999999999998, -5.0), (3.0, -7.249999999999995))
    .close().val())

opening_2 = (cq.Workplane(profile_plane).moveTo(-67.0, -7.249999999999996)
    .threePointArc((-69.25, -5.0), (-67.0, -2.750000000000003))
    .threePointArc((-64.75, -5.0), (-67.0, -7.249999999999995))
    .close().val())

opening_3 = (cq.Workplane(profile_plane).moveTo(73.0, -7.249999999999996)
    .threePointArc((70.75000000000001, -5.0), (73.0, -2.750000000000003))
    .threePointArc((75.25000000000001, -5.0), (73.0, -7.249999999999995))
    .close().val())

extrusion_vector = (0.0, 2.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2, opening_3], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
