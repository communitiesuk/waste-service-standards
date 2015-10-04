
# Materials

This is a standard list of materials as used by [WRAP](http://www.wrap.org.uk/) for kerbside collections. The top categories are listed with individual items that are typically allowed for that type of materials. The relevant material stream and colour (typically used for on-street signage and colour coding) are linked to the material categories.


<br/>

<table>
<tr>
  <th>Category</th>
  <th>Item</th>
  <th>Material stream</th>
  <th>Color</th>
</tr>
{% for code in data.materials %}
<tr>
  <td>{{ code.material_category }}</td>
  <td>{{ code.material_item }}</td>
  <td>{{ code.stream }}</td>
  <td><div style="background: #{{ code.color }}; width: 40px; height: 30px"></div>
  </td>
</tr>
{% endfor %}
</table>
