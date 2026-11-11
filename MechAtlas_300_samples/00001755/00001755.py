import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 2.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(0.0, 0.0)
    .lineTo(0.0, -65.0)
    .lineTo(74.0, -65.0)
    .lineTo(74.0, 0.0)
    .lineTo(0.0, 0.0)
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(11.74999999999968, -54.95764845803845)
    .threePointArc((14.49999999999968, -52.20764845803845), (17.24999999999968, -54.95764845803845))
    .threePointArc((14.49999999999968, -57.70764845803845), (11.74999999999968, -54.95764845803845))
    .close().val())

opening_2 = (cq.Workplane(profile_plane).moveTo(56.749999999999666, -54.95764845803845)
    .threePointArc((59.499999999999666, -52.207648458038456), (62.24999999999966, -54.95764845803845))
    .threePointArc((59.499999999999666, -57.70764845803844), (56.74999999999967, -54.95764845803845))
    .close().val())

opening_3 = (cq.Workplane(profile_plane).moveTo(62.0, -16.857648458034053)
    .threePointArc((59.49999999999981, -19.35764845803405), (57.0, -16.857648458034053))
    .threePointArc((59.49999999999981, -14.357648458034058), (62.0, -16.857648458034053))
    .close().val())

opening_4 = (cq.Workplane(profile_plane).moveTo(17.0, -16.857648458034053)
    .threePointArc((14.499999999999815, -19.357648458034053), (12.0, -16.857648458034053))
    .threePointArc((14.499999999999815, -14.357648458034054), (17.0, -16.857648458034053))
    .close().val())

extrusion_vector = (0.0, 0.0, -2.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2, opening_3, opening_4], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
