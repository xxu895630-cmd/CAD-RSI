import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, -5.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, -1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(340.0, -302.5)
    .lineTo(340.0, 302.5)
    .lineTo(-340.0, 302.5000000000001)
    .lineTo(-340.0, -302.5)
    .lineTo(340.0, -302.4999999999999)
    .close().val())

extrusion_vector = (0.0, 0.0, 5.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
