---
layout: doc
title: 
---

# Waste Services API



## Introduction
This API offers a core set of resources and operations for interacting with local council waste and recycling services.


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
<tt>uprn</tt> | string | Limit results to those related to the property with this UPRN.









<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->


<hr/>
<h4>Get a single service</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/services/{serviceId}</span>
</div>





**Response**
{% highlight json %}
{
  "description": "Please put your recycling wheelie bin on the street.",
  "last_collection": {
    "date": "23 July 2015",
    "features": [
      {
        "status": "In use",
        "type": {
          "image": "",
          "materials": [
            {
              "@id": "/waste/material-streams/mixed-recycling",
              "name": "Mixed recyclables"
            }
          ],
          "name": "Green wheelie bin",
          "description": "Garden refuse green wheelie bin"
        },
        "@type": "WasteContainer",
        "id": "2140541"
      }
    ],
    "events": [
      {
        "type": "Not presented",
        "usrn": "123456789012",
        "@id": "/api/events/1",
        "image": "http://example.com/images/123.png",
        "uprn": "123456789012",
        "date_created": "1 August 2015",
        "geo": {
          "latitude": "40.75",
          "@type": "GeoCoordinates",
          "longitude": "73.98"
        },
        "@type": "WasteEvent",
        "container_color": "black"
      }
    ],
    "@type": "Collection"
  },
  "feature_types": [
    {
      "color": "black",
      "image": "/images/green_bin.png",
      "shape": "wheelie bin",
      "materials": {
        "@id": "/waste/material-streams/mixed-recycling",
        "name": "Mixed recyclables"
      },
      "@type": "ContainerType",
      "lid_color": "green"
    },
    {
      "color": "brown",
      "shape": "caddy",
      "materials": {
        "@id": "/waste/material-streams/food-waste",
        "name": "Food waste"
      },
      "@type": "ContainerType",
      "image": "/images/brown_caddy.png"
    }
  ],
  "service_area": {
    "@type": "AdministrativeArea",
    "name": "Anytown"
  },
  "@type": "WasteService",
  "next_collection": {
    "date": "1 August 2014",
    "changed_date_reason": "Bank holiday",
    "changed_date": "2 August 2015",
    "features": [
      {
        "status": "in_service",
        "id": "2140541",
        "type": {
          "color": "black",
          "shape": "wheelie bin",
          "materials": [
            {
              "@id": "/waste/material-streams/mixed-recycling",
              "name": "Mixed recyclables"
            }
          ],
          "image": "",
          "lid_color": "green"
        },
        "@type": "WasteContainer",
        "size": "240L"
      }
    ],
    "@type": "Collection"
  },
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
  "service_operator": {
    "@type": "Organization",
    "name": "Example Waste Operator Co"
  },
  "id": 1,
  "name": "Mixed recycling"
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
<tt>page</tt> | number | 
<tt>type</tt> | string | Limit results to a specific task type.
<tt>uprn</tt> | string | Limit results to those related to the property with this UPRN.
<tt>date_range</tt> | string | Limit results to those tasks that were started between the given comma-separated date range. Dates should be in xs:dateTime format, e.g. date_range=2015-06-01,2015-08-01.









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
<tt>page</tt> | number | 
<tt>uprn</tt> | string | Limit results to those related to the property with this UPRN.
<tt>usrn</tt> | string | Limit results to those related to the street with this USRN.
<tt>start_date</tt> | date | Limit results to those created on or after this start date.
<tt>end_date</tt> | date | Limit results to those created before this end date.





**Response**
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





**Response**
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





**Response**
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





**Response**
{% highlight json %}
{}
{% endhighlight %}







<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->


<hr/>
<h4>Get a single site indexed by UPRN</h4>

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/sites/{UPRN}</span>
</div>





**Response**
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





**Response**
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





**Response**
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







