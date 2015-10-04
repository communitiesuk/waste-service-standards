
# Round

## Use cases and requirements

The Round model should have properties for:

**name**

> An identifier for this round.

**date**

> When this round took place.

**round plan**

> A reference to which Round plan was used.

**events**

> Any related events that have been recorded.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
name | [schema:name](http://schema.org/name) | Identifer for the round.
date | Date | When the round took place.
round plan | [Round plan](round-plan.md) | The round plan this round is based on.
events | List of [Events](waste-event.md) | Events that happened on the round.


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
      <pre><code class="hljs json">{!examples/round.json!}</code></pre>
    </div>
  </div>

</div>




