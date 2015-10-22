---
layout: doc
title: Place
model: place
---

# Place

## Use cases and requirements

The Address model should have properties for:

**address**

e.g. street, locality, country, postcode.

> To provide basic address information that everyone understands.

**UPRN**

> Defines a unique property ID.

**USRN**

> To identify the street where the property is located.

**geo**

> To be able to plot locations on maps.

**attributes**

> Custom data items recorded against a property, e.g. there is a dog.



## Types

This maps to the [schema.org Place type](http://schema.org/Place) with some extended fields.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
address | [Address](address.md) | Postal address of the item.
uprn | Text | A unique identifier for a property.
usrn | Text | A unique identifier for a street.
geo | [schema:geo](https://schema.org/geo) | The location in WGS84 datum.
attributes | [schema:PropertyValueSpecification](http://schema.org/PropertyValueSpecification) | A custom property definition.


## Serialisation

{% include serialisation.html %}



