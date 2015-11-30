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


## Types

ContainerType derives from FeatureType.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
id |  | Unique identifer.
name | [schema:name](http://schema.org/name) | Identifer for the Feature.
description | [schema:description](https://schema.org/description) | A short description of the Feature.


## Serialisation

{% include serialisation.html %}


## Codelists

### Container shape


