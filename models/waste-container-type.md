---
layout: doc
title: Waste container type
model: waste_container_type
---

# Waste container type

## Use cases and requirements

The ContainerType model should have properties for:

**color**

> The general color.

**shape**

> Wheelie bin, box, caddy, etc.

**lid color**

> In case its different to the body color.

**disposable**

> If the container type is disposable or one-time use, e.g. a bag.

**materials**

> What kind of materials the container is used for.

**sizes**

> What container sizes are available. Relevant if ordering new containers.


## Types

ContainerType derives from FeatureType.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
id |  | Unique identifer.
disposable | boolean | If container is disposable.
material | [Material](material.html) | The materials it stores.
color | [schema:color](https://schema.org/color) | The colour.
shape | text | The shape or type of the container.
lid color | [schema:color](https://schema.org/color) | The lid colour.
sizes | list of integers | Available sizes of containers.

## Serialisation

{% include serialisation.html %}


## Codelists

### Container shape

See the [container types taxonomy]({{ site.baseurl }}/taxonomies/container-types.html).
