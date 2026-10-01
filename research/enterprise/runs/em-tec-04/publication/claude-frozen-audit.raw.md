# Frozen semantic audit — EM-TEC-04 / WM-SFT-010 `0.1.0-candidate.2`

## Verdict

**REVISE.** The boundary, delegation set and identity stratification are sound, but the candidate has a structural hole (no resource-to-environment containment), timeless status on all four subject types, required/optional contradictions that make several invariants unenforceable, and an asset-evidence contract with no carrier object. Fixtures are prose and cannot discharge any of it.

## Findings

**F1 — No resource↔environment relation (hidden aggregate boundary).** `hostingRelationKinds` gives occupant→resource (`runs-on`), resource→cluster (`member-of`), resource→physical (`backed-by`), occupant/logical-system→environment-or-cluster (`served-by`). Nothing binds an `InfrastructureResource` to a `RuntimeEnvironment`, and the resource object has no environment reference — only `region` and `providerRef`. Environment composition is therefore inferable only through occupants; a node with no occupant belongs to no environment. `two-region-service`, `node-replacement-as-of`, `cluster-member-turnover` and `region-flattening` cannot be evaluated.

**F2 — Timeless status (temporal-history loss).** `status` is a scalar current field on environment, resource, occupant and designation. `restricted` and `degraded` periods leave no interval, so "was this environment restricted at T?" is unanswerable while the invariant claims current state is an as-of projection. Lifecycle history is lost for exactly the subjects impact answers depend on.

**F3 — Lifecycle/required contradictions.** `commissionedAt` and `provisionedAt` are required, yet `planned` is the first lifecycle state — a planned subject cannot be recorded. Conversely `retiredAt`, `releasedAt` and `observedTo` are optional with no closure invariant, so terminal subjects keep open intervals and as-of queries after retirement are indeterminate. `HostingRelation` may be `superseded` with open `validTo`.

**F4 — Mandatory references behind optional relations (mastership conflict).** The WM-SFT-009 relation is `required: false`, but `deploymentOccurrenceRef` is required and an invariant asserts "exactly one". The WM-XCT-039 relation is `required: false`, yet `record-state` authority ("declared master for the fact path") and `mastership.projectionAndCompleteness` both depend on it. Optional relations cannot carry mandatory obligations.

**F5 — Duplicate containment path.** `parentResourceRef` (undated attribute) and `member-of` (temporal edge) express the same fact by two routes; no precedence rule. This is the concrete mechanism by which current topology re-enters as timeless truth.

**F6 — Cluster and node share one object, key space and lifecycle.** `identityStack` treats cluster as a stable capacity subject and node as a replaceable member, but both are `InfrastructureResource` with one lifecycle. `resourceKind` has no enumeration, while `hostingEndpointRules` references the type token `InfrastructureResource:cluster` — unresolvable as written.

**F7 — Succession is unevidenced (identity collision risk).** `retire-subject` promises "succession evidence"; the model provides only scalar `successorResourceId` and `successorRuntimeKey` — undated, unsourced, and `successorRuntimeKey` crosses planes (a key, not a record identity). Non-recycling is asserted over `runtimeKey`, which is minted externally by orchestrators that do recycle names; no uniqueness scope (per environment? per occurrence? over all time?) is stated.

**F8 — Unsafe CI/asset merge surface.** `ConfigurationItemDesignation.assetRef` reaches an asset directly, bypassing `assetEvidenceContract`. That contract has no carrier object, no identity, no lifecycle, no authority and no operation — nothing appends, supersedes or closes it — so `asset-link-without-evidence` has no rule to reject against. `identityEvidenceRefs` duplicates `evidenceRef` as a second evidence plane.

**F9 — Control authority exists on two planes.** `controlAuthorityRef` is required and undated on `RuntimeEnvironment`, while designation is dated and withdrawable. The `ci-withdrawal` fixture expects control to lapse with the subject surviving; the schema makes control permanent. Direct fixture/schema contradiction. `mastership` also omits the configuration-control master.

**F10 — Broken observation contract.** `RuntimeOccupantRecord` lacks `recordedAt` and `method`; `ConfigurationItemDesignation` lacks `recordedAt` and `sourceRef`. Both violate the invariant requiring source, method and observed/effective/recorded times. No record type distinguishes correction from withdrawal, so back-dated repair of a closed interval is unmodelled.

**F11 — Drift and conflict unenforceable.** `StateAssertion` has no `stateKind` vocabulary (desired vs observed is never declared), no status or lifecycle despite `supersedesAssertionId`. `HostingRelation` permits overlapping contradictory `runs-on` edges — no functional-cardinality invariant, no precedence over `confidence`. `mastership.observedHosting` names a role, not a master, so no authoritative slice can be selected.

**F12 — Fixtures not executable.** All fifteen cases are English; none binds objects, fields, timestamps or an expected rejection rule. Missing negatives: recycled runtime key resurrecting a closed occupant; two sources asserting conflicting simultaneous hosting; `parentResourceRef` contradicting `member-of`; designation on an ineligible subject type; cloud resource with no asset, and one chassis backing many resources; back-dated correction; occupant whose hosting resource sits in another environment; occupant without a deployment occurrence.

## Required remediations

1. Add a temporal resource→environment containment relation kind with endpoint rules, and an invariant binding an occupant's environment to the environment of its hosting resource (F1).
2. Replace scalar `status` with effective-dated status assertions on all subjects, or state explicitly that subject status is non-historical and remove the as-of claim (F2).
3. Align required fields with first lifecycle states; require a close timestamp in every terminal state and on `superseded`/`withdrawn` (F3).
4. Make the WM-SFT-009 and WM-XCT-039 relations required, or drop the invariants and authorities that presuppose them (F4).
5. Delete `parentResourceRef`; keep `member-of` (F5).
6. Enumerate `resourceKind`; separate cluster and node lifecycles or declare a subtype mechanism that resolves the `:cluster` token (F6).
7. Model succession as a dated, sourced edge; remove the scalar successor fields; scope and source `runtimeKey` uniqueness and state that non-recycling is enforced locally, not assumed of the orchestrator (F7).
8. Promote the asset-evidence link to a first-class dated object with identity, lifecycle, authority and operations; remove `assetRef` from designation; collapse the two evidence planes (F8).
9. Make `controlAuthorityRef` on the environment optional and derived from an active designation (F9).
10. Add `recordedAt`/`method` to occupant records and `recordedAt`/`sourceRef` to designations; add a correction mechanism distinct from withdrawal (F10).
11. Enumerate `stateKind`; give `StateAssertion` a lifecycle; add a non-overlap invariant for functional hosting kinds and a documented conflict-resolution order; name the observed-hosting master (F11).
12. Rewrite fixtures as executable assertions with field bindings, as-of timestamps and expected rule identifiers; add the eight missing negatives (F12).

## Adequate decisions

Occupant record as a dependent, never-master correlation record bound to one logical subject and one occurrence; CI as an effective-dated designation rather than a fifth class; the delegation set to logical-system, deployment-occurrence, projection and physical-item models; address as observation; cluster identity independent of members; the intent to retain drift; honest `canonicalPublishable: false`; retention declared pending rather than assumed unbounded; the identity stack's five-layer stratification.

## Minimal release gate

F1, F3, F4, F8 and F9 are correctness blockers — the model is internally contradictory until they close. F2 requires an explicit decision recorded either way. F12 must produce executable fixtures that fail before remediation and pass after, including the key-recycling and hosting-conflict negatives. Retention policy must be pinned before any finite-history guarantee; the pending external migration and publication holds remain outside this gate.
