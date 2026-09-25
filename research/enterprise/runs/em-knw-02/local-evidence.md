# EM-KNW-02 local synthesis

## Disposition

- Create an **Enterprise decision, claim and evidence profile** over WM-KNW-010, WM-REC-010, WM-KNW-007 and WM-KNW-008.
- Do not create a profile runtime ID.
- Raise **Evidence Artifact / Source Work** as a genuine new-model candidate with identifier unassigned. The four reserved models intentionally do not master the cited item itself.

## Boundary and ownership

WM-KNW-007 masters claim identity, statement, scope, asserter, commitment, confidence and claim lifecycle. WM-KNW-008 masters the reified citation relationship: citing context, cited source reference, stance, locator, consulted representation, verification and source-status observations. A citation is not evidence truth.

WM-KNW-010 masters decision content: question, alternatives, exclusion reasons, criteria, evaluations, selection, conditions, rationale, arguments, objections and dissent. WM-REC-010 masters the authentic issued expression: fixation, signature/seal, issuance, publication/service evidence, record finality timestamps, redacted expressions and records disposition.

Duplicated REC-010 text fields are version-pinned transcriptions of WM-KNW-010 content. They are never independent authoring fields. Content changes create a successor decision and a successor fixed expression.

## Required profile constraints

1. WM-KNW-010 evidence bindings resolve to WM-KNW-008 citation IDs. Locator, stance and citation type remain read-only projections from WM-KNW-008.
2. Every argument premise/conclusion resolves to a pinned WM-KNW-007 claim or is explicitly marked as a local restatement.
3. Observation/source material, citation stance, claim assessment and decision-local appraisal remain separate.
4. Alternative sets, evaluation rounds, objections and dissent are append-only.
5. WM-KNW-010 declares challenge rules; WM-REC-010 owns service events and computed finality dates.
6. Revocation, annulment, reopening or later counter-evidence never erases earlier rationale or fixed expressions.
7. ADR is a lightweight WM-KNW-010 profile and need not create a formal WM-REC-010 instrument unless one is issued.

## Acceptance result

Two decisions may use separate citations to the same source artifact. If that source is later retracted, each citation receives an append-only status observation and verification report. Related claims retain their canonical statements and gain status-notice/conflict references. Each decision rechecks its own premise support and sensitivity. One may reopen and produce a successor decision while the other remains effective. Original outcomes, alternatives, dissent and fixed records remain resolvable.

The negative case fails: a link to a document supplies only a source reference and citation stance. It cannot turn the citing claim into an established fact.

## Evidence Artifact candidate

The cited work or evidence item has identity and lifecycle independent of every claim, citation and decision. It may be cited many times, corrected, retracted, superseded or preserved while all citation acts remain intact. WM-KNW-008 explicitly caches only a non-authoritative descriptor. This proves a missing aggregate boundary, but no registry identifier is allocated, so the candidate remains research-only.

## Holds

All four existing models remain `publishableCanonical: false`. Their relation ledgers do not yet support the proposed binding; WM-KNW-008 deduplication is insufficiently specified; several serial artefact identities are ambiguous; and three bases carry a single-provider waiver. Evidence Artifact requires registry allocation and its own source/bibliographic/record boundary review. This checkpoint is not an installable release.
