

Name | Type | Description
-----|------|------------
{% for param in r.query_params %}<tt>{{ param.name }}</tt> | {{ param.type }} | {% if param.desc != None %}{{ param.desc }}{% endif %}
{% endfor %}