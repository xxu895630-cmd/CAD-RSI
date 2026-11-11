import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 30.0), xDir=(0.0, 1.0, 0.0), normal=(1.0, 0.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-26.0, -30.0)
    .lineTo(-5.0, -30.0)
    .lineTo(0.0, -25.0)
    .lineTo(0.0, -5.0)
    .lineTo(-5.0, 0.0)
    .lineTo(-26.0, 0.0)
    .lineTo(-26.0, -30.0)
    .close().val())

extrusion_vector = (-10.0, 0.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(3.3999999999999924, 10.0, cq.Vector(-10.0, -8.0, 7.0), cq.Vector(1.0, 0.0, 0.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(1.6499999999999986, 11.500000000000002, cq.Vector(-5.0, -14.499999999999998, 24.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCone(0.0, 1.6499999999999986, 0.9914200213954779, cq.Vector(-5.0, -13.508579978604521, 24.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(1.649999999999998, 11.500000000000002, cq.Vector(-5.0, -14.499999999999998, 6.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCone(0.0, 1.6499999999999977, 0.9914200213954771, cq.Vector(-5.0, -13.508579978604521, 6.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCylinder(3.399999999999997, 10.0, cq.Vector(0.0, -8.0, 23.0), cq.Vector(-1.0, 0.0, 0.0))

part = part.cut(cutting_tool_6)

result = part
