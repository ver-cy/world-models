# Frozen semantic audit — EM-TEC-03

Verdict: reject canonical publication; accept the boundary direction. Complete reserved WM-SFT-003, keep WM-SFT-018 as endpoint master, keep payload semantics in WM-DAT-004, introduce no ExchangeEvent, and leave Integration identifier-unassigned.

Blocking defects recorded by the sole no-tools audit:

1. Exposure and ConsumptionRouting were merged in EndpointBinding.
2. `integrationRef` was a dangling reference to an unallocated candidate.
3. Dependent records used surrogate-only identity instead of parent-scoped natural keys.
4. Occurrence relations to WM-REC-003 and WM-ACT-015 pointed in the wrong direction.
5. Several external referents and Environment mastership were unresolved.
6. Valid time, record time, interval closure, corrections, and cross-model interval composition were unspecified.
7. Parent/child lifecycle and pin/exposure lifecycle constraints were missing.
8. `resolutionPolicy` reintroduced floating revision resolution without a reproducible resolution record.
9. Scoped overlap rules for dual-run, blue/green, and DR were absent.
10. Contract surface omitted interaction style, channels, parameters, errors, auth scheme, and declared service targets.
11. Declared service targets were not separated from observed measurements.
12. WM-SFT-003 lacked a secrets exclusion and allowed an unbounded metadata bag.
13. At-most-one-revision-per-message was absent.
14. Contract-to-WM-DAT-004 cardinality was unstated and model-level relations were over-required.
15. Family-level versus revision-level exposure was silently narrowed.
16. Consumer authority over pins was not enforced.
17. Compatibility exceptions had no expiry or authority.
18. Fixtures lacked invariant traceability, mixed valid outcomes with rejection cases, and one pin expectation was wrong.

Required remediation was applied once in candidate.2: split/defer routing, remove unallocated references, declare natural keys, reverse occurrence direction, add unresolved-reference holds, define bitemporal append-only rules, add lifecycle and authority constraints, add resolution records, scoped concurrency, complete contract surface, exclude observations and secrets, state message cardinality and schema cardinality, add expiring exceptions, number invariants, and replace fixtures with traced positive/negative cases. Per program policy the audit was not rerun.

Publication disposition: both reserved candidates remain research candidates and canonicalPublishable=false. Integration and ConsumptionRouting remain unassigned/deferred. No registry allocation or runtime ID is created.
