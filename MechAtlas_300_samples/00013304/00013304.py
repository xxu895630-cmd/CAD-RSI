import cadquery as cq

axis_start = (0.0, 4.0, 0.0)

axis_end = (0.0, 3.0, 0.0)

profile_edge_1 = cq.Edge.makeLine((7.0, 4.0, 0.0), (7.5, 3.500000000000001, 0.0))

profile_edge_2 = cq.Edge.makeLine((7.0, 0.0, 0.0), (7.5, 0.5000000000000013, 0.0))

profile_edge_3 = cq.Edge.makeLine((7.5, 3.5000000000000013, 0.0), (7.5, 0.5000000000000013, 0.0))

profile_edge_4 = cq.Edge.makeLine((0.0, 4.0, 0.0), (7.0, 4.0, 0.0))

profile_edge_5 = cq.Edge.makeLine((0.0, 0.0, 0.0), (7.0, 0.0, 0.0))

profile_edge_6 = cq.Edge.makeLine((0.0, 4.0, 0.0), (0.0, 0.0, 0.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
