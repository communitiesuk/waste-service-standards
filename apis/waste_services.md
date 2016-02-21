---
layout: doc
title: 
---

# Waste Services API



## Introduction
This API offers a core set of resources and operations for interacting with local council waste and recycling services.


## Outstanding issues
* A way to discover if a task has been moved from its regular timeslot and why.
* Handling of non-property sites, e.g. where the bins are located separately from a building.


## ESD Standards
The [ESD Standards](http://standards.esd.org.uk) define all the categories of services that local authorities typically provide. These will be referenced via URL from the Services API, to allow individual council instances of a service to be matched to common service definitions.






<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->

<h2 id="Services">Services</h2>


<hr/>
<h4>Get a list of waste services</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/services</span>
</div>


**Query parameters**

Name | Type | Description
-----|------|------------
<tt>uprn</tt> | string | Dispalys services related to the property with this UPRN. This also includes basic completed and upcoming collection information and automatically includes related tasks if the property has a parent UPRN.
<tt>full</tt> | boolean | Return the full service information.
<tt>start_date</tt> | date | Filter related tasks that occur after this date.
<tt>end_date</tt> | date | Filter related tasks that start before this date.




**Example responses**


HTTP code: 200

{% highlight json %}
[
  {
    "frequency": "weekly",
    "@id": "http://example.com/services/1",
    "name": "Recycling service",
    "description": "Please put your recycling box on the street."
  },
  {
    "frequency": "weekly",
    "@id": "http://example.com/services/2",
    "name": "Refuse",
    "description": "Black bins."
  }
]
{% endhighlight %}


HTTP code: 400

{% highlight json %}
{
  "code": 400,
  "userMessage": "The parameters were incorrect."
}
{% endhighlight %}








<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->


<hr/>
<h4>Get a single service</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/services/{serviceId}</span>
</div>


**Query parameters**

Name | Type | Description
-----|------|------------
<tt>uprn</tt> | string | Limit results to those related to the property with this UPRN. This will include the last and next collection task information.




**Example responses**


HTTP code: 200

{% highlight json %}
{
  "@id": "http://example.com/services/1",
  "feature_types": [
    {
      "color": "black",
      "shape": "wheelie_bin",
      "materials": [
        {
          "@id": "/waste/materials/mixed-recycling",
          "name": "Mixed recyclables"
        }
      ],
      "@type": "ContainerType",
      "lid_color": "green"
    },
    {
      "color": "brown",
      "shape": "caddy",
      "materials": [
        {
          "@id": "/waste/materials/food-waste",
          "name": "Food waste"
        }
      ],
      "@type": "ContainerType"
    }
  ],
  "name": "Mixed recycling",
  "next_collections": [
    {
      "start_date": "2014-05-23T20:00Z",
      "features": [
        {
          "status": "in_service",
          "id": "2140541",
          "@id": "http://example.com/feature-types/2",
          "@type": "WasteContainer",
          "size": 240
        }
      ],
      "@type": "EmptyBinTask"
    }
  ],
  "service_area": {
    "@type": "AdministrativeArea",
    "name": "Anytown"
  },
  "@type": "WasteService",
  "frequency": "weekly",
  "esd_url": "http://id.esd.org.uk/service/1130",
  "provider": {
    "url": "http://www.example.gov.uk",
    "@type": "Organization",
    "name": "Example Council"
  },
  "available_channel": {
    "service_url": "http://www.example.gov.uk/waste",
    "service_phone": {
      "telephone": "0123456789",
      "email": "waste@example.gov.uk",
      "@type": "ContactPoint"
    },
    "name": "Household waste and street maintenance",
    "@type": "ServiceChannel"
  },
  "last_collections": [
    {
      "start_date": "2014-05-23T20:00Z",
      "features": [
        {
          "status": "In use",
          "id": "2140541",
          "@id": "http://example.com/feature-types/1",
          "@type": "WasteContainer",
          "size": 240
        }
      ],
      "@type": "EmptyBinTask"
    }
  ],
  "service_operator": {
    "@type": "Organization",
    "name": "Example Waste Operator Co"
  },
  "id": 1,
  "description": "Please put your recycling wheelie bin on the street."
}
{% endhighlight %}


HTTP code: 400

{% highlight json %}
{
  "code": 400,
  "userMessage": "The parameters were incorrect."
}
{% endhighlight %}








<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->

<h2 id="Tasks">Tasks</h2>


<hr/>
<h4>Get a list of tasks</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/tasks</span>
</div>


**Query parameters**

Name | Type | Description
-----|------|------------
<tt>type</tt> | string | Limit results to a specific task type.
<tt>uprn</tt> | string | Limit results to those related to the property with this UPRN.
<tt>start_date</tt> | date | Filter tasks that occur after this date.
<tt>end_date</tt> | date | Filter tasks that start before this date.
<tt>include</tt> | string | Comma-separated labels of additional information to include. `related` includes all tasks for any parent sites and associated bin stores where possible, e.g. `include=related`. Only applicable when filtering by UPRN.




**Example responses**


HTTP code: 200

{% highlight json %}
[
  {
    "@id": "http://example.com/tasks/123",
    "@type": "EmptyBinTask",
    "name": "Empty Black 240L"
  },
  {
    "@id": "http://example.com/tasks/124",
    "@type": "EmptyBinTask",
    "name": "Empty Green 240L"
  }
]
{% endhighlight %}


HTTP code: 400

{% highlight json %}
{
  "code": 400,
  "userMessage": "The parameters were incorrect."
}
{% endhighlight %}








<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->


<hr/>
<h4>Get a single task</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/tasks/{taskId}</span>
</div>




**Example responses**


HTTP code: 200

{% highlight json %}
{
  "status": "not_started",
  "features": [
    {
      "status": "In use",
      "id": "2140541",
      "type": "http://example.com/feature-types/1",
      "@type": "WasteContainer",
      "size": 240
    }
  ],
  "name": "Empty Black 240L",
  "@type": "EmptyBinTask",
  "location": "http://example.com/sites/1",
  "@id": "http://example.com/tasks/123",
  "start_date": "2015-09-27T21:04:00.743",
  "description": "Empty Black 240L"
}
{% endhighlight %}








<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->

<h2 id="Event types">Event types</h2>


<hr/>
<h4>Get a list of event types</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/event-types</span>
</div>




**Example responses**


HTTP code: 200

{% highlight json %}
[
  {
    "id": "1",
    "@id": "http://example.com/event-types/1",
    "@type": "EventType",
    "name": "NOT PRESENTED"
  },
  {
    "id": "2",
    "@id": "http://example.com/event-types/2",
    "@type": "EventType",
    "name": "DAMAGED"
  }
]
{% endhighlight %}








<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->


<hr/>
<h4>Get a single event type</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/event-types/{eventTypeId}</span>
</div>




**Example responses**


HTTP code: 200

{% highlight json %}
{
  "id": "2",
  "@id": "http://example.com/event-types/2",
  "@type": "EventType",
  "name": "NOT PRESENTED"
}
{% endhighlight %}








<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->

<h2 id="Events">Events</h2>


<hr/>
<h4>Get a list of events</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/events</span>
</div>


**Query parameters**

Name | Type | Description
-----|------|------------
<tt>uprn</tt> | string | Limit results to those related to the property with this UPRN.
<tt>usrn</tt> | string | Limit results to those related to the street with this USRN.
<tt>start_date</tt> | date | Filter events that occurred after this date.
<tt>end_date</tt> | date | Filter events that occurred before this date.




**Example responses**


HTTP code: 200

{% highlight json %}
[
  {
    "event_type": "Not presented",
    "usrn": "123456789012",
    "image": "http://example.com/images/123.png",
    "uprn": "123456789012",
    "date_created": "2014-05-23T20:00",
    "geo": {
      "latitude": "40.75",
      "@type": "GeoCoordinates",
      "longitude": "73.98"
    }
  },
  {
    "event_type": "Too heavy",
    "usrn": "123456789012",
    "image": "http://example.com/images/123.png",
    "uprn": "123456789012",
    "date_created": "2014-05-23T20:00",
    "geo": {
      "latitude": "45.75",
      "@type": "GeoCoordinates",
      "longitude": "53.98"
    }
  }
]
{% endhighlight %}








<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->


<hr/>
<h4>Get a single event</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/events/{eventId}</span>
</div>




**Example responses**


HTTP code: 200

{% highlight json %}
{
  "type": "Not presented",
  "features": [
    {
      "color": "#fff",
      "type": {
        "materials": {
          "@id": "/api/materials/paper",
          "name": "paper"
        },
        "name": "240L wheelie bin",
        "reusable": true
      }
    }
  ],
  "usrn": "123456789012",
  "@id": "/api/events/1",
  "image": "http://example.com/images/123.png",
  "@type": "WasteEvent",
  "uprn": "123456789012",
  "geo": {
    "latitude": "40.75",
    "@type": "GeoCoordinates",
    "longitude": "73.98"
  },
  "start_date": "2014-05-23T20:00Z"
}
{% endhighlight %}








<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->

<h2 id="Features">Features</h2>


<hr/>
<h4>Get a list of features</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/features</span>
</div>


**Query parameters**

Name | Type | Description
-----|------|------------
<tt>uprn</tt> | string | Limit results to those related to the property with this UPRN.
<tt>usrn</tt> | string | Limit results to those related to the street with this USRN.









<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->


<hr/>
<h4>Get a single feature</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/features/{featureId}</span>
</div>




**Example responses**


HTTP code: 200

{% highlight json %}
{
  "type": {
    "description": "240L wheelie bin",
    "materials": {
      "@id": "/api/materials/paper",
      "name": "paper"
    },
    "name": "240L wheelie bin",
    "reusable": true
  },
  "id": "123"
}
{% endhighlight %}








<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->

<h2 id="Feature types">Feature types</h2>


<hr/>
<h4>Get a list of feature types</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/feature-types</span>
</div>


**Query parameters**

Name | Type | Description
-----|------|------------
<tt>uprn</tt> | string | Limit results to those related to the property with this UPRN.









<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->


<hr/>
<h4>Get a single feature type</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/feature-types/{featureTypeId}</span>
</div>




**Example responses**


HTTP code: 200

{% highlight json %}
{
  "description": "240L wheelie bin",
  "sizes": [
    180,
    240
  ],
  "materials": {
    "@id": "/api/materials/paper",
    "name": "paper"
  },
  "reusable": true,
  "@id": "http://example.com/container-types/1",
  "@type": "WasteContainerType",
  "name": "240L wheelie bin"
}
{% endhighlight %}








<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->

<h2 id="Sites">Sites</h2>


<hr/>
<h4>Get a list of sites</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/sites</span>
</div>


**Query parameters**

Name | Type | Description
-----|------|------------
<tt>usrn</tt> | string | Limit results to those related to the street with this USRN.
<tt>postcode</tt> | string | Limit results to those with the given postcode.




**Example responses**


HTTP code: 200

{% highlight json %}
{}
{% endhighlight %}








<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->


<hr/>
<h4>Get a single site indexed by UPRN, or another form of index if some sites do not have a UPRN. In that situation, the format of other IDs must not collide with UPRNs.</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/sites/{ID}</span>
</div>




**Example responses**


HTTP code: 200

{% highlight json %}
{
  "usrn": "12345678",
  "geo": {
    "latitude": "40.75",
    "@type": "GeoCoordinates",
    "longitude": "73.98"
  },
  "address": {
    "locality": "Anytown",
    "region": "Anyshire",
    "street": "Acacia Avenue",
    "postcode": "AB1 2CD",
    "@type": "BS7666Address",
    "paon": "1"
  },
  "uprn": "123456789012",
  "attributes": [
    {
      "name": "assisted collection",
      "value": "yes"
    }
  ],
  "parent_uprn": "123456789012",
  "@id": "/sites/1",
  "@type": "Site"
}
{% endhighlight %}








<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->

<h2 id="Cases">Cases</h2>


<hr/>
<h4>Get a list of cases</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/cases</span>
</div>


**Query parameters**

Name | Type | Description
-----|------|------------
<tt>uprn</tt> | string | Limit results to cases associated with this UPRN.
<tt>usrn</tt> | string | Limit results to cases within this USRN.
<tt>postcode</tt> | string | Limit results to those with the given postcode.




**Example responses**


HTTP code: 200

{% highlight json %}
{}
{% endhighlight %}








<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->


<hr/>
<h4>Create a new case</h4>

<div class="api-call">
  <span class="rest-method post">post</span>
  <span>/cases</span>
</div>









<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->


<hr/>
<h4>Get a case record</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/cases/{caseId}</span>
</div>




**Example responses**


HTTP code: 200

{% highlight json %}
{
  "customer": {
    "name": "Bob Smith"
  },
  "date_created": "2014-05-23T20:00Z",
  "@id": "/cases/1",
  "id": "1"
}
{% endhighlight %}








