import cadquery as cq

axis_start = (0.0, 0.0, 7.5)

axis_end = (0.0, 0.0, 6.5)

profile_edge_1 = cq.Edge.makeLine((7.5000000000000036, 0.0, 7.5), (8.0, 0.0, 7.0))

profile_edge_2 = cq.Edge.makeLine((7.499999999999995, 0.0, -7.499999999999998), (8.0, 0.0, -7.0))

profile_edge_3 = cq.Edge.makeLine((2.499999999999998, 0.0, -3.5), (2.499999999999998, 0.0, 7.5))

profile_edge_4 = cq.Edge.makeLine((0.0, 0.0, -5.002151547568904), (2.499999999999997, 0.0, -3.5))

profile_edge_5 = cq.Edge.makeLine((8.0, 0.0, 7.0), (8.0, 0.0, -7.0))

profile_edge_6 = cq.Edge.makeLine((2.4999999999999982, 0.0, 7.5), (7.5000000000000036, 0.0, 7.5))

profile_edge_7 = cq.Edge.makeLine((0.0, 0.0, -7.5), (7.499999999999995, 0.0, -7.5))

profile_edge_8 = cq.Edge.makeLine((0.0, 0.0, -5.002151547568904), (0.0, 0.0, -7.5))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
