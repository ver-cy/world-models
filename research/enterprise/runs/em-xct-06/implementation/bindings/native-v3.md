# Native V3 binding

One MonetaryCalculationReceipt identity is one V3 object of type vr.profile.enterprise-monetary-calculation:MonetaryCalculationReceipt. One immutable receipt is one restricted fact at monetary.calculation.receipt. factId binds Dimension, receipt ID and digest. Native fact validFrom equals recordedAt (receipt storage time); validTo is null, supersedes is empty. The nested receipt records the calculation's own predecessor and valuation/computation clocks. A correction is another object, leaving old evidence intact.

Use the exact pinned toolchain, bootstrap three fresh synthetic company Dimensions, install code/schema/spec/AGENTS/runtime path assets, append through the V3 writer, validate outer records, then explicitly call installed validate_native and import_receipts. Outer schema acceptance does not establish nested arithmetic. No automatic dispatch, operational adapter or existing-Dimension migration is implemented. The five installed files are not a substitute for reading the complete pinned package and adoption-limits.md.

## Bounded native and storage contract

This reference has a hard lifetime limit of 256 receipt IDs per Dimension, including every correction and historical receipt. It requires the complete Dimension-wide register for this model. Splitting registers or omitting old leaves loses same-ID conflict detection and is unsupported. This is a bounded adoption fixture, not a production store; production paging/indexing/retention requires a separately reviewed design.

validate_native binds the genesis object record only. It does not discover or authenticate the current head, later object revisions, current access/state, or later fact supersession. Object revision, retirement and native retraction are outside this version. A trusted host must inspect full native history and current permissions before access; passing an old genesis record never proves current access. Native record timestamps are strict UTC seconds, without fractional seconds.

The same closed resource bounds apply to receipt JSON and native envelopes: depth 16, 32 keys per object, lists at most 256, generic strings at most 512 characters, integer magnitude at most 9999, and 2 MiB canonical/wire size. This intentionally accepts a narrower envelope vocabulary than general V3. Schema-specific bounds may be tighter.
