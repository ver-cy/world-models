# EM-XCT-01 second frozen candidate — remediation review

**Verdict: ACCEPT WITH LIMITS**

This is not publication authority. It does not rerun tests, does not re-hash files, and does not close WM-XCT-011 / WM-XCT-036 source or waiver holds. EM-XCT-01 remains a partial, additive 0.1.0 profile.

Original first-pass audits stay on the record. This note only judges the **supplied second-candidate bytes**.

---

## Attachment status

**Available, not truncated, for these files:** `identity_profile.py`, `identity-profile.schema.json`, `test_identity.py`, `acceptance.py`, `README.md`, `model-spec.md`, `crosswalk.json`, `examples/policy.json`, `examples/startup.json`, `test-results.json`, `acceptance-results.json`.

**Not in this freeze (bytes unseen):** `examples/group.json`, `examples/ai-team.json`, `field-catalog.json`, `whole-object-coverage.json`, `mastership-and-rights.json`, `lifecycle.json`, `tool-pins.json`, `runtime-model.reference.json`, generated companion schema views, composer/skill/upstream trees. Claims that depend on those files are unverified here.

`test-results.json` (`tests: 78`, `passed: true`) and `acceptance-results.json` (`passed: 3`) are **author reports**, not this review’s execution.

---

## What this candidate actually fixed

Against the prior Grok ACCEPT WITH LIMITS (BUG-1…8) and the stated Claude BLOCK items:

| Prior item | This candidate |
|---|---|
| BUG-1 kind retag | **Closed for label-only attacks.** `schemeKinds` + disjoint `subjectNamespaces` + `binding.kind == target.kind`. `test_retagging_both_kinds_refused`. Residual is policy-register lying (caller-trusted). |
| BUG-2 prefix escape | **Closed for the documented class.** `local_reference` rejects `% \ ? #` and `.` / `..` path segments; kind prefixes must end `:` or `/`; empty suffix refused; near-miss `personality` tested. |
| BUG-3 write-time collision | **Reclassified, not hidden.** Ledger keeps overlapping occurrences; query contests; assignment freeze is `(issuer, assignmentId)`. Documented. |
| BUG-4 negative-only → `unknown` | **Fixed.** `denied-in-input` + `opposing[]`. |
| BUG-5 effect outside window / silent skip | **Fixed.** `effectiveAt` must lie in the assertion window; exclusive end tested; missing history is `not-effective-or-known`. |
| BUG-6 backdated retraction wins | **Explicit semantic**, tested. Not a leftover bug. |
| BUG-7 unseen/open schema | **Closed for the combined file.** `additionalProperties: false`; enums; Z-second patterns; `FormatChecker` required at import. |
| BUG-8 duplicate assertion ids | **Explicit semantic.** Independent claims; replay is by assertion id. |
| F1 receipt-time import | **Implemented** on `import_assertion(..., now=)`. New events must equal `now` and `now` must exceed the global input head. Exact replay is a no-op *before* the receipt check. |
| F3 empty/invalid policy | **Fixed.** `validate_policy` runs even on `[]`. |
| Candidate dispute veto | **Fixed.** Dispute without a prior `asserted` → `candidateDisputes`, does not set `contested`. |
| Genesis / event chain | Genesis `previousDigest == claim_digest(assertion)`; later events digest the previous event. |
| Data class / reader gate | `personalDataClass ∈ policy.dataClasses`; reader/purpose checked before `validate_set` in `resolve`. |
| Endpoints / source≠target | Assert requires both `endpointResolution` values `resolved`; `sourceReferentRef != target.id`. |

The README / model-spec / crosswalk now match the executable contract on the points that previously over-claimed: `accepted-in-input` is input-scoped; outer V3 `asserted` is snapshot-recorded; companion is mandatory and separately invoked; 036 remains Claude-only with 108-source and empty relationship-contract holds; no full parent conformance.

That is a material remediation, not a rename.

---

## Remaining executable counterexamples

These are logical traces against the supplied evaluator. They were **not run**.

### CX-1 — Policy can still register an account scheme as `person`

Frozen registers stop *retagging*. They do not stop a new policy from declaring:

```text
schemeKinds += { scheme: urn:git:account, schemeVersion: 1,
                 issuer: urn:synthetic:source:hr, scope: urn:synthetic:tenant:startup,
                 kind: person }
binding.kind = person
target.id    = urn:synthetic:subject:person:p1
```

`validate()` accepts if the digest is pinned to that policy. Source meaning stays external. Do not republish “cannot become Person even by override” without this caveat.

### CX-2 — `validate_set` / CLI bypass live-import invariants

`main()` only calls `validate_set`. A hand-built two-event history dated `2025-01-01` still validates. Receipt time, global head, and “one new event per second” never run. README already says historical restore is a separate trusted path. Any adapter that writes through CLI/`validate_set` re-opens F1.

### CX-3 — Dispute class uses raw prior, not valid-time-eligible prior

```text
E1 proposed   recorded=T0  effective=T0
E2 asserted   recorded=T2  effective=T2
E3 disputed   recorded=T3  effective=T0
query valid_at=T1  (T0 ≤ T1 < T2),  known_at=T3
```

Filtered last event is E3 `disputed`. `prior = history[:index(E3)]` still contains E2, so the row is treated as a vetoing dispute → `contested`. At `T1` the activation had not taken effect. Classification is chain-order, not `(validAt, knownAt)` eligibility. Tests do not cover this mix.

### CX-4 — Global head is process-wide, one event per UTC second

Any existing event recorded at `T` blocks **every** assertion’s new live event at `T`, including unrelated ids. Intended at one-second granularity; it is a queue, not a per-assertion head.

Two transitions on one assertion cannot share one live receipt: `recordedAt == now` for all new events and `recordedAt` must strictly increase. Documented; still a live-path limit.

### CX-5 — Suffix after a legal kind prefix is not a local identifier grammar

```text
target.id = "urn:synthetic:subject:person:p1 extra"
```

No `% \ ? #`, no `.`/`..` segments, `len(id) > len(prefix)`. Accepted. Spaces and non-ASCII separators (e.g. U+FF0F) are not in `local_reference`. This is weaker than “local subject URI” as a closed identifier.

### CX-6 — No inverse subject index

`resolve` keys only `(scheme, schemeVersion, issuer, scope, value)`. “Three person-reference exports, one Person” is three separate `accepted-in-input` answers. There is no query-by-`target.id`. Startup fixtures demonstrate the one-hop lookup, not a subject assembly API.

### CX-7 — Unseen group / AI fixtures

`test_three_profiles`, `test_reassignment_temporal`, and acceptance profiles `group` / `ai-team` load files that are **not in this attachment**. Those three native scenarios are report-only from here.

---

## Out of scope (not defects in this checker)

Authentication, evidence authenticity, four-eyes, cryptographic attestation, RFC 8785, 011 assignment *allocation* / quarantine reuse engine, cross-scheme alias resolution, existing-Dimension transactional update, IAM, merge/split, `owl:sameAs` reasoner, re-verification of 108 036 sources, second-provider review of the parent.

`grantsAccess: false` and `globalEquality: false` are hardcoded. Ranking is absent (`rank: 0` is outer V3 metadata only). That matches the native note.

---

## Limits that must travel with any 0.1.0 label

1. Additive profile of WM-XCT-036 with WM-XCT-011 carriage. Crosswalk relation is **narrower / overlap**, not conformance, not a ratified registry edge.
2. Policy, clock, evidence, and input completeness remain caller-trusted. Live import is the only path that even *declares* receipt time.
3. Overlapping assignment occurrences are evidence, not allocator errors.
4. Companion validation is mandatory; raw V3 success is not identity-valid. Acceptance demonstrates the distinction only if the unseen harness/pins match the report.
5. Parent publication holds in `crosswalk.json` stay open, including Claude-only 036 and live re-verification of cited URLs.
6. Do not quote `passed: true` / `passed: 3` as this review’s result.

---

## Principal remaining objections

The candidate is now internally aligned enough to be a **reviewable-draft reference profile**, not a merge engine and not a completed parent implementation.

The objections that still matter for adoption:

- Kind safety is register safety. A bad register is still a Person.
- History guarantees exist only if writers use `import_assertion` under a lock. The shipped CLI does not.
- Dispute × bitemporal classification is coarser than the stated `(validAt, knownAt)` rule.
- Group/AI and pin/catalog sidecars were not in the freeze, so the “three native Dimensions” claim is outside this review’s evidence.

**ACCEPT WITH LIMITS.** Do not treat this as clearance to publish as certified enterprise identity, as full 036/011 conformance, or as a replacement of the retained first audits.