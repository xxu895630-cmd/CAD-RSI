import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 12.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(175.0, -77.0)
    .lineTo(175.0, -60.0)
    .lineTo(172.0, -57.0)
    .lineTo(125.0, -57.0)
    .threePointArc((117.92893218813461, -54.07106781186549), (115.0, -47.0))
    .lineTo(115.0, 47.0)
    .threePointArc((117.9289321881346, 54.07106781186548), (125.0, 57.0))
    .lineTo(172.0, 57.0)
    .lineTo(175.0, 60.0)
    .lineTo(175.0, 77.0)
    .lineTo(172.0, 80.0)
    .lineTo(-172.0, 80.0)
    .lineTo(-175.0, 77.0)
    .lineTo(-175.0, -77.0)
    .lineTo(-172.0, -80.0)
    .lineTo(172.0, -80.0)
    .lineTo(175.0, -77.0)
    .close().val())

extrusion_vector = (0.0, 0.0, -12.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(2.500000000000002, 12.0, cq.Vector(122.49999999999999, 66.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(2.500000000000002, 12.0, cq.Vector(122.49999999999999, -66.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(2.499999999999995, 12.0, cq.Vector(37.499999999999964, 66.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(2.499999999999995, 12.0, cq.Vector(37.49999999999998, -66.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(2.499999999999995, 12.0, cq.Vector(-47.50000000000003, 66.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCylinder(2.499999999999995, 12.0, cq.Vector(-47.50000000000003, -66.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_6)

cutting_tool_7 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(58.908922128244065, -75.49999999995855, 4.6), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_7)

cutting_tool_8 = cq.Solid.makeCylinder(2.149999999999999, 7.4, cq.Vector(58.908922128244065, -75.49999999995855, 12.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_8)

cutting_tool_9 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(58.90892212824407, -49.49999999995855, 4.6), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_9)

cutting_tool_10 = cq.Solid.makeCylinder(2.149999999999999, 7.4, cq.Vector(58.90892212824407, -49.49999999995855, 12.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_10)

cutting_tool_11 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(32.908922128244065, -75.49999999995855, 4.6), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_11)

cutting_tool_12 = cq.Solid.makeCylinder(2.149999999999999, 7.4, cq.Vector(32.908922128244065, -75.49999999995855, 12.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_12)

cutting_tool_13 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(32.90892212824407, -49.49999999995854, 4.6), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_13)

cutting_tool_14 = cq.Solid.makeCylinder(2.149999999999999, 7.4, cq.Vector(32.90892212824407, -49.49999999995854, 12.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_14)

cutting_tool_15 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(-29.69107787175592, -75.49999999995853, 4.6), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_15)

cutting_tool_16 = cq.Solid.makeCylinder(2.149999999999999, 7.4, cq.Vector(-29.69107787175592, -75.49999999995853, 12.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_16)

cutting_tool_17 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(-29.691077871755915, -49.499999999958526, 4.6), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_17)

cutting_tool_18 = cq.Solid.makeCylinder(2.149999999999999, 7.4, cq.Vector(-29.691077871755915, -49.499999999958526, 12.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_18)

cutting_tool_19 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(-55.69107787175592, -75.49999999995852, 4.6), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_19)

cutting_tool_20 = cq.Solid.makeCylinder(2.149999999999999, 7.4, cq.Vector(-55.69107787175592, -75.49999999995852, 12.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_20)

cutting_tool_21 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(-55.691077871755915, -49.49999999995852, 4.6), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_21)

cutting_tool_22 = cq.Solid.makeCylinder(2.149999999999999, 7.4, cq.Vector(-55.691077871755915, -49.49999999995852, 12.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_22)

cutting_tool_23 = cq.Solid.makeCylinder(5.0, 5.7, cq.Vector(-25.0, -5.000000000109487, 5.7), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_23)

cutting_tool_24 = cq.Solid.makeCylinder(2.6499999999999995, 6.3, cq.Vector(-25.0, -5.000000000109487, 12.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_24)

cutting_tool_25 = cq.Solid.makeCylinder(5.0, 5.7, cq.Vector(-55.0, -5.000000000109483, 5.7), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_25)

cutting_tool_26 = cq.Solid.makeCylinder(2.6499999999999995, 6.3, cq.Vector(-55.0, -5.000000000109483, 12.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_26)

cutting_tool_27 = cq.Solid.makeCylinder(5.0, 5.7, cq.Vector(-55.0, 68.99999999990277, 5.7), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_27)

cutting_tool_28 = cq.Solid.makeCylinder(2.6499999999999995, 6.3, cq.Vector(-55.0, 68.99999999990277, 12.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_28)

cutting_tool_29 = cq.Solid.makeCylinder(5.0, 5.7, cq.Vector(-25.0, 68.99999999990277, 5.7), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_29)

cutting_tool_30 = cq.Solid.makeCylinder(2.6499999999999995, 6.3, cq.Vector(-25.0, 68.99999999990277, 12.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_30)

cutting_tool_31 = cq.Solid.makeCylinder(10.0, 12.0, cq.Vector(125.0, -47.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_31)

cutting_tool_32 = cq.Solid.makeCylinder(10.0, 12.0, cq.Vector(125.0, 47.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_32)

result = part
