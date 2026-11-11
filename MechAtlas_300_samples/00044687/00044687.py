import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, -1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(55.68, 20.0)
    .lineTo(-55.68, 20.0)
    .threePointArc((-57.09421356237309, 19.414213562373096), (-57.68, 18.0))
    .lineTo(-57.68, -18.0)
    .threePointArc((-57.09421356237309, -19.414213562373096), (-55.68, -20.0))
    .lineTo(-28.000000000009, -20.0)
    .threePointArc((-26.585786437635903, -19.414213562373096), (-26.000000000009, -18.0))
    .lineTo(-26.000000000009, -7.5)
    .threePointArc((-22.500000000009, -4.0), (-19.000000000009, -7.5))
    .lineTo(-19.000000000008995, -18.0)
    .threePointArc((-18.414213562382095, -19.414213562373096), (-17.000000000009, -20.0))
    .lineTo(17.000000000009003, -20.0)
    .threePointArc((18.414213562382095, -19.414213562373096), (19.000000000009, -18.0))
    .lineTo(19.000000000009, -7.5)
    .threePointArc((22.500000000009, -4.0), (26.000000000009, -7.5))
    .lineTo(26.000000000009003, -18.0)
    .threePointArc((26.585786437635903, -19.414213562373096), (28.000000000009, -20.0))
    .lineTo(55.68, -20.0)
    .threePointArc((57.09421356237309, -19.414213562373096), (57.68, -18.0))
    .lineTo(57.68, 18.0)
    .threePointArc((57.09421356237309, 19.414213562373096), (55.68, 20.0))
    .close().val())

opening_1 = cq.Workplane(profile_plane).center(-33.500000000009, 8.71).circle(3.325).val()

opening_2 = cq.Workplane(profile_plane).center(33.500000000009, 8.71).circle(3.325).val()

extrusion_vector = (0.0, 3.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
