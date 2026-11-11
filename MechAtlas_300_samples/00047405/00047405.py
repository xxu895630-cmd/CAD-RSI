import cadquery as cq

axis_start = (9.499999999999998, 0.0, 0.0)

axis_end = (8.499999999999998, 0.0, 0.0)

profile_edge_1 = cq.Edge.makeLine((10.0, 7.500000000000002, 0.0), (9.499999999999998, 8.0, 0.0))

profile_edge_2 = cq.Edge.makeLine((18.0, 5.499999999999992, 0.0), (17.499999999999996, 6.0, 0.0))

profile_edge_3 = cq.Edge.makeLine((0.5, 4.5, 0.0), (0.0, 5.0, 0.0))

profile_edge_4 = cq.Edge.makeLine((5.0, 4.5, 0.0), (0.5, 4.5, 0.0))

profile_edge_5 = cq.Edge.makeLine((8.0, 2.499999999999998, 0.0), (18.0, 2.499999999999998, 0.0))

profile_edge_6 = cq.Edge.makeLine((6.497848452431095, 0.0, 0.0), (8.0, 2.4999999999999973, 0.0))

profile_edge_7 = cq.Edge.makeLine((17.499999999999996, 6.0, 0.0), (10.0, 6.0, 0.0))

profile_edge_8 = cq.Edge.makeLine((9.499999999999998, 8.0, 0.0), (0.0, 8.0, 0.0))

profile_edge_9 = cq.Edge.makeLine((0.0, 5.0, 0.0), (0.0, 8.0, 0.0))

profile_edge_10 = cq.Edge.makeLine((10.0, 6.0, 0.0), (10.0, 7.500000000000002, 0.0))

profile_edge_11 = cq.Edge.makeLine((18.0, 2.499999999999998, 0.0), (18.0, 5.499999999999995, 0.0))

profile_edge_12 = cq.Edge.makeLine((5.0, 0.0, 0.0), (5.0, 4.5, 0.0))

profile_edge_13 = cq.Edge.makeLine((6.497848452431095, 0.0, 0.0), (5.0, 0.0, 0.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8, profile_edge_9, profile_edge_10, profile_edge_11, profile_edge_12, profile_edge_13])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
