import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 1.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(24.0, 10.0)
    .lineTo(-24.0, 10.0)
    .threePointArc((-25.414213562373096, 9.4142135623731), (-26.0, 8.0))
    .lineTo(-26.0, -8.0)
    .threePointArc((-25.414213562373096, -9.414213562373096), (-24.0, -10.0))
    .lineTo(24.0, -10.0)
    .threePointArc((25.41421356237308, -9.414213562373089), (26.0, -8.0))
    .lineTo(26.0, 8.0)
    .threePointArc((25.41421356237308, 9.414213562373105), (24.0, 10.0))
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(-16.25000000000001, 0.0)
    .threePointArc((-19.0, -2.749999999999999), (-21.75000000000001, 0.0))
    .threePointArc((-19.0, 2.749999999999999), (-16.25000000000001, 0.0))
    .close().val())

opening_2 = (cq.Workplane(profile_plane).moveTo(20.24999999999999, 6.750000000000002)
    .threePointArc((18.49999999999999, 5.0), (16.74999999999999, 6.750000000000002))
    .threePointArc((18.49999999999999, 8.500000000000004), (20.24999999999999, 6.750000000000002))
    .close().val())

opening_3 = (cq.Workplane(profile_plane).moveTo(20.24999999999999, -6.749999999999998)
    .threePointArc((18.49999999999999, -8.5), (16.74999999999999, -6.749999999999998))
    .threePointArc((18.49999999999999, -5.0), (20.24999999999999, -6.749999999999998))
    .close().val())

extrusion_vector = (0.0, 0.0, -1.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2, opening_3], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
