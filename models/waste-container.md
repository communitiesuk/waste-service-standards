---
layout: doc
title: Waste container
model: waste_container
---

# WasteContainer


## Types

WasteContainer derives from [Feature](feature.html).


## Properties

Term     | Mapping | Definition
---------|---------|-----------
id | string | Unique identifer.
type | [Container type](container-type.html) | The type of container.
barcode | integer | A barcode number.
RFID | integer | A RFID tag number.
status | string | The status of the container.


## Serialisation

{% include serialisation.html %}

