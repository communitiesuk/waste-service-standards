---
layout: doc_notoc
title: Data models
---

# Data models

This gives an overview of the data model entities:

## Waste services

Model | Description
------|------------
[Bulky item](bulky-item.html) | A bulky item for collection.
[Case](case.html) | A customer interaction record.
[Event type](event-type.html) | A type of event that can occur during provison of the service.
[Feature type](feature-type.html) | A type of item related to a service.
[Feature](feature.html) | An item related to a service.
[Material](material.html) | The types of materials that can be collected.
[Round](round.html) | One or more services delivered on a route according to a repeating schedule.
[Site](site.html) | A place or location that relates to a service.
[Task](task.html) | A unit of work as part of scheduled rounds or resulting from ad-hoc requests.
[Waste container type](waste-container-type.html) | What kinds of containers are used for waste.
[Waste container](waste-container.html) | Where materials are stored for collection.
[Waste event](waste-event.html) | An issue or check that is recorded during a round.
[Waste service](waste-service.html) | A waste or recycling service provided by the council for citizens.


## Places

Model | Description
------|------------
[Address](address.html) | A postal address.
[Place](place.html) | A geographic location, typically with an address, that may be served by council services.

<!---

[Round plan](round-plan.html) | A vehicle emptying containers from a set of properties on a repeating schedule.
[Round](round.html) | An instance of a round plan that has been executed on a particular date.

![Entity Relationships]({{ site.baseurl }}/images/waste_services_erd.png)
-->