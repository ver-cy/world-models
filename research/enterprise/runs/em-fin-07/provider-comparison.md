# EM-FIN-07 provider comparison

Claude and Grok agree that WM-POL-011 owns obligations and authority assessments, WM-ECO-032 owns return revisions, filing attempts and authority responses, calculations remain owned assertions, WM-ACT-052 is thin case correlation, and TaxRegistrationAccount is an optional independently identified but unallocated candidate. No catalogue, model or runtime identifier is allocated.

## Divergences and resolution

- **Balance placement.** Grok allowed account- or obligation-scoped balance; Claude and the preserved boundary require obligation-only placement. The frozen resolution keeps every balance and due position in WM-POL-011.
- **Calculation owner set.** Grok proposed ReturnRevision, Obligation or Assessment; Claude was ambiguous. The frozen resolution permits exactly ReturnRevision or Obligation. Authority-assessed calculations are Obligation-owned with an assessment correlation.
- **Account optionality.** Grok proved the withholding-only path can carry an event, obligation and payment with zero account and zero return. The frozen resolution adopts that stronger optionality and makes basis assertions independently resolvable.

Canonical machine name is `TaxRegistrationAccount`; display name is `Tax registration account`. Slash forms are forbidden. Provider invariant lists are non-normative appendices; `invariants.json` is the sole normative set. Scenario labels are fixture-local and collision-free.

Publication remains held by the unallocated candidate, unresolved canonical aggregate relations, unverified base pins, opaque external version owners, and the registry `parent_ids` versus empty relation-ledger contradiction.
