---
layout: doc
title: Case
model: case
---

# Case

<div class="alert-box warning">
  Note: The Case model is currently incomplete and needs further development.
</div>

A case is a way to track transactions with a citizen.


## Use cases and requirements

The Case model should have properties for:

**subject**

> Describe what the case is about.

**customer**

> The person who created the case, or is recipient of the outcome.

**date created**

> When the case was opened.

**status**

> Current status of the case.


## Types

This maps to the Smart Cities Concept Model [Case type](http://www.legsb.gov.uk/smartcityconceptmodel/index.php?Action=ShowConcept&Id=172).

### Sub-types

Just as Action and other common types have a number of sub-types, here are specific Service request sub-types for different kinds of services councils provide:

* AdditionalBinRequest
* AssistedCollectionRequest
* BulkyCollection
* ChargeableBulkyCollection
* ClinicalOneTimeCollection
* ClinicalCollection
* ReportDamage
* ReportMissedBin
* DeadAnimal
* EmergencyCollection
* FreezerCollection
* NewCollection


## Properties

Term     | Mapping | Definition
---------|---------|-----------
subject | [schema:name](http://schema.org/name) | Subject of the case.
status |  | Current status, e.g. active, closed.
customer | [schema:person](http://schema.org/Person) | Customer of the case.
date_created | [schema:dateCreated](https://schema.org/dateCreated) | When the case was created.


### ReportMissedCollection

Additional properties needed to report a missed bin collection:

Term     | Mapping | Definition
---------|---------|-----------
collection_type | string | The Container type machine name, if related to a missed bin collection. Otherwise a common string identifier of the collection type.



## Serialisation

{% include serialisation.html %}


