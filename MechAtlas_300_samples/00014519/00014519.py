import cadquery as cq

axis_start = (0.0, 0.8660254037844383, 0.0)

axis_end = (0.0, -0.13397459621556174, 0.0)

profile_edge_1 = cq.Edge.makeLine((3.0, 0.8660254037844383, 0.0), (3.4999999999999996, 0.0, 0.0))

profile_edge_2 = cq.Edge.makeLine((5.0500000000000025, 7.5, 0.0), (5.25, 7.300000000000003, 0.0))

profile_edge_3 = cq.Edge.makeLine((6.699999999999999, 0.0, 0.0), (6.900000000000001, 0.20000000000000107, 0.0))

profile_edge_4 = cq.Edge.makeLine((6.700000000000005, 2.0, 0.0), (6.900000000000001, 1.8000000000000034, 0.0))

profile_edge_5 = cq.Edge.makeLine((5.25, 7.300000000000003, 0.0), (5.25, 2.0, 0.0))

profile_edge_6 = cq.Edge.makeLine((6.900000000000001, 1.8000000000000034, 0.0), (6.900000000000001, 0.20000000000000118, 0.0))

profile_edge_7 = cq.Edge.makeLine((3.0, 7.5, 0.0), (3.0, 0.8660254037844383, 0.0))

profile_edge_8 = cq.Edge.makeLine((3.4999999999999996, 0.0, 0.0), (6.699999999999999, 0.0, 0.0))

profile_edge_9 = cq.Edge.makeLine((5.25, 2.0, 0.0), (6.700000000000005, 2.0, 0.0))

profile_edge_10 = cq.Edge.makeLine((3.0, 7.5, 0.0), (5.0500000000000025, 7.5, 0.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8, profile_edge_9, profile_edge_10])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
