---
layout: doc
title: Event type
model: event_type
---

# Event type

## Use cases and requirements

The EventType model should have properties for:

**name**

> Identifer.


## Types

Sub-types are used to distinguish between events from different sources:

* EventType
  * PropertyEventType
  * StreetEventType


## Properties

Term     | Mapping | Definition
---------|---------|-----------
id |  | Unique identifer.
name | [schema:name](http://schema.org/name) | Identifer for the EventType.


## Serialisation

{% include serialisation.html %}




