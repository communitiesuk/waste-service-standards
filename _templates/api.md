---
layout: doc
title: 
---

# {{ api.title }}

{% if api.documentation %}
{% for doc in api.documentation %}
## {{ doc.title }}
{{ doc.content }}
{% endfor %}
{% endif %}

{% for r in api.resources %}

<!-- Hacky check to see if this resource is a root item and ensure it isnt
repeated for GET, POST, etc. It assumes there is always the GET method! -->
{% if r.name == r.path and r.method == 'get' %}
<h2 id="{{ r.display_name }}">{{ r.display_name }}</h2>
{% endif %}

<hr/>
<h4>{{ r.description }}</h4>

<div class="api-call">
  <span class="rest-method {{ r.method }}">{{ r.method }}</span>
  <span>{{ r.path }}</span>
</div>

{% if r.query_params %}
**Query parameters**

Name | Type | Description
-----|------|------------
{% for param in r.query_params %}<tt>{{ param.name }}</tt> | {{ param.type }} | {% if param.desc != None %}{{ param.desc }}{% endif %}
{% endfor %}
{% endif %}

{% if r.responses %}
{% for response in r.responses %}
**Example response**
{{ '{% highlight json %}' }}
{{ response.body[0].example | jsonify(indent=2, separators=(',', ': '), sort_keys=False) }}
{{ '{% endhighlight %}' }}
{% endfor %}
{% endif %}



{% endfor %}


