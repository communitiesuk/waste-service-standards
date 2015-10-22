---
layout: doc
title: Waste event
model: waste_event
---

# Waste event

## Use cases and requirements

The Event model should have properties for:

**event type**

> What kind of event it is.

**start date**

> Know when an event happened.

**location**

> To know what the location information is (property, street, addresss, etc).

**image**

> Visual evidence of an issue.

**comments**

> For any additional information useful to record.

**container type**

> What kind of container does the event relate to? This could be typically matched by colour.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
type | string | A categorisation of the event.
start date | [schema:startDate](https://schema.org/startDate) | When the event was took place.
location | [Place](place.html) | A unique identifier for a property.
image | [schema:image](https://schema.org/image) | A URL to a related image.
round | URL | The URL of the round where this event was recorded.
container_type | [Container type](container-type.html) | The type of container, if relevant.


## Serialisation

{% include serialisation.html %}



