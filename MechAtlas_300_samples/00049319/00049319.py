import cadquery as cq

profile_plane = cq.Plane(origin=(-57.5, -12.5, 15.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, -1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(114.0, 0.0)
    .lineTo(1.0, 0.0)
    .lineTo(0.0, -1.0)
    .lineTo(0.0, -14.0)
    .lineTo(1.0, -15.0)
    .lineTo(114.0, -15.0)
    .lineTo(115.0, -14.0)
    .lineTo(115.0, -1.0)
    .lineTo(114.0, 0.0)
    .close().val())

extrusion_vector = (0.0, 25.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(5.0, 7.0, cq.Vector(-24.499999999999993, -4.500000000000001, 7.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(5.0, 7.0, cq.Vector(27.500000000000004, -4.5, 7.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(4.0, 6.0, cq.Vector(-47.5, 6.500000000000001, 7.5), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(2.2499999999999987, 19.0, cq.Vector(-47.5, -12.5, 7.5), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(4.0, 6.0, cq.Vector(0.0, 6.500000000000001, 7.5), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCylinder(2.249999999999997, 19.0, cq.Vector(0.0, -12.5, 7.5), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_6)

cutting_tool_7 = cq.Solid.makeCylinder(4.0, 6.0, cq.Vector(47.5, 6.500000000000001, 7.5), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_7)

cutting_tool_8 = cq.Solid.makeCylinder(2.2499999999999987, 19.0, cq.Vector(47.5, -12.5, 7.5), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_8)

cutting_tool_9 = cq.Solid.makeCylinder(2.499999999999995, 8.0, cq.Vector(27.500000000000004, -4.5, 7.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_9)

cutting_tool_10 = cq.Solid.makeCylinder(2.499999999999995, 8.0, cq.Vector(-24.499999999999993, -4.500000000000001, 7.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_10)

result = part
