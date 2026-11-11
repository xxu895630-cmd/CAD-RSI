import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, -1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-0.14633913065559145, -199.3963391306556)
    .lineTo(-13.727636104875389, -212.97763610487533)
    .threePointArc((-13.841785095851094, -213.507978868098), (-13.405367118292132, -213.83020982177376))
    .threePointArc((-6.705969194865215, -214.14502673925801), (0.0, -214.25000000000003))
    .threePointArc((146.19509665649662, -156.62074004932305), (213.74267659204492, -14.735355552836644))
    .threePointArc((213.7121105731178, -14.525633614153685), (213.59741393458202, -14.347413934582143))
    .lineTo(200.09992790779057, -0.8499279077905747)
    .threePointArc((199.55642525469707, -0.7409672146246644), (199.24638359224812, -1.2004688295518797))
    .threePointArc((140.53923395341042, -141.2419421410955), (0.2066955759328325, -199.24989279028205))
    .threePointArc((0.015632968693571725, -199.28805206303278), (-0.14633913065560583, -199.39633913065558))
    .close().val())

extrusion_vector = (0.0, 19.9, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(4.0, 4.600000000000001, cq.Vector(203.60900293527388, 15.299999999999997, -35.90176073263866), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(2.2500000000000018, 15.299999999999997, cq.Vector(203.60900293527388, 0.0, -35.90176073263866), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(4.0, 4.600000000000001, cq.Vector(139.67827542453693, 15.299999999999997, -152.43208938549387), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(2.2500000000000018, 15.299999999999997, cq.Vector(139.67827542453693, 0.0, -152.43208938549387), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_4)

cutting_tool_5 = cq.Solid.makeCylinder(4.0, 4.600000000000001, cq.Vector(18.019449813076907, 15.299999999999997, -205.9632538304685), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_5)

cutting_tool_6 = cq.Solid.makeCylinder(2.2500000000000018, 15.299999999999997, cq.Vector(18.019449813076907, 0.0, -205.9632538304685), cq.Vector(0.0, 1.0, 0.0))

part = part.cut(cutting_tool_6)

cutting_tool_7 = cq.Solid.makeCylinder(199.25, 19.9, cq.Vector(0.0, 19.9, 0.0), cq.Vector(0.0, -1.0, 0.0))

part = part.cut(cutting_tool_7)

result = part
