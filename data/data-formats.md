---
layout: doc
title: Data formats
---

# Data formats

Data files are typically exchanged when a council starts a new contract with a supplier. Here are common formats that make this process easier.


## Rounds

Rounds data should be formatted into a CSV file matching the format defined by the Rounds table schema. The CSV fields are listed below:


<table>
  <tr>
    <th>name</th>
    <th>type</th>
    <th>required</th>
    <th>description</th>
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

The table definition is also available as a <a href="https://raw.githubusercontent.com/communitiesuk/waste-service-standards/gh-pages/_data/table_schemas/rounds_tableschema.json" download="rounds_tableschema.json">JSON Table schema</a>.
