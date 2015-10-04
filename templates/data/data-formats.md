# Data formats

Tabular data formats are defined as [JSON Table Schema](http://dataprotocols.org/json-table-schema/).

## Round plans

Round plan data should be formatted into a CSV file matching the format defined by the Round plan table schema. The CSV fields are listed below:

<table>
<tr>
  <th>Name</th>
  <th>Type</th>
  <th>Required</th>
  <th>Description</th>
</tr>
{% for f in data['round_plan.tableschema'].fields %}
<tr>
  <td>{{ f.title }}</td>
  <td>{{ f.type }}</td>
  <td>{% if f.constraints.required %}Yes {% endif %}</td>
  <td>{{ f.description }}</td>
  </td>
</tr>
{% endfor %}
</table>


### Table schema

Here is the table schema in full:

<div role="tabpanel" class="tab-pane active" id="json">
  <pre><code class="hljs json">{!table-schemas/round_plan.tableschema.json!}</code></pre>
</div>


