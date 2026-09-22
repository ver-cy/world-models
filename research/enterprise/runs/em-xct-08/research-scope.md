# EM-XCT-08 — Sources, bindings and synchronization

Status: research scoped, not a published implementation. This is the next contour after the bounded Enterprise Action Requests 0.1.0 release. No Claude or Grok study has yet been submitted for this contour.

## Problem and boundary to investigate

A Company Dimension must be able to reuse the same business identity across repeated imports, source-container renames and moves, while preserving explicit conflicts. A new tracker board must not automatically create a new business Project. A row disappearing from a response must not automatically delete a business object.

Investigate SourceSystem, SourceBinding, ExtractionRun, SyncCursor and SyncConflict as candidate concepts. Their names are research vocabulary, not five mandatory new object models. Compare reuse, embedded value, Event profile, governed binding, shared contract and separate object before choosing a form.

Keep the source's operational identity separate from a software product or its deployment. Keep source record identity separate from business identity. A binding describes how a source scope maps to existing semantic fields; it does not create a subject model, confer source authority or grant disclosure. Operational endpoints and credential values remain local; public specifications and examples contain synthetic identifiers only.

## Pinned predecessor reading still required

Ten public specification/AGENTS artifacts were retrieved and matched against the local site and runtime digests. The retrieval manifest identifies their versions and hashes. Retrieval is not full semantic reading. Complete the specifications, examples, validators, publication holds and relevant prior research before freezing a model boundary:

- WM-XCT-001 Ownership / Stewardship 0.3.1-enterprise.1.
- WM-XCT-012 Provenance 0.3.0-research.1.
- Enterprise Fact Authority 0.1.0.
- Enterprise Assertion Provenance 0.1.0.
- WM-XCT-036 Alias / Same-as Mapping and its separately published Enterprise Identity profile. The latter is not a separate runtime entry; do not invent `vr.profile.enterprise-identity` or silently claim independent installability.

Also inspect current MMAS/protocol source-binding semantics, native source configuration and the earlier enterprise identity/fact-authority/provenance outcomes. Reuse their exact published pins where semantics fit. Source authority, identity resolution and provenance are distinct from delivery/checkpoint correctness.

## Initial primary-source comparison

These are selected-section observations on 2026-09-22, not full-standard conformance claims.

1. [Airbyte Protocol — State & Checkpointing](https://github.com/airbytehq/airbyte/blob/master/docs/platform/understanding-airbyte/airbyte-protocol.md): progress emitted by a source is insufficient by itself; destination commitment matters before using a state to resume. Source state is opaque outside its producer. Per-stream and global states have different ordering scopes. Design consequence, still a proposal: distinguish emitted, received and committed checkpoints and pin the scope that gives a cursor meaning.
2. [Microsoft Graph delta query — state tokens, replays and synchronization reset](https://learn.microsoft.com/en-us/graph/delta-query-overview): opaque continuation tokens include query context; clients must handle replayed changes and resets requiring full synchronization. Design consequence, still a proposal: a cursor is not a universal timestamp and cannot be reused under silently changed scope; reset is an explicit lifecycle transition.
3. [Debezium PostgreSQL connector — snapshots, primary-key updates and deletes](https://debezium.io/documentation/reference/stable/connectors/postgresql.html): the observed documentation labels itself 3.6. It distinguishes snapshot capture from subsequent streaming. A primary-key change can be represented by old-key deletion and new-key creation with linking headers. Delete payload visibility depends on replica identity. Design consequence, still a proposal: transport deletion/key changes are not evidence that the business object died or that a new business object was born. Do not infer unseen before-values.
4. [W3C PROV-DM §5.1.8 Invalidation](https://www.w3.org/TR/prov-dm/#term-Invalidation): invalidation concerns the end of a qualified entity's availability. Design consequence, still a proposal: invalidating a captured source representation must not silently invalidate every entity it describes.

Pin precise upstream revisions where feasible before normative comparison. These sources do not establish an organization's actual permissions, completeness guarantees or master systems.

## Questions the research must settle

1. What identifies an operational source instance, source namespace and generation?
2. What preserves source and business identity through rename, move, key recycling and replacement?
3. Who approves source-record-to-business-object mapping, and how is ambiguity retained?
4. What precisely constitutes a binding revision, and which changes require a new cursor epoch?
5. Which fields are source assertions versus accepted business facts, and who owns each?
6. What scope, filters, principal, audience, schema and partition set qualify capture coverage?
7. Which evidence distinguishes complete empty coverage, partial extraction, access loss and source deletion?
8. When is absence allowed to withdraw a source assertion, and why does it not delete its subject?
9. How do emitted, received, applied and committed checkpoints differ?
10. What proves that every record covered by a checkpoint reached a durable outcome?
11. How are retry identity, changed-content replay and partial failure handled?
12. What order is actually guaranteed: source, stream, partition, transaction or none?
13. How are tombstones, stale late records and key changes qualified?
14. How are conflict resolution, source-priority changes and historical corrections represented?
15. How are token expiry, scope/schema changes, resume refusal and full reconciliation recorded?
16. Which trusted host controls are required for disclosure, cursor protection and source/authority verification?
17. What is the useful descriptive minimum for a startup with a file import and no connector platform?
18. What can a pinned reference actually validate, and what remains an external connector/host duty?

## Proposed acceptance cases, subject to boundary review

Use startup file import, matrix-organization tracker sources and AI/service metadata feeds as synthetic profiles. No production credentials or personal records are required.

- Replay the same source batch without new business identities or duplicate accepted effects.
- Same retry identity with different content yields an explicit conflict.
- Rename/move a source container while retaining established source and business identities.
- Two boards describing one business Project do not create two Projects automatically.
- Recycled external key under a new source generation does not overwrite the old mapping.
- Partial page, failed extraction or reduced access cannot authorize absence-based withdrawal.
- Complete empty coverage remains distinguishable from an error or unknown coverage.
- Old-key delete/new-key create preserves ambiguity unless identity continuity is explicitly evidenced.
- Destination failure before durable commit cannot advance the resumable checkpoint.
- Repeated, stale and out-of-order events are handled according to the declared ordering contract.
- Equal-authority conflicting source assertions remain visible; silent last-write-wins is not a resolution.
- Cursor from another scope, partition, binding revision or epoch is refused.
- Expired cursor causes explicit resync; no fabricated continuation is accepted.
- Historical correction and source retraction preserve the original evidence and its qualified meaning.
- Export/import round-trip preserves IDs, coverage, chronology and unresolved conflicts; unsupported migration refuses explicitly.

These are proposed requirements, not passing tests. Follow with actual independent Claude and Grok studies using the same frozen public boundary, reconcile differences, implement a bounded contract, run a separate complete-input audit and publish only verified usable scope.
