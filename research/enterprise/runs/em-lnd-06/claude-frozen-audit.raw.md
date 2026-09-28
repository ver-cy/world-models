# Frozen semantic audit — EM-LND-06 / PLMM reconciled candidate rev. 2

## 1. Verdict

**REVISE.**

The decision is sound; the carrier is not. The candidate's invariant prose is materially stronger than its structure: several invariants (single-membership-per-product, acyclic successor lineage, access ceiling, reproducible evidence digest, inferred-edge exclusion) have no field, enum or key that can carry them, and at least two structures actively admit what the invariants forbid. That is a semantic defect class, not a drafting nit — it is the exact failure mode where a model reads as governed and behaves as ungoverned.

## 2. Decision on the reserved model

**CONFIRMED — COMPLETE RESERVED MODEL on the existing `vr.vercy.plmm`.**

- Reuse of `vr.vercy.plmm` / `PLMM` / `vercy-plmm`: confirmed. No new identifier is created anywhere in the candidate.
- `0.1.0-legacy` immutable and non-installable, digest `sha256:71003d1d…`: confirmed; the candidate's `legacyRelease` digest matches both `runtime_index.PLMM.digest` and `plmm_runtime_spec.metaModel.version`.
- No second `SoftwareProduct`: confirmed as an intent, **but see D16** — the required-`aismmRef` construction achieves "no second product" by making some real products unrepresentable, which is a different defect, not a satisfied invariant.

Reuse-only, profile and retire are correctly rejected on the frozen evidence (`structure.bundles: []`, `crud: {}`, `roles: []`, `installable: false`; AISMM is per-product by its own README; WM-XCT-039 is `publishableCanonical: false`).

## 3–4. Semantic defects, remediations, fixture expectations

### A. Duplicate identity

**D1 — Membership natural key admits the overlap its own invariant forbids.**
`naturalKey` = `[landscapeId, productRef, aismmRef.contentDigest, validFrom]`, but the invariant says one `productRef` may not hold overlapping active memberships with different AISMM digests. Including the digest in the key makes two such rows *legitimately distinct*. Conversely `productVersionPin` is required but absent from the key, so two memberships of different product versions collide on one key.
*Fix:* key = `[landscapeId, scopeVersionId, productRef, validFrom]`; move `aismmRef.contentDigest` out of the key and `productVersionPin` into the uniqueness rule as a conflict trigger, not a discriminator.
*Fixture:* two memberships differing only in `aismmRef.contentDigest` with overlapping validity are one conflicted identity, never two rows; two memberships differing only in `productVersionPin` are distinguishable and do not collide.

**D2 — `unresolved` is an unrepresentable state.**
The invariant and fixture `overlapping-aismm-contexts` both require a membership state `unresolved`; `lifecycle` is only `[proposed, asserted, withdrawn]`.
*Fix:* add `unresolved` to the lifecycle enum with required `conflictingMembershipRefs` and `resolutionOwnerRef`, retaining both assertions.
*Fixture:* the conflicting pair yields one `unresolved` record citing both assertion ids; neither original is deleted or silently preferred.

**D3 — `productRef` has no issuing authority or namespace rule.**
Nothing declares which master issues `productRef`, so the same product under two namespaces becomes two members — the exact duplicate the model claims to prevent.
*Fix:* `productRef = {namespace, masterSystemId, masterRecordId}` with one declared issuing master per landscape scope version and explicit alias-mapping evidence (pattern already used in WM-XCT-039 `identity_strategy`).
*Fixture:* two memberships whose `productRef`s resolve to the same master record are a duplicate-identity rejection, not two products.

**D4 — Mixed identifier namespaces in `relations`.**
`vr.vercy.aismm` is a runtime id; `WM-XCT-039` is a modelId. The dossier carries `registry_id: vr.wm-xct-039`.
*Fix:* use `vr.wm-xct-039`.
*Fixture:* every relation target resolves as a runtime id; a modelId in a relation target is rejected.

**D5 — Silent rename on a reserved identifier.**
Candidate `name: "Software Product Landscape"`; the registered name on `vr.vercy.plmm` is "Product Landscape Meta-Model", with `aliases: []`. Renaming on a reserved id whose prior release is frozen changes what the identifier historically meant, with no rename record.
*Fix:* keep the registered name, or record the rename with `previousNames` + `aliases` + release evidence.
*Fixture:* resolving `vr.vercy.plmm` at `0.1.0-legacy` returns the legacy name; any new name resolves only at the new version and carries a rename evidence ref.

### B. Mutable historical meaning

**D6 — `pinState` stored on the assertion.**
`pinState` is required on `LandscapeDependency`, but staleness is relative to query time and to later-observed digests. Storing it means the immutable assertion's recorded meaning must be rewritten as the world changes — directly contradicting "an existing edge is never silently retargeted."
*Fix:* store only endpoint pins; derive `pinState` per query and report it on `ImpactQueryResult`.
*Fixture:* after a newer target digest appears, the stored edge's serialized bytes are unchanged; only the result's derived `pinState` moves to `pinned-stale`.

**D7 — No successor lineage field.**
`pin-change-successor` expects "the prior edge remains reconstructible" and an invariant requires acyclic successor lineage, but no `supersedesDependencyId` / `supersedesMembershipId` exists.
*Fix:* add `supersedes*` refs, required on any assertion created by a pin change; acyclicity is checked over that relation.
*Fixture:* a pin-change successor without a predecessor ref is rejected; a lineage cycle is rejected; the predecessor remains resolvable at its original `asOf`.

**D8 — Withdrawal conflates "ceased" with "erroneous".**
The invariant "withdrawn edges remain resolvable for historical as-of queries" makes a retracted *mistake* permanently true in history. There is no correction operation.
*Fix:* `withdrawalReason.kind ∈ {ceased, erroneous}`; `ceased` remains in historical as-of results, `erroneous` is excluded from as-of results but retained in the audit record.
*Fixture:* a `ceased` edge appears in a historical as-of query; an `erroneous` edge does not, yet both remain in the audit trail with retraction evidence.

**D9 — `asOf` is both a stored landscape field and a query instant.**
`Landscape.required` includes `asOf`; `temporalPolicy` defines `asOf` as "the world-time instant evaluated by an impact query". One name, two semantics; the stored one must be mutated to stay meaningful.
*Fix:* remove `asOf` from `Landscape`, or rename the stored field `scopeAsOf` with a distinct, immutable definition.
*Fixture:* a query's `asOf` never reads from or writes to the landscape record.

**D10 — `0.1.0` vs `0.1.0-legacy` divergence unrecorded.**
The pinned repository declares "draft (v0.1.0)"; the runtime declares `0.1.0-legacy`. The candidate's holds cover org provenance but not this label divergence.
*Fix:* record an explicit label-mapping assertion (repo `v0.1.0` @ `a8e388c…` ↔ runtime `0.1.0-legacy`) with evidence, or mark it unresolved in `holds`.
*Fixture:* a version-label lookup that cannot produce the mapping evidence returns unresolved, not equality.

### C. False completeness

**D11 — Two coverage authorities.**
`Landscape.coverageStatus` and `CompletenessStatement.coverageClass` can disagree; the mutable landscape-level field is the one a careless reader reaches first.
*Fix:* delete `coverageStatus` from `Landscape`, or define it as non-authoritative and derived, always carrying `asOf` + `coverageStatementId`.
*Fixture:* a landscape claiming `complete` while its as-of statement says `partial` resolves to `partial` or is rejected.

**D12 — `complete` has no closure condition.**
The class exists with no definition of what closes it, against a dossier whose own invariant is "неполнота графа видима".
*Fix:* `complete` requires `knownMissingSources = ∅`, `staleSources = ∅`, `unknownBoundary` explicitly closed with evidence, and every contributing membership `pinned-current`; otherwise the maximum is `partial`.
*Fixture:* asserting `complete` with any non-empty gap set or open boundary is rejected.

**D13 — `unknownBoundary` untyped.**
An empty string silently reads as "no unknowns".
*Fix:* structured value `{state: closed-with-evidence | open, reasons[], evidenceRefs[]}`; empty is never `closed`.
*Fixture:* an absent or empty `unknownBoundary` forces `coverageClass` to `unknown`.

**D14 — `zero` vs `unknown` is undecidable for an empty graph.**
`emptyGraphRule` says "unknown coverage or zero observed coverage" with no discriminator; fixture `empty-observation` leaves the class unstated.
*Fix:* `zero` only when the source set is enumerated, current and complete and observed edges = 0; otherwise `unknown`.
*Fixture:* the same empty graph classifies `unknown` under incomplete source coverage and `zero` only under a closed, current source set — and `legacy-empty-runtime` is pinned to `unknown`.

**D15 — Dependencies cannot carry `assertionKind`; confidence threshold undefined and contradictory.**
`LandscapeMembership` has `assertionKind`; `LandscapeDependency` does not, yet invariants and fixtures classify edges as declared/observed/inferred/scenario. The invariant excludes inferred edges unconditionally; fixture `inferred-edge` implies a "confirmation threshold" that exists nowhere.
*Fix:* add required `assertionKind ∈ {declared, observed, inferred, scenario}` to `LandscapeDependency`; exclude `inferred` and `scenario` from confirmed paths unconditionally and delete the threshold language.
*Fixture:* an edge with no `assertionKind` is rejected; an inferred edge at confidence 0.99 still appears only in `qualifiedPaths`.

**D16 — Required `aismmRef` silently excludes real products.**
`aismmRef` is required *and* in the natural key, so a product without an AISMM context cannot be a member at all. The graph then omits it with no gap record — false completeness in the direction no one checks. This also contradicts Grok's "unpinned `aismmRef` is an explicit gap, never silent latest" and the hold that AISMM digest-to-commit compatibility is unproven.
*Fix:* make `aismmRef` optional with required `aismmRefAbsenceReason`; keep it out of the key; unpinned memberships are visible and qualified, never confirmed.
*Fixture:* a product with no AISMM model is a visible member with an explicit absence reason and appears in `qualifiedPaths`, not omitted.

**D17 — Eleven bundles read as structure, carry none.**
`plmm.01`–`plmm.11` carry only a `semantics` string. No findings, questions, artifacts, CRUD or roles exist — precisely what `migrationNotes` says is missing in the legacy version. `plmm.03`–`plmm.06` and `plmm.11` are "projections" with no projection entity and no external-master ref fields, so five of eleven bundles have nothing that can hold content.
*Fix:* mark every bundle `contentState: declared-empty` (explicit empty-layer declaration, not blankness); add a model-level hold that no findings/questions/artifacts/CRUD/roles are supplied; define a `ProjectionReference` entity or declare the projection bundles content-free in this revision.
*Fixture:* a bundle with no findings/questions/artifacts renders as an explicit empty layer, and no model-level structural-completeness claim is emitted.

### D. Non-reproducible traversal

**D18 — No record-time cutoff.** *(sharpest reproducibility defect)*
Assertions carry `recordedAt` and `temporalPolicy` defines assertion time, but `ImpactQueryResult` pins only `asOf`. A backdated assertion arriving later changes the answer for a fixed `asOf`, breaking "same pinned scope, graph and parameters ⇒ same evidence digest".
*Fix:* require `asAt` (record-time cutoff) on every result; traversal admits only `recordedAt ≤ asAt`.
*Fixture:* insert a backdated edge after a result; re-running with the same `(asOf, asAt, params)` reproduces the original `evidenceDigest`; only a new `asAt` surfaces the new edge.

**D19 — Traversal parameters are not required structure.**
The invariant names start nodes, relation filter, depth and cycle policy; `ImpactQueryResult.required` carries an opaque `query`. `cyclePolicy` has no enumeration.
*Fix:* explode into required `startRefs`, `relationFilter`, `assertionKindFilter`, `depthLimit`, `cyclePolicy` with a closed enum (`visit-once`, `fail-on-cycle`, `bounded-revisit-n`).
*Fixture:* `cycle-bounded` asserts a deterministic path set plus an `excludedEdges` entry with reason `cycle-policy`; a result missing any named parameter is rejected.

**D20 — `querySeed` undefined; `evidenceDigest` uncanonicalized.**
A seed implies nondeterministic ordering that is never described; the digest has no serialization or array-ordering rule, so two conforming implementations produce different digests for identical answers.
*Fix:* define `querySeed` as a tie-break ordering seed (or remove it); specify a total ordering over `confirmedPaths`, `qualifiedPaths`, `visitedMemberships`, `traversedDependencies`, `excludedEdges` and a canonical serialization for the digest input.
*Fixture:* two independent implementations produce byte-identical `evidenceDigest` for the same pinned inputs.

**D21 — `sourcePin.contentDigest` is an unverifiable invented fact.**
`sha256:050e7848…` appears nowhere in the frozen dossier, and `snapshotRule` ("canonical JSON serialization of the eleven frozen layer documents") does not specify key ordering, encoding, line endings, filename keys, or whether the README — from which the relation vocabulary and federation claims derive — is in or out.
*Fix:* demote to `contentDigest: {value, state: "unverified-claimed"}` or drop it and pin only commit `a8e388c21901540b71cc8479d4d6ef119c2ea276` until a published serialization procedure reproduces it; state README inclusion explicitly.
*Fixture:* recomputing the digest under the stated rule must equal the recorded value; a mismatch or an unspecified rule rejects the pin.

### E. Access leakage

**D22 — The access-ceiling invariant has no carrier.**
No `classification`, `accessPolicyRef` or `visibility` exists on any entity or on `evidenceRefs`; `query-impact` authority is the undefined string "authorized reader". The invariant is unenforceable as written.
*Fix:* required `accessPolicyRef` (or classification) on landscape, membership, dependency and evidence refs; `ImpactQueryResult` carries `effectiveAccessCeiling` derived as the strictest contributing policy.
*Fixture:* a result's ceiling equals the strictest contributing evidence classification; a result whose ceiling is looser than any contributor is rejected.

**D23 — Existence leakage through gaps and traversal arrays.**
`qualifiedPaths`, `visitedMemberships` and `excludedEdges` enumerate products and product-to-product relationships. Disclosing that an edge exists can leak the relationship itself even when the evidence is redacted. WM-XCT-039 handles this with `derivedEdgeFilter`, purpose binding and field allowlists; the candidate has none.
*Fix:* two policy-selected redaction modes — `existence-disclosed` and `existence-suppressed`; under suppression the result reports an aggregate `suppressedEdgeCount` with no endpoint identifiers, and coverage degrades (never `complete`). Add purpose binding to `query-impact`.
*Fixture:* an unauthorized reader's result contains no identifier of a suppressed endpoint, and its coverage class is not `complete`.

**D24 — Access ceiling and digest reproducibility contradict each other.**
Per-reader redaction means the same `(scope, asOf, params)` yields different results, so "same parameters ⇒ same evidence digest" is false across entitlements.
*Fix:* bind `evidenceDigest` to `(scopeVersionId, asOf, asAt, params, entitlementProfileId)`; digests are comparable only within one entitlement profile.
*Fixture:* one query under two entitlement profiles yields two digests, each stable on re-run, with no equality claimed between them.

### F. Unsupported release claims

**D25 — Relation vocabulary replaces evidence with invention.**
The pinned layer `02-relationships` defines `depends_on, consumes_from, provides_to, extends, replaces, federates_with`. The candidate substitutes `uses-platform, integrates, data-flow, event, runtime-shared` — unevidenced — and drops `replaces`/`extends`, on which `plmm.08` (replacement, deprecation, migration) depends, and `federates_with`, on which `plmm.07` depends. Two declared bundles have no relation type able to express their stated semantics.
*Fix:* adopt the six evidenced types as the normative closed vocabulary; if the five-term set is retained, record it as a proposed superset with an explicit mapping to the six and an evidence note.
*Fixture:* a `replaces` edge drives `plmm.08` lineage end to end; a `relationType` outside the closed vocabulary is rejected.

**D26 — Non-normative v1 properties promoted to required.**
`scope`, `architecture_state`, `as_of`, `composition_version` are all `candidate-not-normative` in the dossier; the candidate makes `architectureState`, `compositionVersion`, `asOf` required with no provenance marker.
*Fix:* retain the fields, tag each `provenance: candidate-not-normative (LND-06)`, and keep them out of any conformance claim.
*Fixture:* a conformance report lists these fields as non-normative and does not count them toward conformance.

**D27 — `canonicalPublishable` vs `publishableCanonical`.**
The candidate's top-level field is `canonicalPublishable`; the dossier's field and the candidate's own invariant text both use `publishableCanonical`. A registry gate keyed on one name silently misses the other.
*Fix:* use `publishableCanonical` throughout.
*Fixture:* the publication gate reads the canonical field name and refuses to publish when it is false.

**D28 — Version-label self-contradiction, resting on a label that does not exist.**
The candidate occupies `0.2.0-candidate.2` while asserting that repository labels never assign runtime versions; and `versionGuard` plus fixture `repo-label-not-runtime-version` cite a repository "v0.2.0" label that is absent from the frozen pin — `a8e388c` README shows badge `PLMM-v0.1.0` and "early **draft (v0.1.0)**". This is Grok's unevidenced claim carried into the candidate.
*Fix:* restate the guard generically ("no repository label assigns a runtime version"); rewrite the fixture against the actual `v0.1.0` draft label; state that `0.2.0-candidate.2` is a research label reserving nothing on `0.2.0`.
*Fixture:* using the repository `v0.1.0` draft label as a runtime version assignment is rejected.

**D29 — Missing holds (each one an implicit completeness claim).**
Absent: (a) fixtures are expectations, never executed — the dossier blocking decision requires fixture checks *before* any publication-readiness statement; (b) ELMM's role, named in a blocking decision, appears nowhere in the dossier and is silently dropped; (c) semantic crosswalk PLMM↔AISMM, rights/licensing (Apache-2.0 / NOTICE) and source mastership confirmation; (d) WM-XCT-039's own composition targets `vr.wm-xct-001/003/037` are not in this dossier, so even optional reference is transitively unverified; (e) the contour's "AISMM 3.2 README" question is unsupported — no `3.2` string exists in the frozen material — and must be closed as evidence-absent rather than dropped.
*Fix:* add `fixturesExecuted: false` and one hold per item (a)–(e).
*Fixture:* any publication-readiness assertion while `fixturesExecuted` is false or any hold is open is rejected.

**D30 — Enum values and a bundle claim with no support.**
`entryKind: "landscape-aggregate"` and `status: "research-candidate"` appear in no frozen enumeration (dossier has `kind: landscape`, `entry_kind: aggregate`, statuses `published`/`legacy`); `plmm.07` promises "exposed-projection declarations" with no entity, field or operation behind it.
*Fix:* draw both values from the existing registry enumerations or record them as proposed additions pending registry control; either define a projection declaration or remove the clause from `plmm.07`.
*Fixture:* an enum value absent from the registry enumeration is rejected; a bundle may not declare a capability with no entity or operation.

## 5. Contradictions across dossier, providers, candidate and fixtures

1. **Candidate vs itself (structural).** Membership natural key includes `aismmRef.contentDigest` while the invariant forbids exactly that overlap (D1). `pinStates` includes `source-unpinned`, `target-unpinned`, `missing` while both pins are `required` fields (D6/D37-class). Invariants require a scope-version-bound graph, but neither `LandscapeMembership` nor `LandscapeDependency` carries `scopeVersionId` — only `CompletenessStatement` and `ImpactQueryResult` do, so the scoped traversal the invariant describes cannot be computed from the edges.
2. **Candidate vs fixtures.** `overlapping-aismm-contexts` expects a lifecycle state the enum lacks (D2). `inferred-edge` presumes a confirmation threshold the invariant forbids (D15). `repo-label-not-runtime-version` tests a label absent from the frozen repository (D28). `withdrawn-history` assumes all withdrawals remain historically true (D8).
3. **Candidate vs dossier.** Relation vocabulary replaces the pinned layer-02 vocabulary (D25). `sourcePin.contentDigest` is a fact not present in the dossier (D21). `canonicalPublishable` diverges from `publishableCanonical` (D27). `related_research_contours: []` and no `EM-TEC-01` or `WM-SFT-001` appears anywhere in the dossier, yet the candidate's holds depend on both — inherited from Grok, unverifiable here.
4. **Comparison vs the studies it summarizes.** The comparison credits Claude with "evidence access ceiling" and the "per-membership exact AISMM content pin"; neither appears in Claude's study — Claude proposed a registry-level `requires: [AISMM @ pinned ref]` and flagged the tag-vs-commit choice as undecided, and neither study raises access ceilings at all. The access-ceiling invariant and the per-membership pin are reconciliation inventions presented as provider-derived. Attribution must be corrected; the two ideas are sound but currently carry unearned provenance.
5. **Provider vs provider, unresolved by reconciliation.** Claude's membership key omits the AISMM digest; Grok's includes `aismmRef`. The candidate adopted a hybrid matching neither and contradicting its own invariant (D1). Claude treats AISMM as a required registry relation; Grok and the candidate treat it as optional reference while making `aismmRef` a required field (D16). Both conflicts were merged rather than decided.
6. **Dropped provider findings.** Claude's closure of the "AISMM 3.2" question as evidence-absent, its ELMM gap, and its note that WM-XCT-039's composition targets are outside the dossier were all correct and all lost in reconciliation (D29).
7. **Evidence status, not a contradiction but a bound on every claim above.** Runtime digests are nowhere linked to repository commits for either model; the AISMM pin is `v3.1.0-4-gfe40e61`, four commits past tag; `requires: []` and `relations: []` on both runtime entries mean the PLMM→AISMM federation exists only as prose. The candidate's holds handle this correctly, and it is the reason no compatibility or installability statement in this audit should be read as proven.

## 6. Remediation checklist (closed)

1. Rekey `LandscapeMembership` to `[landscapeId, scopeVersionId, productRef, validFrom]`; remove `aismmRef.contentDigest` from the key; treat differing `productVersionPin` / AISMM digest under overlap as conflict, not discrimination. *(D1)*
2. Add `unresolved` to the membership lifecycle with `conflictingMembershipRefs` and `resolutionOwnerRef`. *(D2)*
3. Structure `productRef` as `{namespace, masterSystemId, masterRecordId}` with one declared issuing master per scope version and alias-mapping evidence. *(D3)*
4. Change the WM-XCT-039 relation target to `vr.wm-xct-039`. *(D4)*
5. Restore the registered model name or record the rename with `aliases` / `previousNames` and evidence. *(D5)*
6. Add `scopeVersionId` to `LandscapeMembership` and `LandscapeDependency` required fields. *(Contradiction 1)*
7. Remove `pinState` from the stored dependency; derive and report it per query. *(D6)*
8. Add `supersedesDependencyId` / `supersedesMembershipId`, required on pin-change successors; check acyclicity over that relation. *(D7)*
9. Split `withdrawalReason.kind` into `ceased` and `erroneous`, with erroneous excluded from as-of results and retained in audit. *(D8)*
10. Remove `asOf` from `Landscape` or rename it `scopeAsOf` with an immutable definition. *(D9)*
11. Record the repo `v0.1.0` ↔ runtime `0.1.0-legacy` label mapping with evidence, or add it to `holds` as unresolved. *(D10)*
12. Delete `Landscape.coverageStatus` or make it derived and non-authoritative with `asOf` + `coverageStatementId`. *(D11)*
13. Define the closure condition for `coverageClass: complete`. *(D12)*
14. Type `unknownBoundary` as `{state, reasons[], evidenceRefs[]}`; empty never means closed. *(D13)*
15. Define the `zero` vs `unknown` discriminator for empty graphs and pin `legacy-empty-runtime` to `unknown`. *(D14)*
16. Add required `assertionKind` to `LandscapeDependency`; exclude `inferred` and `scenario` from confirmed paths unconditionally; delete the confidence-threshold language from fixture `inferred-edge`. *(D15)*
17. Make `aismmRef` optional with required `aismmRefAbsenceReason` and out of the natural key. *(D16)*
18. Mark every bundle `contentState: declared-empty`; add the no-findings/questions/artifacts/CRUD/roles hold; define or disclaim the five projection bundles and `plmm.07`'s exposed projections. *(D17, D30)*
19. Add required `asAt` record-time cutoff to `ImpactQueryResult` and to traversal admission. *(D18)*
20. Replace opaque `query` with required `startRefs`, `relationFilter`, `assertionKindFilter`, `depthLimit`, `cyclePolicy`; enumerate `cyclePolicy`. *(D19)*
21. Define `querySeed` or remove it; specify total ordering and canonical serialization for `evidenceDigest` inputs. *(D20)*
22. Demote `sourcePin.contentDigest` to unverified-claimed or drop it; specify the snapshot rule including README inclusion. *(D21)*
23. Add `accessPolicyRef` / classification to landscape, membership, dependency and evidence refs; add derived `effectiveAccessCeiling` to results; define the `authorized reader` role. *(D22)*
24. Add `existence-disclosed` / `existence-suppressed` redaction modes with aggregate suppression counts and purpose binding on `query-impact`; suppressed results may not be `complete`. *(D23)*
25. Bind `evidenceDigest` to `entitlementProfileId` and state that digests compare only within one profile. *(D24)*
26. Adopt the six evidenced relation types as the closed vocabulary, or map the proposed five to them with an evidence note; restore `replaces`, `extends`, `federates_with` for `plmm.08` and `plmm.07`. *(D25)*
27. Tag `architectureState`, `compositionVersion`, `asOf`, `scope` with `provenance: candidate-not-normative (LND-06)`. *(D26)*
28. Rename `canonicalPublishable` to `publishableCanonical`. *(D27)*
29. Restate `versionGuard` generically, rewrite the fixture against the actual `v0.1.0` draft label, and declare `0.2.0-candidate.2` a research label reserving nothing. *(D28)*
30. Add `fixturesExecuted: false` and holds for ELMM, semantic crosswalk / rights / source mastership, WM-XCT-039's unverified transitive composition targets, and the evidence-absent "AISMM 3.2" question. *(D29)*
31. Draw `entryKind` and `status` from registry enumerations or mark them proposed additions pending registry control. *(D30)*
32. Correct `providerReconciliation` / comparison attribution: the access-ceiling invariant and the per-membership AISMM pin are reconciliation additions, not Claude's; record the unresolved Claude-vs-Grok key and AISMM-requirement conflicts as decisions taken, not as convergence. *(Contradictions 4–5)*
33. Add fixtures for items 6, 9, 12–17, 19–25, 26 and 30 — the current set has no case for scope-version binding, erroneous retraction, `complete` closure, `zero`/`unknown` disambiguation, missing `assertionKind`, missing `authorityRef`, bitemporal replay, digest canonicalization, `sourcePin` digest verification, access ceiling derivation, existence suppression, two-entitlement digest comparison, successor-lineage acyclicity, relation-vocabulary closure, or publication gating on open holds.
34. Re-run this frozen audit against the revised candidate; update the hold "one frozen no-tools semantic audit is pending" to record that this pass reviewed the supplied design summary only — not source truth, digests, or executable behavior.
