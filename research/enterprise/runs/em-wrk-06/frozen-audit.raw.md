# Frozen Semantic Audit — EM-WRK-06

**Auditor role:** sole independent frozen auditor. No tools used, no browsing, no standards claims, no identifiers invented, no registry mutation. Single pass.

---

## 1. Verdict

**REVISE.**

The fixed identity decision is sound and is confirmed unchanged (§5). The reconciliation of the two inputs is not. Sixteen material defects are present in the artifacts themselves — not in the pending registry allocations. Four of them are safety-bearing: the scenario can reach a negative conclusion that can never be invalidated (D10), both acceptance scenarios propagate in a direction no artifact licenses (D2), heterogeneous-type paths traverse under no declared composition rule (D4), and the required `EM-WRK-06` criticality profile does not exist as an artifact at all (D13).

---

## 2. Material defects

### D1 — Dependency types have no identity; per-type lifecycle is unexpressible

**Evidence.** Registry objects declare only two identified things: `"DependencyTypeRegistry":{"identity":["dependencyTypeRegistryId"]}` and `"RegistryRelease":{"identity":["dependencyTypeRegistryId","releaseVersion"],"required":["typeDefinitions",…]}`. A type is an unidentified element inside the `typeDefinitions` payload of a release.

**Contradiction.** The artifacts repeatedly operate on *type* identity and *type* lifecycle: invariant `"Every dependency edge pins one exact type-registry release and canonical type."`; invariant `"Type deprecation never deletes historical edges."`; fixture `deprecated-type` input `"A type is superseded by a refined successor."` expect `"Historical edges retain the prior type version."` None of these are expressible. There is no `dependencyTypeId` to carry stable identity across releases, no per-type `status`, no per-type `successorRef`, and no `"the prior type version"` to retain — only a release version. The declared `independentLifecycle` of eight states (`draft`…`retired`) is bound to the registry object, while `RegistryRelease.status` has no declared enumeration at all and the distinction between `published` and `effective` has no transition rule.

**Impact.** "A type is superseded by a refined successor" degenerates to "the whole registry was re-released", which defeats the stated `versionIdentity` and makes `zero-edge-type`, `deprecated-type` and the pinning invariant mutually inconsistent.

### D2 — Inverse derivation has no permission field, and every acceptance traversal runs counter-canonically

**Evidence.** Grok: `"Canonical direction is asserted; inverse is derived only if the type permits."` and `"Inverse is derived, never a second master edge, and only where the type marks the relation invertible or symmetric."` Local evidence states the rule unconditionally: `"Inverses are derived and never stored as separate facts."` / invariant 2 `"Inverse edges are derived, never duplicated."` The registry `owns` list and `RegistryRelease.typeDefinitions` carry no invertibility, symmetry or inverse-pairing attribute.

**Defect A (unenforceable).** `"Inverse edges are derived and never stored as duplicate facts."` and fixture `duplicate-inverse` (`"Both canonical and inverse edges are stored as independent facts." → "The duplication is rejected."`) have no detection basis: without a declared inverse pairing between type *t* and type *t′*, two edges in opposite directions carrying different type terms are indistinguishable from a legitimate pair of distinct assertions.

**Defect B (safety-bearing, unresolved).** Canonical direction is `dependent to prerequisite`. In both acceptance runs, impact flows *prerequisite → dependent*: local evidence `"an API change traverses interface and package dependencies"` (change at the prerequisite reaches dependents); grok `"A (API contract) provides B (service)"`, `"affected set is {B}"`; and `"B uses C (resource pool)"`, delay at C, `"affected set is {B} under lag"`. So **every** impact traversal in the acceptance set is counter-canonical. Grok guards only one hop of this — `"A is not inverse-affected unless inverse derivation is licensed"` — and local evidence only says licences `"state traversal direction relative to canonical edge direction"`. Nothing anywhere states that a reverse-direction licence requires the pinned type to permit inverse derivation. A licence can therefore authorise reverse traversal over a type the registry marks non-invertible, which is exactly the duplication the invariant forbids, performed at analysis time instead of storage time.

### D3 — Arity is contradicted, and composite prerequisite groups have no owner

**Evidence.** Grok: `"Arity is binary; multi-party dependence is a set of binary edges. Arity violations are invalid, not low-confidence."` Local evidence: types declare `"arity"` and `"Composite prerequisite groups and alternatives remain explicit."` Registry `owns` `"arity and cardinality rules"`; invariant `"Endpoint classes, arity, cardinality and phase constraints are explicit."`

**Defect.** The reconciliation never decides. If arity is binary by construction, the registry must not carry a declarable arity axis; if arity is declarable, grok's binary invariant is dropped and the "invalid, not low-confidence" severity rule is lost. Separately, an AND/OR composite prerequisite group ("B needs C *and* (D *or* E)") is neither an edge, nor a type, nor a scenario, nor an endpoint. It has no object, no field, and no identity in any artifact, yet it is asserted to `"remain explicit"`. No fixture touches arity or groups.

### D4 — Cross-type path composition is undefined, yet the acceptance paths are heterogeneous

**Evidence.** Local evidence: `"Transitivity is declared per type with a recorded basis"`; registry invariants `"Transitivity requires a declared basis and is never inferred from topology."` and `"Cycles are allowed only by type-specific rules."` Grok: `"the type must mark composition eligible, and every participating edge must carry a licence."` Acceptance run: `"an API change traverses interface and package dependencies through build and runtime phases"` — at least two distinct types in one path.

**Defect.** Transitivity, cycle permission and stop rules are all declared *per type*, but no artifact defines the composition of a path whose hops carry different types. Which type's transitivity basis governs the hop from an interface edge to a package edge? Which type's cycle rule governs a cycle spanning two types that disagree? The only acceptance evidence offered for the whole proposal is a multi-type path executing under rules that are single-type by construction. Grok's per-edge-licence requirement is also absent from both candidate invariant sets, which carry only `"Traversal requires an explicit propagation licence."` (scenario-level, not per-edge).

### D5 — Co-location and correlation are carried as dependency edges

**Evidence.** Local evidence: `"Co-location and correlation do not propagate by default."`; acceptance text and ImpactScenario fixture `resource-delay`: `"A resource delay traverses runtime capacity dependencies and stops at co-location edges."` Registry `owns` `"dependency-type definitions"` and invariant `"Canonical direction is dependent to prerequisite unless the pinned type explicitly defines otherwise."`

**Defect.** Co-location is symmetric and non-dependent; correlation is statistical. Neither has a dependent and a prerequisite. Modelling them as dependency edges so that traversal can "stop at" them forces a canonical direction onto a relation that has none, and smuggles a non-dependency relation class into a registry whose boundary excludes it. The registry has no relation class discriminator to separate `dependency` from `adjacency`/`correlation`, so the stop behaviour is implemented by convention rather than by rule.

### D6 — The propagation profile is a required pin with no master, no identity and no versioning

**Evidence.** ImpactScenario `required` includes `"propagationProfileRef"`; invariant `"Every scenario pins graph snapshot, type registry, propagation profile, horizon and code lists."`; identity test names `"propagation profile"` as a successor-forcing axis. Registry `owns` only `"guard, propagation licence and stop-rule templates"` — templates, not releases. ImpactScenario `excludes` does not claim it; no third object exists.

**Defect.** The one object on which the entire acceptance result depends — `"The affected sets differ because type, phase and propagation licence differ, not merely topology."` — is unmastered, unversioned and unlifecycled. `"Propagation licences are deny-by-default"` and `"Traversal requires an explicit propagation licence."` are unenforceable because there is nothing with a version to pin, nothing that can be immutable, and no rule stating that a profile change supersedes rather than mutates. Grok's blocker `"a licence too thin to separate the two events"` cannot be evaluated against an object that does not exist in any artifact.

### D7 — Graph snapshot mastership is ambiguous and no digest is reproducible

**Evidence.** ImpactScenario `owns` `"immutable graph snapshot and digest"` while `excludes` `"dependency type, edge or endpoint identity"`; `required` carries `"graphSnapshotRef"` (a reference, implying external mastership). `RegistryRelease.required` carries `"contentDigest"`.

**Defect A.** The scenario simultaneously *owns* the snapshot and *references* it. If the analysis owns it, two scenarios executed over the identical graph state mint two incomparable snapshots, and the invariant `"No analysis writes to endpoint or dependency masters."` is satisfied only by the analysis writing a new master of its own. If it references it, the snapshot's owner is unnamed.

**Defect B.** Neither `contentDigest` nor the scenario digest names a digest algorithm or a canonical serialisation. `"immutable graph snapshot and digest"` and `"Registry releases are immutable"` are therefore unverifiable: two parties cannot agree on whether a digest matches, and `stale-graph` detection (`"A covering graph snapshot changes after release."`) has no defined comparison.

### D8 — Unknown-edge traversal is contradicted, and the epistemic vocabularies do not reconcile

**Evidence.** Grok invariant 8: `"Unknown and absent are distinct; both lower completeness and block traversal."`; invariant 9: `"Completeness falls if an unknown or incomplete edge lies on a candidate path."`; invariant 12: `"Propagation stops at licence, phase, depth, or incomplete edge."`; blocker `"unknown edges still traversed"`. Local evidence acceptance: `"One inferred edge and one unenumerated region make completeness incomplete, so neither analysis may claim no further impact."` — the inferred edge was *traversed*, and the only consequence was a completeness reduction.

**Defect A.** The two inputs disagree on whether an unknown/incomplete edge blocks traversal or merely degrades completeness. The reconciliation adopts neither. Grok's boundary requires the licence to carry `"unknown-edge policy"`; no artifact has an `unknownEdgePolicy` field, in the scenario, the profile templates, or anywhere else.

**Defect B.** Local evidence enumerates five states: `"Asserted-present, asserted-absent, unknown, not-assessed and unresolved are distinct states."` Grok enumerates four, differently cut: `"The edge holds known, unknown, absent, or incomplete, plus confidence."` `not-assessed`/`unresolved` versus `incomplete` are never mapped. Worse, local invariant 8 protects only three of its own five: `"Unknown, not-assessed and asserted-absent never collapse."` — `unresolved` is declared distinct and then left unprotected and undefined.

### D9 — "Released is immutable" is contradicted by mutable status and successor fields

**Evidence.** ImpactScenario invariant `"Released impact scenarios are immutable and corrections create successors."` Object `required` includes `"status"`; `optional` includes `"successorRef"`; `lifecycle` is `["draft","executed","reviewed","released","stale","superseded","withdrawn"]`. Fixture `stale-graph` expect: `"The scenario becomes stale without rewriting its original output."`

**Defect A.** Every post-release lifecycle state (`stale`, `superseded`, `withdrawn`) is a write to the `status` field of an object declared immutable, and `successorRef` is a write to the frozen predecessor. The fixture's `"without rewriting its original output"` concedes the point by narrowing immutability to the *output* while leaving the record mutable — which is not what the invariant says.

**Defect B (same shape, registry side).** `RegistryRelease` is immutable and carries only `"supersedesRelease"` — a backward pointer on the successor. Forward supersession discovery is structurally impossible: a consumer holding release *n* cannot learn that *n+1* exists without scanning, and the pointer cannot be added to *n* because *n* is immutable. The registry-level `successorRef` does not help, as it is scoped to the registry object, not the release.

### D10 — Staleness safe-harbour hole: the negative-conclusion guard is void exactly where it is needed

**Evidence.** ImpactScenario `optional` includes `"completenessRef"`. Invariants: `"Negative conclusions require covering completeness for subject, kind and phase."` and `"A stale scenario cannot support a negative conclusion."` and `"Changes to graph, registry, profile or completeness can stale prior output."` Local evidence: `"Impact outputs become stale when the graph snapshot, type registry, propagation profile or covering completeness declaration changes."`

**Defect A (safety-bearing).** Because `completenessRef` is optional, a scenario that pinned no completeness declaration can never be staled by a completeness change — there is nothing to compare. Such a scenario stays `released` indefinitely while the completeness basis underneath it collapses. The guard `"A stale scenario cannot support a negative conclusion."` therefore protects only scenarios that already did the right thing, and is silent on the ones that did not.

**Defect B (unenforceable).** There is no `conclusionPolarity` / `resultPolarity` field anywhere in `ImpactScenario`. "Negative conclusion" is not a representable property of the object, so both invariants that turn on it cannot be evaluated by any checker.

**Defect C (undefined predicate).** `"covering"` is never defined. No artifact states what makes a completeness declaration cover a given exposure set: the subject set, kind, phase, and validity interval over which coverage is tested are not modelled, and no in-force test exists despite local evidence requiring `"an in-force completeness statement"`.

**Note (non-material, category error).** `excludes` lists `"automatic negative conclusion from missing edges"` — a forbidden behaviour placed in a list whose other entries are things owned by other models. Prohibitions belong in invariants, not in a boundary exclusion list.

### D11 — Invariants name outputs that have no fields, and status-conditional obligations are expressed as plain optionality

**Evidence.** Invariant `"Every scenario pins graph snapshot, type registry, propagation profile, horizon and code lists."` — `ImpactScenario` has no `codeListRefs` field in `required` or `optional`. Invariant `"Suppressed or omitted edges remain visible with reason codes."` — there is no `suppressedEdges` field and no `stopReasons` field; `optional` carries only `"cycleWitnesses"` and `"unexpandedFrontier"`. Local evidence: `"Traversal over cyclic components is bounded and returns cycle witnesses, stop reasons and the unexpanded frontier."` — `stopReasons` is named in prose and absent from the object.

**Defect.** Three named invariant obligations have no carrier field. Separately, `exposureSet`, `cycleWitnesses` and `unexpandedFrontier` are unconditionally `optional`, so an `executed` or `released` scenario with no outputs at all is a valid instance. Obligations that attach from `executed` onward are being encoded as "never required".

### D12 — Fixtures assert "affected set" where the boundary permits only candidate exposure

**Evidence.** ImpactScenario `owns` `"candidate exposure output and frontier"`; `excludes` `"criticality assessment or affectedness determination"`; invariant `"Candidate exposure never becomes affected or not affected without assessor determination."` Fixture `resource-delay` expect: `"The affected set differs from the API scenario because type and licence differ."` Local evidence acceptance: `"The affected sets differ because type, phase and propagation licence differ"`. Grok: `"affected set is {B}"`.

**Defect.** The sole acceptance fixture for the central claim of the proposal asserts an output the model explicitly cannot produce. Either the fixture passes by producing an affectedness determination — violating the boundary and the invariant — or it fails on its own wording. Grok's own worked scenario repeats the error three times.

### D13 — The `EM-WRK-06` criticality profile does not exist as an artifact

**Evidence.** The fixed decision states `"Criticality Assessment profiles WM-ACT-034"` and `EM-WRK-06-profile` is an in-scope audit target. The submitted artifact set contains two allocation candidates, two fixture files and two validation policies — **none for the profile**. No profile specification, no field map, no fixtures, no validation policy.

**Defect.** Everything asserted about criticality is therefore unverifiable. Local evidence: `"The WM-ACT-034 profile binds edge, dependent purpose, scheme version, authority and validity interval."` — no artifact states which base fields carry these five bindings or which are extension points. Grok: `"Scheme parameters (bands, phase window, licence gate) sit on the WM-ACT-034 instance, pinned to snapshot and edge set."` and the explicit blocker `"criticality unable to pin a snapshot under the profile"`. That blocker cannot be cleared or even tested without a profile artifact declaring the snapshot-pin carrier. This is an artifact gap, not a base-publication hold: the absence of a *profile specification* is independent of whether WM-ACT-034 is published.

### D14 — WM-ACT-034 carries two distinct assessment semantics with no discriminator

**Evidence.** ImpactScenario references `{"target":"WM-ACT-034","purpose":"Assessment promoting exposure to affectedness"}`. Registry references `{"target":"WM-ACT-034","purpose":"Criticality assessment"}`. Local evidence profiles WM-ACT-034 for criticality only.

**Defect.** Affectedness determination (a per-scenario, per-node, binary promotion pinned to one snapshot) and criticality assessment (a purpose-relative, scheme-qualified, interval-valid judgement about an edge) are collapsed onto one base with no assessment-kind discriminator declared in any artifact. Their identity, cardinality and validity semantics differ. With no discriminator, affectedness promotion is unmastered: the invariant `"Candidate exposure never becomes affected or not affected without assessor determination."` points at an object that cannot say which kind of determination it is.

### D15 — Lag time basis and release validity have no fields and no time-axis declaration

**Evidence.** Registry invariant `"Lag semantics pin calendar, zone and timezone database release."`; local evidence `"Lag pins duration semantics, calendar, IANA zone and timezone database release."` No `calendarRef`, `ianaZone` or `tzdbRelease` field exists in `DependencyTypeRegistry`, `RegistryRelease`, or anywhere in the candidate set. `RegistryRelease` carries `"validFrom"` / `"validTo"` and `DependencyTypeRegistry` carries `"retiredAt"`, none with a declared time axis or zone. The invariant `"Event, observation and ingestion times remain distinct."` appears only in `ImpactScenario` and is absent from the registry.

**Defect.** The registry's own lag invariant is unenforceable against its own object definitions, and registry validity timestamps are zone-ambiguous while the registry claims to be the authority on zone pinning. Grok's `"Lag is a temporal annotation and does not grant licence."` has no field to annotate.

### D16 — Registry reference list leaks, and re-asserts impact ownership inside WM-XCT-037

**Evidence.** Registry `references`: `{"target":"WM-XCT-037","purpose":"Dependency edge and impact semantics"}`, plus `WM-ACT-034` (criticality), `WM-KNW-008` (citation), `WM-MAT-008` (observation), `WM-KNW-015` (risk record). Registry `excludes` contains all of `"evidence payload or observation"`, `"impact scenario or traversal result"`, `"criticality assessment or causal claim"`, `"risk determination or authorization"`.

**Defect A.** The purpose string `"Dependency edge and impact semantics"` locates impact semantics in WM-XCT-037 — directly contradicting the fixed decision and the stated disposition `"Move computed affected-set projection to Impact Scenario."`, and matching grok's first blocker verbatim: `"residual Impact or type-catalog ownership in WM-XCT-037"`. The residue survives in the one artifact that is supposed to have removed it.

**Defect B.** A dependency-*type vocabulary* has no legitimate dependency on a risk record, an observation, or a citation; it defines terms. Four of its five references are to models it explicitly excludes and never consumes. The plausible cause is `validation-policy.json`'s `"minimumReferences":3`, which rewards reference count rather than justified coupling — a policy that converts a boundary statement into a quota.

---

## 3. Required bounded fixes

Each fix is scoped to the three audit targets. None allocates an identifier; all new objects are internal to the already-unassigned candidates (see §5).

**F1 (D1).** Add object `DependencyType` with `identity:["dependencyTypeId"]`, `required:["name","status","introducedInRelease","typeVersion"]`, `optional:["successorTypeRef","deprecatedInRelease"]`, and its own lifecycle enum. Make `RegistryRelease.typeDefinitions` a set of `{dependencyTypeRef, typeVersion}` bindings rather than inline definitions. Declare explicit status enumerations for all three levels and the `published` → `effective` transition rule. Restate the pinning invariant as: an edge pins `{dependencyTypeId, typeVersion, releaseVersion}`.

**F2 (D2).** Add to `DependencyType`: `directionality` ∈ `{directed, symmetric}` and `inverseOfTypeRef` (required when an inverse term exists). Add registry invariant: *derivation of an inverse requires `symmetric` or a declared `inverseOfTypeRef`; a stored edge whose type and endpoints match a declared inverse pairing is a duplicate and is rejected*. Add scenario invariant: *a propagation licence whose traversal direction is counter-canonical is valid only where every traversed edge's pinned type permits inverse derivation; otherwise the run is rejected.*

**F3 (D3).** Decide binary-only and record it: set `arity` to a fixed binary constraint at the registry level and delete the declarable-arity axis, **or** keep the axis and drop grok's binary invariant — not both. Under binary-only, add object `PrerequisiteGroup` with `identity`, `groupSemantics` ∈ `{all, any, k-of-n}`, `k`, and member edge references, internal to the registry candidate. Add invariant: *arity violations are invalid instances, never low-confidence instances.*

**F4 (D4).** Add `compositionEligibility` to `DependencyType` and a registry-level `TypeCompositionRule` object keyed by `{antecedentTypeRef, consequentTypeRef}` declaring whether composition is licensed and under what basis. Add invariant: *a multi-hop path whose hops carry different types requires a matching composition rule for each adjacent pair; absent a rule, the path does not compose.* Add: *cycle permission for a heterogeneous cycle is the conjunction of every participating type's cycle rule.* Add per-edge licence requirement to the scenario invariant set.

**F5 (D5).** Add `relationClass` ∈ `{dependency, adjacency, correlation}` to `DependencyType`. Constrain `canonicalDirection` to `relationClass = dependency`. Add invariant: *non-dependency relation classes are never traversed and never propagate; they may only be recorded as stop conditions.*

**F6 (D6).** Place `PropagationProfile` under the Dependency Type Registry candidate as an identified, released, immutable object (`identity:["propagationProfileId"]`, `required:["profileVersion","typeFilter","phaseWindow","traversalDirection","depthLimit","lagBound","unknownEdgePolicy","stopConditions","evidenceThreshold","status","contentDigest"]`), and change the registry `owns` entry from `"templates"` to profile releases. Add invariant: *a profile change produces a new immutable profile version; `propagationProfileRef` must pin a released version.*

**F7 (D7).** Resolve mastership: the graph snapshot is minted by the dependency-edge side (narrowed WM-XCT-037) and **referenced** by `ImpactScenario`; remove `"immutable graph snapshot and digest"` from the scenario `owns` list, retaining `graphSnapshotRef` and a read-only `snapshotDigest` copy for verification. Add `digestAlgorithm` and `canonicalizationMethod` as required on `RegistryRelease`, `PropagationProfile` and the snapshot reference. Add invariant: *two scenarios over the same graph state pin the same snapshot reference and digest.*

**F8 (D8).** Adopt one rule explicitly and record the rejected alternative: **unknown, not-assessed, unresolved and incomplete edges block licensed traversal and are reported on the frontier with a reason code; asserted-absent terminates the branch.** Make `unknownEdgePolicy` required on `PropagationProfile`. Publish a normative mapping table between the five-state local vocabulary and grok's four-state vocabulary, with `unresolved` defined. Extend the non-collapse invariant to all five states.

**F9 (D9).** Remove `successorRef` and post-release `status` from the frozen objects. Add an external `ScenarioSupersession` link record (`{predecessorRef, successorRef, reason, decidedAt}`) and a `ScenarioStatusEvaluation` overlay record carrying `{scenarioRef, evaluatedStatus, basis, evaluatedAt}`. Restate: *the released scenario record is byte-immutable; status and supersession are derived overlays.* Mirror for `RegistryRelease`: add a `ReleaseSupersession` link record; remove reliance on mutating release *n*.

**F10 (D10).** Make `completenessRef` **required whenever `conclusionPolarity = negative`**, and add `conclusionPolarity` ∈ `{positive, negative, indeterminate}` as a required field. Add `completenessCoverage` declaring the covered subject set, dependency kinds, phases and validity interval, plus an explicit coverage predicate. Add invariant: *a scenario with no `completenessRef` is permanently `indeterminate` and may never carry `conclusionPolarity = negative`.* Move `"automatic negative conclusion from missing edges"` out of `excludes` into the invariant list.

**F11 (D11).** Add `codeListRefs` to `required`; add `stopReasons` and `suppressedEdges` (each with reason code) to the output fields. Replace flat optionality with status-conditional requirement: `exposureSet`, `stopReasons`, `cycleWitnesses` and `unexpandedFrontier` are required from `executed` onward.

**F12 (D12).** Rewrite fixture `resource-delay` expect to `"The candidate exposure set differs from the API scenario because type, phase and propagation licence differ."` Apply the same correction to the local-evidence acceptance paragraph and to the required-invariant wording wherever "affected set" is used for a scenario output.

**F13 (D13).** Produce the missing `EM-WRK-06-profile` artifact set (profile specification, fixtures, validation policy). The specification must enumerate, field by field, which WM-ACT-034 element carries: edge reference set, dependent purpose, scheme identifier and version, assessing authority, validity interval, **graph snapshot pin**, and licence gate; and must mark each as base field, base extension point, or unsatisfiable. If the snapshot pin is unsatisfiable, record grok's blocker as an open blocker against the base — not as grounds for a new root.

**F14 (D14).** Add `assessmentKind` ∈ `{affectedness-determination, criticality-assessment}` to the profile, with distinct identity, cardinality and validity rules per kind. Add invariant: *exposure promotion requires `assessmentKind = affectedness-determination` pinned to the same snapshot as the scenario; criticality assessments never promote exposure.*

**F15 (D15).** Add `lagCalendarRef`, `ianaZone` and `tzdbRelease` as required wherever a type declares lag. Add `timeAxis` qualification to `validFrom`, `validTo` and `retiredAt`. Add the event/observation/ingestion distinctness invariant to the registry candidate.

**F16 (D16).** Change the WM-XCT-037 reference purpose to `"Dependency edge semantics"` (impact removed). Reduce the registry reference list to justified couplings only. Amend both `validation-policy.json` files: replace `"minimumReferences":3` with a justification requirement (`requiresReferenceJustification:true`) and add `requiresInvariantFixtureCoverage:true`.

---

## 4. Additional fixtures

```json
[
  {"target":"DependencyTypeRegistry","id":"type-stable-identity-across-releases","kind":"positive","input":"A published dependency type is refined and re-released in a later registry release.","expect":"The type retains its dependencyTypeId, gains a new typeVersion, and edges pinned to the prior typeVersion continue to resolve to the prior semantics."},
  {"target":"DependencyTypeRegistry","id":"type-defined-only-inside-release-blob","kind":"negative","input":"A dependency type is declared solely as an element of RegistryRelease.typeDefinitions with no dependencyTypeId of its own.","expect":"The declaration is rejected because per-type supersession and deprecation cannot be expressed.","expectedCode":"ERR_TYPE_IDENTITY_MISSING"},
  {"target":"DependencyTypeRegistry","id":"undeclared-release-status-enum","kind":"negative","input":"A RegistryRelease carries status 'effective' with no declared status enumeration and no published-to-effective transition rule.","expect":"The release is rejected until status enumerations and transition rules are declared at registry, release and type level.","expectedCode":"ERR_LIFECYCLE_ENUM_UNDECLARED"},
  {"target":"DependencyTypeRegistry","id":"inverse-pairing-declared","kind":"positive","input":"A type declares directionality 'directed' and inverseOfTypeRef pointing at its converse term.","expect":"Inverse assertions are derivable on demand and a stored converse edge is detectable as a duplicate."},
  {"target":"DependencyTypeRegistry","id":"duplicate-inverse-without-pairing","kind":"negative","input":"Canonical and converse edges are stored as independent facts using two type terms with no declared inverse pairing or symmetry flag.","expect":"The duplication rule is unenforceable and the registry state is rejected until an inverse pairing is declared.","expectedCode":"ERR_INVERSE_PAIRING_UNDECLARED"},
  {"target":"ImpactScenario","id":"counter-canonical-licence-on-non-invertible-type","kind":"negative","input":"A propagation licence requests prerequisite-to-dependent traversal over a type whose pinned definition declares neither symmetry nor an inverse pairing.","expect":"The traversal is rejected as unlicensed inverse derivation.","expectedCode":"ERR_INVERSE_NOT_PERMITTED"},
  {"target":"ImpactScenario","id":"api-change-reverse-traversal-licensed","kind":"positive","input":"An API change at a prerequisite propagates to its dependents over types that permit licensed inverse derivation at contract and runtime phase.","expect":"The run proceeds, the counter-canonical direction is recorded on the licence, and no converse edge is stored."},
  {"target":"DependencyTypeRegistry","id":"nary-edge-rejected","kind":"negative","input":"A single dependency edge is asserted with three endpoints under a type declaring arity 3.","expect":"The edge is rejected as invalid, not recorded as low-confidence.","expectedCode":"ERR_ARITY_NOT_BINARY"},
  {"target":"DependencyTypeRegistry","id":"composite-prerequisite-group","kind":"positive","input":"A dependent requires one prerequisite and either of two alternatives.","expect":"A PrerequisiteGroup with groupSemantics 'all' containing a nested 'any' group is recorded, with every member expressed as a binary edge."},
  {"target":"DependencyTypeRegistry","id":"cross-type-composition-rule","kind":"positive","input":"An interface type and a package type are declared composition-eligible with a recorded basis.","expect":"A TypeCompositionRule for the ordered pair is published and multi-hop paths across the two types compose."},
  {"target":"ImpactScenario","id":"mixed-type-path-without-composition-rule","kind":"negative","input":"Traversal composes an interface edge with a package edge where no TypeCompositionRule exists for the pair.","expect":"The path does not compose and traversal halts at the type boundary with a stop reason.","expectedCode":"ERR_COMPOSITION_UNDECLARED"},
  {"target":"ImpactScenario","id":"heterogeneous-cycle-permission","kind":"negative","input":"A cycle spans two types, one permitting cycles and one forbidding them, and traversal proceeds on the permissive rule.","expect":"The traversal is rejected; heterogeneous cycle permission is the conjunction of all participating type rules.","expectedCode":"ERR_CYCLE_RULE_CONFLICT"},
  {"target":"DependencyTypeRegistry","id":"colocation-as-dependency-type","kind":"negative","input":"A co-location relation is registered as a dependency type with a canonical dependent-to-prerequisite direction.","expect":"The registration is rejected; co-location requires relationClass 'adjacency', which carries no canonical direction.","expectedCode":"ERR_NON_DEPENDENCY_RELATION"},
  {"target":"ImpactScenario","id":"adjacency-edge-as-stop-condition","kind":"positive","input":"A resource-delay traversal reaches an adjacency-class co-location edge.","expect":"Traversal halts with a stop reason code; the adjacency edge is reported and never propagates."},
  {"target":"DependencyTypeRegistry","id":"propagation-profile-release","kind":"positive","input":"A propagation profile is published with typeFilter, phaseWindow, traversalDirection, depthLimit, lagBound, unknownEdgePolicy, stopConditions and evidenceThreshold.","expect":"An immutable versioned PropagationProfile release is created and is pinnable by reference."},
  {"target":"ImpactScenario","id":"unversioned-profile-pin","kind":"negative","input":"A scenario pins propagationProfileRef to a profile that has no version, no release state and no digest.","expect":"The scenario is rejected because deny-by-default licensing cannot be evidenced against an unversioned profile.","expectedCode":"ERR_PROFILE_PIN_UNVERSIONED"},
  {"target":"ImpactScenario","id":"boolean-only-licence","kind":"negative","input":"A licence reduced to a single boolean is used for both the API-change and the resource-delay events on one frozen graph.","expect":"The runs are rejected; a licence that cannot carry type, phase, lag and unknown-edge policy cannot separate the two events.","expectedCode":"ERR_LICENCE_UNDERSPECIFIED"},
  {"target":"ImpactScenario","id":"snapshot-minted-by-analysis","kind":"negative","input":"The scenario creates its own graph snapshot record rather than referencing one minted on the dependency-edge side.","expect":"The snapshot is rejected; the analysis references snapshots and never masters them.","expectedCode":"ERR_SNAPSHOT_MASTERSHIP"},
  {"target":"ImpactScenario","id":"two-scenarios-same-graph-state","kind":"positive","input":"Two scenarios are executed over the identical frozen graph state.","expect":"Both pin the same graphSnapshotRef and the same digest under a named digestAlgorithm and canonicalizationMethod, and their outputs are comparable."},
  {"target":"ImpactScenario","id":"digest-without-algorithm","kind":"negative","input":"A snapshot digest is recorded with no digestAlgorithm and no canonicalizationMethod.","expect":"The pin is rejected because immutability and staleness detection are not verifiable.","expectedCode":"ERR_DIGEST_BASIS_MISSING"},
  {"target":"ImpactScenario","id":"unknown-edge-on-candidate-path","kind":"negative","input":"A candidate path traverses an edge in the unknown state and the result is published as a completed exposure set.","expect":"Traversal halts at the unknown edge, the edge is reported on the unexpanded frontier with a reason code, and completeness falls.","expectedCode":"ERR_UNKNOWN_EDGE_TRAVERSED"},
  {"target":"ImpactScenario","id":"absent-edge-terminates-branch","kind":"positive","input":"Traversal reaches an asserted-absent edge under a profile declaring unknownEdgePolicy.","expect":"The branch terminates with a distinct reason code that does not collapse asserted-absent into unknown."},
  {"target":"DependencyTypeRegistry","id":"epistemic-state-collapse","kind":"negative","input":"not-assessed and unresolved are mapped onto unknown in the registry state vocabulary.","expect":"The mapping is rejected; all five states remain distinct and unresolved carries its own definition.","expectedCode":"ERR_EPISTEMIC_COLLAPSE"},
  {"target":"ImpactScenario","id":"successor-ref-written-into-released","kind":"negative","input":"A successorRef is written onto a released scenario when a correction is issued.","expect":"The write is rejected; supersession is recorded in a separate link record.","expectedCode":"ERR_RELEASED_MUTATION"},
  {"target":"ImpactScenario","id":"status-overlay-on-stale-graph","kind":"positive","input":"A covering graph snapshot changes after release.","expect":"A status evaluation overlay records evaluatedStatus 'stale' with its basis and timestamp; the released scenario record is byte-identical before and after."},
  {"target":"DependencyTypeRegistry","id":"forward-supersession-discovery","kind":"negative","input":"A consumer holding registry release n must discover release n+1 using only supersedesRelease, which is recorded on n+1.","expect":"The discovery path is rejected as structurally impossible; a ReleaseSupersession link record is required.","expectedCode":"ERR_SUPERSESSION_UNDISCOVERABLE"},
  {"target":"ImpactScenario","id":"negative-conclusion-without-completeness","kind":"negative","input":"A scenario with no completenessRef publishes conclusionPolarity 'negative' for a subject.","expect":"The conclusion is rejected; a scenario with no completeness pin is permanently indeterminate.","expectedCode":"ERR_COMPLETENESS_REQUIRED"},
  {"target":"ImpactScenario","id":"never-stale-safe-harbour","kind":"negative","input":"A released scenario that pinned no completeness declaration remains released while the underlying completeness declaration is withdrawn, and continues to be cited as evidence of no impact.","expect":"The citation is rejected; absence of a completeness pin must make staleness unevaluable and the conclusion indeterminate, not durable.","expectedCode":"ERR_STALENESS_UNEVALUABLE"},
  {"target":"ImpactScenario","id":"coverage-predicate-applied","kind":"positive","input":"A completeness declaration covering subject set S, kinds K, phases P and interval I is pinned by a scenario whose exposure set falls inside S, K, P and whose execution time falls inside I.","expect":"Coverage evaluates true and a negative conclusion is admissible."},
  {"target":"ImpactScenario","id":"coverage-predicate-out-of-phase","kind":"negative","input":"A completeness declaration scoped to the build phase is pinned by a runtime-phase scenario drawing a negative conclusion.","expect":"Coverage evaluates false and the negative conclusion is rejected.","expectedCode":"ERR_COMPLETENESS_NOT_COVERING"},
  {"target":"ImpactScenario","id":"executed-without-outputs","kind":"negative","input":"A scenario reaches status 'executed' with no exposureSet, no stopReasons and no unexpandedFrontier.","expect":"The status transition is rejected; outputs are required from executed onward.","expectedCode":"ERR_REQUIRED_OUTPUT_MISSING"},
  {"target":"ImpactScenario","id":"suppressed-edges-reported","kind":"positive","input":"Edges are omitted from traversal by licence, depth limit and phase filter.","expect":"Each omitted edge appears in suppressedEdges with a reason code resolved against a pinned code list."},
  {"target":"ImpactScenario","id":"code-lists-unpinned","kind":"negative","input":"Stop reason and suppression reason codes are emitted with no codeListRefs pinned on the scenario.","expect":"The output is rejected; reason codes must resolve against pinned code list versions.","expectedCode":"ERR_CODELIST_UNPINNED"},
  {"target":"ImpactScenario","id":"exposure-labelled-affected","kind":"negative","input":"The scenario output set is published as the affected set with no assessor determination.","expect":"The label is rejected; the scenario may publish only a candidate exposure set.","expectedCode":"ERR_UNDETERMINED_AFFECTEDNESS"},
  {"target":"ImpactScenario","id":"two-events-differ-by-candidate-exposure","kind":"positive","input":"An API change and a resource delay are run on one frozen graph under different type filters, phase windows and licences.","expect":"The candidate exposure sets differ by type, phase and licence rather than topology, and neither is labelled affected or not-affected."},
  {"target":"EM-WRK-06-profile","id":"criticality-profile-field-map","kind":"positive","input":"The profile is specified against WM-ACT-034.","expect":"Edge reference set, dependent purpose, scheme identifier and version, assessing authority, validity interval, graph snapshot pin and licence gate are each mapped to a base field, a declared extension point, or marked unsatisfiable."},
  {"target":"EM-WRK-06-profile","id":"profile-absent","kind":"negative","input":"EM-WRK-06 is submitted with allocation candidates for Dependency Type Registry and Impact Scenario but no profile specification, fixtures or validation policy for the WM-ACT-034 criticality profile.","expect":"The submission is rejected as incomplete; a profile in scope requires its own artifact set.","expectedCode":"ERR_PROFILE_ARTIFACT_MISSING"},
  {"target":"EM-WRK-06-profile","id":"profile-cannot-pin-snapshot","kind":"negative","input":"No WM-ACT-034 base field or extension point can carry a graph snapshot pin for a criticality assessment.","expect":"The condition is recorded as an open blocker against the base; it is not grounds for allocating a new root.","expectedCode":"ERR_PROFILE_SNAPSHOT_UNPINNABLE"},
  {"target":"EM-WRK-06-profile","id":"assessment-kind-discriminator","kind":"positive","input":"An affectedness determination and a criticality assessment are recorded against the same edge set.","expect":"Each carries a distinct assessmentKind with its own identity, cardinality and validity rules, and the two do not merge."},
  {"target":"EM-WRK-06-profile","id":"criticality-promotes-exposure","kind":"negative","input":"A criticality assessment is used to promote a candidate exposure entry to affected.","expect":"The promotion is rejected; only assessmentKind 'affectedness-determination' pinned to the scenario snapshot may promote.","expectedCode":"ERR_ASSESSMENT_KIND_MISMATCH"},
  {"target":"EM-WRK-06-profile","id":"assessment-revision-rewrites-edge","kind":"negative","input":"Revising a criticality assessment writes the new band onto the dependency edge as an attribute.","expect":"The write is rejected; criticality is an assessment output and the edge declaration is unchanged.","expectedCode":"ERR_EDGE_MUTATION"},
  {"target":"EM-WRK-06-profile","id":"ordinal-scales-multiplied","kind":"negative","input":"Severity and likelihood ordinals are multiplied into a composite criticality score with no declared mapping.","expect":"The composite is rejected; severity, likelihood, confidence and uncertainty remain separate and scales are never combined without a named mapping.","expectedCode":"ERR_SCALE_COMPOSITION"},
  {"target":"DependencyTypeRegistry","id":"lag-calendar-zone-tzdb-pin","kind":"positive","input":"A type declaring lag is published with lagCalendarRef, ianaZone and tzdbRelease.","expect":"The lag semantics are resolvable and reproducible across evaluations."},
  {"target":"DependencyTypeRegistry","id":"lag-without-time-basis","kind":"negative","input":"A type declares a lag duration with no calendar, zone or timezone database release.","expect":"The type is rejected; the lag invariant is unenforceable without a pinned time basis.","expectedCode":"ERR_LAG_TIME_BASIS_MISSING"},
  {"target":"DependencyTypeRegistry","id":"release-validity-time-axis","kind":"positive","input":"A registry release records validFrom, validTo and retiredAt.","expect":"Each timestamp declares its time axis and zone, and event, observation and ingestion times remain distinct."},
  {"target":"ImpactScenario","id":"lag-grants-no-licence","kind":"negative","input":"A lag annotation on an edge is treated as authorisation to propagate across it.","expect":"The propagation is rejected; lag is a temporal annotation and grants no propagation or causal licence.","expectedCode":"ERR_LAG_NOT_A_LICENCE"},
  {"target":"DependencyTypeRegistry","id":"residual-impact-ownership-in-reference","kind":"negative","input":"The registry references WM-XCT-037 with purpose 'Dependency edge and impact semantics'.","expect":"The purpose string is rejected; impact semantics belong to Impact Scenario and must not be re-asserted inside the edge work item.","expectedCode":"ERR_RESIDUAL_IMPACT_OWNERSHIP"},
  {"target":"DependencyTypeRegistry","id":"unjustified-reference-padding","kind":"negative","input":"A dependency-type vocabulary declares references to a risk record, an observation and a citation while excluding ownership of all three and consuming none.","expect":"The references are rejected as unjustified coupling introduced to satisfy a reference-count minimum.","expectedCode":"ERR_REFERENCE_NOT_JUSTIFIED"},
  {"target":"ImpactScenario","id":"path-is-cause","kind":"negative","input":"A licensed traversal path is promoted directly to a causal attribution.","expect":"The promotion is rejected; causal attribution requires a separate WM-KNW-007 claim with evidence, scope, confidence and defeaters.","expectedCode":"ERR_PATH_NOT_CAUSE"},
  {"target":"ImpactScenario","id":"scenario-becomes-risk-determination","kind":"negative","input":"A released scenario output is recorded directly as a WM-KNW-015 risk determination.","expect":"The recording is rejected; risk may consume a scenario but is never computed by the traversal.","expectedCode":"ERR_RISK_BOUNDARY_LEAK"}
]
```

---

## 5. Explicit identifier decision

**No identifier is allocated, requested, guessed or implied by this audit.**

| Concern | Decision | Identifier state |
|---|---|---|
| Dependency Type Registry | Independent identity confirmed; stays a candidate | `modelId: null`, `registryId: null`, `allocationState: "unassigned"` — unchanged |
| Impact Scenario | Independent identity confirmed; stays a candidate | `modelId: null`, `registryId: null`, `allocationState: "unassigned"` — unchanged |
| Dependency (edge) | Remains a **narrowed** WM-XCT-037 edge | no new identifier |
| Criticality Assessment | Remains a **profile** of WM-ACT-034 | no own identifier; profile artifact required (F13) |
| Evidence citation / observation / claim / risk / endpoints | Remain external masters | WM-KNW-008, WM-MAT-008, WM-KNW-007, WM-KNW-015, endpoint masters — unchanged |

The new objects required by §3 — `DependencyType`, `PrerequisiteGroup`, `TypeCompositionRule`, `PropagationProfile`, `ReleaseSupersession` (registry side); `ScenarioSupersession`, `ScenarioStatusEvaluation` (scenario side) — are **internal objects of the two already-unassigned candidates**. They consume no registry identifier, create no third root, and must not be read as allocation requests. `DependencyEvidence` remains an inline binding, not a root. `canonicalPublishable` stays `false` for both candidates.

**Holds carried forward (not artifact defects, per audit scope):** registry allocation pending for both candidates; WM-XCT-037 base contradictions (boundary-versus-implementation on type vocabulary and impact computation, weak-versus-first-class identity, duplicate completeness rules, unverified pins) pending normative resolution; relations unapproved; adjacent drafts non-canonical single-provider work; no named confidence-scale master exists, leaving the scale-mapping invariant unenforceable until one is published; package conversion and live verification pending. No installability or publication-readiness claim is made or implied.

---

## 6. Freeze decision

**Closed. No rerun.**

This audit executed once and is now frozen. The REVISE verdict does not schedule a second audit: the sixteen defects are discharged by executing F1–F16 and passing the fifty fixtures in §4 at the next gate, verified by fixture execution and allocation-policy validation — not by re-auditing. Any artifact change beyond the bounded fixes above falls outside this frozen record and requires a new contour, not a reopening of EM-WRK-06.
