---
layout: doc
title: Bulky items
---

# Bulky items

A common list of items that can typically be collected by bulky collection schemes.

**These will need further refinement.**

<table>
<tr>
  <th>Item</th>
  <th>Qualifier</th>
  <th>Category</th>
  <th>Is electrical</th>
  <th>Description</th>
</tr>
{% for item in site.data.bulky_items %}
<tr>
  <td>{{ item.item }}</td>
  <td>{{ item.qualifier }}</td>
  <td>{{ item.category }}</td>
  <td>{{ item.electrical }}</td>
  <td>{{ item.description }}</td>
  </td>
</tr>
{% endfor %}
</table>

Also available as <a href="https://raw.githubusercontent.com/communitiesuk/waste-service-standards/master/_data/bulky_items.csv" download="bulky_items.csv">CSV</a>.

