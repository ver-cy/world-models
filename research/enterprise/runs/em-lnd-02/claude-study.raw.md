## Verdict

EM-LND-02 mints no new model ID. **GroupLandscape** is a *governed profile* over WM-ORG-001 + WM-ORG-012: a versioned definitional artifact holding boundary-kind vocabulary, per-kind graph rules, and disclosure classes. It has profile-version identity only, no instance identity. **GroupScopeView** is a *deterministic projection*: an immutable, digest-identified generated artifact. Its digest is artifact identity, not business identity — it does not become an aggregate. This matches EM-ORG-01 (enterprise group as purpose-qualified profile over WM-ORG-012) and EM-LND-01 (landscape as projection, axis as profile construct, snapshot as generated artifact).

Escalation test for independent identity: a group acquires it only when it bears standing, obligations, statements or succession that cannot attach to members or memberships. When that happens — a registered VAT group, a statutory umbrella — the correct home is a WM-ORG-001 subject with `formality_class = umbrella-of-legal-entities` plus WM-ORG-010 registration records, **not** a GroupLandscape type. WM-ORG-001 forbids using statistical enterprise-group boundaries to merge or split organization records; a landscape must not become a back door to that.

## Evidence

WM-ORG-001 supplies the endpoint subject: identity, formality spectrum, legal personality flag, naming with trading names, affiliation distinct from control (`q-affil-distinct`), statistical-unit alignment with its prohibition, and the Eurostat global-decision-centre question. WM-ORG-012 supplies the membership record: source-qualified relationship identity, kind with exclusions, direction, arity, scope, control basis, interest quantifier, valid/knowledge time, graph rules with cycle and self-link policy, explicit derivation with `inputRefs`/`asOf`/`ruleVersion`/`outputKind`, and `graphLoss`. WM-ORG-001's own adjudication names the ownership layer as the seam to re-test once a relationship sibling is registered. WM-ORG-012 is now that sibling, so the seam is live and must be cut here.

## Identity/mastership

WM-ORG-012 masters relationship kind, direction, endpoint roles, scope, periods, control basis, interest and dispute. WM-ORG-001 retains only organization-side derived indexes and its own reporting exceptions. The landscape reads WM-ORG-012 as master; if it reads WM-ORG-001's endpoint fields as primary it will double-count and mis-attribute consolidation. Blocking: the registry records `parent_ids: WM-ORG-001` for WM-ORG-012 while its specification declares WM-ORG-001 a REFERENCE boundary. A relationship cannot be structurally owned by one endpoint; EM-ORG-01 and EM-ORG-02 flagged this and it remains unresolved.

## Boundary types

Eight parallel scoped graphs, each with its own kind code, definition URI, jurisdiction and rules. None defaults from another.

1. **Legal ownership/control** — WM-ORG-012 `controlBasis` equity/votes/other, quantified with denominator, class, asOf, uncertainty; direct/indirect with component records; prohibited inferences named.
2. **Accounting consolidation** — RR-CDF direct/ultimate consolidating parent with accounting standard and accounting period. Not ownership: both bases record this as an irreconcilable conflict.
3. **Management boundary** — decision-centre assertion, largely self-declared, no register vocabulary. Lowest assurance; must carry claimant capacity.
4. **Operational service perimeter** — WM-ORG-011 presence, site bindings, local activity, service availability. Asserts no legal standing.
5. **Brand/trade-name affiliation** — WM-ORG-001 trading names plus affiliation type. Confers nothing; trademark rights are an explicit WM-ORG-001 omission.
6. **Franchise/network participation** — affiliation + WM-ORG-012 recognition basis and collaboration scope. WM-ORG-001 records franchise networks as weakly covered.
7. **Security trust** — no owner in either base. WM-ORG-001 declares security a deliberate gap. Record as an unowned axis, not a modelled kind.
8. **Data-sharing authorization** — not a group boundary at all: WM-XCT-002 grants per object, shaped by WM-XCT-003.

## Membership and uncertainty

Every membership carries boundary kind and purpose, member and role refs, valid and knowledge time, recognition/control basis, governing instrument, evidence with retrieval context and validation, claimant capacity and counterparty position, master and steward with review date. Unknown is typed, never null: WM-ORG-012 `absence` gives reason, coverage scope and search time; WM-ORG-001 gives eight GLEIF reporting-exception reasons for an unreportable parent plus BODS unspecified-party reasons, under its "absence is data" policy separating unknown, not-applicable, suppressed and pending. Disputed owners persist as coexisting attributed claims with a resolution authority and status; no recency-wins. Unverified owners keep their assurance grade rather than being promoted. A disputed edge is neither an edge nor an absence — it is a contested set.

## Time and scenarios

Two clocks, never fused. World time is the relationship's effective interval with precision and uncertainty; knowledge time is observed/recorded/published with supersession. A view pins boundary kind, `as_of_world`, `as_of_knowledge`, root, depth, graph rule-set version and input revisions, and is refused when any source cannot reconstruct the requested horizon. Publisher record closure is not real-world termination. Scenario stays non-normative: neither base supports branching, so `scenario` defaults to `authoritative`, scenario facts never mix with authoritative facts, and EM-LND-01's constraint carries forward unchanged.

## Federation

Fact owners survive projection. The landscape has no write path: corrections go to WM-ORG-001 or WM-ORG-012. Each view records, per edge, the mastering system, steward, asserting party and capacity, so a parent's claim of control over a subsidiary is visibly the parent's claim rather than the subsidiary's record. Derived edges are labelled with inputs, asOf, rule version and output kind, and are never merged with asserted edges. Pinning follows WM-XCT-040: exact revisions, digests, no in-place mutation of a released view.

## Access and projection

Membership is never a grantor. WM-XCT-001 requires a grantor of record to hold live control, mandate, stewardship or capacity authority; WM-XCT-002 denies by default and verifies grantor authority against that record; WM-XCT-003 governs only the leaving shape — element selection with default-deny, per-element treatment, grain class, compiled template and fingerprint, bound to target and audience by reference. A parent reads subsidiary data only under a subsidiary-granted contract with declared purpose, scope, duties and revocation with entitlement cutoff. Group-level figures travel as `aggregate_only` with a WM-XCT-005 cohort-floor reference. The negative case fails three times: brand is not control, affiliation is not a control modality, and no grant exists.

## Holding/franchise scenario

**Holding:** ownership graph (55% equity, indirect chain via component records), consolidation graph (ultimate consolidating parent under a named standard and period), management graph (decision centre). A 55%-held entity deconsolidated under that standard appears in ownership and not consolidation — the perimeters legitimately disagree. An unknown ultimate parent is an exception-coded edge. Projection: aggregate consolidated measures plus narrowly scoped subsets where a shareholder basis is evidenced.

**Franchise:** brand-licence and network-participation edges only; no control edges inferred; each franchisee a separate subject with its own presence and outlets. The franchisor's operational perimeter covers only outlets it operates. One franchisee's membership is contested and shows as a dispute. Projection: per-franchisee grants; brand licence yields no read right. Both perimeters share members without sharing rules.

## Invariants

1. Control and brand shown separately; no inference either way.
2. Unknown link is typed, never null.
3. Federation preserves fact owners; no remastering.
4. Boundary kind mandatory, versioned, never defaulted.
5. Perimeter confers no authority; membership is never a grantor.
6. Derived edges labelled and never merged with asserted.
7. Cardinality and cycle rules per kind and interval, not over the union.
8. No landscape write path.
9. Statistical or consolidation units never merge or split organization masters.
10. Disputed claims coexist until an authorized resolution.
11. Views immutable, digest-identified, non-reimportable.
12. Cross-organization projection requires per-object grant plus shape.

## Minimal profile shape

`profile_id`; `boundary_kind` + `kind_scheme_version` + `purpose` (replacing free-text `boundary_basis`); `as_of_world` and `as_of_knowledge` (replacing single `as_of`); `consolidation_policy` admissible only when kind is accounting consolidation, and as a reference to standard plus accounting period rather than text; `scenario` retained as a non-normative label defaulting to authoritative; plus `root_refs`, `depth`, member refs with roles, WM-ORG-012 edge refs, `graph_rule_set_version`, `disclosure_class`, input revision pins, `output_digest`, and a gap/conflict register.

## Holds

Both bases are reviewable drafts with `publishableCanonical: false`. WM-ORG-012 is a single-provider waiver — both external providers timed out, its self-audit is not independent review, it has no executable nested schema and no multi-party or cyclic graph fixtures, and its BODS "latest" alias and historical GLEIF 2.8.5 pins are unverified. Its crosswalk evidence is only index-and-publication metadata. The registry `parent_ids` conflict is unresolved. Franchise networks are a declared WM-ORG-001 weakness; trademark rights and security are declared omissions; the security-trust axis has no owner. Pairwise export of multi-party arrangements loses membership context. Nothing here claims canonical completeness or installability.
