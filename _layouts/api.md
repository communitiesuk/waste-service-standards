
# {{ api.title }}

{% if api.documentation %}
{% for doc in api.documentation %}
## {{ doc.title }}
{{ doc.content }}
{% endfor %}
{% endif %}

{% for r in api.resources %}

{% if r.name == r.path %}
## {{ r.display_name }}
{% endif %}

---
{{ r.description }}

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
**Response**
```
{{ response.body[0].example | jsonify(indent=2, separators=(',', ': '), sort_keys=False) }}
```
{% endfor %}
{% endif %}



{% endfor %}


