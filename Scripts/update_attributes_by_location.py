import arcpy
source_fc = arcpy.GetParameterAsText(0)
target_fc = arcpy.GetParameterAsText(1)
transfer_fields= arcpy.GetParameterAsText(2).split(";")

source_geom_type = arcpy.Describe(source_fc).shapeType

fields_info = [
    (f.name , f.aliasName , f.type)
    for f in arcpy.ListFields(source_fc)
    if f.name in transfer_fields
]

target_fc_fields = [f.name for f in arcpy.ListFields(target_fc)]
for name, alias, fcType in fields_info:
    if name not in target_fc_fields:
        arcpy.AddField_management(
            target_fc,
            name,
            field_type=fcType,
            field_alias=alias
        )
        arcpy.AddMessage(f"Added field '{name}' (Alias: {alias}) with type {fcType}")

arcpy.MakeFeatureLayer_management(source_fc, "source_fc_lyr")
arcpy.MakeFeatureLayer_management(target_fc, "target_fc_lyr")


desc = arcpy.Describe("target_fc_lyr")
has_selection = desc.FIDSet not in ("", None)
if has_selection:
    arcpy.AddMessage(f"Selection detected and processing selected features only")
else:
    arcpy.AddMessage("No selection processing all features")

source_fields = ["SHAPE@"] + transfer_fields
source_features = []

with arcpy.da.SearchCursor("source_fc_lyr", source_fields) as cursor:
    for row in cursor:
        source_features.append(row)

target_fields = ["SHAPE@"] + transfer_fields
updated = 0

with arcpy.da.UpdateCursor("target_fc_lyr", target_fields) as cursor:
    for row in cursor:
        target_shape = row[0]

        for source_row in source_features:
            source_shape = source_row[0]
            match = False

            if source_geom_type.lower() == "point":
                if target_shape.contains(source_shape) or target_shape.touches(source_shape):
                    match = True
            else:
                if target_shape.overlaps(source_shape) or target_shape.within(source_shape):
                    match = True

            if match:
                for i in range(1, len(target_fields)):
                    row[i] = source_row[i]

                cursor.updateRow(row)
                updated += 1
                break

arcpy.AddMessage(f"Updated {updated} features")