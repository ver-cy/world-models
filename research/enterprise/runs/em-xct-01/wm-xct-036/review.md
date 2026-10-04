# Enterprise identity 0.1.0: review and publication disposition

**Disposition: publish bounded reviewable draft** under the owner's existing authorization. This is a Codex integration decision, not authority granted by an external reviewer. EM-XCT-01 remains partial.

## Evidence and exact scope

| Pass | Actual provider/mode | Result and limits |
|---|---|---|
| Independent study | Claude Opus, CLI reports `claude-opus-5`, permitted web research | Completed. Initial fetch summaries were partial for large Vercy specs; Codex subsequently read full local/public-byte-matched JSON and exact selected definitions. |
| Independent study | Grok, browser UI Heavy; underlying version not exposed | Completed actual browser memo. Not a schema-valid provider JSON result. |
| First implementation audit | Claude Opus, frozen no-tools text | BLOCK on receipt-time import and smaller issues. Full listed evaluator/schema/tests/fixtures/harness and selected parent definitions; no tool execution or full legacy-source audit. |
| First implementation audit | Grok Heavy, focused browser text | ACCEPT WITH LIMITS with concrete type, namespace, negative and temporal objections. Complete evaluator, design and schema summary only; full schemas/tests/harness unseen. |
| Second implementation audit | Claude Opus, 11-file frozen no-tools text | BLOCK (narrow) on last-event surrogate admission and proposal assignment squatting; requested a bitemporal dispute fix. Prior major corrections recognized. |
| Second implementation audit | Grok Heavy, 11-file text attachment | ACCEPT WITH LIMITS. Attachment explicitly reported available and untruncated. Group/AI fixtures, tooling and sidecars not supplied in this pass. |
| Final focused remediation | Claude Opus and Grok Heavy separately | Both ACCEPT WITH LIMITS. Entire final evaluator, nine additional regression tests, documentation clarification, compact reports and hashes. Schema unchanged; body not resupplied. Earlier audit records retained. |

Frozen prompts, file manifests and actual responses are separate files. No failed run is relabelled successful. Reviewers did not execute tests, re-hash local files or independently certify the reported native results. The source of execution evidence is the local reproducible test/acceptance harness, later rerun from the public download during publication verification.

## Material corrections

- **History admission:** live import requires a trusted receipt time after the input head; new events must use that timestamp. Direct snapshot validation remains incapable of proving reception history. Tests reject both backdated and future-dated live additions.
- **Content and identity:** genesis commits to fixed claim content, later events to the predecessor. Entire assertions must be canonically encodable before admission, including the last event. Resealed endpoint changes still fail live import.
- **Assignment evidence:** issuer qualifies occurrence identity. Proposals cannot reserve an occurrence; a retraction releases its reservation and retains its evidence. Simultaneously reserved asserted observations must agree. Differing carried observations are explicitly reported.
- **Kinds and namespaces:** source scheme/version/issuer/scope registers constrain declared kind, target-kind namespaces are disjoint, local path escapes and empty suffixes are rejected. Source truth and authenticated register ownership remain external.
- **Negative/candidate semantics:** reviewed negatives yield denied-in-input; proposed negatives remain separate. A disputed unasserted candidate cannot veto an accepted claim. Dispute classification uses valid/known-time-filtered prior events.
- **Native limits:** actual stored snapshots are compared with input fixtures. Installed schema and validator source bytes are checked. Outer V3 success is demonstrated to be insufficient; the companion is explicitly invoked. Native-required rank 0 belongs to snapshot metadata and is not read by the identity resolver.

The final executable evaluator SHA-256 is `bec1dcec0584c4dc8de2be4251366db2b4f56aa71d0f0e35ec11d29b3cdbd98f`; the executable schema is `d5dbab037ea7af7f5b9feef95929f461380d824849caad092af7ea1706cc54c7`. Final review manifests pin those bytes. Post-review additions are adoption documentation/support indexes and a clearer statement of the whole-input diagnostic below; no further evaluator/schema change is hidden behind these verdicts.

## Retained limits

**Claude final N1 is accepted as an explicit diagnostic boundary:** `retainedObservationConflicts` describes the complete supplied input, including unrelated assignments and records later than knownAt. It is not a historical query result. The caller must authorize access to the entire supplied input before invocation and must not present this diagnostic as evidence known at the query date. Input digest likewise commits to all supplied records. Per-query and per-field disclosure needs a separate production adapter.

Policies, clocks, evidence, real endpoint meaning and source completeness are caller-trusted. No four-eyes or signature proof is implemented. One frozen policy includes read/write declarations; rotation/expiry fails closed. Live imports are globally serialized at one transition per second. Source-observation revision, account ownership, inverse subject lookup, federation, erasure, endpoint merge/split and existing-Dimension transactional writes remain deferred.

Parent-field mappings are narrower/overlap usage choices, not complete conformance or a ratified predicate register. Whole-model WM-XCT-011 and WM-XCT-036 holds remain open. The broad 036 synthesis still has its historical Claude-only waiver and 108-source verification hold. New dual-provider enterprise work must not be represented as retrospectively reviewing those sources or clearing the parent classification/relationship decisions.

Pinned local source bytes do not establish a hardened execution environment: Python paths/bytecode and post-check changes remain trusted. The schema must remain protected after installation. Invalid parsing/encoding fails closed, but not every parser exception has the same Python exception class. Fixed 2026 synthetic policies make the published acceptance fixture time-bounded; expiry is not permission to backdate a production clock.

## Validation claim

The final local run passed **87 tests** and **three temporary new-Dimension scenarios** (startup, group, AI team). Those results concern the included synthetic reference binding. They are not production performance, universal identity, safety/security certification, or real-company deployment evidence. Read `publication-verification.json` for the separate post-deployment byte checks, catalogue resolution and downloaded-package runs.

## Publication verification and discovery patch

Production readback caught a generic-publisher regression: the unchanged legacy natural-language composition obligations were emitted as executable dependency IDs, blocking automatic discovery. Version 0.3.2-enterprise.1 restores the previous metadata contract (no runtime_requires declaration); it does not resolve or certify the broad conceptual dependency graph. The separate profile closure remains explicitly pinned and tested. Versions 0.3.0-research.1 and 0.3.1-enterprise.1 are preserved; profile 0.1.0 bytes are unchanged. See discovery-metadata-correction.json and publication-verification.json.
