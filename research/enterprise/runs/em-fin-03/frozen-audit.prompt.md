# Frozen no-tools semantic audit — EM-FIN-03

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers, mutate registry reservations or grant publication authority.

Disposition: PROFILE over WM-ECO-009 with reciprocal constraints on WM-ECO-008; no new catalogue or runtime identifier. Payment Allocation and Reconciliation remain payment-owned semantics. Audit semantics only.

Audit questions:
- Do allocation and reconciliation lack independent identity and lifecycle strongly enough to reject a new aggregate?
- Are document correction/dispute, payment finality/return and allocation/reconciliation authorities kept separate?
- Are the three allocation voices, as-of residual, money buckets, overpayment, factoring, short-pay and reversal semantics internally consistent?
- Are cash application, bank/statement reconciliation and invoice/order/receipt matching prevented from proving one another?
- Which holds permit a research profile but block canonical publication?

Return at most 600 words with exactly: Verdict (ACCEPT WITH LIMITS, REVISE, or REJECT); Critical findings; Required holds; Scenario result; Identifier decisions. Registry mutation and identifier allocation remain holds.

## Profile candidate

{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-FIN-03",
  "name": "Enterprise Invoice-Payment Allocation",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": [
    "WM-ECO-009",
    "WM-ECO-008"
  ],
  "constraints": [
    "Commercial-document and payment identifiers remain distinct; remittance references correlate and never merge identity.",
    "Each append-only allocation tuple pins payment ID, document ID, sequence, signed amount and currency, allocating party, allocation instant and basis.",
    "Payer-advised, payee-applied and accepted allocations remain distinct voices; disagreement creates a reconciliation break and never overwrites another voice.",
    "Document residual at instant T derives from accepted allocations through T plus the complete WM-ECO-008 correction chain at T and is never written onto the issued document.",
    "Settlement amount, document-currency allocation, FX difference, rounding difference, rate quote/basis/time/source and unallocated payment residual remain distinct money facts governed by WM-XCT-032 references.",
    "Accepted allocations from one payment cannot exceed final settlement amount net of explicit charge-bearer deductions; charge deductions and obligation discharge remain distinct.",
    "Accepted allocations to one document cannot exceed its admissible chain-derived claim without an explicit overpayment or exception outcome.",
    "Overpayment remains an explicit payment-side residual; on-account cash is a payment with an empty accepted-allocation set and no inferred invoice credit.",
    "Short-pay discount, credit and adjustment reasons travel on the allocation basis and are never silently absorbed into allocated amount.",
    "Payee may differ from seller; allocation keys payment and document masters rather than seller identity.",
    "Post-finality return or recovery creates a new opposite-direction payment and signed counter-allocation; original payment and tuples remain immutable and final.",
    "Invoice cancellation or credit is a WM-ECO-008 chain event; it recomputes residual without becoming a payment reversal or deleting prior allocations.",
    "Closure is derived only from zero residual, settlement finality, no open dispute and no discharge exception; it is never a writable allocation status.",
    "Cash application, bank or statement reconciliation, and invoice/order/receipt matching are separately namespaced and never treated as evidence for one another.",
    "Payment reconciliation never establishes delivery or fulfilment and accounting handoff never owns posting rules."
  ],
  "candidateRevision": 2,
  "references": [
    "WM-XCT-032",
    "WM-ECO-016"
  ],
  "holds": [
    "WM-ECO-008 and WM-ECO-009 are non-canonical reviewable drafts and the profile cannot promote ahead of them.",
    "Account or Holding ownership for credit balances is unresolved; on-account cash therefore remains payment-side residual only.",
    "Contractual appropriation priority and rail-specific return or revocability rules require regime profiles.",
    "ISO 20022, UBL RemittanceAdvice and EN 16931 BT-83 crosswalks remain unpinned alignment targets.",
    "WM-ECO-016 remains the external accounting-posting authority."
  ]
}


## Fixtures

{
  "format": "vercy-enterprise-profile-fixtures/v1",
  "profileName": "Enterprise Invoice-Payment Allocation",
  "cases": [
    {
      "id": "cross-currency",
      "kind": "positive",
      "input": "One final USD payment allocates to two EUR documents using a pinned rate.",
      "expect": "Settlement, document allocations, rate source, FX and rounding differences remain distinct; one document may close while the other retains a disputed residual."
    },
    {
      "id": "multiple-payments",
      "kind": "positive",
      "input": "Several final payments allocate to one invoice.",
      "expect": "Residual derives from the complete accepted-allocation set and correction chain at the requested instant."
    },
    {
      "id": "one-to-many",
      "kind": "positive",
      "input": "One payment allocates to several invoices.",
      "expect": "Each tuple is separately sequenced and source-side conservation applies across all accepted allocations."
    },
    {
      "id": "on-account-cash",
      "kind": "positive",
      "input": "A final payment arrives without an accepted document allocation.",
      "expect": "The payment remains with an explicit unallocated residual and no invoice credit is inferred."
    },
    {
      "id": "factoring",
      "kind": "positive",
      "input": "The payee is a factor and differs from the seller that issued the document.",
      "expect": "Allocation keys payment and document identities and preserves party roles without requiring payee equals seller."
    },
    {
      "id": "recovery",
      "kind": "positive",
      "input": "Funds are recovered after payment finality.",
      "expect": "A new opposite-direction payment and signed counter-allocation preserve the original final payment."
    },
    {
      "id": "cancel-after-allocation",
      "kind": "positive",
      "input": "An issued document is cancelled after an accepted allocation exists.",
      "expect": "The correction chain recomputes residual; prior tuples remain; cancellation is not a payment reversal."
    },
    {
      "id": "voice-disagreement",
      "kind": "negative",
      "input": "Payer advice and payee cash application disagree and one silently overwrites the other.",
      "expect": "Validation rejects the overwrite and requires a reconciliation break."
    },
    {
      "id": "over-allocation",
      "kind": "negative",
      "input": "A settlement of 1000 fully closes two claims of 600 each.",
      "expect": "Source-side conservation rejects accepted allocation of 1200."
    },
    {
      "id": "absorbed-fx",
      "kind": "negative",
      "input": "FX and rounding differences are folded into document allocation or residual.",
      "expect": "Validation rejects conflated money facts."
    },
    {
      "id": "charge-equals-discharge",
      "kind": "negative",
      "input": "A charge-bearer deduction is treated automatically as discharged obligation amount.",
      "expect": "Validation rejects the inference without an explicit basis or exception."
    },
    {
      "id": "reconciliation-proves-delivery",
      "kind": "negative",
      "input": "A cash-application or bank match is treated as evidence that goods were delivered.",
      "expect": "The inference is rejected."
    },
    {
      "id": "three-way-conflation",
      "kind": "negative",
      "input": "Invoice/order/receipt matching is merged with payment/statement reconciliation.",
      "expect": "Validation rejects the namespace and evidence conflation."
    }
  ],
  "candidateRevision": 2
}


## Local evidence

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


## Claude study

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


## Grok study

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
