# EM-LEG-04 provider-reconciled synthesis

## Decision

Regulatory Authorization / Granted Permission remains an identifier-unassigned NEW MODEL candidate. Its identity and lifecycle are independent of WM-POL-004 cases, WM-XCT-017 credentials, WM-ECO-022 entitlements, IP licences and WM-POL-014 stewardship. Permit and Licence are jurisdiction-qualified classes of the same grant kind. Scope, conditions, mappings, register observations and transitions are grant-dependent records. No identifier is allocated.

## Audited shape

The authority-qualified natural key is issuing authority, jurisdiction, instrument class and authority-local grant key. It is unique and never recycled. Holder, validity and operative state revisions use append-only grant versions. Status is derived from the latest effective AuthorizationTransition. Each transition names authority, legal basis, grounds, decision/effect/record times, resulting state, affected scope, appeal route and originating WM-POL-004 case when present.

Operative scope retains authoritative verbatim text and a subordinate structured decomposition. Versioned classifier mappings are explicitly non-normative and loss-aware. Scope is closed-world: silence authorizes nothing. Conditions are typed, versioned, scope-bound dependent records; waivers require authority acts. Register observations carry observed-at, source-as-of, freshness and digest, so stale credentials cannot establish current status.

## Separation rules

Case decision, credential, commercial entitlement, IP licence, ownership and stewardship never become the grant. Affiliates, successors, new holders, activities, sites, assets and territories gain no permission by inference. Expiry, revocation, surrender and annulment remain distinct. Suspension preserves identity and disables exercise; reinstatement never widens scope.

The candidate now has 20 invariants and 18 fixtures covering natural-key collision, transition completeness, distinct ending grounds, reinstatement and supersession lineage, holder change, closed-world absence, typed conditions, waiver acts, lossy mappings, stale observation and IP substitution.

## Publication state

Grok accepted the independent candidate and rejected WM-POL-014 as its owner. One frozen Claude audit found object-model gaps; all concrete defects were remediated without rerunning the audit. Registry allocation, canonical case-to-grant contract and specialist legal review remain required before publication.
