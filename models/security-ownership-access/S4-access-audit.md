# S4 Access Audit

This meta-model is the append-only memory of the cluster: every read, every grant, every denial, recorded once and never rewritten. It exists as its own model because evidence has different physics from the data it describes: entries are written by many systems, owned by none of them, chained so that tampering is detectable, and readable above all by the person whose data was touched. Everything else in the cluster produces events; this model makes them durable and provable.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:s4"
  csn: world.accessAudit
  version: 0.2.0
  displayName: "Access Audit"
  description: "Append-only, integrity-protected log of every read, grant and denial across the catalogue."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.accessAudit
bundles:
  - csn: world.accessAudit.ledger
    displayName: "Ledger"
    layers:
      - world.accessAudit.ledger.entries
      - world.accessAudit.ledger.chainIntegrity
  - csn: world.accessAudit.evidence
    displayName: "Evidence"
    layers:
      - world.accessAudit.evidence.attribution
      - world.accessAudit.evidence.servedShape
  - csn: world.accessAudit.oversight
    displayName: "Oversight"
    layers:
      - world.accessAudit.oversight.ownerVisibility
      - world.accessAudit.oversight.retentionAndSealing
imports:
  - source: merkle-logs
    version: "*"
  - source: mu-event
    version: "*"
  - source: rfc-9162
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `ledger` | The immutable record itself | `entries`: sealed records of access events in write order Â· `chainIntegrity`: hash links between entries and periodic published anchors |
| `evidence` | What each entry proves | `attribution`: who read, as which resolved actor, under which contract Â· `servedShape`: which projection policy version and template fingerprint shaped the disclosure |
| `oversight` | Who may see the log and for how long | `ownerVisibility`: the owner's standing right to their own timeline Â· `retentionAndSealing`: how long entries persist and when they are sealed from further detail queries |

## Objects

- `accessEvent`: one read, grant, revocation or denial; key attributes: time, reader reference, object reference, contract reference, outcome.
- `auditEntry`: the sealed ledger record wrapping one or more events; key attributes: sequence number, content hash, previous-entry hash.
- `merkleAnchor`: a periodically published root hash committing a range of entries; key attributes: root, range, publication time, publication channel.
- `inclusionProof`: the proof that a given entry is committed by an anchor; key attributes: path, anchor reference, verified state.
- `readerAttribution`: the resolved actor behind a read (person, organization, system, agent); key attributes: actor reference, acting capacity, authentication basis.
- `denialRecord`: a refused access attempt; key attributes: requested scope, refusal reason, requester.
- `retentionRule`: how long entries stay queryable in detail; key attributes: class of entry, retention period, sealing condition.

## Relationships

- `auditEntry` -> seals -> `accessEvent` (1..*): events become immutable once wrapped in an entry.
- `auditEntry` -> chainedTo -> `auditEntry` (1..1): each entry commits its predecessor's hash, making insertion and deletion detectable.
- `merkleAnchor` -> commits -> `auditEntry` (1..*): anchors let outsiders verify the log without reading it.
- `inclusionProof` -> provesMembershipOf -> `auditEntry` (1..1): any party can check an entry against a published anchor.
- `accessEvent` -> exercised -> `accessContract` (0..1): permitted reads cite the S2 contract they ran under; denials may cite none.
- `accessEvent` -> touched -> `registryEntry` (1..*): every event names the S1-registered objects involved.

## Events

- `readRecorded`: a permitted read of someone's data was written to the log.
- `grantRecorded`: the creation, amendment or revocation of an access contract was written to the log.
- `denialRecorded`: an attempted read was refused and the refusal preserved.
- `entrySealed`: a batch of events was wrapped, hashed and chained.
- `anchorPublished`: a root hash for a range of entries was made public.
- `proofIssued`: an inclusion proof was produced for a challenged entry.
- `inconsistencyDetected`: a verification failed, indicating tampering or loss between entries and anchors.

## Contracts

- `ownerAuditFeed`: the owner of any object receives, on demand or by subscription, every entry that touched their objects.
- `oversightExtract`: the audit registrar provides aggregate, identity-free extracts for systemic oversight of access patterns.
- `proofService`: any party obtains anchors and inclusion proofs to verify log integrity without reading entry contents.

## Projections

- `ownerTimeline`: who read my data, when, under which contract; omits every other owner's entries.
- `readerActivitySummary`: aggregate read counts and patterns per reader; omits the identities of touched objects and owners.
- `integrityBundle`: anchors, chain heads and proofs only; omits all event payload.

## Composition

- REFERENCE `world.ownership` (S1): entries name registered objects, and owner visibility resolves through ownership records.
- REFERENCE `world.accessContract` (S2): permitted events cite the contract exercised; the log is the contract's execution history.
- REFERENCE `world.disclosureScope` (S3): each disclosure entry carries the policy version and template fingerprint that shaped it.
- REFERENCE `world.accessEnforcement` (S7): the log is the primary evidence source for violation signals and enforcement cases.
- imports: merkle-logs (COMPOSE): the tree structure underlying anchors and inclusion proofs.
- imports: mu-event (EXTEND): the event primitive that access events specialize.
- imports: rfc-9162 (ALIGN): the verifiable-log pattern of published anchors and third-party auditability.

## Stewardship

An audit registrar archetype operates the log but owns none of its content: it may not read entry payloads beyond what operation requires, and it cannot amend them at all. The standing beneficiary is the data owner, whose right to their own timeline is not itself contract-gated, while all other access follows S1/S2.
