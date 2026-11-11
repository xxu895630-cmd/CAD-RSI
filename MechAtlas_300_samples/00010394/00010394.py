import cadquery as cq

profile_plane = cq.Plane(origin=(-30.0, 1.0, -25.500000000000004), xDir=(1.0, 0.0, 0.0), normal=(0.0, 1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(0.0, 2.0)
    .threePointArc((-1.4142135623730994, 1.4142135623730923), (-2.0, 0.0))
    .lineTo(-2.0, -51.0)
    .threePointArc((-1.414213562373103, -52.4142135623731), (0.0, -53.0))
    .lineTo(60.0, -53.0)
    .threePointArc((61.41421356237309, -52.4142135623731), (62.0, -51.0))
    .lineTo(62.0, 0.0)
    .threePointArc((61.41421356237309, 1.4142135623730923), (60.0, 2.0))
    .lineTo(0.0, 2.0)
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(55.0, -48.0)
    .lineTo(5.0, -48.0)
    .threePointArc((3.5857864376269006, -47.41421356237309), (3.0, -46.0))
    .lineTo(3.0, -5.0)
    .threePointArc((3.5857864376268935, -3.5857864376269077), (5.0, -3.0))
    .lineTo(55.0, -3.0)
    .threePointArc((56.41421356237309, -3.585786437626915), (57.0, -5.0))
    .lineTo(57.0, -46.0)
    .threePointArc((56.41421356237309, -47.41421356237309), (55.0, -48.0))
    .close().val())

extrusion_vector = (0.0, -1.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
