# EM-XCT-01 0.1.0 — focused remediation audit

**Verdict: ACCEPT WITH LIMITS**

Not publication authority. Prior audits stay on the record. This note only judges the focused B1/B2/L1/L2/CX5 bytes plus the supplied clarification and reports. Schema body was not re-sent; its hash matches the previous freeze (`d5dbab037ea7af7f5b9feef95929f461380d824849caad092af7ea1706cc54c7`). I did not execute the reported 87 tests or three native scenarios.

---

## Focused fixes versus the supplied evaluator

### B1 — complete assertion must be canonically encodable

`validate()` now calls `encode(assertion)` after schema checks. `encode` UTF-8–dumps the whole object (`ensure_ascii=False`) and maps `UnicodeError`/`ValueError`/`TypeError` to `Invalid`. A lone surrogate in the latest `reason` or `evidence.description` is therefore rejected on `validate` / live import, not only when some earlier event is digested.

The two new import tests match that path. Residual: parse/decode failures elsewhere still need not become `Invalid` (already disclosed).

### B2 — proposals do not reserve `(issuer, assignmentId)`

Reservation is only:

```text
last state ≠ retracted  AND  some event state == asserted
```

Unasserted proposals do not enter `bindings`. Retraction drops the reservation and keeps the row. Two live asserted rows with the same issuer-qualified assignment id and different binding bytes still raise `active asserted assignment has different binding content`.

`resolve()` adds `retainedObservationConflicts` over the **whole** input (proposals and retractions included). That is a report, not a second allocator.

The three regressions match the stated story: bogus lowest-privilege proposal → genuine different observation → assert genuine; retract then different observation; two active asserted observations still rejected.

Residual (explicit, not a reopen of B2): this is write-time reservation of *carried observation bytes*, not 011 exclusive allocation, not a global collision register, and not temporal “asserted as-of now”.

### L1 / prior CX3 — dispute prior is filtered history

```text
history = events with recordedAt ≤ known_at and effectiveAt ≤ valid_at
prior   = history[:-1]
```

A later-effective `asserted` is absent from `prior` at an earlier `valid_at`, so a backdated proposal-level dispute becomes `candidateDisputes` and does not veto an independent accepted claim. The new `test_dispute_prior_must_be_effective_at_query` is the previous counterexample.

Documented corollary remains: a dispute whose **filtered** prior contains `asserted` still sets `contested`, including a previously asserted negative with no positive.

### L2 — `evaluation_at` meaning

Code is unchanged: `known_at ≤ evaluation_at`, and `evaluation_at` inside the frozen policy window. The clarification that this argument is the caller-supplied current clock, not a simulated future-knowledge horizon, is consistent with the function. Clocks stay unauthenticated.

### CX5 — space / U+FF0F in subject URI

No extra normalizer. Tests expect `SCHEMA` failure from the already-required `uri` format checker on unchanged schema bytes. I cannot confirm checker behaviour in this pass. If `jsonschema[format-nongpl]` rejects those strings, CX5 is closed; the tests are the contract. `local_reference` still does not itself ban spaces or U+FF0F.

### Extra test

Reseal-after-target-change now hits `claim-bearing content changed` on import instead of failing only on an unsealed genesis digest. That closes a test gap, not a new rule.

---

## Limits that are unchanged (still not BLOCK items)

- `validate_set` / CLI still do not enforce receipt time or global head; only `import_assertion(..., now=)` does.
- Policy, clock, evidence authenticity, and scheme-kind truth remain caller-trusted. A policy that *registers* an account scheme as `person` still admits that link.
- Live import remains one new transition per UTC second for the whole retained set.
- No inverse subject index.
- Crosswalk stays narrower/overlap; parent 011/036 holds including Claude-only 036 and 108-source re-verification stay open.
- Native V3 `rank: 0` is outer snapshot metadata; companion must still be invoked separately.
- Pins check trusted local source bytes, not a sandbox. Installed schema files must stay protected.
- Group/AI fixture bodies, harness pins, and catalog sidecars were not in this focused bundle.

`test-results.json` (`87`, `passed: true`) and acceptance (`passed: 3`, installed validator digest `sha256:bec1dcec…` matching the stated evaluator hash) are author reports.

---

## Principal remaining objections

The four named holes from the last full candidate are addressed **in the evaluator text and the new tests as written**. What remains is the profile’s declared trust boundary, not an unfixed B1/B2/L1/CX3/CX5.

Do not read this as: certified identity service, full parent conformance, verified 108 sources, or an independently executed 87-test run.

**ACCEPT WITH LIMITS** for 0.1.0 as a reviewable-draft reference profile of WM-XCT-036 with WM-XCT-011 carriage.