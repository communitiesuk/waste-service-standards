
# Round plan

## Use cases and requirements

The Round plan model should have properties for:

**containers**

> What containers at properties the round will collect from.

**start date**

> When rule starts.

**repeating rule**

> How often the round is run.

**exceptions**

> When dates are exceptions to the repeating rule.


## Properties

Term     | Mapping | Definition
---------|---------|-----------
containers | List of [containers](container.md) | The list of containers at properties that will be emptied.
start date | [schema:startDate](https://schema.org/startDate) | When this plan started.
repeating rule | string | How often a round is executed based on the plan. Typically weekly or fortnightly on a specific day of the week.
exceptions | List of [Date](https://schema.org/Date) | Dates removed from the repeating rule.
additions | List of [Date](https://schema.org/Date) | Extra dates not part of the repeating rule.


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
      <pre><code class="hljs json">{!examples/round_plan.json!}</code></pre>
    </div>
  </div>

</div>




