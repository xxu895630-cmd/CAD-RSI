import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, -1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(5.75, 0.0)
    .threePointArc((0.0, 5.75), (-5.75, 0.0))
    .threePointArc((0.0, -5.75), (5.75, 0.0))
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(1.5000000000000013, 2.2499999999999996)
    .threePointArc((3.75, 0.0), (1.5000000000000009, -2.25))
    .lineTo(-1.5000000000000007, -2.2499999999999996)
    .threePointArc((-3.0909902576697323, -1.5909902576697317), (-3.75, 0.0))
    .threePointArc((-3.0909902576697323, 1.5909902576697323), (-1.5000000000000007, 2.2500000000000004))
    .lineTo(1.5000000000000013, 2.2499999999999996)
    .close().val())

extrusion_vector = (0.0, 0.0, 3.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
