**Verdict.** COMPLETE RESERVED MODEL on existing runtime `vr.vercy.plmm`. Preserve `0.1.0-legacy` byte-identical and non-installable. Open a new draft version on the same identifier. No second model ID. No second SoftwareProduct. Product internals remain AISMM-owned. WM-XCT-039 is not a base dependency while held. This is standards alignment, not a new product register.

**Identity / lifecycle test.** Frozen evidence: the reserved runtime is structurally empty (no bundles, CRUD, roles or policies). The catalogue page retains it as a reference while a catalogue-native specification is completed. The pinned PLMM draft at `a8e388c21901540b71cc8479d4d6ef119c2ea276` has eleven landscape layers and states that internals stay in AISMM. EM-TEC-01 already forbids a second product and requires a single owner of internal facts. ISO 42010 / ArchiMate alignment: a landscape view is not a second architecture of the product.

- **SoftwareLandscape.** Identity: landscape-id + spec version + perimeter + architecture-state + `asOf`. Lifecycle versions the spec and generated impact results. It does not mint products. Fail if it stores AISMM internals or if a membership row is treated as a product master.

- **LandscapeMembership.** A reference record. Key: `(landscape-id, productRef, aismmRef)` plus validity interval. `productRef` is one authoritative external product identity (WM-SFT-001 and/or the product’s AISMM passport). One membership per product per landscape per interval. Two `aismmRef`s for one `productRef` at overlapping validity → `unresolved`, not two products. Fail if membership mints a local SoftwareProduct or copies components, SBOMs, APIs or owners.

- **LandscapeDependency.** Typed directed edge between memberships, not between raw product ids. Key: `(fromMembership, toMembership, dependencyType, fromPin, toPin)`. Endpoint pins are immutable. Changing a pin is a new edge. An unpinned target is a first-class state, not a missing row.

Regional deploy, runtime instance and AISMM repository are not products.

**Ownership boundary.** PLMM owns landscape identity, membership references, typed inter-product edges, completeness status and reproducible impact-query results. AISMM owns per-product internals. WM-SFT-001 remains the catalogue product aggregate. The eleven draft layers are internal structure of the new `vr.vercy.plmm` version, not eleven new catalogue IDs. Layers beyond the three types (capabilities, operations, governance, change, trust) are projections of memberships and dependencies plus external references. WM-XCT-039 may later inform a managed-service projection; it is tenant-scoped, `publishableCanonical: false`, and lacks nested schemas/adapters, so it is REFERENCE-optional at most.

**Membership and dependency keys.** Membership requires `productRef`, `aismmRef` (version **and** content digest; commit if used), validity, assertion kind (`observed` | `declared` | `inferred`), confidence and source. Unpinned `aismmRef` is an explicit gap, never silent “latest.” Dependency requires type (`uses-platform`, `integrates`, `data-flow`, `event`, `runtime-shared`), membership endpoints and immutable pins `{membership-id, productRef, aismmRef, recorded-at}`. Internal package dependencies stay in AISMM. Pin states: `pinned-current`, `pinned-stale`, `target-unpinned` / `source-unpinned`, `missing`. Unpinned ≠ absent ≠ no impact.

**Temporal / version semantics.** Landscape `asOf` is the query instant. Membership validity is the assertion interval. Pins are write-time facts. A later AISMM revision does not rewrite an edge; the old pin becomes stale relative to `asOf`. Do not float to latest AISMM. Runtime 3.1.0, the tree four commits past tag `v3.1.0`, and any 3.2 README label are not proven digest-compatible; that is why pins carry digest, not a version label alone.

**Completeness contract.** Every impact result is reproducible from `(landscape-id, asOf, pinned membership+dependency set, query seed)` and returns three parts: confirmed paths; qualified paths (unpinned, stale, missing); gap questions. Coverage class ∈ {`unknown` | `zero` | `partial` | `complete`}. Empty graph means unknown or zero coverage, not “no impact.” An empty `0.1.0-legacy` install must not be read as “nothing depends on this platform.”

**Scenario walkthrough.** Products P1, P2, P3 and platform F. Edges P1→F and P2→F fully pinned. Edge P3→F lacks target version. Platform-change query at `asOf` *t*: return P1 and P2 as confirmed paths with pins; keep P3 visible as affected-but-unpinned; do not invent a version and do not drop the edge; emit gap questions (which F version/digest does P3 bind? is P3’s `aismmRef` stale? what is landscape coverage at *t*?). No second SoftwareProduct is created for F or any Pi. If the landscape had no memberships, the result is unknown coverage, not “no dependents.” Declaring the empty reserved runtime a finished canonical landscape fails this test and the card negative case.

**Required fields / relations** (named on the completed reserved model, not new IDs): landscape `{id, scope, architecture-state, asOf, composition-version, coverage-status}`; membership `{productRef, aismmRef{version,digest}, validity, assertionKind, confidence, source}`; dependency `{type, from, to, fromPin, toPin, pinState}`; impact result `{confirmed[], qualified[], gap-questions[], coverage-status}`.

**Migration from legacy.** Keep `0.1.0-legacy` unchanged and non-installable. No instance data migrates (there is none). Consumers receive a documented successor pointer, not an implicit upgrade. The repo “v0.2.0” label at commit `a8e388c…` is evidence, not an automatic runtime version. Assign the new runtime version only after bundles, CRUD, roles, policies and completeness fixtures exist, with that commit’s digest pinned.

**Publication blockers.**
- Runtime-digest-to-commit compatibility for AISMM 3.1.0 versus the post-tag tree is unproven; membership pins cannot claim a single AISMM coordinate until that hold is explicit.
- `0.1.0-legacy` must not be marked installable or canonical.
- WM-XCT-039 remains held; do not make it a required composition edge.
- WM-SFT-001 ↔ AISMM “no second product” resolution lives on EM-TEC-01 and is still queued.
- No fixtures yet for unpinned-edge retention, empty-graph = unknown coverage, or stale-pin non-retargeting.
- Alignments to ISO 42010, ArchiMate and SBOM/PURL practice are alignments only.
- Do not invent a second PLMM identifier or a landscape-local SoftwareProduct.