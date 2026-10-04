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
