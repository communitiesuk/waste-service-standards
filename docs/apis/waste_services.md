
# Waste Services API



## Introduction
This API offers a core set of resources and operations for interacting with local council waste and recycling services.


## ESD Standards
The [ESD Standards](http://standards.esd.org.uk) define all the categories of services that local authorities typically provide. These will be referenced via URL from the Services API, to allow individual council instances of a service to be matched to common service definitions.







## Services


---
Get a list of waste services

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/services</span>
</div>





**Response**
```
[
  {
    "id": 1,
    "frequency": "weekly",
    "description": "Please put your recycling box on the street.",
    "name": "Recycling service",
    "esd_url": "http://id.esd.org.uk/service/524"
  },
  {
    "id": 2,
    "frequency": "weekly",
    "description": "Black bins.",
    "name": "Refuse",
    "esd_url": "http://id.esd.org.uk/service/525"
  }
]
```









---
Get a single service

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/services/{serviceId}</span>
</div>





**Response**
```
{
  "description": "Please put your recycling wheelie bin on the street.",
  "container_types": [
    {
      "color": "black",
      "image": "",
      "material_stream": {
        "@id": "/waste/material-streams/mixed-recycling",
        "name": "Mixed recyclables"
      },
      "shape": "wheelie bin",
      "lid_color": "green",
      "size": "240L"
    },
    {
      "color": "brown",
      "material_stream": {
        "@id": "/waste/material-streams/food-waste",
        "name": "Food waste"
      },
      "shape": "caddy",
      "image": "",
      "size": "40L"
    }
  ],
  "@type": "WasteService",
  "service_operator": {
    "@type": "Organization",
    "name": "Example Waste Operator Co"
  },
  "service_area": {
    "@type": "AdministrativeArea",
    "name": "Anytown"
  },
  "name": "Mixed recycling",
  "events": [
    {
      "type": "Not presented",
      "usrn": "123456789012",
      "@id": "/api/events/1",
      "image": "http://example.com/images/123.png",
      "@type": "WasteEvent",
      "uprn": "123456789012",
      "date_created": "1 August 2015",
      "geo": {
        "latitude": "40.75",
        "@type": "GeoCoordinates",
        "longitude": "73.98"
      },
      "round": "/rounds/123",
      "container_color": "black"
    }
  ],
  "next_collection": "1 August 2014",
  "frequency": "weekly",
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
  "provider": {
    "url": "http://www.example.gov.uk",
    "@type": "Organization",
    "name": "Example Council"
  },
  "last_collection": "23 July 2015",
  "id": 1,
  "esd_url": "http://id.esd.org.uk/service/1130"
}
```








## Events


---
Get a list of events

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
<tt>type</tt> | string | Limit results to those with a matching type, e.g. "Not presented".
<tt>start_date</tt> | date | Limit results to those created on or after this start date.
<tt>end_date</tt> | date | Limit results to those created before this end date.
<tt>round</tt> | string | Limit results to those recorded against this round.





**Response**
```
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
```









---
Get a single event

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/events/{eventId}</span>
</div>





**Response**
```
{
  "type": "Not presented",
  "usrn": "123456789012",
  "@id": "/api/events/1",
  "image": "http://example.com/images/123.png",
  "@type": "WasteEvent",
  "uprn": "123456789012",
  "date_created": "2014-05-23T20:00",
  "geo": {
    "latitude": "40.75",
    "@type": "GeoCoordinates",
    "longitude": "73.98"
  },
  "round": "/rounds/123"
}
```








## Rounds


---
Get a list of rounds

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/rounds</span>
</div>





**Response**
```
{}
```









---
Get a single round

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/rounds/{roundId}</span>
</div>





**Response**
```
{
  "date": "",
  "@id": "/rounds/456",
  "plan": {
    "start_date": "",
    "rrule": "",
    "containers": "/api/containers?round_plan=1",
    "id": ""
  },
  "events": "/api/events?round=456"
}
```







