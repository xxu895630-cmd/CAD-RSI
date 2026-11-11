import cadquery as cq

axis_start = (0.0, -108.64897028505132, 0.0)

axis_end = (0.0, -109.64897028505132, 0.0)

profile_edge_1 = cq.Edge.makeThreePointArc((0.6396203899719666, -108.14897028505132, 0.0), (0.9319755323038462, -108.24334919246354, 0.0), (1.1139620389972213, -108.4908564020429, 0.0))

profile_edge_2 = cq.Edge.makeLine((3.0, -119.6489702850513, 0.0), (4.0, -120.64897028505132, 0.0))

profile_edge_3 = cq.Edge.makeLine((3.5000000000000453, -122.6489702850513, 0.0), (4.0, -122.14897028505132, 0.0))

profile_edge_4 = cq.Edge.makeLine((1.1139620389972213, -108.4908564020429, 0.0), (2.0, -111.1489702850513, 0.0))

profile_edge_5 = cq.Edge.makeLine((2.0, -119.64897028505132, 0.0), (2.0, -111.1489702850513, 0.0))

profile_edge_6 = cq.Edge.makeLine((4.0, -122.14897028505133, 0.0), (4.0, -120.64897028505132, 0.0))

profile_edge_7 = cq.Edge.makeLine((0.0, -122.6489702850513, 0.0), (3.500000000000045, -122.6489702850513, 0.0))

profile_edge_8 = cq.Edge.makeLine((2.0, -119.6489702850513, 0.0), (3.0, -119.6489702850513, 0.0))

profile_edge_9 = cq.Edge.makeLine((0.0, -108.14897028505132, 0.0), (0.6396203899719667, -108.14897028505132, 0.0))

profile_edge_10 = cq.Edge.makeLine((0.0, -122.6489702850513, 0.0), (0.0, -108.14897028505132, 0.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8, profile_edge_9, profile_edge_10])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
