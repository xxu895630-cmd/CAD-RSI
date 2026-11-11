import cadquery as cq

profile_plane = cq.Plane(origin=(177.50000000000003, -17.0, 6.4), xDir=(0.0, 1.0, 0.0), normal=(1.0, 0.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(9.5, -4.4)
    .lineTo(24.5, -4.4)
    .lineTo(24.5, -6.4)
    .lineTo(34.0, -6.4)
    .lineTo(34.0, 0.0)
    .lineTo(0.0, 0.0)
    .lineTo(0.0, -6.4)
    .lineTo(9.5, -6.4)
    .lineTo(9.5, -4.4)
    .close().val())

extrusion_vector = (-355.0, 0.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(2.0, 4.4, cq.Vector(-63.49999999999996, 0.0, 2.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(2.0, 4.4, cq.Vector(116.50000000000003, 0.0, 2.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(1.6499999999999986, 6.4, cq.Vector(-78.0, 10.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(1.6499999999999986, 6.4, cq.Vector(102.0, 10.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(1.6499999999999986, 6.4, cq.Vector(102.0, -7.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCylinder(1.6499999999999986, 6.4, cq.Vector(-78.0, -7.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_6)

cutting_tool_7 = cq.Solid.makeCylinder(1.250000000000001, 4.4, cq.Vector(-90.0, 0.0, 2.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_7)

cutting_tool_8 = cq.Solid.makeCylinder(1.250000000000001, 4.4, cq.Vector(-150.0, 0.0, 2.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_8)

cutting_tool_9 = cq.Solid.makeCylinder(2.0, 6.4, cq.Vector(-142.49999999999997, 12.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_9)

cutting_tool_10 = cq.Solid.makeCylinder(2.0, 6.4, cq.Vector(-104.49999999999996, 12.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_10)

cutting_tool_11 = cq.Solid.makeCylinder(2.0, 6.4, cq.Vector(-104.49999999999996, -12.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_11)

cutting_tool_12 = cq.Solid.makeCylinder(2.0, 6.4, cq.Vector(-142.49999999999997, -12.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_12)

cutting_tool_13 = cq.Solid.makeCylinder(2.7500000000000027, 6.4, cq.Vector(-133.49999999999994, 12.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_13)

cutting_tool_14 = cq.Solid.makeCylinder(2.7500000000000027, 6.4, cq.Vector(-133.49999999999994, -12.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_14)

cutting_tool_15 = cq.Solid.makeCylinder(2.7500000000000027, 6.4, cq.Vector(-113.49999999999996, 12.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_15)

cutting_tool_16 = cq.Solid.makeCylinder(2.7500000000000027, 6.4, cq.Vector(-113.49999999999994, -12.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_16)

cutting_tool_17 = cq.Solid.makeCylinder(2.0, 4.4, cq.Vector(-170.0, 0.0, 2.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_17)

cutting_tool_18 = cq.Solid.makeCylinder(2.0, 4.4, cq.Vector(170.0, 0.0, 2.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_18)

cutting_tool_19 = cq.Solid.makeCylinder(1.6499999999999848, 6.400000000000002, cq.Vector(-170.0, 12.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_19)

cutting_tool_20 = cq.Solid.makeCylinder(1.6499999999999848, 6.400000000000002, cq.Vector(-170.0, -12.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_20)

cutting_tool_21 = cq.Solid.makeCylinder(1.6499999999999848, 6.400000000000002, cq.Vector(170.0, 12.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_21)

cutting_tool_22 = cq.Solid.makeCylinder(1.6499999999999848, 6.400000000000002, cq.Vector(170.0, -12.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_22)

cutting_tool_23 = cq.Solid.makeCylinder(1.250000000000001, 4.4, cq.Vector(-30.0, 0.0, 2.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_23)

cutting_tool_24 = cq.Solid.makeCylinder(1.250000000000001, 4.4, cq.Vector(30.0, 0.0, 2.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_24)

cutting_tool_25 = cq.Solid.makeCylinder(1.250000000000001, 4.4, cq.Vector(90.0, 0.0, 2.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_25)

cutting_tool_26 = cq.Solid.makeCylinder(1.250000000000001, 4.4, cq.Vector(150.0, 0.0, 2.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_26)

cutting_tool_27 = cq.Solid.makeCylinder(1.6499999999999986, 4.4, cq.Vector(-78.0, -7.0, 2.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_27)

cutting_tool_28 = cq.Solid.makeCylinder(1.6499999999999986, 4.4, cq.Vector(102.0, -7.0, 2.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_28)

result = part
