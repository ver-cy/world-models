# EM-PRD-03 local synthesis

## Disposition

- Complete and reclassify reserved WM-REC-006 as a Requirement aggregate with stable family identity and immutable revisions.
- Contain Acceptance Criteria under exact Requirement revisions. Keep reusable Rule identity, predicate semantics, operands, units, tolerance and evaluation contract in WM-KNW-013 and pin exact Rule revisions.
- Keep Trace Link as a single-owner outbound association whose source is one Requirement revision. The target remains externally mastered; inbound traces are derived projections.
- Remove authoritative Requirement Baseline from this aggregate. Its independent authority, effectivity and successor lifecycle justify an identifier-unassigned candidate for separate reservation review.
- Provide only a derived non-authoritative RequirementRevisionSetView over caller-supplied exact Requirement revision, criterion and Rule pins. It owns no set, approval, effectivity, successor lifecycle, verdict or stored diff.
- Keep inter-Requirement conflict identity and lifecycle in an external issue, case or decision master.
- Keep stakeholder Need, feature/design, task/work order, test/result, evidence, waiver, decision, evaluation and enforcement in their source masters.

A stakeholder Need retains as-authored wording. A Requirement is authority-issued and verifiable. Feature/design proposes realization; task records implementation work. None proves satisfaction. Requirement Acceptance Criterion remains distinct from WM-ACT-007 work-order acceptance findings.

A Rule-pinned criterion cannot override Rule predicate, unit or tolerance locally. A reusable threshold change creates a new Rule revision and re-pin. Conversion to a one-off condition removes the Rule pin, records provenance and creates a Requirement revision.

A revision-set view pins identities and content digests only. It never freezes satisfaction, verification, waiver, compliance or decision verdicts. Diffs are recomputed. If source access is incomplete, the view is `partial-redacted` and cannot imply complete coverage.

## Scenario result

R@rev1 has AC1, three Done tasks and one failed test. It remains unsatisfied or inconclusive and the failure stays visible. Caller-supplied set S1 includes R@rev1. A tolerance change creates R@rev2, AC2 and, when reusable, a new Rule revision pin; S2 includes the successor. The derived comparison reports revision, criterion, tolerance and Rule-pin changes. It is not an authoritative Baseline, stores no verdict and does not carry the failed result to rev2.

## Frozen-audit reconciliation

The single audit returned `REVISE`. Six issues were remediated without rerun: latent Baseline aggregate, unowned conflict, Rule-pin override, mirrored internal traces, verdict sealing and redaction completeness. The final candidate contains 35 constraints, five external relations and 33 fixtures.

## Holds

WM-REC-006 lacks a canonical specification. Requirement Baseline needs separate allocation review. The relation ledger must retire the WM-KNW-013 parent signal. Held bases and external task/test/evidence/waiver/conflict/decision masters remain dependencies. Trace vocabulary, field-level mastership and disclosure rules need approval. Package conversion and live verification remain pending.
