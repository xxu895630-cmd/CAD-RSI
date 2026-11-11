import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 20.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(0.0, -20.0)
    .lineTo(25.0, -20.0)
    .lineTo(25.0, 0.0)
    .lineTo(0.0, 0.0)
    .lineTo(0.0, -20.0)
    .close().val())

extrusion_vector = (0.0, 0.0, -10.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(2.2499999999999973, 20.0, cq.Vector(5.0, 0.0, -5.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(2.249999999999997, 20.0, cq.Vector(20.0, 0.0, -5.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(3.4999999999999996, 10.0, cq.Vector(12.5, 13.0, -10.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_3)

result = part
