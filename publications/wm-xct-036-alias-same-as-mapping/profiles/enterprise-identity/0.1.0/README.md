# Enterprise identity assertions

Version 0.1.0 is a bounded reference profile associated with WM-XCT-036 Alias / Same-as Mapping and a narrower WM-XCT-011 assignment carrier. Research assurance: **reviewable-draft**. It is available for inspection and synthetic adoption; it is not a certified enterprise identity service or complete parent-model implementation.

An assertion links a source's declared referent to one existing local subject in a named Dimension, purpose and validity interval. Its qualified identifier is the lookup carrier, not a claim that an identifier token is a Person. Several reviewed person-reference exports may identify one local Person. Git/tracker accounts and service accounts remain distinct kinds. Account ownership is a separate relationship, outside this release.

## Run and inspect

Use Python 3.12+ with `jsonschema[format-nongpl]>=4,<5`:

```text
python -m pip install "jsonschema[format-nongpl]>=4,<5"
python test_identity.py
python identity_profile.py examples/startup.json --policy examples/policy.json
```

The **executable schema** is `identity-profile.schema.json`. Four companion schema views are generated from its same definitions; the code loads the combined file only. Policy/claim/event digests are SHA-256 over UTF-8 JSON with sorted keys, no insignificant whitespace, `ensure_ascii=False`, and no nonfinite numbers. This Python serialization profile is not a claim of RFC 8785 conformance. Distribution/composer pins instead hash raw file bytes.

The fixtures are synthetic: three person-reference exports for a startup, scoped/reassigned references for a group, and separate human/service-account references for an AI team. They contain no organizational personnel records. The group example has a deliberately pre-agreed fixed end date; it does not demonstrate learning an assignment closure later.

## Read the result

`resolve()` returns `accepted-in-input`, `contested`, `denied-in-input`, `candidate`, `proposal-only`, or `unknown`. It includes supporting/opposing IDs, candidate disputes, negative proposals, exclusions, time coordinates, caller/purpose and digests. `accepted-in-input` means one admissible positive target in this supplied set. It does not prove global uniqueness, source completeness, identity or access rights. A negative assertion against a different target does not contradict a positive claim. A dispute of a previously asserted claim blocks acceptance; a disputed unasserted candidate does not veto an accepted claim.

Different assignment occurrences sharing a qualified key are **preserved**, not rejected on ingestion. Simultaneously active different target claims produce `contested` in the query. This is an assertion-evidence ledger, not an issuer's assignment allocator; write-time namespace exclusivity and a global collision register are deferred. Separate assertion IDs preserve independent supporting claims; replay idempotency is by assertion ID, not semantic deduplication.

## Live import and history

`import_assertion(existing, incoming, policy, now=trusted_receipt_time)` is pure and writes nothing. Every new event must use the supplied receipt time, strictly after the current input's recording head. At second precision, stage one transition per receipt; batch historical events are not accepted through the live import path. Identical replay is a no-op. Fixed claim content and all prior events must remain unchanged. Genesis commits to the fixed claim digest; subsequent events commit to the previous event. These hashes detect inconsistency, not forged signatures.

Historical fixture restoration is a separate, explicitly trusted snapshot operation. `validate_set()` alone cannot prove when data was received or whether history was truncated. A caller bypassing the live import function loses its historical-preservation guarantee. A real adapter must authenticate the clock/policy/evidence, persist the accepted set and import head under a lock, and compare the expected head. No production writer adapter is supplied.

Backdated **effective** corrections are allowed inside claim validity. At a given knowledge time, the latest recorded eligible correction wins from its effective date, including over an earlier activation. Past knowledge answers remain stable only when future additions pass the trusted live-import path and the input set is retained. Input digests include the complete supplied history and may change even when a historical answer does not.

## Trust and limitations

- Policy registers scheme/version/issuer/scope to referent kind, and assigns disjoint kind namespaces inside the local subject namespace. Changing two kind labels cannot bypass those declared registers. The source's real meaning, endpoint existence and evidence authenticity remain external checks. No four-eyes separation is enforced.
- Local subject references use a restrictive URN/HTTPS profile: no percent escapes, dot segments, query, fragment or backslash; an empty local suffix is refused. This is rejection, not silent URI normalization.
- One frozen policy covers writers **and readers**. Any policy change invalidates every pin and fails closed. There is no separate dynamically rotating read policy. The synthetic policy expires on 2027-01-01. Continued use needs an explicitly reviewed new policy/claim set; changing policy in place is not a supported migration. Current-clock checks must never be bypassed by backdating a real read.
- Binding fields form an immutable source observation. A conflicting proposal does not reserve an assignment. Active previously asserted observations must agree; after retraction a corrected observation may be carried by another assertion ID. Retained conflicting observation envelopes are reported separately. Full source-state revision is not implemented. No fake new source assignment ID may be invented to evade this limit. Unknown or pre-recorded future-effective assignments, historical assignment revision, cross-kind negatives, normalization, matching, transitive closure, endpoint merge/split, policy history, erasure and federation remain deferred.
- Raw V3 validates only the outer snapshot record. The **companion validator is mandatory and is explicitly invoked by the acceptance harness; native V3 does not automatically enforce it**. The outer `asserted` status means the snapshot was recorded, not that the inner identity claim is accepted. V3 requires a numeric rank; the harness uses neutral `0` on the snapshot only. The identity resolver never reads it and performs no authority ranking. Outer validity begins when the snapshot is recorded; identity time must be queried through `resolve()`.
- The acceptance harness checks byte-pinned tooling/upstream inputs, installed validator/schema digests and actual stored-snapshot equality. It creates three temporary new Dimensions and demonstrates that V3 alone accepts a bad nested assertion which the companion rejects. It is time-bounded to the disclosed 2026 fixture window. No existing-Dimension transactional update, persistent truncation prevention or production concurrency is tested.
- The parent models' original publication holds remain, including broad source verification and formal boundary work. This increment does not clear them. Independent study/audit scopes and unresolved limits are recorded separately.

See `model-spec.md`, `crosswalk.json`, `field-catalog.json`, `whole-object-coverage.json`, `mastership-and-rights.json`, `lifecycle.json`, and the test/acceptance reports. Start adoption with the full envelope and a trusted policy; never export a bare ID-to-person table as equivalent.

## Final audit clarifications

`evaluation_at` is the caller-supplied trusted current clock, not an arbitrary simulated future knowledge boundary. The function enforces `known_at <= evaluation_at`; the caller authenticates the clock. Static validation and the CLI do not enforce live reception history. At second precision, live imports are globally serialized to one new transition per second in the retained input set. An inverse subject index is not supplied.

Assignment observation reservations are scoped to claims that reached asserted and are not retracted. Unasserted proposals cannot permanently squat a source occurrence. Retraction releases that reservation without erasing the old observation; `retainedObservationConflicts` reports conflicting carried content across the full input, including proposals/retractions. Source truth is still external. A dispute uses only prior events effective at the queried valid time. A disputed previously asserted negative can produce contested even without a positive claim.

Integrity checks pin trusted local **source bytes**, not a hardened execution sandbox: Python import paths/bytecode and changes after verification remain part of the trusted environment. Loader parse/decode exceptions fail closed but are not all normalized to Invalid. Runtime schema integrity must be protected after installation. Source-referent namespaces, issuer qualification of assertion IDs, URI alias identity and complete parent endpoint admissibility remain external governance, not proven by string comparison.

`retainedObservationConflicts` is a whole-input diagnostic, not a historical answer: it can include unrelated assignments and records later than knownAt. Authorize the complete input before calling this reference; do not present that diagnostic as evidence known at the query date. Effective-time filtering can produce a non-contiguous event history by design.
