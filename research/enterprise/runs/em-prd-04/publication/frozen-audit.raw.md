# Frozen semantic audit — EM-PRD-04

## 1. Verdict

**REVISE.**

The identity adjudication is sound and I do not disturb it. The artifacts that are supposed to carry it do not. Twenty-one material defects below are internal to the supplied artifacts — contradictions between a declared invariant and the object schema that must enforce it, fields named by invariants that exist nowhere, lifecycle states that mutate records the same file calls immutable, and two fixtures whose expectations the boundary forbids the model from meeting. None of these is the known registry/base publication gap, which I treat as a hold throughout.

---

## 2. Material defects

### D1 — Research Finding: instance identity asserted away

`profile-candidate.json`: `"Research Finding profiles study findings with WM-KNW-007 claims and WM-KNW-008 evidence bindings without new identity."` `local-evidence.md`: *"No new finding identity is needed."* The fixed decision says Finding has **instance** identity supplied by the composed bases and mints no new **model** identity. The artifacts drop the qualifier and deny identity outright. Grok names exactly this: *"A finding profile of WM-ACT-036 plus WM-KNW-007/008 is a composition rule, not a substitute for instance identity"*, blocker: *"Give Finding instance identity so a profile cannot overwrite study or hypothesis."*

Compounding: **no Finding object is specified anywhere in the supplied artifacts** — no identity key, no required `uncertainty` / `applicability` / `limitations`, no supersession rule, no fixtures. `local-evidence.md` invariant 7 ("Findings state uncertainty, applicability and limitations") is therefore unenforceable, and the acceptance scenario's "one supports and one challenges" assessment has no structure to live in.

### D2 — The design pin has no resolvable referent

`candidate.json` → `ExperimentRun.required: ["studyRef", "designVersionRef", …]`, invariant *"Every run pins exactly one immutable released design version."* But `relations` lists only `WM-ACT-036` ("Resolve the owning study and immutable study-scoped design release"). The cross-study Reusable Experiment Design is registry-unassigned, so a run pinned to it has **no declared relation contract and no namespace**. `designVersionRef` is a single untyped field with no master discriminator, so a reader cannot tell whether a given pin resolves into a WM-ACT-036 release or an unassigned design. "Exactly one" is uncheckable when the referent space is undefined.

Further, Grok invariant 12 — *"Promotion of a study release to a cross-study design creates a new identity with a derivation link, not a silent rewrite"* — is unimplemented. `allocation-candidate.json` references `WM-ACT-036` only as `"Research Study aggregate"`, **excludes** `"study-scoped one-off protocol component"`, and `DesignVersion` offers only `supersedesVersion` (intra-design). There is no `derivedFromStudyReleaseRef`. On promotion, runs pinned to the study-scoped release become unreachable from the promoted design: a provenance break.

### D3 — Content-addressed identity on a mutable draft

`RunManifest.identity: ["manifestDigest"]`, and `operations.plan-run` = *"Create a run pinned to one released design version and **draft** manifest"*, `start-attempt` = *"**Freeze** the manifest…"*. A digest is the identity of content; while the manifest is a draft, every edit silently reassigns its identity, so nothing can reference it and the `planned` run state holds an object whose key churns. There is no `manifestState`, no `frozenAt`, and no invariant forbidding reference to an unfrozen manifest.

Reference style is also inconsistent: `ExperimentRun.required` carries an embedded `runManifest`, while `ExperimentAttempt.required` carries a `manifestDigest`. Embedding versus pinning are different immutability regimes and the file uses both for the same object.

### D4 — Run-level manifest versus attempt-level manifest

`start-attempt` freezes *the* (run-level) manifest, yet `ExperimentAttempt.required` includes its own `manifestDigest`, and no invariant ties attempt digests to the run's. Either the manifest is per-run — in which case attempt 2 after a retry cannot record a changed environment or runtime, defeating `fixtures.json#failed-attempt-retained`'s "separate evidence" — or it is per-attempt, in which case "the run manifest pins…" (invariant 6) names an object the run does not uniquely own. Both readings are open in the file.

### D5 — Result access is governed but never recorded

Four separate invariants turn on it:
- `candidate.json`: *"A preregistered hypothesis pin precedes result access."*
- `local-evidence.md` inv. 4: *"Hypothesis precedes result access or is marked post-hoc"*, plus *"Timing is verified from event clocks."*
- `claude-study.raw.md`: *"timing is derived from clocks, never asserted: a registration whose timestamp does not precede first result access is rejected."*
- Grok inv. 11: *"Result access is logged against hypothesis version before any outcome is readable."*

**No object in `candidate.json` has a result-access event, a `firstResultAccessAt`, or an access log.** The run is the only plausible master (attempts produce the results) and it records nothing. The invariant is decorative.

### D6 — Post-hoc: new instance or successor revision?

Grok: *"A post-hoc hypothesis is a new explicit WM-KNW-009 instance, typed post-hoc … never an edit of the sealed one"* and inv. 2: *"cannot reuse the preregistered identity."* Against this, `local-evidence.md`: *"Reformulation creates a successor hypothesis revision"*, and `fixtures.json#rewrite-hypothesis-after-results` expects *"create an explicit post-hoc **or** successor hypothesis revision externally."* These are different identity outcomes. If a post-hoc proposition can land as a *revision* of the preregistered hypothesis, the preregistered identity absorbs post-hoc content and Grok inv. 2 fails. The disjunction in the fixture makes both outcomes passing.

### D7 — RunDeviation is over-required, untyped, and forces sentinels

`RunDeviation.required: ["experimentRunId","attemptId","kind","observedAt","plannedValue","executedValue","authorityRef","evidenceRefs"]`.

- **`attemptId` required** makes run-scope deviations (an amendment in force across the run; a planned-vs-executed difference found at run close) unrepresentable, or forces false attribution to an arbitrary attempt.
- **`kind` has no enumeration**, so `local-evidence.md` inv. 5 ("Deviations are append-only **and typed**") is unenforceable, and `claude-study.raw.md` inv. 5 — *"Preregistration deviations and protocol conduct deviations are separate, append-only records"* — has no mechanism: one unconstrained `kind` on one record type.
- **`plannedValue` and `executedValue` both required**: an unplanned event has no planned value; an omitted step has no executed value. The schema forces a sentinel, which is precisely the missingness conflation invariant 10 of the same file forbids.

### D8 — Missingness is fixtured but unowned and unmodelled

`fixtures.json#missing-versus-zero` expects *"**Run records** missingness or coverage."* But `boundary.owns` contains no missingness or coverage structure; observations are delegated to WM-MAT-008 and datasets to WM-DAT-001; `ExperimentAttempt` offers only optional `resultDatasetRefs` / `observationRefs`. There is no coded absence reason, no missingness pattern, no expected-versus-observed coverage field. The fixture demands behaviour the boundary forbids — a boundary leak in the fixture or an omission in `owns`; the artifacts do not say which.

### D9 — `successClass` is an unconstrained field adjacent to result semantics

`ExperimentRun.optional: [… "successClass" …]` with no enumeration and no definition, sitting beside invariants *"Successful orchestration proves neither scientific validity nor reproducibility"* and *"Absence, censoring, zero and no effect are never inferred from run status"*, and `excludes: ["truth or support status on a hypothesis"]`. Nothing prevents `successClass: "supported"`. Relatedly, `ExperimentAttempt.lifecycle` includes `failed`, and nothing states that `failed` is an orchestration state rather than a result state — Grok: *"Failed attempt, no effect, null and inconclusive are four states. A failed attempt is none of these."* Nor is it stated whether a run may be `completed` with all attempts `failed`.

### D10 — Lifecycle states mutate records declared immutable

`ExperimentRun.lifecycle: ["planned","running","completed","aborted","superseded"]` against invariant *"A completed or aborted run and its frozen manifest are immutable."* Moving a completed run to `superseded` **is** a mutation of the completed run. Direct contradiction within one file.

The same defect recurs in `allocation-candidate.json`: `DesignVersion.lifecycle` includes `superseded` and `withdrawn` while invariant 2 reads *"Every run pins exactly one **immutable** design version."* Withdrawing an effective version mutates a record closed runs pinned.

### D11 — Record erratum conflated with re-execution

`operations.correct-run-record`: *"Create a **successor run record** with correction reason while preserving the predecessor."* A transcription correction and a re-execution are different events, and here both produce a run occurrence. The acceptance scenario turns on runs being countable, distinct occurrences ("Two runs pin the same design but different input snapshots"); a corrected record that materialises as a second run can be miscounted as independent evidence. Grok permits *"a new run **or an erratum** linked to the original"* — the erratum path is absent.

### D12 — Containment versus reference, and an optional hypothesis pin

`claude-study.raw.md`: *"The relation `WM-ACT-036 CONTAINS WM-ACT-022` is `candidate`."* `candidate.json` declares only `{"target":"WM-ACT-036","relation":"REFERENCE","required":true}`. The two carry different deletion semantics, and invariant *"Deleting or withdrawing a study never cascades to evidence-bearing completed runs"* is consistent with REFERENCE and contradicted by CONTAINS. The artifacts do not resolve which relation holds, so the no-cascade invariant is unenforceable.

Separately: the WM-KNW-009 relation is `"required": false`, yet the preregistration invariant and the acceptance scenario both presuppose a hypothesis pin — **and `ExperimentRun` has no `hypothesisRevisionRefs` field at all**, nor does `RunManifest`. The "pin" named by the invariant has no storage.

### D13 — Access ceiling with no classification field

Invariant: *"Access to a run result cannot exceed access to its contributing design, inputs and observations."* No object carries a sensitivity label, classification, or access-policy reference; the manifest records no access metadata. `fixtures.json#restricted-input` expects *"Run and derived result access retain the stricter evidence ceiling"* — unevaluable against the supplied schema.

### D14 — Dual mastership of success and stopping rules

`local-evidence.md`: hypotheses *"freeze their prospective plan, criteria, success and stopping rules"* **and** *"The design release pins … success criteria and stopping rules."* `allocation-candidate.json` makes `successCriteria` **required** on `DesignVersion` (with `stoppingRules` optional). `claude-study.raw.md` inv. 12 contradicts both: *"Stopping and success rules are hypothesis-side preregistered criteria, not run-side outcomes."* Three artifacts, two masters, no precedence rule and no conflict invariant. A run can satisfy design-side criteria while violating hypothesis-side criteria with no defined resolution.

### D15 — Reusable design lifecycle is internally inconsistent

`ReusableExperimentDesign.lifecycle` and `identityTest.independentLifecycle` both list seven states including `reviewed` and `retired`. `DesignVersion.lifecycle` lists five and omits **both**. Yet invariant 12 reads *"**Retired design versions** remain resolvable for historical runs and findings"* — naming a version state that does not exist. `retiredAt` is optional on the design, absent from the version. Additionally `DesignVersion` carries `validFrom`/`validTo` **and** `status` with no rule tying `validTo` to `superseded`, and `contentDigest` is required with no declared canonicalization, so invariant 3 ("Changing outcomes, method, estimand, success criteria or stopping rules creates a successor version") cannot be mechanically checked.

### D16 — Attempt identity is free-standing, not subordinate

Fixed decision: Experiment Attempt has **stable subordinate identity**. `candidate.json`: `ExperimentAttempt.identity: ["attemptId"]` — a global key — with `experimentRunId` and `sequence` demoted to ordinary required fields. `RunDeviation` then requires *both* `experimentRunId` and `attemptId`, redundant under a global key and necessary under a subordinate one: the file assumes both models at once. Grok's blocker *"Give Attempt a retention key under the run"* is unmet; there is no retention or hold field anywhere, despite invariant *"Retry and rerun append a new attempt or run and never overwrite a failed one."*

### D17 — Temporal integrity is unspecified

`claude-study.raw.md` requires *"All RFC 3339 with seconds and explicit offset"* and clock-derived timing. `candidate.json` carries `startedAt`, `completedAt`, `abortedAt`, `observedAt`, `createdAt` with **no format constraint, no clock source, and no ordering invariants** — nothing requires `completedAt ≥ startedAt`, attempt intervals within the run interval, or monotonic `sequence` against `startedAt`. Invariant 4 ("Every attempt … has a monotonic sequence") constrains the counter but not its relation to time.

### D18 — Manifest is incomplete against its own stated contract

Measured against `claude-study.raw.md`'s enumeration, `RunManifest` omits **effective interval**. It reduces *"configuration and parameter set with secret references only"* to a bare `configurationDigest` — a digest neither demonstrates secret exclusion nor is verifiable without a canonicalization rule; no digest algorithm is declared for `codePins`, `dependencyPins`, or `manifestDigest`. **`randomness` is a single unconstrained field** where the contract requires *"seed, generator, draw order, and any declared nondeterminism"* — the two-run acceptance scenario distinguishes R1 from R2 by seed and cannot show seed was the only difference. Finally, `boundary.owns` claims *"reproducibility declaration"* and `claude-study.raw.md` grades it (*"reproducible … explainable or partially reproducible"*), but **no field or enum represents it**.

### D19 — Fixture suite does not discriminate

- `missing-versus-zero` and `restricted-input` are `"kind": "negative"` but their `input` describes a *condition*, not an attempted violation, and their `expect` describes behaviour rather than rejection — unlike `delete-failed-run` ("Rejected; …"). An executor cannot derive pass/fail.
- **No fixture carries an `expectedCode`**, so no rejection reason is verifiable; any refusal passes any negative case.
- 15 invariants, 7 fixtures. Unfixtured: manifest completeness, monotonic attempt sequence, one-design pin, study-withdrawal no-cascade, orchestration-success-is-not-validity, post-hoc marking, access ceiling enforcement.
- `validation-policy.json` governs only the allocation candidate (which it satisfies: null ids, `unassigned`, 12 ≥ 8 invariants, 7 ≥ 3 references, 6 ≥ 3 fixtures, both polarities present). **There is no validation policy for WM-ACT-022 at all.**

### D20 — Unpinned cross-contour dependency and a schema-name mismatch

`profile-candidate.json`: *"Evidence Artifact reuses the EM-KNW-02 candidate rather than creating a duplicate"* — but Evidence Artifact is not in `bases`, has no artifact in this package, and is cited with no contour version or digest. An unassigned, out-of-contour candidate is load-bearing here with no pin. Separately, `claude-study.raw.md` reports *"All bases are `publishableCanonical: false`"* while `candidate.json` and `allocation-candidate.json` use `canonicalPublishable`. One of the two field names is wrong; mechanical validation fails either way.

### D21 — Authorities are named in operations, unrecorded in objects

All seven operations declare an `authority` ("authorized investigator", "authorized recorder", "study steward"), but **only `RunDeviation` has an `authorityRef`**. No `actorRef` exists on run or attempt lifecycle transitions. Append-only evidence with no accountable agent cannot support the retention and non-repudiation claims in invariants 5 and 14.

**Non-material (recorded, not blocking):** `local-evidence.md` invariant 1 drops `dataset` from the distinct-identity list that `candidate.json` invariant 1 includes; `local-evidence.md` invariant 9 drops "fitness" from `claude-study.raw.md` invariant 10. Drafting slips, same intent.

---

## 3. Required bounded fixes

No new model identifiers, no registry writes, no change to the fixed identity decision.

1. **D1** — In `profile-candidate.json` replace *"without new identity"* with *"without new **model** identity; the Finding **instance** identity is the composed key (studyRef, hypothesisRevisionRef, analysisRef, assertedAt) resolved through WM-KNW-007."* Add a `ResearchFinding` profile object specifying that composed identity key, required `uncertainty` (kind, value, coverage factor, probability), `applicability`, `limitations`, `citedRunRefs`, `assessment` (source-qualified), and supersession-by-successor-assertion. Mirror the correction in `local-evidence.md`.
2. **D2** — Add `designPin: {masterRef, designVersionRef, pinKind: "study-scoped-release" | "reusable-design-version"}` to `ExperimentRun` and `RunManifest`. Add a seventh relation entry targeting the unassigned reusable design, `required: false`, explicitly marked unresolvable until allocation. Add `derivedFromStudyReleaseRef` to `allocation-candidate.json#DesignVersion` and a promotion invariant preserving the predecessor pin.
3. **D3** — Add `manifestState: ["draft","frozen"]` and `frozenAt`. Make `manifestDigest` the identity **only in `frozen`**; give drafts a separate `draftManifestId`. Replace `ExperimentRun.runManifest` with `manifestDigest`. Add invariant: no attempt, deviation or external record may reference a draft manifest.
4. **D4** — State the cardinality: one frozen manifest per **attempt**, with `ExperimentRun.manifestDigest` denoting the first frozen attempt manifest and an invariant requiring every later attempt manifest to differ only in declared fields and to carry `manifestDeltaFromRunManifest`.
5. **D5** — Add `ResultAccessEvent {resultAccessId, experimentRunId, attemptId?, hypothesisRevisionRef, accessedAt, actorRef, clockSourceRef}`, append-only, owned by WM-ACT-022. Add invariant: a hypothesis pin is prospective only if its registration timestamp strictly precedes the earliest `ResultAccessEvent.accessedAt` for that revision; otherwise the pin is `post-hoc`.
6. **D6** — Split the terms. Preregistered → post-hoc is **always a new WM-KNW-009 instance**, never a revision; revision is reserved for refinement **before** first result access. Rewrite `fixtures.json#rewrite-hypothesis-after-results` to drop the "or successor revision" disjunction and expect a new post-hoc instance.
7. **D7** — Move `attemptId` to `optional` and add `scope: ["run","attempt"]` as required. Enumerate `kind: ["preregistration-deviation","protocol-conduct-deviation","configuration-deviation","environment-deviation","sampling-deviation","unplanned-event","omission"]`. Make `plannedValue`/`executedValue` conditionally required by kind, each with an explicit `not-applicable` coded absence rather than a sentinel.
8. **D8** — Add to `boundary.owns`: *"observed-versus-expected coverage of the run's planned collection, with coded absence reason and missingness pattern, referencing but never copying WM-MAT-008 observations."* Add `RunCoverage {experimentRunId, attemptId, plannedUnits, observedUnits, absenceReason, missingnessPattern}`. Restate the fixture against it.
9. **D9** — Enumerate `successClass: ["orchestration-success","orchestration-partial","orchestration-failure"]` and add invariant: `successClass` and attempt lifecycle are orchestration states and may never carry negative, null, inconclusive, no-effect or support semantics. State explicitly that a run may be `completed` with all attempts `failed`.
10. **D10** — Remove `superseded` from `ExperimentRun.lifecycle`; record supersession on the successor as `supersedesRunId` plus an append-only `RunSupersessionLink`. In `allocation-candidate.json`, scope immutability to **content**, and record `superseded`/`withdrawn`/`retired` as append-only `DesignVersionStatusEvent` records, not in-place field edits.
11. **D11** — Split `correct-run-record` into `issue-run-erratum` (append-only erratum attached to the original run; mints no run occurrence) and `supersede-run-by-reexecution` (new run occurrence). Add invariant: errata never increment the run count for evidence aggregation.
12. **D12** — Pin the relation as `REFERENCE` in both this candidate and the WM-ACT-036 coverage note, and record the CONTAINS row as a conflicting external candidate held for reconciliation. Add `hypothesisRevisionRefs` (array, min 1 for runs declaring a hypothesis test) to `ExperimentRun` and `RunManifest`, and make the WM-KNW-009 relation `required: true` for hypothesis-testing runs via a declared conditional.
13. **D13** — Add `accessClassificationRef` to `ExperimentRun`, `RunManifest.inputDatasetPins[]`, and `RunCoverage`, and an invariant computing the run's effective ceiling as the maximum restriction over design, inputs and observations. Restate `restricted-input` as a positive enforcement fixture.
14. **D14** — Declare WM-KNW-009 the master of preregistered success and stopping criteria. In `allocation-candidate.json` rename `successCriteria` to `designSuccessCriteriaRef` and `stoppingRules` to `designStoppingRulesRef`, both pointing at the hypothesis-side criteria, and add a precedence invariant: on conflict, hypothesis-side criteria govern and the divergence is a preregistration deviation.
15. **D15** — Align `DesignVersion.lifecycle` to `["draft","reviewed","approved","effective","superseded","withdrawn","retired"]`, add `retiredAt`, tie `validTo` to the `superseded`/`retired` transition by invariant, and declare the `contentDigest` canonicalization (field set and serialization) covering the five change-triggering elements.
16. **D16** — Change `ExperimentAttempt.identity` to `["experimentRunId","sequence"]`, keep `attemptId` as an optional surrogate, and add `retentionClass` plus `legalHoldRef`. Drop the now-redundant `experimentRunId` duplication rationale in `RunDeviation` by referencing the composite key.
17. **D17** — Add a format constraint: all timestamps RFC 3339 with seconds and explicit offset, plus `clockSourceRef` on every time-bearing record. Add ordering invariants: `completedAt`/`abortedAt` ≥ `startedAt`; attempt interval ⊆ run interval; `sequence` monotonic in `startedAt`.
18. **D18** — Add `effectiveInterval` to `RunManifest`. Replace `configurationDigest` with `{configurationDigest, digestAlgorithm, canonicalizationRule, secretReferencesOnly: true}`; declare `digestAlgorithm` for code, dependency and manifest digests. Expand `randomness` to `{seed, generator, drawOrder, declaredNondeterminism[]}`. Add `reproducibilityGrade: ["reproducible","partially-reproducible","explainable","not-reproducible"]` derived from manifest completeness, with an invariant that it is a manifest property, never a run-outcome property.
19. **D19** — Re-kind `missing-versus-zero` and `restricted-input` as positive enforcement cases; add `expectedCode` to every negative case; add the fixtures in §4 to close invariant coverage; add a `validation-policy.json` for WM-ACT-022 requiring invariant-to-fixture coverage ≥ 1 and both polarities.
20. **D20** — Add Evidence Artifact to `profile-candidate.json` as an explicitly unassigned, pinned cross-contour dependency (`contourRef: "EM-KNW-02"`, candidate version, `allocationState: "unassigned"`), or drop the constraint until EM-KNW-02 is pinned. Normalize the field name to `canonicalPublishable` across all artifacts and correct `claude-study.raw.md`'s reference.
21. **D21** — Add required `actorRef` and `authorityRef` to every lifecycle-transition record on `ExperimentRun`, `ExperimentAttempt` and the new erratum/supersession/result-access records.

---

## 4. Additional fixtures

```json
[
  {"target":"EM-PRD-04-profile","id":"d1-finding-instance-identity-required","kind":"negative","input":"A Research Finding is asserted with no instance identity, relying on the WM-ACT-036 study profile alone to address it.","expect":"Rejected; a finding must carry a composed instance identity resolved through WM-KNW-007 even though no new model identity is minted.","expectedCode":"E_FINDING_INSTANCE_IDENTITY_MISSING"},
  {"target":"EM-PRD-04-profile","id":"d1-finding-required-qualifiers","kind":"negative","input":"A finding is recorded with an assessment but without uncertainty, applicability or limitations.","expect":"Rejected; all three qualifiers are required on every finding assertion.","expectedCode":"E_FINDING_QUALIFIERS_INCOMPLETE"},
  {"target":"EM-PRD-04-profile","id":"d1-finding-supersession-not-edit","kind":"positive","input":"A published finding is revised after further analysis.","expect":"A successor finding assertion is appended and the predecessor remains resolvable; no in-place edit occurs."},
  {"target":"WM-ACT-022","id":"d2-design-pin-discriminator","kind":"negative","input":"A run supplies designVersionRef without pinKind or masterRef.","expect":"Rejected; the design pin must name its master and declare study-scoped-release or reusable-design-version.","expectedCode":"E_DESIGN_PIN_UNRESOLVABLE"},
  {"target":"reusable-experiment-design","id":"d2-promotion-derivation-link","kind":"negative","input":"A study-scoped release is promoted to a reusable design without a derivedFromStudyReleaseRef.","expect":"Rejected; promotion mints a new identity only with an explicit derivation link, and pre-existing run pins remain valid against the predecessor.","expectedCode":"E_PROMOTION_DERIVATION_MISSING"},
  {"target":"WM-ACT-022","id":"d3-draft-manifest-not-referenceable","kind":"negative","input":"An attempt references a manifest whose manifestState is draft.","expect":"Rejected; only a frozen manifest with frozenAt may be referenced or digest-addressed.","expectedCode":"E_MANIFEST_NOT_FROZEN"},
  {"target":"WM-ACT-022","id":"d3-draft-edit-does-not-reassign-identity","kind":"positive","input":"A planned run's draft manifest is edited three times before the first attempt starts.","expect":"The draft retains one draftManifestId across edits; manifestDigest is assigned only at freeze."},
  {"target":"WM-ACT-022","id":"d4-attempt-manifest-delta","kind":"positive","input":"Attempt 2 reruns after a runtime upgrade, so its frozen manifest differs from attempt 1's.","expect":"Attempt 2 carries its own frozen manifestDigest plus manifestDeltaFromRunManifest; attempt 1's manifest is unchanged."},
  {"target":"WM-ACT-022","id":"d4-undeclared-manifest-divergence","kind":"negative","input":"Attempt 2's manifest differs from the run manifest in an undeclared field.","expect":"Rejected; every divergence must appear in manifestDeltaFromRunManifest.","expectedCode":"E_MANIFEST_DELTA_UNDECLARED"},
  {"target":"WM-ACT-022","id":"d5-result-access-logged","kind":"positive","input":"An investigator reads attempt results for the first time.","expect":"A ResultAccessEvent is appended with accessedAt, actorRef, clockSourceRef and the hypothesis revision in scope."},
  {"target":"WM-ACT-022","id":"d5-prospective-claim-without-access-log","kind":"negative","input":"A hypothesis pin is asserted prospective but no ResultAccessEvent exists for the run.","expect":"Rejected; prospective status is clock-derived from the earliest logged result access and cannot be asserted.","expectedCode":"E_RESULT_ACCESS_LOG_MISSING"},
  {"target":"WM-ACT-022","id":"d5-registration-after-first-access","kind":"negative","input":"Hypothesis registration timestamp falls after the earliest ResultAccessEvent for its revision.","expect":"Rejected as prospective; the pin must be recorded post-hoc.","expectedCode":"E_PREREGISTRATION_TIMING_VIOLATION"},
  {"target":"WM-ACT-022","id":"d6-posthoc-must-be-new-instance","kind":"negative","input":"A post-hoc proposition is appended as a successor revision of the sealed preregistered hypothesis.","expect":"Rejected; post-hoc formulation creates a new WM-KNW-009 instance typed post-hoc and may not reuse the preregistered identity.","expectedCode":"E_POSTHOC_IDENTITY_REUSE"},
  {"target":"WM-ACT-022","id":"d6-prefirst-access-revision-allowed","kind":"positive","input":"A hypothesis is refined before any ResultAccessEvent exists.","expect":"A successor revision is created under the same hypothesis identity and remains prospective."},
  {"target":"WM-ACT-022","id":"d7-run-scope-deviation","kind":"positive","input":"A protocol amendment in force for the whole run is recorded at run close with no single responsible attempt.","expect":"A deviation with scope run and no attemptId is accepted."},
  {"target":"WM-ACT-022","id":"d7-untyped-deviation","kind":"negative","input":"A deviation is recorded with a free-text kind outside the enumeration.","expect":"Rejected; deviation kind must be one of the enumerated preregistration or conduct types.","expectedCode":"E_DEVIATION_KIND_UNTYPED"},
  {"target":"WM-ACT-022","id":"d7-sentinel-planned-value","kind":"negative","input":"An unplanned-event deviation supplies plannedValue of 0 to satisfy the required field.","expect":"Rejected; absence of a planned value is a coded not-applicable, never a sentinel number.","expectedCode":"E_DEVIATION_SENTINEL_VALUE"},
  {"target":"WM-ACT-022","id":"d8-coverage-recorded","kind":"positive","input":"Twelve of twenty planned collection units yield no observation.","expect":"RunCoverage records planned and observed units with coded absence reason and missingness pattern; no observation is copied into the run."},
  {"target":"WM-ACT-022","id":"d8-coverage-as-zero","kind":"negative","input":"Uncollected units are summarized in the run as a zero observed value.","expect":"Rejected; absence is coded in RunCoverage and never expressed as zero or no effect.","expectedCode":"E_ABSENCE_AS_ZERO"},
  {"target":"WM-ACT-022","id":"d9-successclass-result-semantics","kind":"negative","input":"A run sets successClass to supported after its analysis.","expect":"Rejected; successClass is restricted to orchestration outcomes and carries no hypothesis support semantics.","expectedCode":"E_RUN_STATUS_RESULT_CONFLATION"},
  {"target":"WM-ACT-022","id":"d9-completed-run-all-attempts-failed","kind":"positive","input":"A run is closed after every attempt reaches failed.","expect":"The run completes with orchestration-failure; the outcome is neither negative, null nor inconclusive."},
  {"target":"WM-ACT-022","id":"d10-no-superseded-state-on-completed-run","kind":"negative","input":"A completed run's status is changed to superseded when a re-execution closes.","expect":"Rejected; supersession is recorded on the successor and as an append-only link, never as a status mutation on the immutable predecessor.","expectedCode":"E_IMMUTABLE_RECORD_STATUS_MUTATION"},
  {"target":"reusable-experiment-design","id":"d10-withdraw-pinned-version","kind":"positive","input":"An effective design version pinned by a closed run is withdrawn.","expect":"A DesignVersionStatusEvent is appended; the version content and the closed run's pin are unchanged and remain resolvable."},
  {"target":"WM-ACT-022","id":"d11-erratum-is-not-a-run","kind":"positive","input":"A mistyped instrument reference on a completed run is corrected.","expect":"An erratum is appended to the original run; no new run occurrence is created and evidence aggregation still counts one run."},
  {"target":"WM-ACT-022","id":"d11-erratum-as-reexecution","kind":"negative","input":"A metadata correction is issued through supersede-run-by-reexecution with no new execution.","expect":"Rejected; record correction uses issue-run-erratum.","expectedCode":"E_ERRATUM_AS_REEXECUTION"},
  {"target":"WM-ACT-022","id":"d12-study-withdrawal-no-cascade","kind":"positive","input":"WM-ACT-036 withdraws the owning study after two completed runs.","expect":"Both completed runs, their manifests, attempts and deviations remain resolvable and citable; nothing is removed."},
  {"target":"WM-ACT-022","id":"d12-hypothesis-pin-missing","kind":"negative","input":"A run declares itself hypothesis-testing but records no hypothesisRevisionRefs.","expect":"Rejected; a hypothesis-testing run must pin at least one WM-KNW-009 revision in run and manifest.","expectedCode":"E_HYPOTHESIS_PIN_MISSING"},
  {"target":"WM-ACT-022","id":"d13-access-ceiling-enforced","kind":"positive","input":"One input dataset is classified more restrictively than the run summary.","expect":"The run's effective access ceiling is raised to the strictest contributing classification and applies to derived results."},
  {"target":"WM-ACT-022","id":"d13-missing-classification","kind":"negative","input":"An input dataset pin carries no accessClassificationRef.","expect":"Rejected; the access ceiling cannot be computed from an unclassified contributor.","expectedCode":"E_ACCESS_CLASSIFICATION_MISSING"},
  {"target":"reusable-experiment-design","id":"d14-criteria-master-precedence","kind":"negative","input":"A design version states success criteria that conflict with the pinned preregistered hypothesis criteria.","expect":"Rejected; WM-KNW-009 masters preregistered success and stopping criteria and the divergence must be recorded as a preregistration deviation.","expectedCode":"E_CRITERIA_DUAL_MASTERSHIP"},
  {"target":"reusable-experiment-design","id":"d15-retired-version-resolvable","kind":"positive","input":"A design version used by a historical run is retired.","expect":"The version enters the retired state with retiredAt, validTo is set, and the historical run and its findings still resolve the pin."},
  {"target":"reusable-experiment-design","id":"d15-silent-criteria-edit","kind":"negative","input":"Stopping rules are edited inside an effective design version without a successor.","expect":"Rejected; the change alters the declared contentDigest field set and requires a successor version.","expectedCode":"E_DESIGN_VERSION_CONTENT_MUTATION"},
  {"target":"WM-ACT-022","id":"d16-attempt-subordinate-key","kind":"negative","input":"An attempt is created with an attemptId but no run-scoped sequence.","expect":"Rejected; attempt identity is the composite experimentRunId plus sequence.","expectedCode":"E_ATTEMPT_IDENTITY_NOT_SUBORDINATE"},
  {"target":"WM-ACT-022","id":"d16-failed-attempt-retention","kind":"negative","input":"A failed attempt is purged under a storage policy after a successful rerun.","expect":"Rejected; the attempt's retentionClass and run-scoped key preserve it as queryable evidence.","expectedCode":"E_ATTEMPT_RETENTION_VIOLATION"},
  {"target":"WM-ACT-022","id":"d17-timestamp-format","kind":"negative","input":"startedAt is recorded without an explicit UTC offset.","expect":"Rejected; all timestamps are RFC 3339 with seconds and explicit offset.","expectedCode":"E_TIMESTAMP_FORMAT_INVALID"},
  {"target":"WM-ACT-022","id":"d17-interval-ordering","kind":"negative","input":"An attempt's startedAt precedes its run's startedAt.","expect":"Rejected; attempt intervals must fall within the run interval and sequence must be monotonic in startedAt.","expectedCode":"E_TEMPORAL_ORDER_VIOLATION"},
  {"target":"WM-ACT-022","id":"d18-manifest-completeness-grade","kind":"positive","input":"A manifest omits calibrationRefs but pins everything else.","expect":"The manifest is accepted with reproducibilityGrade partially-reproducible and the omission is explicit."},
  {"target":"WM-ACT-022","id":"d18-randomness-structure","kind":"negative","input":"Randomness is recorded as the scalar 4711.","expect":"Rejected; randomness requires seed, generator, draw order and declared nondeterminism.","expectedCode":"E_RANDOMNESS_UNDERSPECIFIED"},
  {"target":"WM-ACT-022","id":"d18-secret-in-configuration","kind":"negative","input":"A configuration pin embeds a credential value rather than a secret reference.","expect":"Rejected; configuration pins carry secret references only.","expectedCode":"E_SECRET_MATERIAL_IN_MANIFEST"},
  {"target":"WM-ACT-022","id":"d18-reproducibility-from-single-success","kind":"negative","input":"A run with one successful attempt is declared reproducible on that basis.","expect":"Rejected; reproducibilityGrade is derived from manifest completeness, never from run outcome.","expectedCode":"E_REPRODUCIBILITY_FROM_RUN_OUTCOME"},
  {"target":"WM-ACT-022","id":"d19-negative-fixture-requires-code","kind":"negative","input":"A negative fixture is registered with no expectedCode.","expect":"Rejected; every negative case must name the rejection code it asserts.","expectedCode":"E_FIXTURE_EXPECTED_CODE_MISSING"},
  {"target":"WM-ACT-022","id":"d19-invariant-coverage","kind":"negative","input":"The candidate is submitted with at least one invariant having no fixture.","expect":"Rejected; validation policy requires at least one fixture per invariant and both polarities present.","expectedCode":"E_INVARIANT_COVERAGE_INCOMPLETE"},
  {"target":"EM-PRD-04-profile","id":"d20-unpinned-cross-contour-base","kind":"negative","input":"The profile constrains Evidence Artifact to the EM-KNW-02 candidate with no contour reference, version or allocation state.","expect":"Rejected; a cross-contour dependency must be pinned and marked unassigned, or removed.","expectedCode":"E_CROSS_CONTOUR_DEPENDENCY_UNPINNED"},
  {"target":"EM-PRD-04-profile","id":"d20-publishable-field-name","kind":"negative","input":"An artifact declares publishableCanonical instead of canonicalPublishable.","expect":"Rejected; the field name is canonicalPublishable across all EM-PRD-04 artifacts.","expectedCode":"E_SCHEMA_FIELD_NAME_MISMATCH"},
  {"target":"WM-ACT-022","id":"d21-transition-actor-required","kind":"negative","input":"A run is completed with no actorRef or authorityRef on the transition.","expect":"Rejected; every lifecycle transition records its acting agent and authority.","expectedCode":"E_TRANSITION_ACTOR_MISSING"},
  {"target":"WM-ACT-022","id":"d21-deviation-authority-chain","kind":"positive","input":"A recorder appends a conduct deviation under a steward's standing authorization.","expect":"The deviation retains both actorRef and authorityRef and remains append-only."}
]
```

---

## 5. Identifier decision

Explicit and unchanged from the fixed decision; this audit invents nothing and mutates no registry.

- **WM-ACT-036** — reused as Research Study aggregate. No new identifier. Publication hold retained.
- **WM-KNW-009** — reused as Hypothesis master. No new identifier. Publication hold retained. Post-hoc hypotheses are **new instances of this model**, not new models.
- **WM-ACT-022** — the reserved identifier is completed narrowly as **Experiment Run**. No new identifier allocated; `registryId: "vr.wm-act-022"` is the pre-existing reservation, not an allocation by this audit. `canonicalPublishable` remains `false`.
- **Study-scoped Experiment Design** — **no identity.** An immutable design release inside WM-ACT-036.
- **Reusable cross-study Experiment Design** — genuinely requires independent identity; remains `modelId: null`, `registryId: null`, `allocationState: "unassigned"`. **No identifier is guessed, reserved or implied here.** It satisfies `validation-policy.json` as submitted; allocation is a registry act outside this audit.
- **Experiment Attempt, Run Manifest, Run Deviation, Result Access Event, Run Coverage** — subordinate objects inside WM-ACT-022. No model identifiers. Attempt identity must become the run-subordinate composite (D16).
- **Research Finding** — **mints no model identity**; it is a profile over WM-ACT-036 findings, WM-KNW-007 claims and WM-KNW-008 evidence bindings. It **does** require instance identity, composed from those existing bases (D1). The two are not the same thing and the artifacts currently conflate them.
- **Evidence Artifact** — remains an unassigned EM-KNW-02 candidate. Not allocated here; must be pinned or dropped (D20).

Referenced without change: **WM-KNW-007**, **WM-KNW-008**, **WM-MAT-008**, **WM-DAT-001**, **WM-ACT-053**.

---

## 6. Freeze decision

**Closed. No rerun.**

This was the single frozen semantic audit for EM-PRD-04 and it is now spent. The verdict is REVISE on the artifacts, not on the identity adjudication, which I accept as fixed and leave intact. The twenty-one defects are bounded and locally fixable: they require field additions, enumerations, two operation splits, one lifecycle removal, one identity-key change and a fixture suite that discriminates. None requires a new model identifier and none reopens the identity question.

Registry and base-publication gaps — WM-ACT-036 and WM-KNW-009 holds, candidate-only relation rows, the unallocated reusable design, the unpinned Evidence Artifact allocation — remain **holds**, counted against the package's installability and not against the artifacts' semantics. The remaining gates named in `local-evidence.md` (exact Grok comparison, package conversion, live verification) are unaffected by this audit and still stand. No installable release is claimed.
