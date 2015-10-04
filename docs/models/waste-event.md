
# Waste event

## Use cases and requirements

The Event model should have properties for:

**event type**

> What kind of event it is.

**start date**

> Know when an event happened.

**location**

> To know what the location information is (property, street, addresss, etc).

**image**

> Visual evidence of an issue.

**comments**

> For any additional information useful to record.

**round**

> The round where this event happened.

**container type**

> What kind of container does the event relate to? This could be typically matched by colour.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
type | string | A categorisation of the event.
start date | [schema:startDate](https://schema.org/startDate) | When the event was took place.
location | [Place](place.md) | A unique identifier for a property.
image | [schema:image](https://schema.org/image) | A URL to a related image.
round | URL | The URL of the round where this event was recorded.
container_type | [Container type](container-type.md) | The type of container, if relevant.


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
      <pre><code class="hljs json">{!schemas/waste_event.schema.json!}</code></pre>
    </div>
    <div role="tabpanel" class="tab-pane active" id="json">
      <pre><code class="hljs json">{!examples/event.json!}</code></pre>
    </div>
  </div>

</div>




