# Frozen semantic audit — EM-AI-02

## Verdict

**The intended decision is upheld.** Nothing in the supplied evidence disproves reuse-only: WM-AI-007 for registry identity, WM-SFT-004 for artifacts, WM-AI-006 for runs and run-contained effective configuration, WM-DAT-001 for datasets, WM-AI-001 for systems, WM-FLW-015 for observed consumption, external demand/capacity/reservation for requested and granted compute, family/architecture classificatory, Reusable Training Recipe conditional and identifier-unassigned, no identifier allocated.

The disposition survives; its **expression does not**. Twenty material defects follow. Two are genuine unresolved semantic conflicts inside the supplied text (checkpoint mastership, rights inheritance) that the provider comparison misreports as agreement; one contradicts the preserved decision outright (requested compute); the remainder are mastership leaks, false holds, missing publishability holds, underspecified lifecycle/time/evidence semantics, and fixtures that are neither deterministic nor correctly filed. All are remediable deterministically from the supplied text. No further provider run is required or permitted.

---

## Material defects

### D1 — Requested compute is mastered two ways, one of which contradicts the preserved decision

The preserved decision assigns **requested and granted** compute to external demand/capacity/reservation. The synthesis Disposition agrees ("Reuse EM-WRK-05 demand, pool and reservation semantics for requested and granted compute"), then its own §Compute contradicts it: "Requested compute is a run-owned planning assertion." The profile candidate hard-codes the contradicting version (constraint 5). Claude's study repeats it ("requested (plan, run-owned)"); Grok does not ("Map requested and granted to external capacity/reservation").

**Remediation.** Replace the synthesis sentence with: *"Requested compute is an EM-WRK-05 demand assertion that references the run; granted compute is an EM-WRK-05 reservation or quota with authority, effective period and expiry; observed compute is WM-FLW-015 consumption. WM-AI-006 holds only non-owning typed references to all three and owns none of them."* Replace profile constraint 5 with the same sentence. Delete "run-owned" from every occurrence in all five artifacts.

### D2 — Checkpoint mastership is unresolved, and the derivation edge points at an object with no identity

Synthesis and Claude: the checkpoint is **run-contained in WM-AI-006**, "not a registered artifact". Grok: "Both are WM-SFT-004 instances… A checkpoint is an intermediate immutable artifact." These are incompatible. The acceptance result depends on the answer: CK produced by R0 is bound as an input by R1 and R2, and A1/A2 carry "derivation back to the checkpoint" — a lineage edge terminating on an object that, under the synthesis reading, has no independent identity and no cross-run resolvability.

**Remediation.** Adopt the promotion boundary explicitly; add to synthesis §Checkpoint and as profile constraint 7: *"A checkpoint is run-contained in WM-AI-006 while it is referenced only within its producing run. Binding a checkpoint as an input by any run other than its producing run, or retaining it beyond the producing run's retention window, requires prior promotion to a WM-SFT-004 artifact revision with role `checkpoint`, derivation to the producing run and step, and its own digest. No derivation edge may terminate on a run-contained checkpoint."* Amend the acceptance result to state that CK is promoted to a WM-SFT-004 `checkpoint`-role revision before seeding R1 and R2. Allocate nothing.

### D3 — Rights inheritance is contradicted, in the direction that permits restriction laundering

Synthesis: "Licence and use restrictions remain per input and per resulting artifact and **propagate through derivation**." Claude: "inherited upstream terms propagated through derivation." Grok: rights "**do not inherit from the parent checkpoint**, family classification, shared endpoint, or a sibling run." Read literally, Grok's rule lets a fine-tune drop the base artifact's restrictions.

**Remediation.** Add to synthesis §Data and as a profile constraint: *"The restriction set of a derived artifact is the union of the restrictions of every version-qualified input binding of its producing run — including the seed checkpoint and base model artifact — and any restriction newly asserted on the output. Derivation never relaxes a restriction. Restrictions propagate along derivation edges only, and never along sibling-run, family, architecture, alias, registry-entry or endpoint edges."* Correct Grok's clause in the comparison to the bracketed scope (sibling/family/endpoint), not the parent.

### D4 — Reproducibility mastership is decided in the body and still open in the holds

Synthesis §Time: "Reproducibility is a bounded WM-AI-006 claim." Synthesis §Holds: "Reproducibility ownership overlaps between WM-SFT-004 and WM-AI-006." Claude confirms WM-SFT-004 asserts reproducibility status on the artifact. The same document both decides and defers.

**Remediation.** Keep the decision, delete the hold. Write in §Time: *"WM-AI-006 is the single master of reproducibility. WM-SFT-004 carries a non-authoritative reference of the form (runRef, runRevision) and restates no reproducibility status, scope, seed or limitation."* Remove "Reproducibility ownership overlaps between WM-SFT-004 and WM-AI-006" from synthesis holds and "reproducibility ownership reconciliation" from the profile holds; record instead a base-spec defect hold: *"WM-SFT-004 asserts artifact-level reproducibility status; correction required in the base spec before its next freeze."*

### D5 — Endpoint mastership is unresolved while two invariants depend on it

Claude: endpoints are "explicitly out of scope in WM-SFT-004 and WM-AI-001," mastered by the runtime/compute-environment authority per EM-TEC-04. Grok: "WM-AI-001 may expose one or more endpoints." Synthesis: "No frozen deployment or endpoint model was available in this contour." Invariant 8, invariant 9 and the acceptance result all assert endpoint behaviour with no named owner.

**Remediation.** Add to synthesis §Deployment and as a profile constraint: *"No base in EM-AI-02 masters endpoints or deployments. WM-AI-001, WM-SFT-004 and WM-AI-007 hold only authority-qualified external observations of deployment state. The endpoint is an unowned external typed reference in this contour."* Delete Grok's "WM-AI-001 may expose one or more endpoints" from the comparison as unsupported. Add hold: *"Endpoint and deployment mastership unassigned; EM-AI-02 endpoint invariants are unenforceable until a frozen runtime/serving authority exists."*

### D6 — The acceptance result asserts a co-serving pass that depends on an unowned control

The acceptance result states that A1 and A2 are exposed through E and that E "neither merges lineage nor relaxes D2 terms" — a pass. Grok's blocker (4) states the bind-time rights check has no holder: "if neither WM-SFT-004 nor WM-AI-001 can hold that constraint, serving compliance is a gap." The comparison records it as a hold while the acceptance result already records a pass. That is unsafe inference from an unenforced constraint.

**Remediation.** Rewrite the acceptance sentence as: *"Both are exposed through endpoint E. E merges no lineage and relaxes no D2 term. This outcome is asserted, not enforced: no base in EM-AI-02 owns a bind-time rights evaluation, so co-serving under divergent restrictions is HELD, not accepted."* Add the corresponding hold to the profile.

### D7 — The provider comparison reports agreement where D2 and D3 are conflicts

"Both reviews keep registry entry, artifact, **checkpoint role**, run, evaluation, deployment, endpoint and system distinct" silently adopts Grok's artifact-instance framing while the synthesis and profile adopt Claude's run-contained framing. "Dataset rights… remain bound to each run and derived artifact and never merge through shared serving" elides the parent-checkpoint inheritance question entirely. A comparison that conceals divergence is not usable evidence.

**Remediation.** Add a §Divergences section to the comparison recording both conflicts verbatim with the D2 and D3 resolutions, and state which provider position was not adopted and why. Remove the word "checkpoint role" from the agreement paragraph.

### D8 — `decision: "NEW MODEL"` contradicts every other statement of the candidate's status

The allocation candidate carries `"decision":"NEW MODEL"` alongside `"allocationState":"unassigned"`, `"modelId":null`, and universal agreement across synthesis, both studies, comparison and profile that the recipe has **no present independent identity**. The audit brief also forbids allocating a model ID. A positive `NEW MODEL` decision is readable as an allocation.

**Remediation.** Set `"decision":"CONDITIONAL NEW MODEL — NOT ALLOCATED"` and add two sibling fields: `"presentIndependentIdentity": false` and `"conditionsUnmet": ["independent governance and approval path distinct from WM-AI-005 and from run-pinned effective configuration","demonstrated reuse across two or more executions","named method-governance mastership authority"]`. If the `decision` enum is closed, use `"decision":"NO NEW MODEL"` and carry the conditional status solely in `allocationState`, `presentIndependentIdentity` and `conditionsUnmet`.

### D9 — The candidate asserts a mastership authority that no supplied evidence names

`"mastership":"AI engineering method-governance authority"` names an owner that appears in no frozen model, no ledger, no study and no comparison. Asserting mastership for an unidentified candidate is a mastership leak.

**Remediation.** Set `"mastership": null` and add `"mastershipHold":"No frozen method-governance authority is identified in EM-AI-02; mastership may not be asserted before one exists."`

### D10 — Recipe lifecycle is internally inconsistent and revision lifecycle is missing

`TrainingRecipe.required` includes `currentRevisionRef`, yet `draft` is a valid state in which no revision exists. `TrainingRecipeRevision.required` includes `effectiveFrom`, yet `draft` and `approved` precede effectiveness. Revisions carry `effectiveTo` and `supersedesRevision` — revision-level lifecycle signals — but no lifecycle field. `superseded` is a state with `successorRef` merely optional. The lifecycle enumeration is duplicated in `identityTest.independentLifecycle` and `objects.TrainingRecipe.lifecycle` and can drift.

**Remediation.** Move `lifecycle` to `TrainingRecipeRevision` with the same six states; delete it from `TrainingRecipe` and from `identityTest`, replacing the latter with `"independentLifecycle":"revision-level; see objects.TrainingRecipeRevision.lifecycle"`. Move `currentRevisionRef` and `effectiveFrom` from `required` to `optional`, and add `"conditionalRequirements":{"currentRevisionRef":"required when any revision status is effective","effectiveFrom":"required from status effective onward","effectiveTo":"required when status is superseded or retired","successorRef":"required when status is superseded"}`.

### D11 — Both JSON artifacts carry a hold that the supplied bundle falsifies

Allocation candidate holds: `"Independent Grok review is pending."` Profile holds: `"Independent Grok review and frozen audit remain pending."` The exact Grok response and the provider comparison are supplied. A false hold corrupts the publication gate in both directions.

**Remediation.** In the allocation candidate, replace that hold with `"Independent Grok review complete; recorded in the EM-AI-02 provider comparison."` In the profile, replace with the same string plus `"Frozen semantic audit complete; recorded in this contour's frozen audit."`

### D12 — The profile carries no publishability flag and drops four holds the synthesis records

`vercy-enterprise-profile-candidate/v1` has `newRuntimeId:false` but **no `canonicalPublishable` field at all**, while the allocation candidate has `canonicalPublishable:false`. Its three holds omit: single-provider base drafts (WM-AI-006 and WM-AI-007 are Codex-only under waiver), absence of a frozen evaluation/deployment/endpoint authority, source/crosswalk/fixture holds, and the explicit no-installability/no-publication-readiness statement. Claude's study also records a base-spec defect the reconciliation drops entirely: WM-SFT-004 lists 30 sources while its holds enumerate 21 base plus three Grok, and SPDX, AI RMF, ONNX, safetensors and HF model cards each appear under two source IDs.

**Remediation.** Add `"canonicalPublishable": false` to the profile. Append these holds verbatim: `"WM-AI-006 and WM-AI-007 are single-provider drafts under waiver (Codex only; Claude and Grok timed out at 120 s)."`, `"No frozen evaluation, deployment or endpoint authority exists in this contour."`, `"WM-SFT-004 source ledger is inconsistent: 30 listed sources against 21 base plus three Grok enumerated in holds, with duplicate source IDs for SPDX, AI RMF, ONNX, safetensors and HF model cards."`, `"Source, crosswalk and fixture holds remain."`, `"No installability or publication-readiness claim is made."`

### D13 — Profile constraints are a lossy subset of the invariants they must enforce

The profile carries six constraints; the contour carries fourteen invariants. A consumer applying the profile receives no rule for invariants 1, 2, 7, 10, 11, 12, 13 or 14. The profile is the applicable artifact; the invariant list lives only in prose.

**Remediation.** Add an `"invariants"` array to `vercy-enterprise-profile-candidate/v1` containing the full corrected invariant list (the fourteen, plus D16's additions) verbatim as strings, and add `"constraintsAreNonExhaustive": false` once every invariant is either a constraint or a listed invariant.

### D14 — Unratified relations are declared `required: true` and inherited by the profile

WM-AI-007 declares `composition → WM-SFT-004, required: true` while its own boundary decision calls that parent an unapproved signal and the relation ledger contains no WM-AI-007 edge. WM-AI-006 declares `WM-DAT-001 required: true` against a held candidate edge. The profile names both as bases and builds constraints on those bindings.

**Remediation.** Add to the profile: `"inheritedCardinalityOverrides":[{"from":"WM-AI-007","to":"WM-SFT-004","baseCardinality":"required","profileCardinality":"conditional","reason":"relation unratified; no ledger edge"},{"from":"WM-AI-006","to":"WM-DAT-001","baseCardinality":"required","profileCardinality":"conditional","reason":"ledger edge held as candidate"}]` and a hold: `"No EM-AI-02 constraint may depend on an unratified required relation; both overridden bindings block publication until the ledger edges are approved."`

### D15 — Bases and referenced authorities are unexplained, unnamed, or contradictorily reported

`bases` includes **WM-AI-001** and **WM-AI-005**, neither of which appears in the synthesis Disposition or in any profile constraint. Conversely, profile constraint 5 invokes "external reservation" without naming EM-WRK-05, and invariant 11 separates "evaluation" with no named authority — where Claude names WM-AI-003 as an existing unfrozen evaluation model and Grok states "no adjacent draft covers evaluation."

**Remediation.** Add to the synthesis Disposition: *"Reuse WM-AI-001 as the AI system master; it owns neither weights nor endpoints. Reuse WM-AI-005 as a generic configuration type only; it is never the effective training record and never a second run identity."* Add both as profile constraints. Name EM-WRK-05 explicitly in profile constraint 5. Record the evaluation authority as `"evaluationAuthority": null` with hold `"Evaluation authority contradictorily reported: WM-AI-003 cited as existing but unfrozen in one study, absent in the other. Unresolved; evaluation remains identifier-unassigned."`

### D16 — The contour's load-bearing classificatory rule is not an invariant

Family/architecture-is-classification-not-identity is the central decision of EM-AI-02 and appears only as prose in the Disposition and Identity sections. Grok states it as invariant 1; the synthesis's fourteen omit it. The recipe's unassigned status (Grok invariant 7) is likewise only a hold.

**Remediation.** Append to the synthesis invariant list, and to the profile `invariants` array from D13: `"15. Family and architecture classify registry entries and artifact lineage; they never identify a registry entry, artifact, run, endpoint or system."` and `"16. Reusable Training Recipe has no assigned identifier in this increment and may not be referenced as an identified object."`

### D17 — Time semantics are unpinned; cross-clock comparison is unruled

The synthesis enumerates ten distinct clocks but pins no format and states no comparison rule. Claude's study supplies both ("RFC 3339 with seconds and explicit offset"); neither the synthesis nor the profile carries it forward. No fixture over time semantics can be deterministic without it.

**Remediation.** Add to synthesis §Time and as a profile constraint: *"Every instant is RFC 3339 with seconds precision and an explicit UTC offset. Ordering and duration comparisons are valid only between instants of the same clock kind. Cross-clock arithmetic is rejected, not coerced."*

### D18 — Evidence staleness has no determinate consequence

"Evidence is revision-bound and becomes stale when a referenced digest changes" states a transition with no effect. Nothing says whether stale evidence is invalid, retained, or re-assertable, so no artifact can be tested against it.

**Remediation.** Add to synthesis §Time and as a profile constraint: *"On any change to a referenced digest, the referencing evidence transitions to status `stale`. Stale evidence supports no lifecycle transition, rights determination, reproducibility claim or publication decision until re-asserted against the new digest. Staleness never deletes or rewrites the prior evidence record, which remains resolvable at its original revision."*

### D19 — The fixture set is misfiled and non-deterministic

`vercy-enterprise-allocation-fixtures/v1` is keyed to `candidateName: "Reusable Training Recipe"`, but five of seven cases (`checkpoint-promotion`, `shared-compute-grant`, `digest-only-identity`, `seed-only-reproducibility`, `endpoint-merges-rights`) test the profile, not the candidate. If the candidate is never allocated, the profile's evidence is discarded with it. Separately: `shared-recipe-two-runs` is a *positive* case presupposing a recipe object with identity that does not exist; no case cites the invariant it exercises; no case pins a literal value (no digests, seeds, timestamps, quantities or units), so `"different observed GPU-hours"` and `"different digests"` are not decidable.

**Remediation.** Split into two files. Keep `vercy-enterprise-allocation-fixtures/v1` with `candidateName:"Reusable Training Recipe"` holding only `shared-recipe-two-runs` and `recipe-is-run`, each gaining `"conditional": true, "blockedBy":"allocationState=unassigned", "gatesProfile": false`. Move the other five into a new `{"format":"vercy-enterprise-profile-fixtures/v1","contourId":"EM-AI-02"}` file. Add to every case in both files the required fields `"invariants":[<integers>]` and `"pins":{…}` carrying literal fixed values, and change each `expect` to a single decidable assertion.

### D20 — Eight invariants and both resolved conflicts have no fixture

Existing coverage reaches invariants 1, 5, 7, 9, 13 only. Untested: **2** (equal names ≠ equal weights), **4** (full pin set), **6** (grant implies no employment/identity/deployment/use), **8** (endpoint change creates no run or revision), **10** (transformation creates a successor), **11** (registry entry ≠ artifact ≠ run ≠ evaluation ≠ deployment), **12** (protected weights outside the public catalogue), **14** (quantity kinds never summed) — plus the new 15 and 16, and the D2, D3, D14, D17 and D18 rules.

**Remediation.** Add the fixtures below.

---

## Exact additional fixtures

Each object carries `set` (`"profile"` or `"candidate"`), naming the file from D19 it belongs to. Digest strings are opaque fixed test literals, not real digests.

```json
[
  {"set":"profile","id":"equal-names-different-digests","kind":"negative","invariants":[2,15],"pins":{"displayName":"acme-instruct-7b","aliasA":"latest","artifactA":"sha256:aa01","artifactB":"sha256:aa02","familyRef":"acme-instruct"},"input":"Two artifacts share displayName 'acme-instruct-7b', alias 'latest' and family 'acme-instruct' but hold digests sha256:aa01 and sha256:aa02.","expect":"Equality is rejected. The two artifacts remain distinct WM-SFT-004 identities; name, alias and family carry no identity weight."},
  {"set":"profile","id":"full-pin-set-complete","kind":"positive","invariants":[3,4,13],"pins":{"baseArtifact":"sha256:aa00","tokenizer":"sha256:tk01","datasetSnapshot":"D1@2026-01-04","split":"train=0.9/val=0.1","codeRevision":"rev-7f","dependencyLock":"sha256:dp01","seed":20260105,"environment":"cuda-12.4/driver-550/h100","effectiveConfigDigest":"sha256:cf01"},"input":"A run declares every pinned value above and one effective-configuration digest.","expect":"The run is accepted as reconstructable within its declared limits; exactly one effective-configuration digest is recorded."},
  {"set":"profile","id":"pin-set-missing-environment","kind":"negative","invariants":[4,13],"pins":{"seed":20260105,"codeRevision":"rev-7f","environment":null,"dependencyLock":null},"input":"A run pins seed and code revision but omits resolved dependencies and the framework/compiler/driver/hardware environment, and asserts reproducibility.","expect":"The reproducibility assertion is rejected as under-specified. The run is recorded as non-reproducible; no identity merge or substitution is authorised by the omission."},
  {"set":"profile","id":"grant-implies-nothing","kind":"negative","invariants":[5,6],"pins":{"grantId":"external-reservation-fixture-1","grantedGpuHours":500.0,"effectiveFrom":"2026-01-01T00:00:00+00:00","effectiveTo":"2026-03-31T23:59:59+00:00"},"input":"A compute grant of 500.0 GPU-hours is used to assert that a person is employed, that an agent identity exists, that a deployment is live, and that 500.0 GPU-hours were consumed.","expect":"All four inferences are rejected. A grant asserts capacity only; employment, agent identity, deployment state and consumption each require their own evidenced assertion."},
  {"set":"profile","id":"requested-inferred-from-observed","kind":"negative","invariants":[5],"pins":{"observedGpuHours":45.5,"requestedGpuHours":null,"grantedGpuHours":120.0},"input":"A run has no recorded requested quantity; 45.5 observed GPU-hours are written back as the requested quantity.","expect":"The write-back is rejected. Requested, granted and observed remain three independently sourced assertions and are never derived from one another in either direction."},
  {"set":"profile","id":"requested-is-external-demand","kind":"positive","invariants":[5],"pins":{"demandRef":"em-wrk-05-demand-fixture-1","requestedGpuHours":120.0,"runRef":"R1"},"input":"A run's requested compute of 120.0 GPU-hours is recorded as an EM-WRK-05 demand assertion referencing R1.","expect":"Accepted. WM-AI-006 holds a non-owning typed reference to the demand assertion and stores no owned requested quantity."},
  {"set":"profile","id":"quantity-kinds-not-summed","kind":"negative","invariants":[14],"pins":{"gpuHours":45.5,"energyKwh":310.0,"emissionsKgCo2e":96.2,"currencyUsd":480.00,"elapsedHours":12.25},"input":"GPU-hours 45.5, energy 310.0 kWh, emissions 96.2 kgCO2e, cost 480.00 USD and elapsed 12.25 h are aggregated into one total.","expect":"The aggregation is rejected. Each quantity kind reports separately with its unit, interval, method and uncertainty; any conversion is a separate evidenced assertion."},
  {"set":"profile","id":"endpoint-repoint-creates-nothing","kind":"positive","invariants":[8,11],"pins":{"endpoint":"E","aliasBefore":"sha256:aa01","aliasAfter":"sha256:aa02","at":"2026-02-10T14:00:00+00:00"},"input":"Endpoint E is repointed from artifact sha256:aa01 to sha256:aa02 at 2026-02-10T14:00:00+00:00, and a second serving region is added.","expect":"No training run and no artifact revision are created. Only an authority-qualified external deployment observation is recorded; both artifacts retain their own digests and restrictions."},
  {"set":"profile","id":"quantization-creates-successor","kind":"positive","invariants":[10],"pins":{"sourceArtifact":"sha256:aa01","resultArtifact":"sha256:aa03","transform":"int8-quantization"},"input":"Artifact sha256:aa01 is int8-quantized, producing sha256:aa03.","expect":"A new WM-SFT-004 artifact revision sha256:aa03 is created with a derivation edge to sha256:aa01 and the union of its restrictions. No training run is created."},
  {"set":"profile","id":"in-place-weight-rewrite","kind":"negative","invariants":[1,10],"pins":{"artifact":"sha256:aa01","attemptedNewBytesDigest":"sha256:aa04"},"input":"The payload bytes behind artifact sha256:aa01 are replaced in place while the artifact record is retained.","expect":"The mutation is rejected. Payload bytes are immutable; a changed digest is a new artifact revision with lineage."},
  {"set":"profile","id":"registry-entry-is-not-artifact","kind":"negative","invariants":[11],"pins":{"registryEntry":"registry-entry-fixture-1","artifact":"sha256:aa01","run":"R1","evaluation":"eval-fixture-1","deployment":"E"},"input":"One identifier is used for the registry entry, the artifact, the run, the evaluation and the deployment.","expect":"The collapse is rejected. Registry entry, artifact, run, evaluation and deployment are five distinct identities with distinct lifecycles."},
  {"set":"profile","id":"weights-in-public-catalogue","kind":"negative","invariants":[12],"pins":{"registryEntry":"registry-entry-fixture-1","embeddedPayload":"weight-bytes","embeddedDossier":"confidential"},"input":"A public catalogue entry embeds weight bytes and confidential dossier content rather than referencing the artifact.","expect":"The embedding is rejected under deny-by-default. The catalogue may reference the artifact and its digest only; weights, training data, secrets and checkpoints stay outside."},
  {"set":"profile","id":"family-as-identity","kind":"negative","invariants":[15],"pins":{"family":"acme-instruct","architecture":"decoder-only-transformer","artifactA":"sha256:aa01","artifactB":"sha256:aa02"},"input":"Family 'acme-instruct' with architecture 'decoder-only-transformer' is used as the identity of a registry entry and to equate sha256:aa01 with sha256:aa02.","expect":"Both uses are rejected. Family and architecture classify registry entries and artifact lineage and identify nothing."},
  {"set":"profile","id":"cross-run-checkpoint-binding-requires-promotion","kind":"negative","invariants":[7],"pins":{"producingRun":"R0","checkpointStep":18000,"checkpointDigest":"sha256:ck01","consumingRun":"R1"},"input":"Run R1 binds checkpoint sha256:ck01 at step 18000, which remains run-contained in R0 and was never promoted.","expect":"The binding is rejected. A checkpoint consumed outside its producing run must first be promoted to a WM-SFT-004 revision with role 'checkpoint' and derivation to R0 at step 18000."},
  {"set":"profile","id":"promoted-checkpoint-seeds-two-runs","kind":"positive","invariants":[7,10],"pins":{"producingRun":"R0","checkpointArtifact":"sha256:ck01","runs":["R1","R2"],"outputs":["sha256:aa01","sha256:aa02"]},"input":"Checkpoint sha256:ck01 is promoted to a checkpoint-role artifact, then seeds R1 and R2 producing sha256:aa01 and sha256:aa02.","expect":"Accepted. Three artifacts and three runs exist; both derivation edges terminate on the promoted artifact, and no lineage edge terminates on a run-contained object."},
  {"set":"profile","id":"derived-restrictions-are-union","kind":"positive","invariants":[9],"pins":{"baseArtifact":"sha256:ck01","baseRestriction":"research-only","dataset":"D2","datasetRestriction":"no-commercial-use","output":"sha256:aa02"},"input":"Run R2 binds seed artifact sha256:ck01 (research-only) and dataset D2 (no-commercial-use), producing sha256:aa02.","expect":"sha256:aa02 carries both research-only and no-commercial-use. Derivation never relaxes a restriction."},
  {"set":"profile","id":"sibling-run-restriction-leak","kind":"negative","invariants":[9],"pins":{"runA":"R1","datasetA":"D1","restrictionA":"permissive","runB":"R2","datasetB":"D2","restrictionB":"no-commercial-use","output":"sha256:aa01"},"input":"Artifact sha256:aa01 from R1/D1 is assigned D2's no-commercial-use restriction because R2 shares the same seed checkpoint and family.","expect":"The assignment is rejected. Restrictions propagate along derivation edges only, never along sibling-run, family, alias, registry-entry or endpoint edges."},
  {"set":"profile","id":"co-serving-divergent-rights-is-held","kind":"negative","invariants":[9],"pins":{"endpoint":"E","artifactA":"sha256:aa01","restrictionA":"permissive","artifactB":"sha256:aa02","restrictionB":"no-commercial-use"},"input":"Endpoint E is bound to both sha256:aa01 and sha256:aa02 and the binding is asserted compliant.","expect":"The compliance assertion is rejected as unowned. No EM-AI-02 base holds a bind-time rights evaluation; the binding records HELD, and per-invocation restrictions remain those of the selected artifact digest."},
  {"set":"profile","id":"unratified-required-relation","kind":"negative","invariants":[11],"pins":{"from":"WM-AI-007","to":"WM-SFT-004","baseCardinality":"required","ledgerEdge":null},"input":"A profile constraint is validated against WM-AI-007's required composition to WM-SFT-004, for which the relation ledger holds no approved edge.","expect":"The validation is rejected. Cardinality is overridden to conditional in the profile and the binding is recorded as a publication blocker."},
  {"set":"profile","id":"stale-evidence-on-digest-change","kind":"negative","invariants":[13],"pins":{"evidenceRef":"evidence-fixture-1","referencedDigestBefore":"sha256:aa01","referencedDigestAfter":"sha256:aa04","at":"2026-02-18T08:30:00+00:00"},"input":"Evidence bound to sha256:aa01 is used to support a release transition after the referenced digest changes to sha256:aa04.","expect":"The transition is rejected. The evidence is status 'stale' and supports no lifecycle, rights or reproducibility claim until re-asserted against sha256:aa04; the original record remains resolvable."},
  {"set":"profile","id":"timestamp-without-offset","kind":"negative","invariants":[13],"pins":{"submitted":"2026-01-05T09:00:00","started":"2026-01-05T09:04:12+00:00"},"input":"A run records submitted time '2026-01-05T09:00:00' with no UTC offset and compares it to started time.","expect":"The record is rejected. Every instant requires RFC 3339 with seconds precision and an explicit offset; no offset is inferred."},
  {"set":"profile","id":"cross-clock-arithmetic","kind":"negative","invariants":[13],"pins":{"completed":"2026-01-05T21:15:00+00:00","ingested":"2026-01-07T11:00:00+00:00","released":"2026-01-09T10:00:00+00:00"},"input":"Elapsed run duration is computed as released minus completed, and knowledge currency as ingested minus completed.","expect":"Both computations are rejected. Duration and ordering comparisons are valid only within one clock kind; cross-clock arithmetic is rejected, not coerced."},
  {"set":"candidate","id":"recipe-identifier-assumed","kind":"negative","invariants":[16],"conditional":false,"gatesProfile":false,"pins":{"recipeRef":"any","allocationState":"unassigned"},"input":"An artifact references Reusable Training Recipe as an identified object while allocationState is 'unassigned'.","expect":"The reference is rejected. The candidate has no assigned identifier and no present independent identity; no identifier may be guessed or minted."},
  {"set":"candidate","id":"recipe-revision-draft-without-effective-from","kind":"positive","conditional":true,"blockedBy":"allocationState=unassigned","gatesProfile":false,"invariants":[16],"pins":{"revisionStatus":"draft","effectiveFrom":null,"currentRevisionRef":null},"input":"A recipe in status 'draft' holds a revision in status 'draft' with no effectiveFrom and no currentRevisionRef.","expect":"Accepted once the candidate is allocated. effectiveFrom is required only from status 'effective' onward and currentRevisionRef only when some revision is effective."},
  {"set":"candidate","id":"recipe-superseded-without-successor","kind":"negative","conditional":true,"blockedBy":"allocationState=unassigned","gatesProfile":false,"invariants":[16],"pins":{"revisionStatus":"superseded","successorRef":null,"effectiveTo":null},"input":"A recipe revision is set to 'superseded' with no successorRef and no effectiveTo.","expect":"Rejected. successorRef and effectiveTo are required when status is 'superseded'; a retired or superseded revision identifier remains resolvable and is never recycled."},
  {"set":"candidate","id":"recipe-inherits-run-outcome","kind":"negative","conditional":true,"blockedBy":"allocationState=unassigned","gatesProfile":false,"invariants":[16],"pins":{"recipeRevision":"rev-1","runs":["R1","R2"],"metricSource":"R1"},"input":"R1's metrics, checkpoints and compute actuals are recorded against recipe revision rev-1 and read as properties of R2.","expect":"Rejected. Recipe identity never inherits execution outcomes, checkpoints, metrics or resource actuals; two executions of one recipe remain two independently identified runs."}
]
```

---

## Freeze decision

**The boundary decision freezes. The artifacts, as supplied, do not.**

Freeze the EM-AI-02 semantic disposition now, unchanged: reuse-only across WM-AI-007, WM-SFT-004, WM-AI-006, WM-DAT-001, WM-AI-001, WM-FLW-015 and EM-WRK-05; family and architecture classificatory; Reusable Training Recipe conditional, identifier-unassigned, no present independent identity; no catalogue, model or runtime identifier allocated. This audit is spent; no further provider run is authorised, and none is needed — D1 through D20 are resolvable entirely from the supplied text.

Do **not** seal the five artifacts at their present revision. Apply every remediation above, then seal the synthesis, provider comparison, allocation candidate, profile candidate and the two split fixture files at the corrected revision as a single atomic reconciliation. D1, D2, D3 and D7 are correctness blockers on that seal — the artifacts currently contradict the preserved decision on requested compute and conceal two unresolved semantic conflicts.

`canonicalPublishable` remains **false** on both the profile and the allocation candidate after sealing. Publication stays held by, at minimum: the two unratified required relations (D14), the absent endpoint/deployment/evaluation authority and the unowned bind-time rights check (D5, D6, D15), the single-provider Codex-only bases WM-AI-006 and WM-AI-007, the WM-SFT-004 source-ledger inconsistency and artifact-level reproducibility assertion (D4, D12), and the unallocated recipe candidate. No installability, standards-conformance or publication-readiness claim is made or implied by this freeze.
