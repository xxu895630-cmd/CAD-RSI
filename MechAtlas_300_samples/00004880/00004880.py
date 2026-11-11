import cadquery as cq

axis_start = (0.0, 8.9, 0.0)

axis_end = (0.0, 7.9, 0.0)

profile_edge_1 = cq.Edge.makeLine((5.200000000000001, 8.9, 0.0), (5.5, 8.600000000000003, 0.0))

profile_edge_2 = cq.Edge.makeLine((5.199999999999999, 0.0, 0.0), (5.5, 0.3000000000000007, 0.0))

profile_edge_3 = cq.Edge.makeThreePointArc((4.500000000000001, 8.9, 0.0), (3.43933982822018, 8.460660171779821, 0.0), (3.0, 7.4, 0.0))

profile_edge_4 = cq.Edge.makeLine((3.0, 7.4, 0.0), (3.0, 0.0, 0.0))

profile_edge_5 = cq.Edge.makeLine((5.5, 8.600000000000003, 0.0), (5.5, 0.3000000000000007, 0.0))

profile_edge_6 = cq.Edge.makeLine((4.500000000000001, 8.9, 0.0), (5.200000000000001, 8.9, 0.0))

profile_edge_7 = cq.Edge.makeLine((3.0, 0.0, 0.0), (5.199999999999999, 0.0, 0.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
