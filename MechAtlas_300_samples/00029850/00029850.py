import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 12.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(31.50000000000002, -28.0)
    .lineTo(31.500000000000007, 28.0)
    .lineTo(29.500000000000007, 30.0)
    .lineTo(-29.499999999999986, 30.0)
    .lineTo(-31.5, 28.0)
    .lineTo(-31.499999999999986, -28.0)
    .lineTo(-29.499999999999986, -30.0)
    .lineTo(29.500000000000014, -30.0)
    .lineTo(31.500000000000025, -28.0)
    .close().val())

extrusion_vector = (0.0, -12.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(1.6499999999999917, 12.0, cq.Vector(26.500000000000096, 12.0, -13.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(1.6499999999999935, 12.0, cq.Vector(-26.499999999999893, 12.0, -13.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(14.0, 4.6, 9.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(2.2499999999999987, 7.4, cq.Vector(14.0, 12.0, 9.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(14.0, 4.6, -19.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCylinder(2.2499999999999987, 7.4, cq.Vector(14.0, 12.0, -19.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_6)

cutting_tool_7 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(-14.0, 4.6, -19.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_7)

cutting_tool_8 = cq.Solid.makeCylinder(2.2499999999999987, 7.4, cq.Vector(-14.0, 12.0, -19.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_8)

cutting_tool_9 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(-14.0, 4.6, 9.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_9)

cutting_tool_10 = cq.Solid.makeCylinder(2.2499999999999996, 7.4, cq.Vector(-14.0, 12.0, 9.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_10)

cutting_tool_11 = cq.Solid.makeCylinder(2.749999999999999, 12.0, cq.Vector(-25.0, 0.0, 22.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_11)

cutting_tool_12 = cq.Solid.makeCylinder(2.749999999999999, 12.0, cq.Vector(25.0, 0.0, 22.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_12)

cutting_tool_13 = cq.Solid.makeCylinder(14.0, 12.0, cq.Vector(0.0, 0.0, -5.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_13)

result = part
