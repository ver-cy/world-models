**DECISION**

**COMPLETE RESERVED MODEL.** Do not allocate another identifier. EM-DAT-06 should complete reserved **WM-REC-002 Report / Statement** as the aggregate for reusable report-definition versions and issued report-statement instances.

The reserved purpose is a governed factual or analytical statement issued for an audience and reporting period. That is the same subject as EM-DAT-06: specification, parameters, issued release, and explainable successor. Legacy 0.2.0 is filing-narrow and not installable; completion generalizes it to analytical and operational reports while keeping filing as a profile, not the only path.

**REUSE ONLY** fails. No published neighbor owns definition-plus-issue semantics. **PROFILE** of WM-REC-001 would collapse period, as-of, cutoff, metric bindings, and disclosure pins into generic documentary fields. **NEW MODEL** is barred unless WM-REC-002 has a different purpose; it does not.

**BOUNDARY CHECK**

A report definition has identity and lifecycle independent of processing runs and record artifacts. WM-ACT-053 records one execution and refuses to absorb reusable definitions. WM-REC-001 owns the documentary object: identity, immutable versions, instantiations, signatures, custody, and disposition. The same definition may drive many runs and many artifacts.

One catalogue aggregate should own both grains: **ReportDefinitionVersion** and **ReportIssue**. The issue is meaningless without a pinned definition. This matches legacy `reportTemplate` + `report` and the form-definition versus form-instance split elsewhere in REC. Do not split them into two catalogue IDs. Do not fold runs, files, or publication cases into the same object.

Corrected inputs create a **successor issue**. The published predecessor stays immutable and retrievable. The successor carries predecessor reference, correction reason, authority, new input snapshot, new run evidence, and new artifact refs. Status may become superseded; identity and payload are never mutated. This is the same non-overwrite rule as record supersession, run correction, and publication non-cascade.

Aggregation and suppression remain bound to the exact WM-XCT-003 version plus compiled-template fingerprint stored on the issue. Later policy or dashboard change cannot unhide a previously suppressed slice. Aggregation does not cancel the pinned policy.

Separation that must hold:

| Object | Owner | Role |
|---|---|---|
| Definition version + issued statement | WM-REC-002 | Meaning, pins, successor lineage |
| Processing run | WM-ACT-053 | Execution evidence; referenced |
| Record artifact | WM-REC-001 | Carrier, fixity, custody; referenced |
| Publication case | WM-ACT-044 | Release instruction and delivery; referenced |
| Publication edition | WM-MED-003 | Bibliographic edition when the statement is also a published product; referenced |
| Disclosure policy | WM-XCT-003 | Shape, grain, treatment; pinned, not owned |
| Official-statistics product | WM-DAT-002 | Referenced when the issue is that product |
| Catalog / data product | WM-DAT-008 | Discovery metadata; not the issued statement |

Card candidate types `ReportRun` and `PublicationRecord` are working vocabulary, not objects to absorb. EM-DAT-05 keeps metric and observation mastership; EM-DAT-07 keeps study justification. REC-002 shows results; it does not master formulas or justify conclusions.

**MINIMAL PORTABLE CONTRACT**

WM-REC-002 owns two object kinds and the lineage between them. Neighbors stay REFERENCE-only.

On **ReportDefinitionVersion**: definition identity, version, predecessor definition, audience class, reporting grain, parameter schema, metric or query bindings by reference, permitted projection set, default disclosure-policy binding, authority, and status.

On **ReportIssue**:

- `issueId`, `definitionVersionId`, `predecessorIssueId`
- `audienceClass`, `reportingPeriod`, `cutoffRule`, `cutoffInstant`, `asOfInstant`, `asOfBasis`
- declared and resolved `parameterSet`
- `inputSnapshotRefs`
- `metricOrQueryBindings` (refs, not inline formulas)
- disclosure tuple: policy version + schema version + treatment-matrix version + compiler id + compiled-template fingerprint
- `processingRunRef`, `recordArtifactRefs` with digests
- optional `publicationCaseRef`, `editionRef`, `attestationRef`
- `issuanceInstant`, `issuanceStatus`, `correctionReason`, `authorityRef`

Reproducibility is this pin set, not a live query. Portable semantics are identities, versions, period and as-of, cutoff, bindings, grain, disclosure pin, snapshots, run and artifact refs, successor links, and issuance or attestation status. Not portable: widget layout, theme, slicer chrome, cache TTL, personalization, vendor DAX or M, or tool SQL unless bound as a versioned query artifact by digest.

Minimum invariants: a run pins definition and input snapshot; a corrected release does not overwrite the published predecessor; aggregation does not cancel the pinned disclosure policy; an issue without a definition version is invalid; a live view is not an issue; widening a policy requires a new issue; artifact digest change without a new issue is a custody event, not a restatement.

**DASHBOARD DISPOSITION**

A dashboard definition is a **profile of ReportDefinition**: a named set of permitted projections, or a view of an explicitly modeled aggregate. That is the assignment’s own wording and it should stay.

A live dashboard remains ephemeral. Filters, refresh, and personalization do not issue a statement. An issue exists only when the reproducibility tuple is snapshotted. After the dashboard layout changes, prior issues stay explainable because they pin definition version, snapshots, run, artifacts, and disclosure tuple—not the current tile layout.

**ACCEPTANCE SCENARIO**

1. Issue report R1 for audience A and period P, pinning definition D1, cutoff/as-of, input snapshot S1, run E1, artifacts F1, and disclosure-policy version V1. Sensitive slice X is suppressed under V1.
2. Correct an upstream fact. Create snapshot S2 and run E2. Issue successor R2 with predecessor R1, reason, and authority. R1 remains published and reconstructable from D1, S1, E1, F1, V1.
3. Both versions remain explainable: each issue states which definition, inputs, period, cutoff, as-of, run, artifacts, and policy produced it.
4. Slice X stays hidden on R1 and on any R2 still pinned to V1. A wider policy V2 cannot rewrite R1; it can only authorize a new issue.
5. The dashboard is later redesigned. R1 and R2 still resolve. Layout is not part of issue identity.

Negative case remains invalid: one projection that joins arbitrary HR and financial objects without a rights and disclosure-policy check.

**HOLDS AND PUBLICATION RECOMMENDATION**

Complete WM-REC-002 under the research contract as a reviewable 0.3 draft. Do not treat 0.2.0-legacy as finished or installable. Resolve the stub’s unmet requires (identifier naming, organization, official statistics, calendar) by reference, not by copying those models.

Publication holds until: public-source crosswalk to DCAT, PROV, Data Cube, and SDMX; fixtures for successor issue and pinned suppression; explicit non-ownership of run, artifact, publication case, edition, metric, and official-statistics product; Dimension-declared identity rules for definition versus issue; second-provider review; no private enterprise instance data.

Recommended first publication statement: WM-REC-002 owns report-definition versions and issued statements; it references processing runs, record artifacts, publication operations, publication editions, and disclosure-policy versions without duplicating their lifecycles.