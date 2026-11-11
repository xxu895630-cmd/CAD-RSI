import cadquery as cq

profile_plane = cq.Plane(origin=(22.0, 0.0, -72.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, -1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(-44.0, 0.0)
    .threePointArc((-22.0, -22.0), (0.0, 0.0))
    .threePointArc((-22.0, 22.0), (-44.0, 0.0))
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(-7.536291501015247, -11.313708498984758)
    .threePointArc((-10.686291501015246, -14.463708498984756), (-13.836291501015245, -11.313708498984758))
    .threePointArc((-10.686291501015246, -8.163708498984759), (-7.536291501015247, -11.313708498984758))
    .close().val())

opening_2 = (cq.Workplane(profile_plane).moveTo(-30.163708498984764, -11.313708498984758)
    .threePointArc((-33.31370849898476, -14.463708498984756), (-36.46370849898476, -11.313708498984758))
    .threePointArc((-33.31370849898476, -8.163708498984759), (-30.16370849898476, -11.313708498984758))
    .close().val())

opening_3 = (cq.Workplane(profile_plane).moveTo(-30.163708498984764, 11.313708498984758)
    .threePointArc((-33.31370849898476, 8.163708498984759), (-36.46370849898476, 11.313708498984758))
    .threePointArc((-33.31370849898476, 14.463708498984756), (-30.16370849898476, 11.313708498984758))
    .close().val())

opening_4 = (cq.Workplane(profile_plane).moveTo(-7.536291501015247, 11.313708498984758)
    .threePointArc((-10.686291501015246, 8.163708498984759), (-13.836291501015245, 11.313708498984758))
    .threePointArc((-10.686291501015246, 14.463708498984756), (-7.536291501015247, 11.313708498984758))
    .close().val())

opening_5 = (cq.Workplane(profile_plane).moveTo(-16.0, 0.0)
    .threePointArc((-22.0, -6.0), (-28.0, 0.0))
    .threePointArc((-22.0, 6.0), (-16.0, 0.0))
    .close().val())

extrusion_vector = (0.0, 0.0, 3.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2, opening_3, opening_4, opening_5], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
