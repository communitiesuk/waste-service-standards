---
layout: doc
title: Missed collection events
---

# Missed collection events

The table below lists a set of common possible events that can occur during a waste collection round.

Many council classifications also divide event types by the service or container type. It is assumed here that it will be possible to categorise the events by:

* container type
* property or street


<table>
<tr>
  <th>Term</th>
  <th>Sub-term</th>
  <th>Description</th>
  <th>Apply to bin<sup>1</sup></th>
  <th>Location type</th>
</tr>
{% for code in site.data.collection_event_types %}
<tr>
  <td>{{ code.level_1 }}</td>
  <td>{{ code.level_2 }}</td>
  <td>{{ code.description }}</td>
  <td>{{ code['apply to bin'] }}</td>
  <td>{{ code['location type'] }}</td>
</tr>
{% endfor %}
</table>

1. Some events may be applied to specific containers or bins, whereas others are general events.

Also available as <a href="https://github.com/communitiesuk/waste-service-standards/blob/gh-pages/_data/collection_event_types.csv" download="materials.csv">CSV</a>.