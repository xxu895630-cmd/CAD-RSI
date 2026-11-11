import cadquery as cq

axis_start = (0.0, -2.5, 0.0)

axis_end = (0.0, -1.5, 0.0)

profile_edge_1 = cq.Edge.makeLine((2.5000000000000093, -2.5, 0.0), (3.0, -2.0, 0.0))

profile_edge_2 = cq.Edge.makeLine((2.0, 36.699999999999996, 0.0), (2.0, 35.50000000000001, 0.0))

profile_edge_3 = cq.Edge.makeLine((1.7000000000000002, 37.0, 0.0), (2.0, 36.699999999999996, 0.0))

profile_edge_4 = cq.Edge.makeLine((1.9, 35.50000000000001, 0.0), (1.9, 35.0, 0.0))

profile_edge_5 = cq.Edge.makeLine((3.0, -2.0, 0.0), (3.0, 0.0, 0.0))

profile_edge_6 = cq.Edge.makeLine((2.0, 35.0, 0.0), (2.0, 0.0, 0.0))

profile_edge_7 = cq.Edge.makeLine((2.0, 0.0, 0.0), (3.0, 0.0, 0.0))

profile_edge_8 = cq.Edge.makeLine((0.0, -2.5, 0.0), (2.5000000000000093, -2.5, 0.0))

profile_edge_9 = cq.Edge.makeLine((1.9, 35.50000000000001, 0.0), (2.0, 35.50000000000001, 0.0))

profile_edge_10 = cq.Edge.makeLine((1.9, 35.0, 0.0), (2.0, 35.0, 0.0))

profile_edge_11 = cq.Edge.makeLine((0.0, 37.0, 0.0), (1.7000000000000002, 37.0, 0.0))

profile_edge_12 = cq.Edge.makeLine((0.0, -2.5, 0.0), (0.0, 37.0, 0.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8, profile_edge_9, profile_edge_10, profile_edge_11, profile_edge_12])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
