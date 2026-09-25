# EM-FIN-03 local synthesis

## Disposition

- Create a thin **Enterprise invoice-payment allocation profile** over WM-ECO-009, with reciprocal reference constraints on WM-ECO-008.
- Do not create a new catalogue or runtime identifier.
- Keep Payment Allocation and reconciliation results as owned, addressable records inside Payment. Their changes follow payment finality/reversal or document correction/dispute; the dossier does not prove an independent lifecycle.

## Boundary

WM-ECO-008 owns the authoritative commercial document, lines, amount arithmetic, due terms, dispute state and immutable correction/credit chain. WM-ECO-009 owns payment instruction and settlement identities, finality, reversals, allocation to obligations, remittance and reconciliation handoff. The profile binds the two without merging their identifiers or writing a settlement state into the invoice.

An allocation is an append-only entry referencing one payment and one commercial document. It owns neither. A reconciliation result is a run-keyed serial artefact of Payment and cannot establish fulfilment or delivery.

## Required profile semantics

1. Bind every allocation as a tuple: payment master ID, document authoritative ID, sequence, signed allocated amount, allocation currency, allocating party, allocation instant and basis.
2. Distinguish payer-advised, payee-applied and accepted allocations. Preserve disagreements as reconciliation breaks.
3. Derive document residual from the full allocation set and the document correction chain at an instant. Do not store conflicting residual snapshots on individual payments.
4. For cross-currency allocation, preserve settlement amount/currency, document-currency allocation, exchange-rate quote and basis, rate time and source, separately signed FX and rounding differences, and any unallocated residual.
5. Represent overpayment explicitly as unallocated surplus with a governed disposition. Credit-balance treatment stays blocked until an Account/Holding owner exists.
6. Represent post-finality recovery as a new payment plus counter-allocation. Never mutate the original final payment or allocation.
7. Namespace invoice/order/receipt matching separately from payment/settlement/statement reconciliation.

## Invariants

1. Payment and commercial-document identifiers remain distinct.
2. Allocations from one payment cannot exceed its final settlement amount net of explicitly modelled deductions.
3. Allocations to one document cannot exceed its admissible net claim without an explicit overpayment or exception outcome.
4. Closure is derived from zero residual, final payment, no open dispute and no discharge exception.
5. Reconciliation has no evidential effect on delivery or fulfilment.
6. Correction uses a signed counter-entry; prior entries remain immutable.

## Acceptance result

A final USD payment can allocate document-currency amounts to two EUR documents using a pinned rate. One document closes; the other retains a disputed residual and an open reconciliation break. FX and rounding differences remain separate. The payment stays final, invoice identities remain unchanged and no delivery claim is inferred.

The negative case fails: a settlement of 1,000 cannot fully close two claims of 600 each. Source-side conservation rejects 1,200; a valid 500/500 allocation leaves two residuals of 100.

## Holds

Both parent models remain reviewable drafts with `publishableCanonical: false`; EM-FIN-03 inherits their source, registry, multi-profile and regime-scoping holds. The missing Account/Holding boundary prevents claiming a universal credit-balance disposition. Contractual appropriation priority and EN 16931 prepaid-amount overlap remain unresolved. This checkpoint is research evidence, not an installable release.
