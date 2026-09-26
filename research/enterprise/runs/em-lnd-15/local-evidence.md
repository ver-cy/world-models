# EM-LND-15 local synthesis

## Disposition

- Define Risk Landscape as a governed view definition with immutable snapshots over risk, requirement, control, assessment, audit, finding, obligation and evidence masters.
- Define Assurance Coverage View as a projection of that landscape with explicit denominator and caveats.
- Both need artifact/view identity for reproducibility but no independent subject-model identity. Allocate no runtime/model identifier.

## Identity and mastership

WM-KNW-015 masters risk entities and register membership. WM-XCT-027 supplies host-scoped assessment context and retained risk fields but must not master control state after its split decision. Control remains an identifier-unassigned candidate from EM-RSK-01. WM-ACT-034 profiles control/applicability assessments; WM-ACT-033 owns review/audit engagements and findings; WM-POL-001/WM-KNW-012 requirements; WM-XCT-029 obligations; WM-MAT-008 observations.

The landscape reads these masters, records pending-master markers and never copies control state from disclaimed WM-XCT-027 bundles.

## Scope, requirements and controls

The view pins subjects, jurisdictions, requirement expressions/provisions, control catalogue revision, criteria/taxonomy versions and cut-off. Applicability is an assessment that pins subject state, jurisdiction, facts-as-of and norm version; indeterminate and disputed remain separate outcomes.

Requirement, obligation, control and evidence remain distinct. A current control determination is required before attributing risk reduction. Reliance without determination is explicit.

## Coverage, compliance, assurance and risk

Coverage is structural mapping over an explicit applicable population. Compliance is evidenced obligation fulfilment. Assurance is an examination with scope, method, exclusions and assurance level. Residual risk is a post-control estimate supported by current determinations. They use separate denominators and never collapse into one percentage.

Control existence, design, implementation, operation and effectiveness are independent. A document, completed card, mapping or incident-free period proves none of the later states. Effectiveness conclusions name method, vocabulary, validity and invalidation triggers.

## Assessments, audits, exceptions and time

The trace chain is requirement→applicability→control→assessment→evidence→finding→conclusion→residual attribution. Findings remain engagement-owned; observations never become findings automatically.

Exceptions record authority, beneficiary, scope, interval and compensating duty. Expiry changes the exception, flags dependent conclusions for revalidation and suspends reliance; it does not change the requirement itself.

Event, observation/as-of and record times remain distinct. Currency is recomputed against caller-supplied cut-off. Expired conclusions remain readable but cannot ground new acceptance. Aggregation requires comparable criteria, method, scope, horizon and taxonomy pins; caveats cannot be stripped.

## Acceptance scenario

Control C-1 is designed and implemented but has no required execution in the period, so operating/effectiveness status is unsupported. Requirement R-7 has no applicability conclusion and is reported as a scope gap outside numerator and denominator. Exception X-3 expired before cut-off, so dependent conclusions become revalidation-pending. A 100% card-completion measure reports register currency only and proves no coverage or compliance.

## Invariants

1. Coverage, compliance, assurance and residual risk remain distinct.
2. Every quantity declares denominator and exclusions.
3. Completed documentation is never effectiveness evidence.
4. Design, implementation, operation and effectiveness remain independent.
5. Applicability is an assessment, never a default flag.
6. Indeterminate and disputed outcomes remain countable.
7. Exceptions preserve authority, scope and expiry.
8. Expired conclusions remain visible but not current.
9. Risk reduction requires a current cited determination.
10. Aggregation requires a comparability verdict.
11. Snapshots never re-master or recompute source item values.
12. Pending Control master status remains explicit.

## Minimal profile shape

Risk Landscape records viewpoint/questions, perimeter, requirement/control/criteria pins, cut-off, membership/construction rules, comparability/caveats, denominators/exclusions, gap sets, pending-master markers, owner/reviewer, snapshot digest, access and retention. Assurance Coverage Projection records parent view, quantity, denominator, numerator rule, per-cell states, caveats and digest.

## Holds

Targets remain non-canonical single-provider drafts. WM-XCT-027's split is unresolved, WM-ACT-034 remains a candidate and relationship contracts are empty. Control has no allocated identifier, making coverage provisional. Crosswalks, source pins and fixtures remain unverified. This checkpoint is not legal advice and makes no canonical completeness, installability or publication claim.
