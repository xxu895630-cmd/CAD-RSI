import cadquery as cq

profile_plane = cq.Plane(origin=(20.0, 12.0, -29.499999999999996), xDir=(0.0, 1.0, 0.0), normal=(1.0, 0.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-12.0, 13.499999999999996)
    .lineTo(-12.0, 0.49999999999999645)
    .lineTo(-11.499999999999998, 0.0)
    .lineTo(-0.4999999999999982, 0.0)
    .lineTo(0.0, 0.4999999999999929)
    .lineTo(0.0, 58.499999999999986)
    .lineTo(-0.5000000000000036, 59.0)
    .lineTo(-11.499999999999998, 59.0)
    .lineTo(-12.0, 58.5)
    .lineTo(-12.0, 45.5)
    .lineTo(-5.0, 45.5)
    .lineTo(-5.0, 13.499999999999996)
    .lineTo(-12.0, 13.499999999999996)
    .close().val())

extrusion_vector = (-40.0, 0.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(5.0, 5.400000000000004, cq.Vector(-14.599999999999996, 6.0, -22.5), cq.Vector(-1.0, 0.0, 0.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(2.7499999999999956, 34.60000000000001, cq.Vector(20.0, 6.0, -22.500000000000004), cq.Vector(-1.0, 0.0, 0.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(5.0, 5.400000000000002, cq.Vector(-14.6, 6.0, 22.5), cq.Vector(-1.0, 0.0, 0.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(2.7499999999999956, 34.60000000000001, cq.Vector(20.0, 6.0, 22.499999999999996), cq.Vector(-1.0, 0.0, 0.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(13.5, 5.0, cq.Vector(0.0, 12.0, 0.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_5)

result = part
