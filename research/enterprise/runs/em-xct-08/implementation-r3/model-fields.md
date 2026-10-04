# Fields and whole-object semantics

All 27 command and journal definitions in sync.schema.json are closed and every listed property is required; null is allowed only explicitly. Maximum cardinalities are encoded in the schema and named in model-spec.md. Output state is derived by complete journal replay, never edited as free-form fields.

## SyncRegister

Immutable register/Dimension/bootstrap identity.

Sources, scopes, complete journal and derived state; protected namespace.

Historical replay establishes internal consistency, not current authenticity.

Admin operations and explicitly granted intake/map/read/attest-coverage; archive cannot resume.

One owned local SQLite master; native snapshots are restricted evidence.

## SourceInstance

Immutable product/tenant/environment/generation declaration and local ID.

Product reference and continuity evidence; no connector credential fields.

Host verifies source continuity; matching labels alone are insufficient.

New generation needs a new declaration; close old epochs explicitly when appropriate.

External source operator owns source truth; host owns its declaration.

## AcquisitionScope

Immutable local ID and exact fingerprint excluding that ID.

Resource/key scheme/version, source kind, query/filter/visibility/interpretation/schema refs.

Literal evidence-reference identity; no semantic normalization.

New scope for changed interpretation; unpartitioned stream only.

One SourceInstance; evidence namespace controlled by host.

## RecordSubjectMapping

Stable claim ID and immutable lineage/target/purpose/issuer anchors.

Known qualified key, target kind, validity, evidence and correction predecessor.

Aboutness claim with target-catalogue and pair checks, never same-as.

Append revisions; every activation checks uniqueness; retracted terminal.

Authenticated steward with exact map right; catalogue and policy pinned.

## SyncEpoch

Immutable epoch ID within a scope; independent of record generation.

Open/closed state, fence, head, local progress and reset evidence.

Progress follows committed sequence; opaque tokens are not ordered.

One open epoch per scope; close after all rounds sealed; reopen with new ID.

Admin owns lifecycle; intake transaction alone advances head.

## SnapshotRound

Immutable round ID and scope/epoch/purpose anchors.

Consistency, visibility, ordering evidence, pages, errors and completeness.

Strong local key accounting is not proof of actual source completeness.

Append contiguous pages, then seal once; compare only explicit compatible rounds.

Source guarantees are host-verified; only proposals arise from absence.

## BatchReceipt

Scope/epoch-wide key and host sequence-derived receipt ID.

Exact content, immutable mapping outcomes, counts, previous head and policy revision.

Destination acknowledgement of local metadata only.

One first commit; exact own replay returns old ack; no reapplication.

Serialized local journal; current read rights govern receipt disclosure.

## RecordOccurrence

Receipt identity plus original input ordinal, including duplicates.

Qualified key, protected content ref, availability operation, times, correction and pin.

Distinguish source-declared acquisition from host receipt and nullable source time.

Immutable; later corrections append evidence without repinning.

Part of one receipt; domain truth and subject lifecycle remain external.

## QuarantineEntry

Receipt identity plus original rejected ordinal.

Protected descriptor, reason, retry obligation and open state.

Adapter classifies raw failures; this register validates descriptors, not raw bytes.

Retained open in 0.1.0; reingestion is a new batch; resolution API deferred.

Host evidence custody and external operational resolution.

## ConflictDiagnostic

Host sequence-derived immutable ID, actor and attempt.

Scope/epoch, reason, supplied and retained digests where available.

Restricted operational evidence; not a public existence oracle.

Append on admitted collisions/stale preconditions; no canonical denial telemetry.

Privileged archive; a current writer still observes key unavailability.

Source productRef/targetId refer to existing external registries; they do not import those registries. There is one source per scope, one scope per epoch/round, zero or one active mapping per complete lineage/purpose, many occurrences per receipt and one immutable outcome per occurrence. Evidence values carry no independent subject identity. Grants/catalogue are versioned host snapshots; last admitted revision governs subsequent operations.
