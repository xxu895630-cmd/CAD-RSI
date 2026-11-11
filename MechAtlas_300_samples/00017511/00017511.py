import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 12.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-218.5, -55.0)
    .lineTo(218.49999999999994, -55.0)
    .lineTo(223.49999999999997, -50.0)
    .lineTo(223.5, 50.0)
    .lineTo(218.50000000000003, 55.0)
    .lineTo(-218.49999999999994, 55.0)
    .lineTo(-223.49999999999997, 50.0)
    .lineTo(-223.5, -50.0)
    .lineTo(-218.50000000000003, -55.0)
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(-26.500000000000036, 10.0)
    .threePointArc((-24.0, 12.500000000000021), (-21.500000000000007, 10.0))
    .threePointArc((-24.0, 7.4999999999999964), (-26.500000000000036, 10.0))
    .close().val())

opening_2 = (cq.Workplane(profile_plane).moveTo(-26.500000000000043, -35.0)
    .threePointArc((-24.0, -32.49999999999998), (-21.500000000000014, -35.0))
    .threePointArc((-24.0, -37.50000000000001), (-26.500000000000043, -35.0))
    .close().val())

opening_3 = (cq.Workplane(profile_plane).moveTo(-1.6500000000000066, 45.0)
    .threePointArc((0.0, 46.650000000000006), (1.6499999999999702, 45.0))
    .threePointArc((0.0, 43.35000000000002), (-1.6500000000000066, 45.0))
    .close().val())

opening_4 = (cq.Workplane(profile_plane).moveTo(-1.649999999999984, 10.0)
    .threePointArc((0.0, 11.649999999999968), (1.6499999999999926, 10.0))
    .threePointArc((0.0, 8.349999999999993), (-1.6499999999999841, 10.0))
    .close().val())

opening_5 = (cq.Workplane(profile_plane).moveTo(-1.6500000000000175, -35.0)
    .threePointArc((0.0, -33.35), (1.649999999999959, -35.0))
    .threePointArc((0.0, -36.649999999999984), (-1.6500000000000177, -35.0))
    .close().val())

opening_6 = (cq.Workplane(profile_plane).moveTo(-57.0, 43.0)
    .threePointArc((-54.50000000000002, 45.50000000000006), (-52.0, 43.0))
    .threePointArc((-54.50000000000002, 40.50000000000007), (-57.0, 43.0))
    .close().val())

opening_7 = (cq.Workplane(profile_plane).moveTo(-69.0, 43.0)
    .threePointArc((-66.50000000000003, 45.500000000000064), (-64.0, 43.0))
    .threePointArc((-66.50000000000003, 40.500000000000064), (-69.0, 43.0))
    .close().val())

opening_8 = (cq.Workplane(profile_plane).moveTo(187.5, 37.0)
    .threePointArc((190.0, 39.50000000000014), (192.5, 37.0))
    .threePointArc((190.0, 34.50000000000014), (187.5, 37.0))
    .close().val())

opening_9 = (cq.Workplane(profile_plane).moveTo(187.5, -33.0)
    .threePointArc((190.0, -30.499999999999805), (192.5, -33.0))
    .threePointArc((190.0, -35.49999999999981), (187.5, -33.0))
    .close().val())

opening_10 = (cq.Workplane(profile_plane).moveTo(-192.5, -33.0)
    .threePointArc((-190.0, -30.499999999999805), (-187.5, -33.0))
    .threePointArc((-190.0, -35.49999999999981), (-192.5, -33.0))
    .close().val())

opening_11 = (cq.Workplane(profile_plane).moveTo(160.5, -33.0)
    .threePointArc((163.0, -30.499999999999982), (165.5, -33.0))
    .threePointArc((163.0, -35.499999999999986), (160.5, -33.0))
    .close().val())

opening_12 = (cq.Workplane(profile_plane).moveTo(214.5, -33.0)
    .threePointArc((217.0, -30.499999999999982), (219.5, -33.0))
    .threePointArc((217.0, -35.499999999999986), (214.5, -33.0))
    .close().val())

opening_13 = (cq.Workplane(profile_plane).moveTo(160.5, 37.0)
    .threePointArc((163.0, 39.49999999999985), (165.5, 37.0))
    .threePointArc((163.0, 34.49999999999985), (160.5, 37.0))
    .close().val())

opening_14 = (cq.Workplane(profile_plane).moveTo(214.5, 37.0)
    .threePointArc((217.0, 39.49999999999985), (219.5, 37.0))
    .threePointArc((217.0, 34.49999999999985), (214.5, 37.0))
    .close().val())

opening_15 = (cq.Workplane(profile_plane).moveTo(-165.5, 37.0)
    .threePointArc((-163.0, 39.49999999999985), (-160.5, 37.0))
    .threePointArc((-163.0, 34.49999999999985), (-165.5, 37.0))
    .close().val())

opening_16 = (cq.Workplane(profile_plane).moveTo(-219.5, 37.0)
    .threePointArc((-217.0, 39.49999999999986), (-214.5, 37.0))
    .threePointArc((-217.0, 34.49999999999986), (-219.5, 37.0))
    .close().val())

opening_17 = (cq.Workplane(profile_plane).moveTo(-165.5, -33.0)
    .threePointArc((-163.0, -30.499999999999982), (-160.5, -33.0))
    .threePointArc((-163.0, -35.499999999999986), (-165.5, -33.0))
    .close().val())

opening_18 = (cq.Workplane(profile_plane).moveTo(-219.5, -33.0)
    .threePointArc((-217.0, -30.499999999999982), (-214.5, -33.0))
    .threePointArc((-217.0, -35.499999999999986), (-219.5, -33.0))
    .close().val())

opening_19 = (cq.Workplane(profile_plane).moveTo(-192.5, 37.0)
    .threePointArc((-190.0, 39.50000000000014), (-187.5, 37.0))
    .threePointArc((-190.0, 34.50000000000014), (-192.5, 37.0))
    .close().val())

extrusion_vector = (0.0, 0.0, -12.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2, opening_3, opening_4, opening_5, opening_6, opening_7, opening_8, opening_9, opening_10, opening_11, opening_12, opening_13, opening_14, opening_15, opening_16, opening_17, opening_18, opening_19], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
