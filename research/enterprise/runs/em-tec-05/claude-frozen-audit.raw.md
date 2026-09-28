# Frozen semantic audit — EM-TEC-05 / WM-ACT-019 `0.1.0-candidate.2`

## Verdict

**REVISE.**

The boundary adjudication is sound and converges with both studies: one declaration identity per determined occurrence, cyber as qualification rather than peer master, Problem/Defect/Task externally mastered, ImpactAssessment as incident child, RootCauseClaim as namespaced Problem child, no new model identifier. That part I would accept.

The artifact is not acceptable as written because it contains internal contradictions that make four of its own invariants unenforceable, one fixture unsatisfiable, and one version-ordering defect against the model it replaces. These are repairable with field-level edits; none require reopening a boundary decision.

## Blocking findings

**B1 — INV-002 has no carrier. The occurrence key does not exist.**
`Incident.identity` is `incidentId`; nothing on `Incident` or `DeclarationDecision` names the *determined occurrence*. `candidateEventRefs` is a set of candidate inputs, not a determined-occurrence identity. "At most one declaration identity per determined occurrence" is therefore not checkable, and fixture `dual-master-cyber` has nothing to key the duplicate detection on.

**B2 — `reported` in `Incident.lifecycle` contradicts `Incident.required` and INV-001.**
`definitionRevisionRef`, `declaredAt`, `declarationDecisionRef` and `authorityRef` are unconditionally required, yet the lifecycle admits a pre-declaration `reported` state. Either an Incident record can exist before declaration (INV-001 and fixture `alarm-not-incident` breached) or `reported` is unreachable. Pick one.

**B3 — No transition legality table; `reopened` is an event modelled as a state.**
`IncidentStateTransition` accepts any `fromStatus`→`toStatus`, so `declared`→`closed`, `restored`→`reported` and `closed`→`declared` without reopen are all admissible. `reopened` has no defined exit edges, so the resting status after reopen is undefined — INV-021's preservation guarantee is stated over an undefined graph.

**B4 — `definitionRevisionRef` is required but the definition neighbor is unpinned.**
The entire INV-001 gate rests on a pinned definition revision, and `relations` names no definition/policy-catalogue boundary. `residualRiskRef` (required on `ResolutionRecord`), `scaleRef`, `unitRef`, `authorityRef`/`ownerRef`/`assessorRef`/`reviewerRefs`, `affectedSubjectRefs` and `publicationRef` are likewise required-or-used with no declared target boundary in `relations`. Required references to unnamed externals.

**B5 — No reference value type; version pinning has no mechanism.**
Every `*Ref`/`*Refs` is untyped. INV-013 demands version-pinned defect references and INV-004 demands a representation role, but no ref structure carries target model, target id, revision pin, or role. `representationRole` has no enumeration at all, so INV-004 is unenforceable as stated.

**B6 — Origination direction for cyber is undefined, which re-admits dual mastership.**
`cyberQualification.identityRule` covers only the ops-first path ("specializes or qualifies the same incident declaration identity"). Cyber-first (SOC detection first) is not addressed, so both WM-ACT-019 and WM-ACT-020 can each believe they mint the sole declaration identity. Related: nothing forbids a retained separate cyber record from holding its *own* `DeclarationDecision`, which would put two declarations on one occurrence while formally satisfying INV-002's wording.

**B7 — Merge is invariant-referenced but not modelled.**
INV-016 and INV-021 both govern merge; there is no merge object, no survivor rule, and no rule converting the absorbed record into a correspondence with a role. Fixture `dual-master-cyber` resolves to "a cyber qualification **or** correspondence record" — the disjunction leaves the de-duplication procedure open.

**B8 — RootCauseClaim containment leaks through `IncidentReview.findings`.**
`findings` and `recommendations` are unstructured and live inside the incident aggregate. Causal assertions will land there in prose, bypassing the evidence/confidence/status discipline of INV-010/011. The candidate also drops the incident-local cause-hypothesis overlap that WM-ACT-020 already owns, and records no promotion rule for when a Problem is opened.

**B9 — Claim status has no `superseded` value and no status history.**
`supersedesClaimId` exists but `statuses` omits `superseded` (and any rejection outcome), so a superseded claim remains `supported` and a chain is indistinguishable from two live supported claims — directly undercutting fixture `claim-overwrite`, whose expected "status transition" has no object to live in. Status changes carry no time, author, or evidence.

**B10 — Clock set is inconsistent with the objects and with INV-020.**
`clockSemantics` declares `occurrenceAt`, which appears on no object. INV-020 requires an ingestion clock distinct from recording; neither `ingestedAt` nor an incident-level `recordedAt` exists. `SeverityAssessment` has only `assessedAt` where its sibling `ImpactAssessment` splits `effectiveAt`/`recordedAt`; `ResolutionRecord` has `resolvedAt` with no `recordedAt`. No ordering constraints are stated, so `declaredAt` < `detectedAt` and `closedAt` < `restoredAt` are admissible.

**B11 — Fixture `missing-observation-source` is unsatisfiable.**
It expects "unknown or incomplete coverage" for a stale absent source. The model has no source, coverage-window, staleness, or unknown-marker construct anywhere, so INV-023 has no carrier and this case cannot pass or fail meaningfully.

**B12 — Version regression on a retained model identifier.**
`disposition.newModelId: false` with `version: 0.1.0-candidate.2`, against a legacy WM-ACT-019 at `0.2.0`. Same id, lower version. Also, `disposition.kind: complete-reserved-model-by-rewrite` and the phrase "reserved legacy" mislabel the case — WM-ACT-019 has a legacy specification; *reserved* describes WM-KNW-014 and WM-SFT-014.

**B13 — No migration statement.**
Nothing records which legacy constructs (physical-emergency/CAP alerting semantics, the occurrence extension, the legacy impact record) are dropped, retained, or re-expressed, and nothing addresses the inbound reference from WM-AI-010 that treats WM-ACT-019 as general incident context. `boundary.excludes` does not exclude physical-emergency semantics.

**B14 — INV-002/003 assert scope over AI qualification with no AI neighbor.**
Both invariants range over "operational cyber and AI qualifications"; `relations` names no AI incident boundary and `cyberQualificationRef` is singular, so a dual ops+cyber+AI occurrence cannot even be expressed.

**B15 — The candidate legislates foreign aggregate internals.**
`problemProfile` fixes identity, required fields, statuses and a closure rule for a WM-KNW-014 child; `cyberQualification.owns` enumerates WM-ACT-020 contents. This contradicts `boundary.delegates`. The existing registry-approval hold acknowledges the dependency but not the authority inversion.

**B16 — Missing holds.** The following are absent and cannot be resolved in this artifact: the WM-ACT-020 `COMPOSE` ledger edge that contradicts the REFERENCE separation; the unpinned parent shared by WM-KNW-014 and WM-SFT-014; the single-provider/waived-independent-review status of WM-ACT-020; unnamed incident and problem master systems; absent field-level crosswalk; the WM-AI-010 migration obligation.

## Non-blocking findings

1. `boundary.owns` "containment restoration resolution closure" vs `delegates` "containment restoration and remediation work" — collides on wording; owns should read *state and history assertions*, delegates *work execution*.
2. `Incident` carries no affected-service/scope field; affected subjects appear only as optional on `ImpactAssessment`. Weak for a service-incident model.
3. Incident↔Problem linkage is stored in three places (`Incident.problemRefs`, `ResolutionRecord.problemRefs`, `RootCauseClaim.incidentRefs`) with no authoritative side and no reconciliation rule.
4. `DeclarationDecision.decision` is unenumerated; a decision *not* to declare has no recorded outcome vocabulary, and near-miss/false-positive have no home as qualification outcomes.
5. No binding between `Incident.status: resolved` / `resolvedAt` and an `effective` `ResolutionRecord`.
6. `IncidentCorrespondence` has no lifecycle — a mistaken correspondence can only be deleted, against the non-erasure posture of INV-021/025. It has `validTo` without `validFrom`.
7. `problemProfile.closureRule` requires only "own disposition authority" and drops the evidentiary precondition both studies state (a supported claim plus terminal remediation). Defensible as deference, but it should be explicit.
8. `statuses` contains both `supported` and `endorsed` with no stated difference and no cardinality rule.
9. `entryKind: incident-aggregate` — registry-enum conformance not verifiable from frozen material; flag for check, not a finding.

## Invariant and fixture gaps

**Invariants with no carrier field:** INV-002 (B1), INV-004 role enum (B5), INV-013 version pin (B5), INV-020 occurrence/ingestion clocks (B10), INV-023 unknown/stale marker (B11), INV-024 — no classification or disclosure-marking field exists on any WM-ACT-019 object, while `affectedSubjectRefs` and review evidence can carry personal data outside the cyber path.

**Invariants with no fixture (8 of 25):** INV-003, INV-013, INV-014, INV-015, INV-019, INV-022, INV-024, INV-025.

**Missing fixture classes:**
- No positive acceptance case for a well-formed declaration — the model's core act is never exercised positively.
- No positive case for a retained cyber record *with* valid correspondence (only the negative), and none for cyber-first origination.
- No case for withdrawal (incident or declaration decision), for merge, for clock inversion (only collapse), or for cascade *delete* (only closure).
- No case exercising `residualRiskRef`, `IncidentReview`, `supersedesDecisionId`, `ImpactAssessment.method`, or a named `scaleRef`.

**Fixture form:** all cases are prose input/expect pairs with no record fields, and each carries a single `expectRule` even where several invariants are in play (`temporary-restoration` exercises INV-015/016/017/019).

## Exact minimal remediations

1. **B1** — add required `occurrenceRef` to `Incident` and `DeclarationDecision`; restate INV-002 as uniqueness on `occurrenceRef` among non-withdrawn declarations.
2. **B2** — remove `reported` from `Incident.lifecycle` (keep `reportedAt` as an inherited clock), or move `definitionRevisionRef`/`declaredAt`/`declarationDecisionRef` to fields required *at and after* `declared`.
3. **B3** — add an explicit `allowedTransitions` edge list; model reopen as a transition whose `toStatus` is a defined resting state with defined exits.
4. **B4** — add `relations` entries, target ids to be assigned by the registry, for: definition/policy catalogue (required), party/authority, severity scale, unit, residual risk, affected service/configuration subject. Until assigned, mark each as a named hold rather than a bare required ref.
5. **B5** — define one `Reference` value type `{targetModel, targetId, targetRevision?, role?}`; require `targetRevision` on defect references; enumerate `representationRole` as `originating | master | mirror`.
6. **B6** — state both origination directions and add: a qualified or mirrored peer record must reference the governing `declarationDecisionId` and must not hold an independent declaration decision.
7. **B7** — add an `IncidentMerge` object (`survivingIncidentRef`, `absorbedIncidentRef`, authority, evidence, effectiveAt, recordedAt) with the rule that the absorbed identity is retained as correspondence with role `mirror`; replace the `or` in `dual-master-cyber` with the resulting single expected shape.
8. **B8** — forbid causal assertions in `IncidentReview.findings`; add optional typed `causeHypothesisRefs`/`rootCauseClaimRefs`, plus the promotion rule: incident-local hypotheses are permitted only while no Problem exists; once opened, the claim is mastered by the Problem and the incident retains a reference. Record the WM-ACT-020 hypothesis overlap as a hold.
9. **B9** — add `superseded` (and an explicit rejection value) to `statuses`; require `status: superseded` whenever `supersedesClaimId` is set; add append-only claim status assertions carrying `assertedBy`, `assertedAt`, `evidenceRefs`.
10. **B10** — add `occurrenceAt` and `ingestedAt` where declared; add `recordedAt` to `Incident`, `SeverityAssessment` (as `effectiveAt`/`recordedAt` split), and `ResolutionRecord`; add stated ordering constraints among occurrence ≤ detection/observation ≤ declaration and restoration ≤ resolution ≤ closure, with explicit unknown handling.
11. **B11** — either add `observationSourceRefs` with coverage window and staleness marker plus an explicit `unknown` value distinct from absent, or withdraw fixture `missing-observation-source` and record INV-023's carrier as a hold.
12. **B12** — version the rewrite above the legacy `0.2.0` on the retained identifier, or record an explicit hold that a candidate track below the legacy version is registry-permitted; change `disposition.kind` and `purpose` to name a legacy replacement, not a reserved completion.
13. **B13** — add a migration section listing legacy constructs dropped/retained/re-expressed and the inbound WM-AI-010 impact; add "physical-emergency and public-alerting semantics" to `boundary.excludes`.
14. **B14** — make `cyberQualificationRef` a set of `qualificationRefs` with a `qualificationKind`; add an AI-incident neighbor relation or narrow INV-002/003 to the qualifications actually referenced.
15. **B15** — relabel `problemProfile` and `cyberQualification` as neighbor *expectations*, explicitly non-normative for WM-KNW-014 and WM-ACT-020, retaining the approval hold.
16. **B16** — add the six missing holds verbatim as listed.
17. **Gaps** — add fixtures for INV-003, 013, 014, 015, 019, 022, 024, 025; add positive cases for valid declaration, valid cyber correspondence, cyber-first origination, withdrawal, and merge; add negatives for clock inversion and cross-aggregate delete; allow `expectRule` to be a list; give each case record-level input fields.
18. **Non-blocking** — apply items 1–8 of that section as worded.

No publication readiness is claimed or implied by this audit, and no identifier is proposed. On re-submission the items above are checkable mechanically; the boundary decisions themselves need no further semantic adjudication from my side.
