# EM-COM-01 provider review and adjudication

Date: 2026-09-22. These are independent design reviews, not execution or standards-conformance evidence.

## Claude Opus 5 High

Mode: Claude CLI, `--tools ""`, high effort. Verdict: **PROFILE (conditional)**.

Claude rejected `REUSE ONLY` because WM-ORG-014 and WM-ORG-015 are direction-specific authorities and neither owns the cross-role Party view, purpose/time-qualified contact assignment or sourced segmentation. It rejected `NEW MODEL` because all proposed records are bindings or assertions and must not remaster Party, relationship or endpoint identity.

Key corrections:

- One `CounterpartyRelationshipSet` per Party, initially proposed globally; no key by role or account scope.
- Customer binding must point to WM-ORG-014; supplier and partner bindings to WM-ORG-015. Reseller/channel partners remain 015-side even when commercially customer-shaped.
- No independent relationship status; derive it from active upstream bindings.
- No copied Party name, tax ID, address or hierarchy except a clearly non-authoritative display cache.
- Upstream bindings carry exact referent/version or `asOf` evidence.
- `AccountScopeBinding` references an existing account/legal entity/group and never creates scope or derives group membership.
- `ContactAssignment` references an existing endpoint and never creates one or grants permission to contact.
- Segmentation is append-only, source/scheme/version/method/time-qualified classification.
- Party identity mastership is a blocking dependency: this profile cannot repair split Party masters.

Claude recommends WM-PER-010 as sole party-endpoint authority for this profile and constrains endpoint refs to it. WM-XCT-024 may be a projection or technical/non-party channel model, with any crosswalk owned outside this profile. Strong fixtures cover tri-role Party, group-vs-legal-entity scope, shared endpoint with revoked consent, conflicting versioned segment assertions, and simultaneous relationship supersession plus endpoint merge.

## Grok Heavy

Conversation: https://grok.com/c/ced007cc-11d1-4608-a373-1a85ed425b04

Verdict: **PROFILE**. Grok used its own multi-agent research pass, inspected the Vercy public briefs/specifications and explicitly made no execution or standards-conformance claim.

Grok agrees with the five owned profile records and adds two important constraints:

- Cardinality is one set per `(Party × observing Dimension)`, rather than one global set per Party. Different observing enterprises must not collide.
- WM-ORG-014 `customer-contact-record` is relationship-intent/assignment source only after composition; it is not an endpoint store.

Grok treats the WM-PER-010 versus WM-XCT-024 conflict as still open at the source. EM-COM-01 must not silently resolve it or become a third authority. For this profile, party endpoint values, normalization, verification and consent references resolve through WM-PER-010; WM-XCT-024 may describe a channel shape or non-party subject. The open conflict must remain a publication hold rather than a frozen assertion that the registry conflict has been settled.

Grok also identified related authorities that the profile may reference without importing: WM-XCT-023 for generic Party-role shape, WM-XCT-020/WM-KNW-018/EM-XCT-09 for classification, EM-ORG-01 for group perimeter, EM-COM-02/03/04 for commercial processes, commercial-contract models, WM-ACT-027 for communication events and WM-XCT-002 for consent.

## Adjudication

Decision: publish a bounded **Enterprise Counterparty Relationship Profile**, provided an independent frozen implementation audit finds no blocker.

The reconciled boundary is:

1. `CounterpartyRelationshipSet` identity is `(partyRef, observerDimensionRef)`. `partyRef` must resolve through the adopting Dimension's authoritative Party identity policy. The profile neither mints nor merges Parties.
2. `CommercialRoleBinding` references exactly one immutable/upstream-versioned WM-ORG-014 or WM-ORG-015 record. Role-to-authority mapping is closed: customer→014; supplier/partner→015.
3. `AccountScopeBinding` carries `scopeKind ∈ {seller, buyer, legal-entity, group}` plus a resolving target and validity interval. It never owns group membership, customer hierarchy or legal perimeter.
4. `ContactAssignment` carries endpoint ref, purpose, role-binding ref, scope and half-open validity. It never contains endpoint value, normalization, verification, consent or reachability truth and never authorizes outreach.
5. `SegmentationAssertion` carries code, scheme ref/version, source ref, method, asserted time, validity and supersession. It never owns a scheme and never overwrites a conflicting assertion silently.
6. `rolesAt(t)`, `contactsFor(purpose,t)` and `segmentsAt(t)` are pure projections with provenance. They mint no identity or authority.
7. No independent relationship lifecycle exists in the profile. Upstream termination/supersession makes the dependent binding inactive or orphaned while preserving history.
8. No cross-model endpoint edge is frozen as settled. WM-PER-010 is the designated party-endpoint resolver for this profile; the registry ownership conflict with WM-XCT-024 stays visible as a hold.

Publication holds:

- WM-ORG-014/015/PER-010/XCT-024 are reviewable drafts; their publication does not prove complete independent review.
- WM-ORG-014/015 composition edges remain unapproved.
- WM-PER-010 versus WM-XCT-024 ownership is unresolved at source.
- No production Party-master, IAM, CRM, procurement, consent or classification-system integration is included.
- The profile cannot guarantee non-duplication when the adopting Dimension itself has multiple unresolved Party masters.

Minimum implementation tests: tri-role single Party; observer-Dimension isolation; role-to-authority mismatch; duplicate set; dangling and superseded upstream records; group/legal-entity scope collision; contact value smuggling; missing purpose/role/time; expired assignment; bare segment; unknown scheme version; conflicting sourced segments; endpoint conflict hold; B2B/B2C does not split Party; upstream termination preserves history and removes the binding from current projections.
