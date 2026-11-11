import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 5.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-51.5, -114.3)
    .lineTo(51.5, -114.3)
    .lineTo(53.5, -112.3)
    .lineTo(53.5, 112.3)
    .lineTo(51.5, 114.3)
    .lineTo(-51.5, 114.3)
    .lineTo(-53.5, 112.3)
    .lineTo(-53.5, -112.3)
    .lineTo(-51.5, -114.3)
    .close().val())

extrusion_vector = (0.0, 0.0, -10.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(2.75, 4.3, cq.Vector(-33.5000000000736, 76.3000000001607, 0.7), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(5.0, 5.7, cq.Vector(-33.5000000000736, 76.3000000001607, -5.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(2.75, 4.3, cq.Vector(33.4999999999836, 76.3000000001615, 0.7), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(5.0, 5.7, cq.Vector(33.4999999999836, 76.3000000001615, -5.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(2.75, 4.3, cq.Vector(-33.5000000000709, -76.2999999999688, 0.7), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCylinder(5.0, 5.7, cq.Vector(-33.5000000000709, -76.2999999999688, -5.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_6)

cutting_tool_7 = cq.Solid.makeCylinder(2.75, 4.3, cq.Vector(33.4999999999862, -76.2999999999679, 0.7), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_7)

cutting_tool_8 = cq.Solid.makeCylinder(5.0, 5.7, cq.Vector(33.4999999999862, -76.2999999999679, -5.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_8)

cutting_tool_9 = cq.Solid.makeCylinder(4.0, 4.600000000000001, cq.Vector(30.9999999999835, 37.8000000001293, 5.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_9)

cutting_tool_10 = cq.Solid.makeCylinder(2.25, 5.399999999999999, cq.Vector(30.9999999999835, 37.8000000001293, 0.399999999999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_10)

cutting_tool_11 = cq.Solid.makeCylinder(4.0, 4.600000000000001, cq.Vector(-29.0000000000672, 37.8000000001292, 5.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_11)

cutting_tool_12 = cq.Solid.makeCylinder(2.25, 5.399999999999999, cq.Vector(-29.0000000000672, 37.8000000001292, 0.399999999999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_12)

cutting_tool_13 = cq.Solid.makeCylinder(4.0, 4.600000000000001, cq.Vector(30.9999999999839, -27.1999999999255, 5.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_13)

cutting_tool_14 = cq.Solid.makeCylinder(2.25, 5.399999999999999, cq.Vector(30.9999999999839, -27.1999999999255, 0.399999999999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_14)

cutting_tool_15 = cq.Solid.makeCylinder(4.0, 4.600000000000001, cq.Vector(-29.0000000000667, -27.1999999999257, 5.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_15)

cutting_tool_16 = cq.Solid.makeCylinder(2.25, 5.399999999999999, cq.Vector(-29.0000000000667, -27.1999999999257, 0.399999999999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_16)

cutting_tool_17 = cq.Solid.makeCylinder(4.0, 4.600000000000001, cq.Vector(30.9999999999844, -92.1999999999804, 5.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_17)

cutting_tool_18 = cq.Solid.makeCylinder(2.25, 5.399999999999999, cq.Vector(30.9999999999844, -92.1999999999804, 0.399999999999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_18)

cutting_tool_19 = cq.Solid.makeCylinder(4.0, 4.600000000000001, cq.Vector(-29.0000000000663, -92.1999999999805, 5.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_19)

cutting_tool_20 = cq.Solid.makeCylinder(2.25, 5.399999999999999, cq.Vector(-29.0000000000663, -92.1999999999805, 0.399999999999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_20)

result = part
