import cadquery as cq

axis_start = (0.0, 3.5, 0.0)

axis_end = (0.0, 2.5, 0.0)

profile_edge_1 = cq.Edge.makeLine((12.0, 3.5, 0.0), (12.5, 3.0, 0.0))

profile_edge_2 = cq.Edge.makeLine((6.500000000000001, 3.0, 0.0), (7.0, 3.5, 0.0))

profile_edge_3 = cq.Edge.makeLine((6.500000000000001, 0.5000000000000071, 0.0), (7.0, 0.0, 0.0))

profile_edge_4 = cq.Edge.makeLine((12.0, 0.0, 0.0), (12.5, 0.5000000000000022, 0.0))

profile_edge_5 = cq.Edge.makeLine((6.500000000000001, 3.0, 0.0), (6.500000000000001, 0.5000000000000071, 0.0))

profile_edge_6 = cq.Edge.makeLine((12.5, 3.0, 0.0), (12.5, 0.5000000000000022, 0.0))

profile_edge_7 = cq.Edge.makeLine((7.0, 3.5, 0.0), (12.0, 3.5, 0.0))

profile_edge_8 = cq.Edge.makeLine((7.0, 0.0, 0.0), (12.0, 0.0, 0.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
