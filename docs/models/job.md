
# Job

A job could prepresent any form of work required in the council's region, e.g.:

* a scheduled bin collection
* cleanup of a fly tip
* maintenance of a street


## Use cases and requirements

The Job model should have properties for:

**name**

> What the job is.

**description**

> More details about the job.

**status**

> Whether the job is pending, started, completed, etc.

**location**

> The information if it relates to a property or street location.


## Types

This Job type extends from the [Action](http://schema.org/Action) schema.org type.

### Sub-types

Just as Action and other common types have a number of sub-types, here are specific Job sub-types for different kinds of services councils provide:

* BinCollectionJob
* StreetCleansingJob
* FlytippingCleanupJob


## Properties

Term     | Mapping | Definition
---------|---------|-----------
name | [schema:name](http://schema.org/name) | Identifer for the job.
description | [schema:description](https://schema.org/description) | A short description of the job.
status | [schema:actionStatus](http://schema.org/actionStatus) | The status of the job.
location | [schema:location](http://schema.org/location) | Location information.


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




