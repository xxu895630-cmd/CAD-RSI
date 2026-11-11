import cadquery as cq

axis_start = (0.0, 0.0, 3.3)

axis_end = (0.0, 0.0, 2.3)

profile_edge_1 = cq.Edge.makeThreePointArc((17.87575616664925, 0.0, 3.0), (17.728029098618208, 0.0, 3.0388932912180313), (17.618605976438612, 0.0, 3.1454885775269883))

profile_edge_2 = cq.Edge.makeThreePointArc((21.0, 0.0, 3.299999999999997), (20.912132034355963, 0.0, 3.087867965644033), (20.7, 0.0, 3.0))

profile_edge_3 = cq.Edge.makeThreePointArc((13.5, 0.0, 10.831973632179544), (13.60910864037413, 0.0, 10.03025850394478), (13.928498097893659, 0.0, 9.286859407449388))

profile_edge_4 = cq.Edge.makeLine((13.928498097893659, 0.0, 9.28685940744939), (17.618605976438616, 0.0, 3.1454885775269865))

profile_edge_5 = cq.Edge.makeLine((13.5, 0.0, 10.831973632179542), (13.5, 0.0, 15.0))

profile_edge_6 = cq.Edge.makeLine((21.0, 0.0, 23.0), (21.0, 0.0, 3.3))

profile_edge_7 = cq.Edge.makeLine((5.767949192431114, 0.0, 29.0), (7.5, 0.0, 28.0))

profile_edge_8 = cq.Edge.makeLine((7.5, 0.0, 28.0), (7.5, 0.0, 23.0))

profile_edge_9 = cq.Edge.makeLine((2.4999999999999973, 0.0, 15.0), (2.4999999999999973, 0.0, 29.0))

profile_edge_10 = cq.Edge.makeLine((2.4999999999999973, 0.0, 15.0), (13.5, 0.0, 15.0))

profile_edge_11 = cq.Edge.makeLine((7.5, 0.0, 23.0), (21.0, 0.0, 23.0))

profile_edge_12 = cq.Edge.makeLine((2.4999999999999982, 0.0, 29.0), (5.767949192431114, 0.0, 29.0))

profile_edge_13 = cq.Edge.makeLine((17.87575616664925, 0.0, 3.0), (20.7, 0.0, 3.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8, profile_edge_9, profile_edge_10, profile_edge_11, profile_edge_12, profile_edge_13])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
