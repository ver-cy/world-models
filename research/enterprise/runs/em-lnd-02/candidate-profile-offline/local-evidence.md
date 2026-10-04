# EM-LND-02 local synthesis

## Disposition

- Define Group Landscape as a governed profile over WM-ORG-001 Organization and WM-ORG-012 Inter-organizational Relationship. It has profile-version identity, not business-object identity.
- Define Group Scope View as an immutable generated projection with digest and pinned inputs. It is not an aggregate and cannot be re-imported as source truth.
- A group receives WM-ORG-001 identity only when it independently bears standing, obligations, statements or succession, such as a registered statutory umbrella; the landscape never creates that identity.
- Allocate no new runtime/model identifier.

## Identity and mastership

WM-ORG-001 masters organization subjects. WM-ORG-012 masters relationship kind, endpoints and roles, scope, control basis, quantified interest, valid/knowledge time, evidence, dispute and derivation. The landscape reads these masters and has no write path. Corrections return to the owning source.

The WM-ORG-012 registry parent assignment conflicts with its specification's reference boundary: a relationship cannot be structurally owned by one endpoint. This must be resolved before publication.

## Boundary types

The profile keeps parallel graphs for legal ownership/control, accounting consolidation, management boundary, operational service perimeter, brand/trade-name affiliation and franchise/network participation. Security trust remains an unowned axis. Data-sharing authorization is never a group boundary; it remains a WM-XCT-002 grant shaped by WM-XCT-003.

Each boundary kind has its own definition/version, purpose, jurisdiction, direction, arity, graph rules, evidence threshold and disclosure class. No boundary is inferred from another. Brand does not imply control; ownership does not imply consolidation; consolidation does not imply operational control.

## Membership, uncertainty and time

Membership references a governed relationship and records member role, recognition/control basis, governing instrument, evidence, claimant capacity, counterparty position, master, steward and review date. Unknown, not applicable, suppressed and pending are distinct. Disputed or competing claims coexist with attribution and resolution authority; recency does not resolve them.

A view pins world-time and knowledge-time horizons separately, root, depth, boundary kind, graph-rule version, input revisions and scenario. It is refused when sources cannot reconstruct the requested horizon. Scenario defaults to authoritative; hypothetical facts never mix with authoritative facts because the base models do not support branching.

## Federation and projection

Every output edge preserves its mastering system, steward, asserting party, capacity and evidence. Derived edges retain input references, as-of, rule version and output kind and remain visibly separate from asserted edges. Released views are immutable and reproducible through WM-XCT-040 pins and digest.

Group membership never grants access. A parent reads subsidiary facts only through a grant from the authorized fact controller, with purpose, scope, duties and revocation in WM-XCT-002 and a least-disclosure shape in WM-XCT-003. Aggregate views reference cohort/privacy controls where needed.

## Acceptance scenario

A holding has separate ownership, accounting-consolidation and management graphs. A 55%-owned company that is deconsolidated appears in ownership but not consolidation. An unknown ultimate owner remains an exception-coded unknown. A franchise network has brand and participation edges only; no control is inferred, each franchisee remains a separate fact owner, and data access requires per-franchisee grants. The two landscapes can share organizations while preserving different perimeter rules.

## Invariants

1. Control, consolidation, management, operations, brand and franchise remain separate boundaries.
2. Boundary kind and version are mandatory and never defaulted from another graph.
3. Unknown links are typed facts, never null or zero.
4. Disputed claims coexist until authorized resolution.
5. Federation preserves fact owners and claimant capacity.
6. Derived and asserted edges never merge silently.
7. Graph rules apply per kind and interval, not to the graph union.
8. The landscape has no write path to organization or relationship masters.
9. A view pins world time and knowledge time separately.
10. Scenario facts never mix with authoritative facts.
11. Membership never creates authority or access.
12. Cross-organization disclosure requires a valid grant and governed shape.
13. Views are immutable, digest-identified and non-reimportable.

## Minimal profile shape

The profile records profile id/version, boundary kind and scheme version, purpose, world/knowledge as-of, authoritative-or-hypothetical scenario, roots/depth, member and WM-ORG-012 edge references, graph rules, disclosure class, input revision pins, output digest and gap/conflict register. Accounting policy appears only on accounting-consolidation views as a reference plus reporting period.

## Holds

WM-ORG-001 and WM-ORG-012 remain non-canonical reviewable drafts; WM-ORG-012 lacks independent provider review and executable relationship/graph fixtures. Its registry parent conflicts with its reference boundary. Franchise semantics, security trust, trademark rights and some external source pins remain incomplete. Multi-party relationships lose context in pairwise export. This checkpoint makes no canonical completeness, installability or publication claim.

## Grok reconciliation and frozen-audit remediation

Grok confirmed the no-new-ID disposition and required the view digest to bind authorization and disclosure pins. The frozen Claude audit accepted the result with limits and identified five specification gaps. The candidate now makes landscape revision handles and view digests non-registrable artifact identifiers; business objects may cite them only as evidence. The profile revision masters graph and uncertainty propagation rules, while WM-XCT-040 masters the immutable composition pin package. The digest also binds the composition rule and engine revision.

Grant-set and disclosure-shape pins resolve to retained immutable revisions so later revocation changes current entitlement without destroying historical verification. Every emitted cross-organization fact, including membership edges, requires an authorized disclosure basis and governed shape. These changes preserve the profile disposition and allocate no runtime/model identifier.
