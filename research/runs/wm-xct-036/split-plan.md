# WM-XCT-036 bounded Claude research plan

WM-XCT-036 is a format-neutral mixin for governed alias and same-as assertions
between identifiers or records owned by other models. It is researched through
thirteen bounded, independently schema-valid passes.

1. `alias-assertion` owns assertion identity, referenced endpoints, scope,
   cardinality, version pins, endpoint integrity and host-dependent identity.
2. `relation-taxonomy` owns relation kinds, semantic strength, direction,
   symmetry and the boundary between identity, aliases and mappings.
3. `evidence-confidence` owns provenance, authority, match method, evidence,
   confidence, human review, disagreement and reproducibility.
4. `equivalence-properties` owns formal relation properties, contextual and
   temporal equivalence, safe composition, closure constraints and conflicts.
5. `equivalence-clusters` owns traversal, graph safety, clusters, external
   canonical-representative policy, split/merge lineage and impact reporting.
6. `lifecycle-states` owns proposal, review, activation, dispute, expiry,
   supersession, retraction, rejection and immutable transition history.
7. `historical-resolution` owns as-of resolution, redirect-chain safety,
   endpoint merge/split consequences, concurrency and quarantine semantics.
8. `governance-roles` owns authorities, delegations, approval thresholds,
   exceptions, privacy/access separation, retention and legal-hold controls.
9. `governance-platform` owns interoperability, projection-loss reporting,
   artifact identity/time rules and the canonical `service_layers` contract.
10. `mutation-operations` owns propose, validate, evidence submission,
    approve/reject, activate, supersede/retract and mutation concurrency.
11. `query-operations` owns current/as-of reads, resolution, traversal,
    assertion comparison and deterministic ambiguity/no-answer responses.
12. `reporting-operations` owns conflict/impact and disposition-readiness
    reports, with external notification and enforcement boundaries.
13. `projection-operations` owns export/projection semantics and explicit
    loss reporting across RDF, HTTP, files, MCP, databases and APIs.

Each pass uses a disjoint local-ID prefix. The deterministic merger keeps the
complete boundary from `alias-assertion`, service layers from `governance-platform`,
remaps sources and validates the union. A later no-tools adjudication must
verify that this remains a host-scoped relation assertion mixin and does not
become an identifier-scheme registry, naming model, entity-resolution engine,
master-data merge service, redirect server, ontology reasoner, canonical-record
owner, provenance/audit store or authorization decision point. The registry's
WM-XCT-011 parent field is provisional because no relationship contract was
supplied.
