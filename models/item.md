---
layout: doc
title: Item
model: item
---

# Item

## Use cases and requirements

The Item model should have properties for:

**name**

> "Telephone directory"

**image**

> A typical example image of this type of item.

**collectable**

> If the item can be collected by the council, like via a bulky collection service.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
name | [schema:name](http://schema.org/name) | The name of the item.
image | [schema:image](https://schema.org/image) | A URL to a related image.
description | [schema:description](https://schema.org/description) | A short description of the item and how to manage it.

## Serialisation

{% include serialisation.html %}




