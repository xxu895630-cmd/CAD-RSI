import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 10.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-15.0, 0.0)
    .threePointArc((0.0, -15.0), (15.0, 0.0))
    .threePointArc((0.0, 15.0), (-15.0, 0.0))
    .close().val())

extrusion_vector = (0.0, 0.0, -10.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(0.0, 10.0, 4.6), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(2.2499999999999996, 5.4, cq.Vector(0.0, 10.0, 10.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(10.0, 0.0, 4.6), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(2.2499999999999996, 5.4, cq.Vector(10.0, 0.0, 10.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(0.0, -10.0, 4.6), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCylinder(2.2499999999999996, 5.4, cq.Vector(0.0, -10.0, 10.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_6)

cutting_tool_7 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(-10.0, 0.0, 4.6), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_7)

cutting_tool_8 = cq.Solid.makeCylinder(2.2499999999999987, 5.4, cq.Vector(-10.0, 0.0, 10.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_8)

result = part
