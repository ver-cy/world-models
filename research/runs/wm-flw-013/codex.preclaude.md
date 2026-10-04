# Codex pre-provider hypothesis for WM-FLW-013

## Boundary

Supply-chain Trace / Chain of Custody should be a pattern for a governed,
federated, time-aware trace graph and its versioned query results. It owns graph
scope, typed edges, evidence and correction lineage, gap/conflict representation
and trace-query semantics. Traceable objects, events, parties, locations,
shipments, movements, handovers, observations, documents, credentials, claims,
recall actions and evidence remain external masters.

## Proposed structure

1. Trace identity, scope and semantic kind.
2. Traceable objects, aggregation and transformation graph.
3. Events, clocks, locations and custody transitions.
4. Evidence, integrity, quality and correction.
5. Query, exposure, recall and federation.
6. Governance, access, retention and interoperability.

Each bundle should contain two layers and four findings. Each finding should
ask three model-specific questions and define one data element and one serial
evidence artifact. Ten functions should register a trace scope, bind objects,
append events, link aggregation or transformation, record custody assertions,
attach evidence, correct or contest, trace backward or forward, compute a
qualified exposure set and project an authorized standards view.

## Expected hard points

- A trace graph contains source-qualified assertions and gaps, not automatic
  proof that every event, custody claim or product characteristic is true.
- Physical segregation, controlled blending, mass balance and book-and-claim
  have different attribution semantics and must be profile-discriminated.
- Custody, possession, control, responsibility and ownership are independent.
- Event time, observation time, repository record time, ingestion time and
  correction time remain distinct.
- Recall or exposure analysis proposes a scoped result; an accountable external
  authority owns the recall, enforcement or disclosure decision.
