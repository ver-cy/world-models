# Independent review request: EM-LND-06 Software Product Landscape

Review this Enterprise metamodel boundary independently. Use public software portfolio, enterprise architecture, configuration/knowledge graph and impact-analysis practice where useful. Separate standards evidence from design inference. Do not invent a Vercy identifier.

Frozen evidence:

- Existing reserved runtime `vr.vercy.plmm` is `0.1.0-legacy`, non-installable, and structurally empty (`bundles`, CRUD, roles and policies absent).
- The pinned PLMM repository draft at commit `a8e388c21901540b71cc8479d4d6ef119c2ea276` has eleven substantive landscape layers and says product internals stay in AISMM.
- AISMM is a per-product model. Frozen runtime and README both say 3.1.0, but the pinned repository tree is four commits past tag `v3.1.0`; runtime-digest-to-commit compatibility is unproven.
- WM-XCT-039 is a narrower tenant-scoped managed IT service graph and remains `publishableCanonical: false` with nested schemas/adapters absent.

Proposed decision: **COMPLETE RESERVED MODEL** on `vr.vercy.plmm`; preserve `0.1.0-legacy` unchanged and open a new draft version. No second model ID and no second SoftwareProduct.

Proposed ownership:

- `SoftwareLandscape`: identity, scope, architecture state and `asOf`.
- `LandscapeMembership`: one authoritative external `productRef`, pinned `aismmRef`, validity, assertion kind, confidence and source.
- `LandscapeDependency`: typed directed edge between memberships with immutable endpoint pins.
- completeness and reproducible impact-query results, including missing/unpinned/stale/unknown limits.

Product internals remain AISMM-owned. WM-XCT-039 may inform a managed-service projection but is not a base dependency while held.

Test: three products use one shared platform. Two dependency edges are fully pinned; the third lacks a target version. A platform-change query must return the two confirmed paths, keep the third visible as affected-but-unpinned, and emit gap questions. An empty graph must mean unknown/zero coverage rather than no impact.

Return at most 1000 words with: Verdict; identity/lifecycle test; ownership boundary; membership and dependency keys; temporal/version semantics; completeness contract; scenario walkthrough; required fields/relations; migration from legacy; publication blockers.
