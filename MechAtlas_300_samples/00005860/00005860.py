import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, -1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(29.5, 31.500000000000007)
    .lineTo(-29.5, 31.500000000000007)
    .lineTo(-32.499999999999986, 28.500000000000007)
    .lineTo(-32.5, -28.49999999999999)
    .lineTo(-29.499999999999986, -31.499999999999993)
    .lineTo(29.5, -31.499999999999993)
    .lineTo(32.5, -28.499999999999993)
    .lineTo(32.500000000000014, 28.500000000000007)
    .lineTo(29.5, 31.500000000000007)
    .close().val())

extrusion_vector = (0.0, 7.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(1.6499999999999986, 7.0, cq.Vector(-24.7485, 0.0, -24.748974680782236), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(1.6499999999999986, 7.0, cq.Vector(24.7485, 0.0, -24.748974680782236), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(1.6499999999999986, 7.0, cq.Vector(24.7485, 0.0, 24.748974680782236), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(1.6499999999999986, 7.0, cq.Vector(-24.7485, 0.0, 24.748974680782236), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(4.0, 4.4, cq.Vector(-25.98076211353316, 2.5999999999999996, -15.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCylinder(2.2499999999999987, 2.5999999999999988, cq.Vector(-25.98076211353316, 0.0, -15.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_6)

cutting_tool_7 = cq.Solid.makeCylinder(4.0, 4.4, cq.Vector(25.98076211353316, 2.5999999999999996, -15.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_7)

cutting_tool_8 = cq.Solid.makeCylinder(2.2499999999999987, 2.5999999999999988, cq.Vector(25.98076211353316, 0.0, -15.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_8)

cutting_tool_9 = cq.Solid.makeCylinder(4.0, 4.4, cq.Vector(25.98076211353316, 2.5999999999999996, 15.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_9)

cutting_tool_10 = cq.Solid.makeCylinder(2.2499999999999987, 2.5999999999999988, cq.Vector(25.98076211353316, 0.0, 15.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_10)

cutting_tool_11 = cq.Solid.makeCylinder(4.0, 4.4, cq.Vector(-25.98076211353316, 2.5999999999999996, 15.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_11)

cutting_tool_12 = cq.Solid.makeCylinder(2.2499999999999987, 2.5999999999999988, cq.Vector(-25.98076211353316, 0.0, 15.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_12)

cutting_tool_13 = cq.Solid.makeCylinder(25.0, 7.0, cq.Vector(0.0, 0.0, 0.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_13)

result = part
