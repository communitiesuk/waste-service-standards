---
layout: doc
title: Bulky item collection request
model: bulky_collection_request
---

# Bulky collection request

## Use cases and requirements

The BulkyCollectionRequest model should have properties for:

**items**

> Sofa, wardrobe


## Types

This derives from [Case](case.html).


## Properties

Term     | Mapping | Definition
---------|---------|-----------
items | List of [bulky items](bulky-item.html) | List of items.


## Serialisation

{% include serialisation.html %}
