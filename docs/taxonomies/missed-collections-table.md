
<table>
<tr>
  <th>ID</th>
  <th>Name</th>
  <th>Parent</th>
  <th>Type<sup>1</sup></th>
  <th>Description</th>
  <th>Synonyms</th>
</tr>

<tr>
  <td></td>
  <td>Not presented</td>
  <td></td>
  <td>service</td>
  <td>The container was not presented on the street.</td>
  <td>Non-Presentation</td>
</tr>

<tr>
  <td></td>
  <td>Incorrectly presented</td>
  <td></td>
  <td>service</td>
  <td></td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Too heavy</td>
  <td></td>
  <td>service</td>
  <td>The container was too heavy to empty.</td>
  <td>Overweight Bin</td>
</tr>

<tr>
  <td></td>
  <td>Lid open</td>
  <td></td>
  <td>service</td>
  <td>The container was too full, the lid would not close properly.</td>
  <td>Overflowing Bin / Lid up</td>
</tr>

<tr>
  <td></td>
  <td>Side waste present</td>
  <td></td>
  <td>service</td>
  <td>Extra refuse was present at the side of the bins.</td>
  <td>Sidewaste</td>
</tr>

<tr>
  <td></td>
  <td>Contamination</td>
  <td></td>
  <td>service</td>
  <td>The contents was contaminated.</td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Food waste</td>
  <td>Contamination</td>
  <td>service</td>
  <td>Contaminated with food waste</td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Garden waste</td>
  <td>Contamination</td>
  <td>service</td>
  <td>Contaminated with garden waste</td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Refuse waste</td>
  <td>Contamination</td>
  <td>service</td>
  <td>Contaminated with refuse waste</td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Bulky waste</td>
  <td>Contamination</td>
  <td>service</td>
  <td>Contaminated with bulky waste</td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Rubble/DIY</td>
  <td>Contamination</td>
  <td>service</td>
  <td>Contaminated with rubble</td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Commercial</td>
  <td>Contamination</td>
  <td>service</td>
  <td>Contaminated with commercial waste</td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Turf/soil</td>
  <td>Contamination</td>
  <td>service</td>
  <td>Contaminated with turf or soil</td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Animal bedding</td>
  <td>Contamination</td>
  <td>service</td>
  <td>Contaminated with animal bedding</td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Inaccessible container store</td>
  <td></td>
  <td>service</td>
  <td>It was not possible to access the bins.</td>
  <td>Inaccessible Bin Store</td>
</tr>

<tr>
  <td></td>
  <td>Container damaged</td>
  <td></td>
  <td>service</td>
  <td>A bin was damaged.</td>
  <td>Bin damaged</td>
</tr>

<tr>
  <td></td>
  <td>Container lost in vehicle</td>
  <td></td>
  <td>service</td>
  <td>A bin was lost inside the vehicle.</td>
  <td>Receptacle Lost in Vehicle</td>
</tr>

<tr>
  <td></td>
  <td>Not on scheme</td>
  <td></td>
  <td>service</td>
  <td>The property was not on the service.</td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Inaccessible road</td>
  <td></td>
  <td>service</td>
  <td>The road could not be accessed.</td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Road closure</td>
  <td></td>
  <td>service</td>
  <td>The road was closed.</td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Querying assisted</td>
  <td></td>
  <td>service</td>
  <td></td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Street completed</td>
  <td></td>
  <td>general</td>
  <td>All properties on this street have been visited.</td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Blocked by vehicles</td>
  <td></td>
  <td>general</td>
  <td>A street cannot be accessed due to vehicles blocking access.</td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Roadworks</td>
  <td></td>
  <td>general</td>
  <td>Roadworks are blocking the street.</td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Gate locked</td>
  <td></td>
  <td>general</td>
  <td>A street cannot be accessed due to a gate being locked.</td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Part access</td>
  <td></td>
  <td>general</td>
  <td></td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Partly completed street</td>
  <td></td>
  <td>general</td>
  <td></td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Alarm activated</td>
  <td></td>
  <td>general</td>
  <td>A vehicle alarm was activated.</td>
  <td></td>
</tr>

<tr>
  <td></td>
  <td>Breakdown</td>
  <td></td>
  <td>general</td>
  <td>The waste collection truck broke down.</td>
  <td></td>
</tr>

</table>

1. Here "service" means an event type that is applied to a specific service, e.g. refuse, recycling, etc and often relates to the containers. "General" is for event types where the event is not specifically tied to a service but could affect any service.