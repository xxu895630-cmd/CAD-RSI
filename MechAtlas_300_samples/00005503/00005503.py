import cadquery as cq

axis_start = (0.0, 0.0, 2.5)

axis_end = (0.0, 0.0, 1.5)

profile_edge_1 = cq.Edge.makeLine((8.499999999999998, 0.0, 2.5), (9.0, 0.0, 2.0))

profile_edge_2 = cq.Edge.makeLine((8.499999999999998, 0.0, -2.500000000000001), (9.0, 0.0, -2.0))

profile_edge_3 = cq.Edge.makeLine((3.2999999999999976, 0.0, -0.9200000000000013), (6.720000000000001, 0.0, 2.5))

profile_edge_4 = cq.Edge.makeLine((3.2999999999999976, 0.0, -2.500000000000001), (3.2999999999999976, 0.0, -0.9200000000000013))

profile_edge_5 = cq.Edge.makeLine((9.0, 0.0, 2.0), (9.0, 0.0, -2.0))

profile_edge_6 = cq.Edge.makeLine((6.720000000000001, 0.0, 2.5), (8.499999999999998, 0.0, 2.5))

profile_edge_7 = cq.Edge.makeLine((3.2999999999999976, 0.0, -2.5), (8.499999999999998, 0.0, -2.5))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
