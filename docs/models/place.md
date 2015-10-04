
# Place

## Use cases and requirements

The Address model should have properties for:

**address fields**

e.g. street, locality, country, postcode.

> To provide basic address information that everyone understands.

**UPRN**

> To link an address to the property universal ID.

**USRN**

> To identify the street where the property is located.

**geo**

> To be able to plot locations on maps.



## Types

This maps to the [schema.org Place type](http://schema.org/Place) with some extended fields.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
address | [schema:address](https://schema.org/address) | Physical address of the item.
uprn | Text | A unique identifier for a property.
usrn | Text | A unique identifier for a street.
geo | [schema:geo](https://schema.org/geo) | The location in WGS84 datum.


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
      <pre><code class="hljs json">{!examples/place.json!}</code></pre>
    </div>
  </div>

</div>




