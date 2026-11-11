import cadquery as cq

axis_start = (-114.0, 4.99999999999789, 0.0)

axis_end = (-113.0, 4.99999999999789, 0.0)

profile_edge_1 = cq.Edge.makeThreePointArc((-115.0, 16.49999999999789, 0.0), (-114.70710678118655, 17.207106781184436, 0.0), (-114.0, 17.49999999999789, 0.0))

profile_edge_2 = cq.Edge.makeLine((-100.0, 17.49999999999789, 0.0), (-114.0, 17.49999999999789, 0.0))

profile_edge_3 = cq.Edge.makeThreePointArc((-114.5, 12.99999999999789, 0.0), (-114.85355339059328, 13.146446609404615, 0.0), (-115.0, 13.49999999999789, 0.0))

profile_edge_4 = cq.Edge.makeThreePointArc((-108.0, 12.49999999999789, 0.0), (-108.14644660940672, 12.853553390591163, 0.0), (-108.5, 12.99999999999789, 0.0))

profile_edge_5 = cq.Edge.makeLine((-108.5, 12.99999999999789, 0.0), (-114.5, 12.99999999999789, 0.0))

profile_edge_6 = cq.Edge.makeLine((-108.0, 7.74999999999789, 0.0), (-100.0, 7.74999999999789, 0.0))

profile_edge_7 = cq.Edge.makeLine((-100.0, 7.74999999999789, 0.0), (-100.0, 17.49999999999789, 0.0))

profile_edge_8 = cq.Edge.makeLine((-115.0, 13.49999999999789, 0.0), (-115.0, 16.49999999999789, 0.0))

profile_edge_9 = cq.Edge.makeLine((-108.0, 7.74999999999789, 0.0), (-108.0, 12.49999999999789, 0.0))

profile = cq.Wire.assembleEdges([profile_edge_1, profile_edge_2, profile_edge_3, profile_edge_4, profile_edge_5, profile_edge_6, profile_edge_7, profile_edge_8, profile_edge_9])

solid = cq.Solid.revolve(profile, [], 360.0, axis_start, axis_end)

result = cq.Workplane().newObject([solid])
