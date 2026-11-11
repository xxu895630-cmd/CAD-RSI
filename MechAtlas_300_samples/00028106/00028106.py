import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 10.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-130.0, 130.0)
    .lineTo(-130.0, -80.0)
    .lineTo(-125.0, -85.0)
    .lineTo(125.0, -85.0)
    .lineTo(130.0, -80.0)
    .lineTo(130.0, 80.0)
    .lineTo(125.0, 85.0)
    .lineTo(100.0, 85.0)
    .threePointArc((85.85786437626909, 90.85786437626906), (80.0, 105.0))
    .lineTo(80.0, 130.0)
    .lineTo(75.0, 135.0)
    .lineTo(-125.0, 135.0)
    .lineTo(-130.0, 130.0)
    .close().val())

extrusion_vector = (0.0, -10.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(2.0, 10.0, cq.Vector(-50.0, 10.0, -3.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(2.0, 10.0, cq.Vector(50.0, 10.0, -3.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(2.0, 10.0, cq.Vector(80.0, 10.0, 49.49999999999999), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(2.0, 10.0, cq.Vector(-80.0, 10.0, 49.49999999999997), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(1.6499999999999986, 10.0, cq.Vector(50.0, 10.0, 59.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCylinder(1.6499999999999986, 10.0, cq.Vector(100.0, 10.0, 59.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_6)

cutting_tool_7 = cq.Solid.makeCylinder(1.250000000000001, 10.0, cq.Vector(70.0, 10.0, -129.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_7)

cutting_tool_8 = cq.Solid.makeCylinder(1.250000000000001, 10.0, cq.Vector(10.0, 10.0, -129.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_8)

cutting_tool_9 = cq.Solid.makeCylinder(1.250000000000001, 10.0, cq.Vector(-50.0, 10.0, -129.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_9)

cutting_tool_10 = cq.Solid.makeCylinder(1.250000000000001, 10.0, cq.Vector(-110.0, 10.0, -129.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_10)

cutting_tool_11 = cq.Solid.makeCylinder(2.0999999999999943, 10.0, cq.Vector(-50.0, 10.0, -20.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_11)

cutting_tool_12 = cq.Solid.makeCylinder(2.099999999999998, 10.0, cq.Vector(50.0, 10.0, -50.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_12)

cutting_tool_13 = cq.Solid.makeCylinder(2.099999999999998, 10.0, cq.Vector(-50.0, 10.0, -50.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_13)

cutting_tool_14 = cq.Solid.makeCylinder(2.0999999999999943, 10.0, cq.Vector(50.0, 10.0, -20.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_14)

cutting_tool_15 = cq.Solid.makeCylinder(5.0, 5.7, cq.Vector(95.0, 5.7, -75.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_15)

cutting_tool_16 = cq.Solid.makeCylinder(2.7500000000000027, 4.3, cq.Vector(95.0, 10.0, -75.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_16)

cutting_tool_17 = cq.Solid.makeCylinder(5.0, 5.7, cq.Vector(95.0, 5.7, 75.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_17)

cutting_tool_18 = cq.Solid.makeCylinder(2.7500000000000027, 4.3, cq.Vector(95.0, 10.0, 75.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_18)

cutting_tool_19 = cq.Solid.makeCylinder(5.0, 5.7, cq.Vector(-95.0, 5.7, -75.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_19)

cutting_tool_20 = cq.Solid.makeCylinder(2.7500000000000027, 4.3, cq.Vector(-95.0, 10.0, -75.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_20)

cutting_tool_21 = cq.Solid.makeCylinder(5.0, 5.7, cq.Vector(-95.0, 5.7, 75.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_21)

cutting_tool_22 = cq.Solid.makeCylinder(2.7500000000000027, 4.3, cq.Vector(-95.0, 10.0, 75.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_22)

cutting_tool_23 = cq.Solid.makeCylinder(1.6499999999999986, 10.0, cq.Vector(0.0, 10.0, 59.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_23)

cutting_tool_24 = cq.Solid.makeCylinder(1.6499999999999986, 10.0, cq.Vector(-50.0, 10.0, 59.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_24)

cutting_tool_25 = cq.Solid.makeCylinder(1.6499999999999986, 10.0, cq.Vector(-100.0, 10.0, 59.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_25)

cutting_tool_26 = cq.Solid.makeCylinder(20.0, 10.0, cq.Vector(100.0, 0.0, -105.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_26)

result = part
