# Frozen semantic audit — EM-DAT-06 / WM-REC-002

**Verdict: ACCEPT WITH LIMITS.** The two-grain aggregate (definition version + issue) is correctly bounded; defects are field-level and must be fixed before any canonical step.

**Critical findings**

1. *Required-ness has no state binding.* `required` lists are flat, yet lifecycles include `planned` and `computed`. `recordArtifactRefs` as unconditionally required contradicts pre-issuance states, the zero-rendition case and the delegation of custody to WM-REC-001. Bind each required field to the state at which it must hold (evidence tuple complete at `issued`; renditions 0..n always).
2. *Missing as-of instant.* `asOfBasis` is required but no as-of instant exists. `cutoffAt` and `issuedAt` alone do not reconstruct the issue. Add the instant and an ordering invariant (`reportingPeriod.end ≤ cutoffAt ≤ asOf ≤ issuedAt`); "remain distinct" is weaker than ordering.
3. *Second disclosure authority.* `permittedProjectionSet` is owned on the definition version while output shape is delegated to WM-XCT-003. Restate it as a narrowing subset of a pinned XCT-003 shape that can never widen it, or make it reference-only.
4. *Binding duplication.* `measureOrQueryBindings` is required on both grains with no invariant that the issue's set is resolved from — and may not exceed — the pinned definition version. As written the issue can introduce unvalidated bindings, bypassing the parameter contract and absent metric mastership.
5. *Restatement can fail open.* `restatementClass`, `restatementReason` and `supersedesReportIssueId` are all optional, so `invalid-overwrite` and `issue-and-restate` are not structurally enforced. Make class and reason conditionally required whenever a predecessor is set, and require a predecessor on any successor sharing (definitionVersion, parameters, period).
6. *Deployment/BI leakage.* `layoutProfileRef` and `scheduleHint` sit inside an owned immutable definition version while `excludes` bars BI configuration and pipeline scheduling. Keep them external references clearly marked non-identity, or drop them.
7. *Duplicate calendar handles.* `fiscalCalendarRef` and `calendarBasisRef` co-exist optionally against one required issue-level `calendarBasis`; collapse to one WM-XCT-009 pin. `audienceClass` appears in both `required` and `optional` on the definition version — a contradiction.
8. *Fixture gaps.* No fixture for the arbitrary HR–finance join refusal, for coverage exception when run evidence misses the period, for publication referencing a non-issued statement, or for `snapshot-dashboard` lacking execution evidence. Reference-only status of WM-DAT-002, WM-DAT-008, WM-ACT-044, WM-MED-003 is otherwise stated correctly and consistently.

**Required holds**

H1 neighbouring relations remain candidate rows (no cascade authority). H2 metric-definition mastership unassigned (EM-DAT-05) — inline bindings interim. H3 WM-XCT-003 multi-grain validation declarative, so the grain-ceiling invariant is asserted, not demonstrated. H4 crosswalks are alignment only. H5 second-provider adversarial review of the definition/issue split. H6 relation approval, package conversion, live verification before canonical publication. H7 suppression manifests may themselves be disclosive at small counts — unresolved.

**Scenario result**

Issue/restate, suppression pinning, dashboard drift, artifact plurality, fiscal pin, policy widening and custody-only digest change all pass as specified. Overwrite rejection and missing-definition failure pass only after finding 5 is applied; snapshot-dashboard fails closed only after finding 1.

**Identifier decision**

No new identifier. Complete reserved WM-REC-002 (`vr.wm-rec-002`) as an aggregate; remain `canonicalPublishable: false`. This audit discharges the frozen-audit hold only; it grants no publication authority.
