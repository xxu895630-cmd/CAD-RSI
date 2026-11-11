import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, -3.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, -1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-100.0, 20.0)
    .lineTo(-100.0, -20.0)
    .lineTo(100.0, -20.0)
    .lineTo(100.0, 20.0)
    .lineTo(-100.0, 20.0)
    .close().val())

opening_1 = cq.Workplane(profile_plane).center(90.0, -14.0).circle(1.621).val()

opening_2 = cq.Workplane(profile_plane).center(50.0, 14.0).circle(1.621).val()

opening_3 = cq.Workplane(profile_plane).center(90.0, 14.0).circle(1.621).val()

opening_4 = cq.Workplane(profile_plane).center(50.0, -14.0).circle(1.621).val()

opening_5 = (cq.Workplane(profile_plane).moveTo(-93.3, -11.3)
    .lineTo(3.2999999999999545, -11.300000000000008)
    .threePointArc((5.0, -13.0), (3.2999999999999603, -14.7))
    .lineTo(-93.3, -14.7)
    .threePointArc((-95.0, -13.0), (-93.3, -11.3))
    .close().val())

opening_6 = (cq.Workplane(profile_plane).moveTo(-93.3, 11.3)
    .threePointArc((-95.0, 13.0), (-93.3, 14.7))
    .lineTo(3.2999999999999545, 14.699999999999992)
    .threePointArc((5.0, 13.0), (3.2999999999999603, 11.3))
    .lineTo(-93.3, 11.3)
    .close().val())

extrusion_vector = (0.0, 0.0, 3.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2, opening_3, opening_4, opening_5, opening_6], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
