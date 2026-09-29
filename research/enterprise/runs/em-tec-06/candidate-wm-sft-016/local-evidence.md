# EM-TEC-06 local synthesis

## Reconciled disposition

Reserved WM-SFT-016 is conditionally completed as one identifier family with four separate consistency boundaries: immutable policy, append-only evaluation, effective-dated observability coverage binding and derived budget state. No new model or runtime identifier is allocated. Policy/evaluation/budget/binding remain internal artifacts.

Only an identified WM-ACT-004 Service is currently evaluable. Metric Definition still owns formula, population and unit but is identifier-unassigned, so canonical enforceable SLI meaning remains held. WM-MAT-008 owns observations and absence evidence. WM-XCT-009 is the calendar authority. WM-ECO-006 owns contractual SLA obligations, breach mappings, credits and remedies. User Journey remains a specified-deferred-non-normative candidate and cannot receive a verdict.

## Applied provider and audit rules

Policies immutably pin target unit, window/calendar, eligibility, exclusions and absence-to-failure mapping. Binding versions are coverage-only, unique per Service/SLI/instant and define deterministic multi-stream combination. Every evaluation stamps policy, binding and absence-mapping versions and reports coverage ratio and unknown count. Missing coverage is unknown and budget-neutral unless policy explicitly maps a named absence class to failure. Complete coverage with no eligible events is the distinct budget-neutral `no-eligible-traffic` outcome.

Exclusion means present-but-ineligible and is distinct from absence. Retroactive exclusion appends a superseding evaluation and retains the predecessor. Budget consumption is recomputed from evaluations; any balance is a disposable cache. Window/target changes require contiguous, non-overlapping succession and an immutable reset, carry or prorate transition. Retraction is independent of succession, closes new evaluation and retains invalidated evidence. Service retirement closes policy; rename, merge, split or re-identification requires succession.

Diagnostics may support triage but never determine verdict, budget or obligation. The SLA firewall applies both ways: WM-SFT-016 creates no contractual breach/remedy, while WM-ECO-006 cannot define SLI/SLO semantics or infer breach from a verdict without an explicit contract-owned mapping.

## Verification and holds

The exact public Grok prompt was sent once and reconciled. One Claude Opus high no-tools frozen audit was run; its blocking findings were remediated without rerun. Fixtures now cover binding succession/overlap/combination, absence mapping, empty populations, retroactive exclusions, retraction, partial-window transitions, Service lifecycle changes, calendar discontinuity, Journey rejection, SLA leakage, verdict coverage reporting and diagnostic misuse.

Publication stays held for Metric Definition and User Journey allocation, exclusion-event authority, binding precedence and aggregation contracts, base canonical constraints, executable acceptance and live HTTP/runtime/search/package verification.
