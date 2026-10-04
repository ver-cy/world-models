# Grok frozen study — EM-TEC-03

Source conversation: https://grok.com/c/8ccdbc77-f5a5-4d9a-895e-c61c8bfc2e33?rid=abe0c6a7-7b9c-40f2-a759-bd3eacc76ec9

Verdict: ACCEPT WITH CONDITIONS.

Complete reserved WM-SFT-003 as a versioned logical Interface Contract. A published API version is an immutable contract revision. WM-DAT-004 owns payload semantics; WM-SFT-018 owns endpoint/address exposure. Model a stable contract family root with immutable revision children and state this choice explicitly.

Split the former EndpointBinding into two dependent relations: (1) Exposure binds a contract revision or family to an endpoint, environment, and effective interval; (2) ConsumptionRouting binds an Integration to an exposure, environment, role, and effective interval. ContractPin is a dependent, effective-dated relation to one exact revision. `latest` is query behavior only. Dual run uses overlapping, explicitly scoped pin rows.

Integration remains identifier-unassigned. It requires independent continuity, but the candidate grain and natural key remain unresolved. A possible key is producer, consumer, interface family or capability, and purpose discriminator. One provider with many subscribers uses one Integration per subscriber. Consumer replatforming may preserve or replace Integration depending on the final key. Do not invent a successor relation. Exclude test harnesses, intra-component calls, probes, and other ephemeral call paths.

Changing a URL does not change contract or Integration identity. An incompatible payload change at the same URL creates a new contract revision and WM-DAT-004 schema revision; the endpoint may remain. Do not create ExchangeEvent: addressed exchanges use WM-REC-003 Message; other occurrences use WM-ACT-015. A Message interprets against at most one exact revision.

Every published semantic change creates a revision with compatibility assessment, impacted pins, notice, and sunset or successor handling. Retired revisions accept no new pins but remain resolvable for historical messages. Shared gateways may expose many contracts. Blue/green and DR are explicit concurrent scoped relations.

Invariants: published revisions are immutable; address is not contract identity; revision is not Integration identity; Integration continuity survives revision and URL change; every dependent binding has parent, endpoint or exposure, environment, and effective interval; overlap is explicit; bindings cannot change meaning; pins name exact revisions; each message names at most one revision; payload semantics remain in WM-DAT-004; not every call path is an Integration; reserved codes remain reserved.

Open holds: WM-SFT-018 endpoint identity and address-change semantics must be explicit; Integration grain/type/purpose/collision rules remain unallocated; environment is an external master; contract-to-WM-DAT-004 cardinality must be stated; pub/sub and multicast must be covered by fixtures.
