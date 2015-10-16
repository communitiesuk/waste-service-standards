---
layout: doc
title: Container types
---

# Container types

The table below lists common names for typical waste containers.

LA name | Name  | Description | Image<sup>1</sup>
--------|-------|------------ |------------------
{% for c in site.data.container_types %}{{ c.reference_name }} | {{ c.name }} | {{ c.description }} | {% if c.image %}![img]({{ site.baseurl }}/images/{{ c.image }}){% endif %}
{% endfor %}


<sup>1</sup>This material has been reproduced from the website [www.partners.wrap.org.uk](http://www.partners.wrap.org.uk) of The Waste and Resources Action Programme.

<sup>2</sup>Often a wheelie bin may simply be called a "bin" as they are the most common form of bins.
