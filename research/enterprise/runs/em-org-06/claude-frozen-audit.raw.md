# FROZEN SEMANTIC AUDIT — EM-ORG-06 "Позиции, роли и ответственность"
**Auditor:** single independent frozen auditor. **Material:** frozen dossier, Claude study, Grok study, provider comparison, candidate revision 2, fixtures revision 2. No external facts, no tools, no invented identifiers.

---

## 1. VERDICT

**REVISE.**

The boundary decision is correct and should survive revision unchanged. The candidate fails on execution, not on direction: it carries an invented version identifier, one out-of-dossier identifier used normatively, an incomplete required-dependency set that omits six dependencies the pinned bases themselves declare `required: true`, a RACI cardinality rule whose evaluation scope is undecidable, and at least four unclosed segregation-of-duties bypass paths. Fifty-two defects are recorded below; **14 are blockers**. None of them argues for a different decision — all are discharged by tightening the same candidate.

---

## 2. BASE DECISION

| Item | Ruling |
|---|---|
| REUSE of **WM-ORG-004** as durable, vacant-capable Position master | **CONFIRMED** |
| PROFILE of **WM-XCT-023** for Accountability, held DecisionRight, RaciAssignment | **CONFIRMED** |
| No new model or runtime identifier | **CONFIRMED with two breaches** (D-46, D-47) |

**Grounds for confirmation.** The decidable test is stated identically in both specs and both studies: the record must be able to exist while vacant. WM-ORG-004 `scope_statement` ("In scope is everything that is true of a position while it is vacant") and its boundaryDecision rationale settle the seat; WM-XCT-023's reified n-ary assertion (`role-assertion`, `player-ref` 0..1, `host-context-ref` 1, validity) settles the assertion plane and admits a vacant post as player without a person. Every contour candidate type has a home in one of the two: `Position` → WM-ORG-004; `Accountability` → `prescribed-regulatory-responsibilities` (seat) plus `basis-of-authority`/`mandate-ref` (held); `DecisionRight` → `de-decision-right` (seat) plus `representation-and-limits` (held); `RaciAssignment` → `role-type-and-axes` + `host-kind` + `role-validity-period` + `segregation-and-conflict`. Nothing in the contour requires an entity root that neither base owns.

**Identifier discipline.** `newRuntimeId: false` holds; every `profileTypes.*.registryId` and `.runtimeId` is null; `BusinessRole` and `HeadcountPlan` are correctly left unallocated. Two breaches: an **invented version identifier** (`modelVersion: "0.3.0-research.1"`, unsupported by any field in the frozen dossier — D-46) and an **imported identifier used normatively** (`WM-ECO-012` in a MUST constraint and a fixture, contrary to the provider comparison's own rule — D-47). Neither invents a Vercy model id; both must be removed before ACCEPT.

---

## 3. DEFECTS

Severity: **B** blocker · **M** major · **m** minor. Each entry gives exact remediation (**R**) and the fixture expectation (**F**).

### A. Position / person / occupancy collapse

**D-01 (B) — Legacy alias binds the Position master to a unit spec and an employment/membership spec.**
`basePins.legacyAlias: "O2;O3"`, `legacySpecRef: "…O2-organizational-unit.md;…O3-employment-and-membership.md"`. The registry row for `vr.wm-org-004` also carries `owner_or_maintainer: "parent organization; both parties (bilateral record)"` — bilateral-record language belongs to membership, not to a seat. The candidate declares WM-ORG-004 "the sole master of durable Position identity" while its reservation of record still points at both the unit plane (WM-ORG-002) and the occupancy/employment plane (WM-ORG-016). No constraint, no hold, no fixture addresses this.
**R:** Add constraint: *"Reuse is against the pinned `spec.yaml` only. No attribute sourced from legacy O2 (organizational unit) or O3 (employment and membership) may be materialized on Position; the registry `legacy_alias` and `existing_spec_ref` are superseded-by-scope for this contour and MUST be re-cut before canonical reuse."* Add `legacyScopeStatus: "excluded-not-reconciled"` to the WM-ORG-004 pin and a matching publication hold.
**F:** negative `legacy-o3-membership-on-position` — a Position record carries employment or membership attributes traced to O3 → **refuse**; membership facts resolve only through WM-ORG-016 and are absent from the Position record. negative `legacy-o2-unit-attributes-on-position` — unit charter or unit hierarchy attributes materialized on Position → **refuse**.

**D-02 (B) — Erasure of a player is unhandled on the assertion plane.**
Constraints protect the Position from occupant erasure, but say nothing about what erasure does to PartyRole/RACI assertions. WM-XCT-023 owns `retention-and-erasure`, tombstones and `apply-retention-decision`, and its own layer description names the conflict ("how erasure is reconciled with accountability chains that depend on it"). Unconstrained, an erasure either deletes past Accountable assertions (history rewrite) or silently changes a closed interval's A/R count.
**R:** Constraint: *"Erasure or tombstoning of a player's identifying data MUST preserve the assertion node, its host, role concept, validity interval, status history and provenance; it MUST NOT delete the assertion and MUST NOT alter the cardinality evaluation of any closed interval. The player reference is replaced by a tombstone reference, never removed."*
**F:** negative `player-erasure-deletes-assertion` — erasing a person removes their past Accountable assertions → **refuse**. positive `player-erasure-tombstone` — PII erased, assertion retained with tombstone reference; A/R counts over all closed intervals **unchanged**.

**D-03 (M) — "person" / "human bearer" wording collapses agent to natural person.**
Two constraints read *"One person MAY hold multiple concurrent PartyRole assertions"* and *"…while the current human bearer remains resolved through occupancy."* WM-XCT-023 `player-kind` admits organizations, groups and automated agents; WM-ORG-004 `deferredResearch` records *"Occupancy of a position by a non-human agent, unresolved in both packs even though org:holds is defined over agents rather than persons."* The candidate resolves by wording what both bases leave open.
**R:** Replace "person"/"human bearer" with "party or agent" throughout. Add constraint: *"Occupancy of a Position by, and profile-role play by, a non-human agent is UNRESOLVED in both bases and MUST be refused by default in this profile until allocated."*
**F:** negative `non-human-agent-as-accountable` — automated agent asserted as occupant or as an Accountable player → **refuse** with the unresolved-by-default reason code.

**D-04 (M) — v1 predecessor lineage dropped.**
`candidate_properties_from_v1` (ORG-07: `position_code`, `job_family`, `grade`, `authorized_fte`; PEO-05: `role_name`, `accountabilities`, `decision_rights`, `scope`) is mapped in the Claude study but absent from the candidate entirely. Migration risk: these get re-minted as profile-local fields alongside `de-position-code`, `de-job-ref`, `de-grade-ref`, `de-fte`.
**R:** Add a `v1FieldMapping` block mapping all eight fields to a base element id or to `unmapped-deferred`, carrying the dossier's `candidate-not-normative` status verbatim.
**F:** negative `v1-field-reminted` — profile declares its own `position_code` or `authorized_fte` field → **refuse**; must reference the base element.

**D-05 (M) — Source mastership left undecided although it is an explicit dossier blocking decision.**
`blocking_decisions[2]` requires *"Подтвердить semantic crosswalk, права и source mastership."* The candidate records model-level mastership only. There is no system-level statement (HRIS vs corporate registry vs vocabulary owner), no rights statement, and no record that `vercy_candidates.evidence_depth` is only `index-and-publication-metadata` — i.e. the full semantic crosswalk both `note` fields demand is unverified.
**R:** Add a `mastership` block: seat and occupancy → HRIS / position-control system; statutory officer assertions → corporate registry; role-type scheme → vocabulary owner (unallocated); no system in this contour masters the person. Add publication hold: *"Semantic crosswalk verified only at index-and-publication-metadata depth; the reuse and profile decisions are boundary-level and do not assert element-level crosswalk."*
**F:** negative `vocabulary-mastered-by-hris` — HRIS asserted as master of the role-type scheme → **refuse**.

### B. Vacancy ambiguity

**D-06 (B) — Vacancy derivation ignores lifecycle status.**
`vacancySemantics.seatVacancy` is the single string `"derived capacity state"`. WM-ORG-004 requires two independent status elements (`de-hiring-status` 1/required: proposed, approved, frozen; `de-active-status` 1/required) and `de-abolition-date`. As written, an abolished, inactive or frozen seat with no occupancy derives as vacant — and therefore as fillable.
**R:** Redefine vacancy as a function of `(authorized capacity, effective occupancy set, hiring status, active status, abolition date, as-of instant)`. Unoccupied capacity on a seat that is not `active` + `approved` is `unoccupied-not-fillable`, never `vacant`.
**F:** negative `abolished-seat-derived-vacant` — abolished seat, zero occupancy → **refuse** the `vacant` derivation; derive `unoccupied-not-fillable`. negative `frozen-seat-derived-fillable`. Amend `vacant-position` to pin `hiring-status=approved`, `active-status=active`.

**D-07 (B) — The vacancy state set is not enumerated.**
Grok's four states (vacant / partly filled / fully filled / over-established) are named in the provider material and in WM-ORG-004's `vacancy-and-occupancy-state` finding, but the candidate carries none of them. Partial occupancy of a **single** seat (0.5 FTE consumed against authorized 1.0) has no defined state and no fixture.
**R:** Enumerate a closed state set with one derivation rule per state, plus the FTE comparison precision/rounding rule and the mandatory as-of instant.
**F:** positive `single-seat-partial-occupancy` — 0.5 FTE against a 1.0 single seat → derive **partly-filled**; not vacant, not fully-filled.

**D-08 (M) — "MUST NOT be stored" contradicts the base's own elements.**
The constraint forbids vacancy "stored as an independent seat fact", but WM-ORG-004 defines `de-open-capacity` and `de-vacancy-since` as elements **on the seat**. The base's adjudication decision is narrower and correct: no *second source of truth*.
**R:** Restate: *"Derived state MAY be materialized on the seat only as a recomputable projection stamped with the as-of instant, the occupancy-set version and the derivation-rule identifier. It MUST NOT be independently mutable and MUST be invalidated and recomputed on any occupancy change."*
**F:** amend `stored-vacancy-flag` — **refuse** an independently mutable flag; **accept** a stamped projection that recomputes identically. Add negative `stale-vacancy-projection` — projection stamp predates the latest occupancy change → **refuse** as authoritative; recompute.

**D-09 (M) — The derivation rule depends on a model with no reservation.**
WM-ORG-016 appears in the ledger and in WM-ORG-004's composition (`required: true`) but has **no registry reservation** in the dossier and `pinned: false`. Three constraints and nine fixtures are evaluated against it. Those fixtures are not merely unexecuted — they are currently **unexecutable in principle**.
**R:** Tag each dependent case `dependsOn: ["WM-ORG-016"]` and `executionStatus: "blocked-unexecutable"`, and say so in `publicationHolds` rather than only noting the pin is missing.
**F:** apply the tag to `vacant-position`, `successor-occupant`, `delete-employee-cascade`, `stored-vacancy-flag`, `position-as-player`, `pooled-two-half-fte`, `single-two-half-fte`, `pooled-over-capacity`, `occupancy-end-rewrites-capacity`.

**D-10 (m) — The recruitment artifact has no named owner.**
The constraint requires distinctness from "any recruitment Vacancy or PositionOpening artifact" but names no owning contour or model, so nothing prevents this contour from silently re-owning it.
**R:** Record the recruitment artifact as an external unallocated dependency (owner not identified in the frozen dossier).
**F:** extend `recruitment-vacancy-collapse` — the refusal must also **refuse** creation of the recruitment artifact inside this profile, not merely refuse equating it with seat vacancy.

### C. Capacity errors

**D-11 (B) — Single-vs-pooled is defaulted where the base forbids defaulting.**
`de-position-type` is `0..1`, **not required**, and its own description warns: *"W3C also permits a post to be held by more than one person, so single occupancy must never be assumed."* `capacityRule.single` assumes exactly that whenever the element is absent.
**R:** Constraint: *"Where `de-position-type` is absent the capacity mode is `undetermined`. Admission of any second concurrent holder MUST be refused and the seat MUST be flagged for classification. The profile MUST NOT default to single or to pooled."*
**F:** negative `position-type-absent-second-holder` → **refuse**. positive `position-type-absent-single-holder` → **accept** with `capacity-mode: undetermined` flag raised.

**D-12 (M) — FTE/headcount consistency rule not restated; headcount breach not isolated.**
`de-headcount` description: *"greater than one only for pooled positions."* The candidate never restates this, and no negative fixture isolates a headcount breach while FTE is within authorization.
**R:** Constraints: (i) `headcount > 1` MUST imply pooled; (ii) FTE and headcount are **independent** ceilings — breach of either yields over-established.
**F:** negative `single-seat-headcount-two` → **refuse**. negative `pooled-headcount-breach-fte-within` — two 0.5 FTE occupancies against pooled authorized FTE 1.0 / headcount 1 → **refuse on headcount** despite FTE compliance.

**D-13 (M) — The override path has no authority, no bound and no positive case.**
`capacityRule.override: "explicit recorded outcome only"`; `de-overlap-outcome` records *"whether exceeding capacity produced a warning or a hard block, and who overrode it."* Nothing constrains who may override, whether an override may be open-ended, or whether warn-mode may be used to satisfy a profile refusal.
**R:** Constraint: *"An override MUST record overriding authority, reason, effective interval and the resulting over-established state; overrides MUST NOT be open-ended; a warn-mode outcome MUST NOT satisfy a profile refusal."*
**F:** positive `pooled-over-capacity-with-recorded-override` → **accept** for the recorded interval only. negative `override-without-authority` → **refuse**. negative `warn-outcome-used-as-acceptance` → **refuse**.

**D-14 (M) — Job-share is asserted as capability although both bases declare it evidence-free.**
WM-ORG-004 `deferredResearch`: *"Dual-incumbency overlap windows … job-share fractions and union exclusivity of a slot, all widely practised but without primary support in either run."* The Claude study concedes *"the third acceptance case is a declared local profile, not an evidenced capability."* The candidate's `capacityRule` and the positive fixture `pooled-two-half-fte` present it as supported behaviour with no evidence marker.
**R:** Mark the pooled/job-share rule `evidenceStatus: "declared-local-no-primary-source"` in `capacityRule`, in the fixture, and in `publicationHolds`.
**F:** amend `pooled-two-half-fte` — pin `position-type=pooled`, `headcount=2`, `authorized FTE=1.0`, `overlap=allowed`; make the expectation unconditional; carry the `declared-local` marker.

**D-15 (M) — Occupancy end is only negatively fixtured.**
`occupancy-end-rewrites-capacity` tests the wrong behaviour. There is no positive case asserting the right one.
**R + F:** positive `occupancy-end-releases-capacity` — ending one occupancy releases exactly its consumed FTE and headcount; `de-fte`, `de-headcount`, budget amount, funding source, Position identity and all unrelated role assertions **unchanged**; vacancy state re-derived as-of.

### D. Role-concept / assertion collapse

**D-16 (B) — The profile has no conformance marker, so the RACI rule's scope is undecidable.**
Nothing in the candidate states how a consumer recognizes that an assertion belongs to this profile. The exactly-one-Accountable rule therefore has no defined evaluation set: a generic WM-XCT-023 assertion carrying an "accountable" role-type code may be swept into the count, and a genuine profile assertion may be missed. Fixture `raci-rule-on-generic-role` guards one direction of leakage only, and does so without any marker to guard with.
**R:** Define a profile identifier; require every profile assertion to carry `profileRef` = contour profile id + `candidateRevision` + both base pins. Evaluate the cardinality rule **only** over assertions bearing it.
**F:** negative `raci-count-includes-unmarked-assertion` → **refuse**. negative `profile-marker-absent-but-rule-applied` → **refuse**. Amend `raci-rule-on-generic-role` to reference `profileRef` explicitly.

**D-17 (B) — Classification axis not pinned.**
`role-classification-axis` is `cardinality 1, required` in the mixin, and `role-type-and-axes` warns that collapsing axes *"produces vocabularies that cannot be validated."* The Claude study pins the profile to functional-or-statutory. The candidate's 27 constraints never mention the axis.
**R:** Constraint: *"Profile assertions MUST pin `role-classification-axis` ∈ {functional, statutory}; structural and contractual axes MUST be refused in the A and R slots."*
**F:** negative `raci-on-structural-axis` → **refuse**. positive `raci-functional-axis` → **accept**.

**D-18 (B) — Host kind unrestricted.**
The RACI constraint requires "host and host revision" but never constrains `host-kind`, which admits object, activity, agreement, organization **or another party**. An Accountable assertion whose host is a party turns accountability into a person-to-person relation and makes "exactly one A per host" meaningless.
**R:** Restrict the Accountability/RACI profile to a closed declared `host-kind` set (decision, deliverable, process, control); the set is declared at profile level, not per instance.
**F:** negative `raci-host-is-party` → **refuse**. negative `raci-host-is-organization` → **refuse**.

**D-19 (B) — Host reference mode unpinned.**
`host-ref-mode` is `required` and selects float-to-current vs pin-to-version. The constraint asks for a pinned "host revision" but nothing refuses `float`, and nothing states whether cardinality is evaluated per host **version** or per host **lineage**. Two A assertions against two versions of the same logical host are currently both legal and both illegal.
**R:** Profile MUST set `host-ref-mode = pinned` and MUST declare one evaluation basis — per version **or** per lineage — never both.
**F:** negative `raci-float-host-ref` → **refuse**. negative `two-accountable-different-host-versions` → outcome determined by the declared basis, stated in the expectation, not left open.

**D-20 (M) — Multi-typed assertions unaddressed.**
`role-type-code` is `1..n`. One assertion carrying both an A and an R code defeats counting and conceals both the A-without-R failure mode and the A-equals-R case.
**R:** Profile MUST restrict `role-type-code` to exactly one per RACI assertion.
**F:** negative `raci-assertion-multi-typed` → **refuse**.

**D-21 (M) — Binding strength unpinned.**
`role-type-binding-strength` is `required`; a permissive binding admits local unmapped terms into the A and R slots, which `business-role-embedded` does not catch (it tests scheme/version presence, not binding strictness).
**R:** Profile MUST pin the strictest available binding strength and refuse unmapped local terms in the A and R slots.
**F:** negative `raci-local-unmapped-role-term` → **refuse**.

**D-22 (M) — BusinessRole is not mapped to the base dependency slot it fills.**
WM-XCT-023 declares `REFERENCE` to *"Role type vocabulary / concept scheme model"* with `required: true`; WM-ORG-004 carries `abstract-role-binding` with a reference plus a fallback label. Claude says BusinessRole completes that slot; Grok says do not fold it into the mixin. The candidate takes neither position, so a base-declared **required** dependency sits unmapped.
**R:** Record BusinessRole as the unallocated filler of both slots — WM-XCT-023's required vocabulary REFERENCE and WM-ORG-004's `abstract-role-binding` reference — while keeping the identifier unassigned, and state explicitly that it is not part of the mixin.
**F:** negative `business-role-folded-into-mixin` — role terms defined inside a PartyRole assertion instead of referenced from the scheme → **refuse** (companion to `business-role-embedded`).

**D-23 (M) — Standing-vs-participation discriminator is constrained but not fixtured.**
`assignment-mode` is `required` in the mixin and named once in the constraints, but no fixture forbids an activity-instance participation from being counted as a standing RACI assertion — the exact collapse `participation-vs-standing-role` exists to prevent.
**R + F:** negative `participation-counted-as-raci` — assertion with `assignment-mode = activity-instance` counted toward the A/R cardinality → **refuse**.

### E. Authority-plane collapse

**D-24 (B) — DecisionRight is attributed to a single base.**
`profileTypes.DecisionRight.disposition` names two planes, but `baseModelId` is `"WM-XCT-023"` alone and `baseRegistryRef` is `vr.wm-xct-023` alone. Any machine reading `baseModelId` collapses seat authority into the assertion plane — inside the very structure that forbids the collapse.
**R:** Split into `DecisionRight.seat` (WM-ORG-004 / `vr.wm-org-004`) and `DecisionRight.held` (WM-XCT-023 / `vr.wm-xct-023`). No `profileTypes` entry may carry two planes.
**F:** negative `decision-right-single-base-attribution` → **refuse**.

**D-25 (B) — Occupancy is not forbidden from auto-creating held authority.**
The three-plane constraint forbids storing the planes "as one fact", but nothing forbids **deriving** held decision rights from seat decision rights at occupancy start — the most likely real-world collapse, and the one the existing fixture does not reach.
**R:** Constraint: *"Occupancy of a Position MUST NOT create, imply or be read as a held-authority assertion. Held authority exists only as an explicit WM-XCT-023 assertion with its own authority basis, validity interval and provenance."*
**F:** negative `occupancy-implies-held-authority` → **refuse**.

**D-26 (M) — The vacancy authority rule creates a cross-plane fact silently.**
`de-vacancy-authority-rule` (lapse / escalate to the reports-to post / transfer to a delegate) is a seat-plane element that moves authority to a **different** holder. Unconstrained, it produces a held-authority effect with no assertion behind it.
**R:** Constraint: *"Escalation or transfer under a vacancy authority rule remains a seat-plane rule and MUST produce an explicit, time-bounded held-authority assertion on the receiving party or post before any exercise. `lapse` MUST leave no held authority."*
**F:** negative `vacancy-escalation-without-assertion` → **refuse** exercise. positive `vacancy-escalation-with-bounded-assertion` → **accept** for the bounded interval only.

**D-27 (m) — Fixture covers three planes; the model declares four.**
`authorityPlanes` lists seat, held, assignmentConveyance and technicalAccess; `seat-held-assignment-authority-collapse` names three.
**R + F:** negative `four-authority-planes-collapsed` covering the technical-access plane as well.

### F. RACI cardinality leakage

**D-28 (B) — The counting predicate ignores both status machines.**
WM-XCT-023 carries `role-status` and `registration-status`, both `required`, deliberately kept apart (GLEIF-derived). `raciRule` says "exactly one per host and interval" without saying which states count. A suspended A plus a replacement A is either a double-A or, if suspension counts as absence, an undetected accountability gap. `raci-one-a-one-r` pins no statuses.
**R:** Define the counting predicate exactly: enumerate counting vs non-counting `role-status` values; require `registration-status` to be published-equivalent for an assertion to count; state whether a suspension-induced gap is refused or tolerated.
**F:** negative `suspended-a-plus-new-a-counted-twice` → **refuse**. negative `all-a-suspended-gap` → **refuse** (or accept per the declared rule, stated). positive `revoked-a-excluded-from-count` → **accept**; revoked A excluded.

**D-29 (B) — Derived and cascaded assertions may inflate or satisfy the count.**
`cascade-mode` and `derived-assertion-flag` are both `required` in the mixin. A container-host A cascading to parts creates A assertions on the parts with no author; a derived R can satisfy "at least one Responsible" with nobody actually assigned.
**R:** Constraint: *"The RACI cardinality rule counts direct assertions only. Derived holdings MUST be excluded from the A and R counts and MUST NOT satisfy the Responsible requirement. A cascaded A onto a host already carrying a direct A MUST be refused or suppressed; the chosen behaviour MUST be declared."*
**F:** negative `cascaded-a-inflates-count` → **refuse**. negative `derived-r-satisfies-responsible` → **refuse**.

**D-30 (B) — Position-as-player on a pooled seat multiplies accountable persons.**
`position-as-player` is a positive fixture and `capacityRule.pooled` permits multiple holders. One A assertion whose player is a pooled Position with headcount 2 resolves to two accountable parties, defeating exactly-one-A without ever producing a second assertion.
**R:** Constraint: *"Where the player is a Position, the Accountable slot requires the seat to be single-capacity, or a recorded designated-holder rule. Pooled seats MUST NOT be Accountable players absent that rule."*
**F:** negative `pooled-position-as-accountable` → **refuse**. positive `single-position-as-accountable` → **accept**.

**D-31 (M) — Collective players and joint holders unaddressed.**
`collective-player-flag`, `holder-share`, `quorum-requirement` and `joint-action-required` let a single A assertion be a covert committee.
**R:** Constraint: *"Accountable MUST NOT carry a collective player absent a named committee-designation rule; `holder-share` and `quorum-requirement` MUST be refused on the A slot."*
**F:** negative `collective-accountable` → **refuse**.

**D-32 (M) — No enforcement mechanism is named, and the study names the wrong one.**
The Claude study attributes duplicate prevention to `assertion-uniqueness-key`, which is *"the attribute set over which duplicate assertions are prohibited"* — it prevents duplicate **assertions**, not two distinct A assertions by different players. `raciRule` names no mechanism at all.
**R:** State the mechanism: profile-local cardinality evaluation over the `profileRef`-marked assertion set, executed at `validate-role-assertion`. Do not attribute it to `assertion-uniqueness-key`.
**F:** negative `duplicate-key-mistaken-for-cardinality` — two distinct A players with distinct uniqueness keys accepted → **refuse**.

**D-33 (m) — `raci-two-accountable` expectation is non-deterministic** ("refuse or resolve interval before acceptance"). See D-54.

### G. Segregation-of-duties bypass

**D-34 (B) — Static and dynamic separation are conflated.**
`separation-mode` distinguishes assignment-time from transaction-time exclusion. The constraint mandates refusal of the assignment, and `sod-conflict-no-exception` expects "refuse", with no mode pinned. Two failures at once: dynamic-mode conflicts are **false-refused** at assignment, and — the real bypass — the transaction-time check that dynamic mode presupposes lives outside this contour and is never required to exist.
**R:** Constraint: *"Every `incompatible-role-pair` MUST declare `separation-mode`. Static conflicts are refused at assertion time. Dynamic conflicts are accepted at assertion time only with a reference to the external transaction-time enforcement point; absence of that reference MUST cause refusal."*
**F:** negative `sod-static-no-exception` (existing case, mode pinned static) → **refuse**. positive `sod-dynamic-accepted-with-enforcement-point` → **accept**. negative `sod-dynamic-without-enforcement-point` → **refuse**.

**D-35 (B) — Delegation and on-behalf-of bypass.**
`on-behalf-of-ref`, `sub-delegation-permitted` and `delegation-chain-depth` let a party barred from a role exercise it without holding it. No constraint requires SoD evaluation to see delegated holdings.
**R:** Constraint: *"SoD evaluation MUST include delegated and acting-on-behalf-of holdings and MUST traverse the full delegation chain. A delegation that would place an incompatible pair on one party MUST be refused. Sub-delegation MUST NOT widen the delegate's effective role set beyond the delegator's."*
**F:** negative `sod-bypass-via-on-behalf-of` → **refuse**. negative `sod-bypass-via-sub-delegation` → **refuse**.

**D-36 (B) — Position-as-player defeats party-level SoD.**
Two Positions, each holding one side of an incompatible pair, both occupied by the same party: the assertions' players are Positions, so a party-level check finds nothing. Resolution requires WM-ORG-016 — which is unpinned, so today the check can **never** succeed.
**R:** Constraint: *"SoD evaluation MUST resolve Position players to effective occupants through WM-ORG-016 as of the evaluated interval. Where occupancy cannot be resolved, the combination MUST be refused, never accepted. While WM-ORG-016 is unpinned this refusal is unconditional."*
**F:** negative `sod-bypass-via-two-positions-one-occupant` → **refuse**. negative `sod-unresolvable-occupancy-accepted` → **refuse**.

**D-37 (M) — The compensating control has no carrier.**
The constraint makes a compensating-control link mandatory, but no data element in either pinned base holds one; `sod-exception-ref` points at the exception, not at the control.
**R:** Either bind the control to `sod-exception-ref` and say so, or declare it a profile-local requirement with an unallocated carrier recorded in the dependency list.
**F:** negative `sod-exception-without-compensating-control` → **refuse** (distinct from `sod-permanent-exception`, which tests expiry only).

**D-38 (M) — Exception lapse and delegation revocation untested.**
Nothing tests an incompatible assignment continuing past a recorded expiry, nor the `delegation-revoked-at` effect on acts already performed — a question the mixin asks explicitly.
**R:** Constraint: *"On exception expiry the incompatible assignment MUST be automatically suspended or refused as of the expiry instant. Revocation MUST NOT retroactively invalidate acts already performed unless explicitly recorded."*
**F:** negative `sod-exception-lapsed-still-active` → **refuse**. positive `delegation-revoked-prior-acts-preserved` → **accept**; prior acts retained.

**D-39 (M) — Incompatibility sets are asserted as mandatory although they are evidence-free.**
WM-XCT-023 `deferredResearch`: *"Whether any authority publishes a reusable role-incompatibility or segregation-of-duties matrix; grok found none in primary sources, so incompatibilities are currently Dimension-local by default rather than by evidence."* Grok blocker 6 requires the exception lifecycle to be written into the profile rather than deferred. The candidate records neither.
**R:** Add `sodEvidenceStatus: "dimension-local-no-primary-source"` plus a publication hold, and write the exception lifecycle into the profile explicitly (states, approver, expiry, compensating control, review cadence).
**F:** negative `sod-matrix-claimed-as-standard` → **refuse**.

### H. IAM grants

**D-40 (M) — Only forward leakage is fixtured.**
`party-role-grants-iam` covers assertion → grant. The reverse — an entitlement, group membership or session used to infer, evidence or renew a profile assertion — is unconstrained, and launders access into accountability.
**R:** Constraint: *"Flow is one-way. Profile assertions MAY be authorization inputs. An IAM grant, entitlement, group membership or session MUST NOT create, evidence or renew a profile assertion."*
**F:** negative `iam-grant-creates-party-role` → **refuse**. negative `group-membership-evidences-accountability` → **refuse**.

**D-41 (m) — `constraint-expression` can carry permissions.**
It is defined as *"evaluable by a policy engine"*, and the mixin's own deferred research concedes no cited source supplies a suitable expression language.
**R:** Constraint: *"`constraint-expression` MUST express representation and decision limits only and MUST NOT encode permissions, resources or system actions."* Record the missing expression language as an open dependency.
**F:** negative `constraint-expression-encodes-permission` → **refuse**.

### I. History rewrite

**D-42 (B) — Tritemporal claim exceeds both bases.**
The constraint requires preserving *"event, valid and knowledge time"*. WM-ORG-004 supplies bitemporal only (`de-effective-window` business validity vs `de-record-instants` capture); WM-XCT-023 supplies *"separation of effective time from knowledge time"*. "Event time" as a third axis has no owner in either pinned base, and the mixin that would own it is not even enumerated (D-48).
**R:** Restate as bitemporal (valid/effective time, knowledge/record time), or declare event time a profile-local third axis with no base support and an unallocated carrier.
**F:** amend `history-overwrite` to name the exact axes preserved. negative `event-time-claimed-as-base-supported` → **refuse**.

**D-43 (B) — Abolition and reinstatement are unhandled.**
`position-lifecycle-states` asks: *"Can an abolished position be reinstated, or must a new identity be minted?"* The candidate is silent. Reinstating under the same identifier rewrites the seat's history and collapses two seats into one identity; it also interacts with D-06 (an abolished seat must never derive as vacant).
**R:** Constraint: *"Abolition is terminal for the identifier in this profile. Reinstatement MUST mint a new Position identity with a recorded supersession link to the abolished one. `de-abolition-date` (business) MUST remain distinct from the record close instant."*
**F:** negative `abolished-position-reinstated-same-id` → **refuse**. positive `reinstatement-new-id-with-supersession` → **accept**.

**D-44 (M) — Position-side correction vs substantive change untested.**
`de-change-type` determines *"whether prior versions remain assertable"*; the only history fixture is on the assertion side.
**R + F:** negative `position-correction-overwrites-prior-version` → **refuse**. positive `position-substantive-change-appends-version` → **accept**; prior version remains assertable.

**D-45 (M) — Retroactive host re-pointing untested.**
Re-pointing `host-version-ref` after the fact silently rewrites what was accountable for what.
**R + F:** negative `retroactive-host-repoint` → **refuse**; append a superseding assertion instead.

### J. Unsupported release claims, pins, identifiers, fixture hygiene

**D-46 (B) — `modelVersion: "0.3.0-research.1"` is an invented version identifier.**
Asserted for **both** bases. The frozen dossier's `current_specs` carry no version field; the registry carries only `source_version_or_year: "2026-08-22"`; publication carries `generatedAt` 2026-08-24 and 2026-08-23. Nothing underwrites a semver-with-prerelease string, and a version string is precisely a release claim.
**R:** Remove `modelVersion`, or replace with the fields the dossier does carry (`sourceVersionOrYear`, `generatedAt`) and mark any version string `not-evidenced-in-frozen-dossier`.
**F:** negative `unevidenced-model-version-pinned` → **refuse**.

**D-47 (B) — `WM-ECO-012` is used normatively though it lies outside the frozen dossier.**
It appears in a MUST constraint (*"…distinct from … WM-ECO-012 budget lines"*) and in fixture `budget-line-as-position-plan`. It exists only in the Grok study. The provider comparison states the governing rule itself: *"References to models outside the frozen dossier remain explanatory only and are not adopted as verified dependencies."* Every other model id used normatively (WM-ORG-002, WM-ORG-003, WM-ORG-016) is present in the dossier's `relationship_ledger`; this one is not.
**R:** Restate the constraint without the identifier ("an external budget-line record whose owner is not identified in this dossier") and retarget the fixture identically; or add WM-ECO-012 as an explicitly unpinned dependency and demote the constraint to non-normative.
**F:** amend `budget-line-as-position-plan` to name no out-of-dossier identifier; re-compute its digest.

**D-48 (M) — `requiredDependencies` omits six dependencies the bases themselves mark `required: true`.**
Missing — WM-ORG-004: *Job / class / occupation classifier model* (REFERENCE, required true) and *Effective-dated versioning and provenance mixin* (MIX-IN, required true). WM-XCT-023: *Party / Agent identity model* (REFERENCE, required true), *Identifier and identity-resolution mixin* (MIX-IN, required true), *Temporal validity (bitemporal period) mixin* (MIX-IN, required true), *Provenance and assertion-record mixin* (MIX-IN, required true). The `invalidationRule` keys on "required-dependency drift" over an incomplete set — and the two mixins omitted are exactly the owners of the history constraints (D-42) and of duplicate detection (D-32).
**R:** Enumerate all base-declared required dependencies with `pinned: false` and a reason; restate the invalidation rule over the completed set.
**F:** negative `required-dependency-set-incomplete` — candidate asserts bitemporal and identity-resolution constraints while their owning mixins are unenumerated → **refuse** publication readiness.

**D-49 (M) — `registrySnapshotSha256` has no stated input scope or canonicalization.**
Unlike the fixture digests, which declare `digestMeaning`, the two registry snapshot digests declare neither which bytes they cover nor under which canonicalization; they are unreproducible from the frozen material.
**R:** Add `digestMeaning` and `digestInput` (which registry columns, in which order, under which canonical JSON rules) to each snapshot pin.
**F:** negative `unreproducible-registry-digest` → **refuse**.

**D-50 (M) — The reservation of record self-declares as a previous version.**
`vr.wm-org-004`: `status: "described-previous-version"`, `review_state: "migration-boundary-review"`, `source_version_or_year: "2026-08-22"` — pinned alongside a synthesis generated 2026-08-24. The registry row does not describe the pinned spec, yet is treated as its reservation.
**R:** Add `registryDescribesPinnedSpec: false` to the WM-ORG-004 pin plus a publication hold requiring a registry re-cut before canonical reuse.

**D-51 (M) — `entryKindDivergence: true` is flagged but not gated.**
`registryEntryKind: "standalone-mm"` vs `specEntryKind: "entity"`, with `composition_role: "COMPOSE"` and `default_link_type: "TYPED-EDGES"` on the same row. The flag appears in `basePins` and in no hold, no constraint and no fixture.
**R:** Add to `publicationHolds` and add a constraint refusing canonical reuse until the divergence is adjudicated.
**F:** negative `entry-kind-divergence-unresolved` → **refuse**.

**D-52 (M) — Provenance is unpinned.**
`provenance` names three artifacts and `audit: "pending"` with no digests. The bases are pinned to the byte; the studies this revision reconciles are not, so they can drift without invalidating the candidate.
**R:** Add `sha256` per provenance artifact and include provenance drift in the invalidation rule.
**F:** negative `unpinned-provenance-artifact` → **refuse**.

**D-53 (M) — The fixture set under-pins and is unlinked to the candidate.**
`baseSourcePins` carries `sourceSha256` only — no `synthesisSha256`, no registry snapshots, no `contourId`, no candidate digest, and no digest over the ordered case set. Synthesis drift would invalidate the candidate but not the fixtures; cases may be added or removed undetectably; `fixtureRevision: 2` matches `candidateRevision: 2` by convention alone.
**R:** Add `contourId`, `candidateSha256`, per-base `synthesisSha256` and a `caseSetSha256` over the ordered case digests.
**F:** negative `fixture-set-unlinked-to-candidate` → **refuse**.

**D-54 (M) — Five fixture expectations are non-deterministic, and their digests pin the ambiguity.**
`raci-two-accountable` ("refuse **or** resolve interval before acceptance"); `pooled-two-half-fte` ("accept **when** headcount and overlap policy also allow" — conditions not pinned in the input); `pooled-over-capacity` ("refuse **absent** explicit override outcome" — the override is not in the input); `delete-employee-cascade` ("only occupancy/person handling changes" — unspecified); `plan-projection` ("accept with immutable plan and approval pins" — no plan identity exists anywhere in the material).
**R:** Rewrite each `input` to pin every discriminating parameter and each `expect` to one outcome; re-compute all affected digests.

**D-55 (M) — Constraints are untagged as to provenance.**
The 27-item list mixes base restatements, profile-local narrowings and additions with no base support (FTE non-negativity, exactly-one-Accountable, mandatory compensating control, tritemporality). A reader cannot tell which are inherited and which are asserted, so the candidate's own no-unsupported-claim discipline is uncheckable.
**R:** Tag every constraint `base-restatement` (with the base finding or element id), `profile-local-narrowing`, or `profile-local-addition-unsupported`.
**F:** negative `untagged-constraint-treated-as-base-rule` → **refuse**.

**D-56 (m) — HeadcountPlan is simultaneously required and optional.**
It sits in `requiredDependencies` while `profileTypes` calls it a deferred candidate and a constraint says capacity **MAY** be a projection from a plan.
**R:** Move to a `deferredCandidates` list; it is not a required dependency and must not participate in the invalidation rule.

**D-57 (m) — The IAM plane is listed as a required dependency although it is deliberately unidentified**, diluting the invalidation rule.
**R:** Move to an `externalBoundaries` list.

**D-58 (m) — The contour is renamed without record.**
Dossier `contour.name` is "Позиции, роли и ответственность"; the candidate's `name` is "Enterprise Position, Role and Accountability", with the original nowhere recorded. Grok explicitly worked *"without renaming the contour."*
**R:** Carry `contourName` verbatim from the dossier and add an English `profileLabel` as a separate field.

**D-59 (m) — A declared contour question has no fixture.**
`specific_questions[1]` asks *"Как поддержать job sharing и роли без штатной позиции?"*. Job sharing is fixtured (D-14); **roles without a position** are not.
**R + F:** positive `role-without-position` — assertion with a party player, no `position-ref`, host = a process → **accept**.

---

## 4. CONTRADICTIONS

**C-01 — Queue reservation vs. the artifacts being audited.** `queue_reservation` says `status: "queued"`, `claude_status: "not-started"`, `grok_status: "not-started"`, `boundary_decision: "pending"`, `remaining_scope: "Entire research brief pending"` — while both studies, a comparison and a revision-2 candidate exist inside the same frozen package. The reservation row is stale by design or the package is mislabelled; the candidate declares neither. *Resolve:* update the reservation atomically with this audit, or record `queueRowStale: true` with the reason.

**C-02 — Ledger vs. spec on WM-ORG-003.** `relationship_ledger` asserts `WM-ORG-003 COMPOSE WM-ORG-004` ("Team is composed through positions and assignments"); WM-ORG-004's own `composition` asserts `WM-ORG-003 Team — REFERENCE — required: false`. Different relation type and different obligation. The candidate copies the ledger row verbatim into `relationshipLedgerStatus` without flagging the divergence, and omits the spec-side composition rows entirely — so the `required: true` status of WM-ORG-002, WM-ORG-016 and the classifier is invisible in the candidate. *Resolve:* carry both views side by side with an explicit divergence marker; adjudicate before the rows leave `candidate`.

**C-03 — Registry vs. spec entry kind (WM-ORG-004).** `standalone-mm` + `composition_role: COMPOSE` + `default_link_type: TYPED-EDGES` against `entry_kind: entity`. Flagged, ungated (D-51).

**C-04 — Registry currency vs. pinned synthesis.** `status: "described-previous-version"` and `source_version_or_year: "2026-08-22"` against syntheses generated 2026-08-23/24 (D-50).

**C-05 — "published" vs. `publishableCanonical: false`.** Both specs carry `publication.status: "published"` with `adjudicationStatus: "reviewable-draft"`; the dossier's own `vercy_candidates` note states *"published не означает завершённую независимую экспертизу."* The candidate handles this in prose in `publicationHolds` but drops the `status` field from `basePins`, leaving the word unqualified wherever the dossier is read directly. *Resolve:* carry `publicationStatus: "published"` in `basePins` with an adjacent `meaning: "pipeline emission, not canonical adjudication"`.

**C-06 — Claude study contradicts itself, and the candidate inherits it.** *"Position — REUSE ONLY … Nothing in EM-ORG-06 survives the vacancy test as new structure"* against, four sections later, *"Plus a job-share profile over WM-ORG-004 fixing pooled capacity and fractional-sum validation."* The candidate reproduces the split: `profileTypes.Position.disposition = "reuse …"` while `capacityRule` and six constraints constitute a profile over WM-ORG-004; and the top-level `decision` is a single `"PROFILE"` for what is a two-base compound decision. *Resolve:* record `decision` per base — `REUSE(WM-ORG-004) + PROFILE(WM-XCT-023)` — and name the capacity/job-share narrowing as an explicit profile over WM-ORG-004.

**C-07 — Claude vs. Grok on BusinessRole.** Claude: it should *complete* WM-XCT-023's unallocated required vocabulary REFERENCE. Grok: *"do not silently fold it into WM-XCT-023."* Reconcilable — fill the slot by reference without embedding — but the candidate states neither, leaving a base-declared required dependency unmapped (D-22).

**C-08 — Three positions on HeadcountPlan.** Claude: *"identifier-unassigned candidate, but identifier assignment held."* Grok: *"Defer — identifier unassigned."* Candidate: a **required** dependency whose use is nonetheless optional (D-56).

**C-09 — Vacancy storage, inside WM-ORG-004 itself.** Its adjudication decision "Vacancy as derived state" rejects a stored vacancy flag as *"a second source of truth against WM-ORG-016"*; its own `selected_findings` define `de-open-capacity` and `de-vacancy-since` as elements on the seat. The candidate's absolute "MUST NOT be stored" inherits the contradiction rather than resolving it (D-08).

**C-10 — Mandatory SoD vs. the evidence.** The candidate's MUST-refuse rule against WM-XCT-023's `deferredResearch` finding that no authority publishes a reusable incompatibility matrix and that incompatibilities are Dimension-local by default; and against Grok blocker 6 requiring the exception lifecycle to be specified in the profile rather than deferred (D-39).

**C-11 — Job-share asserted vs. declared unsupported.** The contour's `acceptance_scenario` and the positive fixture `pooled-two-half-fte` against both bases' deferred research (no primary support for job-share fractions or dual-incumbency overlap) and Claude's own concession that this is *"a declared local profile, not an evidenced capability"* (D-14).

**C-12 — Comparison rule vs. candidate practice.** The provider comparison forbids adopting out-of-dossier references as verified dependencies; the candidate uses `WM-ECO-012` in a MUST constraint and a fixture (D-47).

**C-13 — Dependency set vs. base composition rows.** Six `required: true` rows omitted from `requiredDependencies` (D-48), while the `invalidationRule` claims to key on required-dependency drift.

**C-14 — Fixtures vs. candidate pin scope.** `baseSourcePins` pins source digests only; `basePins`/`invalidationRule` also key on synthesis and registry drift. Synthesis drift invalidates the candidate but not the fixtures (D-53).

**C-15 — Mechanism mismatch carried forward.** Claude invariant 6 credits `assertion-uniqueness-key` with preventing multiple Accountables; the mixin defines it as the attribute set over which **duplicate** assertions are prohibited. The candidate drops the mechanism entirely rather than correcting it (D-32).

**C-16 — Player kind.** Candidate constraints say "person" and "human bearer"; WM-XCT-023 `player-kind` admits automated agents and WM-ORG-004 lists non-human occupancy as unresolved (D-03).

---

## 5. CLOSED REMEDIATION CHECKLIST

This list is closed: it contains no open-ended items, and discharging all 24 items converts this verdict to ACCEPT. No item may be discharged by summary, merge or restatement; the twelve inherited holds remain verbatim and untouched by this checklist.

1. **Record the decision per base.** `decision` → REUSE(WM-ORG-004) + PROFILE(WM-XCT-023); name the capacity/job-share narrowing as an explicit profile over WM-ORG-004. Restore `contourName` verbatim. *(C-06, D-58)*
2. **Remove `modelVersion` from both base pins**, or replace with `sourceVersionOrYear` / `generatedAt` marked `not-evidenced-in-frozen-dossier`. Add fixture `unevidenced-model-version-pinned`. *(D-46)*
3. **Purge `WM-ECO-012`** from the constraint and from `budget-line-as-position-plan`; restate as an unowned external budget-line record; re-compute the fixture digest. *(D-47, C-12)*
4. **Complete `requiredDependencies`** with all six base-declared `required: true` dependencies; restate the invalidation rule over the completed set; move HeadcountPlan to `deferredCandidates` and the IAM plane to `externalBoundaries`. Add fixture `required-dependency-set-incomplete`. *(D-48, D-56, D-57, C-13)*
5. **Gate the legacy alias.** Add the O2/O3 exclusion constraint, `legacyScopeStatus`, a publication hold, and fixtures `legacy-o3-membership-on-position`, `legacy-o2-unit-attributes-on-position`. *(D-01)*
6. **Gate the registry divergences.** Add `registryDescribesPinnedSpec: false`, promote `entryKindDivergence` to a publication hold plus a refusal constraint, add `digestMeaning`/`digestInput` to both registry snapshot digests. Fixtures: `entry-kind-divergence-unresolved`, `unreproducible-registry-digest`. *(D-49, D-50, D-51, C-03, C-04)*
7. **Qualify "published"** in `basePins` with its meaning; record the `index-and-publication-metadata` crosswalk depth as a publication hold. *(C-05, D-05)*
8. **Add the mastership block** (HRIS / corporate registry / vocabulary owner / no person master) and fixture `vocabulary-mastered-by-hris`; this discharges dossier blocking decision 2 in part. *(D-05)*
9. **Redefine vacancy** as a function of capacity, occupancy, hiring status, active status, abolition date and as-of instant; enumerate the closed state set with per-state derivation and comparison precision. Fixtures: `abolished-seat-derived-vacant`, `frozen-seat-derived-fillable`, `single-seat-partial-occupancy`; amend `vacant-position`. *(D-06, D-07)*
10. **Restate the vacancy storage rule** as a stamped recomputable projection, not a prohibition on storage. Amend `stored-vacancy-flag`; add `stale-vacancy-projection`. *(D-08, C-09)*
11. **Tag every WM-ORG-016-dependent fixture** `blocked-unexecutable` with `dependsOn`, and say so in `publicationHolds`. *(D-09)*
12. **Close the capacity rules:** undetermined position type; headcount>1 ⇒ pooled; independent FTE and headcount ceilings; bounded, authorized overrides; warn-mode may not satisfy a refusal. Fixtures: `position-type-absent-second-holder`, `position-type-absent-single-holder`, `single-seat-headcount-two`, `pooled-headcount-breach-fte-within`, `pooled-over-capacity-with-recorded-override`, `override-without-authority`, `warn-outcome-used-as-acceptance`, `occupancy-end-releases-capacity`. *(D-11, D-12, D-13, D-15)*
13. **Mark job-share `declared-local-no-primary-source`** in `capacityRule`, in `pooled-two-half-fte` and in `publicationHolds`; make that fixture unconditional. *(D-14, C-11)*
14. **Introduce the profile conformance marker** (`profileRef`) and scope the RACI cardinality rule to marked assertions only. Fixtures: `raci-count-includes-unmarked-assertion`, `profile-marker-absent-but-rule-applied`; amend `raci-rule-on-generic-role`. *(D-16)*
15. **Pin the assertion shape for the profile:** classification axis ∈ {functional, statutory}; closed `host-kind` set; `host-ref-mode = pinned` with one declared cardinality evaluation basis; exactly one `role-type-code`; strictest `role-type-binding-strength`. Fixtures: `raci-on-structural-axis`, `raci-functional-axis`, `raci-host-is-party`, `raci-host-is-organization`, `raci-float-host-ref`, `two-accountable-different-host-versions`, `raci-assertion-multi-typed`, `raci-local-unmapped-role-term`. *(D-17, D-18, D-19, D-20, D-21)*
16. **Map BusinessRole to the two base slots it fills** while keeping the identifier unassigned; add `business-role-folded-into-mixin`. *(D-22, C-07)*
17. **Define the RACI counting predicate** over both status machines; exclude derived and cascaded holdings; restrict Accountable players (single-capacity Position or declared designation rule; no collective, share or quorum); name the enforcement mechanism correctly. Fixtures: `suspended-a-plus-new-a-counted-twice`, `all-a-suspended-gap`, `revoked-a-excluded-from-count`, `cascaded-a-inflates-count`, `derived-r-satisfies-responsible`, `pooled-position-as-accountable`, `single-position-as-accountable`, `collective-accountable`, `duplicate-key-mistaken-for-cardinality`, `participation-counted-as-raci`. *(D-23, D-28, D-29, D-30, D-31, D-32, C-15)*
18. **Split the authority planes structurally:** `DecisionRight.seat` / `DecisionRight.held`; forbid occupancy from implying held authority; bind vacancy-rule escalation to an explicit bounded assertion; extend the collapse fixture to four planes. Fixtures: `decision-right-single-base-attribution`, `occupancy-implies-held-authority`, `vacancy-escalation-without-assertion`, `vacancy-escalation-with-bounded-assertion`, `four-authority-planes-collapsed`. *(D-24, D-25, D-26, D-27)*
19. **Close the four SoD bypass paths:** declare `separation-mode` per pair with a mandatory enforcement-point reference for dynamic mode; traverse delegation and on-behalf-of chains; resolve Position players to occupants through WM-ORG-016 and refuse when unresolvable; bind the compensating control to a named carrier; auto-suspend on exception expiry. Fixtures: `sod-static-no-exception`, `sod-dynamic-accepted-with-enforcement-point`, `sod-dynamic-without-enforcement-point`, `sod-bypass-via-on-behalf-of`, `sod-bypass-via-sub-delegation`, `sod-bypass-via-two-positions-one-occupant`, `sod-unresolvable-occupancy-accepted`, `sod-exception-without-compensating-control`, `sod-exception-lapsed-still-active`, `delegation-revoked-prior-acts-preserved`. *(D-34, D-35, D-36, D-37, D-38)*
20. **Record `sodEvidenceStatus: "dimension-local-no-primary-source"`**, add the publication hold, and write the exception lifecycle into the profile. Fixture `sod-matrix-claimed-as-standard`. *(D-39, C-10)*
21. **Make the IAM boundary one-way** and forbid permissions inside `constraint-expression`. Fixtures: `iam-grant-creates-party-role`, `group-membership-evidences-accountability`, `constraint-expression-encodes-permission`. *(D-40, D-41)*
22. **Fix the temporal claim and the history rules:** bitemporal restatement (or declared unsupported third axis); terminal abolition with new-identity reinstatement; Position-side correction vs. substantive change; no retroactive host re-pointing; erasure preserves the assertion and closed-interval counts; "party or agent" wording with non-human occupancy refused by default. Fixtures: `event-time-claimed-as-base-supported`, `abolished-position-reinstated-same-id`, `reinstatement-new-id-with-supersession`, `position-correction-overwrites-prior-version`, `position-substantive-change-appends-version`, `retroactive-host-repoint`, `player-erasure-deletes-assertion`, `player-erasure-tombstone`, `non-human-agent-as-accountable`; amend `history-overwrite`. *(D-02, D-03, D-42, D-43, D-44, D-45, C-16)*
23. **Tag all constraints by provenance**, add the `v1FieldMapping` block, and add fixtures `untagged-constraint-treated-as-base-rule`, `v1-field-reminted`, `role-without-position`. *(D-04, D-55, D-59)*
24. **Re-cut the artifacts and their pins:** link fixtures to the candidate (`contourId`, `candidateSha256`, per-base `synthesisSha256`, `caseSetSha256`); pin all provenance artifacts by digest and include them in the invalidation rule; rewrite the five non-deterministic expectations and re-compute every affected case digest; record both views of the divergent ledger rows with a divergence marker; reconcile or annotate the stale queue reservation. Fixtures: `fixture-set-unlinked-to-candidate`, `unpinned-provenance-artifact`. *(D-52, D-53, D-54, C-01, C-02, C-14)*

**Post-checklist status:** with items 1–24 discharged, `candidateRevision` advances to 3 with `candidateStatus: "frozen-audit-revise-applied"`. `publishableCanonical` remains **false** and publication remains refused independently of this checklist, because the twelve inherited holds, the three `candidate` ledger rows, the unpinned WM-ORG-016 and WM-ORG-002 dependencies, the unallocated BusinessRole vocabulary and the unexecuted fixture set are all still open, and none of them is dischargeable by this contour.