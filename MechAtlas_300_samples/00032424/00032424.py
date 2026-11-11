import cadquery as cq

profile_plane = cq.Plane(origin=(47.0, 68.50000000000003, -58.79838433154441), xDir=(0.0, 1.0, 0.0), normal=(1.0, 0.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-3.500000000000057, 78.79838433154441)
    .lineTo(-45.500000000000064, 78.79838433154441)
    .lineTo(-47.50000000000006, 76.79838433154441)
    .lineTo(-47.50000000000006, 58.79838433154441)
    .lineTo(-1.5000000000000426, 58.79838433154441)
    .lineTo(-1.5000000000000426, 76.79838433154444)
    .lineTo(-3.5000000000000284, 78.79838433154443)
    .close().val())

extrusion_vector = (-10.0, 0.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(1.6499999999999986, 11.5, cq.Vector(42.0, 63.0, 11.5), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCone(0.0, 1.6499999999999986, 0.9914200213954756, cq.Vector(42.0, 63.0, 12.491420021395475), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(1.6499999999999986, 11.5, cq.Vector(42.0, 25.0, 11.5), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCone(0.0, 1.6499999999999986, 0.9914200213954756, cq.Vector(42.0, 25.0, 12.491420021395475), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(2.4999999999999987, 10.0, cq.Vector(37.0, 31.499999999999993, 14.0), cq.Vector(1.0, 0.0, 0.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCylinder(2.4999999999999987, 10.0, cq.Vector(37.0, 56.499999999999986, 14.0), cq.Vector(1.0, 0.0, 0.0))

part = part.cut(cutting_tool_6)

result = part
