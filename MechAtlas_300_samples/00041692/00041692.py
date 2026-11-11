import cadquery as cq

axis_start = (0.0, -6.5, 0.0)

axis_end = (0.0, -5.5, 0.0)

profile_edge_1 = cq.Edge.makeLine((20.0, -6.3, 0.0), (20.0, -0.20000000000000018, 0.0))

profile_edge_2 = cq.Edge.makeLine((23.5, -6.3, 0.0), (23.5, -0.20000000000000018, 0.0))

profile_edge_3 = cq.Edge.makeThreePointArc((20.0, -6.3, 0.0), (20.05857864376269, -6.441421356237309, 0.0), (20.2, -6.5, 0.0))

profile_edge_4 = cq.Edge.makeThreePointArc((20.2, 0.0, 0.0), (20.05857864376269, -0.058578643762690064, 0.0), (20.0, -0.20000000000000018, 0.0))

profile_edge_5 = cq.Edge.makeLine((23.3, -6.5, 0.0), (23.5, -6.3, 0.0))

profile_edge_6 = cq.Edge.makeLine((23.3, 0.0, 0.0), (23.5, -0.20000000000000018, 0.0))

profile_edge_7 = cq.Edge.makeLine((20.2, -6.5, 0.0), (23.3, -6.5, 0.0))

profile_edge_8 = cq.Edge.makeLine((20.2, 0.0, 0.0), (23.3, 0.0, 0.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
