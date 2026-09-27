# EM-LEG-06 local synthesis

## Disposition

- Propose one identifier-unassigned independent **Processing Activity / Processing Register Entry** aggregate. It is the accountability root spanning purposes, operations, controller/processor roles, datasets, systems, recipients, transfers and retention assignments.
- Profile WM-ACT-021 Service Case for Data Subject Request. It already owns requester/representative, intake, verification blockers, SLA clock, evidence, communications, outcome, appeal, retention and tombstone semantics.
- Treat Purpose and Processing Basis as separate attributable dependent assertions of the activity. Consent is one possible basis represented by WM-XCT-002, never a universal prerequisite.
- Represent Retention Rule through WM-KNW-012 policy, instantiate duties through WM-XCT-029 and bind them to datasets/records/instruments. WM-XCT-003 remains output-shape authority.
- A ROPA is a projection of the processing activity, not another aggregate. Allocate no identifier before registry adjudication.

## Identity and mastership

WM-POL-001 owns source norms, WM-KNW-012 internal rules, WM-XCT-029 instantiated duties, WM-XCT-002 permission/consent instruments and WM-XCT-003 disclosure shapes. WM-DAT-001 and WM-REC-001 own payload datasets and records; WM-DAT-004 owns schema semantics; WM-PER-001 owns the person reference. The Processing Activity owns only its accountability identity, lifecycle and bindings.

The activity has a lifecycle independent of any dataset, system, consent grant or report version. One purpose without an accepted basis blocks activation and remains explicitly unresolved.

## Purpose, basis and consent

Purpose is a governed taxonomy term plus activity assertion carrying wording, taxonomy version and granularity. Storage system and dataset are asset references and cannot imply purpose. Colocation does not merge purposes.

Processing Basis is a separate time-qualified assertion linking purpose, basis class, cited provision, asserting role, assessment and effective interval. WM-XCT-002 may carry consent or a declared access basis but does not adjudicate non-consent lawfulness.

Consent withdrawal terminates only instruments whose declared basis is consent, prospectively from its effective time. It does not erase processing supported by a different basis or defeat a statutory retention duty.

## Data Subject Request profile

The WM-ACT-021 profile adds statutory deadline/extension semantics, identity verification as a clock-pausing condition, per-location outcomes and location-specific refusal grounds. The request case references the person; WM-PER-001 must not duplicate case management.

A single request can be partially granted. Each target location records resolution, determination, execution, evidence, propagation and appealability independently.

## Retention and erasure

Erasure proceeds through target discovery, per-location determination, execution, proof and downstream propagation. A retention floor prevents early disposition; a legal hold temporarily suspends disposition. They remain distinct and identify their authority and precedence owner.

Execution can destroy, de-identify or suppress-and-retain under obligation. Retained data is restricted to the obligation purpose and assigned a future expiry. Proof retains a tombstone, disposition method, authority, event time and non-reversible integrity digest, never the erased payload.

## Projection and analytics

Derived datasets inherit a purpose ceiling equal to the intersection of input purposes unless an authorized compatibility assessment records a widening. WM-XCT-003 can only narrow disclosure shape; its purpose binding must remain within the activity's permitted purpose.

Aggregate analytics projections set microdata permission false and reference cohort-floor/privacy controls. Erasure changes cohort membership, so floor satisfaction and cross-release linkability are re-evaluated.

## Roles and parties

Controller, joint controller and processor are time-qualified role assertions per party, activity and purpose. The same party can hold different roles for different purposes. These roles do not collapse into WM-XCT-002 grantor/grantee/access roles. Recipients and subprocessors remain explicit references.

## Acceptance scenario

An erasure request opens a DSR case and identity verification pauses its clock. The marketing dataset is destroyed and leaves a tombstone. Accounting records remain suppressed from ordinary use under a statutory duty, restricted to compliance purpose and scheduled for later destruction. A minimal aggregate analytics projection survives only after its cohort floor and linkability are rechecked. The consent instrument is terminated and its minimized evidence retained. The case closes partially granted with reasons per location.

## Invariants

1. Every processing operation resolves to an activity and at least one declared purpose.
2. Purpose and basis are separate attributable assertions.
3. A system, dataset or storage location never implies purpose.
4. Consent is one basis and withdrawal is prospective and basis-scoped.
5. A projection never widens permitted purpose.
6. Derived data preserves an explicit purpose ceiling.
7. Every erasure request has scope, per-location determination and confirmation.
8. Erasure proof never retains erased payload.
9. Retention floor and legal hold remain distinct.
10. Retained-under-obligation data is restricted to the obligation purpose.
11. Controller and processor roles are scoped by activity, purpose and interval.
12. Event, effective and record time remain distinct.
13. No model silently asserts legal compliance or lawfulness.

## Holds

Processing Activity has no allocated identifier. WM-XCT-002, WM-XCT-003 and WM-ACT-021 remain non-canonical drafts; relationship, source-pin and fixture gaps persist. Legal-hold precedence conflicts across adjacent models directly block executable erasure semantics. WM-PER-001 overlaps request execution, and processing-operation vocabulary plus technical-measures coverage remain unowned. Jurisdiction-specific profiles require specialist review. This checkpoint makes no legal, canonical or publication-readiness claim.
