---
layout: doc
title: Material
model: material
---

# Material

## Use cases and requirements

The Material  model should have properties for:

**name**

> What type of material it is.

**colour**

> A colour matching the WRAP material stream, for consistent colour identification.

**image**

> For clear identification, matching physical signage.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
name | string | The name of the material.
color | [schema:color](https://schema.org/color) | The related colour.


## Serialisation

{% include serialisation.html %}




