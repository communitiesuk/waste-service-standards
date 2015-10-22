---
layout: doc
title: Materials
---

# Materials

This is a standard list of materials as used by [WRAP](http://www.wrap.org.uk/) for kerbside collections. The top categories are listed with individual items that are typically allowed for that type of materials. The relevant material stream and colour (typically used for on-street signage and colour coding) are linked to the material categories.


<table>
<tr>
  <th>Category</th>
  <th>Item</th>
  <th>Material stream</th>
  <th>Colour</th>
</tr>
{% for m in site.data.materials %}
<tr>
  <td>{{ m.material_category }}</td>
  <td>{{ m.material_item }}</td>
  <td>{{ m.stream }}</td>
  <td><div style="background: #{{ m.color }}; width: 40px; height: 30px"></div>
  </td>
</tr>
{% endfor %}
</table>

Also available as <a href="https://raw.githubusercontent.com/communitiesuk/waste-service-standards/master/_data/materials.csv" download="materials.csv">CSV</a>.

