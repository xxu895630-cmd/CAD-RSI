import cadquery as cq

profile_plane = cq.Plane(origin=(-8.0, 35.0, 6.0), xDir=(0.0, 1.0, 0.0), normal=(-1.0, 0.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-35.0, 11.0)
    .lineTo(-35.0, 1.0)
    .lineTo(-34.0, 0.0)
    .lineTo(-1.0, 0.0)
    .lineTo(0.0, 1.0)
    .lineTo(0.0, 11.0)
    .lineTo(-1.0, 12.0)
    .lineTo(-34.0, 12.0)
    .lineTo(-35.0, 11.0)
    .close().val())

extrusion_vector = (16.0, 0.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(3.499999999999998, 12.0, cq.Vector(2.0, 19.0, -6.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(2.6249999999999982, 12.0, cq.Vector(0.0, 6.0, -6.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(3.400000000000004, 30.0, 0.0), cq.Vector(1.0, 0.0, 0.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(2.2499999999999987, 11.4, cq.Vector(-8.0, 30.0, 0.0), cq.Vector(1.0, 0.0, 0.0))

part = part.cut(cutting_tool_4)

result = part
