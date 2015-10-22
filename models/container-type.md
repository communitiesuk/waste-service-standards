---
layout: doc
title: Container type
model: container_type
---

# Container type

## Use cases and requirements

The Container type model should have properties for:

**color**

> The general color.

**size**

> Typically in litres.

**shape**

> Wheelie bin, box, caddy, etc.

**lid color**

> In case its different to the body color.

**disposable**

> If the container type is disposable or one-time use, e.g. a bag.

**material stream**

> What kind of waste the container is used for.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
id |  | Unique identifer.
color | [schema:color](https://schema.org/color) | General color as a hex value.
size | integer | Size in litres.
shape | text | The shape or type of the container.
lid color | [schema:color](https://schema.org/color) | Lid-specific color as a hex value.
disposable | boolean | If container is disposable.
material | [Material](material.html) | The materials used.

## Serialisation

{% include serialisation.html %}


## Codelists

### Container shape


