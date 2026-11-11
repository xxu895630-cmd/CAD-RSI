import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 29.55), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-36.0, 7.099999999999998)
    .lineTo(-36.0, 71.6777485225821)
    .lineTo(-72.66363148130259, 71.6777485225821)
    .lineTo(-72.6636314813026, 7.099999999999999)
    .lineTo(-36.0, 7.1)
    .close().val())

extrusion_vector = (0.0, 0.0, -0.20000000021569875)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
