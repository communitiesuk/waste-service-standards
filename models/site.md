---
layout: doc
title: Site
model: site
---

# Site

## Use cases and requirements

The Site model should have properties for:

**parent UPRN**

> For flats and other shared properties, the parent UPRN is often the site with associated features shared by all child sites.

**attributes**

> To record specific information about the site related to the service provision there.


## Types

This is a sub-type of [Place](place.html). Depending on the system, many of the Place properties may be optional.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
parent_uprn | Text | A unique identifier for a parent property.
attributes | Name-value pairs. | List of attributes.


## Serialisation

{% include serialisation.html %}


## Parent-child relationships

Properties such as flats often have shared bin stores. A typical pattern to model this is:

* The building has a UPRN
* Each flat has a UPRN and a parent UPRN for the building
* The shared bin store is a feature associated with the building

There are other kinds of patterns for recording these relationships, depending on how the council has modelled the information.
