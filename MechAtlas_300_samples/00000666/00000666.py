import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 0.0), xDir=(0.0, 1.0, 0.0), normal=(-1.0, 0.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(10.5, -5.0)
    .lineTo(11.0, -4.5)
    .lineTo(11.0, 4.5)
    .lineTo(10.5, 5.0)
    .lineTo(-14.5, 5.0)
    .lineTo(-15.0, 4.5)
    .lineTo(-15.0, -4.5)
    .lineTo(-14.5, -5.0)
    .lineTo(10.5, -5.0)
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(-9.0, -2.25)
    .threePointArc((-11.25, 0.0), (-9.0, 2.25))
    .threePointArc((-6.75, 0.0), (-9.0, -2.25))
    .close().val())

opening_2 = (cq.Workplane(profile_plane).moveTo(5.0, -2.2499999999999964)
    .threePointArc((2.75, 0.0), (5.0, 2.2500000000000036))
    .threePointArc((7.25, 0.0), (5.0, -2.2499999999999964))
    .close().val())

extrusion_vector = (4.8, 0.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
