# EM-LEG-06 — Independent enterprise metamodel review

## Verdict

**PROFILE + one new aggregate.** Allocate exactly one new identity — `ProcessingActivity` — as the accountability anchor Art 30 requires. Everything else reuses:

- `DataSubjectRequest` → profile of **WM-ACT-021** (conditional; see Holds).
- `Purpose` → dependent statement (governed taxonomy term + assertion edge). No identity.
- `ProcessingBasis` → dependent, attributable, time-qualified assertion. No identity.
- `RetentionRule` → policy (**WM-KNW-012**), instantiated as duties (**WM-XCT-029**) and per-object assignments (**WM-DAT-001**, **WM-REC-001**, **WM-XCT-002**). No identity.

ROPA is a projection of the activity, not an object.

## Evidence

WM-XCT-002 owns the consent *instrument*: grantor/grantee, scope clauses, purpose codes, data categories, lifecycle, withdrawal propagation, decision surface. It explicitly declines to adjudicate non-consent bases and its retention finding covers **the instrument and its evidence only** — not processed payload. WM-XCT-003 owns *shape* and disclaims purpose, lawfulness, evaluation and instance data; its delete clause states a subject-erasure request never acts on its records.

Neither carries: processing operations, controller/processor roles, activity-level purpose, or erasure determination. Art 30 is cited in WM-XCT-002's sources but appears in no finding, and no coverage dimension names it. That absence is real, not an artefact of scope.

## Identity/mastership

Five planes, five masters, no inference between them:

| Plane | Master |
|---|---|
| Norm / provision | WM-POL-001 |
| Internal normative statement | WM-KNW-012 |
| Instantiated duty | WM-XCT-029 |
| Permission instrument | WM-XCT-002 |
| Output shape | WM-XCT-003 |

Payload execution: WM-DAT-001 (dataset), WM-REC-001 (record), WM-DAT-004 (schema-level personal-data flags). Data subject: WM-PER-001. The new activity aggregate holds **no** instrument, shape, payload, audit trail or enforcement.

## Processing activity

Yes — missing. It is the only unit spanning systems, datasets, purposes, recipients and retention rules, and the only place where "this purpose has no basis" is detectable. Its lifecycle is independent of any dataset version or grant.

Narrow it to: activity identity and lifecycle; declared purpose set; role declarations per party per purpose; basis assertions per purpose; typed references to systems, datasets, recipients, transfers and retention rules; and an **erasure-determination series**. It owns nothing it references.

## Purpose and basis

Purpose is a coded taxonomy term (DPV/DUO-aligned) asserted *by* an activity, carrying text, code, taxonomy version and granularity. A storage system is an asset reference on a different plane — purpose is never derivable from where data sits, and colocation in one store never merges two purposes. This is the contour's first question answered structurally, not by convention.

Basis is a separate assertion: purpose → basis code → cited provision → asserting role → effective time → assessment reference (balancing test where legitimate interest). WM-XCT-002 can carry a declared basis on a grant; it cannot adjudicate one, so the assertion lives on the activity.

**Purpose limitation downstream:** derived datasets inherit a *purpose ceiling* — the meet of their inputs' purposes — widened only by a recorded compatibility assessment under a named authority. This mirrors WM-XCT-003's subsumption/meet algebra but must be located on the activity; WM-XCT-003 stays shape-only.

## Consent

Consent is one basis, never the universal one — WM-XCT-002 already rejected consent-as-gate adversarially, and its recorded GDPR Art 7(3) conflict fixes withdrawal as forward-only. Use consent where WM-XCT-002's four validity elements are genuinely satisfiable and freely refusable; otherwise cite contract, legal obligation, vital interests, public task or legitimate interests, and record the assessment.

Withdrawal terminates grants whose **declared basis is consent**. It does not reach processing under another basis, does not retroact, and cannot defeat a statutory retention floor.

## Data-subject request

Profile of WM-ACT-021. That model already supplies everything a DSR needs: requester vs submitter vs represented party; intake channel and times; triage accept/reject/redirect; assignment; state with pending/blocking conditions; SLA KPI with target, clock, **pause** and breach; evidence and communication bindings; outcome; closure; reopen/appeal; privacy projection; retention, hold and tombstone.

Profile adds only: statutory deadline and extension semantics; identity-verification as a clock-pausing condition; a **per-location outcome vector** rather than one global verdict; refusal grounds cited per location.

**Conflict:** WM-PER-001 already declares `subject-rights-execution` with its own case-file artifact and function. Demote it to a reference — the person record points at the case; it must not case-manage.

## Retention and erasure

Erasure is five acts, not one:

1. **Resolve locations** — activity references yield dataset, record, instrument and recipient targets.
2. **Determine per location** — evaluate retention floor and hold state separately (a floor prevents early disposition; a hold suspends disposition).
3. **Execute** — destroy, de-identify, or suppress-and-retain-under-obligation.
4. **Prove** — tombstone (identifier, class, disposal time, authority), integrity digest over the canonical form, disposition certificate naming method and authoriser. The digest proves prior existence and content-identity **without retaining content**; this pattern is already consistent across WM-REC-001, WM-DAT-001 and WM-XCT-002.
5. **Propagate** — WM-XCT-002 propagation ledger to recipients; invalidation signals to compiled templates.

Where retention wins, the surviving data is **repurposed narrowly**: restricted to the obligation's purpose, unavailable to the original purpose, with a computed expiry that later triggers destruction.

## Projection and analytics

A projection may narrow shape freely but may never widen purpose: its declared purpose must be subsumed by the activity's. Bind the projection's applicability condition to the **basis assertion**, not to a consent grant — otherwise a legitimate-interest analytics view inherits a consent lifecycle it does not have.

Aggregate-only projections set `microdata_permitted = false` and carry a WM-XCT-005 cohort-floor reference. Subject removal changes cohort membership, so release-set linkability and floor satisfaction must be re-evaluated, not assumed stable.

## Roles and parties

Controller and processor are **role assertions on the activity, per party, per purpose** — one party can be controller for one purpose and processor for another within the same activity. WM-XCT-002's party-functional-roles (grantor, grantee, subject, manager, enforcer) are access roles and do not substitute. Beneficiary, recipient category and onward sub-processor come from WM-XCT-002's grantee-designation; DPO and accountable steward from the party master.

## Scenario

Erasure request → DSR case; identity verification pauses the clock. Activity resolves four locations. **Marketing dataset:** no competing obligation → payload destroyed, tombstone plus deletion evidence retained. **Accounting ledger:** statutory retention duty (WM-XCT-029 citing WM-POL-001) → payload suppressed from active use, restricted to the compliance purpose, expiry computed. **Analytics aggregate:** no microdata present; projection survives, floor re-checked. **Consent instrument:** terminated; evidence minimised; integrity manifest and tombstone retained to demonstrate the act. Case closes as *partially granted*, with per-location reasons. The negative case — withdrawal deleting accounting history — fails at step 2 and is correctly refused.

## Invariants

1. Every operation resolves to one activity and ≥1 purpose; a purpose without a basis assertion blocks activation.
2. Purpose and basis are separately asserted and separately attributable; neither is inferable from the other.
3. Consent is a basis, never a precondition; withdrawal is forward-only and basis-scoped.
4. A derived dataset's purpose ceiling is the meet of its inputs', widened only by recorded assessment.
5. A projection never widens the permitted purpose.
6. Erasure has a scope, a per-location determination and a confirmation.
7. Destruction leaves a tombstone and a non-reversible digest; proof never retains payload.
8. Retained-under-obligation data is restricted to the obligation's purpose.
9. Retention floor and legal hold are distinct and each names a precedence owner.
10. No model asserts lawfulness; assertions carry authority, assessment and limits.
11. Event, effective and record time stay separate on every determination.

## Minimal completion shape

One aggregate (ProcessingActivity). One profile (DSR over WM-ACT-021). Reuse bindings pinned by version and digest: WM-XCT-002 (instruments only), WM-XCT-003 (shape only), WM-KNW-012 + WM-XCT-029 (rules and duties). References: WM-DAT-001/004, WM-REC-001, WM-PER-001. Bind — do not mint — a purpose taxonomy and a processing-operation vocabulary.

## Holds

Both bases are `publishableCanonical: false`, `adjudicationStatus: reviewable-draft`; no canonical release is possible on them. WM-XCT-002: unpinned FHIR URL, conflicting DPVCG citations, paywalled ISO 27560/29184 (field claims mapping-derived), security dimension a declared gap, single non-EU profile untested. WM-XCT-003: 14 unverified sources, no multi-grain validation, US/EEA-only evidence, and an **unresolved legal-hold precedence conflict across WM-XCT-004 / WM-DAT-004 / WM-KNW-012** that directly blocks the erasure determination. WM-ACT-021: single-provider waiver, no approved relation-ledger edges. Unowned: Art 32 technical measures; processing-operation vocabulary. WM-PER-001 boundary overlap unresolved.

This is not legal advice, claims no canonical completeness, and asserts no installability.
