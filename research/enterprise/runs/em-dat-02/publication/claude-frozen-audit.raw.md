# Frozen audit — EM-DAT-02 / WM-DAT-008 v0.3.1-candidate.2

## Verdict

**REVISE.**

The four load-bearing dispositions survive challenge and should be kept: external mastership of offering and agreement, Catalog Record as a separately identified object rather than a product facet, the consumer entitlement as an identified governed object rather than a bare edge, and pin-versus-head as the version trigger discriminator. None of those are what fails.

What fails is that the invariant set is **unaddressable** (no invariant carries an identifier, so every `expectRule` in the fixture file is dangling), the fixture-to-rule mapping is **demonstrably wrong for 9 of 17 cases**, and three rule-level contradictions are live in the text: published-version immutability against an enumerated trigger list, aggregate containment against a catalog record that may predate and outlive the product, and a required `agreementRef` against a stated hold that no agreement authority has an identifier. These are content defects, not presentation defects, so ACCEPT WITH LIMITS is not available.

I make no claim about publication readiness and I have not minted any identifier.

---

## Blocking findings

### B1. Invariants have no identifiers; every `expectRule` is dangling

`invariants` is a flat array of 22 strings. No `id` field exists on any element. The fixture file references `INV-001` … `INV-022`. There is therefore no defined resolution from a fixture to the rule it claims to exercise — the mapping exists only by implied array position, which is not declared anywhere and which breaks on any insertion.

**Remediation (minimal):** convert `invariants` to an array of objects `{id, statement}` with ids assigned in the current array order, and state in the candidate that ids are stable and never reused. Do not reorder while assigning.

### B2. Nine of seventeen fixtures point at the wrong rule

Taking array position as the intended mapping, fixtures 1–7 appear to have been numbered by **fixture ordinal, not by invariant**, and the last two reuse arbitrary values. Fixtures 8–15 (`two-catalog-records` … `withdraw-history`) map correctly.

| Fixture | Claims | Position resolves to | Should cite (by position) |
|---|---|---|---|
| `promotion-gate-failure` | 001 | separate resolvable identities | 14 |
| `pinned-member-change` | 002 | product-record describes only product | 5 |
| `series-head-advance` | 003 | published versions immutable | 6 |
| `two-consumers-two-terms` | 004 | member declares role/type/policy | 10 (+19) |
| `catalog-record-separation` | 005 | rebinding pinned member | 2 (+1) |
| `availability-is-not-fitness` | 006 | series-head advance | 12 |
| `withdrawal-no-cascade` | 007 | product stores no bytes/runs/results | 13 |
| `offering-inline-price` | 007 | product stores no bytes/runs/results | **no invariant exists** — see B3 |
| `floating-api-contract` | 002 | product-record describes only product | **no invariant exists** — see B4 |

**Remediation:** repoint all nine after B1 lands. Permit `expectRule` to be an array; `catalog-record-separation` and `two-consumers-two-terms` each legitimately exercise two rules.

### B3. No invariant forbids copying commercial master data

`offeringAgreementPlacement.rule` states "No price, SKU or legal text is copied into WM-DAT-008," but `offeringAgreementPlacement` is a descriptive block, not an invariant. The `offering-inline-price` fixture is a negative case with nothing normative to fail against. Grok lists "Offering or Consumer Agreement inlined" as a publication blocker; the candidate carries the prohibition only in prose.

**Remediation:** add an invariant — *No price, tariff, SKU, market, channel, sales-term or legal text is stored in any WM-DAT-008 object; commercial and legal content is referenced only.* Repoint `offering-inline-price` to it.

### B4. No invariant requires access routes to pin an interface-contract revision

Invariant #8 requires an access route to identify "its interface or distribution and authorization requirement" — identification, not pinning. Pinning appears only as a *version trigger* ("pinned interface-contract revision change"), which presupposes a pin the model never requires. The `floating-api-contract` fixture expects rejection of publication with no rule to reject under. Both studies require this (Claude invariant 11 "pinned contract version"; Grok's blocker list "unpinned members").

**Remediation:** amend invariant #8 to *Every access route identifies its interface or distribution reference at a pinned revision, and its authorization requirement.*

### B5. Published-version immutability contradicts the enumerated trigger list

Invariant #3 makes published product versions immutable. `versionTriggers.createsSuccessorProductVersion` enumerates four triggers. `productVersion.required` has fourteen fields. Changes to `accountableOwnerRef`, `stewardRef`, `boundedUseCases`, `accessRoutes`, `deprecationPolicy`, `termsAndAuthorizationRefs`, `measurablePromiseDefinitions` and `versionTriggerPolicy` are therefore either (a) permitted in place, contradicting immutability, or (b) covered, making the enumeration misleading. `accessRoutes` is the sharpest case: changing where a consumer reaches the product is at least as consequential as rebinding a pin, and it is unlisted.

**Remediation:** replace the enumeration semantics with *any change to the required content of a published product version creates a successor version*, and relabel `createsSuccessorProductVersion` as non-exhaustive illustrative cases. Keep `doesNotCreateProductVersion` as an exhaustive exclusion list — that list is the one that must be closed.

### B6. No rule governs a series-head advance that breaks a declared promise

`resourceComposition.versionRule` asserts both that head advance does not change version identity **and** that "every declared promise must remain satisfied." No rule states what happens when it is not. This is precisely Grok's first collapse failure ("D1's series-head advance silently mutates P's promise") and it is currently unmodelled. The `series-head-advance` fixture is positive-only; the breach branch has no fixture and no rule.

**Remediation:** add a rule — *A declared-series-head advance that violates a declared promise does not retroactively alter the published product version; it raises a declared promise-breach state on that version, and remediation is by repinning the member or revising the promise, each of which creates a successor version.* Add a negative fixture for the breach branch.

### B7. `versionTriggerPolicy` is a second, per-version locus for model-level rules

`versionTriggerPolicy` is a required field on every product version while `versionTriggers` is a model-level rule block. If a version may declare its own triggers, invariants #5 and #6 are not invariant. If it may not, the field is redundant and invites drift.

**Remediation:** either delete `versionTriggerPolicy` from `productVersion.required`, or constrain it to declaring only per-member pin/head resolution choices already bounded by the model-level triggers, and state explicitly that it cannot weaken them.

### B8. `productVersion` identity is over-specified and ambiguous

Identity is `["productId","productVersionId","version"]`. `productVersionId` and `version` are each discriminating within `productId`, so the declared key admits contradictory rows (same `productVersionId`, different `version`). Both studies say "product id + immutable version." The candidate added a surrogate without retiring the natural key.

**Remediation:** set identity to `["productId","productVersionId"]` and declare `version` a unique, immutable label scoped to `productId`.

### B9. `ownerNamespace` in product identity makes ownership transfer an identity change

`product` identity is `["productId","ownerNamespace"]`. If `productId` is globally unique, `ownerNamespace` is not identifying. If it is scoped, `ownerNamespace` must be immutable — which makes an ordinary governance event (owner transfer) mint a new product identity, contradicting the stability claim carried by the model's own purpose and by Claude invariant 1. The candidate also carries `accountableOwnerRef` on the version, so two owner-bearing fields exist with undeclared and different mutability.

**Remediation:** either drop `ownerNamespace` from identity, or declare it an immutable minting namespace explicitly distinct from current accountability, and state that `accountableOwnerRef` changes do not affect product identity.

### B10. Entitlement-binding identity is global while its classification is dependent

`consumerEntitlementBinding` is classified as an "identified dependent governed object **inside** the Data Product aggregate," yet its identity is a bare `["entitlementBindingId"]` with no root scope. A dependent object with an unscoped key cannot be located from its root, and the aggregate boundary cannot be enforced on it. Separately, `productVersionId` is required as a reference but — given the version key in B8 — a bare `productVersionId` does not constitute a valid version reference.

**Remediation:** identity `["productId","entitlementBindingId"]`; replace the bare `productVersionId` field with a full `productVersionRef` carrying `productId` + `productVersionId`.

### B11. Containment is asserted but foreign authorities write the contained members

`bind-consumer-entitlement` is authorised to "access or agreement authority"; `register-product-catalog-record` to "catalog operator." Neither is the product owner. An aggregate whose members are written by external authorities has no enforcement point for its own invariants. Note that neither study placed the binding *inside* the product aggregate — Grok says "governed object, not attribute," Claude says "dependent binding"; containment is the candidate's own addition.

**Remediation:** pick one and say it. Either (a) declare the product aggregate the write boundary, with external authorities supplying the referenced decision and the product owner or delegated steward recording the member; or (b) reclassify both as separately rooted objects **mastered by** WM-DAT-008 and referencing the product, and drop the containment language. Option (b) is the one consistent with B12.

### B12. Catalog record cannot be a contained aggregate member and also predate/outlive the root

`coexistenceRule` states "a record may predate completion or survive withdrawal." Invariant #22 requires historical records to remain addressable after product withdrawal. Both are incompatible with the record being contained in the DataProduct aggregate under `entryKind: aggregate`. A member cannot exist before its root.

**Remediation:** distinguish *mastered by WM-DAT-008* from *contained in the DataProduct aggregate* in the boundary text, and declare the product catalog record a second root mastered by the same model. This is the remediation that also resolves half of B11.

### B13. Required `agreementRef` makes internal-use products unconstructible

`agreementRef` is unconditionally required on every binding, while `holds` states agreement authorities are "identifier-unassigned." Grok's minimum completion shape explicitly requires the binding to admit "internal-use / no-fee." As written, an internally consumed data product with no legal instrument cannot be published, and no fixture covers the internal-use path.

**Remediation:** admit a declared internal-use terms basis as an explicit admissible form of `agreementRef` (an authority-qualified internal-terms reference, not inline text), or make `agreementRef` conditionally required on a declared `termsBasis` discriminator. Add a positive fixture for internal-use.

### B14. Offering binding is asserted in placement but absent everywhere else

`offeringAgreementPlacement.offering` says "external commercial master; effective-dated binding only," matching Grok's "product or product-version → offering-ref and/or agreement-ref." But no offering binding exists in `identities`, in `consumerEntitlementBinding.required`/`optional`, in `operations`, in `invariants` or in fixtures. The placement block promises an object the model does not define.

**Remediation:** either add `offeringRef` to `consumerEntitlementBinding.optional` bound by the new B3 invariant, or state in `holds` that offering bindings are deferred and remove "effective-dated binding only" from the offering line so the block stops asserting an undefined object.

### B15. Required relations target non-canonical and unapproved models, and this is not held

`WM-DAT-001` and `WM-DAT-004` carry `required: true`. The Claude study records `publishableCanonical: false` on WM-DAT-008, WM-DAT-001, WM-DAT-004 and WM-DAT-007, and carries "WM-DAT-001 relation unapproved" as an open hold. Neither fact survives into the candidate's `holds`. Declaring a hard dependency on an unapproved edge is an overreach relative to the frozen inputs.

**Remediation:** add holds — *required relations resolve to models that are themselves not canonically publishable, so no canonical layer may rest on WM-DAT-008*; and *the WM-DAT-001 relation is unapproved and `required: true` is provisional pending that approval.*

### B16. The catalog-boundary rule binds WM-DAT-001 unilaterally

`catalogRecordBoundary.rule` allocates dataset/series/distribution records to WM-DAT-001. The Claude study records this as an **unresolved** two-master overlap (WM-DAT-001 retains its own `catalogue-record-and-listing` finding with record state and harvest datestamps) and carries it as a hold. The candidate states the resolution as settled and drops the hold.

**Remediation:** restore the hold — *disjointness requires a reciprocal amendment demoting WM-DAT-001's catalogue-record facet to a reference; until then the rule is declared, not enforced.* Add a negative fixture for the contested case: a dataset that is also published as a product, listed once in the same catalog.

---

## Non-blocking findings

- **N1 — compound type name.** `name: "Data Product with Catalog Record facet"` embeds the second identity into the root type's name, which is the exact collapse the coexistence rule forbids. Rename to `Data Product`; carry the record as a named mastered object. (Claude: "the dual name is a defect of presentation.")
- **N2 — duplicate invariants.** #11 and #18 state the same rule; #17 overlaps both. #5 and #6 restate `resourceComposition.versionRule` and `versionTriggers` verbatim. Redundancy guarantees future drift. Collapse #11 into #18; mark #5/#6 as the normative locus and make the trigger blocks derived.
- **N3 — no transition graphs anywhere.** Four lifecycles are declared as state *sets* only (product 7 states, record 5, binding 6, plus `withdrawn`/`retired` and `withdrawn`/`tombstoned` pairs whose difference is undefined). For a model whose central claim is lifecycle independence, absent transition tables are a material omission. Add `transitions` per lifecycle and define withdrawn-vs-retired.
- **N4 — status/timestamp inconsistency on bindings.** `suspended` and `expired` are lifecycle states while `suspendedAt` and `expiredAt` are optional, and `revocationRef` exists with no `revokedAt`. Make the state-dependent stamps conditionally required on entry to the corresponding state.
- **N5 — no temporal attributes on product version or catalog record.** Invariant #20 asserts three intervals advance independently, but only the binding has an interval (`effectiveFrom`/`effectiveTo`). The `record-product-field-overwrite` fixture references `withdrawnAt` on both objects; that field is declared nowhere. Declare the minimal stamps (record: `listedAt`, `statusChangedAt`; product version: `publishedAt`, `deprecatedAt`, `withdrawnAt`) or the fixture tests undeclared structure.
- **N6 — `tombstoned` unreconciled with addressability.** Invariant #22 requires historical records to remain addressable; `tombstoned` conventionally implies content removal. Add one line: tombstoning retains identifier resolution and records removal; it is not deletion. No fixture exercises it.
- **N7 — `authorityRef` is ambiguous and reads like a grant.** `bind-consumer-entitlement` names "access **or** agreement authority" disjunctively, and `authorityRef` sits beside `approvalRef` and `agreementRef`. Given that invariant #18 turns on the binding not being a grant, rename to `accessAuthorityRef` and state that it names the authority competent to decide, never the decision.
- **N8 — two loci for terms.** `productVersion.termsAndAuthorizationRefs` and the per-binding `agreementRef` both hold terms references with no stated relationship. Risk: version-level terms read as a default agreement, i.e. terms minted in WM-DAT-008. Add: version-level terms references are descriptive and never substitute for a binding.
- **N9 — external refs escape the model's own reference discipline.** Members must declare `role` + `resourceRef` + `resourceType` + `resolutionPolicy`. `agreementRef`, `authorityRef`, `approvalRef` declare none. Given both authorities are identifier-unassigned, require an authority-qualified reference form so the unassigned authority is explicit at the field rather than implicit in a hold.
- **N10 — `required: true` on WM-DAT-001 versus API-only products.** A product composing only a WM-SFT-003 interface has no WM-DAT-001 member, yet the relation is required. Also, `resourceType` has no admissible enumeration and composition has no minimum cardinality. Add the enum, require ≥1 member, and make the WM-DAT-001 relation required *conditionally on a dataset-typed member*.
- **N11 — WM-DAT-005 dropped.** The Claude study names WM-DAT-005 as pipeline master; the candidate delegates only "pipeline and processing-run execution to WM-ACT-053." Pipeline *definition* mastership is now unstated. Either restore the reference or say pipeline definitions are out of scope.
- **N12 — missing operations for declared lifecycles.** No operation transitions a catalog record (yet `two-catalog-records` delists one) and none transitions a binding (yet `binding-suspension-no-product-change` suspends one). No operation reaches `retired`. Add `transition-product-catalog-record`, `transition-consumer-entitlement-binding`, and extend the product operation to `retired`.
- **N13 — deprecation policy has no content requirements.** Both studies require successor-or-explicit-no-successor, sunset instant, and notice to entitlement holders. `deprecationPolicy` is required as a field with no declared sub-structure, no invariant, and no fixture. The `withdrawal-no-cascade` fixture asserts "holders are notified," which no invariant guarantees — either add the notification invariant or strike that clause from the expectation.

---

## Invariant and fixture gaps

Uncovered invariants, by current array position:

| # | Statement | Gap |
|---|---|---|
| 3 | published versions immutable, successor-linked | no negative case attempting in-place mutation of a published version |
| 4 | member declares role, identity, type, resolution policy | no negative case for a member missing `resolutionPolicy` or `resourceType` |
| 7 | product stores no bytes, runs, observations, results | no negative case copying an observation value or distribution into the product |
| 9 | promise identifies metric definition, target, unit, window, measurement point, aggregation rule | no case; and see the caveat below |
| 12 | eight assertions independent | only availability-vs-fitness is exercised; six predicates untested |

Additional missing cases: the promise-breaking head advance (B6); the catalog-boundary collision (B16); internal-use binding (B13); ownership transfer against identity stability (B9); a binding `active` against an unpublished version — no rule currently constrains binding interval against version interval, and if that independence is intended it should be stated rather than left silent; `tombstoned` (N6).

**Caveat on invariant #9.** It requires every promise to identify a *metric definition*, while `holds` states metric-definition authority is pending EM-DAT-05. The invariant is therefore unsatisfiable by reference until that authority exists. This is correctly consistent with `canonicalPublishable: false` and I am not asking you to fix it — but it should be named in `holds` as an unsatisfiable-by-reference invariant, not left to be inferred from the EM-DAT-05 line.

Fixture-file hygiene: `expectRule` should accept an array; `two-consumers-two-terms` and `two-consumers-same-version` are near-duplicates but both earn their place and should be kept once repointed.

---

## What I did not find fault with

No new model identifier is minted for either the catalog record or the entitlement binding — both are members of an existing reserved entry, which is the correct outcome and matches both studies. `doesNotCreateProductVersion` correctly excludes catalog-record status, binding status, pipeline runs and quality observations. `boundary.excludes` correctly keeps authorization evaluation and credential material out. The candidate and fixture files agree on `modelId` and `version`. `canonicalPublishable: false` is correct and, given B15 and the invariant-#9 caveat, is load-bearing rather than cautionary.
