# EM-OPS-05 — Frozen Semantic Audit (final)

**Scope:** supplied dossier and the seven submitted artifacts only. No tools, no browsing, no identifier invention, no registry allocation, no standards-conformance claim, no publication-readiness claim. No further provider study or rerun is requested or required.

---

## 1. Verdict

**CONDITIONAL ACCEPT of the adjudicated semantic boundary. REJECT of the artifact set as submitted.**

The boundary is reconciled and not re-opened. All three studies converge and no submitted artifact contradicts the adjudicated decision:

- **Lot** — new root, identifier-unassigned. Confirmed: issuer-qualified identity plus a lifecycle (production, split, merge, blend, quarantine, release, expiry, exhaustion, recall marking) that WM-OBJ-001 explicitly refuses and WM-OBJ-020 cannot carry.
- **Transformation Event** — new root, identifier-unassigned. Confirmed: WM-FLW-012 owns one stock-affecting transition and no input/output set, yield or scrap; WM-FLW-013 declares its event master external; WM-ACT-007 is maintenance-scoped. The authoritative actual-transformation fact is unmastered.
- **Stock Position** — reuse **WM-OBJ-020** unchanged, not extended into lot identity or genealogy.
- **Shipment** — reuse **WM-FLW-011**, valid only with its mandatory kind discriminator declared and many-to-many split/consolidation allocation intact.
- **Logistics Event** — **rejected as a root**, split across WM-FLW-004 (observation, handover), WM-FLW-012 (stock transition, posting), WM-FLW-013 (trace edge, custody interval), WM-ECO-024 (dispatch, receipt, inspection, acceptance). A generic event root would duplicate four masters.
- **Inventory–Genealogy** — thin declarative binding profile, no runtime identifier, no business-object mastership.

The artifact set is rejected because the artifacts do not mechanically enforce the boundary they state. Nine of the twelve adjudicated check axes are asserted in prose invariants but are unrepresentable or unenforceable in the submitted object schemas: **required genealogy** (no element structure), **partial consumption** (no residual quantity, no consumed-versus-held distinction), **balance derivation** (no enumerated derivation mode, no completeness perimeter), **correction events** (optional, not a required type), **effective/record/knowledge time** (Lot has none; Transformation has recordTime optional), **provenance** (Lot has none; Transformation has evidenceDigest only), **recall scope** (no fixture or constraint refusing whole-SKU recall), **shipment/delivery/acceptance separation** (profile has no fixtures at all), and **zero-identifier/publication holds** (profile asserts neither). Every negative fixture is also missing `expectedCode`, so no negative is deterministically falsifiable.

**35 material defects. 51 additional fixtures required. 12 prior fixtures preserved (one relocated). Post-remediation suite: 63 fixtures.**

---

## 2. Material defects — submitted artifacts only

Invariant references are array-index, 1-based, within the named artifact. Where a `requiredWhen` is specified it is a conditional-required key, not an optional one.

### Artifact A — Lot allocation (`vercy-model-allocation-candidate/v1`)

**D1. `Lot.invariants[4]` requires unit, basis and scope on every quantity, but no object field carries scope. The invariant is unenforceable.**
Remediation: in `objects.Lot.required`, replace `["definitionRef","quantityBasis","unit","status"]` with
`["definitionRef","quantityBasis","quantityScope","unit","status","recordTime","versionId","provenance"]`
and add to `objects.Lot` the key
`"quantityScope": {"grain": ["whole-lot","declared-sublot","declared-position-slice"], "unitCodeListVersionPinned": true, "measurementBasis": ["net","gross","theoretical","mass-balance"]}`.

**D2. Lifecycle declares `partially-consumed` but no field holds residual quantity and no invariant preserves it. Partial consumption — an adjudicated check axis — is unrepresentable.**
Remediation: add to `objects.Lot` the key
`"residual": {"requiredWhen": "status in [partially-consumed, quarantined, released]", "quantity": "required", "unit": "required", "basis": "required", "asOfRecordTime": "required", "derivation": ["authoritative-snapshot","event-ledger-projection"]}`
and append to `Lot.invariants`:
`"Residual lot quantity remains explicit, unit-and-basis qualified and traceable after every partial consumption; consumption never closes a lot by implication."`

**D3. `identityTest.independentLifecycle` and `objects.Lot.lifecycle` collapse two orthogonal axes into one flat list; `released` and `partially-consumed` are concurrently true in the accepted scenario, so the state set is not a state machine.**
Remediation: set
`"independentLifecycle": ["created","available","partially-consumed","exhausted","closed"]`
in both `identityTest` and `objects.Lot.lifecycle`, add
`"concurrentDispositionStates": ["unrestricted","quarantined","released","expired","recall-marked"]`,
and append to `Lot.invariants`:
`"Consumption state and disposition state are concurrent independent axes; no disposition value implies a consumption value and no consumption value implies a disposition value."`

**D4. Lifecycle state `recalled` asserts a recall while `boundary.excludes` excludes recall authority and `Lot.invariants[10]` denies it. The artifact contradicts itself.**
Remediation: in `concurrentDispositionStates` use `"recall-marked"` (never `"recalled"`); add to `objects.Lot`
`"recallDecisionRef": {"requiredWhen": "disposition == recall-marked", "authority": "external", "mustNotBeMintedHere": true}`
and append to `Lot.invariants`:
`"A recall-marked disposition is valid only while citing an external recall decision reference; no model in this contour creates, infers or substitutes recall authority."`

**D5. Lineage is one-directional. `optional.successorRefs` cannot express merge or blend, which need multiple predecessors and a proportion basis, so `Lot.invariants[5]` cannot be satisfied for the accepted blended co-product.**
Remediation: remove `"successorRefs"` from `objects.Lot.optional` and add
`"lineage": {"requiredWhen": "lot was created by, or contributed to, split | merge | blend | repack | requalification", "kind": ["split","merge","blend","repack","requalification"], "predecessorRefs": "required", "successorRefs": "required", "proportionBasis": "required", "proportionMethod": ["measured","declared","mass-balance-inferred"], "edgeAssertionClass": ["asserted","inferred"]}`.

**D6. The Lot has no record or knowledge time and no version key, so the `versionIdentity` claim of append-only correction versions is unenforceable, and effective/record/knowledge time — an adjudicated axis — is absent.**
Remediation: `recordTime` and `versionId` are added to `required` by D1; additionally add to `objects.Lot`
`"knowledgeTimeRange": {"from": "required", "to": "open-ended-allowed"}, "supersedesVersionRef": {"requiredWhen": "versionId is not the first version"}`,
all times `"format": "RFC3339, seconds precision, explicit offset"`, and append to `Lot.invariants`:
`"Effective time, record time and knowledge time remain separately recorded and are never collapsed; a correction creates a new versionId citing supersedesVersionRef and never rewrites a prior version."`

**D7. The Lot carries no provenance. `Lot.invariants[1]` forbids inferred identity and `invariants[8]` distinguishes unobserved from zero, but nothing records source, agent, method or evidence.**
Remediation: add to `objects.Lot`
`"provenance": {"sourceSystem": "required", "assertingAgentRef": "required", "method": ["observed","declared","inferred"], "evidenceDigest": "required", "confidence": "optional"}`
and append to `Lot.invariants`:
`"Every lot assertion carries source system, asserting agent, method and evidence digest; declared, observed and inferred assertions never merge."`

**D8. `optional.originRef` is untyped, so a lot may claim a production origin without citing the transformation occurrence that `Lot.invariants[6]` requires instead of BOM or routing.**
Remediation: replace `"originRef"` with
`"originRef": {"kind": ["transformation-event-candidate","external-receipt","opening-balance"], "candidateName": "Transformation Event", "modelId": null, "registryId": null, "allocationState": "unassigned", "requiredWhen": "origin is production", "mustNotCiteBomOrRouting": true}`.

**D9. Both allocation artifacts carry the stale hold `"Independent Grok review and one frozen semantic audit are pending."` The dossier records a completed independent Grok study and this completed frozen audit. The artifact record contradicts its own provenance.**
Remediation: in `Lot allocation.holds` and `Transformation allocation.holds`, replace that string with
`"Independent provider review is on record and one frozen semantic audit was completed 2026-10-01; closure of the 35 recorded audit defects and the 51 recorded additional fixtures remains pending. No installability, conformance or publication-readiness claim is made."`

### Artifact B — Lot fixtures (`vercy-enterprise-allocation-fixtures/v1`)

**D10. All three negatives (`sku-is-lot`, `stock-position-is-lot`, `bom-proves-genealogy`) lack `expectedCode`, so each rejection is unverifiable — any refusal for any reason passes.**
Remediation: add `"expectedCode": "LOT-SKU-AS-LOT-IDENTITY"` to `sku-is-lot`, `"expectedCode": "LOT-POSITION-AS-LOT-IDENTITY"` to `stock-position-is-lot`, `"expectedCode": "LOT-BOM-NOT-GENEALOGY"` to `bom-proves-genealogy`.

**D11. The fixture shape lacks `target`, `violates` and `closesDefect`, and keys the suite by `candidateName`, so no fixture is traceable to the invariant it guards.**
Remediation: set `"format": "vercy-enterprise-allocation-fixtures/v2"`; retain `"candidateName": "Lot"`; add to every case `"target": "Lot"`, `"violates": "<Lot.invariants[n]>"` for negatives and `"violates": null` for positives, and `"closesDefect": "<D##>"`. Prior cases take `"closesDefect": "preserved-prior"`.

**D12. Three expects are non-deterministic. `targeted-recall` expects "only proven or reason-coded potential descendants" without enumerating the sets; `split-lot` and `serialized-membership` name no concrete identities or values.**
Remediation: replace `targeted-recall.expect` with
`"Exposure set = {proven: S1..S10 via event-backed output edges of T}, {potential: blended co-product lot, reasonCode: mass-balance-commingled}, {notEvidenced: all same-SKU units of other lots}; recallDecisionRef is absent and no SKU-level scope is emitted."`
Replace `split-lot.expect` with
`"Successors L-a and L-b carry distinct issuer-qualified identities, lineage.kind = split, lineage.predecessorRefs = [L], proportionBasis stated with unit; L retains its identity and its residual quantity."`
Replace `serialized-membership.expect` with
`"S1..S10 each retain WM-OBJ-001 identity and carry lot-of-origin provenance referencing L; no item identity is derived from L and L does not decompose into ten instances."`

**D13. Coverage gaps in the Lot suite: no case for partial consumption and residual quantity, merge, blend proportion, identifier reuse, unobserved-versus-zero, disposition-axis collapse, recall marking without authority, record-time absence, provenance absence, untyped origin, membership-as-identity, or custody-versus-title. Twelve of the thirteen invariants are unexercised.**
Remediation: add fixtures `F-LOT-01` … `F-LOT-14` from §3 verbatim.

### Artifact C — Binding profile (`vercy-enterprise-profile-candidate/v1`)

**D14. The profile declares `bases` and `constraints` but never states what it may reference and what it must not own. Thinness is asserted nowhere and is therefore untestable.**
Remediation: add
`"owns": ["cross-model binding constraints","derivation-mode declarations","completeness-perimeter declarations"], "mustNotOwn": ["any business-object identity","any lifecycle or status master","any quantity of record","any posting, dispatch, acceptance, adjustment or recall authority","any identifier namespace"]`.

**D15. The profile binds six registry drafts and omits both identifier-unassigned candidates it exists to bind. The genealogy constraints reference events no base supplies.**
Remediation: add
`"unassignedCandidateBindings": [{"candidateName": "Lot", "modelId": null, "registryId": null, "allocationState": "unassigned"}, {"candidateName": "Transformation Event", "modelId": null, "registryId": null, "allocationState": "unassigned"}], "identifierInventionForbidden": true`.

**D16. The profile asserts `newRuntimeId: false` but carries no `canonicalPublishable` flag, no null identifier keys and no holds, unlike both allocation artifacts. The zero-identifier and publication holds are not stated where the cross-model binding lives.**
Remediation: add
`"canonicalPublishable": false, "modelId": null, "registryId": null, "holds": ["No runtime, catalogue or registry identifier is allocated by this profile.","Reuse of WM-OBJ-020 and WM-FLW-011 is a named-draft reference, not verification that those drafts satisfy these constraints.","All bases are reviewable drafts; no installability, conformance or publication-readiness claim is made."]`.

**D17. `constraints[1]` requires a declared snapshot-or-projection mode but enumerates no values, defines no completeness perimeter, and does not forbid mixing modes within one derived balance. Balance derivation is undecidable.**
Remediation: replace `constraints[1]` with
`"Stock Position reuses WM-OBJ-020 and declares derivationMode ∈ {authoritative-source-snapshot, complete-ledger-projection}; complete-ledger-projection additionally declares completenessPerimeterRef, ledgerCutoffRecordTime and correctionsIncluded = true; a single derived balance never mixes modes and no derivation authorizes a posting."`

**D18. Correction is stated as prose only. No correction event type is a required binding, so `constraints[6]` cannot be enforced and silent overwrite is not mechanically refused.**
Remediation: append constraint
`"Every correction is bound to an explicit append-only correction event: inventory corrections to a WM-FLW-012 compensating posting, transformation corrections to a Transformation Event successor assertion; both cite priorAssertionRef, correctionReason and recordTime. Mutation in place, deletion and identifier reuse are refused."`

**D19. The profile carries no time model. Effective, event, observation, record, posting, knowledge and correction time are nowhere separated at the binding layer where cross-master joins occur.**
Remediation: append constraint
`"Effective, event, observation, record, posting, knowledge and correction time remain separately carried across every binding, RFC 3339 with seconds precision and explicit offset; no join substitutes one time for another and no status implies a time."`

**D20. The profile omits the recall boundary. Nothing at the binding layer refuses whole-SKU scope or distinguishes exposure analysis from recall authority — the two strongest adjudicated negatives.**
Remediation: append constraint
`"Exposure analysis yields proven sets from event-backed consumption and output edges and potential sets from blended, mass-balance, inferred, stale or incomplete edges with reason codes; same-SKU or BOM-only matches are notEvidenced and are never declared unaffected absent a closed perimeter. Exposure analysis is not recall authority and SKU-level scope is never derived from an affected lot."`

**D21. No fixture artifact exists for the profile. The profile carries the shipment-kind, logistics-split, plan/movement/posting/custody/receipt/inspection/acceptance separation and derivation constraints, and none of them is tested anywhere in the submission.**
Remediation: create `{"format": "vercy-enterprise-allocation-fixtures/v2", "candidateName": "Enterprise Inventory and Genealogy Binding", "cases": [...]}` containing `F-PRF-01` … `F-PRF-20` from §3 verbatim.

### Artifacts D and G — Validation policies (`vercy-allocation-validation/v1`)

**D22. Neither policy requires `expectedCode` on negatives, which is why D10 and D33 passed submission.**
Remediation: add to `requirements` in both policies
`"requiresExpectedCodeOnEveryNegative": true, "expectedCodeMustBeUniqueWithinSuite": true`.

**D23. `minimumFixtures: 3` is below the delivered six and far below invariant coverage; the policies require no negative minimum, no deterministic expect, no `violates`/`closesDefect` traceability and no per-invariant coverage.**
Remediation: in both policies replace `"minimumFixtures": 3` with
`"minimumFixtures": 18, "minimumNegativeFixtures": 10, "requiresDeterministicExpect": true, "requiresViolatesReference": true, "requiresClosesDefectReference": true, "requiresEveryInvariantCoveredByAtLeastOneFixture": true, "requiresEveryConditionalRequiredFieldCoveredByOneNegative": true, "requiresProvenanceFields": true, "requiresRecordAndKnowledgeTime": true, "forbidsIdentifierInvention": true`.

**D24. No validation policy exists for the binding profile, so its thinness, zero-identifier state and constraint coverage are ungated.**
Remediation: create
`{"format": "vercy-allocation-validation/v1", "appliesTo": "PROFILE", "requirements": {"modelIdMustBeNull": true, "registryIdMustBeNull": true, "newRuntimeIdMustBeFalse": true, "canonicalPublishableMustBeFalse": true, "requiresOwnsAndMustNotOwn": true, "requiresUnassignedCandidateBindings": true, "minimumConstraints": 10, "minimumFixtures": 20, "minimumNegativeFixtures": 13, "requiresExpectedCodeOnEveryNegative": true, "requiresDeterministicExpect": true, "requiresViolatesReference": true, "requiresClosesDefectReference": true, "forbidsBusinessObjectMastership": true, "forbidsIdentifierInvention": true, "forbidsPublicationReadinessClaim": true}}`.

### Artifact E — Transformation allocation (`vercy-model-allocation-candidate/v1`)

**D25. `recordTime` is optional while `TransformationEvent.invariants[6]` requires event and record time to remain distinct. An invariant cannot rest on an optional field.**
Remediation: move `"recordTime"` from `optional` to `required`; add `"knowledgeTimeRange": {"from": "required", "to": "open-ended-allowed"}` to `required`; pin all times to `"RFC3339, seconds precision, explicit offset"`.

**D26. `yield`, `scrap` and `coProducts` are optional, contradicting `boundary.owns`, `invariants[5]` and local-synthesis required invariant 8; no reconciliation method is declared.**
Remediation: move `"yield"`, `"scrap"` and `"coProducts"` from `optional` to `required` (empty-with-stated-reason permitted, absent not permitted) and add to `required`
`"quantityReconciliation": {"method": ["mass-balance","unit-count","declared-yield-factor"], "basis": "required", "unitCodeListVersionPinned": true, "toleranceDeclared": true, "unreconciledResidualLabelled": true}`.

**D27. `inputs` and `outputs` are required but structureless. Per-element quantity, unit, basis and consumed-versus-held are undefined, so required genealogy and partial consumption are both unrepresentable.**
Remediation: add to `objects.TransformationEvent`
`"inputs[]": {"lotRef": "required", "consumedQuantity": "required", "unit": "required", "basis": "required", "quantityScope": "required", "consumptionCompleteness": ["fully-consumed","partially-consumed"], "residualAssertedOnLot": {"requiredWhen": "consumptionCompleteness == partially-consumed"}, "evidenceDigest": "required"}`
and
`"outputs[]": {"outputKind": ["lot","serialized-item","co-product-lot","scrap"], "ref": "required", "quantity": "required", "unit": "required", "basis": "required", "edgeAssertionClass": ["asserted","inferred"], "evidenceDigest": "required"}`.

**D28. `authorityRef` is optional while `boundary.owns` claims authority and the dossier requires authority on the event that occurred.**
Remediation: move `"authorityRef"` from `optional` to `required` and add
`"authorityScope": ["production-execution","material-genealogy"], "mustNotBeDerivedFromLaterStatus": true`.

**D29. Lifecycle admits `voided` with no void reason, no successor and no non-destructive rule, which defeats `invariants[7]`: a void is an undocumented retraction.**
Remediation: add to `objects.TransformationEvent`
`"voidRecord": {"requiredWhen": "status == voided", "voidReason": "required", "voidAuthorityRef": "required", "priorAssertionRetained": true, "recordTime": "required"}`
and append to `TransformationEvent.invariants`:
`"A void is an appended non-destructive assertion citing reason, authority and record time; prior assertions and their genealogy edges remain readable and are never deleted or rewritten."`

**D30. `supersedesRef` exists with no `supersededByRef`, so status `superseded` is mechanically unreachable and the correction chain is traversable in one direction only.**
Remediation: add to `objects.TransformationEvent`
`"supersededByRef": {"requiredWhen": "status == superseded"}`
and append to `TransformationEvent.invariants`:
`"Correction lineage is bidirectionally resolvable: supersedesRef and supersededByRef are both present on a superseded assertion and no assertion is its own successor."`

**D31. The WM-ACT-007 reference carries its maintenance-only caveat in a free-text purpose string, so nothing prevents the reference being used as production authorization — the exact collapse `invariants[2]` forbids.**
Remediation: replace that reference entry with
`{"target": "WM-ACT-007", "purpose": "Work-order reference", "constraint": "maintenance-scoped; must-not-be-used-as-production-authorization", "referenceClass": "restricted", "blockedUntil": "production-work-order boundary is canonically allocated"}`.

**D32. Provenance is a bare `evidenceDigest`. Source system, asserting agent, method and confidence are absent, so `invariants[10]` — inferred, mass-balance and stale edges stay labelled — has no field to label with.**
Remediation: add to `objects.TransformationEvent.required`
`"provenance": {"sourceSystem": "required", "assertingAgentRef": "required", "method": ["observed","declared","inferred"], "confidence": "optional", "edgeAssertionClass": ["asserted","inferred","mass-balance-inferred","stale","incomplete"]}`.

### Artifact F — Transformation fixtures (`vercy-enterprise-allocation-fixtures/v1`)

**D33. All three negatives (`routing-proves-event`, `event-is-work-order`, `output-means-accepted`) lack `expectedCode`; `output-means-accepted` further expects "both inferences are rejected" without naming either.**
Remediation: add `"expectedCode": "TRX-ROUTING-NOT-EVENT-EVIDENCE"` to `routing-proves-event`, `"expectedCode": "TRX-WORK-ORDER-IDENTITY-MERGE"` to `event-is-work-order`, and to `output-means-accepted` add `"expectedCodes": ["TRX-OUTPUT-NOT-DELIVERY","TRX-OUTPUT-NOT-ACCEPTANCE"]` with expect replaced by
`"Both inferences are rejected separately: output creation does not establish delivery and does not establish acceptance; each rejection is emitted with its own code."`

**D34. Shape and determinism match D11 and D12. `corrected-quantity` names no status transition, no retained original value and no second record time.**
Remediation: set `"format": "vercy-enterprise-allocation-fixtures/v2"`, add `"target": "Transformation Event"`, `violates` and `closesDefect` to every case per D11, and replace `corrected-quantity.expect` with
`"The original assertion retains quantity 99, status becomes superseded with supersededByRef set; the successor asserts 100 with supersedesRef, a later recordTime and an unchanged eventTime; no value is overwritten."`

**D35. `partial-shipment-after-production` is mis-scoped — dispatch, receipt and acceptance separation is profile and WM-ECO-024 scope, not transformation scope — and the suite has no case for inferred-edge promotion, missing-output-as-zero, consumption-as-title-transfer, or exposure-as-recall-authority. Invariants 8, 10, 11 and 12 are unexercised.**
Remediation: move `partial-shipment-after-production` to the profile fixture set created under D21 with `"target": "Enterprise Inventory and Genealogy Binding"` and expect replaced by
`"Transformation of S1..S10, stock postings, shipment SH of S1..S6, receipt of five units, the S6 damage exception and acceptance remain five separately asserted facts; S6 is dispatched, not delivered, not accepted."`
Then add `F-TRX-01` … `F-TRX-17` from §3 verbatim.

---

## 3. Additional deterministic fixtures required

Exactly 51 fixtures. `violates` is `null` if and only if `kind` is `positive`. Every negative carries `expectedCode` in addition to the required keys.

```json
[
  {"id":"F-LOT-01","target":"Lot","kind":"positive","input":"Lot L holds 1000 kg net. Transformation T consumes 400 kg. No other event touches L.","expect":"L retains identity, consumption state partially-consumed, residual.quantity 600, residual.unit kg, residual.basis net, residual.asOfRecordTime set, derivation declared; L is not closed or exhausted.","violates":null,"closesDefect":"D2"},
  {"id":"F-LOT-02","target":"Lot","kind":"positive","input":"Lots L1 (300 kg) and L2 (200 kg) are merged into a single lot L3.","expect":"L3 carries a new issuer-qualified identity, lineage.kind merge, lineage.predecessorRefs [L1,L2], proportionBasis 300 kg and 200 kg with unit, proportionMethod measured, edgeAssertionClass asserted; L1 and L2 retain identity with residual 0 and consumption state exhausted.","violates":null,"closesDefect":"D5"},
  {"id":"F-LOT-03","target":"Lot","kind":"positive","input":"Lot L and lot M are blended in a silo; the resulting co-product lot C cannot be apportioned by measurement.","expect":"C carries lineage.kind blend, predecessorRefs [L,M], proportionMethod mass-balance-inferred and edgeAssertionClass inferred; the inferred lineage is never emitted as asserted and never establishes one-to-one continuity.","violates":null,"closesDefect":"D5"},
  {"id":"F-LOT-04","target":"Lot","kind":"negative","input":"A lot is created with quantityBasis and unit but no quantityScope.","expect":"Creation is refused for a missing quantity scope; no default grain is substituted.","violates":"Lot.invariants[4]","closesDefect":"D1","expectedCode":"LOT-QTY-SCOPE-MISSING"},
  {"id":"F-LOT-05","target":"Lot","kind":"negative","input":"A closed lot identifier is reassigned to a newly produced lot by the same issuer.","expect":"Reassignment is refused; the identifier remains permanently bound to the retired lot.","violates":"Lot.invariants[12]","closesDefect":"D13","expectedCode":"LOT-ID-REUSE-FORBIDDEN"},
  {"id":"F-LOT-06","target":"Lot","kind":"negative","input":"No stock row exists for lot L at site W; a balance report states L holds 0 at W.","expect":"The zero assertion is refused; the absent row resolves to unobserved and unknown, zero, not-applicable, withheld and suppressed remain distinct.","violates":"Lot.invariants[8]","closesDefect":"D13","expectedCode":"LOT-ABSENT-ROW-NOT-ZERO"},
  {"id":"F-LOT-07","target":"Lot","kind":"negative","input":"Lot L is set to disposition recall-marked with no recallDecisionRef, on the strength of an exposure analysis.","expect":"The disposition change is refused for absent external recall authority; the exposure result is retained as analysis only.","violates":"Lot.invariants[10]","closesDefect":"D4","expectedCode":"LOT-RECALL-AUTHORITY-ABSENT"},
  {"id":"F-LOT-08","target":"Lot","kind":"negative","input":"A lot is recorded with the single state released, and partially-consumed is rejected as inconsistent with it.","expect":"The single-axis encoding is refused; consumption and disposition must be valued independently and concurrently.","violates":"Lot.invariants[9]","closesDefect":"D3","expectedCode":"LOT-STATE-AXIS-COLLAPSE"},
  {"id":"F-LOT-09","target":"Lot","kind":"negative","input":"A lot's expiry date is corrected by updating the existing version in place.","expect":"The in-place update is refused; a new versionId citing supersedesVersionRef is required and the prior version remains readable.","violates":"Lot.invariants[12]","closesDefect":"D6","expectedCode":"LOT-CORRECTION-NOT-APPENDED"},
  {"id":"F-LOT-10","target":"Lot","kind":"negative","input":"A lot version is written with producedAt only and no recordTime.","expect":"The write is refused; record time is required and is never defaulted from effective or production time.","violates":"Lot.invariants[12]","closesDefect":"D6","expectedCode":"LOT-RECORD-TIME-MISSING"},
  {"id":"F-LOT-11","target":"Lot","kind":"negative","input":"A lot status change is asserted with no sourceSystem, assertingAgentRef, method or evidenceDigest.","expect":"The assertion is refused for absent provenance; an unprovenanced status change is not recorded as observed.","violates":"Lot.invariants[1]","closesDefect":"D7","expectedCode":"LOT-PROVENANCE-MISSING"},
  {"id":"F-LOT-12","target":"Lot","kind":"negative","input":"A production-origin lot cites originRef as a free-text routing step identifier.","expect":"The origin is refused; a production origin must cite the identifier-unassigned Transformation Event candidate and must not cite BOM or routing.","violates":"Lot.invariants[6]","closesDefect":"D8","expectedCode":"LOT-ORIGIN-REF-UNTYPED"},
  {"id":"F-LOT-13","target":"Lot","kind":"negative","input":"Serialized item S7 is addressed by its lot membership alone as its item identity.","expect":"The substitution is refused; lot membership is provenance on the WM-OBJ-001 item and never resolves item identity.","violates":"Lot.invariants[3]","closesDefect":"D13","expectedCode":"LOT-MEMBERSHIP-AS-ITEM-IDENTITY"},
  {"id":"F-LOT-14","target":"Lot","kind":"negative","input":"Lot L is read at a carrier hub, and the carrier is recorded as owner of L.","expect":"The ownership assertion is refused; location does not imply custody and custody does not imply title.","violates":"Lot.invariants[7]","closesDefect":"D13","expectedCode":"LOT-CUSTODY-NOT-TITLE"},
  {"id":"F-TRX-01","target":"Transformation Event","kind":"positive","input":"T consumes 400 kg of L and outputs ten serialized items of 36 kg each, a 30 kg co-product lot and 10 kg scrap.","expect":"inputs[0].consumedQuantity 400 kg net; outputs total 360 kg serialized plus 30 kg co-product plus 10 kg scrap; quantityReconciliation.method mass-balance with basis, pinned unit code list and declared tolerance; the reconciliation closes to 400 kg with no unlabelled residual.","violates":null,"closesDefect":"D26"},
  {"id":"F-TRX-02","target":"Transformation Event","kind":"positive","input":"T consumes 400 kg of a 1000 kg lot L.","expect":"inputs[0].consumptionCompleteness partially-consumed with residualAssertedOnLot present; L is neither exhausted nor closed by the event and its residual 600 kg remains traceable.","violates":null,"closesDefect":"D27"},
  {"id":"F-TRX-03","target":"Transformation Event","kind":"positive","input":"T occurs 2026-03-01T08:00:00+01:00 and is recorded 2026-03-04T17:20:00+01:00.","expect":"eventTime and recordTime are both stored with explicit offsets and remain distinct; knowledgeTimeRange.from equals the recordTime; no later status alters eventTime.","violates":null,"closesDefect":"D25"},
  {"id":"F-TRX-04","target":"Transformation Event","kind":"positive","input":"A recorded transformation is corrected, then the correction is itself corrected.","expect":"Three assertions form a bidirectionally resolvable chain: each superseded assertion carries both supersedesRef and supersededByRef, only the newest has status validated, and no assertion is its own successor.","violates":null,"closesDefect":"D30"},
  {"id":"F-TRX-05","target":"Transformation Event","kind":"positive","input":"A transformation recorded in error is voided with reason wrong-work-centre by the production authority.","expect":"status voided with voidRecord carrying voidReason, voidAuthorityRef and recordTime; the prior assertion and its genealogy edges remain readable and are not deleted.","violates":null,"closesDefect":"D29"},
  {"id":"F-TRX-06","target":"Transformation Event","kind":"negative","input":"A transformation is recorded with inputs and outputs but no yield and no scrap.","expect":"The record is refused; yield and scrap are required and may be empty only with a stated reason, never absent.","violates":"TransformationEvent.invariants[5]","closesDefect":"D26","expectedCode":"TRX-YIELD-SCRAP-MISSING"},
  {"id":"F-TRX-07","target":"Transformation Event","kind":"negative","input":"A transformation is recorded with eventTime only.","expect":"The record is refused; recordTime is required and is never defaulted from eventTime.","violates":"TransformationEvent.invariants[6]","closesDefect":"D25","expectedCode":"TRX-RECORD-TIME-MISSING"},
  {"id":"F-TRX-08","target":"Transformation Event","kind":"negative","input":"A transformation is recorded with a performing agent but no authorityRef.","expect":"The record is refused; authority is required on the event and is never inferred from a later status or from the performing agent.","violates":"TransformationEvent.invariants[2]","closesDefect":"D28","expectedCode":"TRX-AUTHORITY-REF-MISSING"},
  {"id":"F-TRX-09","target":"Transformation Event","kind":"negative","input":"An input element states consumedQuantity 400 with no unit and no basis.","expect":"The element is refused; every quantity carries unit, basis and scope with a pinned unit code-list version and no unit is inferred.","violates":"TransformationEvent.invariants[1]","closesDefect":"D27","expectedCode":"TRX-QUANTITY-UNIT-MISSING"},
  {"id":"F-TRX-10","target":"Transformation Event","kind":"negative","input":"status is set to voided with no voidRecord.","expect":"The transition is refused; a void requires reason, authority and record time, and never removes the prior assertion.","violates":"TransformationEvent.invariants[7]","closesDefect":"D29","expectedCode":"TRX-VOID-REASON-MISSING"},
  {"id":"F-TRX-11","target":"Transformation Event","kind":"negative","input":"A WM-ACT-007 maintenance work order is cited as the production authority for T.","expect":"The citation is refused; WM-ACT-007 is maintenance-scoped and restricted, and the production-work-order boundary is unallocated.","violates":"TransformationEvent.invariants[2]","closesDefect":"D31","expectedCode":"TRX-WORK-ORDER-SCOPE-INVALID"},
  {"id":"F-TRX-12","target":"Transformation Event","kind":"negative","input":"A mass-balance-inferred output edge of a blended co-product is promoted to edgeAssertionClass asserted so it reads as an observed fact.","expect":"The promotion is refused; inferred, mass-balance-inferred, stale and incomplete edges retain their class and reason permanently.","violates":"TransformationEvent.invariants[10]","closesDefect":"D35","expectedCode":"TRX-INFERRED-EDGE-ASSERTED"},
  {"id":"F-TRX-13","target":"Transformation Event","kind":"negative","input":"One expected output of T was never recorded; a yield calculation treats that output as 0.","expect":"The calculation is refused; the missing output yields incomplete or indeterminate genealogy and an indeterminate yield, never zero.","violates":"TransformationEvent.invariants[11]","closesDefect":"D35","expectedCode":"TRX-INCOMPLETE-NOT-ZERO"},
  {"id":"F-TRX-14","target":"Transformation Event","kind":"negative","input":"Consumption of a consignment-stock input lot by T is treated as transferring title of that lot to the producer.","expect":"The transfer is refused; consumption changes neither custody nor title and no ownership effect is derived from a transformation.","violates":"TransformationEvent.invariants[8]","closesDefect":"D35","expectedCode":"TRX-CONSUMPTION-NOT-TITLE-TRANSFER"},
  {"id":"F-TRX-15","target":"Transformation Event","kind":"negative","input":"An exposure traversal over T's output edges is emitted as a recall decision for S1..S10.","expect":"The emission is refused; traversal yields proven and reason-coded potential sets only, and recall, alert and enforcement authority is external to this contour.","violates":"TransformationEvent.invariants[12]","closesDefect":"D35","expectedCode":"TRX-EXPOSURE-NOT-RECALL-AUTHORITY"},
  {"id":"F-TRX-16","target":"Transformation Event","kind":"negative","input":"T is recorded with an evidenceDigest but no sourceSystem, assertingAgentRef or method.","expect":"The record is refused; provenance is required and a digest alone does not establish who asserted the event or how.","violates":"TransformationEvent.invariants[3]","closesDefect":"D32","expectedCode":"TRX-PROVENANCE-MISSING"},
  {"id":"F-TRX-17","target":"Transformation Event","kind":"negative","input":"An assertion is set to status superseded with no supersededByRef.","expect":"The transition is refused; supersession requires a resolvable successor reference in both directions.","violates":"TransformationEvent.invariants[7]","closesDefect":"D30","expectedCode":"TRX-SUPERSESSION-LINK-MISSING"},
  {"id":"F-PRF-01","target":"Enterprise Inventory and Genealogy Binding","kind":"positive","input":"A stock position for lot L at site W is taken from an authoritative source system with no movement ledger available.","expect":"derivationMode authoritative-source-snapshot is declared on the position; no completenessPerimeterRef is required; the position authorizes no posting and no adjustment.","violates":null,"closesDefect":"D17"},
  {"id":"F-PRF-02","target":"Enterprise Inventory and Genealogy Binding","kind":"positive","input":"A balance for lot L is projected over WM-FLW-012 postings and their corrections within a declared closed perimeter.","expect":"derivationMode complete-ledger-projection with completenessPerimeterRef, ledgerCutoffRecordTime and correctionsIncluded true; the projection is labelled derived and authorizes no posting.","violates":null,"closesDefect":"D17"},
  {"id":"F-PRF-03","target":"Enterprise Inventory and Genealogy Binding","kind":"positive","input":"Shipment SH carrying S1..S6 is bound for a sale under one commercial agreement moved by one carrier.","expect":"WM-FLW-011 is reused with kind trade-shipment explicitly declared, and the transport-consignment view is a separate declared kind rather than an implied synonym.","violates":null,"closesDefect":"D21"},
  {"id":"F-PRF-04","target":"Enterprise Inventory and Genealogy Binding","kind":"positive","input":"A read at a hub, a stock transition, a lineage link and a dispatch milestone arrive as four facts about one consignment.","expect":"They bind to WM-FLW-004, WM-FLW-012, WM-FLW-013 and WM-ECO-024 respectively; no generic logistics-event identity is created and none of the four is derived from another.","violates":null,"closesDefect":"D21"},
  {"id":"F-PRF-05","target":"Enterprise Inventory and Genealogy Binding","kind":"positive","input":"Custody of SH transfers to the carrier; the customer has not accepted.","expect":"Custody transfer is recorded on WM-FLW-004 handover with a time-bounded WM-FLW-013 custody interval; title is unchanged and no WM-ECO-024 receipt, inspection or acceptance assertion exists.","violates":null,"closesDefect":"D21"},
  {"id":"F-PRF-06","target":"Enterprise Inventory and Genealogy Binding","kind":"positive","input":"A posted inventory movement of 100 units is found to have been 90.","expect":"An appended WM-FLW-012 compensating posting of -10 cites priorAssertionRef, correctionReason and recordTime; the original posting remains readable and the prior balance state is preserved.","violates":null,"closesDefect":"D18"},
  {"id":"F-PRF-07","target":"Enterprise Inventory and Genealogy Binding","kind":"positive","input":"A dispatch effective 2026-03-10T09:00:00+01:00 is observed 2026-03-10T09:05:00+01:00, posted 2026-03-11T02:00:00+01:00 and ingested 2026-03-12T06:30:00+01:00.","expect":"All four times are separately carried in RFC 3339 with seconds and explicit offsets across the binding; no join substitutes one for another and the posting time does not become the effective time.","violates":null,"closesDefect":"D19"},
  {"id":"F-PRF-08","target":"Enterprise Inventory and Genealogy Binding","kind":"negative","input":"A stock position is bound with no derivationMode.","expect":"The binding is refused; snapshot and projection are distinct constructs and neither is a default.","violates":"profile.constraints[1]","closesDefect":"D17","expectedCode":"PRF-DERIVATION-MODE-UNDECLARED"},
  {"id":"F-PRF-09","target":"Enterprise Inventory and Genealogy Binding","kind":"negative","input":"One derived balance sums a source snapshot for site W with a partial posting ledger for site X, with no perimeter declared.","expect":"The derivation is refused for mixed modes and an absent completeness perimeter; the partial ledger cannot be read as complete.","violates":"profile.constraints[1]","closesDefect":"D17","expectedCode":"PRF-COMPLETENESS-PERIMETER-ABSENT"},
  {"id":"F-PRF-10","target":"Enterprise Inventory and Genealogy Binding","kind":"negative","input":"WM-FLW-011 is reused for SH with no kind declared.","expect":"The reuse is refused; trade-shipment, transport-consignment and combined view are not interchangeable and no kind is defaulted.","violates":"profile.constraints[2]","closesDefect":"D21","expectedCode":"PRF-SHIPMENT-KIND-UNDECLARED"},
  {"id":"F-PRF-11","target":"Enterprise Inventory and Genealogy Binding","kind":"negative","input":"A single generic LogisticsEvent root is proposed to carry reads, stock transitions, lineage links and milestones.","expect":"The root is refused; it would duplicate WM-FLW-004, WM-FLW-012, WM-FLW-013 and WM-ECO-024.","violates":"profile.constraints[3]","closesDefect":"D21","expectedCode":"PRF-LOGISTICS-EVENT-ROOT-FORBIDDEN"},
  {"id":"F-PRF-12","target":"Enterprise Inventory and Genealogy Binding","kind":"negative","input":"The profile is extended to hold its own lot status field as the quantity and status of record.","expect":"The extension is refused; the profile owns binding constraints only and no business-object identity, lifecycle or quantity of record.","violates":"profile.mustNotOwn","closesDefect":"D14","expectedCode":"PRF-PROFILE-OWNS-MASTER"},
  {"id":"F-PRF-13","target":"Enterprise Inventory and Genealogy Binding","kind":"negative","input":"A runtime identifier is minted for the profile so bindings can be addressed.","expect":"The allocation is refused; newRuntimeId is false and no catalogue, registry or runtime identifier is created here.","violates":"profile.holds[1]","closesDefect":"D16","expectedCode":"PRF-RUNTIME-ID-FORBIDDEN"},
  {"id":"F-PRF-14","target":"Enterprise Inventory and Genealogy Binding","kind":"negative","input":"A physical count differing from the derived balance is applied directly as a stock adjustment.","expect":"The adjustment is refused; a count is an observation and authorizes no posting, and any correction is an appended explicit event by the posting authority.","violates":"profile.constraints[6]","closesDefect":"D21","expectedCode":"PRF-COUNT-NOT-ADJUSTMENT-AUTHORITY"},
  {"id":"F-PRF-15","target":"Enterprise Inventory and Genealogy Binding","kind":"negative","input":"All six units of SH are reported delivered because the dispatch milestone exists.","expect":"The inference is refused; dispatch does not establish delivery and S6 remains dispatched only.","violates":"profile.constraints[4]","closesDefect":"D21","expectedCode":"PRF-DISPATCH-NOT-DELIVERY"},
  {"id":"F-PRF-16","target":"Enterprise Inventory and Genealogy Binding","kind":"negative","input":"The five received units are reported accepted, one of them carrying a damage exception.","expect":"The inference is refused; receipt does not establish inspection and inspection does not establish acceptance or discharge, and inspection determination authority is an external gap.","violates":"profile.constraints[4]","closesDefect":"D21","expectedCode":"PRF-DELIVERY-NOT-ACCEPTANCE"},
  {"id":"F-PRF-17","target":"Enterprise Inventory and Genealogy Binding","kind":"negative","input":"A wrong posted quantity is fixed by editing the stored posting row.","expect":"The edit is refused; corrections append successors, prior states remain readable and identifiers are never reused.","violates":"profile.constraints[6]","closesDefect":"D18","expectedCode":"PRF-CORRECTION-NOT-APPENDED"},
  {"id":"F-PRF-18","target":"Enterprise Inventory and Genealogy Binding","kind":"negative","input":"A placeholder model identifier is written for the Lot or Transformation Event binding so the profile can resolve.","expect":"The write is refused; both candidates stay modelId null, registryId null, allocationState unassigned, and identifier invention is forbidden.","violates":"profile.identifierInventionForbidden","closesDefect":"D15","expectedCode":"PRF-UNASSIGNED-CANDIDATE-ID-INVENTED"},
  {"id":"F-PRF-19","target":"Enterprise Inventory and Genealogy Binding","kind":"negative","input":"The profile is described as installable and publication-ready because all six bases are named.","expect":"The claim is refused; all bases are reviewable drafts with canonicalPublishable false and outstanding absence-of-external-review holds.","violates":"profile.holds[3]","closesDefect":"D16","expectedCode":"PRF-PUBLICATION-CLAIM-FORBIDDEN"},
  {"id":"F-PRF-20","target":"Enterprise Inventory and Genealogy Binding","kind":"negative","input":"Lot L is affected, so every unit of the shared SKU is scoped into the recall and same-SKU units of other lots are additionally declared unaffected.","expect":"Both moves are refused; SKU-level scope is never derived from an affected lot, same-SKU and BOM-only matches are notEvidenced, no unaffected declaration is made absent a closed perimeter, and exposure analysis is not recall authority.","violates":"profile.constraints[10]","closesDefect":"D20","expectedCode":"PRF-SKU-RECALL-FORBIDDEN"}
]
```

---

## 4. Freeze decision

**Semantic boundary: FROZEN.** The five-candidate adjudication, the Logistics Event split across four masters, the thin no-runtime-identifier profile, and the twelve-plus-fifteen invariant families are closed. No artifact contradicts the reconciled decision, so the business boundary was not re-studied and must not be re-opened. No further provider study and no rerun.

**Artifact set: FREEZE WITHHELD.** The 35 defects are mechanical, and every one has exact remediation text above. Re-entry is restricted to mechanical verification against this audit — applying the quoted remediation text, adding the 51 fixtures verbatim, and re-running the amended validation policies. It is not a new adjudication and may not alter boundary, mastership or invariant semantics.

**Counts.** 35 material defects. 51 additional fixtures. 12 prior fixtures preserved — all six Lot cases and all six Transformation cases, with `partial-shipment-after-production` relocated to the profile suite (D35), `expectedCode` added to all six negatives (D10, D33), and four expects made deterministic (D12, D34). Post-remediation suite: **63 fixtures** — Lot 20, Transformation Event 22, Binding Profile 21. Every negative carries `expectedCode`; `violates` is null exactly on positives; 26 of the 35 defects are fixture-backed and the remaining 9 (D9, D10, D11, D12, D22, D23, D24, D33, D34) close on remediation text alone.

**Standing holds, unchanged by this audit.** No identifier is allocated or guessed for Lot, Transformation Event or the profile. Production work order, handling unit (WM-OBJ-021), as-built assembly (WM-OBJ-012), occurrence/event (WM-ACT-015) and inspection-determination/conformity authority remain unallocated or absent. Registry parent/containment signals conflict with specs on WM-OBJ-020→WM-OBJ-001, WM-FLW-012→WM-OBJ-020, WM-FLW-011/013→WM-FLW-004 and WM-ECO-019→WM-ECO-024 (CONTAINS versus COMPOSE); registry `entry_kind` disagrees with spec `entryKind` on four models — reconcile, never overwrite. EPCIS 2.0 versus 2.0.1 and UBL 2.3 versus 2.4 pins diverge. WM-ACT-007 is maintenance-scoped with unresolved K11 duplication. WM-FLW-011/012/013 bundle descriptions carry "Route / Itinerary" template leakage. External crosswalks are absent. **No conformance, installability or publication-readiness claim is made.**
