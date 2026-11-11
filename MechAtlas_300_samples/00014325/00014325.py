import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, -5847.2959671363205, 0.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, -1.0, 0.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-25106.50000000001, -14791.654979470723)
    .lineTo(-25106.50000000001, -15041.654979470723)
    .lineTo(-25231.50000000001, -15041.654979470723)
    .lineTo(-25231.50000000001, -15211.654979470723)
    .lineTo(-25046.50000000001, -15211.654979470723)
    .lineTo(-25046.50000000001, -14791.654979470723)
    .lineTo(-25106.50000000001, -14791.654979470723)
    .close().val())

extrusion_vector = (0.0, 15.0, 0.0)

solid = cq.Solid.extrudeLinear(outer_profile, [], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
