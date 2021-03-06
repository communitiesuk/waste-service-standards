
# Container type

## Use cases and requirements

The Container type model should have properties for:

**color**

> The general color.

**size**

> Typically in litres.

**shape**

> Wheelie bin, box, caddy, etc.

**lid color**

> In case its different to the body color.

**disposable**

> If the container type is disposable or one-time use, e.g. a bag.

**material stream**

> What kind of waste the container is used for.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
id |  | Unique identifer.
color | [schema:color](https://schema.org/color) | General color as a hex value.
size | integer | Size in litres.
shape | text | The shape or type of the container.
lid color | [schema:color](https://schema.org/color) | Lid-specific color as a hex value.
disposable | boolean | If container is disposable.
material stream | [Material stream](material-stream.md) | The materials used.

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
      <pre><code class="hljs json">{!examples/container_type.json!}</code></pre>
    </div>
  </div>

</div>


## Codelists

### Container shape


