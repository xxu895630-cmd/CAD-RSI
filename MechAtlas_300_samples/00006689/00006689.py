import cadquery as cq

axis_start = (0.0, 0.0, 1.5)

axis_end = (0.0, 0.0, 2.5)

profile_edge_1 = cq.Edge.makeThreePointArc((22.500000000000004, 0.0, 1.5), (22.353553390593277, 0.0, 1.8535533905932737), (22.0, 0.0, 2.0))

profile_edge_2 = cq.Edge.makeThreePointArc((22.0, 0.0, 0.0), (22.353553390593277, 0.0, 0.14644660940672605), (22.500000000000004, 0.0, 0.4999999999999998))

profile_edge_3 = cq.Edge.makeThreePointArc((11.5, 0.0, 2.0), (11.146446609406727, 0.0, 1.8535533905932737), (11.0, 0.0, 1.5))

profile_edge_4 = cq.Edge.makeThreePointArc((11.0, 0.0, 0.5000000000000028), (11.146446609406725, 0.0, 0.14644660940672716), (11.5, 0.0, 0.0))

profile_edge_5 = cq.Edge.makeLine((11.0, 0.0, 1.5), (11.0, 0.0, 0.5))

profile_edge_6 = cq.Edge.makeLine((22.500000000000004, 0.0, 1.5), (22.500000000000004, 0.0, 0.5))

profile_edge_7 = cq.Edge.makeLine((11.5, 0.0, 2.0), (22.0, 0.0, 2.0))

profile_edge_8 = cq.Edge.makeLine((11.5, 0.0, 0.0), (22.0, 0.0, 0.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
