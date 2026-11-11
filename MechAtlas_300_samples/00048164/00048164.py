import cadquery as cq

axis_start = (0.0, 0.0, -4.2)

axis_end = (0.0, 0.0, -3.2)

profile_edge_1 = cq.Edge.makeLine((6.499999999999991, 0.0, -4.2), (7.5, 0.0, -3.199999999999987))

profile_edge_2 = cq.Edge.makeLine((7.5, 0.0, -3.199999999999987), (7.5, 0.0, -1.2000000000000002))

profile_edge_3 = cq.Edge.makeLine((7.0, 0.0, -1.2000000000000002), (7.0, 0.0, 0.0))

profile_edge_4 = cq.Edge.makeLine((9.499999999999995, 0.0, 56.0), (10.0, 0.0, 56.50000000000001))

profile_edge_5 = cq.Edge.makeLine((9.0, 0.0, 62.0), (10.0, 0.0, 61.0))

profile_edge_6 = cq.Edge.makeLine((10.0, 0.0, 61.0), (10.0, 0.0, 56.50000000000001))

profile_edge_7 = cq.Edge.makeLine((7.0, 0.0, 56.0), (7.0, 0.0, 55.0))

profile_edge_8 = cq.Edge.makeLine((7.5, 0.0, 55.0), (7.5, 0.0, 0.0))

profile_edge_9 = cq.Edge.makeLine((7.0, 0.0, 55.0), (7.5, 0.0, 55.0))

profile_edge_10 = cq.Edge.makeLine((7.0, 0.0, 0.0), (7.5, 0.0, 0.0))

profile_edge_11 = cq.Edge.makeLine((0.0, 0.0, 62.0), (9.0, 0.0, 62.0))

profile_edge_12 = cq.Edge.makeLine((7.0, 0.0, 56.0), (9.499999999999995, 0.0, 56.0))

profile_edge_13 = cq.Edge.makeLine((0.0, 0.0, -4.2), (6.499999999999991, 0.0, -4.2))

profile_edge_14 = cq.Edge.makeLine((7.0, 0.0, -1.2000000000000002), (7.5, 0.0, -1.2000000000000002))

profile_edge_15 = cq.Edge.makeLine((0.0, 0.0, 62.0), (0.0, 0.0, -4.2))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8, profile_edge_9, profile_edge_10, profile_edge_11, profile_edge_12, profile_edge_13, profile_edge_14, profile_edge_15])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
