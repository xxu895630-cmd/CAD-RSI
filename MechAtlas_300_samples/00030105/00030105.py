import cadquery as cq

axis_start = (0.0, 0.0, 10.5)

axis_end = (0.0, 0.0, 9.5)

profile_edge_1 = cq.Edge.makeLine((2.0, 0.0, 10.3), (2.0, 0.0, -10.3))

profile_edge_2 = cq.Edge.makeLine((1.7999999999999892, 0.0, -10.50000000000001), (2.0, 0.0, -10.3))

profile_edge_3 = cq.Edge.makeLine((1.80000000000001, 0.0, 10.5), (2.0, 0.0, 10.300000000000006))

profile_edge_4 = cq.Edge.makeLine((0.0, 0.0, -10.5), (1.79999999999998, 0.0, -10.5))

profile_edge_5 = cq.Edge.makeLine((0.0, 0.0, 10.5), (1.80000000000001, 0.0, 10.5))

profile_edge_6 = cq.Edge.makeLine((0.0, 0.0, -10.5), (0.0, 0.0, 10.5))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
