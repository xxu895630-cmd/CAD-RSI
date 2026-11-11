import cadquery as cq

axis_start = (0.0, 9.0, 0.0)

axis_end = (0.0, 10.0, 0.0)

profile_edge_1 = cq.Edge.makeLine((2.15, 6.699999999999999, 0.0), (2.15, 9.0, 0.0))

profile_edge_2 = cq.Edge.makeLine((1.1999999999999993, 0.0, 0.0), (1.1999999999999993, 6.699999999999999, 0.0))

profile_edge_3 = cq.Edge.makeThreePointArc((3.2500000000000004, 8.499999999999998, 0.0), (3.1035533905932744, 8.853553390593271, 0.0), (2.7500000000000004, 9.0, 0.0))

profile_edge_4 = cq.Edge.makeLine((3.2500000000000004, 8.499999999999998, 0.0), (3.2500000000000004, 0.0, 0.0))

profile_edge_5 = cq.Edge.makeLine((2.15, 9.0, 0.0), (2.7500000000000004, 9.0, 0.0))

profile_edge_6 = cq.Edge.makeLine((1.1999999999999975, 0.0, 0.0), (3.2500000000000004, 0.0, 0.0))

profile_edge_7 = cq.Edge.makeLine((1.200000000000001, 6.699999999999999, 0.0), (2.15, 6.699999999999999, 0.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
