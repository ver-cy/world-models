# WM-KNW-010 bounded Claude research plan

The normal monolithic Claude pass returned the same API error twice after
roughly ten minutes. The diagnostic wrappers classified both failures as API
or network errors, not authentication, subscription, quota, schema or
permission failures. No provider result was produced, so the validated bounded
split workflow is used instead.

The three passes are deliberately non-overlapping at the structural level:

1. `core` owns decision identity, problem framing, alternatives, criteria,
   evaluation, selection and outcome.
2. `reasoning` owns rationale, evidence bindings, assumptions, uncertainty,
   trade-offs, argumentation, dissent and explainability.
3. `governance` owns authority, participation, lifecycle, review, provenance,
   access, retention, audit and all canonical service-layer rules.

Every pass must satisfy the complete provider schema and local validator. The
deterministic merger stable-unions sources and assigned structure, keeps the
model boundary from `core`, keeps service layers from `governance`, and fails
on identity mismatches, duplicate IDs or questions, unresolved citations or a
final validation error. A normal single-provider no-tools adjudication remains
mandatory after the merge.

Coverage is routed only after all parts validate. Every checklist dimension is
selected from its designated subject owner instead of concatenating partial
claims. Plain-text and structured `SRC-###` references are remapped together;
an unknown reference fails the merge.
