
# Container

## Use cases and requirements

The Container model should have properties for:

**container type**

> For the common properties of the container.

**serial number or ID**

> For identification of the container.

**barcode, RFID number**

> If the container has been tagged with a barcode or RFID chip.

**UPRN**

> To link to its property.

**status**

> Capture whether in-use, damaged, etc.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
id | string | Unique identifer.
type | [Container type](container-type.md) | The type of container.
barcode | integer | A barcode number.
RFID | integer | A RFID tag number.
status | string | The status of the container.


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
      <pre><code class="hljs json">{!examples/container.json!}</code></pre>
    </div>
  </div>

</div>


## Codelists

### Status

* in service
* damaged




