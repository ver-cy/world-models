# EM-LEG-04 local synthesis

## Verdict

- **Do not complete WM-POL-014** for the granted regulatory authorization. Its reserved subject is meta-object ownership and stewardship (`S1-meta-object-ownership-and-stewardship.md`: "who controls every meta-object; transfers, delegation, guardianship"), its nav path is the bare domain root `NAV.SOC.POL`, its spec is unavailable, and its own flag says "лучше mixin + ссылка". Its transfer/delegation semantics directly contradict permit non-transferability.
- **Do not use WM-XCT-017** as the grant. It owns issuer-asserted claims, and its own boundary note is decisive: "a licence or permit credential may evidence an external grant, but its authenticity and status do not themselves make an authorization decision"; `out_of_scope` names "permit grant … master lifecycle". It is the credential *about* the permission, referenced for document authenticity, status method and presentation.
- **Allocate nothing; register one identifier-unassigned independent model candidate**: *Regulatory Authorization (Granted Permission)*. WM-POL-004 externalizes the grant, WM-XCT-017 disclaims it, WM-PER-013 disclaims practice authorization — the grant is an unowned hole, not a missing field.
- Place **Permit** and **Licence** as jurisdiction-qualified classes of that one root, not two models. **PermitCondition** and **LicenceScope** are dependent parts of the grant, without independent identity.
- Keep WM-POL-004 as the application-to-decision case, unchanged.

## Evidence

WM-POL-004 `purpose`: the case is governed "while keeping the permission-bearing grant in its authoritative external master". `out_of_scope` excludes "permission-bearing permit, licence, authorization, credential or right master **and its independently verified current status**". Its composition requires a `REFERENCE` to "Granted Right, Attestation or Credential model" — target unnamed, and its own hold records "no approved WM-POL-004 rows". Its class finding treats permit/licence/approval/registration/exemption/certificate as one jurisdiction-qualified classification axis. WM-XCT-017 reclassified itself to aggregate, held legal-effect and recognition findings from publication for want of a legal authority source. WM-PER-013 states "qualification or valid proof cannot alone authorize intended work". Three specs converge on the same gap.

## Identity/mastership

| Layer | Identity | Master |
|---|---|---|
| Authorization case | case id + register + competent authority | WM-POL-004 |
| Granted authorization | issuing-authority namespace + register + authority-issued grant key + version | authority's public register (candidate model = governed mirror) |
| Condition | grant key + condition id + version | grant |
| Scope version | grant key + scope-version id | grant |
| Certificate/document | credential id | WM-XCT-017 |

Permit number, holder name, activity code, class label, validity dates, decision date, document title and file digest never identify a grant. The enterprise record is a source-qualified mirror carrying observation time, source as-of and freshness; it may never assert current validity without a resolved authoritative-register observation.

## Case versus grant

Application status and grant status are independent axes and neither is inferable from the other. A closed favourable case plus a paid fee plus a signed decision copy is not a grant; a grant exists only when the authority's register carries it. Conversely a suspended grant does not reopen its originating case. Follow-on renewal, variation, suspension, revocation and surrender are cases in WM-POL-004 that *produce* grant-version events; the grant records the resulting event with a back-reference to the case, and no case record may mutate grant state by inference.

## Regulatory versus commercial/IP rights

Separation test, in order: **who confers** — competent public authority vs contracting counterparty vs private right holder; **legal basis** — legal instrument plus enabling power (WM-POL-001) vs agreement vs statutory IP right (WM-KNW-003); **effect of absence** — the activity is unlawful and sanctionable vs merely unpaid/unavailable vs infringing; **transferability** — non-transferable by default vs assignable per contract vs assignable and sublicensable. Consequences: a contract cannot create, cure, waive or extend a regulatory permission; a consumption entitlement (WM-ECO-022) suspension never suspends a permit; an IP licence grants no regulatory permission over the same product. The word "licence" is overloaded across all three and must never be the discriminator.

## Scope and activity

Scope is a versioned component of the grant, changed only by an authority variation decision. It enumerates: regulated activity assertions; regulated product, substance, material or resource; site, installation or asset; equipment and method; quantity, capacity, threshold and quota limits; territory; validity interval; and **explicit exclusions**. Everything not enumerated is outside scope; there is no residual permission.

**Activity without a stable classifier.** Represent the authorized activity as a structured assertion, not a code: (a) the authority's verbatim authorized-activity text, pinned to the decision and legal basis, as the normative anchor; (b) decomposition into act verb, object, method/technology, threshold and site/asset reference; (c) zero or more classifier candidates, each with classifier, version, mapping relation (exact/broader/narrower/related), confidence and declared loss, marked non-normative. A classifier code is a label attached after the fact. It is never identity, never scope and never permission — which is exactly the negative case: an industry code in a company registration is a self-declared descriptor, carries no authority decision, no conditions and no validity, and is not a licence.

## Conditions

A condition is authority-imposed, attached to the grant (not to the case), and typed: precondition to exercise, continuing duty, quantitative limit, reporting or monitoring obligation, prohibition, exception or waiver. Each carries source (grant text vs general legal norm), responsible party, trigger, deadline, evidence requirement, breach consequence and its own effective interval. Conditions version independently of scope; a waiver is a dated authority act, never a flag. Compliance evidence lives in monitoring, inspection and enforcement masters and is referenced, never inlined; an unmet condition does not by itself change grant state — only an authority decision does.

## Lifecycle

States: in force, suspended, expired, revoked, annulled, surrendered, reinstated, superseded. Transitions require authority, legal basis, grounds, due process, affected scope, decision time, effect time, recorded time, appeal route and originating case. Distinctions that must never collapse: expiry (time lapse, no authority act) ≠ revocation (authority termination on grounds) ≠ surrender (holder-initiated) ≠ annulment (retroactive invalidity) ≠ suspension (temporary, reversible, scope-subsettable). Renewal follows the jurisdiction's identity-continuity rule: same grant key with a new validity interval, or a successor grant with a predecessor link — recorded, not assumed. Variation creates a new scope or condition version; prior versions stay citable. All history is append-only.

## Parties and affiliates

The grant binds one named holder (legal person), optionally with operator, owner and beneficiary roles held separately. There is **no traversal of corporate-group, ownership, control, trading-name or contractual edges** to extend coverage. Subsidiaries, affiliates, branches, franchisees, contractors and merger successors are outside the grant unless the authority names them or issues a holder-change decision. Adding a site, an activity, an asset or a holder requires an authority act; each is a distinct variation or new application.

## Scenario

(1) *One-site licence.* Grant G bound to holder H, site S1, activity A1. Site S2 — same holder, same activity — is not covered; no scope entry, no inference from S1. (2) *Temporary suspension.* Suspension S with interval, grounds, authority and affected scope subset: scope content and conditions unchanged, exercisability false for the subset, validity window not extended unless the authority extends it, reinstatement restores the prior scope version, and the suspended interval remains permanently visible. (3) *New activity outside scope.* Activity A2 matches no authorized activity assertion in the current scope version; H's registration classifier code covering A2 is non-normative and irrelevant; A2 requires a variation or new application. All three resolve without editing G's identity.

## Invariants

1. An activity classifier code is never a permission, identity or scope.
2. Issuing authority and legal basis are explicit and resolvable on every grant and every transition.
3. A grant never extends to subsidiaries, affiliates, successors, additional sites, assets or activities by inference.
4. Case state and grant state are distinct and mutually non-inferable.
5. Permit number, holder name, class label, dates or document digest never identify a grant.
6. Scope is enumerative; unlisted is unauthorized.
7. Conditions are authority-sourced, typed, dated and independently versioned; waiver is a dated act.
8. Suspension, expiry, revocation, annulment and surrender remain distinct.
9. Only an authority decision changes grant state; compliance signals do not.
10. The grant is non-transferable absent an authority holder-change decision.
11. Regulatory permission, commercial entitlement and IP licence never merge or substitute.
12. Current validity requires a source-qualified authoritative-register observation with freshness.
13. All grant history is append-only and citable.

## Minimal completion shape

Root *Regulatory Authorization*: identity and register; class (permit/licence/approval/registration/exemption/certificate, jurisdiction- and version-qualified); authority and legal basis; holder and role bindings; scope versions (activity assertions, product, site/asset, territory, quantitative limits, exclusions); condition set; validity intervals; state and transition ledger; appeal and remedy references; credential reference (WM-XCT-017); case references (WM-POL-004); legal-instrument references (WM-POL-001); register-observation and freshness block; purpose-bound access and verification views.

## Holds

No identifier is allocated. WM-POL-004 and WM-XCT-017 are published reviewable drafts under single-provider waiver with zero approved relation rows; WM-POL-014 and WM-KNW-003 have no available spec; WM-POL-014's name and legacy spec disagree. The listed comparison tracks (UBL/FIBO, ODRL, primary legal sources) are unverified here, and applicability to any jurisdiction is untested. Jurisdiction profiles for licensing classes, identity continuity on renewal, transfer rules, due process and appeal remain specialist work; no fixtures exist for one-site scope, suspension or out-of-scope activity. This checkpoint makes no canonical completeness or installability claim.
