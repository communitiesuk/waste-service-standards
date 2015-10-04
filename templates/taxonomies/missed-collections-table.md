
<table>
<tr>
  <!-- <th>ID</th> -->
  <th>Term</th>
  <th>Sub-term</th>
  <th>Description</th>
  <th>Type<sup>1</sup></th>
  <!-- <th>Synonyms</th> -->
</tr>
{% for code in data.collection_event_types %}
<tr>
  <!-- <td></td> -->
  <td>{{ code.level_1 }}</td>
  <td>{{ code.level_2 }}</td>
  <td>{{ code.description }}</td>
  <td>{{ code.service_type }}</td>
  <!-- <td>{{ code.synonyms }}</td> -->
</tr>
{% endfor %}
</table>

1. Here "service" means an event type that is applied to a specific service, e.g. refuse, recycling, etc and often relates to the containers. "General" is for event types where the event is not specifically tied to a service but could affect any service.
