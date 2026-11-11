import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 10.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(0.0, 23.499999999999993)
    .threePointArc((-12.01561484069792, 28.276989350000527), (-17.471405209656147, 40.0))
    .lineTo(-29.0, 40.0)
    .lineTo(-29.0, 8.0)
    .lineTo(-45.0, 8.0)
    .lineTo(-45.0, -4.0)
    .lineTo(45.0, -4.0)
    .lineTo(45.0, 8.0)
    .lineTo(29.0, 8.0)
    .lineTo(29.0, 40.0)
    .lineTo(17.471405209656147, 40.0)
    .threePointArc((12.015614840697916, 28.27698935000052), (0.0, 23.499999999999993))
    .close().val())

extrusion_vector = (0.0, -20.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(2.4999999999999987, 15.0, cq.Vector(21.499999999999996, 0.0, -25.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCone(0.0, 2.499999999999996, 1.502151547568905, cq.Vector(21.499999999999996, 0.0, -23.49784845243109), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(2.499999999999995, 15.0, cq.Vector(-21.500000000000004, 0.0, -25.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCone(0.0, 2.499999999999996, 1.502151547568905, cq.Vector(-21.500000000000004, 0.0, -23.49784845243109), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(4.49999980628489, 12.0, cq.Vector(37.0, 0.0, 4.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCylinder(4.49999980628489, 12.0, cq.Vector(-37.0, 0.0, 4.0), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_6)

cutting_tool_7 = cq.Solid.makeCylinder(17.5, 20.0, cq.Vector(0.0, -10.0, -41.0), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_7)

result = part
