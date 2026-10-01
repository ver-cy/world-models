# Grok independent review — EM-TEC-06

Source conversation: https://grok.com/c/57a0ca39-0a90-4d52-a5a1-b5ffc67e8c18

## Verdict

Conditionally complete reserved WM-SFT-016 as the Service Level Objective and Reliability Commitment identifier family. Keep one reserved identity family but do not treat policy, evaluation stream and ObservabilityBinding as one transactional consistency boundary. User Journey remains identifier-unassigned and cannot yet be an evaluable commitment subject.

## Identity and mastership

WM-SFT-016 owns commitment-scoped SLI specification, immutable SLO policy versions, error-budget policy, evaluation stream and associated ObservabilityBinding. Metric formula, population and unit remain external to the identifier-unassigned Metric Definition candidate. WM-MAT-008 owns raw observations and absence semantics. WM-ACT-004 owns Service, the only currently identified evaluable subject. WM-ECO-006 owns contractual SLA obligations and remedies only.

## SLI, SLO, evaluation and budget

SLI specification references Metric Definition and adds a validity filter and goodness predicate. A semantic change to population, unit or goodness creates a successor policy. Published SLO policy versions are immutable and include target, window definition, cadence and effective time. Evaluations are append-only derived facts with met, not-met or unknown states. Error budget is version-scoped. Unknown neither consumes nor refills budget unless a named absence class is explicitly mapped to failure.

## Subject placement and observability

One commitment has one Service subject; a Service may carry multiple commitments. Instance metrics remain diagnostic unless a declared aggregation connects them to the Service SLI. User Journey may be named as a candidate subject kind but remains non-evaluable and unknown until it has identity, ordered membership, aggregation and effective-dated composition.

ObservabilityBinding is an effective-dated coverage map from subject and SLI to WM-MAT-008 streams. Coverage is a precondition for evaluation rather than an observation and reuses WM-MAT-008 absence vocabulary. A binding change does not succeed policy when SLI meaning is unchanged. The binding interval must cover the evaluation slice or the result is unknown.

## Missing data, windows and SLA

No binding or no-observation absence produces unknown, never success. Partial multi-service coverage produces unknown without declared aggregation. Window length or alignment change creates a successor policy and an explicit transition rule: reset, pro-rata carry or dual-run-stricter. Earlier evaluations are never restated merely because a new version begins. Exclusion clauses may belong to policy, while exclusion events remain external and cannot rewrite observations.

WM-SFT-016 remains internal reliability policy. WM-ECO-006 may cite SLO policy or evaluations as evidence but owns contractual obligations, credits and remedies. An SLO miss or exhausted error budget never creates an SLA breach or remedy automatically.

## Scenario and invariants

Services A, B and C are WM-ACT-004 subjects. A and B have coverage while C is missing for part of the window. Each Service evaluates under its own policy version; C is unknown for uncovered slices. The unassigned journey composition A→B→C cannot be recorded as a commitment subject and its derived view is unknown. Changing from rolling 28 days to a calendar month creates a successor policy and named budget transition.

Invariants: missing coverage is unknown; unknown never silently changes budget; policies are immutable; evaluations append; raw observations stay external; instance metrics require aggregation; only identified Service subjects are evaluable; binding coverage must span the slice; Metric Definition remains external; SLA remedies remain contract-owned; one commitment has one subject.

## Blockers

User Journey and Metric Definition remain unassigned. No instance-to-service or service-to-journey aggregation operator is allocated. Exclusion events are untyped. A budget transition choice is required. ObservabilityBinding must remain coverage-only. Packing policy, evaluation stream and binding into one ACID writer boundary would create lifecycle collision. No new identifier or canonical completeness claim is justified.
