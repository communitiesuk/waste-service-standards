
# Material

## Use cases and requirements

The Material  model should have properties for:

**name**

> What type of material it is.

**colour**

> A colour matching the WRAP material stream, for consistent colour identification.

**image**

> For clear identification, matching physical signage.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
name | string | The name of the material.
color | [schema:color](https://schema.org/color) | The related colour.


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
      <pre><code class="hljs json">{!examples/material_stream.json!}</code></pre>
    </div>
  </div>

</div>




