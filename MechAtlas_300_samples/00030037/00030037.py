import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 2.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = cq.Workplane(profile_plane).center(0.0, 0.0).circle(6.5).val()

opening_1 = cq.Workplane(profile_plane).center(0.0, 0.0).circle(4.5).val()

extrusion_vector = (0.0, 0.0, -2.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
