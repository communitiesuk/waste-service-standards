
Waste Services API




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
    "description": "Please put your recycling box on the street.",
    "frequency": "weekly",
    "id": 1,
    "esd_id": "http://id.esd.org.uk/service/524",
    "name": "Recycling service"
  }
]
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
<tt>uprn</tt> | string | 
<tt>usrn</tt> | string | 
<tt>eventType</tt> | string | The short name of an event type, e.g. "Not presented".





**Response**
```
{}
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
  "event_type": "Not presented",
  "date_created": "2014-05-23T20:00",
  "uprn": "123456789012",
  "usrn": "123456789012",
  "image": "http://example.com/images/123.png",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "40.75",
    "longitude": "73.98"
  }
}
```







