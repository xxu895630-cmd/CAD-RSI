import cadquery as cq

profile_plane = cq.Plane(origin=(-68.5, 0.0, 4.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, -1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-4.0, -8.0)
    .threePointArc((-2.8284271247461845, -10.828427124746192), (0.0, -12.0))
    .lineTo(137.0, -12.0)
    .threePointArc((139.82842712474618, -10.82842712474619), (141.0, -8.0))
    .lineTo(141.0, 0.0)
    .threePointArc((139.82842712474618, 2.82842712474619), (137.0, 4.0))
    .lineTo(0.0, 4.0)
    .threePointArc((-2.8284271247461845, 2.82842712474619), (-4.0, 0.0))
    .lineTo(-4.0, -8.0)
    .close().val())

extrusion_vector = (0.0, 3.2000000000568436, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCone(2.5999999999726238, 5.299999999920146, 2.6999999999475226, cq.Vector(50.0, 2.6999999999475226, 0.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(2.59999999999999, 0.5, cq.Vector(63.5, 0.0, 0.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(2.6000000000000005, 0.5, cq.Vector(-63.5, 0.0, 0.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCone(2.600000000029467, 5.300000000033833, 2.700000000004366, cq.Vector(-50.0, 2.6999999999475226, 0.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(2.5999999999999805, 0.500000000052478, cq.Vector(50.0, 2.699999999947522, 0.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCone(2.6000000000206387, 5.300000000033835, 2.7000000000131963, cq.Vector(63.5, 0.49999999997934763, 0.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_6)

cutting_tool_7 = cq.Solid.makeCone(2.5999999999922236, 5.300000000033833, 2.6999999999847657, cq.Vector(-63.5, 0.5000000000077764, 0.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_7)

cutting_tool_8 = cq.Solid.makeCylinder(2.60000000000001, 0.500000000052478, cq.Vector(-50.0, 2.699999999947522, 0.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_8)

result = part
