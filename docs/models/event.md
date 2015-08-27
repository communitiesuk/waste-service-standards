
# Waste event

## Use cases and requirements

The Event model should have properties for:

**event type**

> What kind of event it is.

**start date**

> Know when an event happened.

**UPRN**

> For recording against specific properties.

**USRN**

> For recording street-level events.

**coordinates**

> For easy geolocation of where the event was recorded.

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
start date | string | When the event was took place.
uprn | string | A unique identifier for a property.
usrn | string | A unique identifier for a street.
geo | [schema:geo](https://schema.org/geo) | The location in WGS84 datum.
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
    </div>
    <div role="tabpanel" class="tab-pane active" id="json">
      <pre><code class="hljs json">{!examples/event.json!}</code></pre>
    </div>
  </div>

</div>




