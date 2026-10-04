# FROZEN SEMANTIC AUDIT — EM-WRK-05
**Scope:** reconciled proposal + `local-evidence.md`, `grok-study.raw.md`, and both offline allocation candidate bundles (Resource Demand, Resource Pool). No tools, no browsing, no standards claims, no identifier invention, no registry mutation. Single pass.

---

## 1. Verdict

**REVISE.**

The identity decision is sound and is upheld unchanged. The two roots are correctly scoped, correctly left unassigned, and the mastership boundary to WM-PER-001 / WM-ORG-016 / WM-OBJ-001 / WM-ECO-012 / WM-XCT-009 / WM-FLW-015 is stated in the right place. The contour fails on **enforceability**, not on disposition: the majority of its declared invariants are borne by three objects — Capacity Plan profile, AllocationScenario, ResourceAllocation — for which **no artifact exists at all**, and the two artifacts that do exist carry comparability keys that do not join, required-field sets that cannot support their own invariants, and a direct contradiction between reservation expiry and release immutability.

Twenty-five material defects follow. All are artifact defects. Known registry/base publication gaps are recorded separately as holds in §6 and are not counted against the artifacts.

---

## 2. Material defects

### D1 — Named-person demand: unresolved contradiction, no discriminator field
`local-evidence.md` §Demand and pool and `allocation-candidate.json` (demand) invariant 4 both assert: *"A named-person request remains distinct from a competence requirement."* This presupposes a named-person request is **admissible**. `grok-study.raw.md` invariant 1 asserts the opposite without qualification: *"Demand does not name a person or asset,"* reinforced by *"It does not name a person or asset."* The reconciled proposal never adjudicates. Meanwhile the demand bundle does both at once: `boundary.excludes` lists *"person, asset, assignment or budget identity"*, while `boundary.references` lists `WM-PER-001` purpose *"Person identity"* and `WM-OBJ-001` purpose *"Physical resource identity"*. No field in `objects.ResourceDemand` expresses a named request, so the distinction the invariant protects is unrepresentable, and no fixture exercises it.

### D2 — Demand required-field set cannot support its own invariants
`objects.ResourceDemand.required = ["requestingWorkRef","resourceClass","quantityKind","unit","quantity","status"]`; `optional` contains `interval`, `deadline`, `divisibility`, `substitutability`, `uncertainty`.
- Invariant 2 reads *"Every demand declares quantity kind, unit, unit-scheme version and interval or deadline."* Both `interval` and `deadline` are optional, so the disjunction is unenforceable; and **`unitSchemeVersion` appears in no field list in either bundle**, although `local-evidence.md` requires *"quantity kind, unit, unit scheme and version"* on every demand, capacity and allocation.
- `divisibility` is optional while conflict detection depends on it (`local-evidence.md` invariant 9; grok *"Every demand, pool capacity and allocation carries a quantity kind, a unit, divisibility and exclusivity"*). An absent `divisibility` is silently readable as divisible.
- `substitutability` has no stated dimension (class, member, interval, or quantity), so it constrains nothing.
- `priority` carries no scheme or scale, so cross-demand priority is not comparable.

### D3 — Demand has no addressable version
`identityTest.versionIdentity` (demand): *"Changes to requesting work, resource class, quantity, interval, priority, divisibility, substitutability or uncertainty create immutable demand versions."* But `objects.ResourceDemand.identity = ["resourceDemandId"]` — no `version`, no `contentDigest`, no `validFrom`, no `supersedesVersion`; only an optional `successorRef`. Contrast the pool bundle, which does define `PoolVersion` with `identity:["resourcePoolId","version"]` and `contentDigest`. Consequences: fixture `revised-quantity` (*"A successor version preserves the prior requirement"*) is unverifiable, and `local-evidence.md` §Capacity plan and scenarios pins *"plan revision, pool versions, demand set, capacity assertions"* — **demand set, not demand versions** — so a released, immutable scenario silently re-points to mutated demands.

### D4 — Demand lifecycle conflates three orthogonal axes
`lifecycle: ["draft","submitted","approved","open","partially-matched","matched","withdrawn","expired","closed"]`.
- `approved` and `open` are not mutually exclusive (approval status vs. openness), and `partially-matched` is simultaneously open and matched. No transition table, no terminal set, no guard conditions.
- `matched` contradicts invariant 5, *"Matching creates a scored candidacy assertion and never an assignment"*, and invariant 1, *"Demand may exist unmet"*: it is undefined whether `matched` means a candidacy exists or that confirmed allocations cover the quantity.
- `expired` is unreachable and undefined for any demand without a `deadline`, which D2 shows is optional.
- `expired` here (demand lapse) collides lexically with reservation expiry in `local-evidence.md` §Allocation and reservation, two unrelated semantics under one word.

### D5 — Demand fulfilment can be driven by a non-baseline scenario (alternative-summation leak)
`local-evidence.md` invariant: *"Alternative scenarios are never summed"* and *"Selecting one as baseline requires an authorized decision."* Nothing states which scenario, if any, may move `ResourceDemand.status` to `partially-matched` / `matched`. Since `status` is required on the non-scenario-scoped demand root, a hypothesis release (S1) can mutate a root fact, and two competing scenarios can drive the same root in opposite directions — the practical equivalent of summing alternatives. No `fulfilmentBasisRef` or baseline-decision reference field exists.

### D6 — Comparability keys do not join between the two roots
Demand declares `quantityKind` and `resourceClass`. Pool declares `resourceKind` and `unit` — **it has no `quantityKind` field at all**. Every summation and rejection rule is phrased over quantity kind (`local-evidence.md` invariants 1–3; grok invariant 8, *"FTE, GPU-hours and currency are never summed"*), so the rule has no field to evaluate on the pool side. Separately, the *matching* key is also split: demand's `resourceClass` and pool's `resourceKind` are nowhere declared to draw from one vocabulary. Cross-kind rejection and demand→pool matching are therefore both unenforceable as specified. (The absence of a *canonical* quantity-kind taxonomy is a hold; the absence of the **field and the join rule** is an artifact defect.)

### D7 — Pool required-field set cannot support its own invariants
`objects.ResourcePool.required = ["name","resourceKind","unit","calendarRef","ownerRef","status"]`; `optional` contains `membershipRules`, `divisibility`, `reservationPolicy`, `overbookingPolicy`.
- Invariant 8: *"Overbooking is explicit policy and never inferred tolerance."* With `overbookingPolicy` optional, its absence is ambiguous between *no overbooking permitted* and *unspecified* — precisely the inferred tolerance the invariant forbids. Grok names this as blocker 1: *"No overbooking-policy attribute is specified."* The negative fixture `implicit-overbooking` is consequently undecidable.
- Invariant 7: *"Reservations have expiry and release capacity when expired"*, yet `reservationPolicy` is optional and no expiry clock, zone or calendar basis field exists anywhere. Grok blocker 3: *"Reservation expiry is not yet tied to the calendar."*
- `boundary.owns` claims *"divisibility and exclusivity rules"* and invariant 6 claims *"Divisibility and exclusivity are explicit per member or resource kind"* — **`exclusivity` appears in no field list in either bundle**, and `divisibility` is pool-level only, with no per-member form.
- `boundary.owns` claims *"calendar and timezone bindings"*, but only `calendarRef` is required: no IANA zone, no offset, no `tzdbRelease`, despite `local-evidence.md` invariant 13, *"Every allocation pins pool version, calendar and timezone release."*
- No `unitSchemeVersion`, as in D2.

### D8 — Pool root/version split is incoherent
`identityTest.versionIdentity` (pool): *"Changes to kind, unit, calendar, membership rules, divisibility, reservation or overbooking policy create immutable pool versions."* Every one of those fields lives on `ResourcePool`, whose `identity` is `["resourcePoolId"]` with **no version and no digest**; `PoolVersion.required` is `["capacityAssertions","validFrom","contentDigest"]`, so the digest covers capacity only. A scenario that *"pins pool versions"* therefore pins capacity while unit, calendar, divisibility, reservation and overbooking policy remain mutable underneath it — the released scenario is not reproducible. Two independent supersession mechanisms coexist with no precedence rule: root `successorRef` plus lifecycle state `superseded`, and `PoolVersion.supersedesVersion`; `superseded` is a version relation misplaced as a root lifecycle state.

### D9 — Membership is entirely unspecified
`boundary.owns` claims *"membership rules and effective membership"*; `local-evidence.md` claims *"effective-dated membership"*; `PoolVersion.optional` holds a bare `memberships` with no schema. There is **no `memberRef` and no declared target master, no `effectiveFrom`/`effectiveTo`, no per-member divisibility or exclusivity, and no cross-pool member key**. Three invariants are thereby unenforceable:
- *"Member capacity is counted once across shared pools"* — no stable member key and no declared consolidation scope. Fixture `shared-specialist` expects counting once *"in consolidated conflict checks"*, a term defined nowhere (same scenario? same plan? across plans?).
- *"Indivisible members admit at most one overlapping confirmed allocation per scenario"* — no member-level indivisibility flag exists to test.
- Membership outside its effective window is not excluded from any allocation.

### D10 — Pool lifecycle states have no defined effect on availability
`lifecycle: ["draft","approved","active","constrained","suspended","superseded","retired"]`. `constrained` is defined nowhere — no trigger, no effect, no allocatability rule. `suspended` is likewise undefined: whether it yields *zero available* or *unknown* is decisive against invariant 9, *"Unknown capacity is never treated as available."* And although invariant 12 says *"Retired pool versions remain resolvable for historical plans and allocations"*, **no invariant bars a new reservation or confirmation against a suspended root, a retired root, or a `PoolVersion` whose `validTo` precedes the allocation interval.**

### D11 — Overbooking arithmetic unreconciled; capacity double counting unresolved
Two incompatible formulas survive side by side:
- `local-evidence.md`: *"confirmed plus reserved demand cannot exceed **effective availability plus an explicit overbooking allowance**"* — additive, based on availability.
- `grok-study.raw.md`: *"reserved quantity of the same kind, unit and interval exceeds **capacity times one plus the allowed overbook fraction**"* — multiplicative, based on capacity.

The bases are not interchangeable: both documents insist capacity ≠ availability (grok invariant 3; `local-evidence.md`'s four-value split *"nominal, calendar-available, committed-elsewhere and effective-available"*). Worse, the scope of `committed-elsewhere` is undefined, producing a trilemma with no safe reading: if it includes **other scenarios of the same plan**, alternatives are netted into one another and *"Alternative scenarios are never summed"* is violated; if it includes **the same scenario's own confirmations**, those quantities are subtracted once and added again as scenario load — double counting; if it includes neither, cross-plan commitments vanish and availability is overstated. Grok's own `#8` blocker list omits this; it is live in both documents.

### D12 — Overbooking vs. exclusivity precedence unstated (unsafe)
`local-evidence.md` invariant 9 is unconditional: *"Indivisible members admit at most one overlapping confirmed allocation."* Invariant 8 permits overbooking under explicit policy, with no stated scope limit. Grok says *"Overlapping exclusive GPU jobs are a conflict under exclusivity even if each job is under 100%"* but never subordinates the overbooking allowance to exclusivity. As written, a pool-level `overbookingPolicy` is readable as licensing two overlapping confirmed allocations on an exclusive GPU.

### D13 — Reservation expiry contradicts allocation immutability
`local-evidence.md` invariant 6: *"Allocation is scenario-scoped and immutable after release."* Invariant 7: *"Reservations have expiry and release capacity when expired."* §Allocation and reservation: *"A reservation has an expiry and temporarily reduces effective availability."* An expiring reservation changes the status of an immutable released record — direct contradiction, with no statement that expiry is a **derived state computed from `expiresAt` and an evaluation instant** rather than a mutation. Compounding: there is no `expiresAt` field, no clock, no zone, no `tzdbRelease`, and no statement of whether expiry runs on wall-clock or working-calendar time. **`ResourceAllocation` has no status enumeration anywhere in the bundle**, so "reserved", "confirmed", "expired" and "lapsed" are prose only.

### D14 — Confirmation "may trigger" an external master write
`local-evidence.md`: *"Confirmation may trigger a referenced WM-ORG-016 assignment or schedule entry but cannot create or amend either master."* This is self-contradictory on its face and contradicts invariant 11, *"Allocation writes to no external master"*, and grok invariant 13, *"Allocation does not create an assignment."* "Trigger" is undefined: a side effect, an event, or a request. Grok blocker 4 confirms the gap: *"The later binding from a pool allocation to a Work Assignment is unspecified."*

### D15 — Quantity character (stock / rate / share) not modelled — the unit defect
Both roots carry a single scalar `quantity` + `unit`. The contour mixes three incommensurable characters under it:
- a **stock**: *"100 GPU-hours for a fixed interval"* (fixture `gpu-hours`);
- a **rate/headcount**: *"one specialist"* (fixture `unmet-specialist`);
- a **share**: *"SPEC-1 is allocated 0.6 and 0.5 of effective weekly capacity"* (§Acceptance result).

Invariant 3 evaluates conflict *"within one scenario, pool or member, interval and unit"* — but 100 GPU-hours and a 0.6 share are not comparable within an interval without integrating capacity over that interval, and the "unit" match does not detect the mismatch. Separately, a share is a **relative** quantity whose denominator is a versioned, calendar-dependent pool value: a released, immutable allocation expressed as `0.6` is not re-evaluable once the pool version or calendar changes, because no `capacityBasis` is recorded. Grok flags the kind axis (*"the kinds are incommensurable, so the sum is not a conflict and not a capacity"*) but not the character axis, which is where this contour actually fails.

### D16 — Acceptance result is arithmetically wrong
§Acceptance result: *"In scenario S1, SPEC-1 is allocated 0.6 and 0.5 of effective weekly capacity, producing a scenario-scoped conflict … two exclusive jobs overlap on GPU-1 … **In S2 one interval moves and both conflicts clear.**"*

The two conflicts have different clearing conditions and the narrative applies one remedy to both. The GPU-1 conflict is an **overlap** conflict under exclusivity and does clear when an interval moves. The specialist conflict is a **window-aggregate** conflict: 0.6 + 0.5 = 1.1 of *weekly* capacity. Moving an interval **within the same week leaves the total at 1.1** and clears nothing; it clears only if the move changes the aggregation window. The document conflates overlap-based and window-aggregate conflict detection, and **no aggregation window is defined anywhere** for share- or rate-valued load. As written, the single acceptance test the contour rests on does not pass.

### D17 — Invariant 3's "pool **or** member" permits missing the contour's own conflict
Invariant 3: *"Conflict is evaluated within one scenario, **pool or member**, interval and unit."* The disjunction authorizes evaluating one level only. §Acceptance result then requires the other: *"Aggregate GPU-hours remain within pool capacity, but two exclusive jobs overlap on GPU-1 and create an indivisibility conflict."* A conformant implementation evaluating the pool level alone reports that scenario clear. Fixture `exclusive-gpu` gestures at this (*"evaluated separately"*) without stating that both levels are mandatory.

### D18 — Time and interval representation absent
`local-evidence.md` asserts *"Every interval pins offset, IANA zone, timezone database release and applicable calendar"* and *"Conflict detection states which calendar expands recurrences and how DST gaps or overlaps are resolved"*, and *"Elapsed, working and effort durations remain distinct."* **No artifact defines an interval structure, a `tzdbRelease` field, a DST gap/overlap resolution policy, a recurrence-expansion owner, or a `durationKind`.** Additionally, pinning *both* offset and IANA zone admits inconsistent pairs at a given instant, with no consistency invariant. Grok's *"A non-overlap in one zone is not assumed in another"* has no field to attach to.

### D19 — Unknown capacity is unrepresentable
Invariant 9: *"Unknown capacity is never treated as available."* But `PoolVersion.required` includes `capacityAssertions` with **no internal schema and no unknown/tri-state value**, so a pool version with unknown capacity cannot be expressed at all — the invariant is vacuous, and the negative fixture `unknown-is-free` has no representable input. Invariant 3 also requires each capacity assertion to declare *"quantity kind, unit, interval, calendar and evidence"*; no `evidenceRef` field exists.

### D20 — Currency leaks into resource quantity; WM-ECO-012 is never referenced
`local-evidence.md` treats currency as a first-class quantity kind (*"Human effort, machine time and currency are different quantity kinds"*) while invariant 14 reserves money to WM-ECO-012 and grok states *"Compute capacity is a quantity kind on the pool, not a currency amount."* As written, `ResourceDemand.quantityKind = currency` is admissible, turning a demand into a budget request. Compounding the leak: **neither bundle lists WM-ECO-012 in `boundary.references`**, although the demand bundle `excludes` *"budget identity"* and `local-evidence.md` says *"Reuse WM-ECO-012 for money."*

### D21 — Dangling required references and derivation-asserting reference purposes
- `ResourceDemand.required.requestingWorkRef` — **no target model declared anywhere**.
- `ResourcePool.required.ownerRef` — **no target master declared**; WM-ORG-016 is referenced only for *"Human standing assignment"*, not for organisational identity.
- `ResourcePool.boundary.references` gives WM-ORG-016 the purpose *"Human standing assignment"*, which asserts membership is sourced from standing assignment — exactly grok's stated failure mode: *"If pool membership is derived from employment or asset mastership … detecting the 110% share or the GPU overlap forces a write to WM-PER-001, WM-ORG-016 or WM-OBJ-001. The test then fails."* Nothing in the artifact forbids derivation.
- `ResourceDemand.boundary.references` gives WM-ORG-016 the purpose *"**Resulting** human assignment"*, asserting causation that invariant 5 and grok invariant 13 both forbid.

### D22 — Uncertainty cannot be represented without collapse
Grok: *"Uncertainty stays attached to the assertion; it is not collapsed into a point value."* `ResourceDemand` has a scalar `quantity` (required) and an optional `uncertainty` of unstated form, with no range, bound or distribution structure. Any capacity evaluation must read `quantity` — i.e. must collapse. Fixture `gpu-hours` expects *"uncertainty are explicit"* with nothing to make it explicit in.

### D23 — No `EM-WRK-05-profile` artifact exists
Capacity Plan (profile on WM-ACT-008), **AllocationScenario** and **ResourceAllocation** have **no field sets, no identity keys, no lifecycles, no status enumerations, no fixtures and no validation policy** anywhere in the bundle. Yet they bear 11 of 15 `local-evidence.md` invariants and 9 of 13 grok invariants — scenario scoping, release immutability, reservation expiry, overbooking evaluation, interval pinning, pool-version pinning, baseline selection and the plan/fact separation. This is the single largest defect and it is not a registry hold: no identifier is needed to specify fields. Further specific gaps inside it:
- No `baselineDecisionRef`, though *"Selecting one as baseline requires an authorized decision."*
- No carry-forward or rebase rule across plan revisions: *"AllocationScenario exists only under one plan revision"* means a new WM-ACT-008 revision orphans every scenario including the selected baseline, while *"Variance cites both immutable revisions"* presumes they remain resolvable and correctly bound.
- Demand↔pool↔scenario linkage lives only on `ResourceAllocation`. Since neither root may reference an unallocated sibling by identifier, the linkage must be declared in the profile — and currently is declared nowhere.

### D24 — Validation policy and fixture-coverage defects
Both `validation-policy.json` files are byte-identical in `requirements` and demand nothing about the contour's actual risks: no required `quantityKind`, no version pinning, no `unitSchemeVersion`, no invariant-coverage rule, no `expectedCode`, and **no policy at all for the profile**. `minimumFixtures: 3` with `requiresPositiveAndNegativeFixtures: true` sets no per-polarity floor. Concretely:
- **No fixture carries `expectedCode`**, so every negative expectation (*"The transition is rejected"*) is untestable against a specific rule.
- Demand: of 12 declared invariants, at least 6 have no fixture — unknown supply, cross-kind conversion, withdrawal preservation, closure not rewriting masters, named-person distinctness, unit-scheme version.
- **Polarity is mislabelled**: pool fixture `implicit-overbooking` is `kind:"negative"` but expects *"The scenario is flagged as conflict"* — a successful detection, i.e. a positive case. The taxonomy conflates *rejected calculation* (`double-count-member`) with *conflict correctly raised*. Validation keys on `kind`, so the policy will score it wrongly.
- **Undecidable expectations**: `exclusive-gpu` expects *"Aggregate capacity and overlapping member exclusivity are evaluated separately"* with no stated outcome; `shared-specialist` expects counting once *"in consolidated conflict checks"*, a term defined nowhere (D9).
- `implicit-overbooking` says *"exceed capacity"*; the governing invariant says *"exceed effective availability"* (D11).

### D25 — Stale holds inside the audited bundle (minor, but a live internal contradiction)
Both bundles hold *"Independent Grok review and one frozen semantic audit are pending"* while the bundle under audit **contains** `grok-study.raw.md` and is the frozen audit. On freeze, those hold lines become false assertions in a published artifact.

---

## 3. Required bounded fixes

No new roots. No identifiers. No registry mutation. All fixes are field, invariant, enumeration or artifact-text changes within the fixed identity decision.

**F1 (D1).** Add required `ResourceDemand.requestMode ∈ {competence, named-preference}`. A `named-preference` demand must still carry `resourceClass`/competence, and its person/asset reference is a non-binding preference: it confers no exclusivity, no reservation and no assignment. Reconcile grok invariant 1 to: *demand never asserts person or asset mastership and never binds a named subject*. Delete the ambiguous `excludes` entry *"person, asset, assignment or budget identity"* in favour of *"mastership of person, asset, assignment or budget"*.

**F2 (D2).** Move to `required`: `unitSchemeVersion` (new field), `divisibility`, and the constraint `exactly one of (interval, deadline)`. Give `substitutability` a declared dimension set and `priority` a named scheme reference.

**F3 (D3).** Add `DemandVersion` with `identity:["resourceDemandId","version"]`, `required:["contentDigest","validFrom"]`, `optional:["validTo","supersedesVersion"]`. Change all scenario pinning language from *"demand set"* to *"demand versions"*.

**F4 (D4).** Split `status` into `approvalState ∈ {draft, submitted, approved, rejected, withdrawn}` and `fulfilmentState ∈ {open, partially-covered, covered, lapsed, closed}`; publish the transition table and terminal set; make `lapsed` reachable only when a `deadline` is present; rename demand `expired` to `lapsed` to free "expired" for reservations.

**F5 (D5).** Add `fulfilmentBasisRef` pinning (scenario release, authorized baseline decision). Invariant: *`fulfilmentState` may be advanced only from the baseline-selected scenario release; a non-baseline scenario never changes a demand root fact.*

**F6 (D6).** Add required `ResourcePool.quantityKind` and `PoolVersion` capacity-assertion `quantityKind`; declare that demand `resourceClass` and pool `resourceKind` draw from one named vocabulary, and that matching requires equal `quantityKind` and compatible `unit` under one `unitSchemeVersion`.

**F7 (D7).** Move to `required` on the versioned payload: `overbookingPolicy` (with an explicit closed form — `allowance: 0` means none; absence is invalid, never tolerance), `reservationPolicy` (with `defaultExpiry`, `expiryClock`, calendar basis), `divisibility`, new `exclusivity`, new per-member overrides, `ianaZone`, `tzdbRelease`, `unitSchemeVersion`.

**F8 (D8).** Relocate kind, unit, calendar, zone, membership rules, divisibility, exclusivity, reservation and overbooking policy into `PoolVersion`, and extend `contentDigest` to cover them. Keep on the root only `resourcePoolId`, `name`, `ownerRef`, `status`. Delete root `successorRef` and root lifecycle state `superseded`; supersession is `PoolVersion.supersedesVersion` only.

**F9 (D9).** Specify `Membership`: `memberRef` with declared target (WM-PER-001 or WM-OBJ-001), `memberKey` stable across pools, `effectiveFrom`, optional `effectiveTo`, per-member `divisibility` and `exclusivity`. Define the consolidation scope explicitly — *one scenario release, one `memberKey`, one `quantityKind`, one interval* — and replace *"consolidated conflict checks"* with that definition everywhere.

**F10 (D10).** Define `constrained` or remove it. Define `suspended` and `retired` as yielding **zero available, never unknown**. Add invariant: *no reservation or confirmation may reference a `PoolVersion` whose validity window does not cover the allocation interval, or whose root status is suspended or retired; retired versions remain resolvable for historical reads only.*

**F11 (D11).** Fix one formula and one base. Required: `effectiveAvailable = nominal − calendarUnavailable − committedElsewhere`, where **`committedElsewhere` excludes every scenario of the plan under evaluation**, and the threshold is `effectiveAvailable + overbookingAllowance` expressed as an absolute amount in the pool unit. Delete the multiplicative `capacity × (1 + fraction)` formulation from the reconciled text. Add invariant: *no quantity is both netted from availability and counted as scenario load.*

**F12 (D12).** Add invariant: *exclusivity is not overridable by any overbooking policy; overbooking allowance applies only to divisible, aggregate quantity-kind capacity and never to an indivisible member interval.*

**F13 (D13).** Define reservation expiry as **derived**: add `ResourceAllocation.expiresAt` (instant + `ianaZone` + `tzdbRelease` + calendar basis and whether wall-clock or working-time) and compute lapse from `expiresAt` versus the evaluation instant. A lapse never mutates the released record; if a lapse must be recorded, it is an appended derived-state assertion. Publish `ResourceAllocation.status ∈ {proposed, reserved, confirmed, lapsed, cancelled, superseded}`.

**F14 (D14).** Replace *"Confirmation may trigger a referenced WM-ORG-016 assignment or schedule entry"* with: *confirmation emits an outbound assignment request reference; WM-ORG-016 independently accepts or refuses it; the confirmation state is unchanged by either outcome and no master is created or amended.*

**F15 (D15).** Add required `quantityCharacter ∈ {stock, rate, share}` on demand, capacity assertion and allocation. Summation and comparison require equal `quantityKind`, `unit` **and** `quantityCharacter`. A `share` allocation must additionally record the absolute amount in the pool unit plus `capacityBasis` (pool version, interval, aggregation window) used to derive it.

**F16 (D16).** Add a required `aggregationWindow` for rate- and share-valued load, and distinguish two conflict classes in the invariants: **overlap conflict** (exclusivity/indivisibility, cleared by moving an interval out of overlap) and **window-aggregate conflict** (cleared only by moving load out of the window or raising availability). Correct §Acceptance result: S2 must move the specialist interval **into a different weekly window** and remove the GPU-1 overlap; state both clearing conditions separately.

**F17 (D17).** Rewrite invariant 3: *"Conflict is evaluated within one scenario, one interval, one quantity kind, unit and character, at the pool aggregate level **and**, wherever members are identified, at each member level."*

**F18 (D18).** Specify a `TimeInterval` structure: `start`, `end`, `ianaZone`, `offset`, `tzdbRelease`, `calendarRef`, `durationKind ∈ {elapsed, working, effort}`, `dstPolicy` for gaps and overlaps, and the named calendar that expands recurrences. Add invariant: *declared offset must be consistent with the declared zone at the interval instant under the pinned tzdb release.*

**F19 (D19).** Give `capacityAssertion` a schema: `quantityKind`, `unit`, `unitSchemeVersion`, `quantityCharacter`, `interval`, `calendarRef`, `valueState ∈ {asserted, unknown}`, `amount` (required iff `asserted`), `evidenceRef` (required iff `asserted`). `unknown` contributes zero to available.

**F20 (D20).** Add invariant: *currency is never a `ResourceDemand.quantityKind` nor a `ResourcePool` capacity unit; it appears only as a valuation on an evidence-bearing conversion assertion producing a new quantity.* Add WM-ECO-012 to both `boundary.references`.

**F21 (D21).** Declare the target master for `requestingWorkRef` and `ownerRef`. Restate the WM-ORG-016 reference purposes: pool → *"optional context only; membership is never derived from, nor constrained by, assignment or employment state"*; demand → *"referenced downstream assignment, non-causal"*. Add invariant: *pool membership is never derived from employment, assignment or asset mastership.*

**F22 (D22).** Replace the scalar quantity with `quantity {amount, lower, upper, distributionRef}` or add a required `quantityRange` where uncertainty is declared, and add invariant: *a declared range is never collapsed to a point value for capacity evaluation.*

**F23 (D23).** Produce the `EM-WRK-05-profile` artifact plus its own `validation-policy.json`, specifying: `CapacityPlanProfile` on WM-ACT-008 (pinning pool versions, demand versions, calendar refs, `tzdbRelease`, `unitSchemeVersion`, planning horizon, aggregation windows); `AllocationScenario` with `identity:["planId","planRevision","scenarioId"]`, `releasedAt`, `contentDigest`, `assumptions`, optional `baselineDecisionRef`, immutable after release; `ResourceAllocation` with `identity:["scenarioId","allocationId"]`, `demandVersionRef`, `poolVersionRef`, optional `memberRef`, `interval`, `quantity`, `status`, `expiresAt`, `capacityBasis`. Add an explicit scenario rebase rule across plan revisions: a new plan revision requires a new scenario release; prior scenarios and the prior baseline remain resolvable and are never silently re-pointed.

**F24 (D24).** Strengthen both validation policies and add the profile's: require `quantityKind` + `quantityCharacter` + `unitSchemeVersion` presence, version pinning, `expectedCode` on every negative case, a per-polarity minimum, and **one or more fixtures per declared invariant**. Re-label `implicit-overbooking` as a positive detection case, split the `kind` taxonomy into `positive` / `negative` / `detection`, and correct its wording from *"exceed capacity"* to *"exceed effective availability"*. Make `exclusive-gpu` and `shared-specialist` state decidable outcomes.

**F25 (D25).** On freeze, replace the "Grok review and frozen semantic audit are pending" hold in both bundles with a record that both are complete and that remaining holds are registry allocation and base publication only.

---

## 4. Additional fixtures

```json
[
  {"target":"ResourceDemand","id":"named-request-mode-declared","kind":"positive","input":"Demand carries requestMode=named-preference, names SPEC-1 via WM-PER-001, and still declares resourceClass, competence, quantityKind, unit and unitSchemeVersion.","expect":"Accepted as a non-binding preference. No exclusivity, no reservation, no assignment; matching still yields a scored candidacy."},
  {"target":"ResourceDemand","id":"named-request-without-mode","kind":"negative","input":"Demand references a WM-PER-001 person with no requestMode declared.","expect":"Rejected.","expectedCode":"E-DEMAND-REQUEST-MODE-MISSING"},
  {"target":"ResourceDemand","id":"named-request-implies-allocation","kind":"negative","input":"A named-preference demand is read as reserving that person's capacity.","expect":"Rejected.","expectedCode":"E-DEMAND-NAMED-IMPLIES-ALLOCATION"},
  {"target":"ResourceDemand","id":"named-request-asserts-mastership","kind":"negative","input":"Demand closure updates the referenced WM-PER-001 or WM-ORG-016 record.","expect":"Rejected.","expectedCode":"E-DEMAND-MASTER-WRITE"},
  {"target":"ResourceDemand","id":"no-interval-no-deadline","kind":"negative","input":"Demand declares neither interval nor deadline.","expect":"Rejected.","expectedCode":"E-DEMAND-TIMEBOUND-MISSING"},
  {"target":"ResourceDemand","id":"both-interval-and-deadline","kind":"negative","input":"Demand declares both an interval and a conflicting deadline with no precedence rule.","expect":"Rejected.","expectedCode":"E-DEMAND-TIMEBOUND-AMBIGUOUS"},
  {"target":"ResourceDemand","id":"unit-scheme-version-missing","kind":"negative","input":"Demand asserts 100 GPU-hour with no unitSchemeVersion.","expect":"Rejected.","expectedCode":"E-DEMAND-UNIT-SCHEME-VERSION-MISSING"},
  {"target":"ResourceDemand","id":"divisibility-inferred","kind":"negative","input":"divisibility is omitted and the matcher treats the demand as divisible.","expect":"Rejected.","expectedCode":"E-DEMAND-DIVISIBILITY-INFERRED"},
  {"target":"ResourceDemand","id":"priority-scheme-unnamed","kind":"negative","input":"Two demands with priority 1 and priority high are ranked against each other with no named priority scheme.","expect":"Rejected.","expectedCode":"E-DEMAND-PRIORITY-SCHEME-MISSING"},
  {"target":"ResourceDemand","id":"demand-version-addressable","kind":"positive","input":"Quantity rises from 100 to 140 GPU-hours.","expect":"A DemandVersion keyed [resourceDemandId, version] is created with contentDigest, validFrom and supersedesVersion; the prior version stays resolvable and unchanged."},
  {"target":"ResourceDemand","id":"scenario-pins-demand-id-only","kind":"negative","input":"A released scenario pins the demand by resourceDemandId with no version.","expect":"Rejected.","expectedCode":"E-DEMAND-VERSION-UNPINNED"},
  {"target":"ResourceDemand","id":"approval-fulfilment-split","kind":"positive","input":"Demand is approved while nothing can satisfy it.","expect":"approvalState=approved and fulfilmentState=open coexist; approval asserts nothing about supply."},
  {"target":"ResourceDemand","id":"candidacy-sets-fulfilment","kind":"negative","input":"A scored candidacy assertion sets fulfilmentState=covered.","expect":"Rejected.","expectedCode":"E-DEMAND-MATCH-IS-NOT-FULFILMENT"},
  {"target":"ResourceDemand","id":"lapse-without-deadline","kind":"negative","input":"A demand with no deadline transitions to lapsed.","expect":"Rejected.","expectedCode":"E-DEMAND-LAPSE-WITHOUT-DEADLINE"},
  {"target":"ResourceDemand","id":"fulfilment-from-non-baseline","kind":"negative","input":"A confirmed allocation inside non-baseline scenario S1 advances fulfilmentState to covered.","expect":"Rejected.","expectedCode":"E-DEMAND-FULFILMENT-FROM-NON-BASELINE"},
  {"target":"ResourceDemand","id":"fulfilment-from-baseline-decision","kind":"positive","input":"S2 is selected as baseline by an authorized decision and its confirmed allocations cover the demanded quantity.","expect":"fulfilmentState advances with fulfilmentBasisRef pinning the scenario release and the decision; S1 has no effect on the root."},
  {"target":"ResourceDemand","id":"currency-as-quantity-kind","kind":"negative","input":"Demand declares quantityKind=currency with amount 50000 EUR as a resource requirement.","expect":"Rejected.","expectedCode":"E-DEMAND-CURRENCY-NOT-RESOURCE-KIND"},
  {"target":"ResourceDemand","id":"conversion-yields-new-quantity","kind":"positive","input":"100 GPU-hours is valued in currency using a pinned conversion factor with evidence.","expect":"A new, separately identified quantity is produced; the original demand quantity is unchanged and the two are never summed."},
  {"target":"ResourceDemand","id":"uncertainty-range-preserved","kind":"positive","input":"Demand asserts 80 to 140 GPU-hours with a declared distribution.","expect":"The range is retained on the assertion and carried into planning without collapse."},
  {"target":"ResourceDemand","id":"uncertainty-collapsed","kind":"negative","input":"The 80 to 140 range is collapsed to its mean for a capacity check.","expect":"Rejected.","expectedCode":"E-DEMAND-UNCERTAINTY-COLLAPSED"},
  {"target":"ResourceDemand","id":"requesting-work-ref-target-undeclared","kind":"negative","input":"requestingWorkRef is populated with no declared target master.","expect":"Rejected.","expectedCode":"E-DEMAND-REF-TARGET-UNDECLARED"},
  {"target":"ResourceDemand","id":"withdrawal-preserves-history","kind":"positive","input":"An approved, partially covered demand is withdrawn.","expect":"Prior approvals, candidacies and scenario references remain resolvable; no external master is written."},
  {"target":"ResourceDemand","id":"approved-demand-as-supply","kind":"negative","input":"Approved demand is counted as available supply in a capacity figure.","expect":"Rejected.","expectedCode":"E-DEMAND-NOT-SUPPLY"},
  {"target":"ResourcePool","id":"pool-quantity-kind-present","kind":"positive","input":"Pool version declares quantityKind, unit, unitSchemeVersion, quantityCharacter and resourceKind from the named vocabulary.","expect":"Demand-to-pool comparison is decidable on quantityKind, unit and quantityCharacter."},
  {"target":"ResourcePool","id":"pool-quantity-kind-missing","kind":"negative","input":"Pool declares resourceKind and unit only, and a cross-kind rejection is attempted against it.","expect":"Rejected.","expectedCode":"E-POOL-QUANTITY-KIND-MISSING"},
  {"target":"ResourcePool","id":"class-kind-vocabulary-split","kind":"negative","input":"Demand resourceClass and pool resourceKind are matched across two undeclared vocabularies.","expect":"Rejected.","expectedCode":"E-MATCH-VOCABULARY-UNDECLARED"},
  {"target":"ResourcePool","id":"cross-kind-comparison","kind":"negative","input":"An FTE demand is evaluated against GPU-hour pool capacity.","expect":"Rejected.","expectedCode":"E-KIND-MISMATCH"},
  {"target":"ResourcePool","id":"overbooking-policy-absent","kind":"negative","input":"A pool version omits overbookingPolicy and a confirmation exceeds effective availability.","expect":"Rejected; absence is never read as tolerance.","expectedCode":"E-POOL-OVERBOOKING-POLICY-ABSENT"},
  {"target":"ResourcePool","id":"overbooking-zero-allowance","kind":"detection","input":"overbookingPolicy.allowance=0 and confirmed plus reserved load exceeds effective availability.","expect":"A conflict is raised in that scenario; both allocations are retained."},
  {"target":"ResourcePool","id":"exclusivity-undeclared","kind":"negative","input":"An indivisible GPU member is added with no exclusivity declared.","expect":"Rejected.","expectedCode":"E-POOL-EXCLUSIVITY-UNDECLARED"},
  {"target":"ResourcePool","id":"pool-version-covers-policy","kind":"positive","input":"overbookingPolicy is changed on an active pool.","expect":"A new PoolVersion is created whose contentDigest covers kind, unit, calendar, zone, divisibility, exclusivity, membership rules and both policies; the prior version stays resolvable."},
  {"target":"ResourcePool","id":"policy-change-without-new-version","kind":"negative","input":"unit or overbookingPolicy is edited in place with no new PoolVersion.","expect":"Rejected.","expectedCode":"E-POOL-UNVERSIONED-MUTATION"},
  {"target":"ResourcePool","id":"dual-supersession-conflict","kind":"negative","input":"Root successorRef and PoolVersion.supersedesVersion assert different chains.","expect":"Rejected.","expectedCode":"E-POOL-SUPERSESSION-CONFLICT"},
  {"target":"ResourcePool","id":"membership-effective-dated","kind":"positive","input":"GPU-1 joins on 2026-02-01 and leaves on 2026-05-01 with memberRef to WM-OBJ-001, memberKey, per-member divisibility=false and exclusivity=true.","expect":"Membership is accepted; allocations outside the effective window are not admissible against that member."},
  {"target":"ResourcePool","id":"allocation-outside-membership-window","kind":"negative","input":"A June interval is allocated to GPU-1 whose membership ended 2026-05-01.","expect":"Rejected.","expectedCode":"E-POOL-MEMBERSHIP-WINDOW"},
  {"target":"ResourcePool","id":"membership-derived-from-employment","kind":"negative","input":"Pool membership is derived automatically from a WM-ORG-016 standing assignment, and a conflict check writes that master.","expect":"Rejected.","expectedCode":"E-POOL-MEMBERSHIP-DERIVED"},
  {"target":"ResourcePool","id":"shared-member-dedup","kind":"positive","input":"SPEC-1 belongs to two pools for different planning views; both are read in one scenario.","expect":"Within the declared consolidation scope of one scenario, one memberKey, one quantityKind and one interval, the underlying capacity is counted once."},
  {"target":"ResourcePool","id":"shared-member-doubled","kind":"negative","input":"Capacity from SPEC-1's two pool memberships is summed into one availability figure.","expect":"Rejected.","expectedCode":"E-POOL-MEMBER-DOUBLE-COUNT"},
  {"target":"ResourcePool","id":"suspended-pool-zero-available","kind":"negative","input":"A reservation is made against a suspended pool version.","expect":"Rejected; suspension yields zero available, never unknown.","expectedCode":"E-POOL-VERSION-NOT-ALLOCATABLE"},
  {"target":"ResourcePool","id":"retired-version-read-only","kind":"positive","input":"A retired pool version is referenced by a historical released allocation and then by a new reservation.","expect":"The historical reference resolves unchanged; the new reservation is refused."},
  {"target":"ResourcePool","id":"constrained-state-undefined","kind":"negative","input":"A pool in lifecycle state constrained is treated as fully allocatable with no defined effect on availability.","expect":"Rejected.","expectedCode":"E-POOL-LIFECYCLE-STATE-UNDEFINED"},
  {"target":"ResourcePool","id":"effective-availability-basis","kind":"positive","input":"Effective availability is computed as nominal minus calendar-unavailable minus committed-elsewhere, where committed-elsewhere excludes every scenario of the plan under evaluation.","expect":"The overbooking threshold is effectiveAvailable plus an absolute allowance in the pool unit; no quantity is both netted and counted as load."},
  {"target":"ResourcePool","id":"committed-elsewhere-double-subtraction","kind":"negative","input":"The evaluated scenario's own confirmations are included in committed-elsewhere and again as scenario load.","expect":"Rejected.","expectedCode":"E-POOL-CAPACITY-DOUBLE-COUNT"},
  {"target":"ResourcePool","id":"committed-elsewhere-crosses-scenarios","kind":"negative","input":"Committed-elsewhere nets S2's confirmations out of S1's availability.","expect":"Rejected.","expectedCode":"E-SCENARIO-NETTING"},
  {"target":"ResourcePool","id":"multiplicative-overbook-formula","kind":"negative","input":"The threshold is computed as nominal capacity times one plus an overbook fraction instead of effective availability plus allowance.","expect":"Rejected.","expectedCode":"E-POOL-OVERBOOK-FORMULA-MISMATCH"},
  {"target":"ResourcePool","id":"overbooking-overrides-exclusivity","kind":"negative","input":"An overbooking allowance is used to admit two overlapping confirmed allocations on indivisible GPU-1.","expect":"Rejected.","expectedCode":"E-POOL-EXCLUSIVITY-NOT-OVERRIDABLE"},
  {"target":"ResourcePool","id":"unknown-capacity-representable","kind":"positive","input":"A pool version asserts a capacity entry with valueState=unknown and no amount or evidence.","expect":"The entry is representable and contributes zero to effective availability."},
  {"target":"ResourcePool","id":"capacity-without-evidence","kind":"negative","input":"An asserted capacity amount is recorded with no evidenceRef.","expect":"Rejected.","expectedCode":"E-POOL-CAPACITY-EVIDENCE-MISSING"},
  {"target":"ResourcePool","id":"unknown-treated-as-available","kind":"negative","input":"A capacity entry with valueState=unknown is counted as available supply.","expect":"Rejected.","expectedCode":"E-POOL-UNKNOWN-AS-AVAILABLE"},
  {"target":"ResourcePool","id":"owner-ref-target-undeclared","kind":"negative","input":"ownerRef is populated with no declared target master.","expect":"Rejected.","expectedCode":"E-POOL-REF-TARGET-UNDECLARED"},
  {"target":"ResourcePool","id":"currency-as-pool-unit","kind":"negative","input":"A pool asserts capacity in EUR as a resource unit.","expect":"Rejected.","expectedCode":"E-POOL-CURRENCY-NOT-CAPACITY"},
  {"target":"ResourcePool","id":"time-pins-complete","kind":"positive","input":"A pool version pins calendarRef, ianaZone, offset and tzdbRelease, with offset consistent with the zone at the interval instant.","expect":"Accepted and reproducible for later conflict evaluation."},
  {"target":"ResourcePool","id":"offset-zone-inconsistent","kind":"negative","input":"A declared offset contradicts the declared IANA zone at the interval instant under the pinned tzdb release.","expect":"Rejected.","expectedCode":"E-TIME-OFFSET-ZONE-INCONSISTENT"},
  {"target":"EM-WRK-05-profile","id":"profile-specified","kind":"positive","input":"The profile declares CapacityPlanProfile on WM-ACT-008 pinning pool versions, demand versions, calendar refs, tzdbRelease, unitSchemeVersion, planning horizon and aggregation windows, plus field sets, identity keys and status enumerations for AllocationScenario and ResourceAllocation.","expect":"Accepted; every scenario-borne invariant has a field to evaluate on and no new root is introduced."},
  {"target":"EM-WRK-05-profile","id":"allocation-status-outside-enum","kind":"negative","input":"An allocation carries a status outside {proposed, reserved, confirmed, lapsed, cancelled, superseded}.","expect":"Rejected.","expectedCode":"E-ALLOC-STATUS-UNDECLARED"},
  {"target":"EM-WRK-05-profile","id":"reservation-expiry-missing","kind":"negative","input":"A reserved allocation omits expiresAt or its zone, tzdbRelease and calendar basis.","expect":"Rejected; a reservation with no resolvable expiry is invalid, not indefinite.","expectedCode":"E-ALLOC-RESERVATION-EXPIRY-MISSING"},
  {"target":"EM-WRK-05-profile","id":"expiry-is-derived","kind":"positive","input":"A released reservation passes its expiresAt without confirmation.","expect":"Effective availability recomputes to release the quantity; the released allocation record is not mutated, and any lapse is an appended derived-state assertion."},
  {"target":"EM-WRK-05-profile","id":"expiry-mutates-release","kind":"negative","input":"Expiry rewrites the status field of a released, immutable allocation in place.","expect":"Rejected.","expectedCode":"E-ALLOC-RELEASED-MUTATION"},
  {"target":"EM-WRK-05-profile","id":"expired-reservation-as-confirmation","kind":"negative","input":"A lapsed reservation is read as a confirmation or as consumption.","expect":"Rejected.","expectedCode":"E-ALLOC-LAPSE-NOT-CONFIRMATION"},
  {"target":"EM-WRK-05-profile","id":"confirmation-emits-request","kind":"positive","input":"An allocation is confirmed and an outbound assignment request reference is emitted to WM-ORG-016, which then refuses it.","expect":"The confirmation state is unchanged by the refusal and no WM-ORG-016 record is created or amended."},
  {"target":"EM-WRK-05-profile","id":"confirmation-creates-assignment","kind":"negative","input":"Confirmation creates or amends a WM-ORG-016 assignment or a WM-ACT-008 schedule entry.","expect":"Rejected.","expectedCode":"E-ALLOC-MASTER-WRITE"},
  {"target":"EM-WRK-05-profile","id":"quantity-character-missing","kind":"negative","input":"An allocation quantity omits quantityCharacter.","expect":"Rejected.","expectedCode":"E-ALLOC-QUANTITY-CHARACTER-MISSING"},
  {"target":"EM-WRK-05-profile","id":"stock-and-share-summed","kind":"negative","input":"100 GPU-hours and a 0.6 FTE share are added into one load figure.","expect":"Rejected; the total is undefined, neither a conflict nor a pass.","expectedCode":"E-QUANTITY-CHARACTER-MISMATCH"},
  {"target":"EM-WRK-05-profile","id":"share-with-capacity-basis","kind":"positive","input":"A 0.6 share allocation records the absolute amount in the pool unit plus capacityBasis naming the pool version, interval and aggregation window.","expect":"The allocation remains evaluable and reproducible after a later pool version changes effective capacity."},
  {"target":"EM-WRK-05-profile","id":"share-without-capacity-basis","kind":"negative","input":"A 0.6 share is stored with no capacityBasis and is re-evaluated against a later pool version.","expect":"Rejected.","expectedCode":"E-ALLOC-SHARE-BASIS-MISSING"},
  {"target":"EM-WRK-05-profile","id":"window-aggregate-conflict","kind":"detection","input":"In S1, SPEC-1 holds 0.6 and 0.5 of effective capacity inside one declared weekly aggregation window.","expect":"A window-aggregate conflict is raised in S1 only; both allocations are retained and no master is written."},
  {"target":"EM-WRK-05-profile","id":"interval-shift-within-window","kind":"negative","input":"Shifting one specialist interval inside the same weekly aggregation window is reported as clearing the 1.1 overrun.","expect":"Rejected; the window total is unchanged.","expectedCode":"E-CONFLICT-WINDOW-UNCHANGED"},
  {"target":"EM-WRK-05-profile","id":"s2-clears-both-conflicts","kind":"positive","input":"S2 moves the specialist interval into a different weekly aggregation window and removes the GPU-1 overlap.","expect":"The window-aggregate conflict and the exclusivity conflict both clear; S1 is unchanged; no WM-PER-001, WM-ORG-016 or WM-OBJ-001 record changes."},
  {"target":"EM-WRK-05-profile","id":"member-level-evaluation-skipped","kind":"negative","input":"Conflict detection evaluates the pool aggregate only and reports the scenario clear while two exclusive confirmations overlap on GPU-1.","expect":"Rejected.","expectedCode":"E-CONFLICT-MEMBER-LEVEL-SKIPPED"},
  {"target":"EM-WRK-05-profile","id":"aggregate-within-member-breached","kind":"detection","input":"Aggregate GPU-hours sit within pool capacity while GPU-1's exclusivity is breached by overlapping confirmations.","expect":"A member-level exclusivity conflict is raised even though the aggregate passes."},
  {"target":"EM-WRK-05-profile","id":"duration-kind-missing","kind":"negative","input":"An interval duration is used in a capacity computation with no durationKind of elapsed, working or effort.","expect":"Rejected.","expectedCode":"E-TIME-DURATION-KIND-MISSING"},
  {"target":"EM-WRK-05-profile","id":"dst-gap-resolved","kind":"positive","input":"An allocation interval starts inside a DST gap.","expect":"Resolution follows the declared dstPolicy and the expanding calendar and tzdbRelease are named in the result."},
  {"target":"EM-WRK-05-profile","id":"recurrence-expander-undeclared","kind":"negative","input":"Recurring capacity is expanded without naming the expanding calendar and tzdbRelease.","expect":"Rejected.","expectedCode":"E-TIME-EXPANDER-UNDECLARED"},
  {"target":"EM-WRK-05-profile","id":"overlap-zone-assumed","kind":"negative","input":"Non-overlap established in one time zone is assumed in another.","expect":"Rejected.","expectedCode":"E-TIME-ZONE-ASSUMED"},
  {"target":"EM-WRK-05-profile","id":"scenarios-summed","kind":"negative","input":"Load from S1 and S2 is added into one figure.","expect":"Rejected.","expectedCode":"E-SCENARIO-SUMMATION"},
  {"target":"EM-WRK-05-profile","id":"above-100-across-scenarios","kind":"positive","input":"SPEC-1 holds 60 percent in S1 and 50 percent in S2.","expect":"No conflict; the scenarios are alternatives and are never combined."},
  {"target":"EM-WRK-05-profile","id":"released-scenario-edited","kind":"negative","input":"A released scenario is edited in place to add an allocation.","expect":"Rejected; change requires a new release.","expectedCode":"E-SCENARIO-RELEASED-MUTATION"},
  {"target":"EM-WRK-05-profile","id":"baseline-without-decision","kind":"negative","input":"A scenario is marked baseline with no authorized baselineDecisionRef.","expect":"Rejected.","expectedCode":"E-SCENARIO-BASELINE-DECISION-MISSING"},
  {"target":"EM-WRK-05-profile","id":"plan-revision-rebase","kind":"positive","input":"WM-ACT-008 issues a new plan revision after a baseline scenario was selected.","expect":"Scenarios are rebased only by explicit new releases; prior scenarios and the prior baseline remain resolvable and correctly bound to their original revision."},
  {"target":"EM-WRK-05-profile","id":"scenario-rebound-silently","kind":"negative","input":"An existing scenario is re-pointed to a new plan revision without a new release.","expect":"Rejected.","expectedCode":"E-SCENARIO-REVISION-REBIND"},
  {"target":"EM-WRK-05-profile","id":"actual-rewrites-baseline","kind":"negative","input":"WM-FLW-015 actual consumption updates the baseline scenario's allocated quantities.","expect":"Rejected.","expectedCode":"E-PROFILE-ACTUAL-REWRITES-PLAN"},
  {"target":"EM-WRK-05-profile","id":"variance-cites-both-revisions","kind":"positive","input":"Variance is reported between plan and actual.","expect":"The report cites the immutable scenario release and the immutable WM-FLW-015 consumption record; neither is rewritten."},
  {"target":"EM-WRK-05-profile","id":"plan-as-performance","kind":"negative","input":"A feasible scenario is treated as evidence that the work was scheduled, assigned or performed.","expect":"Rejected.","expectedCode":"E-PROFILE-PLAN-AS-FACT"},
  {"target":"EM-WRK-05-profile","id":"demand-pool-linkage-undeclared","kind":"negative","input":"An allocation links a demand to a pool while the profile declares no demand-to-pool linkage rule.","expect":"Rejected.","expectedCode":"E-PROFILE-LINKAGE-UNDECLARED"},
  {"target":"EM-WRK-05-profile","id":"policy-coverage-gap","kind":"negative","input":"A declared invariant has no fixture, or a negative fixture carries no expectedCode, and validation still passes.","expect":"Rejected.","expectedCode":"E-POLICY-COVERAGE-GAP"},
  {"target":"EM-WRK-05-profile","id":"fixture-polarity-mislabelled","kind":"negative","input":"A case whose expectation is a successfully raised conflict is labelled kind=negative.","expect":"Rejected; successful detection is kind=detection, not negative.","expectedCode":"E-FIXTURE-POLARITY-MISLABELLED"},
  {"target":"EM-WRK-05-profile","id":"undecidable-expectation","kind":"negative","input":"A fixture expectation references consolidated conflict checks or evaluated separately with no defined scope or outcome.","expect":"Rejected.","expectedCode":"E-FIXTURE-EXPECTATION-UNDECIDABLE"},
  {"target":"EM-WRK-05-profile","id":"stale-holds-after-freeze","kind":"negative","input":"A bundle still holds that independent Grok review and a frozen semantic audit are pending after both are complete.","expect":"Rejected.","expectedCode":"E-HOLD-STALE"}
]
```

---

## 5. Identifier decision

**No identifier is allocated, requested, derived or invented by this audit.**

- **Resource Demand** — identity confirmed independent; `modelId: null`, `registryId: null`, `allocationState: "unassigned"`, `canonicalPublishable: false`. Unchanged.
- **Resource Pool** — identity confirmed independent; `modelId: null`, `registryId: null`, `allocationState: "unassigned"`, `canonicalPublishable: false`. Unchanged.
- **Capacity Plan** — **no root, no identifier.** Profile of WM-ACT-008; identity, revision, baseline and change history remain WM-ACT-008's.
- **AllocationScenario** — **no root, no identifier.** Plan-owned immutable release, keyed within the WM-ACT-008 revision it pins.
- **ResourceAllocation** — **no root, no identifier.** Scenario-owned assertion, keyed within its scenario release; it cannot outlive or contradict that scenario.
- **`EM-WRK-05-profile`** is a contour-local artifact label, not a registry identifier, and must not be treated as one.
- No relation rows are approved. Reused bases (WM-ORG-016, WM-ECO-012, WM-PER-001, WM-OBJ-001, WM-XCT-009, WM-ACT-008, WM-FLW-015) are referenced only; none is mutated, renamed or re-scoped by this audit. **No installability or publication-readiness claim is made.**

**Holds carried forward unchanged, not counted as defects:** registry allocation for both roots; narrowing WM-ACT-008's resource-assignment/contention scope away from cross-plan contention; the WM-FLW-015 forecast-consumption versus capacity-commitment split; WM-ORG-016's missing canonical FTE/headcount grounding; canonical governance of the unit registry and quantity-kind taxonomy; unapproved relation rows; non-canonical, source and provider holds on reused bases; package conversion and live verification. Where grok lists a blocker that is in fact a missing **field or rule** rather than missing governance — overbooking-policy attribute, the quantity-kind join, calendar-tied reservation expiry, and the allocation-to-assignment binding — it is counted above as D7/D11, D6, D13 and D14 respectively, and is fixable without any registry action.

---

## 6. Freeze decision

**Closed. No rerun.**

This was the single frozen semantic audit for EM-WRK-05 and it is now spent. The verdict is REVISE: defects D1–D25 and fixes F1–F25 are applied, and the fixture array in §4 is merged into the two existing fixture files and the new profile fixture file, **without a further audit pass**. Re-auditing is not available; the fixes are bounded, evidence-cited and self-checking via the fixtures, and conformance is thereafter a validation-policy matter, not a semantic-audit matter.

Two conditions must be recorded with the freeze, because they are not satisfiable by the fixes alone:
1. **EM-WRK-05 is not acceptance-passing until the `EM-WRK-05-profile` artifact exists (F23).** The contour's acceptance narrative is currently borne by unspecified objects and, as D16 shows, is arithmetically wrong as written. The corrected narrative in fixture `s2-clears-both-conflicts` replaces it.
2. **No publication, installability or canonical-readiness claim attaches to this freeze.** Both roots stay unassigned and unpublishable until their registry holds clear by separate process.
