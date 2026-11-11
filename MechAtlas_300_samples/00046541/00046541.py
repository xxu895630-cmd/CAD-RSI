import cadquery as cq

profile_plane = cq.Plane(origin=(2.0, 0.0, 0.0), xDir=(0.0, 1.0, 0.0), normal=(1.0, 0.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(29.0, -45.5)
    .lineTo(29.0, 45.5)
    .lineTo(27.0, 47.5)
    .lineTo(-27.0, 47.5)
    .lineTo(-29.0, 45.5)
    .lineTo(-29.0, -45.5)
    .lineTo(-27.0, -47.5)
    .lineTo(27.0, -47.5)
    .lineTo(29.0, -45.5)
    .close().val())

opening_1 = cq.Workplane(profile_plane).center(12.5, -31.0).circle(1.5).val()

opening_2 = cq.Workplane(profile_plane).center(12.5, -4.0).circle(1.5).val()

opening_3 = cq.Workplane(profile_plane).center(12.5, 23.0).circle(1.5).val()

opening_4 = cq.Workplane(profile_plane).center(-12.5, 23.0).circle(1.5).val()

opening_5 = cq.Workplane(profile_plane).center(-12.5, -4.0).circle(1.5).val()

opening_6 = cq.Workplane(profile_plane).center(-12.5, -31.0).circle(1.5).val()

opening_7 = (cq.Workplane(profile_plane).moveTo(-10.0, -25.5)
    .lineTo(10.0, -25.5)
    .lineTo(10.0, -36.5)
    .lineTo(-10.0, -36.5)
    .lineTo(-10.0, -25.5)
    .close().val())

opening_8 = (cq.Workplane(profile_plane).moveTo(-10.0, 1.5)
    .lineTo(10.0, 1.5)
    .lineTo(10.0, -9.5)
    .lineTo(-10.0, -9.5)
    .lineTo(-10.0, 1.5)
    .close().val())

opening_9 = (cq.Workplane(profile_plane).moveTo(-10.0, 28.5)
    .lineTo(10.0, 28.5)
    .lineTo(10.0, 17.5)
    .lineTo(-10.0, 17.5)
    .lineTo(-10.0, 28.5)
    .close().val())

opening_10 = cq.Workplane(profile_plane).center(24.5, 44.0).circle(1.7).val()

opening_11 = cq.Workplane(profile_plane).center(-24.5, 44.0).circle(1.7).val()

opening_12 = cq.Workplane(profile_plane).center(-24.5, -44.0).circle(1.7).val()

opening_13 = cq.Workplane(profile_plane).center(24.5, -44.0).circle(1.7).val()

extrusion_vector = (-2.0, 0.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2, opening_3, opening_4, opening_5, opening_6, opening_7, opening_8, opening_9, opening_10, opening_11, opening_12, opening_13], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
