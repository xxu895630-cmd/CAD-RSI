import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, -1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(20.0, -8.0)
    .lineTo(20.0, 8.0)
    .threePointArc((19.414213562373103, 9.414213562373096), (18.0, 10.0))
    .lineTo(-18.0, 10.0)
    .threePointArc((-19.4142135623731, 9.4142135623731), (-20.0, 8.0))
    .lineTo(-20.0, -8.0)
    .threePointArc((-19.4142135623731, -9.414213562373096), (-18.0, -10.0))
    .lineTo(18.0, -10.0)
    .threePointArc((19.4142135623731, -9.414213562373092), (20.0, -8.0))
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(-12.6, 0.0)
    .threePointArc((-15.0, -2.3999999999999995), (-17.4, 0.0))
    .threePointArc((-15.0, 2.3999999999999995), (-12.600000000000001, 0.0))
    .close().val())

opening_2 = (cq.Workplane(profile_plane).moveTo(17.4, 0.0)
    .threePointArc((15.0, -2.3999999999999995), (12.600000000000001, 0.0))
    .threePointArc((15.0, 2.3999999999999995), (17.4, 0.0))
    .close().val())

extrusion_vector = (0.0, 0.0, 3.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
