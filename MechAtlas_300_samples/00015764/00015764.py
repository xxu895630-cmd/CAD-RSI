import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, -1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(12.500000000000004, -5.0)
    .lineTo(12.500000000000004, 5.0)
    .lineTo(-12.499999999999996, 5.0)
    .lineTo(-12.499999999999996, -5.0)
    .lineTo(12.500000000000004, -5.0)
    .close().val())

extrusion_vector = (0.0, 0.0, 6.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(2.749999999999999, 2.8999999999999995, cq.Vector(-7.5, 0.0, 3.1000000000000005), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(1.4499999999999982, 3.1000000000000005, cq.Vector(-7.5, 0.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(2.749999999999999, 2.8999999999999995, cq.Vector(7.5, 0.0, 3.1000000000000005), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(1.45, 3.1000000000000005, cq.Vector(7.5, 0.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_4)

result = part
