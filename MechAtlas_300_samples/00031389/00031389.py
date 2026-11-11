import cadquery as cq

profile_plane = cq.Plane(origin=(-35.0, 10.0, 20.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(70.0, 0.0)
    .lineTo(68.0, 0.0)
    .lineTo(68.0, -2.0)
    .lineTo(58.0, -2.0)
    .lineTo(58.0, 0.0)
    .lineTo(0.0, 0.0)
    .lineTo(0.0, -10.0)
    .lineTo(70.0, -10.0)
    .lineTo(70.0, 0.0)
    .close().val())

extrusion_vector = (0.0, 0.0, -40.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(4.74999999999999, 5.499999999999998, cq.Vector(28.0, 5.499999999999998, -12.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(2.7500000000000093, 2.5000000000000018, cq.Vector(28.0, 8.0, -12.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(4.74999999999999, 5.499999999999998, cq.Vector(28.0, 5.499999999999998, 12.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(2.7500000000000093, 2.5000000000000018, cq.Vector(28.0, 8.0, 12.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(9.999999776482568, 10.0, cq.Vector(-15.300000000000011, 0.0, -0.1500000000000106), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCylinder(2.099999999999989, 10.0, cq.Vector(-29.442135623731005, 0.0, 13.992135623730912), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_6)

cutting_tool_7 = cq.Solid.makeCylinder(2.099999999999987, 10.0, cq.Vector(-1.1578643762690157, 0.0, -14.292135623730918), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_7)

result = part
