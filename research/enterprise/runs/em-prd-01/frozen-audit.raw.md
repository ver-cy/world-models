# EM-PRD-01 frozen independent semantic audit

## Verdict

Conditionally accepted as an unassigned candidate direction; publication withheld. Product continuity, non-contractual Roadmap Item semantics and external subscription mastership are correct. The audit identified eight blocking defects which were remediated once without rerunning the audit.

## Blocking defects

1. Price Plan was denied independent identity while being externally addressable.
2. Offering was described both as versioned and as successor-based.
3. Change classification lacked precedence, closure and time semantics.
4. Quote-referenced subscriptions could lose their mastered entitlement source.
5. Product, Edition and Offering lifecycle windows were undefined.
6. Bundle-to-Product promotion was circular.
7. Edition versus commercial tier had an ungated exception.
8. The restrictive profile and quote dependency lacked exact non-canonical source pins.

## Applied remediation

The package chose the non-addressable component option for Price Plan. Cross-domain references use a composite path rooted in Offering identity, unique plan name and immutable version ordinal. Offering is succeeded, never versioned. A closed precedence-based change classifier, one effectivity interval per plan version, quote-as-overlay conjunction, orderability/serviceability/support separation, observable bundle promotion evidence, strict Edition capability tests and exact WM-ACT-008/WM-ECO-021 source hashes are now recorded. Product Family classification, display-name authority, bundle billing, optional Roadmap references, explicit zero-rate plans, Edition targets and jurisdiction-scoped tariff behavior are also explicit.

## Publication disposition

Withheld. Both catalogue candidates remain identifier-unassigned, Roadmap Item keeps newRuntimeId=false, and fixtures are specified but not executed. No canonical completeness, stability, installability or publication claim is made.
