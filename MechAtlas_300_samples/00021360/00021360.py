import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, -1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-195.0, 235.0)
    .lineTo(-195.0, -235.0)
    .threePointArc((-192.0710678118655, -242.07106781186548), (-185.0, -245.0))
    .lineTo(185.0, -245.0)
    .threePointArc((192.07106781186545, -242.07106781186548), (195.0, -235.0))
    .lineTo(195.0, 235.0)
    .threePointArc((192.07106781186548, 242.0710678118655), (185.0, 245.0))
    .lineTo(-185.0, 245.0)
    .threePointArc((-192.07106781186542, 242.07106781186548), (-195.0, 235.0))
    .close().val())

extrusion_vector = (0.0, 15.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(7.500000000000007, 9.0, cq.Vector(172.50000000000003, 6.0, 150.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(4.5000000000000036, 6.0, cq.Vector(172.50000000000003, 0.0, 150.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(7.500000000000007, 9.0, cq.Vector(-172.50000000000003, 6.0, -150.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(4.5000000000000036, 6.0, cq.Vector(-172.50000000000003, 0.0, -150.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(7.500000000000007, 9.0, cq.Vector(-172.50000000000003, 6.0, 150.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCylinder(4.5000000000000036, 6.0, cq.Vector(-172.50000000000003, 0.0, 150.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_6)

cutting_tool_7 = cq.Solid.makeCylinder(7.500000000000007, 9.0, cq.Vector(172.50000000000003, 6.0, -150.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_7)

cutting_tool_8 = cq.Solid.makeCylinder(4.5000000000000036, 6.0, cq.Vector(172.50000000000003, 0.0, -150.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_8)

cutting_tool_9 = cq.Solid.makeCylinder(7.499999999999979, 9.0, cq.Vector(-100.0, 6.0, -222.5), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_9)

cutting_tool_10 = cq.Solid.makeCylinder(4.5000000000000036, 6.0, cq.Vector(-100.0, 0.0, -222.5), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_10)

cutting_tool_11 = cq.Solid.makeCylinder(7.500000000000007, 9.0, cq.Vector(100.0, 6.0, 222.49999999999997), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_11)

cutting_tool_12 = cq.Solid.makeCylinder(4.5000000000000036, 6.0, cq.Vector(100.0, 0.0, 222.49999999999997), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_12)

cutting_tool_13 = cq.Solid.makeCylinder(7.499999999999979, 9.0, cq.Vector(100.0, 6.0, -222.5), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_13)

cutting_tool_14 = cq.Solid.makeCylinder(4.5000000000000036, 6.0, cq.Vector(100.0, 0.0, -222.5), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_14)

cutting_tool_15 = cq.Solid.makeCylinder(7.500000000000007, 9.0, cq.Vector(-100.0, 6.0, 222.49999999999997), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_15)

cutting_tool_16 = cq.Solid.makeCylinder(4.5000000000000036, 6.0, cq.Vector(-100.0, 0.0, 222.49999999999997), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_16)

result = part
