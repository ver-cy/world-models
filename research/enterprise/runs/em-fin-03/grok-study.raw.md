**Verdict: PROFILE** over WM-ECO-009, with reciprocal reference constraints on WM-ECO-008. No new catalogue or runtime ID.

## Identity and lifecycle test

**Source (WM-ECO-008).** Document identity is issuer + number, outranked by an authority clearance identifier where one exists. Content is frozen at issue. Payment means, terms, due date and remittance reference are issue-time assertions. “Whether payment occurred, when, and in what amount is governed by the settlement model and must never be written back into the issued document.” Correction, credit, debit and cancel are further documents that refer to the original; the chain, not in-place edit, is the history of the claim. Dispute suspends payment expectation without altering the document. Fulfilment references (order, despatch, receiving advice) exist for matching only. Outstanding is derived.

**Source (WM-ECO-009).** Payment owns instruction, settlement, finality, return and remittance identities. “Allocation is an explicit many-to-many structure with residuals; it cannot be inferred from amount matching alone without producing silent misallocation.” Charge-bearer deductions may diverge from discharge of the obligation; both must be represented. Returns are new opposite-direction payments; the original remains final. Reconciliation is a run result set: matched sets, unmatched items, break classifications, then an accounting handoff that does not own posting rules.

**Source (EM-FIN-03 card).** Payment and document have different IDs; an allocation must not exceed the allowed amount without explanation; reconciliation does not confirm delivery. Candidates remain conceptual; no completed semantic crosswalk.

**Inference.** Allocation identity is the tuple (payment ID, document ID, sequence). It cannot be created, reversed or closed without a living payment and a living document. Reconciliation identity is a run key plus as-of instant and scope. Neither has an autonomous lifecycle in the published parents.

**Payment Allocation and Reconciliation do not deserve separate aggregates.** An allocation cannot exist, reverse or close without its payment and its document. A reconciliation result cannot exist without the run that produced it. ISO 20022 `RfrdDocInf` / `RfrdDocAmt` and UBL RemittanceAdvice are projections of the tuple, not masters. SAP clearing-document numbers and Oracle application IDs are implementation identifiers, not evidence of a Vercy aggregate. Minting a third model would duplicate 009 obligation-linkage and 008 correction-chain ownership.

Do not conflate three reconciliation senses: (1) cash application of a payment to documents — this profile; (2) bank/statement match already inside 009; (3) AP three-way PO/GR match — out. Rule 8 and 008 fulfilment-refs-only keep (3) outside this contour.

## Missing semantics to profile, not mint

- Three voices: payer-advised, payee-applied, accepted. Disagreement is a break, not a silent overwrite.
- Residual at instant T is derived: document-chain net at T minus accepted allocations as-of T. Never stored back onto the issued document.
- Six distinct money facts: settlement amount; document-currency allocation; FX difference; rounding difference; rate quote / basis / time / source; unallocated residual. Bind WM-XCT-032 by reference; do not re-own money math.
- Overpayment is a payment-side residual, not a silent invoice credit. On-account cash is a payment with an empty allocation set.
- Reversal or return is a new payment plus signed counter-allocation. Original tuples stay (append-only).
- Charge-bearer deductions ≠ discharge amount (already warned in 009).
- Payee may differ from seller (factoring). Allocation keys document + payment, not seller.
- Short-pay reasons (discount, credit, adjustment) travel as allocation basis, aligned with ISO 20022 `DscntApldAmt` / `AdjstmntAmt` / `CdtNoteAmt`.
- Closure is derived, not a writable status.
- Discharge-exception codes must be explicit so a zero residual cannot close a contested claim.

## Corrected invariants

1. Payment ID ≠ document ID. Remittance reference is a correlator, never a merge key. Settlement is never written onto the issued document.
2. Each allocation tuple binds payment ID, document ID, sequence, signed amount and currency, allocating party, time and basis. Append-only; no in-place edit.
3. Preserve payer-advised, payee-applied and accepted voices. Disagreement is a break.
4. Residual(T) = f(accepted allocations to T, 008 chain at T). A later credit or cancel does not delete prior allocations.
5. Keep settlement amount, document-currency allocation, FX difference, rounding difference, rate quote/basis/time/source and unallocated residual distinct.
6. Overpayment is explicit on the payment. Post-finality reversal creates a new opposite payment and signed counter-allocations.
7. Closure only if zero residual ∧ settlement finality ∧ no open dispute ∧ no discharge exception.
8. Payment reconciliation never proves order fulfilment or delivery. Cancel after allocation is an 008 chain event, not a payment reversal.

## Scenario results

**Negative — 1,000 paid against two invoices of 600.** Fail. Accepted allocations cannot exceed 1,000. Full close of both is illegal. At least 200 remains as document residual, payment residual, or a documented over-allocation break.

**Acceptance — final USD payment allocated to two EUR documents.** One document may close only if its document-currency residual is zero and the other three closure predicates hold. The other keeps an explicit disputed remainder. FX difference and rounding difference stay separate disclosed amounts; the rate quote is pinned. Differences are never folded into residual.

**Cancel versus credit after an allocation exists.** Both are new 008 documents. Existing allocation tuples remain. Residual is recomputed from the full allocation set plus the chain. Cancel is not a payment reversal. A credit note may itself be allocated.

**N:1, 1:N, overpayment, post-finality reversal.** All via append-only tuples on the payment(s). Several payments against one invoice and one payment against several invoices are the same structure. Overpayment remains on the payment. After finality, reversal adds a new opposite payment and signed counter-allocations; originals stay.

## Publication blockers

Both parents are reviewable drafts with open source-verification, authority-tier and multi-profile holds. A profile cannot become canonical ahead of its parents. Three-voice state, the six money buckets and the as-of residual function are not pinned in parent text. No fixtures exist for the four required cases. ISO 20022 remt/pacs, UBL RemittanceAdvice and EN 16931 BT-83 crosswalks remain unpinned. Accounting handoff stays a reference to WM-ECO-016; this profile does not own posting. Do not invent a catalogue or runtime identifier. Do not let cash-application absorb bank reconciliation or PO/GR match.