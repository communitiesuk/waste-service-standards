---
layout: doc
title: Bulky item
model: bulky_item
---

# Bulky item

## Use cases and requirements

The Bulky item model should have properties for:

**name**

> Sofa

**description**

> 3 person seater, quite rough condition.

**is working**

> Is the item in working order (if it is "functional")?


## Properties

Term     | Mapping | Definition
---------|---------|-----------
name | [schema:name](http://schema.org/name) | The name of the item.
description | [schema:description](https://schema.org/description) | A short description of the item and how to manage it.
is working | boolean | Is the item in working condition?


## Serialisation

{% include serialisation.html %}


