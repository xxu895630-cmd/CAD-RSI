import cadquery as cq

axis_start = (0.0, 0.29999999999999644, 0.0)

axis_end = (0.0, 1.2999999999999965, 0.0)

profile_edge_1 = cq.Edge.makeLine((1.2000000000000033, 0.0, 0.0), (1.5000000000000002, 0.29999999999999644, 0.0))

profile_edge_2 = cq.Edge.makeThreePointArc((1.3047478290881747, 9.562017367294603, 0.0), (1.1395101723492114, 9.874839087907933, 0.0), (0.8086088907313407, 10.0, 0.0))

profile_edge_3 = cq.Edge.makeLine((1.3047478290881747, 9.562017367294603, 0.0), (1.5000000000000002, 8.0, 0.0))

profile_edge_4 = cq.Edge.makeLine((1.5000000000000002, 8.0, 0.0), (1.5000000000000002, 0.29999999999999644, 0.0))

profile_edge_5 = cq.Edge.makeLine((0.0, 0.0, 0.0), (1.2000000000000033, 0.0, 0.0))

profile_edge_6 = cq.Edge.makeLine((0.0, 10.0, 0.0), (0.8086088907313407, 10.0, 0.0))

profile_edge_7 = cq.Edge.makeLine((0.0, 0.0, 0.0), (0.0, 10.0, 0.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
