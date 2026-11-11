import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 3.9), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-230.0, 0.0)
    .threePointArc((0.0, -230.0), (230.0, 0.0))
    .threePointArc((0.0, 230.0), (-230.0, 0.0))
    .close().val())

extrusion_vector = (0.0, 0.0, -3.9)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCone(2.7499999999999973, 5.6, 2.850000000000002, cq.Vector(0.0, 200.0, 2.850000000000002), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(2.7499999999999982, 1.0499999999999972, cq.Vector(0.0, 200.0, 3.899999999999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCone(2.75, 5.599999999999994, 2.8500000000000045, cq.Vector(-141.4213562373115, 141.42135623731437, 2.8500000000000045), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(2.7500000000000027, 1.0499999999999972, cq.Vector(-141.4213562373115, 141.42135623731437, 3.899999999999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCone(2.75, 5.599999999999994, 2.8500000000000045, cq.Vector(-200.00000000000688, 6.859964477545461e-12, 2.8500000000000045), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCylinder(2.7500000000000027, 1.0499999999999972, cq.Vector(-200.00000000000688, 6.859964477545461e-12, 3.899999999999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_6)

cutting_tool_7 = cq.Solid.makeCone(2.75, 5.599999999999994, 2.8500000000000045, cq.Vector(-141.42135623732122, -141.42135623730465, 2.8500000000000045), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_7)

cutting_tool_8 = cq.Solid.makeCylinder(2.7500000000000027, 1.0499999999999972, cq.Vector(-141.42135623732122, -141.42135623730465, 3.899999999999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_8)

cutting_tool_9 = cq.Solid.makeCone(2.7499999999999973, 5.6000000000000005, 2.8500000000000023, cq.Vector(-1.3719928955090922e-11, -200.0, 2.850000000000002), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_9)

cutting_tool_10 = cq.Solid.makeCylinder(2.7499999999999982, 1.0499999999999972, cq.Vector(-1.3719928955090922e-11, -200.0, 3.899999999999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_10)

cutting_tool_11 = cq.Solid.makeCone(2.75, 5.599999999999994, 2.8500000000000045, cq.Vector(141.4213562372978, -141.4213562373144, 2.8500000000000045), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_11)

cutting_tool_12 = cq.Solid.makeCylinder(2.7500000000000027, 1.0499999999999972, cq.Vector(141.4213562372978, -141.4213562373144, 3.899999999999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_12)

cutting_tool_13 = cq.Solid.makeCone(2.75, 5.599999999999994, 2.8500000000000045, cq.Vector(199.99999999999315, -6.884457413528408e-12, 2.8500000000000045), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_13)

cutting_tool_14 = cq.Solid.makeCylinder(2.7500000000000027, 1.0499999999999972, cq.Vector(199.99999999999315, -6.884457413528408e-12, 3.899999999999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_14)

cutting_tool_15 = cq.Solid.makeCone(2.75, 5.6000000000000005, 2.8500000000000107, cq.Vector(141.4213562373075, 141.42135623730465, 2.8500000000000045), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_15)

cutting_tool_16 = cq.Solid.makeCylinder(2.7500000000000027, 1.0499999999999972, cq.Vector(141.4213562373075, 141.42135623730465, 3.899999999999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_16)

cutting_tool_17 = cq.Solid.makeCylinder(190.0, 3.9, cq.Vector(0.0, 0.0, 3.9), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_17)

result = part
