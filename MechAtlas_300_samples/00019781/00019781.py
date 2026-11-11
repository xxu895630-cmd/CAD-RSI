import cadquery as cq

axis_start = (0.0, 0.0, 30.0)

axis_end = (0.0, 0.0, 29.0)

profile_edge_1 = cq.Edge.makeLine((34.5, 0.0, 30.0), (35.0, 0.0, 29.5))

profile_edge_2 = cq.Edge.makeLine((34.50000000000001, 0.0, 10.0), (35.0, 0.0, 10.499999999999993))

profile_edge_3 = cq.Edge.makeLine((30.5, 0.0, 29.500000000000007), (31.0, 0.0, 30.0))

profile_edge_4 = cq.Edge.makeLine((12.5, 0.0, -9.499999999999986), (13.0, 0.0, -10.0))

profile_edge_5 = cq.Edge.makeLine((23.0, 0.0, -10.0), (23.500000000000004, 0.0, -9.500000000000028))

profile_edge_6 = cq.Edge.makeLine((12.0, 0.0, 38.0), (12.5, 0.0, 37.499999999999986))

profile_edge_7 = cq.Edge.makeLine((8.0, 0.0, 37.499999999999986), (8.499999999999993, 0.0, 38.0))

profile_edge_8 = cq.Edge.makeLine((12.5, 0.0, 37.499999999999986), (12.5, 0.0, 20.0))

profile_edge_9 = cq.Edge.makeLine((8.0, 0.0, 8.0), (8.0, 0.0, 37.499999999999986))

profile_edge_10 = cq.Edge.makeLine((30.5, 0.0, 20.0), (30.5, 0.0, 29.500000000000007))

profile_edge_11 = cq.Edge.makeLine((35.0, 0.0, 29.5), (35.0, 0.0, 10.499999999999993))

profile_edge_12 = cq.Edge.makeLine((12.5, 0.0, 8.0), (12.5, 0.0, -9.499999999999986))

profile_edge_13 = cq.Edge.makeLine((23.500000000000004, 0.0, 10.0), (23.500000000000004, 0.0, -9.500000000000028))

profile_edge_14 = cq.Edge.makeLine((12.5, 0.0, 20.0), (30.5, 0.0, 20.0))

profile_edge_15 = cq.Edge.makeLine((13.0, 0.0, -10.0), (23.0, 0.0, -10.0))

profile_edge_16 = cq.Edge.makeLine((8.0, 0.0, 8.0), (12.5, 0.0, 8.0))

profile_edge_17 = cq.Edge.makeLine((31.0, 0.0, 30.0), (34.5, 0.0, 30.0))

profile_edge_18 = cq.Edge.makeLine((23.500000000000004, 0.0, 10.0), (34.50000000000001, 0.0, 10.0))

profile_edge_19 = cq.Edge.makeLine((8.499999999999993, 0.0, 38.0), (12.0, 0.0, 38.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8, profile_edge_9, profile_edge_10, profile_edge_11, profile_edge_12, profile_edge_13, profile_edge_14, profile_edge_15, profile_edge_16, profile_edge_17, profile_edge_18, profile_edge_19])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
