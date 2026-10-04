# EM-FIN-05 provider comparison

Claude and Grok agree on the six-fact separation, reuse of WM-FLW-015 for usage, profiling of unit-cost observations over WM-MAT-008 plus Metric Definition, immutable executions, explicit residuals, one axis and currency per run, conservation, non-additive parallel axes, and explicit treatments for discount, reserved capacity and untagged usage.

## Divergence and resolution

Grok requested separate registry model identifiers for Rule, Run and Result while also treating Run as the aggregate citation root. The frozen audit identified this as a model-identifier/object-identifier conflation. The reconciled candidate keeps one identifier-unassigned Cost Allocation cluster with four independently addressable object identities: Rule, RuleRevision, Run and Result. A run is the citation root and a result is cited by `(allocationRunId, resultId)`. Object citation does not depend on allocation of a registry model identifier. No identifier is allocated or guessed.

Rule is cluster-owned and reusable rather than run-contained. Results are run-contained, immutable and addressable. CostRecord is explicitly modeled as a typed bridge to external fact owners. UnitCostObservation remains a profile with no new identity. Commitment-instrument mastership remains held instead of introducing an unsupported candidate.

`invariants.json` is the sole normative set. The provider studies are evidence and carry no competing normative list. Canonical publication remains held by registry allocation, base and relation approval, unbound commitment mastership, immutable pins and executable crosswalk validation.
