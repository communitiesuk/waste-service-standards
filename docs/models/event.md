
# Event

## Use cases and requirements

The Event model should have properties for:

**event type**

> What kind of event it is.

**date created**

> 1 Jan 2015

**UPRN**

> For recording against specific properties.

**USRN**

> For recording street-level information.

**coordinates**

> For easy geolocation of where the event was recorded.

**image**

> Visual evidence of an issue.

**comments**

> For any additional information useful to record.



## Properties

Term     | Mapping | Description
---------|---------|------------
event type | string | A categorisation of the event.
date created | string | Timestamp.
uprn | string | A unique identifier for a property.
usrn | string | A unique identifier for a street.
geo | [GeoCoordinates](https://schema.org/GeoCoordinates) | The location in WGS84 datum.
image | [URL](https://schema.org/URL) | A URL to an related image.

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




