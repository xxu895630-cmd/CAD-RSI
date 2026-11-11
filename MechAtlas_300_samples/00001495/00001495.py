import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 2.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(3.8999999999999995, -9.500000000000002)
    .lineTo(3.8999999999999995, 9.5)
    .lineTo(3.4000000000000004, 10.0)
    .lineTo(-3.4, 10.0)
    .lineTo(-3.9000000000000017, 9.499999999999998)
    .lineTo(-3.9000000000000004, -9.499999999999996)
    .lineTo(-3.399999999999998, -10.0)
    .lineTo(3.399999999999997, -10.0)
    .lineTo(3.8999999999999995, -9.500000000000002)
    .close().val())

extrusion_vector = (0.0, -2.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCone(1.3499999999999994, 2.75, 1.4000000000000006, cq.Vector(-0.8999999999999976, 1.4000000000000006, 6.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(1.3499999999999996, 0.5999999999999999, cq.Vector(-0.8999999999999976, 2.0, 6.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCone(1.3499999999999999, 2.750000000000001, 1.400000000000001, cq.Vector(-0.8999999999999976, 1.400000000000001, -6.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(1.3499999999999996, 0.5999999999999999, cq.Vector(-0.8999999999999976, 2.0, -6.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_4)

result = part
