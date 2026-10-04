# Verdict

**ACCEPT WITH LIMITS.** PROFILE over WM-ECO-009 with reciprocal constraints on WM-ECO-008 is the correct disposition. Research profile at candidateRevision 2 may stand as evidence; canonical publication is blocked.

# Critical findings

**1. Aggregate rejection is sound.** Allocation identity is the tuple `(payment ID, document ID, sequence)` — it cannot be created, reversed or closed without a living payment and a living document, and every state transition originates in WM-ECO-009 finality/return or the WM-ECO-008 correction chain. Reconciliation is a run-keyed serial artefact already owned by WM-ECO-009. Neither exhibits autonomous lifecycle; the disputed-residual candidate decomposes into document dispute state plus payment break reference, which needs a binding, not an aggregate. Rejection holds.

**2. Authority separation holds with one seam.** Correction/dispute (008), finality/return (009) and allocation/reconciliation (009 under profile) are cleanly assigned, and settlement is never written back. The seam is closure: constraint 13 spans all three authorities. It must be stated as a read-side derivation owned by no authority, not merely "not writable" — otherwise the first implementation materialises it on the payment.

**3. Short-pay basis is underspecified — genuine inconsistency.** Constraint 2 pins one scalar `basis` per tuple; constraint 9 requires discount, credit and adjustment reasons to travel on that basis. A single scalar cannot carry several coded reasons with amounts, so a mixed short-pay silently collapses into allocated amount — exactly what the `charge-equals-discharge` fixture is meant to forbid. Basis must be a set of (reason code, signed amount) summing to the deduction.

**4. Charge-bearer deductions are missing from the money enumeration.** Constraint 5 lists six distinct money facts; constraint 6 introduces deductions as a seventh without granting them bucket status. Add them, or the `absorbed-fx` guard has no analogue for charges.

**5. Conservation is written unsigned.** Constraint 6 ("cannot exceed final settlement amount") does not survive the opposite-direction payment of constraint 11. Restate signed, per payment direction, or recovery payments are unconstrained.

**6. Factoring is only half-constrained.** Constraint 10 permits payee ≠ seller but nothing models assignment or notification, so a factor's standing to accept allocations against a document is unproven. Neither parent owns assignment of receivables.

**7. Cross-proof separation is adequate.** Constraints 14–15 and the two negative fixtures are bidirectional and close the shared "three-way match" naming leak. No further defect.

**8. Fixture coverage is insufficient for promotion.** Missing: closure asserted as writable status; residual revival on the document after return; empty accepted set arising from voice disagreement; credit note exceeding accepted allocations producing negative residual and refund path; multi-reason short-pay.

# Required holds

- Both parents are reviewable drafts, `publishableCanonical: false`; the profile cannot promote ahead of them. WM-ECO-008's registry-metadata conflict must close first, since a profile without its own ID resolves through the parent's identity.
- No Account/Holding owner: on-account cash and overpayment stay payment-side residual only; credit-balance disposition remains unstated.
- Contractual appropriation priority is unresolved — no tie-break exists when payer-advised and payee-applied voices diverge. Disagreement may only produce a break.
- Rail-specific return/revocability windows require regime profiles; they govern residual revival timing.
- ISO 20022, UBL RemittanceAdvice, EN 16931 BT-83 and the prepaid-amount overlap remain unpinned alignment targets.
- WM-ECO-016 stays the external posting authority; this profile owns no posting rules.
- Findings 3–6 and the fixture gaps are revision holds on candidateRevision 3.

# Scenario result

Negative 1000/600+600: source-side conservation rejects 1200 at accepted-allocation time; 500/500 passes conservation but closure is withheld on both (residual 100 each), raising two owned breaks. Positive cross-currency: settlement, document-currency allocations, pinned rate quote, FX and rounding differences stay distinct; document A closes, B retains disputed residual with an open break; payment stays final; no delivery inferred. Cancel-after-allocation recomputes residual through the chain, leaves tuples intact and surfaces surplus as payment-side overpayment, not reversal. Remaining fixtures pass as written.

# Identifier decisions

No new catalogue or runtime identifier. EM-FIN-03 remains a contour identifier; the profile resolves through WM-ECO-009. WM-XCT-032 and WM-ECO-016 are references only. No registry reservation created, mutated or released; no identifier allocated; no publication authority granted.
