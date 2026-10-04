Verdict.

Accept. Neither GroupLandscape nor GroupScopeView needs an independent business-object ID. Landscape is a governed profile over WM-ORG-001 nodes and purpose-qualified WM-ORG-012 edges. ScopeView is an immutable generated projection identified by the digest of its pins and output. A statutory group with independent standing is a WM-ORG-001 organization, not a landscape.

Strongest evidence.

Landscape is a function of already-identified things: WM-ORG-001 nodes, purpose-qualified WM-ORG-012 edges, inclusion rules, and WM-XCT-040 pins. A new business-object ID would duplicate that composition and invite party, asset, contract, or authority roles the profile must not hold. ScopeView is determined by landscape revision, world time, knowledge time, scenario, graph rules, source revisions, grant set, and WM-XCT-003 shape. Digest identity is the content-address of those inputs and the projection. Membership never grants access only if the landscape is not an authority-bearing object. Catalog name plus profile revision is the operator handle; digest plus pin set is the citation handle.

Strongest counterexample.

A pre-incorporation joint holding or network steering body with officers, budget, and delegated rights. Operators will demand a durable key before legal standing exists. Wrong fix: mint Landscape as a business object and attach WM-XCT-001 authority. Right fix: if it has party or standing capacity, instantiate WM-ORG-001; if not, keep authority on existing organizations and use Landscape only as a governed perimeter profile. Near-miss: two purpose-different landscapes over the same nodes at one world time. A single group object would collapse them. The distinguisher is purpose set, profile revision, and pins.

Identity / mastership.

Mastership stays on existing objects. Existence and standing: WM-ORG-001. Each inter-org fact, purpose, owner, claimant capacity, and uncertainty type: WM-ORG-012. Authority, grant, disclosure: WM-XCT-001/002/003. Composition pin: WM-XCT-040. Landscape adds only participating graphs and rules, inclusion predicates, and who may revise the profile. It has no party role, asset-owner role, or contract capacity. A profile name is a label, not a surrogate key. ScopeView has no master; consumers cite digest and pin set. Identical pins must yield the same digest; any pin change yields a new digest. No update-in-place.

Boundary types.

Keep six parallel purpose-qualified graphs; do not union them into one membership: legal ownership/control; accounting consolidation; management; operational perimeter; brand affiliation; franchise/network participation. The same WM-ORG-001 pair may sit on franchise and brand graphs and be absent from consolidation and legal control. Access is not a seventh group graph; it is WM-XCT-002. Disclosure is WM-XCT-003. Crossing a landscape edge never implies grant or shape.

Uncertainty.

WM-ORG-012 edges carry typed unknown, disputed, and unverified statuses. Landscape retains every typed status, fact owner, and claimant capacity. It does not vote, merge, or drop competing claims. Incompatible edges on the same pair and purpose may coexist with distinct owners. ScopeView may hide a typed status only when bound graph rules or the bound WM-XCT-003 shape explicitly exclude it; that exclusion is visible in the pin. Silent collapse is forbidden.

Time / scenario.

Pins that travel together: world time, knowledge time, scenario, graph rules, source revisions, plus landscape profile revision. ScopeView digest also binds grant set and disclosure shape. The same nodes may occupy different perimeters at different world times, under different knowledge, or in different scenarios. A view missing any pin is invalid. Prior views remain immutable after any pin or source change.

Federation.

There is no shared group object to federate. Parties share WM-ORG-001 identities and WM-ORG-012 claims. Each party governs its own Landscape profile. Disagreement appears as typed disputed or unverified edges with distinct owners and capacities, not as a contest over one group ID. WM-XCT-040 pins a composition so a counterparty can reproduce a view without adopting the issuer’s landscape as master.

Access / projection.

Membership is not an access path. A ScopeView may include another organization’s facts only when each included fact is covered by an authorized WM-XCT-002 grant and reduced by a WM-XCT-003 shape. Distinct grant sets or shapes over the same landscape produce distinct digests. Holding consolidation facts do not leak to franchisees by membership; franchise operational facts do not leak to the holding by brand affiliation.

Scenario.

HoldCo H is WM-ORG-001. Legal-control graph: H→S1, H→S2, H→S3. Accounting-consolidation: H, S1, S2 only (S3 held-for-sale). Management: H, S1, and franchisee-operated F1 with no ownership. Operational perimeter: S1, S2, F2; S3 excluded. Brand: S1, F1, F2, F3. Franchise/network: H with F1, F2, F3; F3 unverified in one source and disputed in another — both types retained. Four landscapes over overlapping nodes, no union membership: L-legal {H,S1,S2,S3}; L-accounting {H,S1,S2}; L-ops {S1,S2,F2}; L-franchise {H,F1,F2,F3}. Consolidation ScopeView at world T, knowledge K, scenario Base projects H, S1, S2 only. S1 sees S2 consolidating totals only under grant and shape. Brand-reporting view pins a narrow shape so F1 cannot read F2 financials or PII. Changing franchise graph rules or dropping disputed F3 produces a new digest.

Invariants.

1. Neither GroupLandscape nor GroupScopeView has an independent business-object ID.
2. GroupLandscape is a governed profile revision, not a party, and has no contract, asset, or authority capacity.
3. GroupScopeView identity is the digest of pinned inputs and projection; identical pins yield the identical digest; no update-in-place.
4. A statutory or independently standing group is WM-ORG-001, not a landscape.
5. The six purpose graphs stay parallel and non-substitutable; no canonical member list is emitted.
6. Membership never implies WM-XCT-001 authority, WM-XCT-002 grant, or WM-XCT-003 shape.
7. Cross-organization facts in a view require grant and shape for each included fact.
8. Typed unknown, disputed, and unverified statuses, fact owner, and claimant capacity survive composition and projection unless bound graph rules or bound shape explicitly exclude them; exclusion is visible in the pin.
9. ScopeView digest pins landscape revision, world time, knowledge time, scenario, graph rules, source revisions, grant set, and disclosure shape.
10. Distinct grant sets or shapes over the same landscape produce distinct digests.
11. Federation shares WM-ORG-001 identities and WM-ORG-012 claims, not landscape identity.
12. Profile name is a label, not a surrogate party key.

Minimum profile shape (GroupLandscape).

Required: governed profile name/handle (not a business-object ID); profile revision; purpose set as a subset of the six graphs; referenced WM-ORG-001 set or inclusion predicate; referenced purpose-qualified WM-ORG-012 edges; uncertainty-retention rule; fact-owner and claimant-capacity passthrough; pin slots for world time, knowledge time, scenario, graph rules, and source revisions; governance of who may revise the profile; explicit membership≠access. Forbidden on the profile: party capacity, access grants, disclosure shapes, canonical membership across purposes.

Minimum view shape (GroupScopeView).

Digest; bound pins listed in invariant 9; generated node/edge projection; generation knowledge time; immutability. No independent business-object ID. No grants stored on the view.

Blockers.

B1 assigning independent business-object identity to Landscape or ScopeView. B2 attaching party capacity, contracts, assets, or WM-XCT-001 authority to a landscape. B3 treating membership as an implicit grant or shape. B4 collapsing the six purpose graphs into one member list. B5 silent drop of typed unknown, disputed, or unverified edges. B6 generation missing any required pin. B7 storing grants or shapes on the ScopeView. B8 using profile name as a surrogate party key in ledgers or contracts. B9 cross-organization projection without an authorized grant-and-shape pair. B10 promoting Landscape to WM-ORG-001 because a cluster is convenient to name.
