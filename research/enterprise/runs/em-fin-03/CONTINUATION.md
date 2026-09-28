# EM-FIN-03 continuation

## State

The invoice, payment and reconciliation contour is provider-reconciled and frozen-audited. Claude and Grok independently select **PROFILE** over WM-ECO-009 with reciprocal constraints on WM-ECO-008 and no new catalogue or runtime identifier.

Payment Allocation remains an append-only payment-owned tuple keyed by payment, document and sequence. Reconciliation remains a run-keyed payment-owned result. Neither has identity or lifecycle independent of the parent payment and commercial document aggregates. WM-ECO-008 owns issued-document identity, correction chain, dispute and admissible claim; WM-ECO-009 owns instruction, settlement, finality, return, allocation, remittance and reconciliation.

The single Claude frozen audit returned **ACCEPT WITH LIMITS**. CandidateRevision 3 closes its findings without rerunning the audit: closure is read-side only; short-pay basis is a set of coded signed amounts; charge deductions are a separate money bucket; recovery uses signed direction-aware conservation; and factoring requires external assignment authority or fails closed.

## Validation

- profile: 15 constraints, 2 base models, 2 external references, no runtime ID;
- fixtures: 20 positive and negative cases;
- no model or registry identifier is created or reserved.

## Holds

- WM-ECO-008 and WM-ECO-009 remain non-canonical reviewable drafts;
- Account/Holding ownership for credit balance is unresolved;
- receivables-assignment authority is external and unresolved in this contour;
- appropriation priority and rail-specific return/revocability rules require regime profiles;
- ISO 20022, UBL and EN 16931 crosswalks remain unpinned alignment targets;
- WM-ECO-016 remains the external posting authority;
- canonical publication and live verification remain held.

## Next safe step

Retain this reviewable research profile without publishing it ahead of its parents. Continue with EM-KNW-01 only after fresh action-time confirmation for its saved Grok prompt.
