import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 10.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(11.0, 68.0)
    .lineTo(1.0, 68.0)
    .lineTo(0.0, 67.0)
    .lineTo(0.0, 5.0)
    .lineTo(5.0, 0.0)
    .lineTo(56.0, 0.0)
    .lineTo(57.0, 1.0)
    .lineTo(57.0, 11.0)
    .lineTo(56.0, 12.0)
    .lineTo(43.0, 12.0)
    .lineTo(12.0, 54.0)
    .lineTo(12.0, 67.0)
    .lineTo(11.0, 68.0)
    .close().val())

extrusion_vector = (0.0, -10.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(1.6499999999999884, 10.1, cq.Vector(20.0, 5.0, -10.099999999999998), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCone(0.0, 1.649999999999989, 0.9914200213954801, cq.Vector(20.0, 5.0, -11.091420021395479), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(1.6499999999999848, 10.1, cq.Vector(50.0, 5.0, -10.099999999999998), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCone(0.0, 1.6499999999999848, 0.9914200213954771, cq.Vector(50.0, 5.0, -11.091420021395475), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(1.6499999999999986, 10.1, cq.Vector(10.1, 5.0, -60.0), cq.Vector(-1.0, 0.0, 0.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCone(0.0, 1.6499999999999986, 0.9914200213954779, cq.Vector(11.091420021395477, 5.0, -60.0), cq.Vector(-1.0, 0.0, 0.0))

part = part.cut(cutting_tool_6)

cutting_tool_7 = cq.Solid.makeCylinder(1.6499999999999986, 10.1, cq.Vector(10.1, 5.0, -20.0), cq.Vector(-1.0, 0.0, 0.0))

part = part.cut(cutting_tool_7)

cutting_tool_8 = cq.Solid.makeCone(0.0, 1.649999999999995, 0.9914200213954758, cq.Vector(11.091420021395475, 5.0, -20.0), cq.Vector(-1.0, 0.0, 0.0))

part = part.cut(cutting_tool_8)

result = part
