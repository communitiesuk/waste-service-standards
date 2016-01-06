---
layout: doc
title: Task
model: task
---

# Task

A Task could prepresent any form of work required in the council's region, e.g.:

* a scheduled bin collection
* cleanup of a fly tip
* maintenance of a street


## Use cases and requirements

The Task model should have properties for:

**name**

> What the Task is.

**description**

> More details about the Task.

**status**

> Whether the Task is pending, started, completed, etc.

**location**

> A link to a property or street location.

**start date**

> When the task was started.

**end date**

> When the task ended.

**scheduled start date**

> When the task was planned to start.


## Types

This Task type extends from the [Action](http://schema.org/Action) schema.org type.


### Sub-types

Just as Action and other common types have a number of sub-types, here are specific Task sub-types for different kinds of services councils provide:

* EmptyBinTask
* StreetCleansingTask
* FlytippingCleanupTask


## Properties

Term     | Mapping | Definition
---------|---------|-----------
name | [schema:name](http://schema.org/name) | Identifer for the Task.
description | [schema:description](https://schema.org/description) | A short description of the Task.
status | [schema:actionStatus](http://schema.org/actionStatus) | The status of the Task.
location | [schema:location](http://schema.org/location) | Location information.
start date | [schema:startDate] | Start date.
end date | [schema:endDate] | End date.
scheduled start date | [schema:startDate] | Planned start date.


## Serialisation

{% include serialisation.html %}

## Codelists

### Task statuses

* Not started
* In progress
* On break
* Closed / Complete
* Closed / Not done
* Closed / Not required
* Closed / Part done
* Blocked
* Abandoned


