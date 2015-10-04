

<table>
<tr>
  <th>Name</th>
  <th>Type</th>
  <th>Description</th>
</tr>
{% for f in data['round_plan.tableschema'].fields %}
<tr>
  <td>{{ f.title }}</td>
  <td>{{ f.type }}</td>
  <td>{{ f.description }}</td>
  </td>
</tr>
{% endfor %}
</table>
