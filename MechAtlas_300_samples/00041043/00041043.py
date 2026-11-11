import cadquery as cq

axis_start = (0.0, -8.0, 0.0)

axis_end = (0.0, -7.0, 0.0)

profile_edge_1 = cq.Edge.makeLine((10.0, -7.5, 0.0), (10.0, -0.5, 0.0))

profile_edge_2 = cq.Edge.makeLine((3.0, -8.0, 0.0), (3.0, -4.6, 0.0))

profile_edge_3 = cq.Edge.makeLine((1.7, -4.6, 0.0), (1.7, 0.0, 0.0))

profile_edge_4 = cq.Edge.makeThreePointArc((9.5, -8.0, 0.0), (9.853553390593273, -7.853553390593274, 0.0), (10.0, -7.5, 0.0))

profile_edge_5 = cq.Edge.makeThreePointArc((10.0, -0.5, 0.0), (9.853553390593273, -0.14644660940672605, 0.0), (9.5, 0.0, 0.0))

profile_edge_6 = cq.Edge.makeLine((3.0, -8.0, 0.0), (9.5, -8.0, 0.0))

profile_edge_7 = cq.Edge.makeLine((1.7, 0.0, 0.0), (9.5, 0.0, 0.0))

profile_edge_8 = cq.Edge.makeLine((1.7, -4.6, 0.0), (3.0, -4.6, 0.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
