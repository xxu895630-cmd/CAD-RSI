import cadquery as cq

axis_start = (0.0, 0.0, 0.30000000000000165)

axis_end = (0.0, 0.0, 1.3000000000000016)

profile_edge_1 = cq.Edge.makeLine((3.6999999999999984, 0.0, 0.0), (4.0, 0.0, 0.30000000000000165))

profile_edge_2 = cq.Edge.makeLine((5.700000000000001, 0.0, 20.0), (6.0, 0.0, 20.299999999999997))

profile_edge_3 = cq.Edge.makeLine((5.700000000000004, 0.0, 24.0), (6.0, 0.0, 23.7))

profile_edge_4 = cq.Edge.makeLine((2.099999999999996, 0.0, 24.0), (2.099999999999996, 0.0, 0.0))

profile_edge_5 = cq.Edge.makeLine((6.0, 0.0, 23.7), (6.0, 0.0, 20.299999999999997))

profile_edge_6 = cq.Edge.makeLine((4.0, 0.0, 20.0), (4.0, 0.0, 0.30000000000000165))

profile_edge_7 = cq.Edge.makeLine((2.099999999999998, 0.0, 0.0), (3.6999999999999984, 0.0, 0.0))

profile_edge_8 = cq.Edge.makeLine((4.0, 0.0, 20.0), (5.7, 0.0, 20.0))

profile_edge_9 = cq.Edge.makeLine((2.0999999999999948, 0.0, 24.0), (5.700000000000004, 0.0, 24.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8, profile_edge_9])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
