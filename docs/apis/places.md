
# Places API






## Places


---
Get a list of places

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/places</span>
</div>


**Query parameters**

Name | Type | Description
-----|------|------------
<tt>uprn</tt> | string | Limit results to those related to the property with this UPRN.
<tt>usrn</tt> | string | Limit results to those related to the street with this USRN.





**Response**
```
[
  {
    "usrn": "123456789012",
    "@id": "/places/1",
    "address": {
      "region": "Anyshire",
      "postcode": "AB1 2CD",
      "street_address": "1 Acacia Avenue",
      "locality": "Anytown"
    },
    "uprn": "123456789012",
    "geo": {
      "latitude": "40.75",
      "@type": "GeoCoordinates",
      "longitude": "73.98"
    },
    "@type": "Place"
  }
]
```









---
Get a single place

<div class="api-call">
  <span class="rest-method get">get</span>
  <span>/places/{placeId}</span>
</div>





**Response**
```
{
  "usrn": "123456789012",
  "@id": "/places/1",
  "address": {
    "region": "Anyshire",
    "postcode": "AB1 2CD",
    "street_address": "1 Acacia Avenue",
    "locality": "Anytown"
  },
  "uprn": "123456789012",
  "geo": {
    "latitude": "40.75",
    "@type": "GeoCoordinates",
    "longitude": "73.98"
  },
  "@type": "Place"
}
```







