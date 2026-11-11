import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 1.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-5.5, 4.75)
    .threePointArc((-10.25, 0.0), (-5.500000000000001, -4.75))
    .lineTo(7.5, -4.75)
    .threePointArc((12.25, 0.0), (7.500000000000001, 4.75))
    .lineTo(-5.5, 4.75)
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(7.5, -2.75)
    .lineTo(-5.5, -2.75)
    .threePointArc((-8.25, 0.0), (-5.5, 2.75))
    .lineTo(7.5, 2.75)
    .threePointArc((10.25, 0.0), (7.5, -2.75))
    .close().val())

extrusion_vector = (0.0, -1.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
