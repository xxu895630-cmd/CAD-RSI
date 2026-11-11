import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, -3.5), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, -1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(7.0, -19.0)
    .lineTo(7.0, 19.0)
    .lineTo(6.0, 20.0)
    .lineTo(-6.0, 20.0)
    .lineTo(-7.0, 19.0)
    .lineTo(-7.0, -19.0)
    .lineTo(-6.0, -20.0)
    .lineTo(6.0, -20.0)
    .lineTo(7.0, -19.0)
    .close().val())

extrusion_vector = (0.0, 0.0, 7.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCone(2.7499999999999982, 6.3999999999999995, 3.6500000000000044, cq.Vector(0.0, -12.0, -0.15000000000000346), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(2.7499999999999982, 3.349999999999995, cq.Vector(0.0, -12.0, -3.499999999999999), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCone(2.7499999999999982, 6.3999999999999995, 3.6500000000000044, cq.Vector(0.0, 12.0, -0.15000000000000346), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(2.7499999999999982, 3.349999999999995, cq.Vector(0.0, 12.0, -3.499999999999999), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_4)

result = part
