---
layout: doc
title: Round
model: round
---

# Round

## Use cases and requirements

The Round model should have properties for:

**name**

> for a label or identifier for the round

**UPRNs**

> define which properties are managed by this round. This could be an ordered list.

**schedule**

> e.g. weekly Wed, or a recurring rule.

**services**

> e.g. Recycling service


## Properties

Term     | Mapping | Definition
---------|---------|-----------
name | [schema:name](http://schema.org/name) | Round name or label.
UPRNs | List of UPRNs | Properties serviced by this round.
schedule | Text | Text description of schedule.
service | List of [WasteService](waste-service.html) | Name of the services provided on the round. 


## Serialisation

Currently there is not an identified need to define a round in a serialisation format, as it is not supported in the API. However this model feeds into the [round data format definition]({{ site.baseurl }}/data/data-formats.html#rounds).


