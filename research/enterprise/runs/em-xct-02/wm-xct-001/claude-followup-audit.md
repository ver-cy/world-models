# Verdict: **ACCEPT WITH LIMITS**

I found no concrete defect in this bounded, trusted-host, in-memory reference that justifies BLOCK. Every B1/B2 and M1–M5 disposition matches the code. I traced the relevant paths by hand; I did not execute anything. The remaining holes are mostly disclosed deferrals. A few are undisclosed edges or unverified bindings, and none is an internal contradiction in the machine identity. The holds are listed at the end.

**What I did not verify:** composer and native-validator semantics, whether any digest matches actual bytes, whether the embedded `spec.json` contract equals `model-spec.md`, and the reported 53/53 test pass. I counted 53 tests in `test_authority.py`, which matches the report, and hand-traced about 15 of them against the code.

---

## Blockers

**B1 — native identity: resolved.**
- **Companion:** `modelId` is `vr.profile.enterprise-fact-authority`, with namespace `urn:vercy:model:vr.profile.enterprise-fact-authority`.
  - The binding `forSpecificationDigest` is the `spec.json` descriptor digest.
  - The companion descriptors cover runtime, schema and validator.
  - `runtime-model.reference.json` has the same `modelId` and the path `authority.register.snapshot`, which is the stored fact path.
- **Parent:** WM-XCT-001 is `semantic-only` with `binding=None` and no descriptors beyond spec and AGENTS. Both releases are explicit roots.
- **Digest cross-check:**
  - The report pin `sha256:cf027b56…` equals the bare `spec.json` source digest `cf027b56…`.
  - The parent pin `a09261ca…` equals the crosswalk and composition `specSha256`.
- **Publication vs research status:** these are separate fields (`publicationStatus: published` and `researchAssurance: reviewable-draft`). The "published" value is candidate metadata, and the report's `limits` string discloses this.

**B2 — envelope authority: resolved.**
- The fact has `authority.source = urn:synthetic:register-operator` and `masterSystem = provenance.source = urn:synthetic:governance-register`.
- Acceptance asserts the operator is not any `accountable` party or steward in any authority.
- Domain precedence exists only in nested `rules`.
- The operator is not checked against `issuedBy` or `writers`. The disposition does not claim that check, so this is not a defect.

## Major findings

**M1 — snapshot extension: resolved.**
- `validate_extension` checks:
  - that the header (format, version, dimension) is identical;
  - that each collection's prefix is byte-identical via `encode`;
  - that every appended row's receipt is strictly after the prior global head.
- Acceptance rebuilds the fixture through the installed companion's `admit` and gets exact fixture equality.
- It then admits a correction, stores r1/r2 with `supersedes` and `previousSnapshotDigest`, and rejects a truncated stored r2.
- `previousDigest=module.digest(correction)` is evaluated before `update()` is applied, so it correctly hashes the predecessor.

**M2 — retry: resolved.**
- The replay check compares everything except `recordedAt` and returns the unchanged ledger, so the original receipt is kept.
- Current authorization runs before the replay check. The issuer/governor check applies to authorities, and `authority_for_write` applies to observations.
- A changed payload raises "Conflicting replay".
- Side effect (acceptable, and implied by "current authorization still required"): after a grant is revoked, a retry of a record that is already stored returns a rejection.

**M3 — writer rotation: resolved.**
- `stable` for observations is dimension, scope, predicate, subject and source. `writer` is excluded.
- `authority_for_write` keys on the record's immutable source plus the current actor.
- `test_rotated_source_writer_can_retract` covers this path, and the original writer survives in revision 1.

**M4 — trusted-host boundary: resolved as a disclosed limitation.**
- The boundary is stated in the `admit` docstring, the model-spec "Host integration" section, the README and AGENTS.
- No service projection is implemented, and none is claimed.

**M5 — change kinds and closure guard: resolved.**
- **Change-kind rules:**
  - `change` is a required enum.
  - Genesis is required at revision 1 and forbidden later.
  - `retraction` holds exactly when the state is retracted.
- **Closure guard:**
  - A closure requires a strictly reduced end.
  - It is compared against the old record with the end changed and part ends clipped (`min`). Everything outside the exempt set must be equal.
  - The exempt set is `{revision, previousDigest, recordedAt, change, evidence, issuedBy|writer}`.
  - The state cannot change under closure.
  - `test_closure_cannot_change_accountable` covers this.
- Full-term correction is unguarded, as labeled.

## Low findings, Grok items, retention and pins

- **L1 / L3 / Grok medium: resolved.**
  - `observationIds`, `evidence`, `observationPins` (id, revision, sha256) and `unrankedObservationIds` are populated before both early returns: authority-contested and missing-authority.
  - `rulePins` and `routePins` are set before the `overlapping-source-rules` return.
  - Part pins carry `authorityId`, `authorityRevision` and `authoritySha256`, matching the spec's `(partId, authorityId, authorityRevision, authorityDigest)`.
  - `value` stays `None` on every non-preferred path.
  - `test_no_authority_retains_evidence` covers retention.
- **L2: resolved.**
  - Part IDs are checked against issuer, accountable, stewards, rule and grant sources, and writers.
  - A collision with a record ID is caught by `ids.intersection(parts)`; the `part-id` subtest exercises this.
  - Cross-authority collisions are allowed, as scoped.
- **L4, L5, L7, L8: consistent with the code and docs.**
  - `inputDigest` covers the header.
  - Bare-hex record digests and `sha256:`-prefixed descriptors are documented as distinct encodings.
- **L6: resolved.**
  - Policy and plan windows derive from real UTC.
  - Domain admission uses the rows' own `recordedAt` as `now`, inside the fixed config window. The run is therefore reproducible until the config's `validUntil` passes, because evaluation uses a fixed `now`.
- **Grok lows: behavior matches the stated dispositions.**
  - Contested write grants are retained in archives while live admission denies them.
  - Observation intervals can exceed the governance term without inventing authority.
  - `Denied` is a separate `ValueError`.

## Machine-identity contradictions: resolved?

Yes. The own ID, own `spec.json` digest, semantic-only parent with `binding=null`, and a distinct register operator remove the prior contradiction (a parent identity bound to non-conforming records). What remains is presentational or unverified, not contradictory:

1. **Hosting path.** The schema `$id`, `canonicalUrl` and `sourceUrl` all sit under `/models/wm-xct-001-ownership-stewardship/profiles/…`. This is disclosed as "URI optics", and the README explicitly denies an is-a relationship.
2. **Semantic reference count.** `spec.json`/`composition.yaml` list three semantic references (001, 002, 012), but the plan's `references` includes only WM-XCT-001. This is consistent only if 002 and 012 are documentary-only. That should be stated in one sentence.
3. **"Optional" reference not verified.** The spec calls the parent reference "optional", but the plan roots and references it with an exact version. Whether the composer treats `references` as non-blocking is outside this input.

## Remaining holds

**Disclosed deferrals (accepted as limits):**
- No IAM or authentication.
- No durable or concurrent storage; one receipt per second.
- No signed publication.
- No subject/scope proof, connectors, recursive delegation, independent assignment streams or fine-grained disclosure.
- No legal or domain conformance, and no parent conformance.
- Forged or incomplete root snapshots are outside the trust boundary.
- Historical queries require the current config.
- Unguarded full-term correction.
- The parent's inherited source and legal holds.

**Holds to carry forward (undisclosed or unverified, not blockers):**

| # | Hold | Type |
|---|---|---|
| H1 | Candidate `publicationStatus: published`. The acceptance report is not evidence of publication. After actual publication, the registry digest must equal `sha256:cf027b56…`, or acceptance must be rerun. | Disclosed, needs a gate |
| H2 | No validator checks the stored `supersedes`/`previousSnapshotDigest` chain. It is written, not verified. Replacing r2 with r1 (rollback) passes `validate_extension(r1, r1)`. Freshness depends on the host holding the latest trusted snapshot digest. | Undisclosed edge |
| H3 | A closure cannot express a cutoff before a part's `validFrom`: the clipped part becomes an empty interval and `interval()` rejects it. That case forces an unguarded correction. | Undisclosed edge |
| H4 | A `correction` can move a retracted record back to active or asserted (revival). This is not forbidden and not documented. | Undisclosed transition |
| H5 | Scale at the declared `maxItems` of 10,000 is not demonstrated. `schema()` re-reads the schema file and builds a validator for every record, `validate_ledger` has a quadratic head-order check, and `admit` validates twice. | Performance limit |
| H6 | `admit` raises only `Invalid`, including for authorization failures. The "catch Denied separately" guidance applies to `evaluate` only. This is harmless given the generic-rejection rule, but the wording should say so. | Documentation precision |
| H7 | The report's `sourceDigests` omit `runtime-model.reference.json`, `AGENTS.md` and `composition.yaml`, although the first two are bound descriptors. The report alone cannot attest those installed bytes. | Traceability |
| H8 | `spec.json` contract equality with `model-spec.md`, byte-level digest correctness, and composer/native semantics were not verifiable in this review. | Out of scope |

This is a research review, not publication or deployment authorization. The research assurance level stays reviewable-draft.
