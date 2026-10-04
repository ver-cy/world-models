# EM-OPS-03 frozen semantic audit prompt

You are the sole final Claude Opus high no-tools auditor. This is exactly one frozen audit after an independent Claude study, local synthesis, and the exact visible Grok response. Do not browse, use tools, invent identifiers, claim publication readiness, or request another study.

Admitted evidence is limited to the initial Claude study, local synthesis, exact visible Grok response, and candidate artifacts appended below. Grok disclosed team coordination and exposed a sources control despite the instruction not to browse; hidden reasoning and sources are excluded. The visible response is complete and admitted as text only.

Audit the settled boundary and artifacts:

- Asset Instance profiles WM-OBJ-001 and mints no parallel physical identity.
- Custody is an effective-dated, independently identified relationship record within the WM-OBJ-001 boundary; it does not require a new model/runtime identifier and implies neither title, responsibility, location nor access.
- WM-ECO-011 is an aligned holding view only; WM-OBJ-022 is a projection only.
- WM-ACT-007 authorizes work but never proves execution.
- Maintenance Plan, Maintenance Event and Calibration Event are independent identifier-unassigned roots.
- Operational Responsibility Assignment reuses the identifier-unassigned candidate from EM-LND-17.
- WM-OBJ-023 is the reserved measuring-instrument/configuration boundary and remains a completion dependency, not a new EM-OPS-03 allocation.
- Component replacement follows a pinned identity-continuity rule and never transfers calibration.
- Calibration binds one instrument/configuration to pinned method, references, traceability, range, results, uncertainty, decision rule, certificate and validity conditions.
- Fitness is derived for a stated purpose and never propagated by instrument class/model.
- No runtime or model identifier is allocated.

Return:

1. Verdict on decision and artifacts.
2. Numbered material defects, each with exact deterministic remediation.
3. A single exact JSON array of additional fixtures. Every fixture must contain id, target, kind, input, expect, violates, closesDefect; every negative must also contain expectedCode.
4. Exact final counts for prior, additional, and total fixtures, split into positive and negative.
5. Freeze decision. Do not ask for or perform a rerun.


## INITIAL CLAUDE STUDY

# Verdict

Decide EM-OPS-03 as **reuse-and-profile with three identifier-unassigned candidates**. No new physical-identity master. `AssetInstance` and `Custody` are profiles over `WM-OBJ-001`; the accounted asset view is `WM-OBJ-022` projected over it; instrument semantics are `WM-OBJ-023`. `MaintenancePlan`, `MaintenanceEvent` and `CalibrationEvent` need independent identity and lifecycle that no frozen spec supplies, and are raised as candidates without identifiers, pending registry reservation and boundary review. `WM-ECO-011` is admitted only as an economic/holding view, not as enterprise title master. The negative case is rejected. Boundary decision: `pending → reuse/extend` locally; nothing here is canonical or installable.

# Evidence

Both target models are `conceptual-candidate` at `index-and-publication-metadata` depth, `migration-boundary-review`, and `published` does not mean independently reviewed. `WM-ACT-007` is present in full but `publishableCanonical: false`, Codex-only under single-provider-waiver with Claude and Grok waived, and carries an explicit absence-of-external-review hold. `WM-OBJ-001`, `WM-ACT-034` and `WM-MAT-008` are likewise reviewable drafts; `WM-MAT-008` never read the published OMS/ISO 19156 requirements classes and holds every cardinality claim. For `WM-ECO-011` only the legacy B11 document is in the dossier — no spec, no crosswalk. `WM-ACT-013` and `WM-ACT-007` share one legacy alias and one spec path (`K11`), an unresolved duplication. Relations are `candidate` only; reservation relation fields are empty for most entries.

# Identity/mastership

`WM-OBJ-001` masters physical identity: instance identifiers and issuing scheme, marks and carriers, resolution and collisions, condition assessment, whereabouts, custody, lifecycle state including exceptional loss/theft, event stream and record governance. `asset_tag`, `asset_kind`, `condition`, `criticality` from OPS-05 remain candidate-not-normative: `asset_tag` is an identifier under `WM-OBJ-001`'s priority ladder (master-system, then governed IRI, then Dimension UUID/ULID) and never a surrogate key; `condition` resolves to the dated assessment finding with scale, method and assessor; `criticality` is a `WM-OBJ-022` projection, refused as an instance property. `AssetInstance` therefore mints no identity. The configuration unit is not the asset: type and variant stay in `WM-OBJ-002`/`WM-OBJ-017`, as-built structure in `WM-OBJ-012`. Measuring instruments profile `WM-OBJ-023` (declared parent `WM-OBJ-008`, not supplied here — unverified).

# Asset and economic view

`WM-OBJ-022` is a `VIEW` over `WM-OBJ-001` and explicitly "no second master identity"; value, depreciation and criticality live there. `WM-ECO-011` is an `entry_kind: view-candidate` flagged "view, осторожно", and its legacy content is person-side: holder, `assetRef` into an authoritative register, acquisition, disposal, encumbrance, title evidence. That structure is usable as the *ownership/title and lease-interest* reference shape — holding, counterparty, encumbrance, effective dates, evidence snapshot — but its owner is "the person" and its stewardship model is personal. It cannot be adopted as the enterprise title master without a crosswalk that is not in the dossier. Record it as an aligned view; leave enterprise title mastership as an open gap.

# Custody and responsibility

Five layers stay separate. **Physical identity** — `WM-OBJ-001`. **Ownership/title** — external legal/economic relation (`WM-ECO-011` view, gap above); `WM-OBJ-001` explicitly refuses to master title and cites the keeper-versus-owner split. **Custody** — `WM-OBJ-001`'s custody period and transfer, at most one open period, basis of holding, acknowledgement, condition at handover; `Custody` is a profile, not a new model. **Operational responsibility** — a responsible party bound to an asset scope for a validity interval with a governing basis; EM-LND-17 already raised this as an identifier-unassigned relation candidate, so reuse that candidate rather than open a second one. **Location** — `WM-BLT-002` place identity with `WM-OBJ-001` observed fixes and containment. Possession implies neither title nor responsibility; responsibility implies neither custody nor access.

# Component replacement

`WM-OBJ-001`'s identity-continuity finding owns this, and the dossier is explicit that **no consulted source resolves continuity across component replacement or rebuild** — it is a published local policy, never a standards-backed fact. Rule: the parent instance retains identity when replacement is an evidenced repair recorded as an intervention plus an attach/detach membership period; identity terminates only through an evidenced transformation that consumes it and generates successors with derivation links. The removed component keeps its own identity and its closed membership period; the installed component opens one. Ship-of-Theseus progressive replacement must hit a declared, versioned continuity threshold rather than an implicit answer. Replacement never rewrites history, and never silently transfers the parent's calibration state to a new measuring subsystem.

# Maintenance plan/order/event

Three separable things. **Plan** — recurring rules, intervals, triggers and required resources; `scheduled_period` and `required_resources` sit here. No frozen spec masters it: `WM-ACT-007` delegates scheduling and disclaims lifecycle ownership; `WM-ACT-013` is a previous-version record duplicating the `K11` spec. Raise `MaintenancePlan` as an identifier-unassigned candidate after resolving the `K11` duplication. **Authorization** — reuse `WM-ACT-007` unchanged: identity, authority, scope, revisions, acceptance criteria, closure; a request is not an order. **Performed work** — `WM-ACT-007` states that released, dispatched or closed never proves work occurred, and performed-work evidence is external. `MaintenanceEvent` therefore requires independent identity and lifecycle. `completion_evidence` is a reference, evaluated against issued acceptance criteria. Condition evidence: `WM-MAT-008` for measured observations, `WM-ACT-034` for graded condition judgement, both referenced from `WM-OBJ-001`'s condition-assessment history.

# Calibration event and certificate

`CalibrationEvent` requires independent identity and lifecycle: `WM-MAT-008` references a calibration certificate but does not issue, renew, revoke or verify one; `WM-ACT-034` excludes calibration programmes and traceability management; `WM-OBJ-001` lists calibration status among its omissions. It is neither a plain observation nor a plain work order. Required content: subject instrument instance; method/procedure at pinned version; reference standard and reference materials in force with the traceability chain and any declared break; calibrated range and points; result values with unit code system and code; uncertainty kind, value, coverage factor and coverage probability; decision rule identifier and risk basis where a conformity statement is made; performing party with competence/accreditation reference and impartiality declaration; certificate artifact with issuer, digest and validity window. Determination, decision and attestation stay separable.

# Validity and fitness

Calibration stops confirming fitness when: the validity window expires; a declared condition is breached (shock, repair, relocation, out-of-tolerance drift, environmental excursion); the intended use falls outside the calibrated range or required uncertainty; the traceability chain is broken or the certificate digest fails; or the instrument's measuring subsystem is replaced. Fitness-for-use is a derived assessment against a stated purpose and decision rule, never a stored timeless flag on the instrument, and a certificate released without its range, uncertainty and decision rule is uninterpretable.

# Time/version/scenario

Keep event time, effective time, observation time and ingestion/record time distinct; RFC 3339 with seconds and explicit offset; date-only identity forbidden. Issued order revisions and released results are immutable and superseded, never overwritten; corrections are new statements. Planned maintenance belongs to a named plan/scenario and authorizing context; observed work and observed condition carry source, precision and confidence; divergence is an explicit exception. Every historical interval — custody, responsibility, membership, calibration validity — stays reconstructable.

# Acceptance scenario

Leased instrument: title with the lessor as an encumbered holding; custody with the enterprise; operational responsibility assigned to a named party on its own effective date; location observed. Component replacement: the measuring subsystem is detached and a successor attached; parent identity survives under the continuity rule; prior calibration ceases to confirm fitness and the instrument becomes unfit-for-use pending recalibration, without erasing the earlier certificate. Expired calibration: validity lapses, fitness evaluates negative for purposes requiring it, the open maintenance order remains due and re-resolves without proving completion. Responsibility chain and suitability history remain continuous and queryable across all three.

# Invariants

Serial belongs to the manufacturer's scheme and is not a surrogate key; repair does not change identity absent an evidenced rule; a calibration certificate has a range and a validity period. Added: at most one open custody period; responsibility assignment requires basis and interval; no conformity statement without decision rule and uncertainty; order state never proves performed work; condition requires scale, method, assessor and date; absence is coded, never zero or null.

# Minimal model set

Reuse/profile: `WM-OBJ-001`, `WM-OBJ-022`, `WM-OBJ-023`, `WM-ACT-007`, `WM-ACT-034`, `WM-MAT-008`, `WM-BLT-002`, `WM-OBJ-002`/`WM-OBJ-012`/`WM-OBJ-017`; `WM-ECO-011` as an aligned view. Identifier-unassigned candidates: MaintenancePlan, MaintenanceEvent, CalibrationEvent, plus the existing operational-responsibility relation candidate. No identifiers allocated.

# Holds

Model-level calibration is rejected: calibration binds the individual instrument as feature of interest, and class-level inference to every instance of a model contradicts `WM-OBJ-001`'s type/instance boundary and its completeness-verification conflict, and would be an unstated extrapolation under `WM-ACT-034`. Open: `WM-ECO-011` semantic crosswalk, rights and source mastership; `K11` duplication between `WM-ACT-007` and `WM-ACT-013`; enterprise title mastership; `WM-OBJ-023`'s unsupplied parent; empty relation contracts; single-provider waivers on every target. Immutable refs and fixture checks are not done. No canonical completeness and no installability claimed.



## LOCAL SYNTHESIS

# EM-OPS-03 local synthesis

## Disposition

- Reuse WM-OBJ-001 for Asset Instance and Custody. Use WM-OBJ-022 only as the economic/criticality/lifecycle projection and WM-ECO-011 only as an aligned holding view, not an enterprise title master.
- Reuse WM-ACT-007 for Work Order authorization. A closed order does not prove performed work.
- Raise **Maintenance Plan**, **Maintenance Event** and **Calibration Event** as identifier-unassigned new-model candidates. Each needs identity and lifecycle absent from the frozen bases.
- Reuse the identifier-unassigned Operational Responsibility Assignment candidate from EM-LND-17 rather than duplicating it.

## Identity and responsibility boundary

WM-OBJ-001 masters the physical instance, scheme-qualified identifiers, condition history, whereabouts, custody, lifecycle events and exceptional states. Serial number belongs to its issuer's scheme and is not a universal key. Type, configuration and as-built assembly remain separate masters.

Ownership/title, custody, operational responsibility, location and access are distinct. The legacy WM-ECO-011 person-side view can describe a holding, acquisition, disposal, encumbrance and title evidence, but does not establish enterprise title authority. Custody is an effective-dated WM-OBJ-001 profile with transfer and acknowledgement. Responsibility is a separate effective-dated relation with governing basis.

## Component replacement

An evidenced repair may preserve parent identity while closing the removed component's membership and opening the replacement component's membership. A transformation that consumes the parent ends that identity and creates linked successors. The continuity rule and any threshold are versioned local policy because the current evidence does not supply a universal rule. Component replacement never transfers calibration state silently.

## Maintenance boundary

Maintenance Plan owns recurring rules, intervals, triggers, required resources and applicability. Work Order authorizes scoped work with issued acceptance criteria. Maintenance Event records performed work, actual resources, observations, replaced components and completion evidence. These three records remain separate.

Condition measurements use WM-MAT-008; graded condition judgements use WM-ACT-034. Released, dispatched or closed order status cannot substitute for performed-work evidence.

## Calibration boundary

Calibration Event binds one instrument instance to a pinned method, reference standards/materials, traceability chain, calibrated range and points, results, units, uncertainty, conformity decision rule, performing party and certificate artifact. The certificate has issuer, digest, issue time and validity/conditions. Determination, decision and attestation remain separable.

Calibration ceases to support fitness when validity expires, a limiting condition is breached, the intended use falls outside range or uncertainty, traceability breaks, certificate integrity fails or the measuring subsystem changes. Fitness-for-use is a derived assessment for a stated purpose, never a timeless instrument property.

## Acceptance result

A leased instrument keeps title with the lessor, custody with the enterprise and operational responsibility with a named party. Replacement of its measuring subsystem preserves parent identity under the recorded continuity rule but invalidates fitness for uses dependent on the old calibration. The prior certificate remains historical evidence. When calibration expires, the instrument becomes unsuitable for the governed purpose until recalibrated; the maintenance order remains open and cannot prove execution.

The negative case fails: a successful calibration applies only to the identified instrument and calibrated configuration, range, method and validity conditions. It cannot be inherited by every instance of the same model.

## Holds

WM-ECO-011 lacks a current complete specification and semantic crosswalk. WM-ACT-007 and WM-ACT-013 have an unresolved K11 duplication. WM-OBJ-023 and the three new candidates lack complete specs/allocations; enterprise title mastership is unresolved. Existing bases remain non-canonical reviewable drafts with relation and provider holds. No new identifier or installable release is created.



## VISIBLE GROK RESPONSE

Verdict: Conditionally accept. The proposal correctly keeps title, custody, operational responsibility, location and access apart; treats WM-ECO-011 as an aligned holding view only; treats WM-OBJ-022 as a projection; treats WM-ACT-007 as authorization that never proves execution; forbids silent calibration transfer on component replacement; and rejects class-level propagation. It is not accepted as stated on Custody: Custody profiles nothing in WM-OBJ-001. Three new candidates remain identifier-unassigned and cannot be mastered by the legacy objects named below.

Strongest evidence: WM-OBJ-001 is the only physical master in the given set, so an Asset Instance can be grounded there without a second physical master. WM-ECO-011 is named as an Economic Asset view, so it can align a holding interest and nothing operational. WM-ACT-007 is a Work Order, so it can authorize scope and resources only. WM-ACT-034 Assessment and WM-MAT-008 Observation can attach evidence, but neither is an execution master. WM-OBJ-022 and WM-OBJ-023 are reserved, so lifecycle must stay derived and a measuring configuration is not yet a master.

Strongest counterexample: A leased instrument of one model has its measuring subsystem replaced under a closed WM-ACT-007, and the prior certificate is still inside its stated dates. If calibration is stored on the Asset Instance shell, on the model, or copied because the order closed, the new subsystem inherits a result that never measured it, and every other instrument of that model is treated as covered. Title never left the lessor and custody never left the lessee, so economic and possession history cannot repair the false fitness claim.

Identity/mastership: Asset Instance does not receive a parallel physical identity. It profiles the WM-OBJ-001 assembly whose continuity identity survives component replacement; a component serial is never the asset identity. Custody requires an independent temporal relationship identity (holder, interval, basis), not a profile of the item. Maintenance Plan, Maintenance Event and Calibration Event each require independent identity; none may reuse WM-ACT-007, WM-ACT-034 or WM-MAT-008 as master. WM-OBJ-022 requires no independent identity. WM-OBJ-023 requires an independent configuration identity, as a specialization, because calibration binds a configuration rather than a model or an economic view.

Title/custody/responsibility: Title is the holding interest aligned only through WM-ECO-011. Custody is physical control over an interval. Operational responsibility is accountability for safe use and upkeep. Location and access are further assignments. All five may differ at the same time, and a change to one does not rewrite the others.

Component continuity: Replacement follows a versioned identity-continuity rule. The parent Asset Instance identity stays; the retired component version is frozen with its history; the replacement starts a new component version. Calibration, certificate and fitness do not move with the parent.

Maintenance plan/order/event: A Maintenance Plan is recurring intent and needs its own identity. WM-ACT-007 authorizes a bounded scope and never proves that work occurred. A Maintenance Event is the execution fact and may cite the order. An order may have zero events. Assessment and Observation may evidence an event; they do not replace it.

Calibration event/certificate: A Calibration Event binds exactly one instrument configuration to a pinned method, references, traceability chain, range, results, uncertainty, decision rule, certificate and validity conditions. The certificate is an immutable artifact of that event, not a substitute for it. WM-OBJ-023 is the configuration the event binds, not a class.

Validity/fitness: Validity is a condition of one Calibration Event on one configuration. Fitness is derived for a stated purpose from the current configuration and its validity conditions. Expiry, configuration change or purpose change drops the current fitness assertion and leaves history intact.

Scenario: A pressure instrument is leased. The lessor retains title in the WM-ECO-011 holding view. The lessee holds custody and operational responsibility; location is a third site; access is a fourth assignment. Sensor module S1 carries Calibration Event E1 and certificate C1, valid to T1. At T2 before T1, S1 is replaced by S2 under a WM-ACT-007 order. Asset Instance identity continues. S1 and E1/C1 stay bound to the retired version. S2 has no calibration. Closing the order does not create E2. At T3 after T1, even an unrestored S1 would be outside validity. Fitness for the stated purpose is not established until a new Calibration Event binds S2. No other serial of the model is affected. Title, custody, responsibility, component and suitability histories remain separately queryable.

Invariants:

1. An Asset Instance profiles exactly one WM-OBJ-001 assembly continuity identity.
2. A component serial is never adopted as the Asset Instance identity.
3. Title holder, custodian and operational responsible party may be three parties at once.
4. A custody interval does not imply title, responsibility, location or access.
5. A location or access change does not imply a custody change.
6. WM-ECO-011 never masters custody, responsibility or fitness.
7. WM-ACT-007 authorizes work and never constitutes a Maintenance Event or Calibration Event.
8. A Maintenance Event may cite at most one authorizing order; an order may cite zero events.
9. Assessment and Observation may evidence an event and never replace event identity.
10. Component replacement preserves parent identity, freezes the retired version, and never transfers calibration.
11. A Calibration Event references exactly one instrument configuration.
12. A successful calibration never covers another serial of the same model.
13. A certificate is the immutable artifact of exactly one Calibration Event.
14. Fitness is derived and purpose-scoped; expiry or configuration change invalidates the current assertion without deleting history.
15. WM-OBJ-022 is derived only and never masters identity or validity.

Minimum model set: WM-OBJ-001 Asset Instance profile; custody relationship; title alignment via WM-ECO-011; responsibility role; location and access as separate assignments; component version under identity continuity; Maintenance Plan; Maintenance Event; Calibration Event with certificate artifact; WM-OBJ-023 configuration; derived fitness assertion; WM-OBJ-022 as projection only.

Blockers: Maintenance Plan, Maintenance Event and Calibration Event are still identifier-unassigned. Custody must not be profiled onto WM-OBJ-001. No rule yet states that WM-ACT-034 and WM-MAT-008 evidence an event without becoming it. WM-OBJ-023 remains reserved and is not yet the configuration master. Until those are fixed, class propagation and silent transfer stay possible in implementation even if rejected in this proposal.



## ARTIFACT candidate-allocation-offline-maintenance-plan/allocation-candidate.json

{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-OPS-03","proposedName":"Maintenance Plan","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A governed recurring maintenance definition remains identifiable independently of assets, work orders and performed events.","versionIdentity":"Changes to intervals, triggers, resources, applicability or acceptance policy create an immutable successor version.","independentLifecycle":["draft","reviewed","approved","published","effective","suspended","superseded","retired"],"mastership":"enterprise maintenance planning authority"},"boundary":{"owns":["maintenance-plan identity","immutable plan versions","recurring intervals and triggers","asset applicability","required resource classes","maintenance policy and acceptance templates","successor history"],"references":[{"target":"WM-OBJ-001","purpose":"Asset instance"},{"target":"WM-ACT-007","purpose":"Work authorization"},{"target":"WM-MAT-008","purpose":"Condition observation"},{"target":"WM-ACT-034","purpose":"Condition assessment"}],"excludes":["asset identity","work-order authorization","performed maintenance","calibration result","condition observation","resource instance"]},"objects":{"MaintenancePlan":{"identity":["maintenancePlanId"],"required":["name","ownerRef","status"],"optional":["successorRef"]},"PlanVersion":{"identity":["maintenancePlanId","version"],"required":["applicability","rules","validFrom","contentDigest"],"optional":["validTo","supersedesVersion"]}},"invariants":["A plan may exist before applicable assets.","Published versions are immutable.","Intervals pin calendar and unit semantics.","Triggers distinguish schedule, usage, condition and event bases.","Applicability is explicit and versioned.","A plan never proves work authorization.","A plan never proves performed work.","Resources are requirements, not actual consumption.","Acceptance templates do not become event evidence.","Retirement preserves historical work references.","Missing observations remain unknown.","Calibration requirements never imply calibration success."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Base specifications and approved relations remain incomplete.","Package conversion and live verification are pending."]}



## ARTIFACT candidate-allocation-offline-maintenance-plan/profile-candidate.json

{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-OPS-03","name":"Enterprise Asset Custody and Maintenance","decision":"PROFILE","newRuntimeId":false,"bases":["WM-OBJ-001","WM-OBJ-022","WM-ECO-011","WM-ACT-007","WM-MAT-008","WM-ACT-034"],"constraints":["Asset identity and custody remain WM-OBJ-001-owned.","Ownership, custody, operational responsibility, location and access remain distinct.","Work-order status never proves performed work.","Condition observations and graded assessments retain separate masters.","Operational Responsibility Assignment is reused from EM-LND-17."]}



## ARTIFACT candidate-allocation-offline-maintenance-plan/fixtures.json

{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Maintenance Plan","cases":[{"id":"unused-plan","kind":"positive","input":"A plan is published before assets are assigned.","expect":"It remains independently valid."},{"id":"condition-trigger","kind":"positive","input":"A condition threshold triggers a work-order request.","expect":"The plan triggers authorization without claiming execution."},{"id":"successor","kind":"positive","input":"An interval changes next year.","expect":"A successor version is appended."},{"id":"order-proof","kind":"negative","input":"The plan is treated as proof of a work order.","expect":"The inference is rejected."},{"id":"execution-proof","kind":"negative","input":"A due plan item is treated as performed maintenance.","expect":"The inference is rejected."},{"id":"mutable-version","kind":"negative","input":"A published interval is overwritten.","expect":"The mutation is rejected."}]}



## ARTIFACT candidate-allocation-offline-maintenance-plan/validation-policy.json

{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}



## ARTIFACT candidate-allocation-offline-maintenance-event/allocation-candidate.json

{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-OPS-03","proposedName":"Maintenance Event","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"An evidenced occurrence of performed maintenance remains identifiable independently of its plan, authorization and asset.","versionIdentity":"Corrections append evidence revisions while the occurrence identity and original record remain stable.","independentLifecycle":["recorded","verified","accepted","rejected","corrected","superseded","voided","closed"],"mastership":"authorized maintenance execution recorder"},"boundary":{"owns":["maintenance-event identity","performed-work interval","actual activities and resources","asset and component effects","observations and completion evidence bindings","performer and verifier attestations","correction history"],"references":[{"target":"WM-OBJ-001","purpose":"Maintained asset and component"},{"target":"WM-ACT-007","purpose":"Authorizing work order"},{"target":"WM-MAT-008","purpose":"Measured condition"},{"target":"WM-ACT-034","purpose":"Condition judgement"}],"excludes":["maintenance-plan definition","work authorization","asset identity","calibration determination","inventory master","generic resource identity"]},"objects":{"MaintenanceEvent":{"identity":["maintenanceEventId"],"required":["assetRef","performedInterval","activities","status"],"optional":["workOrderRef","resourceActuals","componentChanges","evidenceRefs","supersedesRef"]}},"invariants":["Each event identifies the maintained asset instance.","Performed interval is distinct from scheduled and recorded time.","A closed order never substitutes for an event.","Actual resources remain distinct from planned resources.","Component replacement closes and opens membership explicitly.","Asset continuity follows a pinned local rule.","Transformation that consumes an asset ends that identity.","Measurements remain WM-MAT-008 facts.","Judgements remain WM-ACT-034 assessments.","Corrections append and never erase original evidence.","Calibration state never transfers silently across component replacement.","Missing completion evidence remains unknown."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Base specifications and approved relations remain incomplete.","Package conversion and live verification are pending."]}



## ARTIFACT candidate-allocation-offline-maintenance-event/fixtures.json

{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Maintenance Event","cases":[{"id":"performed-repair","kind":"positive","input":"A repair records actual work and evidence against an order.","expect":"The event remains distinct from authorization."},{"id":"component-replacement","kind":"positive","input":"A component is replaced under a pinned continuity rule.","expect":"Membership episodes change without silent calibration transfer."},{"id":"corrected-event","kind":"positive","input":"A verifier corrects a resource actual.","expect":"A revision preserves the original record."},{"id":"closed-order","kind":"negative","input":"A closed work order is treated as proof of execution.","expect":"The inference is rejected."},{"id":"silent-continuity","kind":"negative","input":"Parent identity is preserved without a continuity rule.","expect":"The assertion is rejected."},{"id":"copied-calibration","kind":"negative","input":"Replacement inherits calibration automatically.","expect":"The transfer is rejected."}]}



## ARTIFACT candidate-allocation-offline-maintenance-event/validation-policy.json

{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}



## ARTIFACT candidate-allocation-offline-calibration-event/allocation-candidate.json

{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-OPS-03","proposedName":"Calibration Event","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A calibration occurrence for one instrument configuration remains identifiable independently of the instrument, method and certificate artifact.","versionIdentity":"Corrections and re-evaluations append revisions while preserving the original determination and attestation.","independentLifecycle":["recorded","evaluated","conforming","nonconforming","attested","expired","invalidated","superseded"],"mastership":"authorized calibration authority"},"boundary":{"owns":["calibration-event identity","instrument configuration binding","pinned method and standards","range and calibration points","results, units and uncertainty","decision rule and conformity determination","certificate attestation binding","validity and invalidation conditions"],"references":[{"target":"WM-OBJ-001","purpose":"Instrument instance"},{"target":"WM-KNW-013","purpose":"Pinned method or rule"},{"target":"WM-MAT-008","purpose":"Measurement results"},{"target":"WM-REC-010","purpose":"Conformity decision"},{"target":"WM-REC-001","purpose":"Certificate artifact"}],"excludes":["instrument identity","method definition","reference-standard identity","maintenance event","timeless fitness property","certificate file payload"]},"objects":{"CalibrationEvent":{"identity":["calibrationEventId"],"required":["instrumentRef","configurationRef","methodRef","performedAt","results","uncertainty","status"],"optional":["standardRefs","decisionRef","certificateRef","validUntil","supersedesRef"]}},"invariants":["Each event identifies one instrument and configuration.","Method, standards and units are pinned.","Range and calibration points are explicit.","Uncertainty accompanies interpreted results.","Determination, decision and attestation remain separable.","Certificate digest and issuer are preserved.","Fitness is derived for a stated use.","Expiry ends fitness support without deleting history.","Configuration change invalidates dependent fitness.","Broken traceability invalidates dependent fitness.","Calibration never transfers to sibling instances.","Corrections append rather than overwrite evidence."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Base specifications and approved relations remain incomplete.","Package conversion and live verification are pending."]}



## ARTIFACT candidate-allocation-offline-calibration-event/fixtures.json

{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Calibration Event","cases":[{"id":"traceable-calibration","kind":"positive","input":"One instrument is calibrated against pinned standards and method.","expect":"Results, uncertainty, decision and certificate bindings are retained."},{"id":"expired","kind":"positive","input":"The certificate validity ends.","expect":"Historical evidence remains while current fitness support ceases."},{"id":"configuration-change","kind":"positive","input":"The measuring subsystem is replaced.","expect":"Dependent fitness is invalidated pending recalibration."},{"id":"model-inheritance","kind":"negative","input":"All instruments of the same model inherit one result.","expect":"The inheritance is rejected."},{"id":"timeless-fitness","kind":"negative","input":"Calibration creates an unconditional permanent fitness property.","expect":"The claim is rejected."},{"id":"missing-uncertainty","kind":"negative","input":"A conformity result omits required uncertainty.","expect":"The result is rejected."}]}



## ARTIFACT candidate-allocation-offline-calibration-event/validation-policy.json

{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}

