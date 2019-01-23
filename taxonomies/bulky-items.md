---
layout: doc
title: Bulky items
---

# Bulky items

A common list of items that can typically be collected by bulky collection schemes.


<table>
<tr>
  <th>item</th>
  <th>qualifier</th>
  <th>category</th>
  <th>electrical</th>
  <th>description</th>
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

Also available as <a href="https://github.com/communitiesuk/waste-service-standards/blob/gh-pages/_data/bulky_items.csv" download="bulky_items.csv">CSV</a>.

