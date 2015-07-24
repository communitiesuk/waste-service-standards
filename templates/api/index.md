
{{ api.title }}

{% for r in api.resources %}

## {{ r.display_name }}

`{{ r.path }}`

---
{{ r.description }}

<div class="api-call">
  <span class="rest-method {{ r.method }}">{{ r.method }}</span>
  <span>{{ r.path }}</span>
</div>


{% if r.responses %}
{% for response in r.responses %}

**Response**

```
{{ response.body[0].example | jsonify(indent=2, separators=(',', ': '), sort_keys=False) }}
```

{% endfor %}

{% endif %}

{% endfor %}


