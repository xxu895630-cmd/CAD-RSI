import cadquery as cq

stock_size = (30.0, 7.0, 6.0)

stock_origin = (-15.0, -3.500000000000006, 0.0)

part = cq.Workplane("XY").box(*stock_size, centered=(False, False, False)).translate(stock_origin)

part = part.edges().chamfer(0.2999999999999994)

cutting_tool_1 = cq.Solid.makeCylinder(2.5000000000000124, 2.0, cq.Vector(11.0, 1.4999999999999982, 3.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(1.2500000000000133, 5.0, cq.Vector(11.0, -3.500000000000006, 3.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(2.5000000000000124, 2.0, cq.Vector(-11.0, 1.4999999999999982, 3.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(1.2500000000000133, 5.0, cq.Vector(-11.0, -3.500000000000006, 3.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(3.0, 3.3999999999999995, cq.Vector(-4.0, 0.0, 2.6000000000000005), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCylinder(1.7000000000000053, 2.6, cq.Vector(-4.0, 0.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_6)

cutting_tool_7 = cq.Solid.makeCylinder(3.0, 3.3999999999999995, cq.Vector(4.0, 0.0, 2.6000000000000005), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_7)

cutting_tool_8 = cq.Solid.makeCylinder(1.7000000000000053, 2.6, cq.Vector(4.0, 0.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_8)

result = part
