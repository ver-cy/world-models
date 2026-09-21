# Lifecycle, guards and effects

| Operation | Actor and guard | Effect and evidence |
|---|---|---|
| Draft → immutable proposal revision | Host-authorized proposer; complete closed metadata and qualified pins | seal validates structure/digest; import merges into complete register; host persists atomically and records provenance. No review implied. |
| Proposal → revised proposal | Authorized proposer; same identity and new opaque revision, or new identity if package purpose/boundary no longer denotes the same governed proposal | Old bytes retained; new digest; old review pins do not apply. The semantic identity decision is host-owned. |
| Record review | Attributed reviewer with separately checked write authority; exact proposal, method, evidence and ordered times | Immutable cleared/rejected/inconclusive assessment; import checks internal links; current read applicability independently checks authority. |
| Correct review | Authorized reviewer/correction owner; new revision; optional exact supersedes link with same proposal identity and nondecreasing assessment time | Prior evidence preserved; active selection is a separate governance action, not a side effect of import. |
| Select/withdraw current review | Authorized host governance operator; complete history and identity resolved | New external snapshot; no record mutation. Active and withdrawn sets cannot overlap. Host also deactivates transitive predecessors. |
| Expiry/context drift/authority change | Evaluated under current authorized snapshot and clock | Derived insufficient-context/stale/conflict/rejected/inconclusive/applicable-review result; historical recorded verdict remains unchanged. |
| Replay/import conflict | Authorized host importer; complete bounded store and exact bytes | Exact replay idempotent; same revision with different bytes rejects transaction; no silent winner. |
| Dispose record | Separate actual custodian and policy; outside this reference | No method implemented. Neither immutability nor a retained digest proves an obligation to keep records forever or successful erasure. |

Capture, assessment, review validity, host snapshot as-of and native storage receipt are separate axes. Revision strings do not order time. Native object active state is storage lifecycle, not an applicable review verdict. Restoration, durable conflict recording and clock recovery are host obligations.
