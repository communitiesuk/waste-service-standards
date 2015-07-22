
{{ api.title }}

{% for r in api.resources %}
## {{ r.path }}

`{{ r.method }}`
{{ r.description }}

{% if r.responses %}
{% for response in r.responses %}

**Response**

```
{{ response.body[0].example | jsonify(indent=2, separators=(',', ': ')) }}
```

{% endfor %}

{% endif %}

{% endfor %}


