## Verdict

**COMPLETE RESERVED MODEL** — in place, under the existing reserved id `vr.vercy.plmm`, as a new version line; keep `0.1.0-legacy` frozen as a historical artifact.

Rejected alternatives, on dossier evidence:

- **REUSE ONLY** is impossible. The runtime spec has `structure.bundles: []`, `serviceLayers.crud: {}`, `roles: []`, `policies: []`, `artifactFormats: []`, and `installable: false`. There is nothing instantiable to reuse.
- **PROFILE** has no valid base. AISMM is explicitly per-product ("full structured context of ONE product"); profiling it would relocate landscape facts into product scope. WM-XCT-039 is narrower (tenant-scoped service→asset graph, `entry_kind: aggregate`) and is itself `publishableCanonical: false`.
- **RETIRE** is unjustified: the repository pin `a8e388c` carries eleven substantive layers covering exactly the contour's scope, and no other dossier model masters product-to-product landscape membership.

## Evidence state/version reconciliation

**AISMM 3.2 mismatch: not present in this dossier.** Runtime `version: 3.1.0`; repository README badge `AISMM v3.1.0`; `previousVersions` lists only 3.0.0 and 2.x. No 3.2 string appears anywhere. The contour's `specific_questions` entry about "AISMM 3.1 runtime and 3.2 README" is stale against these bytes and should be closed as a numbering question.

It is replaced by a different, narrower discrepancy: `describe: v3.1.0-4-gfe40e61` — the pinned tree is **four commits past the v3.1.0 tag** (last commit 2026-08-03, an FCD link change). So the *label* reconciles while the *bytes* do not equal the tag. Additionally `aismm_runtime_spec_summary.metaModel.status` reads "canonical legacy assembly projection" while the registry says `status: published, installable: true`; the dossier contains no fixture or digest cross-check linking the runtime digest `sha256:a603…` to commit `fe40e61`. I therefore assert no compatibility and no installability for either model.

**PLMM.** Runtime `0.1.0-legacy`, `status: legacy`, digest `sha256:7100…`, empty projection, `legacySource: https://github.com/ver-cy/plmm`. Repository pin `a8e388c` (2026-06-22) declares **v0.1.0 draft** and links to `orkestron-ai/software-meta-model` and the Orkestron org. Two unreconciled facts: (a) the runtime `-legacy` suffix versus the repository's plain `0.1.0` draft label; (b) org provenance `ver-cy` versus `orkestron-ai`. Neither is resolvable from the dossier; both are publication holds.

**Declared federation is prose only.** Both models have `requires: []` and `relations: []`. The PLMM→AISMM federation exists in README text and in layer `07-federation`, not in the registry graph.

## Boundary

PLMM masters the landscape *between* products and nothing inside one:

| PLMM masters | PLMM references only |
|---|---|
| `SoftwareLandscape` identity, scope, `architecture_state`, `as_of`, `composition_version` | Product internals (requirements, architecture, code, runtime) — AISMM |
| `LandscapeMembership` (which product is in which landscape, since when, with what confidence) | `SoftwareProduct` identity itself — held by the product's own master/AISMM registry |
| `LandscapeDependency` (typed, directed, version-pinned product-to-product edges) | Asset-level and tenant-isolated service graphs — WM-XCT-039 |
| Completeness/coverage of the graph and impact-routing results | Projection/IAM enforcement, CMDB/discovery adapters — out of scope per WM-XCT-039's own `out_of_scope` |

**No second `SoftwareProduct`.** Membership carries `productRef` (external authoritative id) plus `aismmRef`; the product record is never re-mastered. Relation vocabulary can be adopted from repo layer 02: `depends_on, consumes_from, provides_to, extends, replaces, federates_with`.

**Tenant/service specialization.** WM-XCT-039 is not a parent and not a dependency. For managed-service landscapes, `LandscapeMembership` may carry an optional `tenantScopeRef`; isolation, projection grants and per-fact mastership stay delegated. Any `COMPOSE` edge to `vr.wm-xct-039` would inherit its single-provider waiver and its "nested schemas not supplied" hold — so do not declare one now.

## Membership/dependency/completeness contract

- **Membership identity:** namespace-scoped immutable surrogate, natural key `(landscapeId, productRef, validFrom)`. Lifecycle `proposed → asserted → withdrawn`; withdrawal tombstones, never deletes, so historical impact answers stay explainable. Each membership carries `assertionKind (declared|observed|inferred)`, `confidence`, `sourceRef`.
- **Dependency identity:** `(landscapeId, sourceMembershipRef, targetMembershipRef, relationType, validFrom)`, plus mandatory `sourceVersionPin` and `targetVersionPin` (tag **and** commit **and** digest). An edge lacking either pin is state `unpinned` and is excluded from any answer labelled canonical; it still appears in the result as a gap. Edges reference memberships, not raw products, so an edge cannot outlive its membership.
- **Completeness:** every impact answer emits `traversal { startRefs, relationFilter, depthLimit, cyclePolicy }` and `limits { missingEdgeRefs, staleSourceRefs, unknownMembershipRefs, unpinnedEdgeRefs, confidence, completenessBoundary }`. An empty graph must return "unknown, zero coverage", never "no impact".

## Migration path

1. Freeze `0.1.0-legacy` with digest `sha256:7100…` as a non-installable historical record; do not edit it.
2. Open `0.2.0-draft` on the same id `vr.vercy.plmm`, sourced from immutable ref `a8e388c21901540b71cc8479d4d6ef119c2ea276`, recorded as commit + describe + content digest.
3. Project the eleven repo layers into `structure.bundles` (today `[]`), preserving layer numbering as stable ids.
4. Close the three gaps the legacy spec itself names: findings, questions, artifacts — plus `crud` and `roles`.
5. Add `requires: [AISMM @ pinned ref]` so federation is registry-visible rather than prose.
6. Resolve `ver-cy` vs `orkestron-ai` provenance with the owner before any canonical label.
7. Flip `installable` only after fixtures execute. Nothing in this dossier supports that flip.

## Invariants

1. **No product internals.** Membership/dependency records may hold refs, typed edges, ownership and criticality; any field that duplicates an AISMM bundle is a violation.
2. **Pinned versions.** Every dependency edge pins both endpoints to immutable refs; unpinned edges are visible and non-canonical.
3. **Visible incompleteness.** Absence is represented explicitly (unknown/not-applicable with reason); no silent empty result.
4. **Single product master.** One authoritative `productRef` per membership; duplicate product identities are rejected.
5. **Non-destructive lifecycle.** Withdrawals tombstone; recorded impact answers keep their `as_of` and coverage.

## Scenario walkthrough

**Negative — "legacy install is the canonical landscape."** Rejected. `installable: false`; `bundles: []` means `LandscapeMembership` and `LandscapeDependency` have no definitions to instantiate; `crud: {}` and `roles: []` mean no write authority or lifecycle exists; `migrationNotes` states findings, questions, artifacts, CRUD and roles are absent. The digest makes that emptiness reproducible, not correct. Calling it canonical would return empty impact graphs indistinguishable from "no impact" — violating invariant 3.

**Acceptance — three products + shared platform.** Four memberships (P1, P2, P3, Platform), each `productRef` + `aismmRef`, no new `SoftwareProduct`. Edges: P1 `depends_on` Platform (both pinned), P2 `consumes_from` Platform (both pinned), P3 `depends_on` Platform (`declared`, target pin missing). Query "change Platform": returns P1, P2 as pinned-confirmed; P3 as affected-but-unpinned; `limits` lists the missing pin, any stale source, and open questions ("which Platform revision does P3 consume?"). Impact graph plus visible gaps, product internals untouched.

## Gaps and publication holds

- No fixtures run; **no installability or compatibility claim** for PLMM or AISMM.
- AISMM pinned tree is 4 commits past v3.1.0; immutable-ref choice (tag vs `fe40e61`) undecided.
- No evidence linking runtime digests to repository commits.
- `requires: []` on both models: federation unproven in the registry.
- `ver-cy` vs `orkestron-ai` provenance unresolved.
- WM-XCT-039: `publishableCanonical: false`, single-provider waiver with Claude and Grok waived, nested schemas and adapters absent — unusable as a normative base; its composition targets `vr.wm-xct-001/003/037` are not in this dossier.
- `candidate_properties_from_v1` are `candidate-not-normative`.
- **ELMM appears nowhere in the dossier** despite being named in a blocking decision — its role cannot be decided here.
- Semantic crosswalk PLMM↔AISMM unverified; `published` ≠ independently reviewed.
