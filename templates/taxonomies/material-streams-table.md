
<table>
<tr>
  <th>Name</th>
  <th>Parent</th>
  <th>Color</th>
</tr>
{% for code in data.material_streams %}
<tr>
  <td>{{ code.name }}</td>
  <td>{{ code.parent }}</td>
  <td><div style="background: #{{ code.color }}; width: 40px; height: 30px"></div>
  </td>
</tr>
{% endfor %}
</table>
