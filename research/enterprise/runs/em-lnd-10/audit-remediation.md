# EM-LND-10 audit remediation

The single frozen Claude audit returned `ACCEPT WITH LIMITS`. All six limits were incorporated without adding an aggregate or identifier; the audit was not repeated.

- The landscape is citation-only for run-produced elimination, allocation, translation and other derived rows. Recomputing them would create a shadow master and is prohibited.
- Every result row's ledger revision must be a member of the Finance View Policy's pinned ledger revision set.
- Allocation conservation is tested only in source currency. Presentation-currency rows are derived and non-authoritative for conservation.
- The affirmative plan/actual, elimination and allocation paths remain rehearsal-only until every required dependency type and pin is allocated.
- Without an allocated Metric Definition, paired plan and actual rows may expose a raw arithmetic difference but never a governed variance metric.
- Registration grants no authority to create governed totals, eliminate, allocate, disclose or publish; those actions require their external authorities.

Fixtures cover each correction. The disposition remains `PROFILE` with `newRuntimeId=false` and held publication status.
