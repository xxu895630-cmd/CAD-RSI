import cadquery as cq

axis_start = (0.0, 0.0, 3.55)

axis_end = (0.0, 0.0, 2.55)

profile_edge_1 = cq.Edge.makeLine((0.9500000000000003, 0.0, 3.55), (1.0500000000000003, 0.0, 3.4499999999999997))

profile_edge_2 = cq.Edge.makeLine((0.9499999999999995, 0.0, 2.55), (1.05, 0.0, 2.6499999999999995))

profile_edge_3 = cq.Edge.makeLine((1.05, 0.0, 3.4499999999999997), (1.05, 0.0, 2.6499999999999995))

profile_edge_4 = cq.Edge.makeLine((0.7500000000000001, 0.0, 2.55), (0.7500000000000001, 0.0, 0.0))

profile_edge_5 = cq.Edge.makeLine((0.0, 0.0, 0.0), (0.7500000000000001, 0.0, 0.0))

profile_edge_6 = cq.Edge.makeLine((0.0, 0.0, 3.55), (0.9500000000000003, 0.0, 3.55))

profile_edge_7 = cq.Edge.makeLine((0.7500000000000001, 0.0, 2.55), (0.9499999999999995, 0.0, 2.55))

profile_edge_8 = cq.Edge.makeLine((0.0, 0.0, 0.0), (0.0, 0.0, 3.55))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
