import cadquery as cq

profile_plane = cq.Plane(origin=(0.0, 0.0, 1.0), xDir=(1.0, 0.0, 0.0), normal=(0.0, 0.0, 1.0))

outer_profile = (cq.Workplane(profile_plane).moveTo(0.0, 197.0)
    .lineTo(0.0, 3.0)
    .threePointArc((0.8786796564403572, 0.8786796564403572), (3.0, 0.0))
    .lineTo(187.0, 0.0)
    .threePointArc((189.12132034355966, 0.8786796564403554), (190.0, 3.0))
    .lineTo(190.0, 197.0)
    .threePointArc((189.12132034355966, 199.12132034355963), (187.0, 200.0))
    .lineTo(3.0, 200.0)
    .threePointArc((0.8786796564403581, 199.12132034355963), (0.0, 197.0))
    .close().val())

opening_1 = (cq.Workplane(profile_plane).moveTo(157.10000000000002, 15.0)
    .threePointArc((155.0, 12.900000000000011), (152.90000000000003, 15.0))
    .lineTo(152.90000000000003, 95.0)
    .threePointArc((155.0, 97.1), (157.10000000000002, 95.0))
    .lineTo(157.10000000000002, 15.0)
    .close().val())

opening_2 = (cq.Workplane(profile_plane).moveTo(37.1, 15.0)
    .threePointArc((35.0, 12.900000000000004), (32.900000000000006, 15.0))
    .lineTo(32.900000000000006, 89.86045234318847)
    .threePointArc((35.0, 91.96045234318846), (37.099999999999994, 89.86045234318847))
    .lineTo(37.1, 15.0)
    .close().val())

extrusion_vector = (0.0, 0.0, -1.0)

solid = cq.Solid.extrudeLinear(outer_profile, [opening_1, opening_2], cq.Vector(*extrusion_vector))

result = cq.Workplane().newObject([solid])
