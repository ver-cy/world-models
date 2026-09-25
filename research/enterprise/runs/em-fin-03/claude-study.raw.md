# EM-FIN-03 Boundary Review

## Verdict

**PROFILE** — over WM-ECO-009 primarily, with reciprocal constraints on WM-ECO-008. No new catalogue or runtime identifier.

Allocation has *local* identity (an addressable, signed, reversible entry) but no lifecycle independent of the two aggregates it joins. Every allocation state change is triggered elsewhere: by payment finality, return or reversal in WM-ECO-009, or by correction, cancellation or dispute in WM-ECO-008's correction chain. Reconciliation is already an owned serial artefact (`reconciliation-result-set`, run-keyed) inside WM-ECO-009. Neither proves independent lifecycle, so the registry rule bars a third model — and no third candidate ID exists in `candidate_ids` anyway. Allocation therefore remains **owned semantics of WM-ECO-009**, published as the EM-FIN-03 profile.

## Boundary

**Reuse as-is:** `obligation-discharge-and-allocation`, `remittance-information-and-purpose`, `reconciliation-and-accounting-handoff`, `settlement-finality-and-obligation-discharge`, `returns-reversals-and-recalls` (WM-ECO-009); `fnd-totals-rounding-and-arithmetic-consistency`, `fnd-payment-means-terms-and-due-date`, `fnd-preceding-document-and-correction-chain`, `fnd-buyer-response-and-dispute`, `art-correction-chain-graph` (WM-ECO-008).

**Owned by WM-ECO-009 under profile:** the allocation entry, residual derivation, FX/rounding attribution, allocation reversal, match state.

**Owned by WM-ECO-008:** admissible amount (net claim from the correction chain less prepaid), dispute state, cancellation-versus-credit mechanism choice. Settlement state is never written back — the existing `q-payment-settlement-boundary` rule is preserved unchanged.

**No new aggregate.** The only candidate with a plausible independent claim — a *disputed residual* — resolves to two existing states in combination (`de-dispute-state` on the document, `reconciliation-break-reference` on the payment) and needs a binding, not an aggregate.

## Required semantics

1. **Allocation entry as a tuple.** WM-ECO-009 currently exposes `discharged-obligation-reference` (0..n) and `allocated-amount` (0..n) as two parallel flat lists with no binding. This cannot express n×m safely. The profile must constrain them into an entry: `(payment master id, document authoritative id, sequence, signed amount, document currency, allocating party, allocation instant, basis)`. Sequence-keyed, never date-keyed.
2. **Allocating party is mandatory.** `payment-allocation-advice` is issued "by or on behalf of the payer", but the payee also allocates on cash application. The profile must distinguish *asserted* allocation from *accepted* allocation and keep both; divergence is a break, not a merge.
3. **Residual is derived, not stored per payment.** `residual-obligation-balance` at 0..n on each payment produces conflicting snapshots when several payments hit one invoice. Profile: residual is a function of the full allocation set against a document plus the chain's net claim, computed at an instant, never an authoritative field.
4. **Cross-currency allocation is three values, not one.** Allocated amount in document currency, FX difference and rounding difference, each signed and separately attributed, each bound to an `exchange-rate-quote-record` and, where the document carries a tax accounting currency, to `de-exchange-rate-basis`. Differences are never absorbed into the allocated amount.
5. **Overpayment is an explicit outcome.** Unallocated surplus is retained as a stated residual with a disposition (refund as a new payment, credit balance, or allocation to a future document). It may not be silently absorbed.
6. **Reversal is counter-entry.** Post-finality recovery produces a new payment (`q-post-finality-reversal`) plus a signed counter-allocation. The original allocation and the original payment stay intact and final.
7. **Two distinct "three-way matches."** WM-ECO-008's `fn-match-to-order-and-receipt` (invoice/order/receipt) and WM-ECO-009's `q-match-state` (instruction/settlement/statement) share a name and share nothing else. The profile must namespace them. This is the concrete mechanism by which "reconciliation proves delivery" leaks in.

## Invariants

- **I1** Payment master identifier and document authoritative identifier are never merged, substituted or co-keyed; an allocation references both and owns neither.
- **I2** Σ allocations to one document ≤ admissible amount at the allocation instant, unless an explicit overpayment or exception code is recorded.
- **I3** Σ allocations from one payment ≤ settlement amount net of charge-bearer deductions (not instructed amount).
- **I4** Closure is derived: residual = 0 **and** no open dispute **and** payment final **and** no discharge exception invoked. It is never an asserted field.
- **I5** Reconciliation match state is not an input to any fulfilment or delivery assertion, and carries no evidential weight for supply. Cross-reference from match state to `art-matching-result-record` is forbidden.
- **I6** Discharge is asserted only at finality, and remains defeasible under the four recognised exceptions.
- **I7** Allocations are append-only; correction is by signed counter-entry.

## Scenario walkthrough

**Negative case — one payment closing two invoices.** Payment settles 1,000; invoices A and B are 600 each. Failure path is amount-blind matching plus asserted closure. I3 fires first (1,200 > 1,000). If the payer advice instead states 500/500, I2 passes but I4 blocks closure on both: residual 100 each. Two ageing breaks are raised in `reconciliation-result-set` with owners; neither document changes state. Matching binds on `de-remittance-reference`, with truncation signalled per `q-remittance-truncation` — never on amount equality.

**Acceptance case — cross-currency, two documents, disputed remainder.** USD payment; EUR documents. Settlement amount ≠ instructed amount; `q-amount-divergence` records cause. Rate pinned to one `exchange-rate-quote-record`; conversion party and quotation time captured. Document A allocated in full; FX difference and rounding difference booked separately and attributed. Document B allocated partially; the remainder is disputed — `de-dispute-state` on B with coded reason, residual explicit, break open, discharge partial, closure withheld. Payment remains final throughout.

**Cancellation versus correction.** A cancelling document voids the claim: admissible amount falls to zero, existing allocations become overpayment. A credit note reduces net claim via the chain graph, potentially to negative residual → refund path. Neither edits the original document or silently re-allocates.

## Gaps and publication holds

- Both parents are `reviewable-draft` / `publishableCanonical: false`. **A profile cannot be published ahead of its parents**; EM-FIN-03 inherits all holds from both.
- WM-ECO-008's registry-metadata hold (conflicting `registry_id`, unreconciled alias, empty parent) must be closed first — a profile with no new ID resolves through the parent's identity.
- The **missing Account and Holding sibling** is the sharpest gap: overpayment held as a credit balance has no home and will be absorbed into WM-ECO-009 by default. Hold I5's overpayment-as-credit-balance option until that neighbour is registered.
- WM-ECO-009's multi-profile and regime-scoping holds apply directly: revocability and return windows differ per rail and change residual revival timing.
- Not resolvable from this dossier: which party's allocation prevails on divergence absent contractual appropriation rules, and the EN 16931 prepaid-amount versus allocation overlap.
