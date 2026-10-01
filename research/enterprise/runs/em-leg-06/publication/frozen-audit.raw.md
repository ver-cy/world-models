# Frozen audit — EM-LEG-06

## Verdict

**Proceed, but not to allocation adjudication yet.** The boundary judgment is sound and I would sustain it: Processing Activity is an independent accountability aggregate, DSR is correctly a WM-ACT-021 profile, Purpose and Basis are correctly separated, ROPA is correctly a projection, and the erasure-proof shape is correctly payload-free in intent. The defects are not boundary defects — they are (a) one unreconciled rule that the three artifacts state three different ways, (b) four invariants the candidate asserts but its object model cannot express, and (c) a fixture set that tests only the allocation candidate and leaves the profile untested. The checkpoint's own claim of no legal, canonical or publication-readiness status is consistent with the evidence and should stand.

## Material defects

**D1 — The purpose-widening rule contradicts itself across the three artifacts.** The comparison records adoption of the stricter rule (widening requires a separately governed activity). The synthesis (*Projection and analytics*) still says "unless an authorized compatibility assessment records a widening," and fixture `derived-purpose-ceiling` still *expects* that widening. The candidate's invariant is silent either way, so the fixture currently encodes the rejected rule. *Smallest fix:* delete the compatibility-assessment clause from the synthesis and from the fixture expectation; make the candidate invariant read that a derived dataset's ceiling is the intersection of input ceilings and can only be preserved or narrowed.

**D2 — Suppress-and-retain violates the rule adopted in D1.** Compliance/obligation purpose is not inside the original activity's ceiling, yet `partial-erasure` keeps retained accounting records inside the same case outcome "with separate bases." *Smallest fix:* require a suppress-and-retain outcome to bind retained data to a distinct compliance-purpose activity revision with its own purpose assertion, basis assertion and expiry, referenced from the case outcome.

**D3 — No RoleAssertion object exists.** The invariant requires roles scoped by activity, purpose and interval, but roles appear only as `controllerRoleRefs` (on the activity root — neither purpose-scoped nor revisioned) and `processorRoleRefs`. Fixture `role-by-purpose` cannot be evaluated against this schema. *Smallest fix:* define `RoleAssertion{roleAssertionId; partyRef, roleClass, purposeAssertionRef, effectiveFrom; opt effectiveTo, supersedesRef}` and move all role refs onto the revision.

**D4 — The temporal invariant has no carrier.** "Event, effective and record times remain distinct" is asserted, but no object holds a record/transaction time; revisions carry only `effectiveFrom`/`effectiveTo`. *Smallest fix:* add required `recordedAt` to revision, purpose, basis, role and disposition records, plus `eventTime` where an event is recorded.

**D5 — "Accepted basis" is undefined, so the activation block is unenforceable.** `ProcessingBasisAssertion` has no acceptance state, and the lifecycle's `assessed`/`approved`/`active` steps are not mapped to it. *Smallest fix:* add required `acceptanceState` (proposed | accepted | rejected | withdrawn) and state that a revision cannot enter `active` while any of its purpose assertions lacks an accepted basis over the same interval.

**D6 — Consent withdrawal is unresolvable.** Nothing links a basis assertion to the WM-XCT-002 instrument, so a withdrawal cannot identify which assertions it terminates. The synthesis also conflates the two ("withdrawal terminates instruments whose declared basis is consent" — an instrument has no basis; the assertion cites the instrument). *Smallest fix:* add `instrumentRef`, required when `basisClass` is consent; withdrawal sets `effectiveTo` and never deletes.

**D7 — "Location" is undefined in every artifact** although per-location determination is the core DSR mechanic and the comparison names location ownership as an audit target. The revision carries `datasetRefs` and `systemRefs`; neither is a location. *Smallest fix:* define the erasure target as a resolvable tuple (datasetRef + systemRef + optional recordSetRef), state that the activity supplies the bindings and WM-ACT-021 records one outcome per resolved tuple.

**D8 — Retention floor, legal hold and precedence are unmodeled** while the synthesis states that the precedence conflict *blocks* executable erasure. The invariant asserts distinctness only; `retentionAssignments` has no defined shape and nothing carries authority or precedence owner. *Smallest fix:* define `RetentionAssignment` and `Hold` with required `authorityRef`, `constraintKind` (floor | suspension) and `precedenceOwner`; demote the unresolved cross-model precedence from invariant to an explicit blocking hold.

**D9 — Tombstone mastership is ambiguous.** The profile gives WM-ACT-021 "retention and tombstone semantics"; the synthesis gives record mastership to WM-DAT-001/WM-REC-001. A tombstone must outlive both the record and the case, so case-owned tombstones expire with case retention. *Smallest fix:* master the durable tombstone with the dataset/record owner, have the case reference it, and state that tombstone retention is independent of case retention.

**D10 — Digest coverage is undefined, so the proof can leak.** "Non-reversible integrity digest" names no input; a digest over erased payload is a verification oracle and a derived identifier, defeating invariant 8 in effect. *Smallest fix:* state that the digest covers the disposition record only (target tuple id, method, authority, event time); if any subject-derived input is included, require a keyed digest whose key is outside the proof.

**D11 — Unsupported and dangling references.** `WM-ACT-034` appears only in the profile `bases`, with no purpose, constraint or mention in any other artifact. Conversely `provisionRef` and retention bindings have no declared referent: WM-POL-001 and WM-REC-001 are in the synthesis and profile bases but absent from `boundary.references`. `purposeTerm`/`taxonomyVersion` dangle — no model owns the purpose taxonomy. ROPA edition identity is excluded from the aggregate and assigned to nothing. *Smallest fix:* remove WM-ACT-034 or state its role; add WM-POL-001 and WM-REC-001 references; record purpose-taxonomy and ROPA-edition mastership as explicit unowned holds.

**D12 — Two sources of truth for the in-force revision.** `currentRevisionRef` and the revision effective interval can disagree, and no non-overlap rule exists. *Smallest fix:* declare `currentRevisionRef` derived from the interval containing now and add a non-overlap constraint on revision intervals.

**D13 — Stale holds in a frozen checkpoint.** Both JSON candidates still hold "Independent Grok review is pending" although the comparison records the completed reconciliation; the profile omits the WM-PER-001 overlap hold the candidate carries. *Smallest fix:* replace the Grok hold with the reconciliation outcome and make the hold sets identical across all three artifacts.

**D14 — The base profile asserts jurisdiction-specific law.** "Statutory deadline/extension semantics" and verification as a clock-pausing condition are jurisdictional, which contradicts invariant 13 and the open jurisdiction-profile hold. *Smallest fix:* parameterize pause and extension per jurisdiction profile with default "no pause," and mark deadline fields as profile-supplied.

**D15 — Coverage: the profile has zero fixtures,** and the acceptance scenario's aggregate controls (microdata permission false, cohort floor, linkability recheck) and downstream cascade appear in no invariant, constraint or fixture; privacy-control and derivation-lineage ownership are unassigned. *Smallest fix:* emit a separate profile fixture file, add the cases below, and record cohort-control and derivation-lineage mastership as holds.

## Exact additional fixtures required

Amend one existing case: `derived-purpose-ceiling` — expectation becomes "ceiling is the intersection; no widening is representable."

Add to the allocation-candidate fixtures:

1. `analytics-widening-new-activity` / positive — a wider analytics purpose is requested → accepted only as a new activity with its own purpose and basis; the source activity is unchanged.
2. `purpose-without-accepted-basis` / negative — revision with a purpose whose basis is `proposed` → activation rejected, purpose remains explicitly unresolved.
3. `multi-basis-conflict` / positive — one purpose carries consent and a statutory basis over overlapping intervals → both persist as separate assertions; withdrawal of consent leaves the statutory basis in force.
4. `role-interval-overlap` / negative — two controller assertions for the same party, activity and purpose with overlapping intervals and no supersession → rejected.
5. `joint-controller-by-purpose` / positive — two parties joint controllers for P1, one sole controller for P2 → coexisting purpose-scoped assertions.
6. `temporal-distinctness` / positive — revision recorded after its effective start with a distinct event time → all three times retained and queryable independently.
7. `revision-interval-overlap` / negative — two revisions in force at the same instant → rejected.
8. `identifier-recycling` / negative — a retired activity's id or revision number is reused → rejected.
9. `hold-and-floor-distinct` / positive — a statutory floor and a legal hold apply to one target → both recorded with separate authority and constraint kind; neither is collapsed.
10. `unresolved-precedence-refuses` / negative — floor and hold prescribe conflicting disposition and no precedence owner is resolvable → execution refused, not guessed.
11. `projection-narrows-only` / positive — a WM-XCT-003 shape narrows fields within the permitted purpose → accepted; the same shape bound to a purpose outside the ceiling → rejected.
12. `unsupported-model-reference` / negative — a candidate cites a model with no declared purpose or mastership → rejected.
13. `ropa-edition-unowned` / negative — the activity claims ROPA edition identity → rejected; mastership remains an open hold.

Add as profile fixtures (WM-ACT-021 Data Subject Request):

14. `location-tuple-resolution` / positive — a request resolves to three target tuples across two systems → one determination, execution, evidence and appealability record per tuple.
15. `partial-closure-semantics` / positive — case closes partially granted → closure implies neither that every location erased nor that the activity is retired.
16. `verification-pause-requires-jurisdiction` / negative — base profile pauses the clock with no jurisdiction parameter → rejected; default is no pause.
17. `suppress-and-retain-binds-new-activity` / positive — accounting records suppressed under statutory duty → bound to a distinct compliance-purpose activity with its own basis and future expiry.
18. `tombstone-outlives-case` / positive — the case reaches its own retention expiry → the tombstone, method, authority, event time and digest survive.
19. `digest-covers-disposition-record` / negative — the digest input includes erased payload → rejected unless keyed with the key outside the proof.
20. `cascade-propagation` / positive — an erased record feeds a derived dataset → propagation obligation raised against the derived target and its determination recorded.
21. `cohort-floor-recheck` / positive — erasure changes cohort membership → floor satisfaction and cross-release linkability re-evaluated before the projection survives.
22. `microdata-in-aggregate-projection` / negative — an aggregate projection sets microdata permission true → rejected.
23. `withdrawal-scoped-to-instrument` / positive — withdrawal of instrument A leaves basis assertions citing instrument B in force, prospectively only.

This is the frozen audit; I am not requesting a second one.
