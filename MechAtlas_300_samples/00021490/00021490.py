import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 400.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(1.5, 7.5)
    .lineTo(4.5000000000000036, 7.5)
    .lineTo(4.5000000000000036, 6.249999999999998)
    .lineTo(6.0, 6.249999999999998)
    .lineTo(6.0, 9.0)
    .lineTo(2.0, 9.0)
    .lineTo(2.0, 19.0)
    .lineTo(0.0, 19.0)
    .lineTo(0.0, 0.0)
    .lineTo(6.0, 0.0)
    .lineTo(6.0, 2.749999999999999)
    .lineTo(4.5000000000000036, 2.749999999999999)
    .lineTo(4.5000000000000036, 1.5)
    .lineTo(1.5000000000000007, 1.5)
    .lineTo(1.5, 7.5)
    .close().val())

extrusion_vector = (0.0, 0.0, -400.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(2.2499999999999987, 2.0, cq.Vector(0.0, 14.0, 20.0), cq.Vector(1.0, 0.0, 0.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(2.2499999999999742, 2.0, cq.Vector(0.0, 14.0, 380.0), cq.Vector(1.0, 0.0, 0.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(2.2500000000000018, 2.0, cq.Vector(0.0, 14.0, 140.0), cq.Vector(1.0, 0.0, 0.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(2.2499999999999742, 2.0, cq.Vector(0.0, 14.0, 260.0), cq.Vector(1.0, 0.0, 0.0))

part = part.cut(cutting_tool_4)

result = part
