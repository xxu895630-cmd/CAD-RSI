import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, -1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-6.4999999999999964, -6.0)
    .lineTo(6.500000000000003, -6.0)
    .lineTo(7.499999999999999, -5.0)
    .lineTo(7.499999999999999, 5.0)
    .lineTo(6.4999999999999964, 6.0)
    .lineTo(-6.5000000000000036, 6.0)
    .lineTo(-7.500000000000001, 5.0)
    .lineTo(-7.500000000000001, -5.0)
    .lineTo(-6.4999999999999964, -6.0)
    .close().val())

extrusion_vector = (0.0, 0.0, 12.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(4.0, 4.6, cq.Vector(0.0, 0.0, 7.4), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(2.2500000000000013, 7.4, cq.Vector(0.0, 0.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_2)

result = part
