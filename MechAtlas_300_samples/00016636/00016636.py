import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 3.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-61.49999999999994, -38.49999999999999)
    .lineTo(61.49999999999997, -38.49999999999999)
    .lineTo(64.50000000000001, -35.499999999999964)
    .lineTo(64.50000000000003, 35.49999999999999)
    .lineTo(61.50000000000003, 38.50000000000001)
    .lineTo(-61.49999999999993, 38.50000000000001)
    .lineTo(-64.49999999999996, 35.499999999999986)
    .lineTo(-64.49999999999994, -35.49999999999998)
    .lineTo(-61.49999999999995, -38.5)
    .close().val())

extrusion_vector = (0.0, -3.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(1.6999999999999862, 1.3399999999999774, cq.Vector(-59.49999999999993, 3.0, -33.50000000000003), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCone(1.6999999999999877, 3.3600000000000008, 1.6600000000000217, cq.Vector(-59.49999999999993, 1.6600000000000212, -33.50000000000003), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(1.6999999999999862, 1.3399999999999774, cq.Vector(59.50000000000008, 3.0, -33.49999999999999), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCone(1.6999999999999877, 3.3600000000000008, 1.6600000000000217, cq.Vector(59.50000000000008, 1.6600000000000212, -33.49999999999999), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(1.6999999999999862, 1.3399999999999774, cq.Vector(59.50000000000006, 3.0, 33.500000000000014), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCone(1.6999999999999855, 3.3599999999999954, 1.6600000000000252, cq.Vector(59.50000000000006, 1.660000000000023, 33.500000000000014), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_6)

cutting_tool_7 = cq.Solid.makeCylinder(1.6999999999999862, 1.3399999999999774, cq.Vector(-59.49999999999994, 3.0, 33.499999999999986), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_7)

cutting_tool_8 = cq.Solid.makeCone(1.6999999999999857, 3.3600000000000025, 1.6600000000000255, cq.Vector(-59.49999999999994, 1.6600000000000232, 33.499999999999986), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_8)

result = part
