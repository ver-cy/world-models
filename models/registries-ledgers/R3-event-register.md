# R3 Event Register

Semantic timeline event stores, one log per domain: what happened, in what order, provably untampered. Every other model in the catalogue describes things and their changes; this model describes the store in which those changes are recorded as append-only, sequenced, integrity-proofed events. It is its own meta-model because ordering, replay, retention and tamper-evidence are one discipline regardless of the domain whose history is being kept.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:r3"
  csn: world.eventRegister
  version: 0.2.0
  displayName: "Event Register"
  description: "Append-only, sequenced and integrity-proofed event logs that keep domain timelines."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.eventRegister
bundles:
  - csn: world.eventRegister.capture
    displayName: "Capture"
    layers:
      - world.eventRegister.capture.eventSchema
      - world.eventRegister.capture.appendDiscipline
  - csn: world.eventRegister.ordering
    displayName: "Ordering"
    layers:
      - world.eventRegister.ordering.sequenceAssignment
      - world.eventRegister.ordering.temporalSemantics
  - csn: world.eventRegister.integrity
    displayName: "Integrity"
    layers:
      - world.eventRegister.integrity.hashChaining
      - world.eventRegister.integrity.proofPublication
  - csn: world.eventRegister.consumption
    displayName: "Consumption"
    layers:
      - world.eventRegister.consumption.replayAndQuery
      - world.eventRegister.consumption.retention
imports:
  - source: mu-event
    version: "*"
  - source: merkle-logs
    version: "*"
  - source: rfc-6962
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `capture` | Getting events into the log correctly | `eventSchema`: typed event payloads and their subject references · `appendDiscipline`: who may append what, idempotency, no in-place change |
| `ordering` | Making the timeline a timeline | `sequenceAssignment`: monotonic sequence numbers and checkpoints · `temporalSemantics`: occurrence time versus record time and their reconciliation |
| `integrity` | Making tampering evident | `hashChaining`: each event bound to its predecessors by hash · `proofPublication`: signed tree heads and inclusion proofs offered to verifiers |
| `consumption` | Reading history safely | `replayAndQuery`: cursors, subscriptions and subject timelines · `retention`: how long payloads persist and what compaction preserves |

## Objects

- `eventLog`: one append-only store for a domain's events; key attributes: domainRef, sequenceScheme, retentionRuleRef
- `recordedEvent`: a single immutable event in a log; key attributes: eventType, occurredAt, recordedAt, sequenceNumber, payloadHash
- `eventRef`: a typed link from an event to the world objects it concerns; key attributes: subjectCsn, subjectId, role
- `sequenceMarker`: a sealed checkpoint over a contiguous range of events; key attributes: fromSequence, toSequence, sealedAt
- `integrityProof`: a verifiable proof over sealed ranges; key attributes: proofKind, rootHash, signature
- `consumerCursor`: a reader's position in a log; key attributes: consumerRef, position, subscriptionScope
- `retentionRule`: what survives and for how long; key attributes: period, compactionPolicy, legalHoldFlag

## Relationships

- `recordedEvent` -> appendedTo -> `eventLog` (many-to-one): every event lives in exactly one log
- `recordedEvent` -> carries -> `eventRef` (one-to-many): an event names each object it concerns
- `integrityProof` -> seals -> `sequenceMarker` (one-to-one): each checkpoint gets exactly one published proof
- `consumerCursor` -> positionedIn -> `eventLog` (many-to-one): many readers advance independently through one log
- `eventLog` -> governedBy -> `retentionRule` (many-to-one): retention is declared per log, not per event
- `sequenceMarker` -> checkpoints -> `eventLog` (many-to-one): a log accumulates an ordered chain of checkpoints

## Events

- `eventAppended`: a new domain event was written at the next sequence position
- `checkpointSealed`: a range of events was closed under a sequence marker
- `proofPublished`: an integrity proof for a sealed range was made available to verifiers
- `retentionApplied`: expired payloads were compacted while hashes and proofs were preserved
- `integrityViolationDetected`: verification found the chain inconsistent with a published proof
- `subscriptionOpened`: a consumer began following a log from a stated position

## Contracts

- `appendContract`: which producer may append which event types to a log, under what schema version
- `replayContract`: a consumer's scope for reading or subscribing, by subject, type and time range
- `proofVerificationContract`: public terms for obtaining inclusion and consistency proofs without payload access
- `retentionContract`: the agreed retention period, compaction rules and legal-hold behavior for a log

## Projections

- `subjectTimelineView`: all events concerning one subject in order; omits events of other subjects sharing the log
- `inclusionProofView`: proof material for one event; omits the payload entirely
- `logHealthView`: sequence continuity, checkpoint cadence and lag for operators; omits payloads and subjects

## Composition

- COMPOSE (inbound): domain models across the catalogue, for example `world.registry` (R1), `world.ledgerAndAccount` (R2) and `world.lifeEventsAndCivilStatus` (B12), publish their Events into logs of this model
- REFERENCE `world.identityRegister` (R4): producers, consumers and event actors resolve to anchored identities
- EXTEND (inbound) `world.audit` (S4): the audit trail specializes this model for access and disclosure events
- COMPOSE `world.registryFederationAndMirroring` (R6): mirrors synchronize by replaying source logs under federation rules
- imports: mu-event (ALIGN): the shared semantic shape of an event, its subject references and time semantics
- imports: merkle-logs (ALIGN): hash-chained log structure for tamper evidence
- imports: rfc-6962 (ALIGN): verifiable log proofs, signed tree heads and consistency checking

## Stewardship

Each log is owned by the domain registrar whose history it keeps; the registrar guarantees append-only discipline and proof publication. Read and replay access is granted by that owner through the S1/S2 access and consent models, with all access itself auditable via S4.
