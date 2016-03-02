---
layout: doc
title: Container types
---

# Container types

The table below lists common names for typical waste containers.

The `name` field is intended to be read by citizens. 


name | reference name  | machine name | description | image
--------|-------|--------------|-------------|------
{% for c in site.data.container_types %}{{ c.name }} | {{ c.reference_name }} | {{ c.machine_name }} | {{ c.description }} | {% if c.image %}![img]({{ site.baseurl }}/images/{{ c.image }}){% endif %}
{% endfor %}


**Notes:**

* This material has been reproduced from the website [www.partners.wrap.org.uk](http://www.partners.wrap.org.uk) of The Waste and Resources Action Programme.
* Often a wheelie bin may simply be called a "bin" as they are the most common form of bins.

Also available as <a href="https://raw.githubusercontent.com/communitiesuk/waste-service-standards/master/_data/container_types.csv" download="container_types.csv">CSV</a>.
