# R1 implementation audit — adjudication and R2 work

22 September 2026. Both actual provider responses were read in full. Claude Opus 5 High says **revise-before-release**. Grok Heavy says **accept-with-explicit-limits**, but its acceptance does not dispose of Claude's concrete counterexamples. **R1 must not be released.** It remains immutable public research evidence; the working implementation is separate.

Both received the identical 264,109-character frozen packet (SHA-256 `9033b68dcb6a218e5e8328dc0c050e58e8437fed9484053a13402d79ec8349de`). Claude's pasted preview matched after outer trimming; Grok's matched exactly. The packet explicitly identified 28 shown files and the supplemental hash-pinned files it did not show. JSON displays were compacted and not presented as raw-byte hash verification. Original Markdown/code was not abbreviated.

Claude's response was obtained via the provider Copy control. An immediate stale clipboard read returned the original prompt and was rejected; the subsequent read returned the complete 18,843-character audit. Grok's Copy response contains 18,113 characters, including its own opening team sentence. That sentence is not agreement among Claude, Grok and Codex.

## Method caveat

The common prompt requested no tools. Claude states it used none; no external tool activity was observed. Grok's UI displayed attachment extraction, file reads and a code-executions panel. Its final answer says it did not run the package tests; the complete executed code was not inspected. **Grok R1 is preserved as a frozen-input tool-assisted implementation review, not a strict no-tools audit.** A focused/final R2 review must make its actual method explicit; do not retroactively relabel R1. The owner is not asked for new permission because review and fixes are already authorized.

## Accepted corrections

| Finding | Disposition | Required work |
|---|---|---|
| Claude B1: later resource creation invalidates an earlier correct rejection | Confirmed independently against the actual frozen R1 bundle | Resource revisions need a host control sequence; historical preconditions must use existence at that sequence, including same-second creation. |
| Claude B2: executor can exceed the snapshot's 10,000-row bounds | Accepted; capacity promise and mutator behavior disagree | Align authoritative store admission/capacity with archive bounds; roll back a whole attempted operation on overflow; avoid evidence growth by an actor with no current rights. Document exhaustion and test the actual boundary. Consider definitions/policies/resources/requests as well as Events. Do not create a fresh store/key automatically on capacity exhaustion. |
| Claude M1: terminal replay denial hides committed state from an authorized reader | Accepted as an API clarity defect | Preserve current read independently. A readable denied replay must disclose the retained terminal state/request identity rather than look identical to pending denial. Do not grant read to execute-only callers. |
| Claude M2 / Grok L3: native records omit policy/retirement state needed for replay | Accepted binding gap | Retain the exact snapshot and manifest inside the installed synthetic Dimension as mandatory companion evidence; validate from stored readback, not only the in-memory snapshot. State that native objects alone do not prove definition availability, policy or latest state. Do not add a duplicate execution master. |
| Claude M3: missing transaction tails can be accepted after rewriting snapshots | Accepted internal-consistency gap, separate from unavoidable complete forgery | Validate forward completion of each control-sequence operation: submission/delivery/try and required receipt/disposition/observation. Add removals of delivery, try, receipt, cancel outcome and observation outcome as negative cases. |
| Claude M4: retiring a definition prevents same-pin compensation | Accepted as a visible narrow limit | Document it prominently and test it; a reviewed cross-version compensation contract remains deferred. |
| Both: simulation flag is outside a lock saying published | Accepted fixture-label risk | Determine whether the native validator accepts candidate status; use candidate plus an in-lock simulation flag if supported. Never weaken the native validator or ship a falsely published lock to make a test pass. The old composer route is not being used. |
| Claude: malformed archive/row exceptions escape | Accepted | Normalize supported malformed-input errors to Refused or withheld at entry points. Add malformed manifest type/files/encoding, corrupt row and integer/shape tests without treating corrupted state as valid. |
| Claude: raw event IDs used as filenames allow Windows colon/case hazards for imported snapshots | Accepted export-boundary issue | Use portable deterministic filenames derived from full IDs, retain IDs in payloads, verify exact mapping and closure, and test colon/case distinctions. Generated fixture UUIDs being safe does not excuse the archive API. |
| Claude: partial-file interruption cannot resume in place | Accepted stated-scope correction | Implement durable temporary-file publication or explicitly require a new export directory after a torn file; do not describe the existing between-files test as crash/power-loss recovery. Preserve mismatched evidence rather than overwrite it. |
| Both: read transactions allocate cut sequence; denied observe/cancel and retired-key behavior differ | Accepted documentation/testing work | Specify these endpoints exactly, define expiry materialization separately from effect permission, and test read-only terminal/retired behavior. |
| Claude: finding-level answer data is generic | Accepted semantic quality improvement | Replace duplicated finding-level hints with precise per-question answer contracts and explicit insufficient-context handling. Enrich the layer grouping only where it expresses real semantic distinctions. |

## Corrections to reviewer wording

- Grok's statement that `_bounded` allows 256 object members is inaccurate: objects are capped at 128, arrays at 256. Bool is a valid JSON primitive for boolean fields; the integer schemas correctly refuse it for revision/time. Do not ban all booleans.
- The request's derived state, receipt and key-retirement status are reconstructible from native Events. The missing **policy and definition retirement** snapshots are the binding problem, not proof that every omitted derived field needs a second master property.
- A native Event's host issuer is deliberately different from the request actor/observer. Clarify the mapping instead of replacing its issuer with an unauthenticated asserted party.
- Empty labels and empty lists are within the named synthetic opaque-label operation. They are not arbitrary code or a general company tag validator. Make the allowance explicit rather than inventing a business restriction.
- Fixtures using source helpers to build inputs do not invalidate the observed installed Executor execution; nevertheless, R2 can construct/verify reference pins through the installed companion too and should show bundle-build evidence directly.
- Startup/matrix/AI-service currently demonstrate self versus direct representation in three independent Dimensions. They do not implement a matrix organization or an AI governance system. Keep that limit explicit; additional meaningful distinct scope cases are desirable, not permission to invent claims about real companies.
- Grok's accepting verdict missed B1, B2 and M3. Preserve the disagreement; do not average verdicts or call this unanimous acceptance.

## Work already performed after the R1 freeze

`r1-history-probe.json` records the B1 reproduction against the immutable R1 bundle. The working `action.py` now stores resource `control_sequence`; `history.py` checks historical resource existence and includes that sequence when replaying effects. A new regression covers later creation both in the same second and the next second, followed by a valid new request. **51 source tests pass.** The standalone bundle was regenerated, but the entire bundle suite and native installations have not yet been rerun for this post-R1 revision. Their R1 reports must not be reused as final R2 evidence.

All remaining corrections above are outstanding. Complete them in the working directory, regenerate schema/bundle/metadata, run appropriate source/bundle/native checks, create a new immutable R2 freeze and obtain actual independent focused/frozen reviews. R1 files and hashes must remain unchanged. No new broad research round is needed.
