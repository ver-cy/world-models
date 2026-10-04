You are the single frozen no-tools semantic auditor for EM-RSK-01. Use only the material below. Audit revision 2 for identity, lifecycle, mastership, risk/control/assessment/treatment boundaries, comparability, temporal and evidence semantics, stable rule IDs and bound fixtures. Confirm no identifier is allocated and no publication readiness is claimed. Return PASS or REVISE first, then one closed numbered defect checklist. Do not invent another root.


===== provider-comparison.md =====
# EM-RSK-01 provider comparison

Claude and Grok agree that WM-KNW-015 remains the Risk / Opportunity identity, WM-XCT-027 becomes a host-scoped assessment-context profile, and Control is an identifier-unassigned independent root. Both separate control definition, execution and time-bounded effectiveness and reject inference from control existence or policy status.

Grok corrects the initial local synthesis: EM-RSK-02 is Audit, Review and Finding, not Risk Treatment. Treatment execution therefore remains an unowned gap rather than being delegated there. Grok also blocks a WM-ACT-034 control-assessment profile until a written occupancy crosswalk resolves WM-ACT-033 and WM-XCT-027 collisions. The reconciled candidate therefore keeps WM-ACT-034 reference-only and conditional, allocates no identifier and claims no publication readiness.


===== claude-study.raw.md =====
# Verdict

**Reuse WM-KNW-015 as the risk entity.** Its declared root — a persistent item with identity separate from assessment revisions, gated lifecycle, single accountable owner, and survival through re-estimation, split, merge and closure — is exactly the risk entity EM-RSK-01 needs. No new identifier is justified.

**Profile WM-XCT-027, do not reuse as published.** Retain it as the host mixin for *assessment context* only (its bundles 1–3 and 7–9). Its control-authoring bundles (4–6) are excluded by its own `scope_statement`, `out_of_scope` list and boundary note 2, and its adjudication already records `status: split`. A profile that keeps binding/framing/estimation/residual/comparability/governance and reduces all control content to citation is the defensible EM-RSK-01 base.

**Identifier-unassigned candidates required for three planes** (independent identity, lifecycle and mastership in each case, none satisfiable by a host-scoped field group): control (design + implementation state), control assessment (test activity + effectiveness determination), and treatment (decision + action). Evidence, appetite/tolerance and acceptance-decision planes are already named as external in both specs; reference them, do not author them.

**Treatment ownership is a live boundary conflict:** EM-RSK-01 lists `RiskTreatment` among candidate types while EM-RSK-02 exists as a related contour. Settle which contour masters treatment before either claims it.

# Evidence

Both bases are `published` but `adjudicationStatus: reviewable-draft`, `publishableCanonical: false`, `providerMode: single-provider-waiver` with Grok waived (authorised 2026-08-29T09:06:27Z). Evidence depth on both registry candidates is `index-and-publication-metadata`; `mapping_status` is `conceptual-candidate`; `review_state` is `boundary-review-required` on both. Specs were pinned by digest (WM-KNW-015 `6725…3ccd`; WM-XCT-027 `4abb…5928`). The only ratified relation in the pack is WM-AI-008 → WM-KNW-015 `REFERENCE` (`candidate`). WM-ACT-017 parenthood is asserted in registry `parent_ids` and boundary notes but is explicitly held unratified. Both packs carry unretrieved primary-text holds (ISO 31000/31073/Guide 73, ISO/IEC 27001/27002, COSO, Basel OPE10) and unverified source pins. No semantic crosswalk is verified. Nothing below rests on sources beyond this dossier.

# Identity/mastership

| Plane | Master | Basis |
|---|---|---|
| Risk entity | WM-KNW-015 | identity persists across revisions, register membership, closure |
| Assessment context/result | WM-XCT-027 profile (host-scoped) | no identity independent of host; revision-pinned binding |
| Treatment decision/action | identifier-unassigned candidate (or EM-RSK-02) | own owner, schedule, milestones, closure; outlives the assessment |
| Control design | identifier-unassigned candidate | a control exists and is owned without any risk; catalogue/parameter lifecycle |
| Control implementation/execution | same control candidate for implementation state; **execution occurrences referenced** from operational masters (GRC/SIEM/service desk) | occurrence volume, retention and custody are not governable in a mixin |
| Control test/effectiveness determination | identifier-unassigned candidate | determinations are cited, expire, and are invalidated independently of any risk |
| Evidence | external evidence model (identifier-unassigned in both specs) | custody, digest, availability, lawful destruction |
| Appetite/tolerance | enterprise governance, referenced | authored and approved elsewhere; versioned |
| Residual-risk acceptance | decision/authority model, referenced | authorisation act, not an estimate |

**Resolving WM-XCT-027's ownership split.** Remain in the mixin: `rctl-risk-*` in full — risk reference, revision pin, statement digest, `binding-validity-state`, anchors, causal anchors, taxonomy pin, scope/horizon/as-of/recorded/validity times, criteria-method-expression pins, likelihood and consequence dimension declarations, inherent estimate with its exclusion statement, assumptions/basis/uncertainty, residual value, `relied-on-control-reference`, `cited-effectiveness-determination-reference`, `reliance-without-determination-flag`, `changed-dimension`, `residual-change-explanation`, appetite reference and `comparison-outcome`, comparability verdicts/caveats/scenario; plus `rctl-gov-*` stamps, provenance, sensitivity, evidence-integrity refs and retention refs **scoped to the binding only**.

Move to the external control/assessment masters: `rctl-control-catalogue-binding`, `-objective-classification`, `-applicability-scope`, `-accountability-references` (including `rctl-gov-de-control-owner-ref`), `-design-assertion`, `-implementation-assertion`, `-operating-cadence`, `-assessment-evidence-binding`, `-effectiveness-conclusion`, `-crosswalk-alignment`, and `-coverage-dependency` (cross-record state a host mixin cannot own — retain the traversal query, drop the authored matrix). `rctl-control-link-record` becomes a contained collection under the single host-scoped context root, not a second root. `rctl-control-residual-contribution` splits: the attribution *claim* is authored by the control assessment master; `attribution-status` (accepted/rejected/suspended) is the risk owner's, held with the risk entity.

# Assessment and comparability

Comparison is gated, never normalised. Every estimate carries criteria-set + version, method + version, expression mode, scale reference, scope, exclusions, horizon, as-of and recorded times. `rctl-risk-fn-check-comparability` returns `comparable` / `comparable-with-caveats` / `not-comparable` plus `mismatched-pin-list`; aggregation requires WM-KNW-015 `de-aggregation-eligibility` true **and** a comparability verdict, and caveats are non-strippable. Ordinal bands are stored as codes: no difference, product or mean is defined under qualitative, ordinal or scenario modes — the inherent→residual comparison records changed dimensions and direction, computing magnitude only where the pinned mode admits it. Cross-horizon comparison is refused unless horizons match or a declared conversion exists; `case-basis` (expected / most likely / worst credible) must match; records pinned to withdrawn criteria are handled by `superseded-criteria-handling`, not silently re-scored.

# Control design/execution/effectiveness

Four separate states, each with its own determining party and event time: design adequacy (would achieve objective if operated as prescribed); implementation (is in place, with deviations, exceptions, expiry, compensating controls); operation (operating / suspended / not operating, with expected vs observed occurrences by reference); effectiveness (a conclusion on a named vocabulary whose **only** permitted basis is assessment method + coverage + evidence bindings, carrying confidence, validity expiry and invalidation triggers). Design status never implies implementation; implementation never implies operation; none of the three implies effectiveness. An expired conclusion degrades to unknown, not to effective.

# Treatment/residual risk

Response option selection and rationale sit with the risk entity; plans, milestones and closure sit with the treatment master; residual estimate and appetite comparison sit in the assessment context; acceptance is a referenced decision with required authority level, threshold-table version and authorisation time. Residual must state grounds: relied-on controls, their cited determinations, changed dimensions and an explanation. Reliance on a control with no current determination sets `reliance-without-determination-flag` and bars any residual reduction attribution.

# Shared cause

Two risks share a cause when they cite the same `risk-source-reference` / threat-catalogue identifier, the same `predisposing-condition-statement`, the same held-fixed `context-condition-statement`, or the same relied-on control or control dependency. Shared cause is recorded as a declared correlation and a `aggregation-caveat`; it never licenses summation, and it never merges identities. Common dependence on one control is the strongest form: it makes simultaneous degradation plausible and must appear as a caveat on any roll-up.

# Invariants

1. Every estimate carries scale, expression mode, horizon, as-of time and criteria version; otherwise it is unusable, not merely unvalidated.
2. Control existence, documentation, mapping, policy status or incident absence never yield an effectiveness value.
3. A policy or requirement status never transitions a risk lifecycle state or closes a risk.
4. Residual risk without recorded grounds and a cited determination is invalid.
5. Acceptance requires a referenced decision and sufficient recorded authority.
6. Aggregation requires an explicit comparability verdict; caveats travel with the aggregate.
7. Item identity is independent of assessment revision and register membership.
8. Assessment context has no identity independent of its host and its pinned risk revision.
9. Event time, observation/as-of time and record time are distinct and never substituted.
10. Superseded upstream risk revision marks the binding stale; the mechanism must be named (currently a declared gap).

# Scenario

Control C is cited by contexts for R1, R2, R3. A failed execution of C is recorded in the executing system. Effect:

- **R1** — cites determination D over a period covering the failure; C's claimed mechanism is likelihood reduction on the same population; evidence reference resolves with a matching digest. The failure invalidates D via a fired reassessment trigger; currency becomes invalidated, `reliance-without-determination-flag` set, residual estimate reopened, `changed-dimension` recorded. Assessment changes.
- **R2** — relies on C for a consequence dimension and population outside the failed occurrence's covered scope. No causal link; reliance note recorded, currency unchanged. No assessment change.
- **R3** — links C by coverage/crosswalk with no cited determination. The flag was already true; the failure adds a coverage-gap finding. No assessment change, because there was no effectiveness claim to falsify.

Negative case: a green policy status on C closes none of R1–R3 and alters no estimate.

# Minimal profile/candidate shape

Reuse WM-KNW-015 unchanged. WM-XCT-027 profile: one host-scoped assessment-context root; retained field groups as listed; control content citation-only; contained risk↔control edge collection; comparability gate mandatory; coverage matrix and control-authoring artifacts removed. Three identifier-unassigned candidates: control (design + implementation), control assessment (test + effectiveness determination), treatment (decision + action) — each pending an identity, lifecycle and mastership justification of its own. Evidence, appetite, acceptance-decision, party, criteria/method registry and execution telemetry: reference only.

# Holds

Single-provider waiver on both bases; no independent second-provider corroboration. WM-XCT-027's split is unresolved upstream and this review's resolution is a recommendation, not a ratified boundary. Crosswalk, rights and source mastership unconfirmed; `published` does not mean independently reviewed. Unretrieved primary texts and unverified source/version pins on both packs. Composition-link counts in both packs are unsupported by delivered structure. Upstream-supersession detection is undefined. WM-ACT-017 parenthood unratified. Registry defects open: empty `namespace_uri`, vague `owner_or_maintainer`, adverse-only purpose line on WM-KNW-015. No claim of canonical completeness and no claim of installability is made here; immutable refs and fixture checks remain outstanding per the contour's blocking decisions.


===== grok-study.raw.md =====
# Grok independent study — EM-RSK-01

## Verdict
Conditional accept. Reuse WM-KNW-015 as the persistent Risk / Opportunity identity. Restrict WM-XCT-027 to a host-scoped Risk Assessment Context. Keep one identifier-unassigned Control candidate owning definition, implementation state and lifecycle. Reference evidence, appetite and acceptance. Control Assessment cannot safely profile WM-ACT-034 until a written crosswalk is closed. EM-RSK-02 is Audit, Review and Finding, not treatment; EM-RSK-01 may reference treatment and execution outcomes but must not absorb a treatment workflow. No identifier is allocated and no canonical completeness is claimed.

## Identity and mastership
WM-KNW-015 masters risk identity, articulation, valence, classification pin, owner and lifecycle. Assessment revisions and comparability pins live on the host embedding WM-XCT-027; any current estimates on WM-KNW-015 are a current-view projection. WM-XCT-027 binds one assessment context to a risk revision, cited controls and effectiveness determinations, and compares residual position with referenced appetite or tolerance. It does not own risk, control register, effectiveness evidence or treatment workflow. Control remains identifier-unassigned and independently owns definition, implementation state and lifecycle. Implementation state is not effectiveness.

## Assessment and comparability
An assessment is time-bounded and distinct from risk identity. It pins scope, exclusions, horizon, as-of time, recorded time, valid-until time, criteria version, method version, technique version, expression mode and scale. Contexts are comparable only when pins match or a declared conversion records trace and caveats. Missing scale, method, criteria, scope or horizon makes records incomparable. Inherent and residual are distinct findings. Residual cites controls, current effectiveness, changed dimension and explanation.

## Control design, execution and effectiveness
Four layers remain separate: Control master; Control Execution occurrence; time-bounded effectiveness determination; referenced policy or requirement. A failed execution does not rewrite the control definition. Effectiveness needs method, sample, evidence chain, confidence, validity window and invalidation triggers. Control existence, implementation or green policy status never proves effectiveness or closes risk. WM-XCT-027 may cite these facts but cannot author a shadow control register.

## Residual risk and treatment
Residual risk requires a pinned assessment context, cited controls, cited current effectiveness and appetite comparison. Appetite is referenced, not set. Acceptance is a referenced decision and is not a close-the-risk verb. EM-RSK-02 is an assurance contour and cannot be treated as the treatment master. WM-KNW-015 may carry a response option and treatment-plan reference, but treatment execution has no published master in this contour. Do not invent one.

## Shared cause
Shared cause is a referenced source or event, not a shared identity or assessment. One control linked to three risks is coverage topology. Common cause does not imply common residual, horizon or evidence chain.

## Invariants
1. An assessment contains scale and horizon; a score without both is not an assessment.
2. Control existence, implementation state or policy status never proves effectiveness or closes risk.
3. Design, implementation, operation and tested effectiveness are distinct assertions.
4. Residual risk without cited controls, cited effectiveness, changed dimension and comparison or acceptance reference is incomplete.
5. Estimates compare only with matching or explicitly convertible scale, method, criteria, scope and horizon.
6. One control to many risks is linkage, not shared identity or assessment.
7. Failed execution changes only assessments whose population, period, mechanism and evidence chain match.
8. Test completion is not residual-risk closure; conclusions expire and have invalidation triggers.
9. Evidence, appetite and acceptance are referenced, not owned.
10. Treatment execution is not owned here; EM-RSK-02 is not that workflow.

## Scenario
Control C is linked to R1, R2 and R3. C fails for population P, period T, mechanism M and evidence E. Only the assessment whose pins match P, T, M and E may change. Other assessments remain unchanged until their matching evidence chain is shown. Green policy status closes none. Shared cause does not rewrite the second risk if its assessment does not cite the failed mechanism and evidence.

## Blockers
- WM-KNW-015 overlaps Assessment Context and treatment-plan semantics; reuse requires an explicit mastership cut.
- Risk Treatment has no published treatment master and EM-RSK-02 is audit, not treatment.
- Control has no assigned identifier and remains unassigned.
- WM-ACT-034 is not an EM-RSK-01 target and WM-ACT-033 already includes control assessment as an engagement type.
- All relevant published models remain reviewable drafts with source, relation and composition holds.
- Candidate types still include Risk Treatment and Control Execution while the proposed boundary strips treatment and keeps execution separate.

## WM-ACT-034 challenge
Not yet safe. WM-ACT-034 is a generic Assessment / Evaluation aggregate with subject, criteria version, method, evidence, criterion outcomes, composite result, conclusion and validity window. That shape is necessary but not sufficient. Design versus operating effectiveness are not first-class, activity and judgment sit on one aggregate, parentage is unratified, and no completed relation contract exists. A completed assessment must not be read as residual-risk closure or implementation state. Gate profiling on a written occupancy crosswalk against WM-ACT-033 and WM-XCT-027; make population, period, mechanism and evidence chain mandatory and preserve the design-versus-operation split. If the generic aggregate cannot do so without overload, keep testing as an activity that emits a cited effectiveness conclusion. Do not invent a replacement identifier.


===== candidate\control.json =====
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-RSK-01",
  "proposedName": "Control",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NEW MODEL",
  "canonicalPublishable": false,
  "identityTest": {
    "stableIdentity": "A governed control definition remains identifiable across revisions, implementations, execution occurrences, linked risks and effectiveness assessments.",
    "versionIdentity": "Changes to objective, mechanism, applicability, owner, cadence or dependencies create immutable control revisions while preserving the control identity and prior reliance history.",
    "independentLifecycle": [
      "draft",
      "approved",
      "active",
      "suspended",
      "retired",
      "superseded"
    ],
    "mastership": "control owner or control-governance authority"
  },
  "boundary": {
    "owns": [
      "stable control identity and immutable definition revisions",
      "control objective, mechanism and applicability",
      "accountable owner and operating cadence",
      "implementation-state declarations and dependencies",
      "revision, supersession, suspension and retirement history"
    ],
    "references": [
      {
        "target": "WM-KNW-015",
        "purpose": "Risk or opportunity that cites or relies on the control"
      },
      {
        "target": "WM-XCT-027",
        "purpose": "Risk-assessment context and residual-risk reliance"
      },
      {
        "target": "WM-ACT-034",
        "purpose": "Scoped control assessment and effectiveness determination"
      },
      {
        "target": "WM-REC-001",
        "purpose": "Execution, test and documentary evidence records"
      }
    ],
    "excludes": [
      "risk identity or risk-assessment estimates",
      "control execution occurrence identity",
      "effectiveness assessment, conclusion or expiry",
      "treatment-plan and corrective-action lifecycle",
      "policy, evidence or decision mastership"
    ]
  },
  "objects": {
    "Control": {
      "identity": [
        "controlId"
      ],
      "required": [
        "ownerRef",
        "status",
        "currentRevisionRef"
      ],
      "optional": [
        "successorRef",
        "retiredAt"
      ],
      "lifecycle": [
        "draft",
        "approved",
        "active",
        "suspended",
        "retired",
        "superseded"
      ]
    },
    "ControlRevision": {
      "identity": [
        "controlId",
        "revision"
      ],
      "required": [
        "objective",
        "mechanism",
        "applicability",
        "ownerRef",
        "contentDigest",
        "effectiveFrom"
      ],
      "optional": [
        "effectiveTo",
        "cadence",
        "dependencyRefs",
        "implementationState",
        "supersedesRevision"
      ],
      "lifecycle": [
        "draft",
        "approved",
        "effective",
        "superseded",
        "withdrawn"
      ]
    }
  },
  "invariants": [
    "Control identity survives revision, reassignment, implementation change, execution occurrence and assessment turnover.",
    "Changing objective, mechanism, applicability, owner, cadence or dependency creates an immutable successor revision.",
    "Every effective control references exactly one immutable approved revision.",
    "Control existence, documentation, implementation or policy status never proves effectiveness or closes risk.",
    "Design adequacy, implementation state, operating cadence, execution occurrence and effectiveness conclusion remain distinct.",
    "Effectiveness requires external assessment pins for population, period, mechanism, method, evidence chain, confidence, conclusion time, validity and invalidation triggers.",
    "A risk may rely on a control only through an explicit risk-revision-pinned assessment-context citation.",
    "Residual reduction requires a current effectiveness determination covering the relied-on mechanism, scope and changed dimension.",
    "Missing, expired or invalidated effectiveness makes reliance unknown and bars residual reduction attribution.",
    "Execution occurrences and telemetry remain external evidence and never become control revisions.",
    "One control cited by many risks never merges risk identities or assessments.",
    "A failed execution changes only assessments whose population, period, mechanism and evidence chain match the failure.",
    "Superseding or retiring a control revision marks dependent assessment contexts stale without rewriting history.",
    "Control ownership, execution custody and assessment authority remain separately attributable.",
    "Shared cause or control dependence creates aggregation caveats and never arithmetic permission.",
    "Retired control identifiers remain resolvable and are never recycled."
  ],
  "holds": [
    "Registry namespace and identifier allocation are pending; no identifier is guessed.",
    "WM-KNW-015 and WM-XCT-027 are non-canonical single-provider reviewable drafts.",
    "WM-KNW-015 current-estimate overlap and WM-XCT-027 control-authoring overlap require an explicit mastership cut.",
    "WM-ACT-034 profiling is conditional on a written occupancy crosswalk against WM-ACT-033 and WM-XCT-027.",
    "Risk Treatment execution has no published master; EM-RSK-02 is not that workflow.",
    "Approved relations, primary-source pins, upstream staleness, rights, package conversion and live conformance remain pending.",
    "One frozen semantic audit is pending after provider reconciliation."
  ],
  "candidateRevision": 2,
  "invariantRules": [
    {
      "id": "EM-RSK-01.CTL-01",
      "text": "Control identity survives revision, reassignment, implementation change, execution occurrence and assessment turnover."
    },
    {
      "id": "EM-RSK-01.CTL-02",
      "text": "Changing objective, mechanism, applicability, owner, cadence or dependency creates an immutable successor revision."
    },
    {
      "id": "EM-RSK-01.CTL-03",
      "text": "Every effective control references exactly one immutable approved revision."
    },
    {
      "id": "EM-RSK-01.CTL-04",
      "text": "Control existence, documentation, implementation or policy status never proves effectiveness or closes risk."
    },
    {
      "id": "EM-RSK-01.CTL-05",
      "text": "Design adequacy, implementation state, operating cadence, execution occurrence and effectiveness conclusion remain distinct."
    },
    {
      "id": "EM-RSK-01.CTL-06",
      "text": "Effectiveness requires external assessment pins for population, period, mechanism, method, evidence chain, confidence, conclusion time, validity and invalidation triggers."
    },
    {
      "id": "EM-RSK-01.CTL-07",
      "text": "A risk may rely on a control only through an explicit risk-revision-pinned assessment-context citation."
    },
    {
      "id": "EM-RSK-01.CTL-08",
      "text": "Residual reduction requires a current effectiveness determination covering the relied-on mechanism, scope and changed dimension."
    },
    {
      "id": "EM-RSK-01.CTL-09",
      "text": "Missing, expired or invalidated effectiveness makes reliance unknown and bars residual reduction attribution."
    },
    {
      "id": "EM-RSK-01.CTL-10",
      "text": "Execution occurrences and telemetry remain external evidence and never become control revisions."
    },
    {
      "id": "EM-RSK-01.CTL-11",
      "text": "One control cited by many risks never merges risk identities or assessments."
    },
    {
      "id": "EM-RSK-01.CTL-12",
      "text": "A failed execution changes only assessments whose population, period, mechanism and evidence chain match the failure."
    },
    {
      "id": "EM-RSK-01.CTL-13",
      "text": "Superseding or retiring a control revision marks dependent assessment contexts stale without rewriting history."
    },
    {
      "id": "EM-RSK-01.CTL-14",
      "text": "Control ownership, execution custody and assessment authority remain separately attributable."
    },
    {
      "id": "EM-RSK-01.CTL-15",
      "text": "Shared cause or control dependence creates aggregation caveats and never arithmetic permission."
    },
    {
      "id": "EM-RSK-01.CTL-16",
      "text": "Retired control identifiers remain resolvable and are never recycled."
    }
  ]
}


===== candidate\enterprise-risk-control-profile.json =====
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-RSK-01",
  "name": "Enterprise Risk Assessment and Control Reliance",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "candidateRevision": 2,
  "bases": [
    "WM-KNW-015",
    "WM-XCT-027"
  ],
  "conditionalReferences": [
    {
      "id": "WM-ACT-034",
      "condition": "written occupancy crosswalk against WM-ACT-033 and WM-XCT-027"
    }
  ],
  "constraintRules": [
    {
      "id": "EM-RSK-01.EP-01",
      "text": "WM-KNW-015 remains the Risk / Opportunity identity and lifecycle master; assessment revisions are not risk identities."
    },
    {
      "id": "EM-RSK-01.EP-02",
      "text": "WM-XCT-027 is host-scoped and pins risk revision, scope, exclusions, scale, criteria, method, horizon, as-of, recorded and validity times."
    },
    {
      "id": "EM-RSK-01.EP-03",
      "text": "Comparability requires matching or explicitly converted scale, expression mode, criteria, method, scope and horizon with non-strippable caveats."
    },
    {
      "id": "EM-RSK-01.EP-04",
      "text": "Inherent and residual are distinct; residual cites controls, current effectiveness, changed dimension and causal explanation."
    },
    {
      "id": "EM-RSK-01.EP-05",
      "text": "WM-XCT-027 cites control and effectiveness facts and never authors a control register, execution occurrence or evidence payload."
    },
    {
      "id": "EM-RSK-01.EP-06",
      "text": "Appetite, tolerance, evidence and residual acceptance are external referenced authorities."
    },
    {
      "id": "EM-RSK-01.EP-07",
      "text": "Treatment execution remains unowned in this contour; EM-RSK-02 is assurance and must not be relabeled as treatment."
    },
    {
      "id": "EM-RSK-01.EP-08",
      "text": "WM-ACT-034 is reference-only until a written crosswalk makes population, period, mechanism, evidence chain and design-versus-operation explicit."
    },
    {
      "id": "EM-RSK-01.EP-09",
      "text": "A completed test or assessment never implies implementation, residual-risk closure or acceptance."
    }
  ],
  "unownedScopeRegister": [
    "risk treatment execution master",
    "control execution occurrence master",
    "evidence custody master",
    "appetite and tolerance master",
    "residual acceptance decision master"
  ],
  "holds": [
    "Registry namespace and identifier allocation are pending; no identifier is guessed.",
    "WM-KNW-015 and WM-XCT-027 are non-canonical single-provider reviewable drafts.",
    "WM-KNW-015 current-estimate overlap and WM-XCT-027 control-authoring overlap require an explicit mastership cut.",
    "WM-ACT-034 profiling is conditional on a written occupancy crosswalk against WM-ACT-033 and WM-XCT-027.",
    "Risk Treatment execution has no published master; EM-RSK-02 is not that workflow.",
    "Approved relations, primary-source pins, upstream staleness, rights, package conversion and live conformance remain pending.",
    "One frozen semantic audit is pending after provider reconciliation."
  ],
  "canonicalPublishable": false,
  "publicationStatement": "Research candidate only; not canonically publishable, installable or verified."
}


===== candidate\fixtures.json =====
{
  "format": "vercy-enterprise-combined-fixtures/v1",
  "contourId": "EM-RSK-01",
  "candidateRevision": 2,
  "canonicalPublishable": false,
  "executable": false,
  "cases": [
    {
      "id": "EM-RSK-01.FX-001",
      "kind": "negative",
      "input": "An implementation contradicts: Control identity survives revision, reassignment, implementation change, execution occurrence and assessment turnover.",
      "expect": "The contradiction is rejected under EM-RSK-01.CTL-01.",
      "rules": [
        "EM-RSK-01.CTL-01"
      ]
    },
    {
      "id": "EM-RSK-01.FX-002",
      "kind": "negative",
      "input": "An implementation contradicts: Changing objective, mechanism, applicability, owner, cadence or dependency creates an immutable successor revision.",
      "expect": "The contradiction is rejected under EM-RSK-01.CTL-02.",
      "rules": [
        "EM-RSK-01.CTL-02"
      ]
    },
    {
      "id": "EM-RSK-01.FX-003",
      "kind": "negative",
      "input": "An implementation contradicts: Every effective control references exactly one immutable approved revision.",
      "expect": "The contradiction is rejected under EM-RSK-01.CTL-03.",
      "rules": [
        "EM-RSK-01.CTL-03"
      ]
    },
    {
      "id": "EM-RSK-01.FX-004",
      "kind": "negative",
      "input": "An implementation contradicts: Control existence, documentation, implementation or policy status never proves effectiveness or closes risk.",
      "expect": "The contradiction is rejected under EM-RSK-01.CTL-04.",
      "rules": [
        "EM-RSK-01.CTL-04"
      ]
    },
    {
      "id": "EM-RSK-01.FX-005",
      "kind": "negative",
      "input": "An implementation contradicts: Design adequacy, implementation state, operating cadence, execution occurrence and effectiveness conclusion remain distinct.",
      "expect": "The contradiction is rejected under EM-RSK-01.CTL-05.",
      "rules": [
        "EM-RSK-01.CTL-05"
      ]
    },
    {
      "id": "EM-RSK-01.FX-006",
      "kind": "negative",
      "input": "An implementation contradicts: Effectiveness requires external assessment pins for population, period, mechanism, method, evidence chain, confidence, conclusion time, validity and invalidation triggers.",
      "expect": "The contradiction is rejected under EM-RSK-01.CTL-06.",
      "rules": [
        "EM-RSK-01.CTL-06"
      ]
    },
    {
      "id": "EM-RSK-01.FX-007",
      "kind": "negative",
      "input": "An implementation contradicts: A risk may rely on a control only through an explicit risk-revision-pinned assessment-context citation.",
      "expect": "The contradiction is rejected under EM-RSK-01.CTL-07.",
      "rules": [
        "EM-RSK-01.CTL-07"
      ]
    },
    {
      "id": "EM-RSK-01.FX-008",
      "kind": "negative",
      "input": "An implementation contradicts: Residual reduction requires a current effectiveness determination covering the relied-on mechanism, scope and changed dimension.",
      "expect": "The contradiction is rejected under EM-RSK-01.CTL-08.",
      "rules": [
        "EM-RSK-01.CTL-08"
      ]
    },
    {
      "id": "EM-RSK-01.FX-009",
      "kind": "negative",
      "input": "An implementation contradicts: Missing, expired or invalidated effectiveness makes reliance unknown and bars residual reduction attribution.",
      "expect": "The contradiction is rejected under EM-RSK-01.CTL-09.",
      "rules": [
        "EM-RSK-01.CTL-09"
      ]
    },
    {
      "id": "EM-RSK-01.FX-010",
      "kind": "negative",
      "input": "An implementation contradicts: Execution occurrences and telemetry remain external evidence and never become control revisions.",
      "expect": "The contradiction is rejected under EM-RSK-01.CTL-10.",
      "rules": [
        "EM-RSK-01.CTL-10"
      ]
    },
    {
      "id": "EM-RSK-01.FX-011",
      "kind": "negative",
      "input": "An implementation contradicts: One control cited by many risks never merges risk identities or assessments.",
      "expect": "The contradiction is rejected under EM-RSK-01.CTL-11.",
      "rules": [
        "EM-RSK-01.CTL-11"
      ]
    },
    {
      "id": "EM-RSK-01.FX-012",
      "kind": "negative",
      "input": "An implementation contradicts: A failed execution changes only assessments whose population, period, mechanism and evidence chain match the failure.",
      "expect": "The contradiction is rejected under EM-RSK-01.CTL-12.",
      "rules": [
        "EM-RSK-01.CTL-12"
      ]
    },
    {
      "id": "EM-RSK-01.FX-013",
      "kind": "negative",
      "input": "An implementation contradicts: Superseding or retiring a control revision marks dependent assessment contexts stale without rewriting history.",
      "expect": "The contradiction is rejected under EM-RSK-01.CTL-13.",
      "rules": [
        "EM-RSK-01.CTL-13"
      ]
    },
    {
      "id": "EM-RSK-01.FX-014",
      "kind": "negative",
      "input": "An implementation contradicts: Control ownership, execution custody and assessment authority remain separately attributable.",
      "expect": "The contradiction is rejected under EM-RSK-01.CTL-14.",
      "rules": [
        "EM-RSK-01.CTL-14"
      ]
    },
    {
      "id": "EM-RSK-01.FX-015",
      "kind": "negative",
      "input": "An implementation contradicts: Shared cause or control dependence creates aggregation caveats and never arithmetic permission.",
      "expect": "The contradiction is rejected under EM-RSK-01.CTL-15.",
      "rules": [
        "EM-RSK-01.CTL-15"
      ]
    },
    {
      "id": "EM-RSK-01.FX-016",
      "kind": "negative",
      "input": "An implementation contradicts: Retired control identifiers remain resolvable and are never recycled.",
      "expect": "The contradiction is rejected under EM-RSK-01.CTL-16.",
      "rules": [
        "EM-RSK-01.CTL-16"
      ]
    },
    {
      "id": "EM-RSK-01.FX-017",
      "kind": "negative",
      "input": "An implementation contradicts: WM-KNW-015 remains the Risk / Opportunity identity and lifecycle master; assessment revisions are not risk identities.",
      "expect": "The contradiction is rejected under EM-RSK-01.EP-01.",
      "rules": [
        "EM-RSK-01.EP-01"
      ]
    },
    {
      "id": "EM-RSK-01.FX-018",
      "kind": "negative",
      "input": "An implementation contradicts: WM-XCT-027 is host-scoped and pins risk revision, scope, exclusions, scale, criteria, method, horizon, as-of, recorded and validity times.",
      "expect": "The contradiction is rejected under EM-RSK-01.EP-02.",
      "rules": [
        "EM-RSK-01.EP-02"
      ]
    },
    {
      "id": "EM-RSK-01.FX-019",
      "kind": "negative",
      "input": "An implementation contradicts: Comparability requires matching or explicitly converted scale, expression mode, criteria, method, scope and horizon with non-strippable caveats.",
      "expect": "The contradiction is rejected under EM-RSK-01.EP-03.",
      "rules": [
        "EM-RSK-01.EP-03"
      ]
    },
    {
      "id": "EM-RSK-01.FX-020",
      "kind": "negative",
      "input": "An implementation contradicts: Inherent and residual are distinct; residual cites controls, current effectiveness, changed dimension and causal explanation.",
      "expect": "The contradiction is rejected under EM-RSK-01.EP-04.",
      "rules": [
        "EM-RSK-01.EP-04"
      ]
    },
    {
      "id": "EM-RSK-01.FX-021",
      "kind": "negative",
      "input": "An implementation contradicts: WM-XCT-027 cites control and effectiveness facts and never authors a control register, execution occurrence or evidence payload.",
      "expect": "The contradiction is rejected under EM-RSK-01.EP-05.",
      "rules": [
        "EM-RSK-01.EP-05"
      ]
    },
    {
      "id": "EM-RSK-01.FX-022",
      "kind": "negative",
      "input": "An implementation contradicts: Appetite, tolerance, evidence and residual acceptance are external referenced authorities.",
      "expect": "The contradiction is rejected under EM-RSK-01.EP-06.",
      "rules": [
        "EM-RSK-01.EP-06"
      ]
    },
    {
      "id": "EM-RSK-01.FX-023",
      "kind": "negative",
      "input": "An implementation contradicts: Treatment execution remains unowned in this contour; EM-RSK-02 is assurance and must not be relabeled as treatment.",
      "expect": "The contradiction is rejected under EM-RSK-01.EP-07.",
      "rules": [
        "EM-RSK-01.EP-07"
      ]
    },
    {
      "id": "EM-RSK-01.FX-024",
      "kind": "negative",
      "input": "An implementation contradicts: WM-ACT-034 is reference-only until a written crosswalk makes population, period, mechanism, evidence chain and design-versus-operation explicit.",
      "expect": "The contradiction is rejected under EM-RSK-01.EP-08.",
      "rules": [
        "EM-RSK-01.EP-08"
      ]
    },
    {
      "id": "EM-RSK-01.FX-025",
      "kind": "negative",
      "input": "An implementation contradicts: A completed test or assessment never implies implementation, residual-risk closure or acceptance.",
      "expect": "The contradiction is rejected under EM-RSK-01.EP-09.",
      "rules": [
        "EM-RSK-01.EP-09"
      ]
    },
    {
      "id": "EM-RSK-01.FX-026",
      "kind": "positive",
      "input": "One control revision is cited by three independent risk assessments.",
      "expect": "One control identity and three independent risk contexts remain.",
      "rules": [
        "EM-RSK-01.CTL-11"
      ]
    },
    {
      "id": "EM-RSK-01.FX-027",
      "kind": "positive",
      "input": "A failure covers only R1 population, period, mechanism and evidence chain.",
      "expect": "Only R1 determination is invalidated; R2 and R3 remain unchanged.",
      "rules": [
        "EM-RSK-01.CTL-12"
      ]
    },
    {
      "id": "EM-RSK-01.FX-028",
      "kind": "negative",
      "input": "Green policy status closes all linked risks.",
      "expect": "Closure is rejected.",
      "rules": [
        "EM-RSK-01.CTL-04",
        "EM-RSK-01.EP-09"
      ]
    },
    {
      "id": "EM-RSK-01.FX-029",
      "kind": "negative",
      "input": "Residual likelihood is lowered without current effectiveness evidence.",
      "expect": "Attribution is rejected and reliance is unknown.",
      "rules": [
        "EM-RSK-01.CTL-08",
        "EM-RSK-01.CTL-09"
      ]
    },
    {
      "id": "EM-RSK-01.FX-030",
      "kind": "negative",
      "input": "EM-RSK-02 is treated as the risk-treatment master.",
      "expect": "Boundary is rejected.",
      "rules": [
        "EM-RSK-01.EP-07"
      ]
    },
    {
      "id": "EM-RSK-01.FX-031",
      "kind": "negative",
      "input": "Generic WM-ACT-034 completion closes residual risk before crosswalk.",
      "expect": "Inference is rejected.",
      "rules": [
        "EM-RSK-01.EP-08",
        "EM-RSK-01.EP-09"
      ]
    }
  ]
}
