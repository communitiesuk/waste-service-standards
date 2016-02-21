---
layout: doc_notoc
title: Tutorials - Waste Service Standards
description: Technical specifications for local waste and recycling services
---

# Tutorials

_These assume the citizen can search for their address and the relevant [UPRN](https://www.geoplace.co.uk/addresses/uprn) has been obtained._


## Next collections

To find basic information about the waste services available to a property and when their next collections are, call:

`/services?uprn=123456789`

This will return a list of relevant services with basic metadata and at least one collection listed for last and next collections. See [Services]({{ site.baseurl }}/apis/waste_services.html#Services) for more information. If collection information is needed covering a wider timespan, use `start_date` and `end_date` query parameters.


## Missed bins

Citizens contacting the council to report a bin not emptied is a common problem. Often it is because of an error on the part of the citizen, for example it is contaminated.

Events represent unexpected issues that arose during collections. Find events related to a property with the [events endpoint]({{ site.baseurl }}/apis/waste_services.html#Events):

`/events?uprn=123456789`

This also includes related street events. These will have a date that corresponds to a collection task. If possible they will reference a specific task.
