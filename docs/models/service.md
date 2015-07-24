
# Service

## Use cases and requirements

The Service model should have properties for:

**name**

> For identification.

**frequency**

> An indication of typically how often the collection is run.

**description**

> For specific instructions about the service, such as when and where to put containers out, that bin lids must be closed, etc.

**next collections**

> To know upcoming dates of when upcoming collections will happen.

**previous collections**

> To know when the last few collections have taken place.

**material stream**

> What kinds of materials are handled by this service.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
name | Text | Name of the service.
frequency | Text | How often it runs, e.g. weekly.
description | [schema:description](https://schema.org/description) | A short description of the service.
next collections | Date | List of dates of next collections.
previous collections | Date | List of dates of previous collections.
material stream | ? | The material stream that is collected.


## Serialisation

<div>

  <!-- Nav tabs -->
  <ul class="nav nav-tabs" role="tablist">
    <li role="presentation"><a href="#schema" aria-controls="schema" role="tab" data-toggle="tab">JSON Schema</a></li>
    <li role="presentation" class="active"><a href="#json" aria-controls="json" role="tab" data-toggle="tab">JSON</a></li>
  </ul>

  <!-- Tab panes -->
  <div class="tab-content">
    <div role="tabpanel" class="tab-pane" id="schema">
    </div>
    <div role="tabpanel" class="tab-pane active" id="json">
      <pre><code class="hljs json">{!examples/service.json!}</code></pre>
    </div>
  </div>

</div>

## Codelists

### Freqency
TBD



