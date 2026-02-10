# Update Attributes by Location (ArcGIS Pro)

A custom ArcGIS Pro geoprocessing tool that updates feature attributes **in place**
based on a spatial relationship with another layer.

This tool behaves similarly to a Spatial Join, but **without creating a new feature class**.

---

## Key Features

- Updates the **existing target feature class**
- Supports **multiple fields** transfer
- Automatically **creates missing fields**
- Preserves **field aliases**
- Respects **feature selections**

---

## Typical Use Case

- Assigning administrative zone attributes to buildings
- Updating parcel attributes from planning boundaries
- Transfer population and location names from points to areas or districts
- Government workflows requiring **data integrity** without duplication


---

## Requirements

- ArcGIS Pro 2.9+

---

## Installation

1. Clone this repository
2. Open ArcGIS Pro
3. Add the toolbox (`.atbx`)
4. Run the tool from the Geoprocessing pane

---

## Notes

- For very large datasets, Spatial Join may be faster
- This tool is intended for **controlled, in-place updates**
- Always test on a copy of your data

---
## Drive Link

You can also download from here `https://drive.google.com/file/d/11wVVcmQOnS8_FRBx0ink8gI2tjGVhbwg/view?usp=sharing`


