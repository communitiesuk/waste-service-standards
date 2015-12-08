---
layout: doc
title: Feature type
model: feature_type
---

# Feature type

## Use cases and requirements

The ContainerType model should have properties for:

**name**

> Identifer.

**description**

> Additional information.

**manufacturer**

> To know who to order from.


## Types

ContainerType derives from FeatureType.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
id |  | Unique identifer.
name | [schema:name](http://schema.org/name) | Identifer for the Feature.
description | [schema:description](https://schema.org/description) | A short description of the Feature.
manufacturer | [schema:manufacturer](https://schema.org/manufacturer) | The organisation that manufactured it.


## Serialisation

{% include serialisation.html %}




