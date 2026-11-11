import cadquery as cq

profile_plane = cq.Plane(origin=(-26.09747935004, -127.7167379087, -8.919989496319), xDir=(1.0, 2.810401049369e-10, 0.0), normal=(-2.810401049369e-10, 1.0, -2.117957963991e-10))

outer_profile = cq.Workplane(profile_plane).center(0.0, 0.0).circle(3.5).val()

extrusion_vector = (5.620802099350173e-10, -2.000000000217824, 4.235915928443342e-10)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(2.05, 1.999999998991001, cq.Vector(-26.097479350038547, -127.716737908993, -8.919989496318902), cq.Vector(4.104066281995e-11, -1.0, -4.559987940501e-11))

part = part.cut(cutting_tool_1)

result = part
