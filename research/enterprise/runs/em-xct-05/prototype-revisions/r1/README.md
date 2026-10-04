# EM-XCT-05 — metadata-only research prototype

This is a tested research candidate, **not an installable Vercy release**, native V3 integration, production security boundary or completed externally audited metamodel. Candidate version `0.0.0-prototype.1` is local research syntax and reserves no public runtime ID. English public evidence contains only authored model material and synthetic examples.

## Contract

Two immutable records are supported: a proposal containing 1–32 single-object metadata members, and a review referring to exactly one proposal identity/revision/digest. Proposals may contain multiple distinct source objects; every member names exactly one. A calculated source aggregate must already be owned/modelled by its domain. The review does not become that domain aggregate.

Every proposal pins its audience, purpose, environment, known previous-release context and custody-instruction context. Every member pins source revision, source schema, output shape and 1–64 named top-level scalar fields. Every field has 1–8 exact classification-binding references. These are opaque external record pins: identity, revision and digest. This prototype does not duplicate external scheme/term definitions, retrieve/interpret artifacts, validate source values or infer a classification order.

The host snapshot must contain the complete current context/member declarations for this proposal and the complete active review-pin set. The host attests that the selected fields are scalar leaves of a closed source schema and that its external pins actually resolve to their declared objects, classifications and current custody context. The reference checks exact agreement, not the truth or completeness of those assertions. Merely echoing the caller's proposal as the host snapshot defeats the integration contract.

`inspect()` returns restricted internal applicability diagnostics. It requires a **trusted host assertion** for Dimension and inspect capability before inspecting record contents. This assertion is not an authentication token, signature or user request field. The host must authenticate and authorize the request separately. No result is suitable for forwarding verbatim to a recipient. Uniform HTTP refusal, timing/existence protection and actual serving are not implemented.

Current author/reviewer authority, exact context/membership, the complete review set, withdrawal and the half-open review interval `[validFrom, validTo)` affect applicability. Assessment time cannot predate proposal capture; future capture is stale. A cleared applicable review yields `applicable-review` with `notServingAuthorization=true`. Rejection, inconclusive assessment, absent/expired review, stale context and conflicting active verdicts remain distinct. An explicit startup profile permits self-review; segregation profiles require a different reviewer. These are governance choices, not a NIST conformance claim.

The `priorReleases` pin records the host's known relevant release context, not all knowledge held by every recipient. Human clearance and exact pins do not prove privacy, prevent subtraction/re-identification, or erase earlier releases. `custodyContext` is an opaque pin to separately owned instructions, including any unresolved hold/schedule conflict. Matching it proves no permission to retain, serve or destroy. No actual disposition-state calculation exists here.

## Identity, time and changes

The digest is SHA-256 over the entire record with only its top-level `digest` member removed. Type/version, Dimension, identity, revision and body are included. Encoding is a named local restricted JSON representation: UTF-8, sorted string keys, compact separators, no floats/nonfinite values or Unicode normalization; list order is significant. This is not RFC 8785/JCS. JSON input rejects duplicate keys, invalid UTF-8 and non-integer numeric syntax. No missing offset or leap-second support: timestamps are actual calendar instants in whole UTC seconds with `Z`.

`seal()` computes content integrity and validates local structure. It does not approve content. `import_records()` performs a pure transactional immutable merge: same revision+digest is idempotent; a conflicting revision fails; corrections use a new revision and preserve history. It does not persist, authenticate the writer's object-specific role, compare-and-swap a database, or enforce review authority at write time. The host must do those things. Imported unauthoritative reviews may be retained as evidence but cannot count as applicable under a different current authority snapshot.

No automatic supersession resolution is implemented: the host supplies the complete current active-review set and records its decision to withdraw/supersede a prior review. The nullable `supersedes` pin preserves the declared evidence link; the reference does not resolve its existence, direction or cycle graph. Future lifecycle integration must validate this relation or remove it before release. Historical answers need preserved snapshots and current permission to read those records; no past serving decision is reusable as a current grant.

## Execution and limits

Run `python test_disclosure.py` with Python 3.11+ and `jsonschema==4.26.0`. This writes a test report and three synthetic fixtures. The reference has no network, data-serving or destruction operation. Input bounds (256 KiB, depth 20, at most 128 entries in a generic list/object, 32 members, 64 fields/member) are prototype constraints, not a tested denial-of-service protection.

The 51 tests include three profiles, schema/classification/context drift, changed membership/fields/order, known prior-release/custody-context changes, withdrawn authority, reviewer segregation, half-open expiry, equal-authority conflict, incomplete review sets, immutable correction/import, type preservation, rights assertions, malformed/unsupported JSON, nested-field rejection and round-trip. They do not test a real source resolver, policy engine, schema compiler, reviewer judgment, custodian, database concurrency, recipient channel or native V3 engine.

Before release: audit this frozen prototype with Claude and Grok; implement or precisely defer cross-record supersession and source-binding semantics; complete the Bundle/Layer/Finding/Question/Artifact/Action tree, five facets and mastership contracts; test representative native V3 binding; choose and publish an immutable model version through Vercy's normal pipeline. A prototype test pass is not that release.
