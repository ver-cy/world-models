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
