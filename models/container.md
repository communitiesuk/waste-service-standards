---
layout: doc
title: Container
model: container
---

# Container

## Use cases and requirements

The Container model should have properties for:

**container type**

> For the common properties of the container.

**serial number or ID**

> For identification of the container.

**barcode, RFID number**

> If the container has been tagged with a barcode or RFID chip.

**UPRN**

> To link to its property.

**status**

> Capture whether in-use, damaged, etc.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
id | string | Unique identifer.
type | [Container type](container-type.md) | The type of container.
barcode | integer | A barcode number.
RFID | integer | A RFID tag number.
status | string | The status of the container.


## Serialisation

{% include serialisation.html %}


## Codelists

### Status

* in service
* damaged




