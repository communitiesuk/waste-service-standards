
# Missed collection reasons

<table>
<tr>
  <th>ID</th>
  <th>Name</th>
  <th>Description</th>
</tr>
{% for code in data.collection_event_types %}
<tr>
  <td>{{ code.id }}</td>
  <td>{{ code.name }}</td>
  <td>{{ code.description }}</td>
</tr>
{% endfor %}
</table>
