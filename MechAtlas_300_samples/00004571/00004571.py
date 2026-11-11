import cadquery as cq

axis_start = (0.0, 0.0, 0.0)

axis_end = (0.0, 1.0, 0.0)

profile_edge_1 = cq.Edge.makeLine((1.800000000000003, 0.0, 0.0), (2.0, 0.1999999999999997, 0.0))

profile_edge_2 = cq.Edge.makeLine((2.700000000000003, 16.7, 0.0), (3.0, 16.400000000000002, 0.0))

profile_edge_3 = cq.Edge.makeLine((3.0, 16.400000000000002, 0.0), (3.0, 14.7, 0.0))

profile_edge_4 = cq.Edge.makeLine((2.0, 14.7, 0.0), (2.0, 2.0, 0.0))

profile_edge_5 = cq.Edge.makeLine((1.5, 2.0, 0.0), (1.5, 1.1999999999999997, 0.0))

profile_edge_6 = cq.Edge.makeLine((2.0, 1.1999999999999997, 0.0), (2.0, 0.19999999999999968, 0.0))

profile_edge_7 = cq.Edge.makeLine((0.0, 0.0, 0.0), (1.800000000000003, 0.0, 0.0))

profile_edge_8 = cq.Edge.makeLine((1.5, 1.1999999999999997, 0.0), (2.0, 1.1999999999999997, 0.0))

profile_edge_9 = cq.Edge.makeLine((1.5, 2.0, 0.0), (2.0, 2.0, 0.0))

profile_edge_10 = cq.Edge.makeLine((2.0, 14.7, 0.0), (3.0, 14.7, 0.0))

profile_edge_11 = cq.Edge.makeLine((0.0, 16.7, 0.0), (2.7000000000000024, 16.7, 0.0))

profile_edge_12 = cq.Edge.makeLine((0.0, 0.0, 0.0), (0.0, 16.7, 0.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8, profile_edge_9, profile_edge_10, profile_edge_11, profile_edge_12])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
