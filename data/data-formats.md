---
layout: doc
title: Data formats
---

# Data formats

Data files are typically exchanged when a council starts a new contract with a supplier. Here are common formats that can be used.


## Rounds

Rounds data should be formatted into a CSV file matching the format defined by the Rounds table schema. The CSV fields are listed below:


<table>
  <tr>
    <th>Name</th>
    <th>Type</th>
    <th>Required</th>
    <th>Description</th>
  </tr>
  {% for f in site.data.table_schemas.rounds_tableschema.fields %}
  <tr>
    <td>{{ f.title }}</td>
    <td>{{ f.type }}</td>
    <td {% if f.constraints.required == true %}class="required"{% endif %}>{{ f.constraints.required }}</td>
    <td>{{ f.description }}</td>
  </tr>
  {% endfor %}
</table>


## Technical notes

Tabular data formats are defined as [JSON Table Schema](http://dataprotocols.org/json-table-schema/).

