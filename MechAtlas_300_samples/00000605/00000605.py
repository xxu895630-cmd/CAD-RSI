import cadquery as cq

profile_plane = cq.Plane(origin=(-12.500000000000002, 5.0, 10.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(0.0, -1.0)
    .lineTo(0.0, -9.0)
    .lineTo(1.0, -10.0)
    .lineTo(24.0, -10.0)
    .lineTo(25.0, -9.0)
    .lineTo(25.0, -1.0)
    .lineTo(24.0, 0.0)
    .lineTo(1.0, 0.0)
    .lineTo(0.0, -1.0)
    .close().val())

extrusion_vector = (0.0, 0.0, -20.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(-7.499999999999997, 0.0, -5.399999999999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(2.249999999999998, 15.4, cq.Vector(-7.499999999999997, 0.0, 10.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(7.499999999999997, 0.0, -5.399999999999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(2.249999999999997, 15.4, cq.Vector(7.499999999999997, 0.0, 10.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_4)

result = part
