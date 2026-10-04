# Independent review request: EM-FIN-03 Invoice, payment and reconciliation

Review this proposed Enterprise boundary independently. Use public standards and mature ERP/accounting practice where useful, but distinguish observed source facts from your design inference. Do not invent a Vercy catalogue/runtime identifier.

Current Vercy parents:

- WM-ECO-008 Invoice / Commercial Document owns document identity, lines, totals, due terms, dispute state, fulfilment references and immutable correction/credit chains. It excludes payment execution, settlement, clearing and reconciliation.
- WM-ECO-009 Payment owns payment instruction and settlement identities, finality, returns/reversals, allocation across obligations, remittance and reconciliation/accounting handoff.
- Both are published research specifications but remain reviewable drafts with publication holds.

Proposed decision: **PROFILE**, primarily over WM-ECO-009 with reciprocal reference constraints on WM-ECO-008. No new model ID. Allocation is an append-only owned entry that references one payment and one document; reconciliation is a run-keyed owned result. Neither has an independent lifecycle in the available evidence.

Required profile rules:

1. Never merge payment and document identities.
2. Bind each allocation tuple to payment ID, document ID, sequence, signed amount/currency, allocating party, time and basis.
3. Preserve payer-advised, payee-applied and accepted allocations; disagreement is a break.
4. Derive residual from the complete allocation set plus the document correction chain at an instant.
5. Keep settlement amount, document-currency allocation, FX difference, rounding difference, rate quote/basis/time/source and unallocated residual distinct.
6. Model overpayment explicitly; reversal creates a new payment and signed counter-allocation.
7. Derive closure only from zero residual, finality, no open dispute and no discharge exception.
8. Payment reconciliation never proves order fulfilment or delivery.

Test these cases:

- Negative: one payment of 1,000 is made to close two invoices of 600 each fully.
- Acceptance: a final USD payment is allocated to two EUR documents; one closes and one keeps an explicit disputed remainder, with FX and rounding differences retained separately.
- Cancellation versus credit correction after an allocation already exists.
- Multiple payments to one invoice, one payment to multiple invoices, overpayment and post-finality reversal.

Return at most 900 words with: Verdict (REUSE ONLY / PROFILE / NEW MODEL); independent identity/lifecycle test; missing semantics; corrected invariants; scenario results; publication blockers. State explicitly whether Payment Allocation or Reconciliation deserves a separate aggregate and why.
