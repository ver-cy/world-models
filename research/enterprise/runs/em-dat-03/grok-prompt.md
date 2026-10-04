# Exact unsent Grok prompt — EM-DAT-03

Independent enterprise metamodel review. Do not browse, invent identifiers or claim standards conformance.

EM-DAT-03 covers Data Pipeline, Pipeline Run, Transformation and Lineage Assertion. Reserved boundaries are WM-DAT-005 for reusable pipeline definitions, WM-ACT-053 for executions, and WM-DAT-006 for lineage assertions. Dataset/schema masters and generic provenance remain external.

Assess this proposed disposition: use a profile across the three reserved models; do not create a Transformation model; map definition component plus pinned logic to executed task/attempt and then to an observed lineage edge. Keep intended topology separate from observed lineage. Each run pins definition, code, inputs and interval. Each edge declares granularity, capture method, producer, confidence and evidence. Correlation or matching column names never proves direct derivation. Missing lineage means unknown unless a closed-world perimeter is declared. Manual corrections are evidenced activities without invented runs; opaque inputs are boundary nodes with unresolved ancestry. Reproducibility requires an immutable processing-context manifest.

Test two runs where one retry is preserved, a manual correction changes the output, and an external input has unknown ancestry. Return <=900 words with: Verdict; strongest evidence; strongest counterexample; identity/mastership; transformation placement; partial-lineage rules; reproducibility gate; scenario; at least 10 invariants; minimum completion shape; blockers. Explicitly decide whether Transformation needs an independent lifecycle and whether a lineage assertion is an aggregate root or a dependent record.
