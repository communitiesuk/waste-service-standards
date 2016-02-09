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

**feature type**

> What kind of feature does the event relate to (e.g. waste container such as a bin)? This could be typically matched by colour.

**task**

> What task this event relates to, if any.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
type | string | A categorisation of the event. This should be limited to 20 characters for ease of use on in-cab systems.
start date | [schema:startDate](https://schema.org/startDate) | When the event was took place.
location | [Place](place.html) | A unique identifier for a property.
image | [schema:image](https://schema.org/image) | A URL to a related image.
round | URL | The URL of the round where this event was recorded.
feature type | [Feature type](feature-type.html) | The type of feature, if relevant.
task | [Task](task.html) | Task related to the event.

## Serialisation

{% include serialisation.html %}



