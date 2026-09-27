# EM-LEG-04 local synthesis

## Disposition

- Keep WM-POL-004 as the application-to-decision Authorization Case. Its specification explicitly excludes the permission-bearing grant and its current status.
- Propose one identifier-unassigned independent **Regulatory Authorization / Granted Permission** model. Permit and Licence are jurisdiction-qualified classes of this root; PermitCondition and LicenceScope are dependent grant components.
- Do not complete WM-POL-014 for this purpose: its reservation concerns broad rights/entitlements and legacy ownership/stewardship semantics, with no available specification and a boundary-review flag.
- Use WM-XCT-017 only for the credential or document that evidences the grant. Its own boundary excludes the permit-grant lifecycle.
- Keep regulatory permission separate from WM-ECO-022 commercial subscription/consumption entitlement and from an intellectual-property licence. Allocate no identifier before registry adjudication.

## Identity and mastership

The authorization case, granted permission, condition, scope version and credential have distinct identities. The grant is identified in the issuing authority's namespace and register, with authority-issued grant key and version. Permit number, holder, activity code, dates, decision document and file digest do not independently identify it.

The enterprise representation is a source-qualified mirror of the authority register. It records observation time, source as-of and freshness and cannot assert current validity from a stale certificate or closed favorable case.

## Case versus grant

Application and grant lifecycles are independent. A favorable decision can create or change a grant only when the competent authority's master records the effect. Renewal, variation, suspension, revocation and surrender may run as WM-POL-004 cases, while the grant records resulting authority events and never infers a transition from case status.

## Regulatory, commercial and IP rights

Regulatory permission comes from a competent public authority and legal enabling power; without it, the regulated activity is unlawful or sanctionable. Commercial entitlement comes from an agreement and controls consumption or service access. An IP licence comes from a right holder and controls use of protected subject matter. Their scopes, transfer rules and consequences differ, and none creates or cures another.

## Scope, activity and conditions

Each scope version enumerates the authorized activity, product/substance/resource, site/installation/asset, equipment or method, quantity/capacity/quota limits, territory, interval and explicit exclusions. Unlisted activity, location, asset or holder is outside scope.

Where no stable classifier exists, preserve the authority's verbatim activity text pinned to the decision and legal basis; add a structured decomposition of act, object, method, threshold and site; attach optional classifier mappings with scheme version, mapping relation, confidence and information loss. Classifier mappings are non-normative.

Conditions are authority-imposed dependent components typed as precondition, continuing duty, limit, reporting/monitoring duty, prohibition, exception or waiver. They record source, responsible party, trigger, deadline, evidence requirement, breach consequence and effective interval. A waiver is an authority act, not a boolean.

## Lifecycle and parties

Grant states include in force, suspended, expired, revoked, annulled, surrendered, reinstated and superseded. Transitions preserve authority, basis, grounds, due process, affected scope, decision/effect/record times, appeal route and originating case. Variation creates new scope or condition versions; history remains append-only.

The grant names one holder and may separately reference operator, owner and beneficiary. Corporate ownership, control, trade names and contracts never extend it to subsidiaries, affiliates, branches, contractors, additional sites or successors. Extension requires an explicit authority act.

## Acceptance scenario

A grant binds holder H, site S1 and activity A1. S2 is outside scope. A temporary suspension records authority, grounds, interval and affected scope without erasing the grant or extending validity. New activity A2 remains unauthorized even when H's registration carries a matching industry code; it requires a variation or new application.

## Invariants

1. An activity classifier is never permission, grant identity or scope.
2. Every grant and transition identifies issuing authority and legal basis.
3. Authorization case state and grant state are distinct and non-inferable.
4. Scope is enumerative; unlisted activity, site, asset or party is unauthorized.
5. Conditions are authority-sourced, typed, dated and versioned.
6. Suspension, expiry, revocation, annulment and surrender remain distinct.
7. Only an authority act changes grant state.
8. The grant is non-transferable unless an authority holder-change decision says otherwise.
9. Subsidiaries and successors receive no permission by relationship traversal.
10. Regulatory, commercial and IP rights never substitute for one another.
11. Current status requires a fresh authoritative-register observation.
12. Credentials evidence grants but do not own or create them.
13. Grant and scope history remains append-only and citable.

## Holds

The independent grant candidate has no allocated identifier. WM-POL-004 and WM-XCT-017 are non-canonical reviewable drafts with single-provider and relationship-ledger holds. WM-POL-014 lacks a current specification and its legacy intent conflicts with permit non-transferability. Jurisdiction-specific classes, renewal identity, transfer, due process and appeal require specialist review. Crosswalks, immutable pins and acceptance fixtures are absent. This checkpoint makes no publication-readiness claim.
