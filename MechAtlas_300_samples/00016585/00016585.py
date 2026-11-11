import cadquery as cq

axis_start = (0.0, 22.0, 0.0)

axis_end = (0.0, 23.0, 0.0)

profile_edge_1 = cq.Edge.makeThreePointArc((33.0, 23.0, 0.0), (32.29289321881346, 22.707106781186546, 0.0), (32.0, 22.0, 0.0))

profile_edge_2 = cq.Edge.makeThreePointArc((35.0, 22.0, 0.0), (34.70710678118655, 22.707106781186546, 0.0), (34.0, 23.0, 0.0))

profile_edge_3 = cq.Edge.makeLine((11.250000000000002, 0.0, 0.0), (11.250000000000002, 3.0, 0.0))

profile_edge_4 = cq.Edge.makeLine((32.0, 22.0, 0.0), (32.0, 3.0, 0.0))

profile_edge_5 = cq.Edge.makeLine((35.0, 22.0, 0.0), (35.0, 0.0, 0.0))

profile_edge_6 = cq.Edge.makeLine((33.0, 23.0, 0.0), (34.0, 23.0, 0.0))

profile_edge_7 = cq.Edge.makeLine((11.250000000000002, 0.0, 0.0), (35.0, 0.0, 0.0))

profile_edge_8 = cq.Edge.makeLine((11.250000000000002, 3.0, 0.0), (32.0, 3.0, 0.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
