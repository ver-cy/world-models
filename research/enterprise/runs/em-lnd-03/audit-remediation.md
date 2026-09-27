# EM-LND-03 audit remediation

The single frozen Claude audit returned `REVISE`. Its six coherence findings were incorporated without adding an aggregate or identifier; the audit was not repeated.

- The dual-employment fixture now sources 0.6 and 0.5 from WM-ORG-016 assignment allocations and labels the 1.1 result `assignment allocated supply FTE`. Employment and demand FTE remain separate.
- The measure register now uses `employer legal headcount` for the party-scoped qualifying WM-ORG-005 count and `consolidated distinct employed persons` for the cross-employer deduplicated count. Former label variants are retired.
- Person deduplication uses a transient engine-scoped anchor derived through WM-PER-001 identity resolution. It is non-registrable, never persisted and never emitted.
- Consolidated measures fail closed unless the pinned WM-XCT-002 scope authorizes every contributing employer and source revision.
- Cross-tabs, deltas and comparisons require one release-level temporal convention or an explicit reconciliation rule.
- Contractors, volunteers and agency workers enter unique persons only when their WM-PER-001 anchor resolves and Scope explicitly includes their assignment class. Vacancies never enter unique persons.

Fixtures cover all six corrections. The disposition remains `PROFILE` with `newRuntimeId=false` and held publication status.
