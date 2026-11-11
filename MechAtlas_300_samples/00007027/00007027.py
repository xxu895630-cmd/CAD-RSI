import cadquery as cq

axis_start = (0.0, 0.0, 0.0)

axis_end = (-1.0, 0.0, 0.0)

profile_edge_1 = cq.Edge.makeThreePointArc((0.0, 0.75, 0.0), (-0.25000000000000006, 0.5, 0.0), (0.0, 0.24999999999999994, 0.0))

profile_edge_2 = cq.Edge.makeThreePointArc((0.0, 0.24999999999999994, 0.0), (0.25000000000000006, 0.49999999999999994, 0.0), (0.0, 0.75, 0.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
