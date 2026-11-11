import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 4.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(0.0, 2.75)
    .threePointArc((-2.75, 0.0), (0.0, -2.75))
    .threePointArc((2.75, 0.0), (0.0, 2.75))
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(0.0, -1.5000000000000002)
    .threePointArc((-1.5000000000000002, 0.0), (0.0, 1.5000000000000002))
    .threePointArc((1.5000000000000002, 0.0), (0.0, -1.5000000000000002))
    .close().val())

extrusion_vector = (0.0, -4.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
