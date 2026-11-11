import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, -5.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, -1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(0.0, -2.0)
    .lineTo(0.0, -33.0)
    .lineTo(2.0, -35.0)
    .lineTo(8.0, -35.0)
    .lineTo(10.0, -33.0)
    .lineTo(10.0, -16.0)
    .lineTo(16.0, -10.0)
    .lineTo(58.0, -10.0)
    .lineTo(60.0, -8.0)
    .lineTo(60.0, -2.0)
    .lineTo(58.0, 0.0)
    .lineTo(2.0, 0.0)
    .lineTo(0.0, -2.0)
    .close().val())

extrusion_vector = (0.0, 10.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(2.249999999999988, 10.0, cq.Vector(54.0, 0.0, 0.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(2.249999999999988, 10.0, cq.Vector(34.0, 0.0, 0.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(2.249999999999995, 10.0, cq.Vector(0.0, 0.0, -29.0), cq.Vector(1.0, 0.0, 0.0))

part = part.cut(cutting_tool_3)

result = part
