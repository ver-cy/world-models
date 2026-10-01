# Provider comparison — EM-TEC-03

Claude and Grok agree that WM-SFT-003 should be completed rather than replaced, WM-SFT-018 owns endpoint identity, WM-DAT-004 owns payload semantics, Integration has independent continuity but must remain identifier-unassigned, and no ExchangeEvent model should be introduced.

The reconciled design uses a stable InterfaceContract root with immutable ContractRevision children. It separates contract Exposure from Integration-specific ConsumptionRouting, pins every consumer to an exact revision, preserves historical messages after retirement, and keeps address changes independent of semantic revisions. WM-SFT-018 uses stable endpoint identity with effective-dated address and exposure records.

Grok adds conditions that were under-specified locally: explicit family/revision choice; separate exposure and routing relations; pub/sub per subscriber; exclusion of ephemeral call paths; exact one-revision message interpretation; explicit concurrency; contract-to-schema cardinality; and Integration collision rules. Those conditions are frozen for the audit and remediation.
