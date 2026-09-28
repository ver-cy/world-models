# Frozen no-tools semantic audit — EM-DAT-06

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers or grant publication authority.

Disposition: COMPLETE RESERVED MODEL for WM-REC-002 Report / Statement. No new identifier is allocated. Audit the reconciled boundary and candidate semantics only.

Audit questions:
- Does one aggregate safely own immutable report-definition versions and issued report statements without merging their identities?
- Do issue pins make a release reproducible and explainable after corrected inputs, dashboard changes and disclosure-policy changes?
- Are processing run, record artifact, publication operation, edition, metric definition, official-statistics product and catalogue metadata correctly reference-only?
- Do correction, suppression, widening, artifact-custody and ephemeral-dashboard cases fail closed?
- Is any field deployment policy, BI configuration or accidental second authority?
- Which inherited holds prevent canonical publication while still allowing a reviewable completion draft?

Return at most 500 words with exactly: Verdict (ACCEPT WITH LIMITS, REVISE, or REJECT); Critical findings; Required holds; Scenario result; Identifier decision. Treat registry relation approval and inherited neighboring-model blockers as holds unless they contradict the candidate.

## Candidate

{
  "format": "vercy-world-model-candidate/v1",
  "contourId": "EM-DAT-06",
  "modelId": "WM-REC-002",
  "registryId": "vr.wm-rec-002",
  "name": "Report / Statement",
  "version": "0.1.0-candidate.2",
  "entryKind": "aggregate",
  "status": "research-candidate",
  "canonicalPublishable": false,
  "purpose": "Represent a reusable governed report definition and each immutable issued factual or analytical statement without conflating computation, artifact custody, publication or edition identity.",
  "boundary": {
    "owns": [
      "stable report-definition identity and immutable definition versions",
      "parameter contract, declared grain and metric or query bindings",
      "report-issue identity, lifecycle and successor lineage",
      "reporting period, cutoff, as-of basis and issue time",
      "pinned input snapshots, execution evidence and disclosure tuple",
      "suppression manifest and explanation references"
    ],
    "delegates": [
      "processing execution to WM-ACT-053",
      "record artifact, fixity and retention to WM-REC-001",
      "delivery and correction propagation to WM-ACT-044",
      "allowed output shape and disclosure policy to WM-XCT-003",
      "bibliographic edition identity to WM-MED-003",
      "fiscal and civil calendar semantics to WM-XCT-009"
    ],
    "excludes": [
      "BI layout or vendor dashboard configuration",
      "metric-definition mastership",
      "data-pipeline execution and retry state",
      "record retention or physical rendition custody",
      "publication-channel delivery and audience receipt",
      "legal or regulatory acceptance of reported assertions"
    ]
  },
  "definitionVersion": {
    "identity": [
      "definitionId",
      "definitionVersionId",
      "version"
    ],
    "required": [
      "title",
      "purpose",
      "audienceClass",
      "parameterContract",
      "declaredGrain",
      "measureOrQueryBindings",
      "permittedProjectionSet",
      "defaultDisclosurePolicyBinding",
      "authorityRef",
      "effectiveFrom",
      "status"
    ],
    "optional": [
      "audienceClass",
      "scheduleHint",
      "layoutProfileRef",
      "fiscalCalendarRef",
      "supersedesDefinitionVersionId",
      "calendarBasisRef"
    ],
    "lifecycle": [
      "draft",
      "issued",
      "superseded",
      "withdrawn"
    ]
  },
  "reportIssue": {
    "identity": [
      "reportIssueId"
    ],
    "required": [
      "definitionVersionId",
      "audienceClass",
      "boundParameters",
      "reportingPeriod",
      "cutoffRule",
      "cutoffAt",
      "asOfBasis",
      "calendarBasis",
      "issuedAt",
      "inputSnapshots",
      "measureOrQueryBindings",
      "executionEvidenceRefs",
      "disclosurePolicyTuple",
      "compiledTemplateFingerprint",
      "suppressionManifest",
      "recordArtifactRefs",
      "authorityRef",
      "status"
    ],
    "optional": [
      "publicationRefs",
      "editionRefs",
      "coverageExceptions",
      "restatementClass",
      "restatementReason",
      "supersedesReportIssueId",
      "attestationRefs",
      "explanationRefs"
    ],
    "lifecycle": [
      "planned",
      "computed",
      "issued",
      "superseded",
      "withdrawn"
    ]
  },
  "relations": [
    {
      "target": "WM-ACT-053",
      "relation": "REFERENCE",
      "purpose": "Pin processing-run evidence without importing execution lifecycle.",
      "required": false
    },
    {
      "target": "WM-REC-001",
      "relation": "REFERENCE",
      "purpose": "Resolve immutable artifacts, fixity, custody and retention.",
      "required": false
    },
    {
      "target": "WM-ACT-044",
      "relation": "REFERENCE",
      "purpose": "Resolve delivery and correction-propagation operations.",
      "required": false
    },
    {
      "target": "WM-XCT-003",
      "relation": "REFERENCE",
      "purpose": "Pin disclosure policy, output shape, binding and schema version.",
      "required": false
    },
    {
      "target": "WM-MED-003",
      "relation": "REFERENCE",
      "purpose": "Resolve bibliographic publication or edition identity.",
      "required": false
    },
    {
      "target": "WM-XCT-009",
      "relation": "REFERENCE",
      "purpose": "Pin calendar identity, version, timezone and period convention without owning calendar arithmetic.",
      "required": false
    },
    {
      "target": "WM-DAT-002",
      "relation": "REFERENCE",
      "purpose": "Resolve official-statistics product identity when the issue is such a product.",
      "required": false
    },
    {
      "target": "WM-DAT-008",
      "relation": "REFERENCE",
      "purpose": "Resolve optional data-product or catalogue discovery metadata without importing issue identity.",
      "required": false
    }
  ],
  "operations": [
    {
      "id": "issue-report",
      "effect": "Create an immutable issued report statement from one definition version and a complete evidence tuple.",
      "authority": "authorized report issuer"
    },
    {
      "id": "supersede-definition",
      "effect": "Issue a new definition version while preserving the predecessor.",
      "authority": "definition steward"
    },
    {
      "id": "restate-report",
      "effect": "Issue a successor statement with a restatement class, reason and predecessor reference.",
      "authority": "authorized report issuer"
    },
    {
      "id": "withdraw-report",
      "effect": "Mark an issued statement withdrawn without deleting its evidence or lineage.",
      "authority": "authorized report issuer"
    },
    {
      "id": "snapshot-dashboard",
      "effect": "Mint a citable report issue from an ephemeral view by freezing cutoff, inputs, policy and evidence.",
      "authority": "authorized report issuer"
    }
  ],
  "invariants": [
    "Every report issue pins exactly one immutable report-definition version.",
    "Bound parameters validate against the pinned definition version.",
    "Input dataset versions, partitions and digests are immutable issue evidence.",
    "Reporting period, cutoff, as-of basis and issue time remain distinct.",
    "Execution evidence covers the declared period or records a coverage exception.",
    "Asserted grain never exceeds the shape allowed by the pinned disclosure policy.",
    "Suppression records policy version and reason without leaking withheld values.",
    "Correction or changed input creates a successor issue; an issued issue is never overwritten.",
    "Restatement lineage is acyclic and has one current head per definition, parameter set and period.",
    "Publication does not prove report validity, and report validity does not prove publication.",
    "Report issue, processing run, record artifact, publication operation and edition use disjoint identifiers.",
    "Explanation references remain resolvable for the applicable retention period.",
    "A fiscal or civil reporting period pins calendar identity, calendar version, timezone and period convention.",
    "An issue without one pinned definition version is invalid.",
    "Widening a disclosure policy or projection requires a new issue and never rewrites a predecessor.",
    "Changing only a record-artifact digest is a custody event unless report meaning or evidence changes.",
    "A dashboard layout, theme, slicer or cache setting never participates in report-issue identity."
  ],
  "dashboardDisposition": {
    "definition": "A dashboard definition is a profile of a report definition with external layout and refresh metadata.",
    "liveView": "An ephemeral live view is not a report issue.",
    "snapshot": "A citable dashboard snapshot mints a report issue with a frozen evidence tuple."
  },
  "holds": [
    "One frozen no-tools semantic audit of the reconciled candidate is pending.",
    "Neighboring model relations remain candidate rows and grant no cascade authority.",
    "Metric-definition authority remains an identifier-unassigned EM-DAT-05 research candidate.",
    "External product and standards crosswalks are alignment notes, not conformance claims.",
    "Multi-grain disclosure validation remains declarative until WM-XCT-003 validation is executable.",
    "Canonical publication requires relation approval, package conversion and live verification."
  ]
}

## Fixtures

{
  "format": "vercy-world-model-candidate-fixtures/v1",
  "modelId": "WM-REC-002",
  "fixtures": [
    {
      "id": "issue-and-restate",
      "input": "Issue A pins definition v1.2, parameters, input snapshots, run R1 and disclosure policy P7. An upstream fact is corrected.",
      "expected": "Issue B pins the corrected snapshots and run R2, explicitly supersedes A and leaves A immutable and explainable."
    },
    {
      "id": "suppressed-slice",
      "input": "A sensitive cohort fails the minimum disclosure threshold under policy P7.",
      "expected": "The issue records the suppressed slice, P7 version and suppression reason without retaining or leaking the withheld value."
    },
    {
      "id": "dashboard-change",
      "input": "A dashboard layout and current filters change after a citable snapshot was issued.",
      "expected": "The prior report issue remains reproducible from its frozen definition, parameters, cutoff, inputs, policy and evidence."
    },
    {
      "id": "run-is-not-report",
      "input": "A processing run completes successfully but no authorized report issue is created.",
      "expected": "The run is execution evidence only and does not become an issued report or prove publication."
    },
    {
      "id": "artifact-is-not-issue",
      "input": "One report issue is rendered as PDF, HTML and CSV records.",
      "expected": "All renditions retain record identities and fixity while referencing one report-issue identity."
    },
    {
      "id": "invalid-overwrite",
      "input": "A producer attempts to replace the inputs and values of an already issued statement in place.",
      "expected": "Validation rejects the mutation and requires a successor issue with restatement lineage."
    },
    {
      "id": "fiscal-period-pin",
      "input": "A report covers fiscal Q4 under calendar version FY-2026-EU and is issued after the organization adopts a later fiscal calendar.",
      "expected": "The issue keeps the pinned FY-2026-EU calendar identity, version, timezone and period convention; later calendar changes do not reinterpret its reporting period."
    },
    {
      "id": "policy-widening-new-issue",
      "input": "A later disclosure policy permits a slice that the issued report suppressed.",
      "expected": "The earlier issue remains unchanged; any wider disclosure is a new issue pinned to the later policy."
    },
    {
      "id": "missing-definition-invalid",
      "input": "A producer attempts to issue a statement without an immutable definition-version reference.",
      "expected": "Validation fails closed because an issued statement cannot exist without one pinned report definition."
    },
    {
      "id": "artifact-digest-custody-event",
      "input": "A record carrier is rewrapped and receives a new artifact digest while report meaning and evidence remain unchanged.",
      "expected": "The artifact system records a custody event; no restatement or replacement report issue is minted."
    },
    {
      "id": "dashboard-layout-not-identity",
      "input": "Widgets, colours and slicer positions change while a prior dashboard snapshot remains cited.",
      "expected": "The earlier issue identity and reconstruction tuple remain unchanged because layout is external configuration."
    }
  ]
}

## Local evidence

# EM-DAT-06 local synthesis

## Disposition

**COMPLETE RESERVED MODEL: WM-REC-002 Report / Statement.** The registry already reserves the correct identity and purpose. The missing specification must own the reusable report definition and the issued report statement while referencing execution, record, publication, edition and disclosure authorities.

## Identity boundaries

Owned by WM-REC-002:

- stable report-definition identity and immutable definition versions;
- parameter contract, asserted reporting grain and measure/query bindings;
- report-issue identity and lifecycle;
- reporting period, cutoff and as-of semantics asserted by the issue;
- pinned input snapshots and execution-evidence references;
- disclosure-policy provenance tuple and suppression manifest;
- correction/restatement lineage.

Referenced authorities:

- WM-ACT-053 owns processing-run execution and resolved inputs/outputs;
- WM-REC-001 owns record versions, artifacts, instantiations, fixity and retention;
- WM-ACT-044 owns publication operations, delivery and propagation of corrections;
- WM-XCT-003 owns permitted output shape and disclosure-policy semantics;
- WM-MED-003 owns bibliographic edition identity.

These identities are never interchangeable. Issuing a report is not executing it, rendering it, publishing it or assigning it an edition.

## Lifecycles

Definition version: `draft -> issued -> superseded -> withdrawn`.

Report issue: `planned -> computed -> issued -> superseded | withdrawn`.

An issued issue is immutable. Correction or changed inputs create a successor issue with an explicit restatement class and reason. The predecessor remains resolvable.

## Core invariants

1. An issue pins one report-definition version.
2. Bound parameters validate against that exact definition version.
3. Input dataset versions, partitions and digests are immutable issue evidence.
4. Reporting period, cutoff, as-of basis and issue time remain distinct.
5. Each execution reference covers the declared period or records a coverage exception.
6. Asserted grain may not exceed the applicable disclosure shape.
7. Every suppressed slice records its policy version and suppression reason without leaking withheld values.
8. A correction creates a successor; no published issue is overwritten.
9. Restatement lineage is acyclic and has one current head for a definition, parameter set and period.
10. Publication does not imply issue validity, and issue validity does not imply publication.
11. Report issue, processing run, record artifact, publication case and edition use disjoint identifiers.
12. Explanation references remain resolvable throughout the record retention period.

## Dashboard disposition

A dashboard definition is a profile of a report definition with external layout and refresh metadata. A live dashboard view is ephemeral and is not a report issue because it lacks a frozen cutoff and evidence tuple. A citable dashboard snapshot mints a report issue. WM-XCT-003 remains the authority for allowed output shape; it is not the dashboard definition itself.

## Acceptance result

Issue A pins definition v1.2, parameters, input snapshots, cutoff, as-of, run R1 and disclosure policy P7. A sensitive slice is recorded as suppressed. After an upstream correction, Issue B is created with new snapshots and run R2, explicitly superseding A. Both remain explainable; neither depends on the current dashboard configuration.

## Holds

All neighboring releases are reviewable drafts, several under single-provider waivers. Metric-definition authority is pending EM-DAT-05. Fiscal and civil periods now pin WM-XCT-009 calendar identity, version, timezone and convention. WM-XCT-003 multi-grain validation remains declarative. These holds permit a research candidate but block canonical publication.

## Initial Claude study

DECISION

**COMPLETE RESERVED MODEL.** Publish WM-REC-002 *Report / Statement* as a standalone aggregate owning two identities — the reusable **report-definition version** and the issued **report statement (issue)** — with every execution, artifact, publication, edition and disclosure-shape concern held as an external reference.

BOUNDARY PROOF

Tested candidate by candidate against dossier text, not intuition.

*Owned.* (1) **Reusable report-definition versions.** WM-ACT-053 excludes reusable definitions by name ("Pipeline, job and workflow definitions … remain external"), and its only candidate parent is WM-DAT-005 Data Pipeline, an execution graph, not an analytical specification. No dossier model owns a reusable report spec. (2) **Parameter and reporting-grain contract.** WM-ACT-053 owns *resolved* parameters of one execution; the declared contract that constrains all executions has no owner. Grain is two-layered: WM-XCT-003 owns the *permitted* grain (a ceiling on what may leave), WM-REC-002 owns the *asserted* grain (what the statement claims). (3) **Report issue identity.** Not a WM-REC-001 version — that model's out-of-scope excludes "subject-matter semantics of the record's content (… financial postings)", which is exactly what a statement asserts. Not a WM-MED-003 edition (bibliographic identity, no parameter contract). Not a WM-ACT-044 case (an operation, not a claim). (4) **Reporting period, cutoff, as-of.** WM-ACT-053 has "effective data interval" and watermark as execution scoping; the asserted period is a semantic commitment that survives re-execution. (5) **Correction/restatement lineage.** Four neighbouring lineages exist and none says *the number changed because an input fact changed*: ACT-053 rerun/backfill (execution), ACT-044 correction/takedown (delivery propagation), MED-003 erratum/corrigendum (bibliographic), REC-001 supersedes (record version). Restatement class and reason are owned here.

*External references, with owned pinning.* Source snapshots and runs → WM-ACT-053 (the issue owns the echoed identifier tuple, never the run lifecycle). Disclosure binding → WM-XCT-003, stored as the exact output of its `assemble-disclosure-provenance-tuple`. Artifacts → WM-REC-001 record/version/instantiation. Publication → WM-ACT-044 case; edition → WM-MED-003. Metric and query references → reference-first, but the dossier names no metric-definition owner, so an inline measure binding pinned to a WM-DAT-004 schema version is the interim (see H2).

*Rejected alternatives.* REUSE ONLY / composition-only leaves the pinned tuple homeless: nothing owns the join of definition version + parameters + snapshots + cutoff + policy version, so the negative case (arbitrary HR–finance join) has no object to refuse it. PROFILE of WM-REC-001 collapses statement identity into a document version and fails when an issue has zero artifacts or many. NEW MODEL is unwarranted: the reservation already carries the matching purpose, NAV.INF.REC.RPT, legacy alias N2 and `factor_overlap` 0.09. The flag "часто subtype N1" describes a frequent instantiation pattern, not identity; adopt REFERENCES, not subtype.

MINIMAL CONTRACT

**Identities (all disjoint):** `reportDefinitionVersionId` and `reportIssueId` (owned); `runId` (ACT-053), `recordId/versionId/instantiationId` (REC-001), `publicationCaseId` (ACT-044), `editionId` (MED-003), `policyVersionId + templateFingerprint` (XCT-003) — all foreign.

**Lifecycle.** Definition version: draft → issued → superseded → withdrawn. Issue: planned → computed → issued → superseded | withdrawn. No issue returns to computed.

**Core fields (18):** 1 reportDefinitionId · 2 reportDefinitionVersionId · 3 definitionVersionState · 4 parameterContract (name, type, domain, required, default) · 5 assertedGrain (kept dimensions + level) · 6 measureBinding (metric ref or expression + pinned schema version) · 7 reportIssueId · 8 issueState · 9 boundParameterValues · 10 reportingPeriod · 11 dataCutoff (RFC 3339) · 12 asOfBasis (instant + transaction/valid-time code) · 13 inputSnapshotPin (dataset version, partition, digest) 1..n · 14 executionEvidenceRef (runId) 1..n · 15 disclosureProvenanceTuple · 16 suppressionManifest (slice key, basis ref, withheld count — never withheld values) · 17 restatementLink (supersedes, class, reason) · 18 artifactRef / publicationCaseRef 0..n.

**Invariants.** I1 An issued issue is immutable; change requires a successor. I2 Issue cannot reach *issued* without fields 2, 9, 13, 11, 12, 14, 15. I3 Bound values validate against the parameter contract of that exact definition version. I4 Asserted grain is no wider than the meet of applicable shapes; subsumption is decided by WM-XCT-003, not re-implemented. I5 reportingPeriod.end ≤ dataCutoff ≤ asOf ≤ issuedAt. I6 Every referenced run's effective data interval covers the reporting period, or a coverage exception is declared. I7 Correction creates a successor; the predecessor is retained in issued/superseded state, never overwritten or deleted. I8 The restatement chain is acyclic with one head per (definitionVersion, parameters, period). I9 The five identity classes are disjoint; no field may carry one as another. I10 Any withheld slice appears in the suppression manifest with the withholding policy version; silent omission is prohibited. I11 Every source in a definition version resolves to a pinned schema/contract version and a binding reference; an unresolved path blocks issuance. I12 Publication is not issuance: an issue may exist unpublished, and a publication case without a valid issue reference may not claim report status. I13 The explanation tuple stays resolvable for the retention period assigned under WM-REC-001, including after template withdrawal (tombstone).

**Functions.** F1 *Version report definition* — fix an immutable definition version with its parameter contract, grain and measure bindings. F2 *Issue report statement* — bind parameters, pin snapshots, cutoff, as-of, run evidence and disclosure tuple; delegates execution, never performs it. F3 *Restate* — create a successor issue with class and reason, retaining the predecessor. F4 *Explain issue* — return the full reconstruction tuple including suppression manifest, artifacts and publications.

DASHBOARD DISPOSITION

A **dashboard definition is a profile of the report-definition version**: same parameter contract, asserted grain, measure bindings and disclosure binding, with added layout and refresh attributes that WM-REC-002 does not own. A **dashboard view is not a report issue** — it is an ephemeral evaluation with no pinned cutoff, and WM-REC-002 does not model it; a citable view must be converted by snapshot-on-cite, minting a real issue under F2. It is *not* a "governed projection": WM-XCT-003 projection is output-shape policy, not a definition. The negative case is blocked structurally by I11 plus I4 — a panel whose sources are not declared in a governed definition version cannot be evaluated, so arbitrary joins never reach disclosure evaluation to bypass it.

ACCEPTANCE WALKTHROUGH

Issue: F2 mints issue A pinning definition v1.2, parameters, three snapshot digests, cutoff, as-of, run R1 and policy tuple P7/fingerprint F9; a sensitive region slice is withheld and recorded in A's suppression manifest with P7 (I10). A is published via an ACT-044 case referencing A (I12). Correct: an input fact is restated upstream; a new snapshot digest appears. A is untouched (I1, I7). Successor: F3 mints issue B, same definition version and parameters, same period, `restatementClass = input-restatement`, supersedes A, new run R2. A remains issued-and-superseded, still explainable via F4 from its own pins (I13). Suppression: B re-evaluates under P7 as pinned, so the sensitive slice is suppressed under the *exact* version that governed A, even if a newer policy exists. Dashboard drift: changing a dashboard profile alters no issue, because A and B carry their own pins — explainability is independent of the live view.

HOLDS AND PUBLICATION RECOMMENDATION

H1 *Inherited-neighbour hold*: all five neighbours are reviewable-draft with `publishableCanonical: false`, and ACT-044, ACT-053 and MED-003 are single-provider waivers; WM-REC-002 cannot claim a stronger status than its weakest referenced authority. H2 *Metric ownership gap*: no dossier model owns metric definitions; field 6's inline fallback must be revisited when an owner exists. H3 *Time-model gap*: WM-REC-001 excludes calendar and period arithmetic, so fiscal-calendar semantics behind fields 10–12 are unowned. H4 *Subsumption is declarative*: WM-XCT-003 carries an open multi-grain validation hold, so I4 is a declared check, not a demonstrated one. H5 *Single-reviewer hold*: this adjudication is one independent reviewer; the definition/issue split needs adversarial second-provider review before canonical status. H6 *Alignment-only*: state alignment and mapping, with lossiness recorded; no conformance claims. H7 *Live-view deferral*: the runtime dashboard-view concern needs a registry placeholder decision.

Recommendation: publish WM-REC-002 at `0.1.0-research.1`, `entry_kind: aggregate`, `status: reviewable-draft`, `publishableCanonical: false`; add candidate REFERENCES rows to WM-ACT-053, WM-ACT-044, WM-REC-001, WM-XCT-003 and WM-MED-003 — no CONTAINS, and explicitly reject the N1 subtype reading.

## Grok study

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