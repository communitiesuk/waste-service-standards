---
layout: doc
title: 
---

# Data formats

Tabular data formats are defined as [JSON Table Schema](http://dataprotocols.org/json-table-schema/).

## Round plans

Round plan data should be formatted into a CSV file matching the format defined by the Round plan table schema. The CSV fields are listed below:

<table>
<tr>
  <th>Name</th>
  <th>Type</th>
  <th>Required</th>
  <th>Description</th>
</tr>

<tr>
  <td>UPRN</td>
  <td>integer</td>
  <td>Yes </td>
  <td>The Unique Property Reference Number for the location.</td>
  </td>
</tr>

<tr>
  <td>Round plan</td>
  <td>string</td>
  <td>Yes </td>
  <td>An identifier for a round plan, or set of properties visited by a crew.</td>
  </td>
</tr>

<tr>
  <td>Container type</td>
  <td>string</td>
  <td>Yes </td>
  <td>The type of container at the property or place.</td>
  </td>
</tr>

<tr>
  <td>Schedule</td>
  <td>string</td>
  <td>Yes </td>
  <td>For example, alternate weekly on Monday.</td>
  </td>
</tr>

</table>


### Table schema

Here is the table schema in full:

  {% highlight json %}
  {% include table-schemas/round_plan.tableschema.json %}
  {% endhighlight %}



