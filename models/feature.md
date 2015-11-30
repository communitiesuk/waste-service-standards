---
layout: doc
title: Feature
model: waste_container
---

# Feature

## Use cases and requirements

The Feature model should have properties for:

**feature type**

> For the common properties of the feature.

**serial number or ID**

> For identification of the feature.

**barcode, RFID number**

> If the feature has been tagged with a barcode or RFID chip.

**UPRN**

> To link to its property.

**status**

> Capture whether in-use, damaged, etc.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
id | string | Unique identifer.
type | [Feature type](feature-type.html) | The type of feature.
barcode | integer | A barcode number.
RFID | integer | A RFID tag number.
status | string | The status of the feature.


## Serialisation

{% include serialisation.html %}


## Codelists

### Status

* in use
* damaged

