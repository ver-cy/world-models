**ACCEPT WITH LIMITS**

Severity: Medium operational residual / Low contract. No High breaker. Runtime behavior is unchanged from the R4 reducer already audited in this conversation.

## Completeness

Accessible:
- R3 30 body-supplied files, complete R4 delta, and R4 added files from this conversation.
- This R4a addendum: full `model-spec.md` and `test_sync.py` diffs, exhaustive `spec.json` scalar replacements, complete `test-results.json` and `acceptance-results.json`.
- END marker `SYNC-R4A-FINAL-20260922`.

Not body-supplied (unchanged from R4; not inferred from hashes): the same eight inventory-only files and external composer/native/parent toolchain.

`spec.json` `/model/scope` was not recopied. It is specified as R4 `model-spec.md` plus the two hunks in this addendum. That is enough to review the claimed identity as a text delta, not as an independent byte check.

No tools, no execution, no browsing, no independent hash verification. Author 101-pass and 3-profile reports, and the listed digests including executable `buildId` `sha256:b782bbca6c4b5bcc9344dde998d88486c1635ce45a00fbcf6bb7bb179af25cd6`, are supplied evidence only. `review.json` / `review.md` remain pending bookkeeping. This does not authorize publication.

## What R4a actually changes

Runtime, schema, generator, fixtures, examples, `acceptance.py`, worker, and benchmark bytes are unchanged. H1/M1 closure, receiving-scope pins, capacity caps, transport/canonical split, and compact conflicts stand as in the R4 verdict.

Documentation now matches that reducer:
- Same immutable scope: catalogue reclassification or `observedAt` outside the mapping window → `active-pin-suspended`.
- Changed source-kind interpretation requires a new scope; the receiving scope is `unmapped` until a mapping declared there is activated. No inherited suspended pin.
- The leftover `sourceObjectKind` inequality in `mapping_outcome` is documented as dead defense after the same-scope filter.
- Shared attested rounds: intake may append nonterminal pages or error-seal incomplete; page slots are not reserved; the attester’s review of the whole page set is a host duty, not a proved machine check.

`spec.json` SS-F10 evidence/question/artifact strings are updated to “Current catalogue/validity check within the receiving scope and active-pin-suspended outcome.” That matches the corrected sentence and does not reintroduce cross-scope suspension.

## New tests versus unchanged `apply()`

`test_scope_b_only_principal_cannot_probe_or_move_scope_a_claim`: policy limited to scope B; reuse of scope-A mapping/round IDs → `DENIED`; retract of the A claim → `DENIED`; activate of a B mapping while A still holds the lineage → `DENIED`; B intake is `unmapped`. Matches R4 collision and pin rules.

`test_exact_terminal_retry_after_attestation_revocation_keeps_ack`: after revoke of `attest-coverage` (intake+read remain), exact terminal retry returns the original ack and does not append; error-free seal is `DENIED`. Matches the R4 short-circuit-before-attest-gate rule.

`test_shared_nonterminal_page_and_intake_error_close_are_incomplete`: other writer takes page 0; planned page 0 is `Invalid` (`page chain gap`) with no archive change; intake error-seal yields `complete=false` and `assess_rounds` `insufficient-context`. Documents interference rather than inventing page ownership.

No new runtime path was added that would reopen H1 or M1.

## Required changes

None for this addendum verdict.

## Residual adoption limits

All R4 limits remain: 128 events / 512 KiB canonical / 8 MiB raw transport / 32 and 4 conflicts; full-history replay under lock; hashes ≠ authenticity or latest-head; no IAM, connectors, writable resume, quarantine resolver, EFA/EAP adapter, or production-scale claim; `requirements.txt` still pins only `jsonschema`; recorded runtime versions are not a lock; quadratic work and SQLite busy are host operational errors; global mapping/round IDs and active-lineage reservations still disclose unavailability; privileged export/analysis/native helpers still need a host disclosure wrap.

Newly explicit, not newly introduced:
- Shared-page displacement and intake-only errored incomplete closure are allowed; attester review of foreign pages is external.
- Nonempty partial SQLite bootstrap can still surface a raw host error; empty 0-byte interrupted files stay refused and preserved; no automatic recovery.
- No new round-predecessor purpose gate; assessment already requires equal purpose.
- Prior capacity run remains valid only for its exact unchanged input bytes and is not an SLA.

Research assurance remains reviewable-draft. Synthetic candidate installation is not production publication.