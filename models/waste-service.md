---
layout: doc
title: Waste service
model: waste_service
---

# Waste service

## Requirements

The Service model should have properties for:

**name**

> For identification.

**frequency**

> An indication of typically how often the collection is run.

**description**

> For specific instructions about the service, such as when and where to put containers out, that bin lids must be closed, etc.

**next collections**

> To know upcoming dates of when upcoming collections will happen, when filtered by property. Also if any adjustments to the scheduled dates are made.

**last collections**

> To know when the last few collections have taken place, when filtered by property.

**container types**

> What types of containers (and in relation, materials) are collected by this service.


## Types

This WasteService type:

* Is a derivation of the [Service concept](http://www.legsb.gov.uk/smartcityconceptmodel/index.php?Action=ShowConcept&Id=169) in the Smart City Concept Model.
* Extends from the [GovernmentService](http://schema.org/GovernmentService) schema.org type.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
name | [schema:name](http://schema.org/name) | Name of the service.
description | [schema:description](https://schema.org/description) | A short description of the service.
frequency | Text | How often it runs, e.g. weekly.
next collections | [Task](task.html) | List of dates of next collections.
last collections | [Task](task.html) | List of dates of previous collections.
feature types | [Feature type](feature-type.html) | The [container types](waste-container-type.html) that are collected.
provider | [schema:provider](http://schema.org/provider) | The council providing the service.
service area | [schema:serviceArea](http://schema.org/serviceArea) | The geographic area where the service is provided.
service operator | [schema:serviceOperator](http://schema.org/serviceOperator) | The operator of the service, if different to the provider.


## Serialisation

{% include serialisation.html %}


## Codelists

### Freqency

* weekly
* alternate weekly




