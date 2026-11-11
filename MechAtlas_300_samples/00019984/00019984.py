import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 5.0, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(0.0, 0.0)
    .lineTo(-611.0, 0.0)
    .lineTo(-611.0, -508.0)
    .lineTo(0.0, -508.0)
    .lineTo(0.0, 0.0)
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(-9.999999999994886, -501.49999999999994)
    .threePointArc((-13.499999999994834, -498.0), (-9.999999999994886, -494.50000000000006))
    .threePointArc((-6.499999999994938, -498.0), (-9.999999999994886, -501.49999999999994))
    .close().val())

opening_2 = (cq.Workplane(profile_plane).moveTo(-600.9999999999949, -501.50000000000404)
    .threePointArc((-604.4999999999949, -498.0000000000041), (-600.9999999999949, -494.50000000000415))
    .threePointArc((-597.4999999999949, -498.0000000000041), (-600.9999999999949, -501.50000000000404))
    .close().val())

opening_3 = (cq.Workplane(profile_plane).moveTo(-601.0, -13.500000000004096)
    .threePointArc((-604.5, -10.000000000004128), (-601.0, -6.500000000004162))
    .threePointArc((-597.5, -10.000000000004128), (-601.0, -13.500000000004095))
    .close().val())

opening_4 = (cq.Workplane(profile_plane).moveTo(-10.0, -13.500000000000002)
    .threePointArc((-13.499999999999998, -10.0), (-10.0, -6.500000000000002))
    .threePointArc((-6.499999999999998, -10.0), (-10.0, -13.500000000000002))
    .close().val())

extrusion_vector = (0.0, -5.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2, opening_3, opening_4], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
