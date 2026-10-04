**Verdict.** PROFILE over WM-ORG-001 and WM-ORG-012. No new catalogue or runtime ID. Company is a constrained 001 view. EnterpriseGroup / BusinessBoundary is a purpose-qualified 012 profile whose members reference 001. BrandAssociation is a relationship or name-form fact, not an identity. Legal personality stays on the EM-ORG-02 neighbor; ownership shares stay on EM-ORG-03. This is standards alignment, not a GLEIF, IFRS 10 or Eurostat conformance claim.

**Company identity test.** Source facts: 001 already masters externally addressable organization identity, name forms (legal, trading, former), legal-form / personality flags, statistical-unit alignment and succession. Card parks legal personality and ownership shares on neighbors. Dates, names and addresses are never keys. Many organizations are not legal entities; some umbrellas contain several.

Company does not mint a second identifier. The PROFILE constrains a 001 subject as a commercial actor: trading-name set in force, optional statistical-enterprise alignment, legal-personality flag referenced from EM-ORG-02 rather than copied. Business and legal entity coincide as *one object* only when that 001 subject also has an EM-ORG-02 registration with separate legal personality; they remain two aspects. Informal collectives stay 001 without being companies-as-legal-persons.

Fail-to-new-ID if Company copies registry attributes, treats a trading name as the key, or collapses three same-brand actors into one legal entity.

**Group identity / lifecycle.** EnterpriseGroup / BusinessBoundary is a named perimeter specification plus a generated as-of view, not a third organization. Identity: `(perimeter-id, boundaryKind, purpose, spec-version)` over the 012 membership-fact set it evaluates. Lifecycle versions the specification (which kinds count, which roles, which control basis, as-of policy). It does not mint 001 identities for “the group as actor” unless an independent constitutive organization already exists — a listed holding is already a 001 subject; the consolidation graph *around* it is the perimeter.

A materialized perimeter is a reproducible query at one `(valid-time, knowledge-time)` pair. Same pins produce the same member set. It is not a stored second master of the members and does not become owner of member facts (card invariant).

**Membership / perimeter contract.** GroupMembership is a 012 relationship under a named purpose. Every fact must carry:

1. `boundaryKind` + `purpose` ∈ {management, consolidation, ownership-control, statistical, franchise, alliance} (extensible; not a merge key).
2. Endpoint roles scoped to that kind.
3. `validTime` and `knowledgeTime`; inclusion date mandatory.
4. Recognition or control *basis* — accounting standard + consolidation class; equity / votes / contract / de facto; statistical-authority mapping; franchise instrument; alliance instrument. Basis is not inferred from brand or from another kind.
5. Evidence and claimant authority.
6. Master / steward of *this relationship* (012), distinct from endpoint mastership (001) and from 02 / 03.
7. Dispute / absence / reporting-exception status (GLEIF-style “no parent / opt-out / unknown” remains first-class).

One organization may sit in many perimeters. Graphs are not unioned before evaluation. A materialized “the group” without a declared kind is refused.

**Mastership seam.** 012 masters relationship kind, period, direction, quantifier, control / interest facts, evidence, claimant and dispute. 001 retains identity, names, succession, statistical alignment, derived endpoint *indexes* and organization-side reporting exceptions.

Challenge the registry parent 012 → 001. A relationship is not a subtype of an organization. W3C ORG membership / `org:linkedTo` relate Organizations; they are not child types. GLEIF RR-CDF is a separate record from Level 1 identity. Demote PARENT to REFERENCE (composition of endpoints only). 012 cites two or more 001 identities; it does not inherit names or legal personality. 001’s current consolidation endpoint fields become derived projections of 012 edges, not a second write path. Dual-write of the same consolidating-parent fact is a blocker until 012 is named master of that fact. Ownership *shares* remain EM-ORG-03.

**Brand / rebranding / succession.** BrandAssociation is `{orgRef, mark, role, validity, source}`. It does not prove control (card invariant; IFRS 10 alignment: typical franchise rights protect the brand, they do not confer power over returns). Rebranding updates 001 name forms with identity-continuity true; former names stay citable. Sale or split uses 001 succession plus 012 membership close / open with inclusion dates. Brand edges may persist across a sale if the mark transfers; that does not merge successor with predecessor. Statistical-enterprise alignment on 001 blocks silently merging legal units into “the company.”

**Scenario results.**

1. *Three organizations share one brand.* Three 001 identities remain. BrandAssociation edges connect each to the mark. No control or consolidation edge is inferred. Auto-merge into one legal entity fails the negative case.

2. *Franchise network versus holding / consolidation group.* Franchise graph: kind = franchise / affiliation; basis = licence; purpose = brand-system; control = false unless separately evidenced. Holding graph: kind = control / consolidation; basis = accounting standard + interest; purpose = consolidation; GLEIF L2 analogue. Management graph: kind = direction; basis = mandate; purpose = management. Three queries over the same store yield three graphs. A brand-only member does not appear in the consolidation perimeter.

3. *Rebranding of one franchisee.* 001 identity unchanged; former name retained; BrandAssociation may update. Holding perimeter unchanged unless a control fact also changed.

**Split trigger for a true group subject.** Mint a group-as-actor only if all hold: (1) an identifier that is not any member’s 001 id and not a query digest (register-issued enterprise-group number that outlives particular edges); (2) obligations or legal capacity that are not those of any member and not EM-ORG-02; (3) other models must master the group without going through 012. Today none are proven. That actor would still be a **001 instance**, not a new catalogue type; membership graphs stay 012. Eurostat “enterprise group” can be the *result* of a purpose = statistical query over control links.

**Required constraints.** Company = 001 profile, not a second identity. Every membership carries kind, purpose, roles, bitemporal interval, basis, evidence, claimant, steward, dispute / absence. Do not infer control from brand. Do not union perimeters. 012 REFERENCE 001, not PARENT. Perimeter does not own member facts.

**Publication blockers.** Both bases are non-canonical reviewable drafts; 012 lacks independent review and executable fixtures. 012 has no franchise kind and no named perimeter-profile object — PROFILE fields, not new IDs. 001 still writes ownership / control endpoints pending the sibling-seam retest it already declared. Dual-write of consolidating-parent facts is unresolved. No fixtures for three-org brand non-merge, franchise ≠ holding, rebranding continuity, or as-of reproducibility with reporting exceptions. Alignments to GLEIF L2, IFRS 10, W3C ORG and Reg. 696/93 are alignments only. Do not invent Company, EnterpriseGroup or BrandAssociation runtime identifiers.
