# Frozen audit verdict — EM-COM-03

**Verdict: ACCEPT WITH CORRECTIONS.** The core adjudication is sound: allocation is correctly withheld, the identityGate is the right instrument, the profile is declared correspondence-only, and no standards-compliance or publishability claim is made. The defects below are real but all are drafting/authority-assignment errors, not covert mastership by the profile. One exception: the candidate itself contains two genuine dual-mastership seams (D1, D4).

## Material defects

**D1 — usage authority is doubly assigned.** The candidate references both `WM-MAT-008` ("measured usage observations used for allowance projections") and `WM-FLW-015` ("actual resource-consumption events"). `WM-MAT-008` appears nowhere in the local evidence or the provider comparison; the reconciliation states WM-FLW-015 owns usage. Two usage authorities for one projection.
*Fix:* delete the `WM-MAT-008` reference entry.

**D2 — `decision: "NEW MODEL"` contradicts the record.** `allocationState: "unassigned"`, `identityConclusion: "PARKED HYPOTHESIS"` and the reconciliation all deny a decision was reached.
*Fix:* set `decision` to `"NO DECISION — PARKED PENDING IDENTITY GATE"`.

**D3 — the `objects` block mints identity unconditionally.** `ConsumptionEntitlement.identity: ["entitlementId"]` and `EntitlementRevision.identity: ["entitlementId","revision"]` are stated as fact while `boundary.owns[0]` makes identity "conditional… only after identityGate evidence".
*Fix:* add `"conditionalOnIdentityGate": true` to `objects` and prefix the block as a hypothetical shape that is void if the gate fails.

**D4 — head and revision both master the terms.** `permission`, `resourceScope` and period appear as required on both `ConsumptionEntitlement` and `EntitlementRevision`; lineage is duplicated as `successorRef` and `supersedesRevision`. Immutable revisions plus a mutable head carrying the same fields is a second authoritative copy.
*Fix:* leave only `entitlementId`, `subjectRef`, `grantBasisRef`, `status` and `currentRevisionRef` on the head; move all terms and lineage to revisions.

**D5 — revision-vs-successor boundary undetermined.** `versionIdentity` says changes create "immutable entitlement revisions **or** successors" with no rule for which, permitting identity re-minting on a term change.
*Fix:* state the rule — change of subject, resource scope or grant basis ⇒ new entitlement; change of period, allowance, limits or reset rule ⇒ revision.

**D6 — candidate exclusions cover identity only, not authority.** `excludes` bars "order, subscription, offer, invoice or payment **identity**" but never bars the candidate from asserting order-line delivered/outstanding/allocated quantity, the subscription version head, subscription suspension state, or payment residual.
*Fix:* append those four items to `boundary.excludes` with their owning models (WM-ECO-020, WM-ECO-022, WM-ECO-022, WM-ECO-009).

**D7 — mastership field contradicts the provisioning exclusion.** `mastership: "entitlement or service-access authority"` names an access authority while `excludes` removes "service provisioning and runtime-availability state".
*Fix:* narrow to `"entitlement or licence grant authority"`.

**D8 — identityGate threshold is undefined.** `promotionEvidenceRequired` reads as conjunctive; the local evidence and comparison read disjunctively ("…lineage **or** external authority evidence").
*Fix:* add `"promotionRule": "any one item opens registry adjudication; evidence never allocates an identifier"`.

**D9 — binding ownership overlaps between candidate and profile.** `boundary.owns` claims "external execution evidence bindings" and the local evidence places `RenewalAssertion` in the profile, while the profile gives WM-ECO-022 exclusive ownership of "suspension and renewal clocks". Cross-model bindings then have two possible homes and the renewal link has two.
*Fix:* restrict candidate ownership to entitlement-internal successor lineage; state that `RenewalAssertion` is a read-only correspondence record of the WM-ECO-022-owned successor link, pinning both version revisions, and is never the sole record of a renewal.

**D10 — fulfilment-evidence master is unnamed.** `FulfilmentEvidenceBinding` and invariant 3 make delivered quantity move only through line-bound evidence, but no base in `bases` is assigned mastership of that evidence and `WM-ECO-024` is declared an unverified fulfilment boundary.
*Fix:* add a profile constraint naming WM-ECO-020 as provisional master of line-bound fulfilment evidence pending WM-ECO-024 adjudication, and add the same as an explicit hold.

**D11 — overage and refund are unmastered money assertions.** The profile assigns WM-ECO-008 "invoice, credit, debit and proration lines"; local-evidence invariant 14 also governs refund and overage, which no constraint assigns.
*Fix:* extend the WM-ECO-008 constraint to "invoice, credit, debit, refund, overage and proration lines".

**D12 — fixture traceability rests on an undeclared register.** `covers` tags resolve correctly and completely against `profile-candidate.constraints[1..16]` — but that mapping is stated nowhere, and the frozen set contains two other numbered lists of comparable length (local-evidence invariants 1–16, candidate invariants 1–12), so the tags are ambiguous on their face. `P06` (WM-ECO-009 payment allocation, residual, settlement exceptions) has no fixture, and no fixture exercises any candidate invariant.
*Fix:* add a `predicates` register to `fixtures.json` mapping P01–P16 to the profile constraint texts, and cover P06.

**D13 — WM-FLW-015 is a base with no binding.** It is listed in `bases` and the `usage-correction` fixture asserts downstream recomputation across that seam, but the local-evidence profile member list (`OfferVersionBinding`, `OrderSubscriptionOrigination`, `EntitlementBinding`, `RenewalAssertion`, `FulfilmentEvidenceBinding`, `SettlementBinding`) has no usage member.
*Fix:* add a correspondence-only `UsageProjectionBinding` pinning usage stream identity plus as-of time, minting no balance.

**D14 — the acceptance scenario couples payment state to entitlement state.** "Month 4 nonpayment suspends S **and** E1… Month 5 reactivates them" makes one payment event drive two clocks, contradicting invariant 8 and the independent-clock claim; the scenario also names `E1` as an instance, which the reconciliation demoted to a projection.
*Fix:* rewrite so nonpayment suspends S only, any grant restriction is a separate authority-issued assertion with its own basis and effective time, and `E1` is labelled a projected grant with no key.

**D15 — the disposition still asserts what the reconciliation demoted.** "Its right-to-consume identity and lifecycle **are** independent from Order, Subscription and actual Usage."
*Fix:* replace "are independent" with "are hypothesised independent and unproven pending identityGate evidence".

**D16 — invoice/payment references on the candidate carry no non-coupling constraint.** `WM-ECO-008` ("invoice or fiscal document references") and `WM-ECO-009` ("payment or settlement references") are admitted with vague purposes on a model whose invariants forbid payment-implied entitlement.
*Fix:* restate both purposes as "evidence-only reference; never a grant basis and never a state trigger".

**D17 — exclusivity is asserted over unsettled bases.** The profile says WM-ECO-020/022 "exclusively own" their authorities while the holds record both as reviewable drafts under waiver with single-provider/noncanonical holds.
*Fix:* qualify each "exclusively owns" as "provisionally owns under draft waiver; exclusivity re-asserted on base settlement".

## Exact additional fixtures required

1. `payment-residual-authority` — negative, P06. Profile or candidate asserts payment allocation or residual → rejected; WM-ECO-009 owns allocation, residual and settlement exceptions.
2. `external-licence-authority` — positive, P15. Grant mastered by an external licence authority distinct from the commercial instrument → recorded as the fifth identityGate evidence class; identifier remains unassigned.
3. `second-usage-source` — negative, P07. A second measurement model is cited for allowance projection → rejected; WM-FLW-015 is the sole usage authority.
4. `unpinned-subscription-binding` — negative, P14. Binding cites a subscription without version, revision or as-of time → rejected as non-reproducible.
5. `unpinned-usage-binding` — negative, P14. Usage projection binding omits as-of time → rejected.
6. `binding-edited-in-place` — negative, P14, P16. A binding is mutated instead of superseded → rejected; bindings are append-only.
7. `overage-in-profile` — negative, P01, P05. Overage or refund held as profile or entitlement state → rejected; materialized on WM-ECO-008 lines.
8. `availability-implies-entitled` — negative, P13. Successful service access treated as proof of an active grant → rejected.
9. `entitlement-restriction-independent-basis` — positive, P12, P13. Nonpayment suspends the subscription; any grant restriction requires its own assertion, basis and effective time; months 1–3 remain unrewritten.
10. `revision-vs-successor-boundary` — positive. Allowance-only change yields a revision; subject, scope or grant-basis change yields a new candidate entitlement; all prior revisions stay resolvable.
11. `head-revision-term-conflict` — negative, P01. Head and current revision disagree on permission, scope or period → rejected; terms are revision-mastered only.
12. `entitlement-id-recycled` — negative. A retired entitlement identifier or revision number is reused → rejected; retired identifiers and revisions remain resolvable and are never recycled.
13. `fulfilment-evidence-unmastered` — negative, P08. Despatch evidence admitted with no named fulfilment-evidence master while WM-ECO-024 is unverified → blocked pending boundary adjudication.
14. `candidate-asserts-line-quantity` — negative, P02. Candidate or profile asserts delivered, outstanding or allocated line quantity → rejected; WM-ECO-020 owns line quantity progress.
15. `gate-partial-evidence` — positive, P15. One promotion evidence item is present → adjudication opens; allocation state stays `unassigned`.
