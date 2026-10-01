# EM-LND-11 — Final Frozen Semantic Audit

Materials used: `local-evidence.md`, `claude-study.raw.md`, `grok-study.raw.md`, `candidate-profile-offline/{profile-candidate.json, fixtures.json, README.md}`, `checkpoint-manifest.json`, `CONTINUATION.md`. No tools, no browsing, no external facts. Defect IDs (`D…`), invariant IDs (`INV-…`), fixture IDs (`EM-LND-11-FX-…`) and error codes are audit/test labels only — they are not catalogue or runtime identifiers and allocate nothing.

---

## 1. Verdict on decision and artifacts

**The boundary is settled, and it is preserved.**

Claude and the visible Grok response converge independently on the same disposition, and the supplied evidence contains nothing that contradicts it:

- **Operations Landscape** — accepted as a governed declaration plus a reproducible, exception-aware projection, holding *artifact* identity only (viewpoint, scope, pinned source revisions, as-of, completeness perimeter, freshness, disclosure policy, projection digest, gap/conflict register). Not a subject root. Never mutates sources.
- **Supply Network** — rejected as a stable subject root; accepted as one scoped graph view/declaration hosted inside the landscape declaration, over party, facility and supply-relation masters it cannot itself master.
- **No identifier allocated**; the nine named gaps (Lot/Batch, Handling Unit, As-Built Assembly, Party/Supplier, Facility/Location, Supply Relationship, Transformation Plan, Actual Consumption/Production Event, Occurrence/Event) stay identifier-unassigned and unpromoted.
- All fourteen bases are reused as non-canonical drafts; no publication or installability claim.

Reconciliation of the two studies produces three genuine deltas, all **tightening** and none inconsistent with the decision, so they are folded in rather than used to reopen it:

1. **Quantity bound on proof** (Grok only): a proven-affected output is proven *only to the consumed quantity cited by the event*. Claude's and the local synthesis' "proven affected" is unbounded. Grok is correct on the evidence: an edge citing quantity cannot prove more than the quantity it cites. Folded in as INV-15.
2. **Unknown-origin break cannot be bridged by a view edge** (Grok invariant 14): neither a network path nor a landscape projection may close the supplier break. Claude implies this; it is not stated as an invariant anywhere in the artifacts. Folded in as INV-14.
3. **Apparent conflict on the unknown-supplier break** — Grok folds it into *not-evidenced*; Claude and the local synthesis treat it as an *incomplete result* with residual uncertainty. This is an axis conflation, not a disagreement: per-item classification (`proven-affected | potentially-affected | not-evidenced`) and per-result completeness (`complete-within-declared-perimeter | incomplete`) are distinct fields. Both readings hold once separated; neither is overturned. Captured as D12.

**Artifacts: not acceptable as frozen.** The decision is sound but the four artifacts under-encode it. `profile-candidate.json` carries eight prose constraints and no invariant registry, no mastership map, no as-of, no source pins, no projection digest, no access policy, no time/quantity rules, and a `holds` list that collapses nine gaps into eight names and is now stale on Grok. `fixtures.json` has seven prose cases with no `target`, `violates`, `closesDefect` or error codes, one of which conflates two separate inferences, and it does not exercise the majority of the stated invariants. `checkpoint-manifest.json` records one provider study, still reports the Grok prompt as unsent, omits the Grok response and the whole `candidate-profile-offline/` directory from `files`, and carries a bare untyped date. `README.md` states neither non-canonicity nor the gaps. `CONTINUATION.md` is stale on Grok and on fixture absence. The frozen evidence also exposes one arithmetic defect inside Claude's own study (ten vs eleven single-provider bases).

All thirty defects below are encoding, enumeration, schema and staleness defects. Each has a closed-form literal edit. **None requires rerunning a provider study, re-reading the dossier, or reopening the boundary.**

---

## 2. Material defects and exact deterministic remediation

Paths are JSON pointers relative to the named file. `+=` means append to array. Where a value is not derivable from frozen materials it is written as an explicit-unknown marker or a `to-be-computed` status — **no digest, revision, timestamp or provider setting is invented.**

### D1 — Identity: artifact identity vs subject identity is not encoded
`profile-candidate.json` asserts the distinction only in prose, so a consumer can read `decision:"PROFILE"` as a root.

```
/identity = {
  "operationsLandscape": {"identityClass":"declaration-artifact","subjectIdentityMinted":false,"rootPromotionAllowed":false},
  "supplyNetwork": {"identityClass":"view-definition","subjectIdentityMinted":false,"rootPromotionAllowed":false,"hostedIn":"operationsLandscape.declaration"},
  "projection": {"identityClass":"derived-output","subjectIdentityMinted":false,"rootPromotionAllowed":false,"mayBeCitedAsMaster":false}
}
```

### D2 — Mastership: no fact→owner map; nine gaps collapsed to eight names
`/holds/0` reads "…transformation plan **and event masters**", merging two distinct unassigned boundaries (Actual Consumption/Production Event; Occurrence/Event) that `checkpoint-manifest.json:/unassignedCandidates` keeps separate.

```
/mastership = {
  "productType":"WM-OBJ-002","variant":"WM-OBJ-017","design":"WM-OBJ-018",
  "engineeringBomRevisionAndOccurrence":"WM-OBJ-019","serializedItem":"WM-OBJ-001",
  "stockPosition":"WM-OBJ-020","inventoryMovement":"WM-FLW-012","shipmentConsignment":"WM-FLW-011",
  "goodsMovementFlow":"WM-FLW-004","traceGraphResult":"WM-FLW-013","maintenanceWorkOrder":"WM-ACT-007",
  "purchaseOrder":"WM-ECO-019","salesOrder":"WM-ECO-020","fulfilmentCase":"WM-ECO-024"
}
/mastership/_rules = {"ownersPerFact":1,"unknownMastershipBlocksMutation":true,"alignmentMayBeMaster":false}
/unmasteredFacts = [
  {"name":"Lot / Batch","identifierUnassigned":true,"promoted":false},
  {"name":"Handling Unit","identifierUnassigned":true,"promoted":false},
  {"name":"As-Built Assembly","identifierUnassigned":true,"promoted":false},
  {"name":"Party / Supplier","identifierUnassigned":true,"promoted":false},
  {"name":"Facility / Location","identifierUnassigned":true,"promoted":false},
  {"name":"Supply Relationship","identifierUnassigned":true,"promoted":false},
  {"name":"Transformation Plan","identifierUnassigned":true,"promoted":false},
  {"name":"Actual Consumption / Production Event","identifierUnassigned":true,"promoted":false},
  {"name":"Occurrence / Event","identifierUnassigned":true,"promoted":false}
]
/holds/0 = "Nine subject/event boundaries remain identifier-unassigned in owning contours and are not promoted here; see /unmasteredFacts for the exact nine, which must match checkpoint-manifest.json:/unassignedCandidates element-for-element."
```
Assertion for the script: `len(/unmasteredFacts) == 9` and its `name` list equals `/unassignedCandidates` exactly.

### D3 — Declaration/projection reproducibility is claimed but unencodable
Constraint `/constraints/2` demands as-of, pins and digest; the profile carries none, so it violates its own rule.

```
/projection = {
  "asOf": {"status":"unbound","boundAtProjectionTime":true,"format":"RFC3339-seconds-explicit-offset"},
  "ruleSetVersion": {"status":"unbound"},
  "sourceRevisionPins": [
    {"base":"WM-OBJ-001","revision":null,"pinStatus":"unpinned"},
    {"base":"WM-OBJ-002","revision":null,"pinStatus":"unpinned"},
    {"base":"WM-OBJ-017","revision":null,"pinStatus":"unpinned"},
    {"base":"WM-OBJ-018","revision":null,"pinStatus":"unpinned"},
    {"base":"WM-OBJ-019","revision":null,"pinStatus":"unpinned"},
    {"base":"WM-OBJ-020","revision":null,"pinStatus":"unpinned"},
    {"base":"WM-FLW-004","revision":null,"pinStatus":"unpinned"},
    {"base":"WM-FLW-011","revision":null,"pinStatus":"unpinned"},
    {"base":"WM-FLW-012","revision":null,"pinStatus":"unpinned"},
    {"base":"WM-FLW-013","revision":null,"pinStatus":"unpinned"},
    {"base":"WM-ACT-007","revision":null,"pinStatus":"unpinned"},
    {"base":"WM-ECO-019","revision":null,"pinStatus":"unpinned"},
    {"base":"WM-ECO-020","revision":null,"pinStatus":"unpinned"},
    {"base":"WM-ECO-024","revision":null,"pinStatus":"unpinned"}
  ],
  "digestAlgorithm":"sha256",
  "digestStatus":"to-be-computed-at-projection-time",
  "reproducibility":"byte-identical-for-identical-declaration-plus-pins-plus-asOf-plus-ruleSetVersion",
  "mutatesSources": false,
  "emissionBlockedWhen": ["asOf.status=unbound","any sourceRevisionPins[].pinStatus=unpinned","ruleSetVersion.status=unbound","completenessPerimeter missing"]
}
/viewDeclarationRequiredFields = ["viewpoint","stakeholderConcerns","scope","asOf","freshnessPolicy","completenessPerimeter","disclosurePolicy","projectionDigest","gapRegister","conflictRegister"]
```

### D4 — Graph scope: network may silently invent edges
`/constraints/3` states edge attributes but not permitted edge provenance, and nothing forbids a network path standing in as genealogy or closing an origin break.

```
/supplyNetworkScope = {
  "nodeTypes":["party-supplier","facility-location"],
  "edgeTypes":["supply-relation"],
  "edgeDerivationAllowedFrom":["supply-relation-master","actual-movement-event"],
  "edgeDerivationForbiddenFrom":["co-location","shared-scope","projection-inference","engineering-bom","plan"],
  "edgeRequiredFields":["validityInterval","determinationMethod","evidenceRef","confidence"],
  "absenceSemantics":"unobserved",
  "absenceClaimRequiresClosedVersionedPerimeter":true,
  "mayServeAsGenealogyEdge":false,
  "mayCloseUnknownOriginBreak":false,
  "mayMasterPartyOrFacilityOrRelation":false
}
```

### D5 — Design-versus-actual: WM-OBJ-019 sub-rules and plan substitution unencoded
`/constraints/4` covers BOM only; engineering occurrence, candidate alternates, nominal aggregates and transformation-plan substitution are unguarded.

```
/designVsActual = {
  "designArtifacts":["product-type","variant","design","engineering-bom","transformation-plan"],
  "provesActualComposition": false,
  "boundsPossibleComposition": true,
  "engineeringOccurrenceIsSerializedItem": false,
  "candidateAlternateImpliesInstalled": false,
  "nominalAggregateIsMeasuredProperty": false,
  "planQuantityLocationPartySubstitutesForExecuted": false,
  "authorizationProvesExecution": false
}
/constraints/4 = "BOM, design, variant and transformation plan bound possible composition only; they never prove actual lot or serial composition, and genealogy edges require a cited actual event with evidence."
```

### D6 — Lot / serial / bulk identity classes not separated
`/constraints/1` lists "serialized item" but no lot, bulk or handling-unit class, so WM-OBJ-001's refusal and its missing-sibling redirect are invisible.

```
/materialIdentityClasses = {
  "serializedItem": {"master":"WM-OBJ-001","requiresIndividuatingBoundary":true},
  "lotBatch": {"master":null,"identifierUnassigned":true,"lotMembership":"provenance-not-instance-identity"},
  "bulkFungible": {"master":null,"identifierUnassigned":true,"redirectedBy":"WM-OBJ-001","mayReceiveSerializedIdentity":false},
  "handlingUnit": {"master":null,"identifierUnassigned":true,"containsSemantics":"typed-membership-only","packingProvesContents":false},
  "asBuiltAssembly": {"master":null,"identifierUnassigned":true,"requiresActualConsumptionAndProductionEvents":true}
}
```

### D7 — Stock / movement / posting rules absent from the profile
`missing-stock-zero` exists only as a fixture; the profile states no rule, and "count is not posting authority" and "stock is not a genealogy node" appear nowhere.

```
/stockAndPosting = {
  "missingRowIsZero": false,
  "countAuthorizesPosting": false,
  "stockPositionIsMovement": false,
  "stockPositionIsGenealogyNode": false,
  "planIsMovement": false,
  "movementIsPosting": false,
  "authoritativePosting": {"ownedBy":"external-system","referencedVia":"WM-FLW-012","inferredFromCount":false}
}
```

### D8 — Shipment/consignment discriminator and cardinality unencoded
```
/shipmentConsignment = {
  "semanticKindRequired": true,
  "semanticKindEnum": ["trade-shipment","transport-consignment","combined-view"],
  "allocationCardinality": "many-to-many",
  "forcedOneToOneAllowed": false,
  "handlingUnitContains": "typed-membership-only"
}
```

### D9 — Custody/title and location/custody collapsed into one prose clause
`/constraints/5` lists "custody transfer" among distinct events but never denies the two dangerous inferences.

```
/custodyAndTitle = {
  "locationImpliesCustody": false,
  "scanImpliesCustodyTransfer": false,
  "custodyImpliesTitle": false,
  "statusCodeImpliesClearance": false,
  "custodyImpliesInstanceContinuity": false
}
```

### D10 — Delivery/acceptance axes not enumerated
```
/fulfilmentAxes = {
  "axes": ["dispatch","handover","receipt","inspection","acceptance","completion"],
  "independent": true,
  "receiptImpliesAcceptance": false,
  "dispatchImpliesCompletion": false,
  "scanImpliesAcceptance": false,
  "acceptanceImpliesTitle": false
}
```

### D11 — Genealogy edge required-field list exists only in prose
```
/genealogyEdge = {
  "requiredFields": ["relationType","citedActualEventRef","quantityValue","quantityUnit","eventTime","recordTime","readPoint","businessLocation","capacityOrYield","sourceSystem","assertingAgent","determinationMethod","confidence","evidenceDigest"],
  "relationTypeEnum": ["aggregation","disaggregation","transformation","custody"],
  "locationOrExplicitUnknownRequired": true,
  "edgeMode": {"enum":["declared","observed","inferred"],"required":true,"inferredPromotableToAsserted":false},
  "alignmentAsEdgeSource": {"allowed":false,"note":"EPCIS/CBV alignments on WM-OBJ-001, WM-FLW-012, WM-FLW-013 are alignments, not genealogy masters"},
  "massBalanceOrBlendedEdgeImpliesOneToOneContinuity": false
}
```

### D12 — Incomplete trace: item classification and result completeness share one axis
This is the Claude/Grok reconciliation point. Split the axes so both readings hold.

```
/traceResult = {
  "perItemClassificationField": "classification",
  "perResultCompletenessField": "traceCompleteness",
  "traceCompletenessEnum": ["complete-within-declared-perimeter","incomplete"],
  "unknownOriginMarkerRequired": true,
  "unknownOriginRepresentation": "explicit-marker-never-null-never-empty",
  "residualUncertaintyRequiredWhenIncomplete": true,
  "completeRequiresClosedVersionedPerimeterAndZeroUnknownOriginMarkers": true
}
```

### D13 — Recall classification: no enum, no reason codes, no quantity bound, no "not cleared" guard
```
/recall = {
  "classificationEnum": ["proven-affected","potentially-affected","not-evidenced"],
  "closedWorldTermsForbidden": ["unaffected","cleared","safe"],
  "clearanceRequiresClosedVersionedPerimeter": true,
  "provenAffectedRequires": ["citedActualConsumptionOrTransformationEvent","quantityValue","quantityUnit","eventTime","readPointOrExplicitUnknown","verifiedEvidenceDigest"],
  "provenAffectedQuantityBound": "consumed-quantity-cited-by-event-only",
  "potentiallyAffectedReasonCodeRequired": true,
  "potentiallyAffectedReasonEnum": ["MASS_BALANCE","CONTROLLED_BLENDING","RESIDENCY_WINDOW","INFERRED_EDGE","STALE_EDGE","UNSERIALIZED_BULK","PARTIAL_LINKING_EVENT","SHARED_HANDLING_CONTEXT"],
  "bomOnlyMatch": "not-evidenced",
  "planOnlyMatch": "not-evidenced",
  "siblingLotOfUnresolvedSupplier": "not-evidenced",
  "decisionAuthority": "accountable-authority-outside-landscape"
}
```
Also amend the two existing positive fixtures so they assert the bound and the reason code:
```
fixtures.json:/cases/0/expect = "Those units are proven affected, bounded by the consumed quantity cited by each event, with cited events and verified evidence digests."
fixtures.json:/cases/1/expect = "They are potentially affected with reasonCode MASS_BALANCE and explicit residual uncertainty."
```

### D14 — Time: bare untyped dates; no axis separation; no backdating guard
`checkpoint-manifest.json:/checkpointDate = "2026-09-26"` is an untyped day string with no axis and no offset, while the frozen invariants require RFC 3339 with seconds and explicit offset for instants. Do not invent a time of day.

```
profile-candidate.json:/time = {
  "axes": ["event","effective","observation","record","posting","ingestion","publication","correction"],
  "axesCollapsible": false,
  "instantFormat": "RFC3339-seconds-explicit-offset",
  "declarationEffectiveTimeBackdatesExecution": false
}
checkpoint-manifest.json:/checkpointDate = {"value":"2026-09-26","precision":"day","timeAxis":"record","offsetKnown":false}
checkpoint-manifest.json:/auditDate = {"value":"2026-10-01","precision":"day","timeAxis":"record","offsetKnown":false}
```

### D15 — Quantity/unit and null semantics absent from the profile
```
/quantity = {
  "requiredFields": ["itemScope","value","unit","unitCodeList","unitCodeListVersion","precision","measurementBasis"],
  "quantityWithoutUnitValidOnEvidenceEdge": false,
  "nullSemanticsEnum": ["unknown","zero","not-applicable","withheld","suppressed"],
  "nullSemanticsCollapsible": false
}
```

### D16 — Authority: prohibited actions not enumerated
```
/authority = {
  "prohibitedForLandscapeAndNetworkAndProjection": ["allocate-identifier","dispatch","post","accept","recall","enforce","clear","mutate-source"],
  "recallAndEnforcementOwner": "accountable-authority-outside-landscape",
  "viewOutputKind": "read-only-candidate-set"
}
```

### D17 — Provenance: single-provider base count is wrong, and the profile records none
`claude-study.raw.md` Holds says "ten carry single-provider waivers", but its Evidence section enumerates ten Codex-only waivers **plus** the WM-ECO-020 Claude-only waiver, against three dual-provider bases (WM-OBJ-001, WM-OBJ-002, WM-ECO-019) out of fourteen. The arithmetic is 14 − 3 = **11** single-provider. Record eleven; the "ten" figure is an undercount of the Codex subset only.

```
/baseProvenance = {
  "dualProvider": ["WM-OBJ-001","WM-OBJ-002","WM-ECO-019"],
  "singleProviderCodexWaiver": ["WM-OBJ-017","WM-OBJ-018","WM-OBJ-019","WM-OBJ-020","WM-FLW-004","WM-FLW-011","WM-FLW-012","WM-FLW-013","WM-ACT-007","WM-ECO-024"],
  "singleProviderClaudeWaiver": ["WM-ECO-020"],
  "counts": {"total":14,"dualProvider":3,"singleProvider":11,"singleProviderCodex":10,"singleProviderClaude":1},
  "allBasesPublishableCanonical": false
}
```
Assertion: `dualProvider + singleProviderCodexWaiver + singleProviderClaudeWaiver` is a partition of `/bases` with no duplicates and length 14.

### D18 — Privacy/access policy entirely absent from all artifacts
```
/access = {
  "default": "deny",
  "purposeBindingRequired": true,
  "minimumProjection": true,
  "withheldRepresentation": "explicit-withheld-marker-never-absent",
  "suppressedDistinctFromWithheld": true,
  "retentionLegalHoldTombstoningExecutedIn": "adopting-dimension-records-model"
}
```

### D19 — References: fixtures unanchored; manifest file list incomplete
`fixtures.json` identifies its profile by display name only; `checkpoint-manifest.json:/files` omits `grok-study.raw.md` and all three `candidate-profile-offline/` files. Digests must be computed by the script, never invented.

```
fixtures.json:/format = "vercy-enterprise-profile-fixtures/v2"
fixtures.json:/contourId = "EM-LND-11"
fixtures.json:/profileRef = "candidate-profile-offline/profile-candidate.json"
fixtures.json:/invariantRegistryRef = "candidate-profile-offline/profile-candidate.json#/invariants"
fixtures.json:/defectRegisterRef = "frozen-audit-EM-LND-11.md#defects"
fixtures.json:/baseRefsMustResolveIn = "candidate-profile-offline/profile-candidate.json#/bases"

checkpoint-manifest.json:/files += {"path":"grok-study.raw.md","bytes":null,"sha256":null,"digestStatus":"to-be-computed-by-local-script"}
checkpoint-manifest.json:/files += {"path":"candidate-profile-offline/profile-candidate.json","bytes":null,"sha256":null,"digestStatus":"to-be-computed-by-local-script"}
checkpoint-manifest.json:/files += {"path":"candidate-profile-offline/fixtures.json","bytes":null,"sha256":null,"digestStatus":"to-be-computed-by-local-script"}
checkpoint-manifest.json:/files += {"path":"candidate-profile-offline/README.md","bytes":null,"sha256":null,"digestStatus":"to-be-computed-by-local-script"}
checkpoint-manifest.json:/files += {"path":"frozen-audit-EM-LND-11.md","bytes":null,"sha256":null,"digestStatus":"to-be-computed-by-local-script"}
checkpoint-manifest.json:/digestPolicy = {"algorithm":"sha256","fabricationForbidden":true,"nullMeansToBeComputed":true}
```

### D20 — Relation holds: registry conflicts recorded as vague prose
`/holds/1` says conflicts "require reconciliation" without naming entries, so a consumer cannot tell which signal is unsafe. Record both sides, unresolved, with no selection.

```
/registryConflicts = [
  {"entry":"WM-OBJ-019","signalA":"registry parent_ids = WM-OBJ-002","signalB":"relation row WM-OBJ-019 COMPOSE WM-OBJ-002","status":"unresolved","selected":null},
  {"entry":"WM-FLW-011","signal":"registry parent signal candidate-only and contradicts specification","status":"unresolved","selected":null},
  {"entry":"WM-FLW-012","signal":"registry parent signal candidate-only and contradicts specification","status":"unresolved","selected":null},
  {"entry":"WM-FLW-013","signal":"registry parent signal candidate-only and contradicts specification","status":"unresolved","selected":null},
  {"entry":"WM-ECO-024","signal":"registry parent signal candidate-only and contradicts specification","status":"unresolved","selected":null},
  {"entry":"WM-OBJ-020","signal":"registry parent signal candidate-only and contradicts specification","status":"unresolved","selected":null},
  {"scope":"most entries","signalA":"registry entry_kind = standalone-mm","signalB":"specification entry kinds = aggregate | event | pattern","status":"unresolved","selected":null}
]
/registryConflicts/_rules = {"conflictingSignalUsableAsAuthority": false, "silentSelectionForbidden": true}
/holds/1 = "Registry parent signals for WM-OBJ-019, WM-OBJ-020, WM-FLW-011, WM-FLW-012, WM-FLW-013 and WM-ECO-024 and the entry_kind signal conflict with their specifications; see /registryConflicts. None is resolved or selected here."
```

### D21 — Publication holds: no `publishableCanonical` flag; pin divergence unrecorded; WM-ACT-007 hold missing; two holds stale
`/holds/2` still says Grok review is pending, and `local-evidence.md`/`CONTINUATION.md` still say fixtures are absent while `fixtures.json` exists with seven cases. Neither correction asserts readiness.

```
/publishableCanonical = false
/installabilityClaimed = false
/publicationReadinessClaimed = false
/fixtureExecution = "not-executed"
/externalPinDivergence = [
  {"standard":"EPCIS","pins":["2.0","2.0.1"],"note":"URL/PDF label mismatch","status":"unresolved","selected":null},
  {"standard":"CBV","pins":["2.0","2.0.0"],"status":"unresolved","selected":null},
  {"standard":"UBL","pins":["2.3","2.4"],"status":"unresolved","selected":null}
]
/publicationHolds = [
  "Nine subject/event masters identifier-unassigned (see /unmasteredFacts).",
  "Registry parent-signal and entry_kind conflicts unresolved (see /registryConflicts).",
  "WM-ACT-007 is maintenance-scoped with an unresolved legacy K11 duplication; no production/transformation work order or routing/manufacturing plan master exists.",
  "EPCIS, CBV and UBL pins divergent and unselected (see /externalPinDivergence).",
  "Crosswalks absent.",
  "Fixtures specified but not executed; fixtureExecution = not-executed.",
  "All fourteen bases non-canonical; eleven single-provider (see /baseProvenance)."
]
/holds/2 = "Independent Grok review received and reconciled (grok-study.raw.md); frozen semantic audit complete. Crosswalks remain absent and fixtures remain unexecuted; no canonicity, installability or publication-readiness is claimed."
/workOrderScope = {"WM-ACT-007":{"scope":"maintenance-and-repair","usableAsProductionTransformationWorkOrder":false,"legacyDuplication":"K11-unresolved"}}

CONTINUATION.md: replace "One Claude Opus high no-tools study, local synthesis and exact unsent Grok prompt are preserved."
  with "One Claude Opus high no-tools study, one Grok study response, local synthesis, the Grok prompt and the frozen semantic audit are preserved."
CONTINUATION.md: replace "and absent crosswalks and fixtures."
  with "absent crosswalks; and fixtures that are specified but not executed."
```

### D22 — Fixture schema: no `target`, `violates`, `closesDefect`, `expectedCode`, no canonical IDs
Apply to all seven existing cases (slug IDs retained for referential stability; canonical IDs added):

```
/cases/0 += {"canonicalId":"EM-LND-11-FX-001","target":"recall-classifier","violates":[],"closesDefect":["D13"]}
/cases/1 += {"canonicalId":"EM-LND-11-FX-002","target":"recall-classifier","violates":[],"closesDefect":["D13"]}
/cases/2 += {"canonicalId":"EM-LND-11-FX-003","target":"trace-result","violates":[],"closesDefect":["D12"]}
/cases/3 += {"canonicalId":"EM-LND-11-FX-004","target":"recall-classifier","violates":["INV-03","INV-15"],"closesDefect":["D5","D13"],"expectedCode":"EMLND11_E_BOM_NOT_COMPOSITION"}
/cases/4 += {"canonicalId":"EM-LND-11-FX-005","target":"fulfilment-case","violates":["INV-02"],"closesDefect":["D10","D23"],"expectedCode":"EMLND11_E_SCAN_NOT_ACCEPTANCE"}
/cases/5 += {"canonicalId":"EM-LND-11-FX-006","target":"stock-ledger","violates":["INV-12"],"closesDefect":["D7"],"expectedCode":"EMLND11_E_MISSING_ROW_NOT_ZERO"}
/cases/6 += {"canonicalId":"EM-LND-11-FX-007","target":"landscape-declaration","violates":["INV-18"],"closesDefect":["D16"],"expectedCode":"EMLND11_E_VIEW_EXERCISES_AUTHORITY"}
/schemaVersion = 2
/requiredCaseFields = ["id","canonicalId","target","kind","input","expect","violates","closesDefect"]
/requiredNegativeCaseFields = ["expectedCode"]
```

### D23 — Fixture conflation: `scan-proves-acceptance` bundles two distinct inferences
Its input asserts both delivery acceptance **and** title transfer, so a single failure cannot localise which rule fired. Narrow it to acceptance; title is covered by `EM-LND-11-FX-048`.

```
/cases/4/input = "A location scan is treated as delivery acceptance."
/cases/4/expect = "The inference is rejected; acceptance requires a separate acceptance assertion on its own axis."
```

### D24 — No invariant registry, so `violates` cannot resolve
Add the reconciled, de-duplicated merge of the Claude (10), local (10) and Grok (14) sets — Grok's quantity bound and origin-break rule included:

```
/invariants = [
 {"id":"INV-01","text":"Every genealogy edge cites an actual event and carries verified evidence."},
 {"id":"INV-02","text":"Plan is not movement; movement is not posting; posting is not acceptance."},
 {"id":"INV-03","text":"BOM, design, variant and plan never establish actual lot or serial composition."},
 {"id":"INV-04","text":"Unknown origin and incomplete trace are explicit first-class states."},
 {"id":"INV-05","text":"Absence implies non-exposure only inside a closed, versioned completeness perimeter."},
 {"id":"INV-06","text":"Custody is not title; location is not custody; a scan or status code is not clearance."},
 {"id":"INV-07","text":"Every quantity carries item scope, unit, pinned code-list version, precision and measurement basis; unknown, zero, not-applicable, withheld and suppressed never collapse."},
 {"id":"INV-08","text":"Declared, observed and inferred edges stay distinct; an inferred edge never becomes an asserted fact."},
 {"id":"INV-09","text":"Views declare viewpoint, scope, as-of, freshness, completeness perimeter, disclosure policy and digest, and reproject byte-identically."},
 {"id":"INV-10","text":"Corrections append linked successors; identifiers are never reused and retired identifiers stay resolvable."},
 {"id":"INV-11","text":"Serialized identity, lot identity and bulk quantity are distinct; lot membership is provenance; packing is not proof of contents."},
 {"id":"INV-12","text":"Stock position is not a movement and not a genealogy node; a missing row is not zero; a count is not posting authority."},
 {"id":"INV-13","text":"Neither Operations Landscape nor Supply Network nor a projection is a root or master; no subject identity is minted, no identifier is allocated, no gap is promoted."},
 {"id":"INV-14","text":"No landscape or network edge may close an unknown-origin break."},
 {"id":"INV-15","text":"Recall returns only proven-affected, potentially-affected or not-evidenced; not-evidenced is not cleared; proven is bounded by the cited consumed quantity; potentially-affected carries a reason code."},
 {"id":"INV-16","text":"The eight time axes stay distinct; instants are RFC 3339 with seconds and explicit offset; a declaration's effective time never backdates an execution event."},
 {"id":"INV-17","text":"Access is deny-by-default and purpose-bound; withheld segments are marked withheld, never absent."},
 {"id":"INV-18","text":"One owning model per fact; unknown mastership blocks mutation; an alignment is never a master; views exercise no allocation, dispatch, posting, acceptance, recall or enforcement authority."},
 {"id":"INV-19","text":"Shipment is not consignment; the semantic-kind discriminator is mandatory; allocation is many-to-many."},
 {"id":"INV-20","text":"Design and plan intent never substitute for executed quantity, location or party; authorization never proves execution."},
 {"id":"INV-21","text":"No canonicity, installability or publication-readiness claim while holds stand; conflicting registry signals and divergent external pins are recorded unresolved and never silently selected."},
 {"id":"INV-22","text":"Provenance records only provider studies that completed and returned usable output; unknown provenance is explicit and never fabricated."}
]
```

### D25 — README underspecified
Replace the body after the title with:

```
Defines Operations Landscape as a governed declaration plus a reproducible, exception-aware projection, and Supply Network as a scoped graph view hosted inside that declaration, over existing masters and nine explicitly unassigned gaps.

- Decision: PROFILE. No catalogue or runtime identifier is allocated. Neither candidate is a root.
- Bases: 14 reused drafts (3 dual-provider, 11 single-provider). publishableCanonical: false.
- Identifier-unassigned gaps (not promoted): Lot/Batch; Handling Unit; As-Built Assembly; Party/Supplier; Facility/Location; Supply Relationship; Transformation Plan; Actual Consumption/Production Event; Occurrence/Event.
- Holds: see profile-candidate.json#/publicationHolds. Fixtures are specified, not executed.
- No canonicity, installability or publication readiness is claimed.
```

### D26 — Manifest records one study and a stale Grok status
`/providerStudy` is a single object and `/grokPromptStatus` is `"prepared-unsent-action-time-confirmation-required"`, both contradicted by the frozen `grok-study.raw.md`. Do not invent Grok's model, effort or tool settings.

```
delete /providerStudy
/providerStudies = [
  {"provider":"Claude","model":"opus","effort":"high","tools":false,"responseFile":"claude-study.raw.md","status":"completed"},
  {"provider":"Grok","model":"unknown-not-recorded","effort":"unknown-not-recorded","tools":"unknown-not-recorded","responseFile":"grok-study.raw.md","status":"completed","note":"visible response only; hidden reasoning and UI source controls excluded from evidence"}
]
/grokPromptStatus = "sent-response-received-reconciled"
/frozenAudit = {"status":"completed","scope":"single-final-semantic-audit","rerunRequired":false,"recordFile":"frozen-audit-EM-LND-11.md"}
/unassignedCandidates/_rules = {"count":9,"identifierAllocated":false,"promoted":false}
/disposition = "Operations Landscape declaration/projection; Supply Network graph view; no catalogue identifier and no runtime identifier allocated"
```

### D27 — `local-evidence.md` holds stale on fixtures
```
local-evidence.md: replace "crosswalks and fixtures are absent"
  with "crosswalks are absent and fixtures are specified but not executed"
```

### D28 — Alignment-as-master risk unstated in the profile
Covered structurally by `/genealogyEdge/alignmentAsEdgeSource` (D11); additionally:
```
/externalAlignments = {"EPCIS-TransformationEvent":{"role":"alignment-only","mayServeAsGenealogyMaster":false,"appearsOn":["WM-OBJ-001","WM-FLW-012","WM-FLW-013"]}}
```

### D29 — Nothing in any artifact mechanically forbids allocation or gap promotion
`newRuntimeId:false` covers one allocation class only.
```
/identifierAllocation = {
  "catalogue": "none",
  "runtime": "none",
  "newRuntimeId": false,
  "newCatalogueId": false,
  "gapPromotionAllowed": false,
  "reuseConfersIdentifier": false,
  "allocatedInThisContour": []
}
```

### D30 — Correction lineage, identifier non-reuse and retired resolvability under-specified
`/constraints/7` says "corrections append lineage" but omits immutability of issued revisions, non-reuse and continued resolvability.
```
/corrections = {
  "mechanism": "append-linked-successor",
  "issuedRevisionMutable": false,
  "inPlaceOverwriteAllowed": false,
  "identifierReuseAllowed": false,
  "retiredIdentifierResolvable": true
}
/constraints/7 = "Landscape and network views never allocate, dispatch, post, accept, recall or enforce; corrections append linked successors, issued revisions are immutable, identifiers are never reused, and retired identifiers stay resolvable."
```

---

## 3. Additional fixtures

```json
[
{"id":"EM-LND-11-FX-008","target":"landscape-declaration","kind":"positive","input":"Declaration carries identityClass=declaration-artifact, subjectIdentityMinted=false, rootPromotionAllowed=false.","expect":"Accepted as a governed declaration with artifact identity only.","violates":[],"closesDefect":["D1"]},
{"id":"EM-LND-11-FX-009","target":"landscape-declaration","kind":"negative","input":"The declaration asserts itself as the aggregate root for operations facts.","expect":"Rejected; a declaration cannot become a subject root.","violates":["INV-13"],"closesDefect":["D1"],"expectedCode":"EMLND11_E_ROOT_PROMOTION_FORBIDDEN"},
{"id":"EM-LND-11-FX-010","target":"supply-network-view","kind":"negative","input":"Supply Network is registered as a persistent root master.","expect":"Rejected; Supply Network is a view definition only.","violates":["INV-13"],"closesDefect":["D1"],"expectedCode":"EMLND11_E_VIEW_AS_ROOT"},
{"id":"EM-LND-11-FX-011","target":"supply-network-view","kind":"negative","input":"A network node is treated as the authoritative record of supplier party identity.","expect":"Rejected; party mastership is unassigned and outside this package.","violates":["INV-13","INV-18"],"closesDefect":["D1","D2"],"expectedCode":"EMLND11_E_DUPLICATE_MASTERSHIP"},
{"id":"EM-LND-11-FX-012","target":"projection-engine","kind":"negative","input":"A projection output is cited by another contour as a master source of record.","expect":"Rejected; a projection is a derived output and never a master.","violates":["INV-13","INV-18"],"closesDefect":["D1"],"expectedCode":"EMLND11_E_PROJECTION_AS_ROOT"},
{"id":"EM-LND-11-FX-013","target":"mastership-map","kind":"positive","input":"All fourteen fact classes resolve to exactly one base each.","expect":"Accepted; one owning model per fact.","violates":[],"closesDefect":["D2"]},
{"id":"EM-LND-11-FX-014","target":"mastership-map","kind":"negative","input":"WM-OBJ-020 and WM-FLW-012 both claim mastership of stock quantity.","expect":"Rejected; stock quantity has exactly one owner.","violates":["INV-18"],"closesDefect":["D2"],"expectedCode":"EMLND11_E_MULTIPLE_OWNERS"},
{"id":"EM-LND-11-FX-015","target":"mastership-map","kind":"negative","input":"A Lot/Batch fact is mutated although its master is unassigned.","expect":"Rejected; unknown mastership blocks mutation.","violates":["INV-18"],"closesDefect":["D2"],"expectedCode":"EMLND11_E_UNKNOWN_MASTERSHIP_BLOCKS_MUTATION"},
{"id":"EM-LND-11-FX-016","target":"gap-register","kind":"negative","input":"The gap list collapses Actual Consumption/Production Event and Occurrence/Event into one entry, yielding eight names.","expect":"Rejected; exactly nine distinct gaps must be enumerated and must match the manifest list.","violates":["INV-13"],"closesDefect":["D2"],"expectedCode":"EMLND11_E_GAP_ENUMERATION_INCOMPLETE"},
{"id":"EM-LND-11-FX-017","target":"projection-engine","kind":"positive","input":"Identical declaration, pins, asOf and ruleSetVersion are reprojected twice.","expect":"Byte-identical output and identical sha256 projection digest.","violates":[],"closesDefect":["D3"]},
{"id":"EM-LND-11-FX-018","target":"projection-engine","kind":"negative","input":"A projection is emitted while one source revision pin is unpinned.","expect":"Rejected; emission is blocked until all pins resolve.","violates":["INV-09"],"closesDefect":["D3"],"expectedCode":"EMLND11_E_UNPINNED_SOURCE_REVISION"},
{"id":"EM-LND-11-FX-019","target":"projection-engine","kind":"negative","input":"A projection is emitted with no asOf instant.","expect":"Rejected; every view answers as-of a stated instant.","violates":["INV-09"],"closesDefect":["D3"],"expectedCode":"EMLND11_E_MISSING_AS_OF"},
{"id":"EM-LND-11-FX-020","target":"projection-engine","kind":"negative","input":"A projection declares a digest field but never computes it.","expect":"Rejected; the digest must be computed over the emitted bytes.","violates":["INV-09"],"closesDefect":["D3"],"expectedCode":"EMLND11_E_MISSING_PROJECTION_DIGEST"},
{"id":"EM-LND-11-FX-021","target":"projection-engine","kind":"negative","input":"Reprojection normalises and writes back a source revision.","expect":"Rejected; views never mutate sources.","violates":["INV-09","INV-18"],"closesDefect":["D3"],"expectedCode":"EMLND11_E_VIEW_MUTATES_SOURCE"},
{"id":"EM-LND-11-FX-022","target":"landscape-declaration","kind":"positive","input":"View declares viewpoint, concerns, scope, asOf, freshness, completeness perimeter, disclosure policy, digest, gap and conflict registers.","expect":"Accepted; all ten declaration fields present.","violates":[],"closesDefect":["D3"]},
{"id":"EM-LND-11-FX-023","target":"landscape-declaration","kind":"negative","input":"A view omits its completeness perimeter.","expect":"Rejected; the perimeter is mandatory before any absence reasoning.","violates":["INV-05","INV-09"],"closesDefect":["D3"],"expectedCode":"EMLND11_E_MISSING_COMPLETENESS_PERIMETER"},
{"id":"EM-LND-11-FX-024","target":"supply-network-view","kind":"positive","input":"An edge derived from a supply-relation master carries validity interval, determination method, evidence reference and confidence.","expect":"Accepted as a scoped network edge.","violates":[],"closesDefect":["D4"]},
{"id":"EM-LND-11-FX-025","target":"supply-network-view","kind":"negative","input":"An edge is created from shared facility co-location with no supply-relation master and no movement event.","expect":"Rejected; the network may not invent edges.","violates":["INV-13"],"closesDefect":["D4"],"expectedCode":"EMLND11_E_UNSOURCED_NETWORK_EDGE"},
{"id":"EM-LND-11-FX-026","target":"supply-network-view","kind":"negative","input":"A missing edge is reported as proof that no supply relationship exists, with no closed perimeter.","expect":"Rejected; a missing edge means unobserved.","violates":["INV-05"],"closesDefect":["D4"],"expectedCode":"EMLND11_E_ABSENCE_NOT_NON_EXPOSURE"},
{"id":"EM-LND-11-FX-027","target":"supply-network-view","kind":"positive","input":"A closed, versioned completeness perimeter licenses a scoped absence claim inside its bounds.","expect":"Accepted; the absence claim is scoped to the declared perimeter version.","violates":[],"closesDefect":["D4"]},
{"id":"EM-LND-11-FX-028","target":"genealogy-edge-validator","kind":"negative","input":"A network path from supplier to plant is used as a genealogy edge for a lot.","expect":"Rejected; a network snapshot is not genealogy.","violates":["INV-01","INV-14"],"closesDefect":["D4"],"expectedCode":"EMLND11_E_NETWORK_PATH_NOT_GENEALOGY"},
{"id":"EM-LND-11-FX-029","target":"trace-result","kind":"negative","input":"A network edge is used to substitute a probable supplier and close the unknown-origin break.","expect":"Rejected; the break stays exposed with its unknown-origin marker.","violates":["INV-04","INV-14"],"closesDefect":["D4","D12"],"expectedCode":"EMLND11_E_UNKNOWN_ORIGIN_BRIDGED"},
{"id":"EM-LND-11-FX-030","target":"genealogy-edge-validator","kind":"negative","input":"An engineering BOM occurrence is treated as a serialized item.","expect":"Rejected; occurrence is design intent, not instance identity.","violates":["INV-03","INV-11"],"closesDefect":["D5"],"expectedCode":"EMLND11_E_OCCURRENCE_NOT_SERIAL"},
{"id":"EM-LND-11-FX-031","target":"genealogy-edge-validator","kind":"negative","input":"A candidate alternate BOM line is reported as the installed component.","expect":"Rejected; alternates do not imply installation.","violates":["INV-03"],"closesDefect":["D5"],"expectedCode":"EMLND11_E_ALTERNATE_NOT_INSTALLED"},
{"id":"EM-LND-11-FX-032","target":"quantity-validator","kind":"negative","input":"A nominal BOM aggregate is published as a measured property.","expect":"Rejected; nominal is not measured.","violates":["INV-03","INV-07"],"closesDefect":["D5"],"expectedCode":"EMLND11_E_NOMINAL_NOT_MEASURED"},
{"id":"EM-LND-11-FX-033","target":"genealogy-edge-validator","kind":"negative","input":"Transformation-plan quantity, location and supplier are recorded as the executed quantity, location and party.","expect":"Rejected; plan never substitutes for execution.","violates":["INV-20"],"closesDefect":["D5"],"expectedCode":"EMLND11_E_PLAN_NOT_EXECUTION"},
{"id":"EM-LND-11-FX-034","target":"recall-classifier","kind":"positive","input":"A BOM is used only to bound candidate composition and the result is tagged design-intent.","expect":"Accepted as a candidate bound, not as composition evidence.","violates":[],"closesDefect":["D5"]},
{"id":"EM-LND-11-FX-035","target":"genealogy-edge-validator","kind":"negative","input":"Lot membership is used as the instance identity of the consumed material.","expect":"Rejected; lot membership is provenance only.","violates":["INV-11"],"closesDefect":["D6"],"expectedCode":"EMLND11_E_LOT_NOT_INSTANCE_IDENTITY"},
{"id":"EM-LND-11-FX-036","target":"mastership-map","kind":"negative","input":"Fungible bulk material is given serialized item identity under WM-OBJ-001.","expect":"Rejected; no individuating boundary, and the sibling lot/bulk model is unassigned.","violates":["INV-11","INV-13"],"closesDefect":["D6"],"expectedCode":"EMLND11_E_NO_INDIVIDUATING_BOUNDARY"},
{"id":"EM-LND-11-FX-037","target":"genealogy-edge-validator","kind":"negative","input":"A handling-unit packing list is used as proof of the unit's actual contents.","expect":"Rejected; CONTAINS is typed membership, not contents proof.","violates":["INV-11"],"closesDefect":["D6"],"expectedCode":"EMLND11_E_PACKING_NOT_CONTENTS_PROOF"},
{"id":"EM-LND-11-FX-038","target":"mastership-map","kind":"positive","input":"A serialized unit, its lot membership as provenance, and a bulk quantity are held as three distinct records.","expect":"Accepted; the three identity classes remain separate.","violates":[],"closesDefect":["D6"]},
{"id":"EM-LND-11-FX-039","target":"stock-ledger","kind":"negative","input":"A physical count result is used as authority to post an inventory adjustment.","expect":"Rejected; a count is not posting authority.","violates":["INV-12"],"closesDefect":["D7"],"expectedCode":"EMLND11_E_COUNT_NOT_POSTING_AUTHORITY"},
{"id":"EM-LND-11-FX-040","target":"movement-event","kind":"negative","input":"A planned movement line is reported as a movement that occurred.","expect":"Rejected; plan is not movement.","violates":["INV-02"],"closesDefect":["D7"],"expectedCode":"EMLND11_E_PLAN_NOT_MOVEMENT"},
{"id":"EM-LND-11-FX-041","target":"movement-event","kind":"negative","input":"A recorded movement is treated as the authoritative inventory posting.","expect":"Rejected; movement is not posting.","violates":["INV-02","INV-12"],"closesDefect":["D7"],"expectedCode":"EMLND11_E_MOVEMENT_NOT_POSTING"},
{"id":"EM-LND-11-FX-042","target":"movement-event","kind":"positive","input":"One stock-affecting transition is recorded with the authoritative posting held as an external reference.","expect":"Accepted; movement and posting stay distinct.","violates":[],"closesDefect":["D7"]},
{"id":"EM-LND-11-FX-043","target":"genealogy-edge-validator","kind":"negative","input":"A stock position row is used as a genealogy node linking input lot to output lot.","expect":"Rejected; stock is not a genealogy node.","violates":["INV-12"],"closesDefect":["D7"],"expectedCode":"EMLND11_E_STOCK_NOT_GENEALOGY_NODE"},
{"id":"EM-LND-11-FX-044","target":"shipment-record","kind":"negative","input":"A shipment is recorded with no trade-shipment / transport-consignment / combined-view discriminator.","expect":"Rejected; the semantic kind is mandatory.","violates":["INV-19"],"closesDefect":["D8"],"expectedCode":"EMLND11_E_MISSING_SHIPMENT_KIND"},
{"id":"EM-LND-11-FX-045","target":"shipment-record","kind":"negative","input":"Shipment and consignment are forced into a one-to-one link.","expect":"Rejected; allocation is many-to-many.","violates":["INV-19"],"closesDefect":["D8"],"expectedCode":"EMLND11_E_SHIPMENT_CONSIGNMENT_CARDINALITY"},
{"id":"EM-LND-11-FX-046","target":"shipment-record","kind":"positive","input":"One transport consignment is allocated across two trade shipments, each with its discriminator set.","expect":"Accepted; many-to-many allocation preserved.","violates":[],"closesDefect":["D8"]},
{"id":"EM-LND-11-FX-047","target":"custody-ledger","kind":"negative","input":"A location read point is recorded as a custody transfer.","expect":"Rejected; location is not custody.","violates":["INV-06"],"closesDefect":["D9","D23"],"expectedCode":"EMLND11_E_LOCATION_NOT_CUSTODY"},
{"id":"EM-LND-11-FX-048","target":"custody-ledger","kind":"negative","input":"A custody transfer is recorded as a transfer of title.","expect":"Rejected; custody is not title.","violates":["INV-06"],"closesDefect":["D9","D23"],"expectedCode":"EMLND11_E_CUSTODY_NOT_TITLE"},
{"id":"EM-LND-11-FX-049","target":"custody-ledger","kind":"negative","input":"A carrier status code is interpreted as customs clearance.","expect":"Rejected; a status code is not clearance.","violates":["INV-06"],"closesDefect":["D9"],"expectedCode":"EMLND11_E_SCAN_NOT_CLEARANCE"},
{"id":"EM-LND-11-FX-050","target":"custody-ledger","kind":"positive","input":"Custody passes to a 3PL while title remains with the consignor.","expect":"Accepted; custody and title recorded independently.","violates":[],"closesDefect":["D9"]},
{"id":"EM-LND-11-FX-051","target":"fulfilment-case","kind":"negative","input":"Goods receipt is recorded as acceptance.","expect":"Rejected; receipt and acceptance are separate axes.","violates":["INV-02"],"closesDefect":["D10"],"expectedCode":"EMLND11_E_RECEIPT_NOT_ACCEPTANCE"},
{"id":"EM-LND-11-FX-052","target":"fulfilment-case","kind":"negative","input":"Dispatch is recorded as fulfilment completion.","expect":"Rejected; dispatch and completion are separate axes.","violates":["INV-02"],"closesDefect":["D10"],"expectedCode":"EMLND11_E_DISPATCH_NOT_COMPLETION"},
{"id":"EM-LND-11-FX-053","target":"fulfilment-case","kind":"positive","input":"Dispatch, handover and receipt are recorded while inspection is pending and acceptance is unset.","expect":"Accepted; six axes remain independent.","violates":[],"closesDefect":["D10"]},
{"id":"EM-LND-11-FX-054","target":"work-order","kind":"negative","input":"An issued WM-ACT-007 work order is treated as proof the work was performed.","expect":"Rejected; authorization never proves execution.","violates":["INV-20"],"closesDefect":["D10","D21"],"expectedCode":"EMLND11_E_AUTHORIZATION_NOT_EXECUTION"},
{"id":"EM-LND-11-FX-055","target":"genealogy-edge-validator","kind":"positive","input":"A transformation edge carries all fourteen required fields including relation type, cited event, quantity with unit, event and record times, read point, business location, yield, source, agent, method, confidence and evidence digest.","expect":"Accepted as an evidence-bearing genealogy edge.","violates":[],"closesDefect":["D11"]},
{"id":"EM-LND-11-FX-056","target":"genealogy-edge-validator","kind":"negative","input":"A consumption edge is stored with no cited actual event.","expect":"Rejected; no genealogy edge without an actual event citation.","violates":["INV-01"],"closesDefect":["D11"],"expectedCode":"EMLND11_E_EDGE_WITHOUT_EVENT"},
{"id":"EM-LND-11-FX-057","target":"genealogy-edge-validator","kind":"negative","input":"An edge cites an event but carries no evidence digest.","expect":"Rejected; evidence digest is mandatory.","violates":["INV-01"],"closesDefect":["D11"],"expectedCode":"EMLND11_E_MISSING_EVIDENCE_DIGEST"},
{"id":"EM-LND-11-FX-058","target":"genealogy-edge-validator","kind":"negative","input":"An inferred edge is persisted with edgeMode=declared and later reported as an asserted fact.","expect":"Rejected; inferred edges never become asserted.","violates":["INV-08"],"closesDefect":["D11"],"expectedCode":"EMLND11_E_INFERRED_AS_ASSERTED"},
{"id":"EM-LND-11-FX-059","target":"genealogy-edge-validator","kind":"negative","input":"The EPCIS TransformationEvent alignment on WM-FLW-013 is cited as the genealogy master.","expect":"Rejected; an alignment is not a master.","violates":["INV-18"],"closesDefect":["D11","D28"],"expectedCode":"EMLND11_E_ALIGNMENT_NOT_MASTER"},
{"id":"EM-LND-11-FX-060","target":"genealogy-edge-validator","kind":"negative","input":"A mass-balance custody claim is asserted as one-to-one instance continuity.","expect":"Rejected; mass balance and controlled blending break one-to-one continuity.","violates":["INV-06","INV-08"],"closesDefect":["D11"],"expectedCode":"EMLND11_E_MASS_BALANCE_NOT_CONTINUITY"},
{"id":"EM-LND-11-FX-061","target":"trace-result","kind":"positive","input":"A backward trace reaches an unresolvable supplier and returns traceCompleteness=incomplete with an explicit unknown-origin marker and residual uncertainty.","expect":"Accepted; the break is exposed and not bridged.","violates":[],"closesDefect":["D12"]},
{"id":"EM-LND-11-FX-062","target":"trace-result","kind":"negative","input":"Unknown origin is represented as a null or empty supplier field.","expect":"Rejected; unknown origin is an explicit first-class state.","violates":["INV-04"],"closesDefect":["D12"],"expectedCode":"EMLND11_E_UNKNOWN_ORIGIN_NOT_EXPLICIT"},
{"id":"EM-LND-11-FX-063","target":"trace-result","kind":"negative","input":"A result carrying an unknown-origin marker is returned as complete.","expect":"Rejected; completeness requires a closed perimeter and zero unknown-origin markers.","violates":["INV-04","INV-05"],"closesDefect":["D12"],"expectedCode":"EMLND11_E_INCOMPLETE_REPORTED_COMPLETE"},
{"id":"EM-LND-11-FX-064","target":"trace-result","kind":"positive","input":"Per-item classification and per-result traceCompleteness are emitted as two separate fields.","expect":"Accepted; item classification and result completeness do not share an axis.","violates":[],"closesDefect":["D12"]},
{"id":"EM-LND-11-FX-065","target":"recall-classifier","kind":"negative","input":"Forty BOM-only units are reported as unaffected and cleared.","expect":"Rejected; not-evidenced is not cleared without a closed completeness perimeter.","violates":["INV-05","INV-15"],"closesDefect":["D13"],"expectedCode":"EMLND11_E_NOT_EVIDENCED_NOT_CLEARED"},
{"id":"EM-LND-11-FX-066","target":"recall-classifier","kind":"negative","input":"An output is classified potentially-affected with no reason code.","expect":"Rejected; a reason code from the enum is mandatory.","violates":["INV-15"],"closesDefect":["D13"],"expectedCode":"EMLND11_E_MISSING_POTENTIAL_REASON"},
{"id":"EM-LND-11-FX-067","target":"recall-classifier","kind":"negative","input":"An output is classified as 'suspected'.","expect":"Rejected; only proven-affected, potentially-affected and not-evidenced are permitted.","violates":["INV-15"],"closesDefect":["D13"],"expectedCode":"EMLND11_E_INVALID_RECALL_CLASS"},
{"id":"EM-LND-11-FX-068","target":"recall-classifier","kind":"negative","input":"An event cites consumption of 20 kg of the recalled lot and the entire 500 kg output batch is declared proven affected.","expect":"Rejected; proven affected is bounded by the cited consumed quantity, the remainder is potentially affected with a reason code.","violates":["INV-15"],"closesDefect":["D13"],"expectedCode":"EMLND11_E_PROVEN_QUANTITY_UNBOUNDED"},
{"id":"EM-LND-11-FX-069","target":"recall-classifier","kind":"positive","input":"Recalled lot L: three serialized units with cited consumption events; two bulk lots from a blended silo; forty units with BOM only; L's inbound supplier unresolvable.","expect":"Exactly 3 proven-affected bounded by cited quantities, 2 potentially-affected with reasonCode MASS_BALANCE, 40 not-evidenced and not cleared, traceCompleteness=incomplete with an unknown-origin marker.","violates":[],"closesDefect":["D12","D13"]},
{"id":"EM-LND-11-FX-070","target":"recall-classifier","kind":"negative","input":"Sibling lots from the unresolved supplier are declared unaffected.","expect":"Rejected; they are not-evidenced and the question is unanswerable inside this perimeter.","violates":["INV-04","INV-15"],"closesDefect":["D13"],"expectedCode":"EMLND11_E_SIBLING_LOT_UNRESOLVED"},
{"id":"EM-LND-11-FX-071","target":"time-validator","kind":"negative","input":"Event time and record time are written to one shared timestamp field.","expect":"Rejected; the eight time axes stay distinct.","violates":["INV-16"],"closesDefect":["D14"],"expectedCode":"EMLND11_E_TIME_AXIS_COLLAPSE"},
{"id":"EM-LND-11-FX-072","target":"time-validator","kind":"negative","input":"An event instant is recorded as 2026-09-26T14:00:00 with no offset.","expect":"Rejected; instants are RFC 3339 with seconds and an explicit offset.","violates":["INV-16"],"closesDefect":["D14"],"expectedCode":"EMLND11_E_TIME_OFFSET_MISSING"},
{"id":"EM-LND-11-FX-073","target":"time-validator","kind":"negative","input":"A declaration's effective time is applied as the event time of an execution event.","expect":"Rejected; a declaration never backdates an execution event.","violates":["INV-16"],"closesDefect":["D14"],"expectedCode":"EMLND11_E_DECLARATION_BACKDATES_EXECUTION"},
{"id":"EM-LND-11-FX-074","target":"checkpoint-manifest.json","kind":"positive","input":"checkpointDate is typed {value, precision=day, timeAxis=record, offsetKnown=false} and no time of day is synthesised.","expect":"Accepted; day precision is preserved without inventing an instant.","violates":[],"closesDefect":["D14"]},
{"id":"EM-LND-11-FX-075","target":"quantity-validator","kind":"negative","input":"An evidence edge carries quantity 12 with no unit.","expect":"Rejected; quantity without unit is invalid on evidence edges.","violates":["INV-07"],"closesDefect":["D15"],"expectedCode":"EMLND11_E_QUANTITY_WITHOUT_UNIT"},
{"id":"EM-LND-11-FX-076","target":"quantity-validator","kind":"negative","input":"A unit is given from a code list with no pinned code-list version.","expect":"Rejected; the code-list version must be pinned.","violates":["INV-07"],"closesDefect":["D15"],"expectedCode":"EMLND11_E_UNIT_CODELIST_VERSION_MISSING"},
{"id":"EM-LND-11-FX-077","target":"quantity-validator","kind":"negative","input":"A withheld quantity is rendered as 0 in a projection.","expect":"Rejected; unknown, zero, not-applicable, withheld and suppressed never collapse.","violates":["INV-07"],"closesDefect":["D15"],"expectedCode":"EMLND11_E_NULL_SEMANTICS_COLLAPSE"},
{"id":"EM-LND-11-FX-078","target":"quantity-validator","kind":"positive","input":"A quantity carries item scope, value, unit, code list, pinned code-list version, precision and measurement basis.","expect":"Accepted as a complete quantity.","violates":[],"closesDefect":["D15"]},
{"id":"EM-LND-11-FX-079","target":"landscape-declaration","kind":"negative","input":"The landscape view allocates a new identifier for an observed lot.","expect":"Rejected; views never allocate identifiers.","violates":["INV-13","INV-18"],"closesDefect":["D16","D29"],"expectedCode":"EMLND11_E_VIEW_ALLOCATES_ID"},
{"id":"EM-LND-11-FX-080","target":"landscape-declaration","kind":"negative","input":"The landscape view issues a recall decision for the affected candidate set.","expect":"Rejected; recall is an accountable authority decision outside the landscape.","violates":["INV-18"],"closesDefect":["D16"],"expectedCode":"EMLND11_E_VIEW_EXERCISES_AUTHORITY"},
{"id":"EM-LND-11-FX-081","target":"landscape-declaration","kind":"negative","input":"The landscape view dispatches a shipment derived from its projection.","expect":"Rejected; dispatch is outside the view boundary.","violates":["INV-18"],"closesDefect":["D16"],"expectedCode":"EMLND11_E_VIEW_DISPATCHES"},
{"id":"EM-LND-11-FX-082","target":"landscape-declaration","kind":"positive","input":"The view emits a read-only candidate set and refers the decision to the accountable authority.","expect":"Accepted; no authority is exercised by the view.","violates":[],"closesDefect":["D16"]},
{"id":"EM-LND-11-FX-083","target":"provenance-register","kind":"negative","input":"The profile records ten single-provider bases out of fourteen with three dual-provider.","expect":"Rejected; 14 minus 3 dual equals 11 single-provider (10 Codex-only plus 1 Claude-only).","violates":["INV-22"],"closesDefect":["D17"],"expectedCode":"EMLND11_E_PROVENANCE_COUNT_MISMATCH"},
{"id":"EM-LND-11-FX-084","target":"provenance-register","kind":"positive","input":"baseProvenance partitions the fourteen bases into 3 dual-provider, 10 Codex-only waivers and 1 Claude-only waiver.","expect":"Accepted; the partition is disjoint, complete and sums to 14 with singleProvider=11.","violates":[],"closesDefect":["D17"]},
{"id":"EM-LND-11-FX-085","target":"provenance-register","kind":"negative","input":"The Grok study is recorded with model 'grok-4' and effort 'high' although neither value appears in the frozen materials.","expect":"Rejected; unrecorded provenance must be an explicit unknown marker.","violates":["INV-22"],"closesDefect":["D17","D26"],"expectedCode":"EMLND11_E_FABRICATED_PROVENANCE"},
{"id":"EM-LND-11-FX-086","target":"access-policy","kind":"negative","input":"A withheld segment is omitted from a minimum projection with no marker.","expect":"Rejected; withheld segments are marked withheld, never absent.","violates":["INV-17"],"closesDefect":["D18"],"expectedCode":"EMLND11_E_WITHHELD_RENDERED_ABSENT"},
{"id":"EM-LND-11-FX-087","target":"access-policy","kind":"negative","input":"A projection is served with no purpose binding on the request.","expect":"Rejected; access is deny-by-default and purpose-bound.","violates":["INV-17"],"closesDefect":["D18"],"expectedCode":"EMLND11_E_PURPOSE_BINDING_MISSING"},
{"id":"EM-LND-11-FX-088","target":"access-policy","kind":"positive","input":"A purpose-bound minimum projection returns permitted fields and explicit withheld markers for the rest.","expect":"Accepted; deny-by-default disclosure preserved.","violates":[],"closesDefect":["D18"]},
{"id":"EM-LND-11-FX-089","target":"fixtures.json","kind":"negative","input":"The fixtures file identifies its profile by display name only, with no contourId or profileRef.","expect":"Rejected; artifact references must resolve by contourId and path.","violates":["INV-09"],"closesDefect":["D19"],"expectedCode":"EMLND11_E_MISSING_ARTIFACT_REF"},
{"id":"EM-LND-11-FX-090","target":"fixtures.json","kind":"negative","input":"A fixture targets base WM-OBJ-099, which is absent from the profile bases.","expect":"Rejected; base references must resolve against the profile bases list.","violates":["INV-09"],"closesDefect":["D19"],"expectedCode":"EMLND11_E_DANGLING_BASE_REF"},
{"id":"EM-LND-11-FX-091","target":"checkpoint-manifest.json","kind":"negative","input":"The files list omits grok-study.raw.md and the three candidate-profile-offline files.","expect":"Rejected; every frozen artifact must appear in the manifest files list.","violates":["INV-09"],"closesDefect":["D19"],"expectedCode":"EMLND11_E_MANIFEST_FILE_LIST_INCOMPLETE"},
{"id":"EM-LND-11-FX-092","target":"checkpoint-manifest.json","kind":"positive","input":"Every files entry has either a computed sha256 or sha256 null with digestStatus to-be-computed-by-local-script.","expect":"Accepted; no digest is invented and none is silently missing.","violates":[],"closesDefect":["D19"]},
{"id":"EM-LND-11-FX-093","target":"checkpoint-manifest.json","kind":"negative","input":"A manifest entry carries a sha256 value that was not computed over the file bytes.","expect":"Rejected; digests are computed, never fabricated.","violates":["INV-22"],"closesDefect":["D19"],"expectedCode":"EMLND11_E_FABRICATED_DIGEST"},
{"id":"EM-LND-11-FX-094","target":"registry-conflict-register","kind":"negative","input":"The WM-OBJ-019 registry parent_ids signal is used as authoritative while the COMPOSE relation row contradicts it.","expect":"Rejected; a conflicting signal cannot be used as authority.","violates":["INV-21"],"closesDefect":["D20"],"expectedCode":"EMLND11_E_UNRESOLVED_PARENT_SIGNAL"},
{"id":"EM-LND-11-FX-095","target":"registry-conflict-register","kind":"negative","input":"registry entry_kind standalone-mm overrides the specification entry kinds aggregate, event and pattern.","expect":"Rejected; the conflict stands unresolved and unselected.","violates":["INV-21"],"closesDefect":["D20"],"expectedCode":"EMLND11_E_ENTRY_KIND_CONFLICT"},
{"id":"EM-LND-11-FX-096","target":"registry-conflict-register","kind":"positive","input":"Both sides of each registry conflict are recorded with status unresolved and selected null.","expect":"Accepted; conflicts are disclosed without silent selection.","violates":[],"closesDefect":["D20"]},
{"id":"EM-LND-11-FX-097","target":"publication-gate","kind":"negative","input":"An artifact sets publishableCanonical true while publicationHolds is non-empty.","expect":"Rejected; no canonicity or publication-readiness claim while holds stand.","violates":["INV-21"],"closesDefect":["D21"],"expectedCode":"EMLND11_E_PUBLICATION_CLAIM_FORBIDDEN"},
{"id":"EM-LND-11-FX-098","target":"publication-gate","kind":"negative","input":"EPCIS 2.0 is silently selected over 2.0.1 to resolve the divergence.","expect":"Rejected; divergent pins are recorded unresolved with selected null.","violates":["INV-21"],"closesDefect":["D21"],"expectedCode":"EMLND11_E_PIN_DIVERGENCE_UNRESOLVED"},
{"id":"EM-LND-11-FX-099","target":"work-order","kind":"negative","input":"WM-ACT-007 is used as the production and transformation work order for a manufacturing routing.","expect":"Rejected; WM-ACT-007 is maintenance-scoped and the production work order and routing master are unassigned.","violates":["INV-13","INV-21"],"closesDefect":["D21"],"expectedCode":"EMLND11_E_MAINTENANCE_SCOPE_EXCEEDED"},
{"id":"EM-LND-11-FX-100","target":"publication-gate","kind":"negative","input":"A hold states that fixtures are absent while fixtures.json contains cases.","expect":"Rejected; the hold must state fixtures specified and not executed.","violates":["INV-21"],"closesDefect":["D21","D27"],"expectedCode":"EMLND11_E_STALE_HOLD"},
{"id":"EM-LND-11-FX-101","target":"publication-gate","kind":"negative","input":"A hold states that independent Grok review is pending while grok-study.raw.md is frozen evidence.","expect":"Rejected; the hold must state the review received and reconciled, with remaining holds unchanged.","violates":["INV-21","INV-22"],"closesDefect":["D21","D26"],"expectedCode":"EMLND11_E_STALE_HOLD"},
{"id":"EM-LND-11-FX-102","target":"publication-gate","kind":"positive","input":"publicationHolds enumerates missing masters, registry conflicts, maintenance scope, pin divergence, absent crosswalks, unexecuted fixtures and single-provider bases.","expect":"Accepted; all seven holds disclosed and no readiness claimed.","violates":[],"closesDefect":["D21"]},
{"id":"EM-LND-11-FX-103","target":"publication-gate","kind":"negative","input":"An artifact reports that the fixture suite passed during this frozen audit.","expect":"Rejected; fixtureExecution is not-executed and no run occurred.","violates":["INV-21","INV-22"],"closesDefect":["D21"],"expectedCode":"EMLND11_E_UNRUN_FIXTURE_CLAIM"},
{"id":"EM-LND-11-FX-104","target":"fixtures.json","kind":"negative","input":"A case omits target, violates and closesDefect.","expect":"Rejected against fixtures schema v2 required fields.","violates":["INV-09"],"closesDefect":["D22"],"expectedCode":"EMLND11_E_FIXTURE_SCHEMA_INCOMPLETE"},
{"id":"EM-LND-11-FX-105","target":"fixtures.json","kind":"negative","input":"A negative case omits expectedCode.","expect":"Rejected; every negative case declares a stable error code.","violates":["INV-09"],"closesDefect":["D22"],"expectedCode":"EMLND11_E_MISSING_EXPECTED_CODE"},
{"id":"EM-LND-11-FX-106","target":"fixtures.json","kind":"negative","input":"One case asserts both delivery acceptance and title transfer from a single scan.","expect":"Rejected; one case asserts one inference so the failing rule is localisable.","violates":["INV-06","INV-09"],"closesDefect":["D23"],"expectedCode":"EMLND11_E_FIXTURE_CONFLATION"},
{"id":"EM-LND-11-FX-107","target":"fixtures.json","kind":"positive","input":"The seven original cases, upgraded with canonicalId, target, violates, closesDefect and expectedCode, are validated against schema v2.","expect":"Accepted; all seven conform and retain their original slug ids.","violates":[],"closesDefect":["D22","D23"]},
{"id":"EM-LND-11-FX-108","target":"invariant-registry","kind":"negative","input":"A fixture lists violates INV-99, which is absent from the registry.","expect":"Rejected; every violates entry resolves to a registered invariant.","violates":["INV-09"],"closesDefect":["D24"],"expectedCode":"EMLND11_E_UNKNOWN_INVARIANT_REF"},
{"id":"EM-LND-11-FX-109","target":"invariant-registry","kind":"positive","input":"Coverage is computed across the full suite for INV-01 through INV-22.","expect":"Accepted; each of the twenty-two invariants has at least one positive and at least one negative fixture.","violates":[],"closesDefect":["D24"]},
{"id":"EM-LND-11-FX-110","target":"candidate-profile-offline/README.md","kind":"negative","input":"The README omits non-canonical status, the nine gaps and the no-allocation statement.","expect":"Rejected; the delta README must state decision, bases, provenance counts, gaps, holds and absence of readiness claims.","violates":["INV-21"],"closesDefect":["D25"],"expectedCode":"EMLND11_E_README_UNDERSPECIFIED"},
{"id":"EM-LND-11-FX-111","target":"checkpoint-manifest.json","kind":"negative","input":"grokPromptStatus remains prepared-unsent-action-time-confirmation-required while grok-study.raw.md is frozen.","expect":"Rejected; status must read sent-response-received-reconciled.","violates":["INV-22"],"closesDefect":["D26"],"expectedCode":"EMLND11_E_STALE_PROVIDER_STATUS"},
{"id":"EM-LND-11-FX-112","target":"checkpoint-manifest.json","kind":"negative","input":"A single providerStudy object is retained although two provider studies exist.","expect":"Rejected; providerStudies must be an array holding both studies.","violates":["INV-22"],"closesDefect":["D26"],"expectedCode":"EMLND11_E_PROVIDER_STUDY_CARDINALITY"},
{"id":"EM-LND-11-FX-113","target":"checkpoint-manifest.json","kind":"positive","input":"providerStudies holds the Claude entry with recorded settings and the Grok entry with explicit unknown-not-recorded settings and visible-response-only scope.","expect":"Accepted; both studies attributed without fabrication.","violates":[],"closesDefect":["D26"]},
{"id":"EM-LND-11-FX-114","target":"identifier-guard","kind":"negative","input":"The Lot/Batch gap is promoted and given an allocated model identifier in this contour.","expect":"Rejected; the nine gaps stay identifier-unassigned and unpromoted.","violates":["INV-13"],"closesDefect":["D29"],"expectedCode":"EMLND11_E_GAP_PROMOTION_FORBIDDEN"},
{"id":"EM-LND-11-FX-115","target":"identifier-guard","kind":"negative","input":"A new catalogue or runtime identifier is allocated for Operations Landscape or Supply Network.","expect":"Rejected; identifierAllocation is none for both classes and allocatedInThisContour is empty.","violates":["INV-13"],"closesDefect":["D29"],"expectedCode":"EMLND11_E_IDENTIFIER_ALLOCATION_FORBIDDEN"},
{"id":"EM-LND-11-FX-116","target":"identifier-guard","kind":"positive","input":"All nine gaps are recorded identifierUnassigned true, promoted false, with allocatedInThisContour empty.","expect":"Accepted; reuse confers no identifier.","violates":[],"closesDefect":["D29"]},
{"id":"EM-LND-11-FX-117","target":"correction-lineage","kind":"negative","input":"A correction overwrites an issued declaration revision in place.","expect":"Rejected; corrections append linked successors and issued revisions are immutable.","violates":["INV-10"],"closesDefect":["D30"],"expectedCode":"EMLND11_E_CORRECTION_NOT_APPENDED"},
{"id":"EM-LND-11-FX-118","target":"correction-lineage","kind":"negative","input":"A retired identifier is reassigned to a new subject.","expect":"Rejected; identifiers are never reused.","violates":["INV-10"],"closesDefect":["D30"],"expectedCode":"EMLND11_E_IDENTIFIER_REUSE"},
{"id":"EM-LND-11-FX-119","target":"correction-lineage","kind":"positive","input":"A correction is appended as a linked successor and the retired revision identifier still resolves.","expect":"Accepted; lineage appended and retired identifier resolvable.","violates":[],"closesDefect":["D30"]}
]
```

---

## 4. Exact final fixture counts

| | Total | Positive | Negative |
|---|---|---|---|
| Existing (`fixtures.json`, canonical IDs `EM-LND-11-FX-001`…`007`) | 7 | 3 | 4 |
| Added here (`EM-LND-11-FX-008`…`119`) | 112 | 29 | 83 |
| **Final suite** | **119** | **32** | **87** |

Checks the local script must assert:

- `len(cases) == 119`; IDs `EM-LND-11-FX-001`…`EM-LND-11-FX-119` present exactly once, contiguous, no duplicates; the seven original slug IDs (`event-backed-recall`, `blended-bulk`, `unknown-supplier`, `bom-proves-installation`, `scan-proves-acceptance`, `missing-stock-zero`, `view-orders-recall`) retained and mapped to `EM-LND-11-FX-001`…`007` in that order.
- `count(kind=="positive") == 32`, `count(kind=="negative") == 87`, sum 119; no other `kind` value.
- Every negative case has a non-empty `expectedCode`; distinct error codes: 83 negative cases over 82 distinct codes (`EMLND11_E_STALE_HOLD` is shared by `FX-100` and `FX-101` by design).
- `closesDefect` coverage: D1…D30, all thirty referenced by at least one case; D1→5 cases, D2→5, D3→7, D4→6, D5→6, D6→4, D7→5, D8→3, D9→4, D10→4, D11→6, D12→6, D13→8, D14→4, D15→4, D16→4, D17→3, D18→3, D19→5, D20→3, D21→7, D22→3, D23→4, D24→2, D25→1, D26→4, D27→1, D28→1, D29→4, D30→3.
- `violates` coverage: INV-01…INV-22, each with ≥1 positive and ≥1 negative case (`FX-109`); every `violates` entry resolves in `/invariants`.
- `fixtureExecution` remains `"not-executed"`; counts are specification counts, not pass counts.

---

## 5. Freeze decision

**FROZEN. Deterministic remediation closes this audit without rerun.**

The EM-LND-11 boundary decision is settled and preserved exactly as adjudicated: Operations Landscape is a governed declaration plus a reproducible, exception-aware projection with artifact identity only; Supply Network is a scoped graph view hosted inside that declaration over party, facility and supply-relation masters it does not own; neither is a root, neither mints subject identity, no projection becomes a root; no catalogue or runtime identifier is allocated; the nine named gaps remain identifier-unassigned and unpromoted. The visible Grok response corroborates the decision and contributes two tightening invariants (consumed-quantity bound on proven-affected; no view edge may close an unknown-origin break) plus one axis separation (item classification versus result completeness); none of these is evidence that the decision is inconsistent, so none reopens it.

All thirty defects are encoding, enumeration, schema, reference and staleness defects in the profile, fixtures, README, manifest and continuation records. Every one has a closed-form literal edit in Section 2 and at least one closing fixture in Section 3, and the full suite is specified at 119 cases (32 positive, 87 negative) with 22 registered invariants, 82 stable error codes, and no fabricated digest, timestamp, revision or provider setting. Applying Section 2 verbatim and writing Section 3 into `candidate-profile-offline/fixtures.json` under `schemaVersion: 2` discharges the audit; no further provider study, dossier re-read, fixture execution or review round is required or requested.

Holds that survive the freeze and continue to bar publication: nine unassigned subject/event masters; unresolved registry parent-signal and `entry_kind` conflicts; WM-ACT-007 maintenance scope with unresolved K11 duplication and no production/transformation work order or routing master; divergent and unselected EPCIS, CBV and UBL pins; absent crosswalks; fixtures specified but not executed; eleven single-provider non-canonical bases. `publishableCanonical` is false and no canonicity, installability or publication-readiness is claimed.
