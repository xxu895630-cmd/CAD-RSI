import cadquery as cq

axis_start = (0.0, 52.0, 0.0)

axis_end = (0.0, 51.0, 0.0)

profile_edge_1 = cq.Edge.makeLine((2.300000000000024, 52.0, 0.0), (2.5000000000000018, 51.80000000000001, 0.0))

profile_edge_2 = cq.Edge.makeLine((2.2999999999999754, 0.0, 0.0), (2.5, 0.20000000000001705, 0.0))

profile_edge_3 = cq.Edge.makeLine((1.800000000000003, 60.0, 0.0), (2.0, 59.800000000000004, 0.0))

profile_edge_4 = cq.Edge.makeLine((2.0, 59.800000000000004, 0.0), (2.0, 52.0, 0.0))

profile_edge_5 = cq.Edge.makeLine((2.5, 51.80000000000001, 0.0), (2.5, 0.20000000000001705, 0.0))

profile_edge_6 = cq.Edge.makeLine((2.0, 52.0, 0.0), (2.300000000000024, 52.0, 0.0))

profile_edge_7 = cq.Edge.makeLine((0.0, 0.0, 0.0), (2.2999999999999754, 0.0, 0.0))

profile_edge_8 = cq.Edge.makeLine((0.0, 60.0, 0.0), (1.800000000000003, 60.0, 0.0))

profile_edge_9 = cq.Edge.makeLine((0.0, 0.0, 0.0), (0.0, 60.0, 0.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8, profile_edge_9])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
