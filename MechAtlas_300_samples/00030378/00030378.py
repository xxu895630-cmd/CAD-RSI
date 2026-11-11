import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 8.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(10.0, -5.0)
    .lineTo(10.0, 3.0)
    .threePointArc((9.414213562373096, 4.414213562373095), (8.0, 5.0))
    .lineTo(-8.0, 5.0)
    .threePointArc((-9.414213562373096, 4.414213562373095), (-10.0, 3.0))
    .lineTo(-10.0, -5.0)
    .lineTo(10.0, -5.0)
    .close().val())

extrusion_vector = (0.0, 0.0, -8.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(1.621, 8.0, cq.Vector(0.0, 0.0, 0.0), cq.Vector(0.0, 0.0, 1.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(1.621, 10.0, cq.Vector(6.0, 5.0, 4.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(1.621, 10.0, cq.Vector(-6.0, 5.0, 4.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_3)

result = part
