import cadquery as cq

profile_plane = cq.Plane(origin=(-61.0, 70.68521213776731, -90.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, -1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(88.5, 45.585212137768806)
    .threePointArc((89.56066017177983, 46.024551965988984), (90.0, 47.085212137768806))
    .lineTo(90.0, 69.18521213776731)
    .threePointArc((89.56066017177983, 70.24587230954712), (88.5, 70.68521213776731))
    .lineTo(88.0, 70.68521213776731)
    .lineTo(88.0, 47.085212137768806)
    .lineTo(71.5, 47.085212137768806)
    .lineTo(71.5, 51.28521213776581)
    .lineTo(68.3, 51.28521213776581)
    .lineTo(68.3, 49.78521213776581)
    .lineTo(70.0, 49.78521213776581)
    .lineTo(70.0, 47.085212137768806)
    .lineTo(61.0, 47.085212137768806)
    .lineTo(61.0, 28.43521213776731)
    .threePointArc((61.75, 27.68521213776731), (62.5, 28.43521213776731))
    .lineTo(62.5, 45.585212137768806)
    .lineTo(68.7, 45.585212137768806)
    .lineTo(68.7, 28.43521213776731)
    .threePointArc((69.45, 27.68521213776731), (70.2, 28.43521213776731))
    .lineTo(70.2, 45.585212137768806)
    .lineTo(76.4, 45.585212137768806)
    .lineTo(76.4, 28.43521213776731)
    .threePointArc((77.15, 27.68521213776731), (77.9, 28.43521213776731))
    .lineTo(77.9, 45.585212137768806)
    .lineTo(84.1, 45.585212137768806)
    .lineTo(84.1, 28.636212137768204)
    .threePointArc((84.85, 27.886212137768204), (85.6, 28.636212137768204))
    .lineTo(85.6, 45.585212137768806)
    .lineTo(88.5, 45.585212137768806)
    .close().val())

extrusion_vector = (0.0, 0.0, 1000.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(2.249999999999995, 2.0, cq.Vector(27.0, 13.099999999999907, -30.0), cq.Vector(1.0, 0.0, 0.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(2.2500000000000018, 2.0, cq.Vector(27.0, 13.099999999999907, 190.0), cq.Vector(1.0, 0.0, 0.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(2.2499999999999742, 2.0, cq.Vector(27.0, 13.099999999999907, 850.0), cq.Vector(1.0, 0.0, 0.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(2.2499999999999742, 2.0, cq.Vector(27.0, 13.099999999999907, 630.0), cq.Vector(1.0, 0.0, 0.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(2.2499999999999742, 2.0, cq.Vector(27.0, 13.099999999999907, 410.0), cq.Vector(1.0, 0.0, 0.0))

part = part.cut(cutting_tool_5)

result = part
