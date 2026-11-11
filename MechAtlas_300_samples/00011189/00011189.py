import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 14.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-9.0, 2.0)
    .lineTo(-9.0, -2.0)
    .lineTo(-7.0, -4.0)
    .lineTo(7.0, -4.0)
    .lineTo(9.0, -2.0)
    .lineTo(9.0, 2.0)
    .lineTo(7.0, 4.0)
    .lineTo(-7.0, 4.0)
    .lineTo(-9.0, 2.0)
    .close().val())

extrusion_vector = (0.0, 0.0, -14.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(2.2500000000000004, 3.0, cq.Vector(0.0, -1.0, 4.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(3.0, 3.4, cq.Vector(-5.5, 0.0, 3.4), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(1.6999999999999984, 10.6, cq.Vector(-5.5, 0.0, 14.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(3.0, 3.4, cq.Vector(5.5, 0.0, 3.4), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(1.6999999999999984, 10.6, cq.Vector(5.5, 0.0, 14.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCylinder(2.2500000000000004, 3.0, cq.Vector(0.0, 1.0, 4.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_6)

result = part
