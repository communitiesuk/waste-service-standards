---
layout: doc
title: Material streams
---

# Material streams

The table below lists the material streams as defined by [WRAP](https://partners.wrap.org.uk/assets/3647/). These are used to categorize the types of resources that can be collected in different kinds of containers.


<table>
<tr>
  <th>Name</th>
  <th>Parent</th>
  <th>Color</th>
</tr>
{% for code in site.data.material_streams %}
<tr>
  <td>{{ code.name }}</td>
  <td>{{ code.parent }}</td>
  <td><div style="background: #{{ code.color }}; width: 40px; height: 30px"></div>
  </td>
</tr>
{% endfor %}
</table>

