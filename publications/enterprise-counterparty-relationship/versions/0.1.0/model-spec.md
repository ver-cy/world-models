# Enterprise Counterparty Relationship 0.1.0

This bounded profile composes existing authorities so one Party can be a customer, supplier and partner without acquiring multiple identities. The profile set is identified by `(partyRef, observerDimensionRef)`. The adopting Dimension must already have an authoritative Party-resolution policy.

`CommercialRoleBinding` points to an exact versioned WM-ORG-014 customer record or WM-ORG-015 supplier/partner record. It never copies relationship lifecycle, qualification, approval, risk or performance. `AccountScopeBinding` names seller, buyer, legal-entity or group scope; it does not own group membership or infer a group from tax identifiers or CRM hierarchy.

`ContactAssignment` references a WM-PER-010 endpoint and qualifies it by purpose, commercial role, scope and half-open validity interval. It stores no endpoint value, normalization, verification, reachability or consent. An assignment never grants permission to contact. The registry conflict between WM-PER-010 and WM-XCT-024 remains open; this profile designates WM-PER-010 for party endpoints without claiming the wider conflict is settled.

`SegmentationAssertion` is a sourced, method-qualified assertion against a named scheme version. Conflicting assertions coexist; correction appends a superseding assertion. The profile never owns a scheme.

`rolesAt(t)`, `contactsFor(purpose,t)` and `segmentsAt(t)` are pure, provenance-carrying projections. They mint no Party, relationship, endpoint, consent or classification authority. Upstream termination or supersession removes a binding from the current view while preserving history.

`counterparty.schema.json` checks closed record structure only. Schema validity does not imply profile conformance: the Python evaluator additionally enforces authority mapping, cross-record references, set isolation, interval order, non-self same-set supersession and forbidden ownership. Production adopters must apply both layers or an equivalent implementation.
