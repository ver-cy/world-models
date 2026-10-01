# Frozen semantic audit — EM-LEG-04

## Verdict

**Conditional fail — sound boundary, under-specified object model.** The nine semantic commitments are correctly *asserted* in the synthesis, comparison and invariant list, but the `objects` block cannot carry at least seven of the fourteen invariants. Decision (`NEW MODEL`), `allocationState: unassigned` and `canonicalPublishable: false` are correct and must stay. No identifier may be allocated on this artifact.

## Defects

1. **No transition object.** Lifecycle exists only as an enum on `RegulatoryAuthorization`. Nothing carries authority, legal basis, grounds, due process, affected scope, decision/effect/record times, appeal route or originating case. Invariants 2, 3, 6, 7 and the suspension/renewal fixtures are unsatisfiable as declared.
2. **Authority-qualified key is not a key.** `authorityRef` + `authorityGrantKey` are ordinary required fields. No uniqueness constraint, no scoping of the key to the authority, no invariant preventing two `regulatoryAuthorizationId`s sharing one authority grant key.
3. **No grant-level version.** `identityTest.versionIdentity` promises governed versions on holder, validity and authority state, but only scope and (nominally) conditions version. Holder change and reinstatement have no version carrier.
4. **No register observation fields.** Synthesis requires observation time, source as-of and freshness; objects offer only optional `registerRef`. Invariant 11 and `certificate-currentness` have nothing to bind to.
5. **Activity representation collapsed.** `authorizedActivity` is a single field. Verbatim authority text pinned to decision and legal basis, structured decomposition (act, object, method, threshold, site) and classifier mappings with scheme version, mapping relation, confidence and information loss are absent; nothing marks mappings non-normative. Invariant 1 is unenforceable.
6. **Closed-world scope not encoded.** `siteRefs`, `assetRefs`, `capacityLimits` are optional with no closure rule. Absence currently reads as unconstrained, i.e. the opposite of invariant 4.
7. **Conditions are not dependent.** `PermitCondition.identity` is `conditionId` alone, with no `regulatoryAuthorizationId`, no scope-version reference and no version component or `supersedes`. `conditionKind` is unenumerated, so the seven declared types (precondition, continuing duty, limit, reporting/monitoring, prohibition, exception, waiver) are not constrained. `waiverRef` permits a bare pointer where the synthesis requires an authority act.
8. **Parties incomplete.** Only `holderRef`. Operator, owner and beneficiary references named in the synthesis are missing, and there is no holder-change decision carrier for invariant 8.
9. **No grant validity interval.** Lifecycle includes `expired` while validity exists only per scope version.
10. **Denormalized `status`** with no rule deriving it from the latest authority transition, against invariant 13's append-only history.
11. **Unsupported reference targets.** `WM-POL-001`, `WM-ACT-034` and `WM-KNW-003` appear only in the candidate; neither the synthesis nor the comparison establishes them. Verify or drop — do not substitute new identifiers.
12. **Stale holds.** "Independent Grok review is pending" contradicts the completed comparison. `WM-POL-014` is recorded as unresolved ambiguity although synthesis and comparison both record an explicit rejection; `boundary.excludes` omits the stewardship boundary.

## Minimal remediation

Add `AuthorizationTransition` (identity: authorization + sequence; required: authorityRef, legalBasisRefs, transitionKind, grounds, decisionTime, effectTime, recordTime; optional: affectedScopeRefs, appealRoute, originatingCaseRef). Make (`authorityRef`, `authorityGrantKey`) uniquely identifying and add the non-recycling invariant to the key. Add `grantVersion`, grant `validFrom`/`validTo`, and `registerObservation` (observedAt, sourceAsOf, freshness). Split activity into `verbatimActivityText` + `activityDecomposition` + optional `classifierMappings` (scheme, schemeVersion, relation, confidence, informationLoss, normative: false). State scope closure explicitly: absent site/asset/capacity authorizes nothing. Add `regulatoryAuthorizationId` and `conditionVersion` to `PermitCondition`, enumerate `conditionKind`, replace `waiverRef` with a waiver act reference. Add optional operator/owner/beneficiary refs and a holder-change decision ref. Derive `status` from the latest transition. Resolve the three unsupported references, close the Grok hold, and record WM-POL-014 in `excludes`.

## Required fixtures

Authority-key uniqueness collision; transition-record completeness; non-collapsibility of expiry / revocation / annulment / surrender; reinstatement and supersession lineage; holder change only by authority act; absent-site closure; condition typing, versioning and waiver-as-act; verbatim retention with lossy non-normative classifier mapping; stale register observation blocking current-status assertion; IP-licence substitution rejection (invariant 10 is fixtured only for commercial entitlement).

## Publication disposition

Hold as reviewable draft. Not canonical, not publishable, no registry allocation. Re-audit after the transition object, key constraint, activity split, condition dependency and the ten fixtures land; jurisdiction-qualified classes, appeal and due process still need specialist review.
