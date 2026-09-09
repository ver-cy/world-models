# WM-XCT-037 bounded Claude research plan

WM-XCT-037 is a format-neutral, host-scoped mixin for typed dependency
assertions and downstream-impact knowledge between objects owned by other
models. The frozen registry supplies no parent and no ratified relationship
contract, so every neighbor relation remains provisional. Research is divided
into fifteen bounded, independently schema-valid passes.

1. `dependency-core` owns the assertion envelope, dependent and prerequisite
   endpoints, direction, scope, version pins, cardinality and identity.
2. `technical-taxonomy` owns software, data, schema, API, infrastructure,
   configuration, build, deployment and security dependency kinds.
3. `socio-operational-taxonomy` owns process, capability, organizational,
   supplier, contractual, legal, financial, temporal and spatial kinds.
4. `conditions-strength` owns hard/soft, mandatory/optional, alternatives,
   thresholds, guards, compatibility ranges and satisfaction semantics.
5. `evidence-observation` owns provenance, observation, discovery method,
   authority, confidence, freshness, contradiction and unknown states.
6. `lifecycle-health` owns proposal, activation, satisfaction, degradation,
   breakage, restoration, deprecation, supersession and historical state.
7. `graph-analysis` owns path semantics, cycles, strongly connected groups,
   fan-in/fan-out, cut sets, reachability and no-silent-closure constraints.
8. `impact-scenarios` owns change/event/scenario inputs, direct and indirect
   effects, propagation assumptions, affected sets, time horizon and outcomes.
9. `criticality-resilience` owns criticality, severity, likelihood,
   confidence, blast radius, substitutes, redundancy and mitigation references.
10. `governance-roles` owns authorities, stewardship, review, exceptions,
    privacy/access, retention, legal hold and segregation of duties.
11. `governance-platform` owns format/interface neutrality, artifact and time
    rules, namespace/canon/patch and the canonical `service_layers` contract.
12. `mutation-operations` owns declare, validate, approve, activate, revise,
    supersede, retire and observation-update command contracts.
13. `query-operations` owns current/as-of read, traverse, compare and
    dependency-health query contracts with completeness disclosure.
14. `impact-reporting` owns analyze-impact, conflict, change-readiness,
    mitigation and notification-content reports without executing changes.
15. `projection-operations` owns Git/files, Markdown, HTML, JSON, YAML, CSV,
    RDF, APIs, MCP, MongoDB and domain-standard projections with loss reports.

Every pass uses a disjoint local-ID prefix. The deterministic merger keeps the
complete boundary from `dependency-core`, service layers from
`governance-platform`, remaps sources and validates the union. A separate
no-tools adjudication must verify that the result stays an assertion and impact
knowledge mixin and does not become a configuration-management database,
package manager, build/deployment orchestrator, runtime monitor, graph database,
risk engine, business-continuity system, authorization point, audit store,
notification service or change executor. Dates and timestamps are qualifiers,
never identifiers; timestamps include seconds and an explicit offset or `Z`.
