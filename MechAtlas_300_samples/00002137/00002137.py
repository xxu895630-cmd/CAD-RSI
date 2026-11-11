import cadquery as cq

profile_plane = cq.Plane(origin=(-18.299699999999998, -52.900000000000006, 158.31509874728948), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, -1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(56.0, 12.0)
    .threePointArc((53.65685424949237, 17.656854249492383), (48.0, 20.0))
    .lineTo(-10.500000000000004, 20.0)
    .threePointArc((-16.156854249492387, 17.656854249492383), (-18.500000000000004, 12.0))
    .lineTo(-18.499999999999996, -120.0)
    .threePointArc((-16.156854249492387, -125.6568542494924), (-10.500000000000004, -128.0))
    .lineTo(48.0, -128.0)
    .threePointArc((53.65685424949238, -125.6568542494924), (56.0, -120.0))
    .lineTo(56.0, 12.0)
    .close().val())

extrusion_vector = (0.0, 0.0, 3.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
