---
layout: doc
title: 
---

# Missed collections reasons

The table below lists a set of common possible events that can occur during a waste collection round.

Many council classifications also divide event types by the service or container type. It is assumed here that it will be possible to categorise the events by:

* container type
* property or street


<table>
<tr>
  <!-- <th>ID</th> -->
  <th>Term</th>
  <th>Sub-term</th>
  <th>Description</th>
  <th>Apply to bin<sup>1</sup></th>
  <!-- <th>Synonyms</th> -->
</tr>
{% for code in site.data.collection_event_types %}
<tr>
  <!-- <td></td> -->
  <td>{{ code.level_1 }}</td>
  <td>{{ code.level_2 }}</td>
  <td>{{ code.description }}</td>
  <td>{{ code['apply to bin'] }}</td>
  <!-- <td>{{ code.synonyms }}</td> -->
</tr>
{% endfor %}
</table>

1. Here "service" means an event type that is applied to a specific service, e.g. refuse, recycling, etc and often relates to the containers. "General" is for event types where the event is not specifically tied to a service but could affect any service.

Also available as <a href="https://raw.githubusercontent.com/communitiesuk/waste-service-standards/master/_data/collection_event_types.csv" download="materials.csv">CSV</a>.