# Frozen semantic audit — EM-LEG-01 (candidateRevision 2)

## Verdict

**REVISE.** The disposition is right: PROFILE over WM-ECO-006 and WM-XCT-029, no new identifier, and the single-writer split between instrument and duty is well grounded and consistent across both studies. But the constraint set as written cannot adjudicate four of its own fixtures, and three named ownership seams are unassigned. A targeted revision 3 is required before these constraints are asserted as enforceable. No identifier action either way.

## Critical findings

1. **Fixtures contradict declared holds.** `delegation` and `delegation-discharges` are scored as passing, yet hold 3 says delegation/third-party-performance typing is absent from WM-ECO-006 change events. `evidence-revoked` requires outstanding quantity recomputed from the surviving accepted set, while hold 4 declares recomputation unratified. These three cases are not entailed by the constraints; reclassify as expected-blocked rather than passing.
2. **Acceptance as a legal act has no master.** Constraint 11 gives issuer attestation to WM-XCT-029 and payload/digest/custody to an unnamed external owner. The obligee's act of acceptance — and acceptance-with-reservation, which constraint 10 requires to stay distinct — is assigned nowhere, risking exactly the dual mastership constraint 4 forbids. Name the owner; state one document, one digest, two roles, one chain. Name WM-XCT-028 as evidence-item master (it is reference-only today) and require item identity to survive revocation, which `evidence-revoked` silently depends on.
3. **SLA duties have no required-field floor.** Constraint 12 requires "enforceable criteria" but never requires obligee, clause locator, threshold and unit, measurement window, method, conformity assessor, or a typed consequence. With WM-SFT-016 reference-only, the profile must state that metric identifier, window and method are held inline on the duty; otherwise `disputed-sla` and `service-credit` have no defined home for the contested measurement. Constraint 13 also reads as a forward ownership grant to an uninstalled stub — restate it as a non-dependency: the profile must be publishable without WM-SFT-016.
4. **Amendment / transfer / novation / new agreement typology missing.** Constraint 8 gates occupancy change but nothing distinguishes amendment (same positions, changed terms) from assignment with consent (residual liability unless discharge is explicitly indicated) from novation (release-and-substitute with successor link) from a new agreement instance with a predecessor link. `novation` expects an explicit link the constraints never require, and nothing rejects a misclassification in either direction.
5. **Narrative escape hatch unbounded.** Constraint 3 permits an "auditable non-normative narrative" with no precedence rule and no bar on promoting predecessor `obligation_text`. State that the cited expression governs, the narrative has no normative effect, and legacy free-text obligation fields are alias-only.
6. **Uncovered constraints.** No fixture exercises conformed-projection overwrite (6), legal-effect vs observation time collapse (11), double exclusive-remedy election (4), or the positive incorporation path where an executed amendment does give an internal target contractual force.

## Required holds

Keep all eight as stated, and add: (a) acceptance and evidence mastership, including the WM-XCT-028 seam, unratified; (b) SLA required-field floor and inline measurement unresolved while WM-SFT-016 is a stub; (c) party-change typology unratified. Reaffirm that both bases are non-canonical and the profile cannot promote ahead of them, that no jurisdictional enforceability conclusion is made, that UBL/FIBO/ODRL/LegalRuleML/ISO-IEC 19086 are alignment only, and that the canonical package and live verification stay held.

## Scenario result

Of thirteen cases: eight hold on the constraints as written (`two-amendments`, `partial-performance`, `service-credit`, and all five negatives other than the delegation pair — notably `amendment-overwrites` on 5/6, `contract-stores-duty-state` on 4, `revocation-deletes-acceptance` on 11, `credit-is-always-penalty` on 14, `internal-slo-as-guarantee` on 12). Three are not entailed (`delegation`, `delegation-discharges`, `evidence-revoked`). Two are under-determined: `novation` lacks a required link rule, `disputed-sla` lacks a defined home for the challenged measurement. Reserved acceptance versus unconditional discharge remains untested.

## Identifier decisions

No new catalogue or runtime identifier. `contourId` EM-LEG-01 unchanged; bases WM-ECO-006 and WM-XCT-029 unchanged and still non-canonical. WM-SFT-016, WM-XCT-028, EM-TEC-06 and EM-LEG-05 remain references — elevating WM-XCT-028 to a named seam allocates nothing. Contract Amendment, Fulfilment Evidence and SLA remain non-aggregates with no identifiers. No reservation mutated, no version invented, no publication authority granted; `candidateRevision` advances to 3 on revision.
