# Frozen semantic audit — EM-PEO-05 Learning, Development and Succession

Auditor scope: the frozen dossier only. No tools, no external facts, no invented identifiers. Every `WM-*` token below is quoted from the dossier; I make no claim that any of them resolves, since `sourceFacts.bases` states the bases are held reviewable drafts.

---

## 1. Verdict

**REVISE.**

The four-root reconciliation plus the fifth Learning Result root is semantically sound in direction, and the collapse prohibitions are unusually well stated. But the dossier cannot be advanced as-is: it contains at least one internal impossibility in the object schema (`finalizedAt` required against a `provisional` state), one outcome value asserted in `objects` but absent from the identity and boundary statements (`indeterminate`), a duplicated field, several concepts declared `owns` with no field able to carry them, load-bearing pins whose referent has no defined identity (objective version), no attribution field anywhere despite repeated "attributable" invariants, and no rule determining which of several appended Learning Results is the effective outcome. Those are definition-, history- and privacy-affecting, not cosmetic.

---

## 2. Unassigned roots and allocation

**Confirmed: five roots, all identifier-unassigned, no allocation performed.**

| Root | `modelId` | `registryId` | `allocationState` | `decision` | `canonicalPublishable` |
|---|---|---|---|---|---|
| Learning Program | null | null | unassigned | NEW MODEL | false |
| Enrollment | null | null | unassigned | NEW MODEL | false |
| Career Path | null | null | unassigned | NEW MODEL | false |
| Succession Plan | null | null | unassigned | NEW MODEL | false |
| Learning Result | null | null | unassigned | NEW MODEL | false |

Confirmations:
- No candidate guesses, reserves or implies a registry identifier. Each carries the hold "Registry allocation is pending and no identifier may be guessed." Learning Result additionally states it as an invariant.
- The profile declares `decision: PROFILE`, `newRuntimeId: false`, `canonicalPublishable: false`, and all six `relationContracts` provisional.
- `candidateRevision: 2` is consistent at dossier, candidate and profile level.

One rejection at this level: **`profile.newRuntimeId: false` is not confirmable as written** (see D28). The profile has no field that binds the five unallocated roots it governs, so "no new runtime identity" reads against five `NEW MODEL` decisions. The flag needs scoping, not removal.

---

## 3. Defects

Each defect: evidence → remediation → one fixture expectation. All fixture expectations are declarative per `sourceFacts.runtime`; each is phrased for later executable conversion.

### A. Concepts with no owning master (collapse risk)

**D1 — Attendance and delivery completion have no master.**
`learning-program.excludes`, `enrollment.excludes` and `learning-result.excludes` all exclude attendance and completion; `enrollment.objects.Enrollment.optional` carries `attendanceRefs` and `completionRef`; the only candidate reference is `WM-ACT-038` "Delivery participation". No base or root owns attendance or completion identity, so both will be read off Enrollment status or Delivery state.
*Remediation:* add an explicit profile constraint naming the master for attendance facts and for delivery completion (either a narrowed `WM-ACT-038` participation object or a sixth candidate root), and add a hold if neither is decided; retype `attendanceRefs`/`completionRef` as non-authoritative back-references.
*Fixture:* `attendance-master` (negative) — "An attendance fact is asserted with only an Enrollment status change as its source. Normatively, the assertion is non-conformant without a reference to the named attendance master."

**D2 — Assessment administration/occurrence has no master.**
`WM-ACT-034` is described only as "Assessment result" / "Readiness assessment"; `learning-program.excludes` excludes "assessment occurrence" and `learning-result.excludes` excludes "assessment administration or raw score ownership". The sitting, administration and raw score therefore have no owner, yet `assessmentBasisRefs` is required.
*Remediation:* state in `profile.constraints` whether administration and raw score are inside the narrowed `WM-ACT-034` or excluded from the contour, and pin which object `assessmentBasisRefs` targets.
*Fixture:* `basis-target` (negative) — "A Learning Result cites an assessment basis that resolves to no named administration or result master. Normatively, the result is non-conformant."

**D3 — Competency assertion has no master.**
`learning-result.excludes` excludes "competency assertion" and `profile.constraints` declares it non-equivalent to results; `career-path.references` cites `WM-PER-009` only for "Competency expectations", and `WM-PER-009` is absent from `profile.bases` and `relationContracts`.
*Remediation:* either add the competency authority to `bases` and `relationContracts` with a stated purpose covering assertion (not only expectation), or record a hold that competency assertion is out of contour.
*Fixture:* `competency-not-result` (negative) — "An achieved Learning Result is exposed as a competency assertion. Normatively, the identity collapse is non-conformant."

**D4 — Credential has no contracted master.**
`learning-result.references` cites `WM-XCT-017` "Optional downstream credential", and three other roots exclude "credential", but `WM-XCT-017` appears in neither `profile.bases` nor `profile.relationContracts`.
*Remediation:* add `WM-XCT-017` to `bases` and `relationContracts` with a provisional contract, or hold the credential relation as out of contour and delete the reference.
*Fixture:* `credential-contract` (negative) — "A credential relation is exercised against a target with no recorded relation contract. Normatively, the relation is non-conformant."

**D5 — Aspiration has no master.**
`career-path.excludes` excludes "worker aspiration" and its invariant asserts "Aspiration is a time-stamped person assertion and never path identity, nomination or appointment" — a positive semantic claim about an object no root or base owns, with no time-stamp field anywhere.
*Remediation:* assign aspiration to a named base (candidate: the `WM-ACT-008` development-plan profile) with a stated constraint, or add it as a sixth candidate root; the invariant must not assert structure the dossier does not locate.
*Fixture:* `aspiration-located` (positive) — "A worker records a career aspiration with no career path published. Normatively, the aspiration is recorded against its named master with recorded time and is not path, nomination or appointment."

**D6 — Access/entitlement has no named authority.**
`enrollment` ("grants no access"), `career-path` ("never creates assignment or access") and `succession-plan` ("access grant" excluded; `ready-not-access` fixture) all deny granting access, but no base governs access or entitlement. `WM-ORG-016` is assignment, not access.
*Remediation:* name the access/entitlement authority in `bases` and `relationContracts`, or record an explicit hold that access is governed outside EM-PEO-05 and that all access denials are therefore unenforceable here.
*Fixture:* `access-authority` (negative) — "An access entitlement is derived from Enrollment, pool membership or path step. Normatively, the derivation is non-conformant and access remains owned by the named external authority."

**D7 — Nomination has no traceable representation.**
`succession-plan.owns` includes "candidate-pool membership" and its fixture `later-appointment` expects "Separate nomination, appointment and assignment records are required", but `SuccessionPlanRevision` has no field linking a `poolEntries` entry to a `WM-REC-010` nomination or appointment decision. The chain pool entry → nomination → appointment → assignment is unrepresentable, so nomination history can be lost.
*Remediation:* add optional `nominationRefs` / `appointmentRefs` on the pool entry (not the revision), each pinning the decision identity and its recorded time, with an invariant that references are non-authoritative pointers to `WM-REC-010`.
*Fixture:* `nomination-traceable` (positive) — "A pool entry produces a nomination and later an appointment. Normatively, both decisions remain resolvable from the pool entry without the plan owning either decision."

### B. Relation contracts

**D8 — Six referenced targets carry no relation contract.**
`profile.relationContracts` lists only `WM-ACT-038`, `WM-PER-008`, `WM-ACT-008`, `WM-ACT-034`, `WM-REC-010`, `WM-ORG-016`. Candidates additionally reference `WM-PER-001`, `WM-ORG-004`, `WM-XCT-023`, `WM-PER-009`, `WM-KNW-013`, `WM-XCT-017` — all uncontracted and absent from `bases`.
*Remediation:* add all six to `bases` and `relationContracts` as provisional, or remove the references and record the loss as a hold. Do not leave references outside the contract table.
*Fixture:* `contract-closure` (negative) — "A candidate references a target absent from `relationContracts`. Normatively, the candidate is non-conformant until the contract is recorded."

**D9 — Intra-contour relations between the five unallocated roots are unrecorded.**
`Enrollment.programVersionRef`, `LearningResult.enrollmentRef`/`programVersionRef`/`objectiveVersionRef`, the career-path invariant "Path steps may recommend Program Versions and objective versions", and the succession invariant "pins the assessed position or path-step profile version" are all cross-root relations. None appears in `relationContracts`, which contains bases only.
*Remediation:* extend `relationContracts` (or add `internalRelationContracts`) to cover every root-to-root relation with contract state `provisional` and an explicit note that the targets are identifier-unassigned.
*Fixture:* `internal-contract` (negative) — "A root-to-root reference is exercised with no recorded internal relation contract. Normatively, the reference is non-conformant."

**D10 — Pool membership references persons with no person authority.**
`succession-plan.owns` includes "candidate-pool membership" and `excludes` "person or position identity", yet `succession-plan.references` cites no person model (`WM-PER-001` is referenced only by Enrollment and Learning Result).
*Remediation:* add the person reference with purpose "pool member identity" and contract state `provisional`.
*Fixture:* `pool-person-ref` (negative) — "A pool entry carries an inline person label instead of a reference to the person master. Normatively, the entry is non-conformant."

### C. Load-bearing pins

**D11 — Objective-version identity is asserted but never defined.**
`ProgramVersion.required` lists both `objectives` and `objectiveVersions` with no stated relationship, no identifier field, and no identity tuple; `LearningProgram.invariants` claims "Objectives have stable version-scoped identifiers"; `LearningResult.required.objectiveVersionRef` and the fixture `missing-objective-version` both depend on that identity. The most load-bearing pin in the contour has no referent.
*Remediation:* define an addressable objective-version identity (e.g. `ObjectiveVersion` with identity `[learningProgramId, version, objectiveId, objectiveVersion]`), state whether `objectives` is descriptive content or the identity carrier, and remove the duplication.
*Fixture:* `objective-version-resolvable` (positive) — "A Learning Result pins an objective version. Normatively, the pin resolves to exactly one identified objective version inside the pinned Program Version."

**D12 — Result pins are not constrained to be mutually consistent.**
`LearningResult` requires `enrollmentRef`, `programVersionRef` and `objectiveVersionRef`, and `Enrollment` requires its own `programVersionRef`, but no invariant requires the result's Program Version to equal the enrollment's, nor the objective version to belong to the pinned Program Version. Cross-program and cross-version contamination is admissible.
*Remediation:* add two invariants: the result's `programVersionRef` equals the pinned enrollment's `programVersionRef` (or an explicitly recorded transfer successor of it, per D22); the `objectiveVersionRef` is scoped to that Program Version.
*Fixture:* `pin-consistency` (negative) — "A Learning Result pins a Program Version other than the one pinned by its Enrollment, with no recorded transfer. Normatively, the result is non-conformant."

**D13 — Three overlapping assessment-criteria mechanisms with no authority order.**
`ProgramVersion.required.assessmentDesignVersion`, `ProgramVersion.optional.assessmentPolicy`, and the `WM-KNW-013` "Pinned criteria" reference all bear on the invariant "Assessment criteria are pinned", with no statement of which prevails.
*Remediation:* declare one authoritative pin, state the other two as derived or descriptive, and make the invariant name the authoritative field.
*Fixture:* `criteria-authority` (negative) — "A Program Version carries an assessment policy that conflicts with its pinned criteria. Normatively, the version is non-conformant and the authoritative pin governs."

**D14 — `assessmentBasisRefs` versus `assessmentResultRefs` ambiguity.**
The first is required, the second optional, both point at assessment facts; the invariant "Every result cites an attributable assessment basis" does not say whether a basis may exist with no result, or a result with no basis.
*Remediation:* define `assessmentBasisRefs` as the authoritative citation and `assessmentResultRefs` as a resolvable subset, with an invariant that every basis reference is attributable and time-stamped.
*Fixture:* `basis-vs-result` (positive) — "A result cites a basis that has no separately recorded assessment result. Normatively, the basis remains authoritative and the result is conformant."

### D. Owned concepts with no carrying field

**D15 — Career Path owns "applicability" with no field.**
`career-path.owns` includes "applicability"; `CareerPathVersion` has `nodes`, `transitions`, `validFrom`, `contentDigest`, `expectations`, `validTo` only.
*Remediation:* add `applicability` to `CareerPathVersion` (required or optional, stated), or remove it from `owns`.
*Fixture:* `applicability-recorded` (positive) — "A path version applies to one job family only. Normatively, the scope is recorded on the version and not inferred from nodes."

**D16 — Enrollment owns "capacity and waitlist state" and asserts "Capacity state is explicit" with no capacity field.**
Only `waitlistPosition` exists; capacity plausibly belongs to the Delivery, which Enrollment excludes.
*Remediation:* either add an explicit capacity-decision field on Enrollment (the seat state the registrar owns) or move capacity to the Delivery master and rewrite `owns` and the invariant accordingly.
*Fixture:* `capacity-explicit` (negative) — "A waitlist position is recorded with no explicit capacity or seat state at its named master. Normatively, the enrollment state is non-conformant."

**D17 — Succession Plan owns "bench-depth and coverage state" but `coverageState` is optional, contradicting fixture `empty-bench`.**
`empty-bench` expects "The coverage gap is explicit"; with `coverageState` optional and no bench-depth field, an uncovered critical position can remain silent.
*Remediation:* make coverage state required per critical position in each revision, add bench-depth as a recorded (not inferred) value, and align the invariant.
*Fixture:* `empty-bench-explicit` (negative) — "A revision scopes a critical position with no pool entries and no recorded coverage state. Normatively, the revision is non-conformant; absence of candidates must be recorded as an explicit gap."

**D18 — Succession Plan asserts time-bounded pools, pinned readiness and expiring, contestable ratings with no fields.**
`poolEntries` is unspecified; the revision has no `validFrom`/`validTo`; there is no expiry, no contest/dispute state, and `readinessRefs` sits at revision level with no binding to a pool entry, person or position — so the invariants "Pool membership is time-bounded", "Ratings expire and remain contestable" and "Every readiness reference pins the assessed position or path-step profile version" are unenforceable and readiness is unattributable.
*Remediation:* specify `poolEntries` as an object with person reference, position reference, `validFrom`/`validTo`, `readinessRef`, the pinned assessed profile version, `expiresAt` and a contest state; move `readinessRefs` under the pool entry.
*Fixture:* `readiness-attributable` (negative) — "A revision carries a readiness reference that resolves to no pool entry, assessed position or pinned profile version. Normatively, the reference is non-conformant."

**D19 — Enrollment owns "learner rights" — undefined, unfielded, and privacy-loaded.**
No field, no invariant, no definition; the phrase conflates consent, data-subject rights and participation entitlement inside a registrar-mastered record.
*Remediation:* delete it from `owns` and, if consent or data-subject rights are in contour, add them as an explicitly named concern with a master (see D24), not as an Enrollment property.
*Fixture:* `learner-rights-located` (negative) — "A data-subject right is asserted as an Enrollment property. Normatively, the assertion is non-conformant; rights are owned by the named privacy authority."

### E. History loss

**D20 — No attribution field on any object.**
"attributable" appears in `enrollment.versionIdentity`, `enrollment.invariants` ("Prerequisite evaluation is attributable"), `learning-result.versionIdentity` and two Learning Result invariants; no object carries an actor, steward or decision-maker field. Attribution is claimed and unrecordable.
*Remediation:* add a required attribution field (actor/authority reference plus recorded time) to every state-appending object: Enrollment successor states, `LearningResult` finalization and correction, `ProgramVersion` publication, `CareerPathVersion`, `SuccessionPlanRevision`.
*Fixture:* `attribution-required` (negative) — "A finalized result is corrected with no recorded actor. Normatively, the successor is non-conformant."

**D21 — No bitemporality on four of six objects.**
Only `Enrollment` and `LearningResult` require `recordedAt`. `LearningProgram`, `CareerPath`, `SuccessionPlan` carry a mutable `status` with no recorded time; `ProgramVersion`, `CareerPathVersion` and `SuccessionPlanRevision` have valid time (or `reviewAt`) but no recorded time. Prior lifecycle states are therefore unrecoverable, and "Supersession preserves historical results/plans" is unverifiable.
*Remediation:* require `recordedAt` on every object and make root `status` an appended, time-stamped state rather than an overwritten scalar.
*Fixture:* `status-history` (negative) — "A program moves from approved to deprecated and the prior status is no longer resolvable. Normatively, the transition is non-conformant."

**D22 — Successor linkage is inconsistent, one-directional and uncollected.**
`LearningProgram.successorRef` and `CareerPath.successorRef` (forward), `Enrollment.supersedesRef` (backward), `SuccessionPlanRevision.supersedesRevision` (backward), `LearningResult.predecessorRef` (backward) — four namings, two directions, all optional, none a collection, while three candidates claim to own "successor history" or "revision history".
*Remediation:* adopt one naming and one direction across all five roots, require it on every non-initial state, and state that chain traversal must reconstruct the full history without gaps.
*Fixture:* `chain-closure` (positive) — "A program reaches its third version. Normatively, every earlier version remains reachable through an unbroken successor chain."

**D23 — Enrollment transfer does not say what happens to the pinned Program Version.**
`versionIdentity` admits transfer and `cancelled-delivery` expects "Enrollment survives and records transfer", but "Enrollment pins one program version" plus a required `programVersionRef` leaves it undefined whether transfer may repin. If it may, the version a learner was admitted under is lost; if it may not, cross-version transfer is silently impossible and D12 has no legal path.
*Remediation:* state explicitly that transfer appends a successor state pinning the new Program Version while the predecessor state retains the original pin, and that Learning Results resolve against the state in force at assessment time.
*Fixture:* `transfer-repins` (positive) — "A learner transfers to a delivery of a later Program Version. Normatively, a successor state pins the new version and the original admitted-under version remains resolvable."

**D24 — `deliveryRef` is listed twice in `Enrollment.optional`.**
A literal duplicate in the field list.
*Remediation:* delete the duplicate; state whether `deliveryRef` is single-valued (current allocation) or historical, given that transfer history is owned.
*Fixture:* `delivery-allocation-history` (positive) — "A learner is allocated to two deliveries in sequence. Normatively, both allocations remain resolvable and exactly one is current."

**D25 — `voided` has no reason, actor, time, or retention rule; `retained`/`disposed` have no tombstone rule.**
`LearningResult.lifecycle` includes `voided`, `retained`, `disposed`; `dispositionState` is optional; the only guard is "Disposition never cascades to Person, award or credential masters". Nothing prevents a void or disposal from erasing the fact that a result existed, and nothing governs a downstream award or credential that references a disposed result.
*Remediation:* require void reason, actor and recorded time; require that voided and disposed results leave a non-personal tombstone preserving identity, pins and state transitions; add an invariant that no downstream award or credential reference may be left dangling by disposition.
*Fixture:* `void-tombstone` (negative) — "A voided result becomes unresolvable. Normatively, the void is non-conformant; identity, pins and transitions must remain resolvable after void or disposal."

**D26 — No rule determines the effective outcome among appended results.**
`retake-appends` produces a second result for the same person and objective version while the earlier not-achieved result remains; `validFrom`/`validTo` are optional and `predecessorRef` is optional. Nothing states which result is current, so a downstream award, credential, readiness or path gate may read a stale or contradictory outcome.
*Remediation:* add a deterministic effective-outcome rule over (person, objectiveVersion) by valid time and status, require valid time on finalized results (see D27), and state that the rule yields at most one effective outcome at any instant.
*Fixture:* `effective-outcome` (positive) — "A not-achieved result is followed by an achieved retake. Normatively, exactly one effective outcome resolves at any instant and both results remain resolvable."

**D27 — `validFrom`/`validTo` optional though "valid and recorded time" is owned.**
Achievement effective date is therefore unrecordable and indistinguishable from `finalizedAt`, which is a recording event, not an achievement date.
*Remediation:* require `validFrom` on any finalized result and state the semantic difference between achievement valid time and finalization recorded time.
*Fixture:* `valid-vs-recorded` (negative) — "An achievement date is read from `finalizedAt`. Normatively, the inference is non-conformant."

### F. Privacy

**D28 — Minimum disclosure is asserted for one root only; the most sensitive root has none.**
"Sensitive data uses minimum disclosure" appears solely in `succession-plan.invariants`. `LearningResult` holds not-achieved and indeterminate outcomes plus `evidenceRefs`, with no confidentiality, purpose-limitation, disclosure-scope or lawful-basis invariant and only an optional `retentionPolicyRef`. `Enrollment` (prerequisite decisions, withdrawal reasons) and `CareerPath`/aspiration data have none either. No fixture in the entire dossier tests disclosure.
*Remediation:* add minimum-disclosure, purpose-limitation and disclosure-scope invariants to all five roots; make `retentionPolicyRef` required on finalized results; state that `evidenceRefs` are minimized and retention-bound; add at least one disclosure fixture per root.
*Fixture:* `minimum-disclosure` (negative) — "A not-achieved result or readiness rating is disclosed to a recipient outside its recorded disclosure scope. Normatively, the disclosure is non-conformant."

**D29 — "Missing … remains unknown" is stated three times with no representation.**
`learning-program` ("Missing outcome evidence remains unknown"), `enrollment` ("Missing attendance remains unknown"), `career-path` ("Missing transition evidence remains unknown") have no unknown-marker field; combined with optional references, absence and unknown are indistinguishable — and `indeterminate` exists only on Learning Result.
*Remediation:* define how unknown is represented distinctly from absent for each named case, or downgrade the three invariants to holds.
*Fixture:* `unknown-not-absent` (negative) — "An absent attendance reference is read as attendance not having occurred. Normatively, the inference is non-conformant."

### G. Lifecycle and outcome integrity

**D30 — `finalizedAt` is required while `provisional` is a lifecycle state.**
`LearningResult.required` includes `finalizedAt`; `lifecycle` and `independentLifecycle` both begin at `provisional`. A provisional result cannot satisfy the schema; either the state is unreachable or the requirement is false.
*Remediation:* make `finalizedAt` conditionally required — required exactly when status is `finalized` or later, forbidden when `provisional` — and state it as an invariant.
*Fixture:* `provisional-no-finalization` (negative) — "A provisional result carries a finalization time. Normatively, the result is non-conformant."

**D31 — `indeterminate` is absent from identity and boundary.**
`outcomes` lists `achieved`, `not-achieved`, `indeterminate`, and the invariant and fixture `indeterminate-not-fail` protect it, but `stableIdentity` says "achieved or not-achieved result" and `boundary.owns` says "achieved or not-achieved outcome". The third value is unowned by the root that asserts it.
*Remediation:* rewrite `stableIdentity` and `boundary.owns` to cover all three outcome values.
*Fixture:* `indeterminate-owned` (positive) — "A result is indeterminate. Normatively, it is a conformant owned outcome, neither achieved nor not-achieved."

**D32 — One `independentLifecycle` per candidate spans two objects.**
`learning-program` and `career-path` mix root states (`draft`…`retired`) with version states (`superseded`); `succession-plan` mixes revision states (`revised`, `superseded`) with plan states (`closed`, `archived`); `learning-result` mixes result states with retention states (`retained`, `disposed`). Root `status` therefore cannot be typed, and version/revision state has no enumeration at all.
*Remediation:* split each `independentLifecycle` into a root lifecycle and a version/revision lifecycle (and, for Learning Result, a separate retention lifecycle), and bind each object's `status` to exactly one enumeration.
*Fixture:* `lifecycle-allocation` (negative) — "A root `status` is set to a version-level state. Normatively, the state is non-conformant."

**D33 — Required `enrollmentRef` silently forecloses recognition of prior learning and challenge assessment.**
Every Learning Result must cite an Enrollment. Externally achieved or challenge-assessed objectives are thereby impossible, with no exclusion recorded anywhere.
*Remediation:* decide explicitly — either add "recognition of prior learning" to `learning-result.excludes` with a hold, or relax `enrollmentRef` to conditionally required with a recorded non-enrollment basis.
*Fixture:* `prior-learning-scope` (negative) — "An objective achieved outside any enrollment is recorded as a Learning Result. Normatively, the record is non-conformant under the declared scope."

**D34 — Retake is modelled two ways.**
`versionIdentity` says a retake "creates a new result or explicit successor"; the invariant says a retake "appends a result and never overwrites"; the fixture `retake-appends` expects "a successor result is appended". With `predecessorRef` optional, the retake chain may be lost entirely.
*Remediation:* choose one model — retake appends an independent result linked by a required predecessor reference, correction appends a successor — and make the three statements identical.
*Fixture:* `retake-linked` (negative) — "A retake result is recorded with no link to the prior result for the same person and objective version. Normatively, the result is non-conformant."

**D35 — Nothing prohibits automatic award or credential creation from an achieved result.**
Invariants establish that a result is not an award or credential and that downstream award and credential are optional, but no invariant or fixture forbids an achieved result from auto-issuing either. The profile constrains only the unsuccessful direction ("unsuccessful results never enter WM-PER-008 award identity").
*Remediation:* add the symmetric invariant — an achieved result authorizes but never creates an award or credential, which requires a separate governed decision — and add the missing fixture.
*Fixture:* `achieved-no-auto-award` (negative) — "An achieved result issues a qualification award with no separate award decision. Normatively, the issuance is non-conformant."

### H. Overclaim of validation and publication

**D36 — Fixture register implies execution.**
`sourceFacts.runtime` states fixtures are "declarative, not executable tests", yet the positive and negative fixtures of four roots are written as outcomes ("The inference is rejected", "It remains independently valid", "The cascade is rejected"), while `semantic` fixtures and all Learning Result fixtures are correctly hedged with "Normatively,". The unhedged register reads as verified behaviour.
*Remediation:* prefix every `expect` with the normative qualifier, or add a per-fixture `executable: false` field; do not leave two registers in one dossier.
*Fixture:* `fixture-register` (negative) — "A fixture expectation is stated as an observed runtime outcome. Normatively, the statement is non-conformant while `sourceFacts.runtime` holds."

**D37 — Immutability is claimed without a verifiable mechanism.**
"Published versions are immutable" and "Revisions are immutable" rest on `contentDigest` with no algorithm, no canonicalization, no coverage statement (which fields are digested), and no executable check.
*Remediation:* specify the digest algorithm, the canonical serialization and the exact field coverage, and state that immutability is asserted and unverified until live verification closes.
*Fixture:* `digest-coverage` (negative) — "A published version changes a digest-excluded field. Normatively, the change is non-conformant; the digest must cover every field bearing on published semantics."

**D38 — "Published" is overloaded.**
`published` is a curriculum and path lifecycle state; `canonicalPublishable: false` and the hold on package conversion concern model publication; the fixture `credential` speaks of "Program publication". One token, three meanings, in a dossier whose whole purpose is preventing identity collapse.
*Remediation:* rename the lifecycle state (e.g. `released`) or qualify each use, and add a glossary line separating curriculum release from canonical model publication.
*Fixture:* `publication-sense` (negative) — "A released curriculum version is read as a canonically published model. Normatively, the inference is non-conformant."

**D39 — Learning Result carries a weaker hold set than the other four roots.**
Its `holds` omit "Base specifications and approved relations remain incomplete." and "Package conversion and live verification are pending." — both present in all four other candidates — even though it is the newest root and depends on the least-settled relations.
*Remediation:* normalize the hold set across all five candidates; the newest root must carry at least the holds of the others.
*Fixture:* `hold-parity` (negative) — "A candidate omits a hold carried by its sibling candidates in the same contour. Normatively, the candidate is non-conformant."

**D40 — The profile does not bind the five roots it governs.**
`profile.bases` lists six bases; nine of fourteen `constraints` govern Learning Program, Enrollment, Learning Result, Career Path and Succession Plan, none of which is named as a governed candidate anywhere in the profile object, and `newRuntimeId: false` sits beside five `NEW MODEL` decisions.
*Remediation:* add a `candidateRoots` list naming the five identifier-unassigned roots, scope `newRuntimeId: false` explicitly to the profile itself, and add a hold that the profile cannot be published before the five roots are allocated.
*Fixture:* `profile-root-binding` (negative) — "A profile constrains a root it does not name as a governed candidate. Normatively, the profile is non-conformant."

**D41 — Narrowings are asserted over draft bases.**
`profile.constraints` states "WM-ACT-038 is narrowed to scheduled Delivery or cohort" and profiles `WM-ACT-008`, `WM-ACT-034`, `WM-REC-010`, `WM-ORG-016` as settled, while `sourceFacts.bases` says "Supplied bases remain held reviewable drafts" and every relation contract is provisional. A narrowing of a draft cannot be authoritative.
*Remediation:* mark every narrowing as conditional on base approval, or add a hold that all narrowings lapse if a base changes.
*Fixture:* `conditional-narrowing` (negative) — "A narrowing of a draft base is relied on as settled semantics. Normatively, the reliance is non-conformant."

---

## 4. Contradictions

1. **`finalizedAt` required vs `provisional` state** — `learning-result.objects.LearningResult.required` against `lifecycle[0]`. The schema and the lifecycle cannot both hold (D30).
2. **`indeterminate` outcome vs "achieved or not-achieved" identity and ownership** — `outcomes` and the `indeterminate-not-fail` fixture against `stableIdentity` and `boundary.owns` (D31).
3. **`coverageState` optional vs fixture `empty-bench`** — a fixture demands explicit coverage that the schema permits to be absent (D17).
4. **"Capacity state is explicit" vs no capacity field, and capacity excluded to Delivery** (D16).
5. **"Pool membership is time-bounded" / "Ratings expire and remain contestable" / readiness pinning vs an unspecified `poolEntries` with no time, expiry, contest or pin fields** (D18).
6. **"Sensitive data uses minimum disclosure" asserted as an operative invariant, and Learning Result owning "retention and disposition state", vs the profile and candidate hold "Privacy, retention, source pins and executable conformance remain pending"** — an operative privacy capability asserted under a privacy hold (D28).
7. **Retake as successor (fixture, `versionIdentity`) vs retake as independent appended result (invariant), with `predecessorRef` optional** (D34).
8. **"Enrollment pins one program version" plus required `programVersionRef` vs transfer history ownership and the `cancelled-delivery` fixture** — repinning is neither permitted nor forbidden (D23).
9. **Declarative-only fixtures (`sourceFacts.runtime`) vs sixteen unhedged fixture expectations written as observed outcomes** (D36).
10. **Profile narrowing `WM-ACT-038` and profiling four further bases as settled vs `sourceFacts.bases` holding all bases as reviewable drafts and all contracts provisional** (D41).
11. **`profile.newRuntimeId: false` vs five `NEW MODEL` unassigned roots the profile constrains but never names** (D40).
12. **`career-path` fixture `branching` — "Both governed transitions remain available" — vs the invariants "Transitions are typical possibilities, not promises" and "advisory unless a separately governed gate is explicitly attached"**: the fixture calls transitions governed where the model makes governance an exception.
13. **Learning Result's hold set vs its siblings' hold sets in the same contour revision** (D39).
14. **`learning-result.excludes` "attendance or delivery completion" and "assessment administration" vs `Enrollment.optional` carrying `attendanceRefs`, `completionRef` and `resultRefs`** — exclusion at one root and unqualified reference-holding at another, with no non-authoritative-back-reference rule, is the classic path to reading achievement off an Enrollment (D1).
15. **"attributable" in four invariants vs no attribution field in any of the six objects** (D20).

---

## 5. Closed numbered checklist

Each item is closed: it is satisfied or not, with no open-ended judgement.

1. Remove the duplicate `deliveryRef` from `Enrollment.optional`. — D24
2. Make `finalizedAt` conditionally required on status, forbidden when `provisional`. — D30
3. Extend `learning-result.stableIdentity` and `boundary.owns` to cover `indeterminate`. — D31
4. Define an addressable objective-version identity and resolve `objectives` vs `objectiveVersions`. — D11
5. Add the two pin-consistency invariants (result↔enrollment Program Version; objective version scoped to Program Version). — D12
6. Declare one authoritative assessment-criteria pin among `assessmentDesignVersion`, `assessmentPolicy`, `WM-KNW-013`. — D13
7. Define `assessmentBasisRefs` as authoritative and `assessmentResultRefs` as a resolvable subset. — D14
8. Name the master for attendance and for delivery completion; retype `attendanceRefs`, `completionRef`, `resultRefs` as non-authoritative back-references. — D1, C14
9. Name the master for assessment administration and raw score. — D2
10. Contract or exclude competency assertion. — D3
11. Contract or remove the credential relation (`WM-XCT-017`). — D4
12. Locate aspiration under a named master with a recorded-time field. — D5
13. Name the access/entitlement authority or record the hold that access denials are unenforceable here. — D6
14. Add pool-entry-level nomination and appointment references. — D7
15. Add all six uncontracted targets to `bases` and `relationContracts`, or remove their references. — D8
16. Record contract state for every root-to-root relation inside the contour. — D9
17. Add the person reference to `succession-plan`. — D10
18. Add `applicability` to `CareerPathVersion` or remove it from `owns`. — D15
19. Resolve capacity ownership and add the field or move it to the Delivery master. — D16
20. Make per-position coverage state required and add bench depth. — D17
21. Specify `poolEntries` with person, position, valid time, readiness reference, pinned profile version, expiry and contest state. — D18
22. Delete "learner rights" from `enrollment.owns`. — D19
23. Add a required attribution field to every state-appending object. — D20
24. Require `recordedAt` on all six objects and make root `status` an appended time-stamped state. — D21
25. Unify successor naming and direction across all five roots and require unbroken chains. — D22
26. State transfer repinning semantics and predecessor-state pin retention. — D23
27. Require void reason, actor and time; require post-void and post-disposal tombstones; forbid dangling downstream references. — D25
28. Add the deterministic effective-outcome rule over (person, objectiveVersion). — D26
29. Require `validFrom` on finalized results and distinguish achievement valid time from finalization recorded time. — D27
30. Add minimum-disclosure, purpose-limitation and disclosure-scope invariants to all five roots; make `retentionPolicyRef` required on finalized results; bind `evidenceRefs` to minimization. — D28
31. Define unknown-versus-absent representation for the three "remains unknown" invariants, or downgrade them to holds. — D29
32. Split every `independentLifecycle` into root, version/revision and retention enumerations, and bind each `status` to one. — D32
33. Decide recognition of prior learning: exclude it with a hold, or relax `enrollmentRef`. — D33
34. Unify the three retake statements and require the retake link. — D34
35. Add the achieved-result-authorizes-but-never-creates-award-or-credential invariant. — D35
36. Normalize fixture register to declarative across all forty fixtures. — D36
37. Specify digest algorithm, canonicalization and field coverage; state immutability as asserted and unverified. — D37
38. Disambiguate "published" between curriculum release and canonical publication. — D38
39. Normalize the hold set across all five candidates. — D39
40. Add `candidateRoots`, scope `newRuntimeId: false` to the profile, and add the pre-allocation publication hold. — D40
41. Mark every base narrowing as conditional on base approval. — D41
42. Correct the `branching` fixture wording to match the advisory default. — C12
43. Add the twenty-nine fixture expectations specified in §3, one per defect, all declarative. — §3
44. Re-issue as `candidateRevision: 3` with `allocationState: unassigned`, `modelId: null`, `registryId: null`, `canonicalPublishable: false` on all five roots; the frozen-audit hold closes only against that revision, and this audit closes no other hold. — §2
