import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, -1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(0.0, 5.0)
    .threePointArc((-5.0, 0.0), (0.0, -5.0))
    .threePointArc((5.0, 0.0), (0.0, 5.0))
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(0.0, 3.499999999999994)
    .threePointArc((3.499999999999994, 0.0), (0.0, -3.499999999999994))
    .threePointArc((-3.499999999999994, 0.0), (0.0, 3.499999999999994))
    .close().val())

extrusion_vector = (0.0, 30.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
