# Independent review request: EM-ORG-01 Company and Enterprise Group

Review this Enterprise boundary independently using public organization, legal-entity, corporate-group, consolidation, beneficial-ownership, statistical-enterprise and franchise practice where useful. Separate standards evidence from design inference. Do not invent a Vercy identifier.

Current bases:

- WM-ORG-001 Organization is a non-canonical reviewable draft for an externally addressable actor and its identity/lifecycle. It already distinguishes organization, legal category, statistical alignment, names, succession and organization-side relationship endpoints.
- WM-ORG-012 Inter-organizational Relationship is a non-canonical reviewable draft for source-qualified, temporal, scoped organizational relationships, including multi-party context. It lacks independent external review and executable fixtures.

Proposed decision: **PROFILE**, no new ID. Company is a constrained WM-ORG-001 view. EnterpriseGroup/BusinessBoundary is a purpose-qualified WM-ORG-012 profile whose members reference WM-ORG-001.

Every membership must carry boundary kind and purpose, endpoint roles, valid/knowledge time, recognition or control basis, evidence, claimant authority, master/steward and dispute/absence status. Management, consolidation, ownership/control, statistical, franchise and alliance perimeters coexist as separate graphs. A materialized perimeter is a reproducible as-of query over membership facts.

WM-ORG-012 should master relationship kind, period, direction, quantifier and control/interest facts; WM-ORG-001 retains derived endpoint indexes and organization-side reporting exceptions. Challenge the current registry parent claim from WM-ORG-012 to WM-ORG-001.

Test: three organizations share one brand; they must not collapse into one identity or legal entity. A franchise network and a holding/consolidation group must produce different graphs, and rebranding must preserve organization identity.

Return at most 1000 words with: Verdict; company identity test; group identity/lifecycle test; membership/perimeter contract; mastership seam; brand/rebranding/succession rules; scenario results; split trigger for a true group subject; required constraints; publication blockers.
