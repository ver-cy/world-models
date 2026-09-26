# EM-LND-06 local synthesis

## Disposition

- Complete the existing reserved model `vr.vercy.plmm` as **Software Product Landscape** on a new version line.
- Keep `0.1.0-legacy` immutable and non-installable; do not create a second runtime/model identifier.
- Treat WM-XCT-039 as an optional managed-service projection reference, not as PLMM's base or replacement.

## Boundary

PLMM owns landscape identity and scope, temporal product membership, typed product-to-product dependencies, completeness statements and reproducible impact-query results. Products and their internals remain external masters, normally resolved through pinned AISMM references. PLMM must never copy requirements, architecture, code, deployment or runtime facts from a product model.

`LandscapeMembership` identifies an assertion that a product participates in a landscape. It references one authoritative `productRef` plus a pinned `aismmRef`, and records validity, assertion kind, confidence and source. `LandscapeDependency` connects memberships rather than raw products and pins both endpoint versions. Withdrawals are tombstones so historical impact results remain explainable.

WM-XCT-039 covers a narrower tenant-scoped managed IT service graph. Its service/asset mastership, tenant isolation and projections stay outside PLMM. No composition dependency is asserted while WM-XCT-039 remains non-canonical and its nested schemas are absent.

## Completeness and impact

Every impact result declares its start nodes, relation filter, depth limit, cycle policy and `asOf`. It also reports missing edges, stale sources, unknown memberships, unpinned endpoints, confidence and the boundary beyond which completeness is unknown. An empty graph means zero observed coverage, not zero impact.

## Invariants

1. One authoritative product identity is referenced per membership; PLMM never creates a second SoftwareProduct.
2. Product internals are referenced, not copied.
3. Every canonical dependency pins both endpoints to immutable tag, commit and digest evidence.
4. Unpinned or stale edges remain visible but are excluded from canonical answers.
5. Membership and dependency withdrawal is non-destructive.
6. Every impact answer exposes its coverage limits and evidence time.
7. Scenario or inferred edges cannot silently become authoritative observations.

## Acceptance result

For three products and one shared platform, four memberships reference the existing product masters. Two pinned edges produce confirmed impact paths. A third edge with a missing target pin remains visible as affected-but-unpinned, and the answer asks which platform revision it consumes. The query therefore returns a useful graph plus explicit gaps without duplicating any product.

## Version reconciliation and migration

The frozen AISMM evidence consistently labels version 3.1.0; the earlier 3.2 README question is stale. Its repository tree is four commits past the `v3.1.0` tag. The candidate does not impose either ref globally: every membership must pin the exact product-context commit and content digest it actually uses, and a tag is descriptive evidence only. PLMM's repository is frozen at commit `a8e388c21901540b71cc8479d4d6ef119c2ea276` with a canonical digest over the eleven layer documents, while the runtime `0.1.0-legacy` projection remains immutable.

Migration freezes the legacy artifact and opens `0.2.0-candidate.1` on `vr.vercy.plmm`. The candidate projects the eleven repository layers into stable bundle IDs and defines membership, dependency, completeness and impact-query semantics. Seven fixtures cover confirmed impact, missing pins, empty coverage, withdrawal history, cycles, scenarios and restricted evidence. Package conversion and live runtime/search verification remain publication work.

## Holds

Provenance differs between the historical `ver-cy` runtime source and the `orkestron-ai` repository links. The legacy digest is preserved without claiming it maps to the repository commit. The candidate now provides explicit federation and fixture semantics, but exact Grok comparison, one frozen semantic audit and package/live verification remain required. The checkpoint is not yet a canonical release.
