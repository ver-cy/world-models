# EM-FIN-02 local synthesis

## Disposition

- Reuse WM-ECO-015 only for externally serviced Financial Accounts such as bank and custody accounts.
- Reuse WM-ECO-016 for ledger-local Financial Transaction / Journal Entry and contained Posting lines.
- Reuse WM-ECO-017 for derived, time-bound balances and positions; treasury position and GL balance remain distinct.
- Introduce an identifier-unassigned **Chart of Accounts / Accounting Policy** candidate that masters CoA versions, Ledger Accounts, ledger adoption and effective accounting rules.
- Define a thin correspondence-only Enterprise Financial Event and Multi-Ledger Binding profile. It allocates no identity or runtime ID.

## Identity and mastership

Financial Account identity is issuer/custodian plus external identifier and is mastered by WM-ECO-015. Ledger Account identity is ledger plus effective Chart node/version and interval and is mastered only by the unassigned candidate. WM-ECO-016 owns one-ledger entries and their posting lines. WM-ECO-017 owns balances qualified by ledger, account, currency, scope and as-of time. External events, payments and invoices keep their own masters and are referenced only by pinned correlation.

## Boundary rules

A posting target is always a Ledger Account, never a raw WM-ECO-015 Financial Account. A Ledger Account may optionally map to at most one externally serviced backing account for a declared context and interval; the mapping is not identity. Account codes are never global and code equality across ledgers or chart revisions proves no equivalence.

One external event may correlate to sibling entries in several ledgers. Every sibling belongs to one ledger, cites the event, records a divergence reason when amount, timing, account, policy or currency differs, and balances independently. No cross-ledger netting, plugging, tolerance or correction is permitted.

## Currency, close and correction

Balancing is evaluated only within one ledger, declared balancing currency role, scope and tolerance. Settlement currency, transaction currency, functional currency and presentation currency remain explicit roles. Translation residuals post inside the same ledger.

Posted entries and lines are immutable. A correction appends a linked same-ledger entry. An open book reverses or adjusts in an open period. A hard-closed book uses the earliest permitted later period or an explicitly authorised hard-close exception. Correcting one sibling does not change another. Closed WM-ECO-017 balances remain immutable and successor balance assertions carry their own as-of time.

## Provider reconciliation

Grok conditionally accepted the reuse split but rejected Ledger Account as a WM-ECO-015 profile. The reconciled candidate owns Ledger Account under the Chart-of-Accounts lifecycle. The profile now records only source-pinned correspondence and optional backing mappings and cannot master or mutate any source object.

## Holds

The candidate has no registry allocation. WM-ECO-015/016/017 remain reviewable drafts with contradictory ownership text. Financial Transaction naming, currency roles, scope dimensions, tolerance units, CoA-to-ledger cardinality and hard-close policy need canonical adjudication. No publication or installability claim is made.

## Frozen-audit remediation

Exactly one Claude Opus high no-tools audit returned REJECT FOR ALLOCATION and required candidate revision 3. All twenty-one material defects were remediated without rerun: definition/instance mastership is separated; LedgerPeriod owns close state; WM-ECO-016 owns closed-kind correction links; Ledger Account has stable identity plus versions; interval/code uniqueness and exact posting target are explicit; context-qualified backing mappings are representable; lifecycle, adoption and policy precedence are closed; accountingDate/recordedAt, currency roles, FX pins, scope vector and exact-zero balancing are explicit; event correlation is many-to-many; all balance assertions are immutable; the profile has an unassigned required base, non-subject local binding keys and stable constraint ids; thirty-eight stable-id fixtures cover the rules. Allocation and publication remain held.
