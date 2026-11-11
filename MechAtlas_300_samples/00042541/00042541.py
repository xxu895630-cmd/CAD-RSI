import cadquery as cq

profile_plane = cq.Plane(origin=(-259.171570791995, -418.853308176929, 20.0000000999999), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, -1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(303.53581712295284, -375.5340826992105)
    .threePointArc((304.94972076185405, -374.9481268116629), (305.5353377124165, -373.53408275666897))
    .lineTo(305.5353377124165, -288.53552093086)
    .threePointArc((304.9495512747896, -287.1213073684869), (303.5353377124165, -286.53552093086))
    .lineTo(297.5353377124165, -286.53552093086)
    .threePointArc((296.12112415004344, -287.1213073684869), (295.5353377124165, -288.53552093086))
    .lineTo(295.5353377124165, -373.535520988319)
    .threePointArc((296.12129365742254, -374.9499040377565), (297.5358171229527, -375.53552093086034))
    .lineTo(303.53581712295284, -375.5340826992105)
    .close().val())

extrusion_vector = (0.0, 0.0, 6.299999999999997)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])

part = result

cutting_tool_1 = cq.Solid.makeCylinder(1.75, 2.299999999999997, cq.Vector(41.3612030768291, -112.319129562148, 22.3000000999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_1)

cutting_tool_2 = cq.Solid.makeCylinder(1.75, 2.299999999999997, cq.Vector(41.3612030768291, -58.3191295621475, 22.3000000999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_2)

cutting_tool_3 = cq.Solid.makeCylinder(3.0, 4.0, cq.Vector(41.3612030768291, -112.319129562148, 26.3000000999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_3)

cutting_tool_4 = cq.Solid.makeCylinder(3.0, 4.0, cq.Vector(41.3612030768291, -58.3191295621475, 26.3000000999999), cq.Vector(0.0, 0.0, -1.0))

part = part.cut(cutting_tool_4)

result = part
