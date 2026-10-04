# EM-OPS-04 — Final Frozen Semantic Audit

---

## 1. Verdict on decision and artifacts

**Boundary decision: SETTLED. Preserved unchanged.**

The disposition in `local-evidence.md` survives reconciliation. Claude and Grok agree on every root decision that matters: split ItemDefinition across WM-OBJ-002 (commercial/product type) and WM-OBJ-018 (engineering definition) with no combined root; SKU as a party-scoped identifier, never a root and never a serial; Engineering Revision as an immutable contained revision of WM-OBJ-018; WM-OBJ-019 reused for EBOM only; BOM Line as a baseline-scoped contained occurrence; Substitution Rule as a contained component-selection profile; MBOM/Manufacturing Plan, As-Built Assembly, Lot/Batch, Actual Transformation Event and Production Work Order left identifier-unassigned; no identifier allocated.

**Grok reconciliation.** Grok's verdict is "conditional accept," and its conditions are satisfied by the frozen evidence, so the conditional resolves to accept:

- Grok condition: containment in WM-OBJ-018 and reuse of WM-OBJ-019 hold only if those objects master versioned definitions rather than sellable items or serials. The frozen Claude evidence records exactly that — WM-OBJ-018 masters controlled design revisions and baseline packages and out-of-scopes BOM composition; WM-OBJ-019 masters occurrences, quantity basis, effectivity and alternates and out-of-scopes production routes, procurement execution, as-built item state and actual consumption. Condition met; containment and reuse stand.
- Grok blocker (b) "firmware release and SBOM have no decided root" is **contradicted** by the frozen evidence: WM-SFT-007 (component/package), WM-SFT-008 (release) and WM-SFT-012 (SBOM) exist as drafts. Grok was working from a prompt that named these only as a category. Rejected as evidence against the decision; retained only as the narrower true point that the firmware **installation occurrence** model is referenced but unsupplied.
- Grok's "still required, missing or unassigned: Variant, Occurrence, SerializedItem" is **contradicted**: WM-OBJ-017 owns configuration variants, WM-OBJ-001 owns individuated items, and occurrence is a baseline-scoped contained identity inside WM-OBJ-019, not a root. Rejected. Grok's own invariant 12 is preserved as a *distinctness* rule, not as a root claim.
- Grok blocker (c) — baseline containment of Substitution Rule does not name the effectivity-authority owner — is **valid and unclosed** in the artifacts. Carried as D3.
- Grok blockers (a), (d), (f) restate holds already recorded locally (unassigned actuals; EBOM ≠ MBOM; scenario does not close inside the assigned set). They are scope cuts explicitly stated in `local-evidence.md` ("Lot-based effectivity remains unresolved until the lot master exists"), not inconsistencies. The decision is not disturbed.

Nothing in the supplied evidence proves the settled decision inconsistent. No root is promoted, no identifier allocated, no internal schema invented for WM-OBJ-002/017/018/019/001 or WM-SFT-007/008/012.

**Artifacts: CONDITIONALLY REJECTED pending the deterministic remediation in §2.** All five candidate packages pass their own `validation-policy.json` minimums mechanically (modelId/registryId null, state `unassigned`, 10 invariants ≥ 8, 4 references ≥ 3, 4 fixtures ≥ 3, positive and negative present, stable-identity and lifecycle statements present). The policy itself is too weak to detect the 27 material defects below. Specific artifact-level findings:

- `allocation-candidate.json` ×5: identity, lifecycle and invariant text are substantively correct and consistent with the settled boundary; defects are in quantity typing, time typing, provenance basis, reference verification status, lifecycle-axis collapse, conditional-required fields and mastership overlap.
- `fixtures.json` ×5 (20 cases): structurally non-conformant — every case lacks `target`, `violates` and `closesDefect`, and all 10 negative cases lack `expectedCode`. No error-code registry exists.
- `validation-policy.json` ×5: identical v1 files; no enforcement of fixture fields, reference verification, holds non-emptiness, decision enum, publication hold, or identifier-allocation lock.
- `profile-candidate.json` ×1: misfiled inside the Manufacturing Plan package, carries only 5 constraints against 11 required invariants, omits SKU-vs-serial, occurrence scoping, identifier non-reuse, EBOM→MBOM mapping, firmware/SBOM rules and the effectivity-authority owner, and carries no `canonicalPublishable`, `holds` or publication-hold fields.
- `README.md` ×5: identical boilerplate; no decision, allocation state, boundary or hold statement.
- Missing artifacts: contour decision record, error-code registry, crosswalk hold record.

No installability, canonical-completeness or publication-readiness claim is made here.

---

## 2. Material defects and exact deterministic remediation

Notation: `<package>/<file>` paths are relative to the EM-OPS-04 review root; `+` adds, `−` removes, `→` replaces. Shared shapes are defined once in D8/D11/D12/D15 and applied by reference.

**D1 — No contour-level root-decision record; contested roots unrecorded.**
`+ contour-decision.json`:
```
{"format":"vercy-contour-decision/v1","contourId":"EM-OPS-04","decisionState":"settled","identifiersAllocated":0,
 "candidates":[
  {"name":"ItemDefinition","decision":"REJECT_AS_ROOT","resolution":"SPLIT","targets":["WM-OBJ-002","WM-OBJ-018"]},
  {"name":"SKU","decision":"REJECT_AS_ROOT","resolution":"PROFILE","targets":["WM-OBJ-002","WM-OBJ-017"]},
  {"name":"EngineeringRevision","decision":"REJECT_AS_ROOT","resolution":"CONTAINED","targets":["WM-OBJ-018"]},
  {"name":"BillOfMaterials","decision":"REUSE","resolution":"EBOM_ONLY","targets":["WM-OBJ-019"]},
  {"name":"BOMLine","decision":"REJECT_AS_ROOT","resolution":"CONTAINED_BASELINE_SCOPED","targets":["WM-OBJ-019"]},
  {"name":"SubstitutionRule","decision":"REJECT_AS_ROOT","resolution":"CONTAINED_COMPONENT_SELECTION","targets":["WM-OBJ-019"]}],
 "unassignedRoots":["MBOM / Manufacturing Plan","As-Built Assembly","Lot / Batch","Actual Transformation Event","Production Work Order"],
 "rejectedRootClaims":[
  {"claim":"Occurrence as root","source":"grok-study.raw.md","disposition":"REJECTED","basis":"WM-OBJ-019 masters occurrences; identity is baseline-scoped"},
  {"claim":"Variant as missing root","source":"grok-study.raw.md","disposition":"REJECTED","basis":"WM-OBJ-017 exists"},
  {"claim":"SerializedItem as missing root","source":"grok-study.raw.md","disposition":"REJECTED","basis":"WM-OBJ-001 exists"},
  {"claim":"FirmwareRelease as missing root","source":"grok-study.raw.md","disposition":"REJECTED","basis":"WM-SFT-007/WM-SFT-008 exist"},
  {"claim":"SBOM as missing root","source":"grok-study.raw.md","disposition":"REJECTED","basis":"WM-SFT-012 exists"}],
 "canonicalPublishable":false,"publicationHold":true}
```

**D2 — Promotion and allocation locks absent from candidate files.**
In all five `*/allocation-candidate.json`: `+ "promotionBlocked": true`, `+ "identifierAllocationBlocked": true`, `+ "publicationHold": true`, `+ "decisionEnum": "NEW_MODEL_UNASSIGNED"`, and `"decision": "NEW MODEL" → "NEW MODEL (unassigned; no identifier may be allocated by this audit)"`.

**D3 — Effectivity-authority owner unnamed for contained Substitution Rule (Grok blocker c).**
In `profile-candidate.json`: `+ "authorityAssignments": {"effectivityAuthorityOwner":"composition authority of WM-OBJ-019","substitutionApprovalOwner":"composition authority of WM-OBJ-019","designRevisionReleaseOwner":"design authority of WM-OBJ-018","catalogIdentityOwner":"product/catalog steward of WM-OBJ-002","variantOwner":"configuration authority of WM-OBJ-017","itemStewardOwner":"item steward of WM-OBJ-001","softwareReleaseOwner":"software product owner of WM-SFT-007/WM-SFT-008/WM-SFT-012"}`, `+ "constraints[]": "No substitution is valid without a named approving authority and a bounded effectivity range."`

**D4 — Profile artifact misfiled and incomplete.**
Move `candidate-allocation-offline-manufacturing-plan/profile-candidate.json → candidate-profile-offline-enterprise-product-engineering/profile-candidate.json`. In that file: `+ "canonicalPublishable": false`, `+ "publicationHold": true`, `+ "newRuntimeId": false` (retain), `+ "holds": ["Base specifications remain reviewable drafts and mostly single-provider.","Crosswalks are absent.","Firmware installation-occurrence model (cited as WM-SFT-009 by WM-SFT-008) is unsupplied.","CLASSIFIES is absent from the relation enum.","No publication or installability readiness is claimed."]`, and replace `constraints` with the full 11 invariants verbatim from `local-evidence.md` §"Required invariants" plus: `"SKU is a seller-scoped alias or variant qualifier and never identifies a serialized item or a design revision."`, `"A priced sellable unit belongs to the separate Offering boundary."`, `"Commercial substitution on WM-OBJ-002 and engineering component substitution in WM-OBJ-019 are distinct relations and never merged."`, `"Occurrence identity is baseline-scoped and never global."`, `"Firmware binding to a physical item is a deployment/installation occurrence with its own time and evidence."`, `"Reuse of WM-OBJ-019 never implies MBOM."` `+ "bases[]": "WM-FLW-013"`.

**D5 — Lot identity: no scoped alternate key, no retirement/tombstone.**
In `candidate-allocation-offline-lot-batch/allocation-candidate.json`, `objects.Lot`: `+ "alternateKeys": [["issuerRef","identifierSchemeRef","lotCode"]]`, `+ "uniqueness": {"lotId":"global","alternateKey:issuerRef+identifierSchemeRef+lotCode":"unique-per-issuer-scheme"}`, `optional + "retirement": {"retiredAt":"<rfc3339-with-offset>","tombstoneRef":"<string>","reason":"<string>"}`, `invariants[9] "Identifiers are never reused." → "Identifiers are never reused; retirement writes a tombstone and the retired identifier stays resolvable."` Apply the same `retirement` optional and invariant wording to all five candidate root objects (`AsBuiltAssembly`, `ManufacturingPlan`, `ProductionWorkOrder`, `TransformationEvent`).

**D6 — Lifecycle axis collapse.**
Lot: `identityTest.independentLifecycle → ["created","released","partiallyConsumed","exhausted","closed"]`, `+ "dispositionStates": ["unrestricted","quarantined","blocked","recalled"]`, `objects.Lot.required "status" → "lifecycleState"`, `required + "dispositionState"`, `required + "dispositionValidFrom"`.
As-built: `independentLifecycle` remove `"effective"`, result `["initiated","assembled","verified","current","modified","disassembled","superseded","closed"]` (intent-time "effective" is not an actual-composition state).

**D7 — BOM kind absent on plan versions.**
`candidate-allocation-offline-manufacturing-plan/.../objects.PlanVersion.required + "bomKind"` with `+ "enums": {"bomKind":["MBOM"]}`; `+ "versionImmutability": {"mutableAfterStatus":["draft","reviewed"],"immutableAfterStatus":["approved","released","effective","superseded","retired"],"immutabilityWitness":"contentDigest"}`; `invariants[1] "Every plan states immutable version." → "Every plan version states bomKind and an immutable version witnessed by contentDigest."`

**D8 — Quantity lacks unit, basis, code-list version and unknown handling.**
Define once in each candidate file as `+ "sharedShapes": {"Quantity": {"value":"<decimal-string|null>","unitCode":"<string>","unitCodeListRef":"<string>","unitCodeListVersion":"<string>","basis":"per-each|per-parent-assembly|per-batch|per-unit-length|per-unit-mass|per-unit-volume|per-operation","basisParentQuantity":{"value":"<decimal-string>","unitCode":"<string>"},"rounding":"none|half-up|half-even|ceil|floor","unknownReason":"null|unknown|not-applicable|withheld"}}` with rule `+ "sharedRules": ["Quantity.value and Quantity.unknownReason are mutually exclusive and exactly one is non-null.","Zero never denotes unknown, not-applicable or withheld."]`. Then type every quantity field as `Quantity`: as-built `objects.ComponentMembership.required.quantity`; lot `objects.Lot.optional.quantity`; work order `objects.ProductionWorkOrder.required.quantity`; transformation event `objects.TransformationEvent.required.inputs[].quantity` and `.outputs[].quantity`. Lot `invariants[4] "Quantities carry units." → "Quantities carry unit, basis and unit code-list version."`

**D9 — As-built uses effectivity vocabulary for actual composition state.**
`candidate-allocation-offline-as-built-assembly/.../objects.AsBuiltAssembly.required`: `"effectiveFrom" → "compositionValidFrom"`, `optional "effectiveTo" → "compositionValidTo"`, `required + "derivedFromEventRefs"` (non-empty array), `required "status" → "lifecycleState"`. `+ "sharedRules[]": "This model declares no effectivity predicate; effectivity is an intent property of WM-OBJ-018 revisions and WM-OBJ-019 baselines."`

**D10 — Substitution applicability/effectivity/authority and lot resolvability not expressed in the profile.**
`profile-candidate.json + "containedProfileRequirements": {"WM-OBJ-019.component-selection": {"required":["direction","applicableDesignRevisionRefs","applicableBaselineRefs","effectivity","approvingAuthorityRef","evidenceRef"],"effectivity":{"oneOfBounds":["timeRange","serialRange","lotRange","siteScope"],"resolvability":"A lotRange bound is unresolvable until the Lot/Batch master exists; it must be recorded as unresolved, never defaulted to satisfied."}}}`

**D11 — Declared/observed/inferred provenance not separated.**
In all five candidate files: `sharedShapes + "AssertionBasis": "declared|observed|inferred"`; add `required + "assertionBasis"` to `AsBuiltAssembly`, `ComponentMembership`, `LotMembership` (D19), `TransformationEvent`, and `optional + "assertionBasis"` to `PlanVersion` and `ProductionWorkOrder`. `+ "sharedRules[]": "Declared, observed and inferred assertions never merge and never overwrite one another."`

**D12 — Time semantics collapsed; no RFC 3339 offset requirement.**
In all five candidate files: `sharedShapes + "Timestamp": "<rfc3339-with-mandatory-explicit-offset>"`. Transformation event `objects.TransformationEvent.required + "recordedAt"`, `optional + "ingestedAt"`, `optional + "correctedAt"`, and `required "eventTime"` typed `Timestamp`. `+ "sharedRules[]": "Event, effective, observation, record, posting, ingestion, publication and correction times are distinct fields and never collapse."` Type all `validFrom`/`validTo`/`compositionValidFrom`/`compositionValidTo`/`producedInterval`/`scheduledWindow`/`dispositionValidFrom`/`retiredAt` as `Timestamp`.

**D13 — Work order pinning contradicts its own invariant 3; EBOM baseline reference unmodelled.**
`candidate-allocation-offline-production-work-order/.../objects.ProductionWorkOrder`: move `"designRevisionRef"` from `optional` to `required`; `required + "ebomBaselineVersionRef"`; `+ "pinningRule": "planVersionRef, designRevisionRef and ebomBaselineVersionRef must each resolve to an immutable version; unversioned references are rejected."`

**D14 — Firmware/SBOM rules and the unsupplied installation-occurrence model are unrecorded.**
`profile-candidate.json + "constraints[]"`: `"A firmware release (WM-SFT-008) is neither a device nor an EBOM line nor a part number."`, `"WM-SFT-012 is the SBOM record and never carries firmware-release identity."`, `"WM-SFT-007 masters component/package identity; releases do not."`
As-built: `boundary.excludes + "firmware installation occurrence"`, `invariants[8] "Firmware binding uses installation evidence." → "Firmware is never a component membership; firmware presence is asserted only by an external installation occurrence with its own time and evidence."`, `holds + "The installation-occurrence model cited by WM-SFT-008 (WM-SFT-009) is referenced but unsupplied; firmware-to-item binding stays unresolved."`

**D15 — Reference targets unverified; references to unassigned candidates undeclared.**
In all five candidate files, convert each `boundary.references[]` entry to `{"target":"<id>","purpose":"<text>","status":"<enum>"}` with `+ "enums": {"referenceStatus":["verified-supplied","unverified-draft","dangling","unassigned-candidate"]}`. Set `status` from the frozen evidence: `verified-supplied` for WM-OBJ-001, WM-OBJ-002, WM-OBJ-017, WM-OBJ-018, WM-OBJ-019, WM-SFT-007, WM-SFT-008, WM-SFT-012, WM-FLW-013; `unverified-draft` for WM-MAT-008, WM-KNW-008, WM-ACT-034, WM-REC-010, WM-ORG-016, WM-SFT-009; `dangling` for WM-OBJ-012, WM-OBJ-020, WM-OBJ-021, WM-OBJ-022, WM-ACT-015. Add `boundary.references + {"target":"WM-FLW-013","purpose":"Genealogy edge must cite an actual event with evidence","status":"verified-supplied"}` to the as-built and transformation-event candidates. Add to as-built, lot and work order: `+ "unresolvedReferences": [{"targetName":"Actual Transformation Event","state":"unassigned-candidate","field":"sourceEventRef|derivedFromEventRefs"}]` (as-built, lot) and `[{"targetName":"MBOM / Manufacturing Plan","state":"unassigned-candidate","field":"planVersionRef"}]` (work order), each with `+ "resolutionHold": true`.

**D16 — Relation contradictions and the missing CLASSIFIES term are not recorded in any package.**
In all five candidate files, replace the generic `holds` array by that array plus: `"WM-OBJ-019 to WM-OBJ-002 is simultaneously asserted as parent, COMPOSE and REFERENCE; unresolved."`, `"WM-OBJ-018 as child of WM-OBJ-002 conflicts with its own required REFERENCE boundary; unresolved."`, `"WM-SFT-012 and WM-SFT-008 claim CHILD of WM-SFT-007 while the ledger records REFERENCE or no edge; unresolved."`, `"WM-OBJ-012, WM-OBJ-020, WM-OBJ-021, WM-OBJ-022 and WM-ACT-015 are dangling relation targets."`, `"CLASSIFIES is absent from the relation enum; WM-OBJ-017 expresses it as REFERENCE, diverging from the relations ledger."`, `"WM-ACT-007 is maintenance-scoped with unresolved K11 duplication."`

**D17 — Mastership overlap between As-Built Assembly and Lot/Batch.**
As-built `identityTest.mastership → "authorized as-built composition-state authority (composition state only; no lot or serial identity)"`; `invariants + "This model never asserts lot identity, serialized-item identity or product-type identity."`
Lot `identityTest.mastership → "authorized bulk-cohort identity and lot-genealogy authority (cohort identity only; no composition state)"`; `invariants + "This model never asserts as-built composition state."`

**D18 — Correction lineage not enforced; void unspecified.**
Transformation event: `+ "conditionalRequired": [{"when":"status in [corrected,superseded]","require":["supersedesRef","correctedAt","correctionAuthorityRef"]},{"when":"status == voided","require":["voidReason","voidAuthorityRef","originalRetained"]}]`, `+ "immutability": {"originalOccurrence":"never-mutated","voidedRecords":"retained"}`, `invariants[8] "Corrections append and never erase originals." → "Corrections and voids append attributable successors; originals and their evidence are retained and remain resolvable."` Apply the `status in [corrected,superseded] → supersedesRef` rule to as-built (`supersedesRef`) and to lot and plan successors.

**D19 — Membership provenance unowned (lot) and unclosed (as-built).**
As-built `objects.ComponentMembership + "conditionalRequired": [{"when":"validTo is non-null","require":["closingEventRef"]}]`, `optional + "closingEventRef"`.
Lot `objects + "LotMembership": {"identity":["lotId","membershipId"],"required":["memberRef","memberKind","validFrom","sourceEventRef","assertionBasis"],"optional":["validTo","closingEventRef"],"enums":{"memberKind":["serialized-item","child-lot"]}}` and `objects + "LotGenealogyEdge": {"identity":["lotId","edgeId"],"required":["edgeKind","counterpartLotRef","sourceEventRef"],"enums":{"edgeKind":["split-from","merged-from","split-into","merged-into"]}}`.

**D20 — All 20 existing fixture cases are structurally non-conformant.**
In each `*/fixtures.json`, rewrite every case to `{"id":<unchanged>,"target":"<package-directory-name>","kind":<unchanged>,"input":<unchanged>,"expect":<unchanged>,"violates":[...],"closesDefect":[...],"expectedCode":"<only when kind==negative>"}`. Literal assignments:
`attached-component` → `violates:["ABA-INV-01","ABA-INV-03"]`, `closesDefect:["D19"]`; `detached-component` → `violates:["ABA-INV-06"]`, `closesDefect:["D19"]`; `bom-as-built` → `violates:["ABA-INV-02","LE-INV-05"]`, `closesDefect:["D9"]`, `expectedCode:"EMOPS04-E012"`; `silent-replacement` → `violates:["ABA-INV-01","ABA-INV-09"]`, `closesDefect:["D18"]`, `expectedCode:"EMOPS04-E014"`;
`produced-lot` → `violates:["LOT-INV-01"]`, `closesDefect:["D5"]`; `split` → `violates:["LOT-INV-05"]`, `closesDefect:["D19"]`; `serial-collapse` → `violates:["LOT-INV-02","LE-INV-09"]`, `closesDefect:["D17"]`, `expectedCode:"EMOPS04-E019"`; `unresolved-effectivity` → `violates:["LOT-INV-06"]`, `closesDefect:["D10"]`, `expectedCode:"EMOPS04-E011"`;
`released-plan` → `violates:["MBOM-INV-01","MBOM-INV-05"]`, `closesDefect:["D7"]`; `successor-route` → `violates:["MBOM-INV-09"]`, `closesDefect:["D7"]`; `actual-consumption` → `violates:["MBOM-INV-07","LE-INV-05"]`, `closesDefect:["D7"]`, `expectedCode:"EMOPS04-E012"`; `ebom-overwrite` → `violates:["MBOM-INV-05","LE-INV-10"]`, `closesDefect:["D7"]`, `expectedCode:"EMOPS04-E032"`;
`released-order` → `violates:["PWO-INV-01","PWO-INV-06"]`, `closesDefect:["D13"]`; `completed-order` → `violates:["PWO-INV-08"]`, `closesDefect:["D13"]`; `closed-proof` → `violates:["PWO-INV-06"]`, `closesDefect:["D13"]`, `expectedCode:"EMOPS04-E034"`; `floating-plan` → `violates:["PWO-INV-03"]`, `closesDefect:["D13"]`, `expectedCode:"EMOPS04-E033"`;
`consume-produce` → `violates:["ATE-INV-02","ATE-INV-06"]`, `closesDefect:["D19"]`; `assembly` → `violates:["ATE-INV-02"]`, `closesDefect:["D19"]`; `planned-as-actual` → `violates:["ATE-INV-09","LE-INV-05"]`, `closesDefect:["D12"]`, `expectedCode:"EMOPS04-E012"`; `overwrite` → `violates:["ATE-INV-08"]`, `closesDefect:["D18"]`, `expectedCode:"EMOPS04-E014"`.

**D21 — Fixture file format lacks contour and registry linkage.**
In each `*/fixtures.json`: `"format":"vercy-enterprise-allocation-fixtures/v1" → "vercy-enterprise-allocation-fixtures/v2"`, `+ "contourId":"EM-OPS-04"`, `+ "target":"<package-directory-name>"`, `+ "errorCodeRegistryRef":"error-codes.json"`, `+ "defectRegistryRef":"audit-defects.json"`. Retain `candidateName`.

**D22 — Validation policy too weak to detect D1–D21.**
In all five `*/validation-policy.json` (and a new copy in the profile package): `"format" → "vercy-allocation-validation/v2"` and `requirements +`
```
"forbidsIdentifierAllocation": true,
"decisionEnum": ["NEW_MODEL_UNASSIGNED","PROFILE","REUSE","REJECT_AS_ROOT","SPLIT","CONTAINED"],
"requiresPromotionBlocked": true,
"requiresPublicationHold": true,
"canonicalPublishableMustBeFalse": true,
"requiresHoldsNonEmpty": true,
"requiresRelationHoldsEnumerated": true,
"minimumVerifiedReferences": 2,
"requiresReferenceStatusOnEveryReference": true,
"requiresUnresolvedReferencesDeclared": true,
"minimumFixtures": 6,
"minimumNegativeFixtures": 3,
"minimumPositiveFixtures": 2,
"fixtureRequiredFields": ["id","target","kind","input","expect","violates","closesDefect"],
"negativeFixtureRequiredFields": ["expectedCode"],
"closesDefectMustBeNonEmptyArray": true,
"expectedCodeMustResolveInRegistry": true,
"requiresQuantityUnitBasisAndCodeListVersion": true,
"requiresRfc3339WithExplicitOffset": true,
"requiresAssertionBasis": true,
"requiresRetirementTombstone": true,
"requiresSeparateLifecycleAndDispositionAxes": true,
"requiresBomKindOnBomVersions": true,
"requiresConditionalRequiredRules": true,
"forbidsEffectivityVocabularyOnActualStateModels": true,
"requiresEveryDefectClosedByAtLeastOneFixture": true
```

**D23 — No error-code registry; negative fixtures cannot be made deterministic.**
`+ error-codes.json` with `{"format":"vercy-allocation-error-codes/v1","contourId":"EM-OPS-04","codes":{...}}` containing exactly: `EMOPS04-E001 ROOT_PROMOTION_DENIED`, `E002 IDENTIFIER_ALLOCATION_DENIED`, `E003 IDENTITY_CONFLATION`, `E004 LIFECYCLE_AXIS_CONFLATION`, `E005 BOM_KIND_MISSING`, `E006 BOM_VERSION_NOT_IMMUTABLE`, `E007 QUANTITY_UNIT_MISSING`, `E008 QUANTITY_BASIS_MISSING`, `E009 EFFECTIVITY_MISSING`, `E010 AUTHORITY_MISSING`, `E011 EFFECTIVITY_UNRESOLVABLE`, `E012 INTENT_AS_ACTUAL`, `E013 EVENT_EVIDENCE_MISSING`, `E014 OVERWRITE_DENIED`, `E015 ALTERNATE_SUMMED_AS_INSTALLED`, `E016 FIRMWARE_AS_BOM_LINE`, `E017 FIRMWARE_AS_DEVICE`, `E018 SBOM_AS_RELEASE_IDENTITY`, `E019 LOT_AS_SERIAL`, `E020 OCCURRENCE_GLOBAL_IDENTITY`, `E021 SKU_AS_SERIAL`, `E022 SKU_AS_REVISION`, `E023 IDENTIFIER_REUSE`, `E024 TOMBSTONE_MISSING`, `E025 REFERENCE_UNVERIFIED`, `E026 REFERENCE_DANGLING_OR_UNSUPPLIED`, `E027 RELATION_CONTRADICTION`, `E028 RELATION_TERM_ABSENT`, `E029 PUBLICATION_HOLD_VIOLATION`, `E030 PROVENANCE_BASIS_MISSING`, `E031 TIME_SEMANTICS_COLLAPSE`, `E032 EBOM_MBOM_MAPPING_MISSING`, `E033 VERSION_PIN_MISSING`, `E034 AUTHORIZATION_AS_EXECUTION`, `E035 RESERVATION_AS_CONSUMPTION`, `E036 PROFILE_CONSTRAINT_MISSING`, `E037 FIXTURE_FIELD_MISSING`, `E038 MASTERSHIP_OVERLAP`, `E039 UNKNOWN_COLLAPSED`, `E040 CORRECTION_LINEAGE_MISSING`, `E041 SETTLED_BOUNDARY_REOPENED`, `E042 UNASSIGNED_CANDIDATE_CITED_AS_AUTHORITY`.

**D24 — READMEs are contentless boilerplate.**
In each `*/README.md`, append: `- Decision: NEW MODEL (unassigned).` / `- Allocation state: unassigned; modelId null; registryId null.` / `- Mastership: <identityTest.mastership value>.` / `- Excludes: <boundary.excludes list>.` / `- Open holds: see allocation-candidate.json "holds".` / `- No identifier allocation, publication, installability or runtime registration is claimed.` In the profile README (new file, same template) substitute `- Decision: PROFILE (no new runtime id).`

**D25 — Publication holds and crosswalk absence not recorded as artifacts.**
`+ publication-hold.json`: `{"format":"vercy-publication-hold/v1","contourId":"EM-OPS-04","publicationHold":true,"installabilityClaimed":false,"canonicalCompletenessClaimed":false,"runtimeRegistrationClaimed":false,"reasons":["Identifier allocation pending for five unassigned roots.","Base specifications are reviewable drafts, mostly single-provider.","Relation contradictions D16 unresolved.","Crosswalks absent."]}` and `+ crosswalk-hold.json`: `{"format":"vercy-crosswalk-hold/v1","contourId":"EM-OPS-04","crosswalksPresent":false,"state":"pending","mappings":[],"note":"No crosswalk content is invented by this audit."}`

**D26 — Occurrence-as-root claim and SKU scoping not fixture-guarded.**
Covered by D1 record plus `profile-candidate.json + "constraints[]": "BOM occurrences are baseline-scoped and remain distinct even when displayed row numbers match; occurrence is not a root."` and `+ "constraints[]": "Alternates are candidates and are never summed as installed components."`

**D27 — Unknown / zero / not-applicable / withheld may collapse.**
Covered by the D8 `sharedRules`; additionally as-built `invariants[10] "Missing event evidence remains unknown." → "Missing event evidence remains explicitly unknown and never defaults to zero, absent or not-applicable."` and the same wording applied to lot `invariants[10]`, work order `invariants[10]`, transformation event `invariants[10]`.

---

## 3. Additional fixtures

```json
[
  {"id":"F-CON-001","target":"contour:EM-OPS-04","kind":"positive","input":"contour-decision.json records all six candidate decisions, five unassigned roots and zero allocated identifiers.","expect":"The settled boundary validates and the decision record is accepted.","violates":["LE-INV-04"],"closesDefect":["D1"]},
  {"id":"F-CON-002","target":"contour:EM-OPS-04","kind":"negative","input":"A single combined ItemDefinition root is proposed covering both commercial type and engineering definition.","expect":"The combined root is rejected and the WM-OBJ-002 / WM-OBJ-018 split is retained.","violates":["LE-INV-04"],"closesDefect":["D1"],"expectedCode":"EMOPS04-E003"},
  {"id":"F-CON-003","target":"contour:EM-OPS-04","kind":"negative","input":"Occurrence is promoted to a root with globally unique identity outside any EBOM baseline.","expect":"The promotion is rejected; occurrence stays a baseline-scoped contained identity in WM-OBJ-019.","violates":["LE-INV-06"],"closesDefect":["D1","D26"],"expectedCode":"EMOPS04-E020"},
  {"id":"F-CON-004","target":"contour:EM-OPS-04","kind":"negative","input":"Variant, SerializedItem, FirmwareRelease or SBOM is re-declared a missing root despite WM-OBJ-017, WM-OBJ-001, WM-SFT-008 and WM-SFT-012 existing.","expect":"The reopening is rejected and the rejectedRootClaims record is cited.","violates":["LE-INV-08"],"closesDefect":["D1"],"expectedCode":"EMOPS04-E041"},
  {"id":"F-CON-005","target":"contour:EM-OPS-04","kind":"negative","input":"A model identifier is assigned to any of the five unassigned candidates.","expect":"The allocation is rejected; modelId and registryId stay null.","violates":["POL-REQ-forbidsIdentifierAllocation"],"closesDefect":["D2"],"expectedCode":"EMOPS04-E002"},
  {"id":"F-CON-006","target":"contour:EM-OPS-04","kind":"negative","input":"An unassigned candidate is cited as a resolvable authority for lot effectivity or as-built composition.","expect":"The citation is rejected and the unresolvedReferences hold is reported.","violates":["LOT-INV-06","ABA-INV-01"],"closesDefect":["D2","D15"],"expectedCode":"EMOPS04-E042"},
  {"id":"F-CON-007","target":"contour:EM-OPS-04","kind":"positive","input":"Every expectedCode used by any fixture resolves to a code in error-codes.json.","expect":"Registry resolution succeeds for all negative fixtures.","violates":["POL-REQ-expectedCodeMustResolveInRegistry"],"closesDefect":["D21","D23"]},
  {"id":"F-CON-008","target":"contour:EM-OPS-04","kind":"negative","input":"A fixture case omits target, violates or closesDefect.","expect":"The fixture file fails validation.","violates":["POL-REQ-fixtureRequiredFields"],"closesDefect":["D20"],"expectedCode":"EMOPS04-E037"},
  {"id":"F-CON-009","target":"contour:EM-OPS-04","kind":"positive","input":"Every candidate, profile, policy and README artifact carries publicationHold true and canonicalPublishable false.","expect":"The publication hold is uniformly asserted.","violates":["POL-REQ-requiresPublicationHold"],"closesDefect":["D24","D25"]},
  {"id":"F-CON-010","target":"contour:EM-OPS-04","kind":"negative","input":"An artifact claims publication readiness, installability or canonical completeness.","expect":"The claim is rejected.","violates":["POL-REQ-canonicalPublishableMustBeFalse"],"closesDefect":["D25"],"expectedCode":"EMOPS04-E029"},
  {"id":"F-CON-011","target":"contour:EM-OPS-04","kind":"positive","input":"crosswalk-hold.json declares crosswalksPresent false with an empty mappings array.","expect":"The absence of crosswalks is recorded without inventing mappings.","violates":["POL-REQ-requiresHoldsNonEmpty"],"closesDefect":["D25"]},
  {"id":"F-CON-012","target":"contour:EM-OPS-04","kind":"negative","input":"CLASSIFIES is used as a relation term while absent from the relation enum.","expect":"The edge is rejected and the enum-absence hold is reported.","violates":["LE-INV-04"],"closesDefect":["D16"],"expectedCode":"EMOPS04-E028"},
  {"id":"F-CON-013","target":"contour:EM-OPS-04","kind":"negative","input":"WM-OBJ-019 to WM-OBJ-002 is accepted simultaneously as parent, COMPOSE and REFERENCE.","expect":"The contradictory edge set is rejected and held unresolved.","violates":["LE-INV-06"],"closesDefect":["D16"],"expectedCode":"EMOPS04-E027"},
  {"id":"F-CON-014","target":"contour:EM-OPS-04","kind":"positive","input":"Each candidate holds array enumerates the WM-OBJ-019/002, WM-OBJ-018, WM-SFT CHILD/REFERENCE, dangling-target, CLASSIFIES and WM-ACT-007 items.","expect":"Relation holds are explicit per package.","violates":["POL-REQ-requiresRelationHoldsEnumerated"],"closesDefect":["D16"]},

  {"id":"F-PRF-001","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"positive","input":"The profile carries all eleven required invariants plus the SKU, occurrence, firmware and EBOM-MBOM constraints.","expect":"The profile validates as complete against the settled boundary.","violates":["PROF-CON-completeness"],"closesDefect":["D4"]},
  {"id":"F-PRF-002","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"negative","input":"The profile omits one of the eleven required invariants.","expect":"The profile fails validation.","violates":["PROF-CON-completeness"],"closesDefect":["D4"],"expectedCode":"EMOPS04-E036"},
  {"id":"F-PRF-003","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"positive","input":"A seller-scoped SKU is profiled as a party-qualified alias on WM-OBJ-002 and a variant qualifier on WM-OBJ-017.","expect":"The scoped alias is accepted with no root and no serial identity.","violates":["LE-INV-04"],"closesDefect":["D4"]},
  {"id":"F-PRF-004","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"negative","input":"A SKU value is used to identify a serialized unit.","expect":"The conflation is rejected.","violates":["LE-INV-04"],"closesDefect":["D4"],"expectedCode":"EMOPS04-E021"},
  {"id":"F-PRF-005","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"negative","input":"A SKU value is used to identify an engineering design revision.","expect":"The conflation is rejected.","violates":["LE-INV-04"],"closesDefect":["D4"],"expectedCode":"EMOPS04-E022"},
  {"id":"F-PRF-006","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"positive","input":"A substitution carries direction, applicable design and baseline revisions, a bounded effectivity range, evidence and an approving authority.","expect":"The substitution is accepted.","violates":["LE-INV-03"],"closesDefect":["D10"]},
  {"id":"F-PRF-007","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"negative","input":"A substitution is recorded without an approving authority reference.","expect":"The substitution is rejected.","violates":["LE-INV-03"],"closesDefect":["D10"],"expectedCode":"EMOPS04-E010"},
  {"id":"F-PRF-008","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"negative","input":"A substitution is recorded with no effectivity bound in time, serial, lot or site.","expect":"The substitution is rejected and absence never implies interchangeability.","violates":["LE-INV-03"],"closesDefect":["D10"],"expectedCode":"EMOPS04-E009"},
  {"id":"F-PRF-009","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"negative","input":"A lot-bounded effectivity predicate is evaluated as satisfied while the Lot/Batch master is unassigned.","expect":"Evaluation is refused and the predicate is recorded unresolved, not defaulted.","violates":["LOT-INV-06"],"closesDefect":["D10"],"expectedCode":"EMOPS04-E011"},
  {"id":"F-PRF-010","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"positive","input":"authorityAssignments names the effectivity-authority owner, substitution approver and revision release owner.","expect":"Grok blocker (c) is closed by an explicit named owner.","violates":["LE-INV-03"],"closesDefect":["D3"]},
  {"id":"F-PRF-011","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"negative","input":"Baseline containment of the Substitution Rule is asserted without naming the effectivity-authority owner.","expect":"The containment assertion is rejected as governance-incomplete.","violates":["LE-INV-03"],"closesDefect":["D3"],"expectedCode":"EMOPS04-E010"},
  {"id":"F-PRF-012","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"positive","input":"Firmware 1.2.0 is a WM-SFT-008 release over a WM-SFT-007 component with a WM-SFT-012 SBOM record.","expect":"The three identities stay distinct and no root is invented.","violates":["LE-INV-08"],"closesDefect":["D14"]},
  {"id":"F-PRF-013","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"negative","input":"A firmware release is entered as an EBOM line or part number.","expect":"The entry is rejected.","violates":["LE-INV-08"],"closesDefect":["D14"],"expectedCode":"EMOPS04-E016"},
  {"id":"F-PRF-014","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"negative","input":"A firmware release is treated as the device it runs on.","expect":"The conflation is rejected.","violates":["LE-INV-08"],"closesDefect":["D14"],"expectedCode":"EMOPS04-E017"},
  {"id":"F-PRF-015","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"negative","input":"A WM-SFT-012 SBOM record is used as the identity of the firmware release.","expect":"The substitution of identity is rejected.","violates":["LE-INV-08"],"closesDefect":["D14"],"expectedCode":"EMOPS04-E018"},
  {"id":"F-PRF-016","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"positive","input":"The profile holds record states that the installation-occurrence model cited by WM-SFT-008 is unsupplied.","expect":"Firmware-to-item binding is recorded as an open hold, not a resolved relation.","violates":["LE-INV-08"],"closesDefect":["D14"]},
  {"id":"F-PRF-017","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"negative","input":"The firmware installation-occurrence model is cited as supplied and verified.","expect":"The citation is rejected as unsupplied.","violates":["POL-REQ-requiresReferenceStatusOnEveryReference"],"closesDefect":["D14","D15"],"expectedCode":"EMOPS04-E026"},
  {"id":"F-PRF-018","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"positive","input":"Two occurrences in baselines B1 and B2 share a displayed row number.","expect":"They remain distinct baseline-scoped identities and are never merged.","violates":["LE-INV-06"],"closesDefect":["D26"]},
  {"id":"F-PRF-019","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"negative","input":"A primary component and its approved alternate are summed as simultaneously installed quantity.","expect":"The summation is rejected; alternates are candidates only.","violates":["LE-INV-07"],"closesDefect":["D26"],"expectedCode":"EMOPS04-E015"},
  {"id":"F-PRF-020","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"positive","input":"A retired identifier is resolved through its tombstone record.","expect":"Resolution succeeds and history is preserved.","violates":["LE-INV-11"],"closesDefect":["D5"]},
  {"id":"F-PRF-021","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"negative","input":"A retired identifier is reassigned to a new subject.","expect":"The reuse is rejected.","violates":["LE-INV-11"],"closesDefect":["D5"],"expectedCode":"EMOPS04-E023"},
  {"id":"F-PRF-022","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"negative","input":"An identifier is retired with no tombstone written.","expect":"The retirement is rejected as unresolvable.","violates":["LE-INV-11"],"closesDefect":["D5"],"expectedCode":"EMOPS04-E024"},
  {"id":"F-PRF-023","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"positive","input":"An evidenced mapping links EBOM occurrences in B2 to MBOM operations in a released plan version.","expect":"Both masters stay independently versioned and the mapping carries evidence.","violates":["LE-INV-10"],"closesDefect":["D7"]},
  {"id":"F-PRF-024","target":"profile:enterprise-product-engineering-and-manufacturing","kind":"negative","input":"An EBOM baseline is consumed directly as a manufacturing plan with no reconciliation mapping.","expect":"The derivation is rejected; reuse of WM-OBJ-019 never implies MBOM.","violates":["LE-INV-10"],"closesDefect":["D7"],"expectedCode":"EMOPS04-E032"},

  {"id":"F-POL-001","target":"validation-policy/v2","kind":"positive","input":"All six validation-policy files declare format v2 with the full v2 requirement set.","expect":"Policy validation detects every class of defect D1 through D27.","violates":["POL-REQ-v2"],"closesDefect":["D21","D22"]},
  {"id":"F-POL-002","target":"validation-policy/v2","kind":"negative","input":"A negative fixture omits expectedCode.","expect":"The fixture file fails validation.","violates":["POL-REQ-negativeFixtureRequiredFields"],"closesDefect":["D20","D22"],"expectedCode":"EMOPS04-E037"},
  {"id":"F-POL-003","target":"validation-policy/v2","kind":"negative","input":"minimumReferences is satisfied using only unverified-draft or dangling targets.","expect":"The reference count is rejected under minimumVerifiedReferences.","violates":["POL-REQ-minimumVerifiedReferences"],"closesDefect":["D15"],"expectedCode":"EMOPS04-E025"},
  {"id":"F-POL-004","target":"validation-policy/v2","kind":"positive","input":"Each candidate cites at least two verified-supplied targets with explicit referenceStatus values.","expect":"Reference verification passes and unverified targets stay flagged.","violates":["POL-REQ-requiresReferenceStatusOnEveryReference"],"closesDefect":["D15"]},
  {"id":"F-POL-005","target":"validation-policy/v2","kind":"negative","input":"A candidate presents an empty holds array.","expect":"The candidate fails validation while allocation and publication remain pending.","violates":["POL-REQ-requiresHoldsNonEmpty"],"closesDefect":["D22","D25"],"expectedCode":"EMOPS04-E029"},
  {"id":"F-POL-006","target":"validation-policy/v2","kind":"negative","input":"modelId or registryId is set to a non-null value.","expect":"The candidate fails validation.","violates":["POL-REQ-modelIdMustBeNull"],"closesDefect":["D2"],"expectedCode":"EMOPS04-E002"},
  {"id":"F-POL-007","target":"validation-policy/v2","kind":"positive","input":"Every artifact decision value is a member of decisionEnum.","expect":"Decision enumeration validates across candidates and the profile.","violates":["POL-REQ-decisionEnum"],"closesDefect":["D22"]},
  {"id":"F-POL-008","target":"validation-policy/v2","kind":"negative","input":"canonicalPublishable is set to true on any artifact.","expect":"The artifact fails validation under the publication hold.","violates":["POL-REQ-canonicalPublishableMustBeFalse"],"closesDefect":["D22","D25"],"expectedCode":"EMOPS04-E029"},

  {"id":"F-ABA-001","target":"candidate-allocation-offline-as-built-assembly","kind":"positive","input":"A composition state is recorded with compositionValidFrom, derivedFromEventRefs and a membership carrying sourceEventRef.","expect":"The actual-state record validates with event derivation explicit.","violates":["ABA-INV-01","ABA-INV-03"],"closesDefect":["D9"]},
  {"id":"F-ABA-002","target":"candidate-allocation-offline-as-built-assembly","kind":"negative","input":"effectiveFrom or an effectivity predicate is used to express as-built composition validity.","expect":"The field is rejected; actual-state models carry no effectivity vocabulary.","violates":["ABA-INV-02","LE-INV-05"],"closesDefect":["D9"],"expectedCode":"EMOPS04-E012"},
  {"id":"F-ABA-003","target":"candidate-allocation-offline-as-built-assembly","kind":"negative","input":"A membership sets validTo with no closingEventRef.","expect":"The closure is rejected as unevidenced.","violates":["ABA-INV-06","ABA-INV-03"],"closesDefect":["D19"],"expectedCode":"EMOPS04-E013"},
  {"id":"F-ABA-004","target":"candidate-allocation-offline-as-built-assembly","kind":"positive","input":"A membership quantity states value, unitCode, unitCodeListVersion and basis.","expect":"The quantity validates under the shared Quantity shape.","violates":["ABA-INV-04","LE-INV-02"],"closesDefect":["D8"]},
  {"id":"F-ABA-005","target":"candidate-allocation-offline-as-built-assembly","kind":"negative","input":"A membership quantity states a unit but no basis.","expect":"The quantity is rejected.","violates":["ABA-INV-04","LE-INV-02"],"closesDefect":["D8"],"expectedCode":"EMOPS04-E008"},
  {"id":"F-ABA-006","target":"candidate-allocation-offline-as-built-assembly","kind":"negative","input":"A composition assertion omits assertionBasis so declared and observed content merge.","expect":"The assertion is rejected.","violates":["ABA-INV-01"],"closesDefect":["D11"],"expectedCode":"EMOPS04-E030"},
  {"id":"F-ABA-007","target":"candidate-allocation-offline-as-built-assembly","kind":"negative","input":"The as-built record asserts lot identity for a consumed bulk component.","expect":"The assertion is rejected; lot identity is mastered elsewhere.","violates":["ABA-INV-01","LE-INV-09"],"closesDefect":["D17"],"expectedCode":"EMOPS04-E038"},
  {"id":"F-ABA-008","target":"candidate-allocation-offline-as-built-assembly","kind":"negative","input":"Firmware 1.2.0 is recorded as a component membership of the serialized parent.","expect":"The membership is rejected; firmware presence requires an external installation occurrence.","violates":["ABA-INV-08","LE-INV-08"],"closesDefect":["D14"],"expectedCode":"EMOPS04-E016"},
  {"id":"F-ABA-009","target":"candidate-allocation-offline-as-built-assembly","kind":"positive","input":"WM-FLW-013 is referenced as verified-supplied so every genealogy edge must cite an actual event with evidence.","expect":"The reference set satisfies minimumVerifiedReferences.","violates":["ABA-INV-01","LE-INV-05"],"closesDefect":["D15"]},
  {"id":"F-ABA-010","target":"candidate-allocation-offline-as-built-assembly","kind":"negative","input":"The lifecycle retains the intent-time state 'effective' for an actual composition record.","expect":"The lifecycle is rejected; 'current' replaces it.","violates":["ABA-INV-02"],"closesDefect":["D6"],"expectedCode":"EMOPS04-E004"},
  {"id":"F-ABA-011","target":"candidate-allocation-offline-as-built-assembly","kind":"negative","input":"A component with no event evidence is recorded with quantity zero instead of unknown.","expect":"The collapse is rejected; unknown stays explicit.","violates":["ABA-INV-10"],"closesDefect":["D27"],"expectedCode":"EMOPS04-E039"},

  {"id":"F-LOT-001","target":"candidate-allocation-offline-lot-batch","kind":"positive","input":"Two lots share lotCode 'A-77' under different issuers and schemes.","expect":"Both validate; the alternate key is issuer and scheme scoped.","violates":["LOT-INV-01"],"closesDefect":["D5"]},
  {"id":"F-LOT-002","target":"candidate-allocation-offline-lot-batch","kind":"negative","input":"Two lots share lotCode, issuerRef and identifierSchemeRef with different lotId values.","expect":"The second lot is rejected on the alternate key.","violates":["LOT-INV-01"],"closesDefect":["D5"],"expectedCode":"EMOPS04-E003"},
  {"id":"F-LOT-003","target":"candidate-allocation-offline-lot-batch","kind":"positive","input":"A serialized member is bound to lot L by a LotMembership with memberKind, validFrom, sourceEventRef and assertionBasis.","expect":"Membership validates as provenance only.","violates":["LOT-INV-03"],"closesDefect":["D19"]},
  {"id":"F-LOT-004","target":"candidate-allocation-offline-lot-batch","kind":"negative","input":"A lot membership is asserted with no sourceEventRef.","expect":"The membership is rejected as unevidenced.","violates":["LOT-INV-03","LOT-INV-05"],"closesDefect":["D19"],"expectedCode":"EMOPS04-E013"},
  {"id":"F-LOT-005","target":"candidate-allocation-offline-lot-batch","kind":"positive","input":"Lot L is lifecycleState partiallyConsumed and dispositionState quarantined at the same time.","expect":"Both axes record independently with dispositionValidFrom.","violates":["LOT-INV-07"],"closesDefect":["D6"]},
  {"id":"F-LOT-006","target":"candidate-allocation-offline-lot-batch","kind":"negative","input":"Quarantine is written into the single collapsed lifecycle field, erasing the consumption state.","expect":"The collapse is rejected.","violates":["LOT-INV-07"],"closesDefect":["D6"],"expectedCode":"EMOPS04-E004"},
  {"id":"F-LOT-007","target":"candidate-allocation-offline-lot-batch","kind":"negative","input":"A lot quantity carries a unit with no basis or unit code-list version.","expect":"The quantity is rejected.","violates":["LOT-INV-04","LE-INV-02"],"closesDefect":["D8"],"expectedCode":"EMOPS04-E008"},
  {"id":"F-LOT-008","target":"candidate-allocation-offline-lot-batch","kind":"negative","input":"The lot record asserts the as-built composition of a serialized member.","expect":"The assertion is rejected as outside lot mastership.","violates":["LOT-INV-03","LE-INV-05"],"closesDefect":["D17"],"expectedCode":"EMOPS04-E038"},
  {"id":"F-LOT-009","target":"candidate-allocation-offline-lot-batch","kind":"negative","input":"A recalled lot's identifier is reassigned to a replacement batch.","expect":"The reuse is rejected and recall genealogy is preserved.","violates":["LOT-INV-08","LOT-INV-09"],"closesDefect":["D5"],"expectedCode":"EMOPS04-E023"},

  {"id":"F-MBM-001","target":"candidate-allocation-offline-manufacturing-plan","kind":"positive","input":"A released plan version states bomKind MBOM, an immutable version and a contentDigest.","expect":"The plan version validates and is distinguishable from any EBOM version.","violates":["MBOM-INV-01","LE-INV-01"],"closesDefect":["D7"]},
  {"id":"F-MBM-002","target":"candidate-allocation-offline-manufacturing-plan","kind":"negative","input":"A plan version is released with no bomKind field.","expect":"The release is rejected.","violates":["MBOM-INV-01","LE-INV-01"],"closesDefect":["D7"],"expectedCode":"EMOPS04-E005"},
  {"id":"F-MBM-003","target":"candidate-allocation-offline-manufacturing-plan","kind":"negative","input":"Operations are edited in place on a released plan version.","expect":"The mutation is rejected; a successor version is required.","violates":["MBOM-INV-09"],"closesDefect":["D7"],"expectedCode":"EMOPS04-E006"},
  {"id":"F-MBM-004","target":"candidate-allocation-offline-manufacturing-plan","kind":"negative","input":"A yield or scrap assumption is reported as an observed production outcome.","expect":"The reclassification is rejected.","violates":["MBOM-INV-08","LE-INV-05"],"closesDefect":["D7","D11"],"expectedCode":"EMOPS04-E012"},
  {"id":"F-MBM-005","target":"candidate-allocation-offline-manufacturing-plan","kind":"positive","input":"ebomMappings link baseline B2 occurrences to plan operations with evidence references.","expect":"The reconciliation validates as an evidenced mapping between separate masters.","violates":["MBOM-INV-06","LE-INV-10"],"closesDefect":["D7"]},
  {"id":"F-MBM-006","target":"candidate-allocation-offline-manufacturing-plan","kind":"negative","input":"An ebomMapping entry is written with no evidence reference.","expect":"The mapping is rejected.","violates":["MBOM-INV-06","LE-INV-10"],"closesDefect":["D7"],"expectedCode":"EMOPS04-E032"},

  {"id":"F-PWO-001","target":"candidate-allocation-offline-production-work-order","kind":"positive","input":"An order pins planVersionRef, designRevisionRef and ebomBaselineVersionRef, with quantity stating unit and basis and an explicit decisionRef.","expect":"The authorization validates with all three versions immutably pinned.","violates":["PWO-INV-01","PWO-INV-03","PWO-INV-04"],"closesDefect":["D13"]},
  {"id":"F-PWO-002","target":"candidate-allocation-offline-production-work-order","kind":"negative","input":"An order omits designRevisionRef while claiming pinned definitions.","expect":"The authorization is rejected.","violates":["PWO-INV-03"],"closesDefect":["D13"],"expectedCode":"EMOPS04-E033"},
  {"id":"F-PWO-003","target":"candidate-allocation-offline-production-work-order","kind":"negative","input":"An order references WM-OBJ-019 without an ebomBaselineVersionRef.","expect":"The authorization is rejected as unpinned.","violates":["PWO-INV-03"],"closesDefect":["D13"],"expectedCode":"EMOPS04-E033"},
  {"id":"F-PWO-004","target":"candidate-allocation-offline-production-work-order","kind":"negative","input":"A closed order with no execution events is reported as 100 units produced rather than execution unknown.","expect":"The inference is rejected and execution stays explicitly unknown.","violates":["PWO-INV-06","PWO-INV-10"],"closesDefect":["D13","D27"],"expectedCode":"EMOPS04-E034"},
  {"id":"F-PWO-005","target":"candidate-allocation-offline-production-work-order","kind":"negative","input":"A material reservation is posted as actual consumption against a lot.","expect":"The posting is rejected.","violates":["PWO-INV-07","LE-INV-05"],"closesDefect":["D13"],"expectedCode":"EMOPS04-E035"},
  {"id":"F-PWO-006","target":"candidate-allocation-offline-production-work-order","kind":"negative","input":"An order states quantity 100 with no unitCode.","expect":"The authorization is rejected.","violates":["PWO-INV-02","LE-INV-02"],"closesDefect":["D8"],"expectedCode":"EMOPS04-E007"},

  {"id":"F-ATE-001","target":"candidate-allocation-offline-transformation-event","kind":"positive","input":"An event records eventTime and recordedAt as distinct RFC 3339 values with explicit offsets.","expect":"Both times persist separately and neither overwrites the other.","violates":["ATE-INV-04"],"closesDefect":["D12"]},
  {"id":"F-ATE-002","target":"candidate-allocation-offline-transformation-event","kind":"negative","input":"recordedAt is omitted and eventTime is reused as the record time, or an offset is absent.","expect":"The event is rejected.","violates":["ATE-INV-04"],"closesDefect":["D12"],"expectedCode":"EMOPS04-E031"},
  {"id":"F-ATE-003","target":"candidate-allocation-offline-transformation-event","kind":"positive","input":"A correction appends a successor with supersedesRef, correctedAt and correctionAuthorityRef while the original is retained.","expect":"The correction validates and the original remains resolvable.","violates":["ATE-INV-08"],"closesDefect":["D18"]},
  {"id":"F-ATE-004","target":"candidate-allocation-offline-transformation-event","kind":"negative","input":"An event is set to status corrected with no supersedesRef.","expect":"The status change is rejected.","violates":["ATE-INV-08"],"closesDefect":["D18"],"expectedCode":"EMOPS04-E040"},
  {"id":"F-ATE-005","target":"candidate-allocation-offline-transformation-event","kind":"negative","input":"An event is voided without voidReason and voidAuthorityRef and the original payload is removed.","expect":"The void is rejected.","violates":["ATE-INV-08"],"closesDefect":["D18"],"expectedCode":"EMOPS04-E014"},
  {"id":"F-ATE-006","target":"candidate-allocation-offline-transformation-event","kind":"negative","input":"An output quantity is recorded with no unitCode or basis.","expect":"The event is rejected.","violates":["ATE-INV-03","LE-INV-02"],"closesDefect":["D8"],"expectedCode":"EMOPS04-E007"},
  {"id":"F-ATE-007","target":"candidate-allocation-offline-transformation-event","kind":"positive","input":"Consumption of the approved alternate is recorded with assertionBasis observed and attributable evidence.","expect":"The actual consumption fact validates and proves which alternate was installed.","violates":["ATE-INV-07","LE-INV-05"],"closesDefect":["D11"]},
  {"id":"F-ATE-008","target":"candidate-allocation-offline-transformation-event","kind":"negative","input":"An output is recorded with neither a distinct identity nor a lot binding.","expect":"The event is rejected and the output remains unknown rather than inferred.","violates":["ATE-INV-06","ATE-INV-10"],"closesDefect":["D19","D27"],"expectedCode":"EMOPS04-E013"},
  {"id":"F-ATE-009","target":"candidate-allocation-offline-transformation-event","kind":"positive","input":"WM-FLW-013 is referenced as verified-supplied and WM-MAT-008 and WM-KNW-008 are flagged unverified-draft.","expect":"Reference verification passes with incomplete targets explicitly held.","violates":["POL-REQ-requiresReferenceStatusOnEveryReference"],"closesDefect":["D15"]}
]
```

---

## 4. Exact final fixture counts

| Target | Existing | Added | Final | Positive | Negative |
|---|---|---|---|---|---|
| `contour:EM-OPS-04` | 0 | 14 | 14 | 5 | 9 |
| `profile:enterprise-product-engineering-and-manufacturing` | 0 | 24 | 24 | 9 | 15 |
| `validation-policy/v2` | 0 | 8 | 8 | 3 | 5 |
| `candidate-allocation-offline-as-built-assembly` | 4 | 11 | 15 | 5 | 10 |
| `candidate-allocation-offline-lot-batch` | 4 | 9 | 13 | 5 | 8 |
| `candidate-allocation-offline-manufacturing-plan` | 4 | 6 | 10 | 4 | 6 |
| `candidate-allocation-offline-production-work-order` | 4 | 6 | 10 | 3 | 7 |
| `candidate-allocation-offline-transformation-event` | 4 | 9 | 13 | 6 | 7 |
| **Total** | **20** | **87** | **107** | **40** | **67** |

Existing split: 10 positive, 10 negative. Added split: 30 positive, 57 negative. Every negative in the final set carries an `expectedCode` resolving in `error-codes.json`; every one of the 107 cases carries `id`, `target`, `kind`, `input`, `expect`, `violates` and a non-empty `closesDefect` array after D20. Every package meets `minimumFixtures: 6`, `minimumPositiveFixtures: 2` and `minimumNegativeFixtures: 3` under policy v2. Every defect D1–D27 is closed by at least one fixture; defect-to-fixture coverage: D1→F-CON-001/002/003/004; D2→F-CON-005/006, F-POL-006; D3→F-PRF-010/011; D4→F-PRF-001/002/003/004/005; D5→F-LOT-001/002/009, F-PRF-020/021/022; D6→F-ABA-010, F-LOT-005/006; D7→F-MBM-001..006, F-PRF-023/024; D8→F-ABA-004/005, F-LOT-007, F-PWO-006, F-ATE-006; D9→F-ABA-001/002; D10→F-PRF-006..009; D11→F-ABA-006, F-ATE-007, F-MBM-004; D12→F-ATE-001/002, plus existing `planned-as-actual`; D13→F-PWO-001..005, plus existing `released-order`, `completed-order`, `closed-proof`, `floating-plan`; D14→F-PRF-012..017, F-ABA-008; D15→F-POL-003/004, F-ABA-009, F-ATE-009, F-CON-006; D16→F-CON-012/013/014; D17→F-ABA-007, F-LOT-008, plus existing `serial-collapse`; D18→F-ATE-003/004/005, plus existing `overwrite`, `silent-replacement`; D19→F-ABA-003, F-LOT-003/004, F-ATE-008, plus existing `attached-component`, `detached-component`, `split`, `consume-produce`, `assembly`; D20→F-CON-008, F-POL-002; D21→F-CON-007, F-POL-001; D22→F-POL-001/005/007/008; D23→F-CON-007; D24→F-CON-009; D25→F-CON-009/010/011, F-POL-005/008; D26→F-CON-003, F-PRF-018/019; D27→F-ABA-011, F-PWO-004, F-ATE-008.

---

## 5. Freeze decision

**FROZEN.** This is the single final semantic audit of EM-OPS-04 and no rerun, re-review or further provider pass is required or requested.

The boundary decision is settled and preserved verbatim: the ItemDefinition split across WM-OBJ-002 and WM-OBJ-018, SKU as a party-scoped identifier, Engineering Revision contained in WM-OBJ-018, WM-OBJ-019 reused for EBOM only, BOM Line and Substitution Rule contained and baseline-scoped, five roots left identifier-unassigned, and zero identifiers allocated. Claude and Grok reconcile to that same decision once Grok's containment/reuse condition is checked against WM-OBJ-018's and WM-OBJ-019's own mastership and out-of-scope statements, which satisfy it, and once Grok's four contradicted "missing root" claims are rejected on frozen evidence. Grok's one unclosed finding — the unnamed effectivity-authority owner — is closed by D3. No supplied evidence proves the decision inconsistent, so nothing is reopened.

The 27 defects are artifact-level, not boundary-level. Every remediation in §2 is a literal field or value edit plus the 87 fixture additions in §3, all mechanically applicable by a local script against the frozen files with no judgment, no new identifier, no promotion of an unassigned candidate, no invented internal schema for WM-OBJ-002/017/018/019/001, WM-SFT-007/008/012 or WM-FLW-013, and no external lookup. Applying D1–D27 and the fixture set closes the audit in a single deterministic pass, after which the packages are internally consistent, policy-detectable and fully fixture-covered.

The following remain open as recorded holds and are deliberately not closed by this audit, because closing them requires authority this audit does not hold: identifier allocation for the five unassigned roots; the WM-OBJ-019/WM-OBJ-002, WM-OBJ-018 and WM-SFT CHILD/REFERENCE relation contradictions; the dangling targets WM-OBJ-012/020/021/022 and WM-ACT-015; the absence of CLASSIFIES from the relation enum; WM-ACT-007's maintenance scope and K11 duplication; the unsupplied firmware installation-occurrence model; the absence of crosswalks; lot-bounded effectivity resolvability; and the single-provider, reviewable-draft status of most bases. After remediation these are explicitly declared in `holds`, `unresolvedReferences`, `publication-hold.json` and `crosswalk-hold.json` rather than silently carried.

Publication, canonical promotion, installability and runtime registration remain held. No publication-readiness, canonical-completeness or installability claim is made.
