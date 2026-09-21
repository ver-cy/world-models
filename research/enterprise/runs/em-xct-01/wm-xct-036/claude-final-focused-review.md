# Focused remediation audit: EM-XCT-01 profile 0.1.0

**Verdict: ACCEPT WITH LIMITS**

## Scope of this verdict

This verdict covers only what you sent in this message:
- the final `identity_profile.py`
- the nine new regression tests
- the documentation clarification
- the compact reports and hashes

I did not see the combined schema body, the `IdentityTests` helpers (`other`, `append`, `seal`, `query`, `rows`), the earlier tests, `acceptance.py`, or the native harness. I did not execute anything. I did not recompute any hash. The 87 passing tests and 3 passing acceptance profiles are your reported results, not ones I verified. This is not a complete source review or a parent-model review. Prior audits stand, including Claude's earlier BLOCK on B1/B2 and Grok's ACCEPT WITH LIMITS, as the record for the earlier bytes.

## Prior blockers

**B1: closed.**
- `validate` now calls `encode(assertion)` on the whole object, right after schema checks and before any digest or lifecycle check. A lone surrogate anywhere in the assertion now raises `Invalid('value cannot be canonically encoded')`. This covers any event's `reason` or `evidence.description`, not only the last one. `encode` catches `UnicodeError`, which includes `UnicodeEncodeError`.
- `import_assertion` calls `validate(incoming)` before any other use of the incoming assertion, so the live import path is covered.
- Surrogates in the query binding or reader are never encoded or echoed. They can only cause a failed match or a policy denial, so they are harmless.
- The two import tests exercise this path. Neither reseals, but that doesn't matter because the encode failure comes before the predecessor checks. Both would pass as long as the schema does not reject the surrogate first, and your report says it doesn't.

**B2: closed.**
- A claim reserves an `(issuer, assignmentId)` observation only if both hold:
  - its current state is not `retracted`, and
  - its history ever reached `asserted`.
- Proposals therefore cannot squat an assignment. A retraction releases the reservation, and because `retracted` is terminal, a released claim cannot reactivate. Asserted-then-disputed claims keep their reservation, so correcting them requires retraction. That is a reasonable, privilege-gated outcome.
- Conflict detection does not depend on list order. No evidence is deleted and no synthetic assignment IDs are introduced.
- The three tests (squat, reservation release, active conflict) test the right properties. That holds only if `other()` shares `assignmentId` with the base fixture and is asserted by default, which `test_active_observation_conflict_still_rejected` implies.

## Prior limits

**L1 / Grok CX3: closed.**
- `prior=history[:-1]` now uses the filtered history, which is bounded by both `known_at` and `valid_at`.
- `test_dispute_prior_must_be_effective_at_query` distinguishes the old behaviour from the new. Under the old code, the June activation would have counted as prior and made the result `contested`. Under the new code, the result is a candidate dispute and `accepted-in-input`.
- Remaining note: `effectiveAt` does not have to be monotone across recorded events. A filtered history can therefore be a non-contiguous lifecycle view, for example an activation followed by a retroactive retraction. This is consistent with the bitemporal model, but the documentation should say so explicitly.

**L2: acceptably defined.**
- The code enforces `known_at <= evaluation_at`, and the documentation now states that `evaluation_at` is caller-trusted and unauthenticated.
- `valid_at` remains unbounded, so prospective valid-time queries are allowed. That appears intended.

**CX5: accepted on your report.** I accept that spaces and U+FF0F in the subject URI are rejected by the schema, relying on your statement that the required format checker is installed and on the tests shown. I have not verified the checker's behaviour myself.

## New limit found in this change (non-blocking)

**N1: `retainedObservationConflicts` is not scoped to the query.** It is built from every assertion in the input, and it is not filtered by:
- the query binding or its assignment,
- `known_at`, or
- `valid_at`.

This has two effects:
- **Temporal leak:** a historical view can report conflicts involving assertions recorded after `known_at`.
- **Disclosure:** any authorised reader can see issuer, `assignmentId` and assertion IDs for unrelated bindings.

The documentation does say "across the full input", and `inputDigest` already commits to the full input, so this is disclosed rather than hidden. It is still a limit. If you want the field to be a view as of the query, consider scoping it to the queried assignment and to `recordedAt <= known_at`, or renaming it so that it is clearly a whole-input diagnostic.

## Minor notes (no action required)

- The surrogate tests are named "latest", but the fix covers the whole assertion. One more case with the surrogate in a non-final event or in the binding would document that scope.
- `test_proposal_cannot_squat_assignment` asserts exactly one conflict. This relies on the base `self.rows` having no pre-existing observation conflicts.

## Limits that carry forward unchanged

All the limits you listed remain, as stated:
- Snapshot and CLI validation do not enforce reception history.
- Policy, clock, evidence and source kind are caller-trusted inputs.
- A global head allows one transition per second.
- There is no inverse subject index.
- The crosswalk is narrower/overlap only, not full conformance.
- Native V3 does not consume identity ranking, and the companion must be invoked separately.
- Existing-Dimension transactions are deferred.
- Pins check trusted local source bytes; they are not a sandbox.
- Loader exceptions fail closed but are not all normalised to `Invalid`.
- The schema must be protected after installation.
- Namespace and assertion-ID ownership remain external governance.
- The broad parent holds remain.

N1 is added to this list.
