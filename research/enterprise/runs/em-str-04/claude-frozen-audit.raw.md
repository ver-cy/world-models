# Frozen No-Tools Semantic Audit — EM-STR-04

## Verdict
`ACCEPT WITH LIMITS`

## Critical findings
1. **D-1 is an unmastered label.** The scenario names D-1 separately from occurrence O-1 and record REC-1, but clause 7 defines Investment Decision as a *binding*, not an identity. With `newRuntimeId=false`, D-1 has no allocator. Left as-is, repeated reference to "D-1" will accrete into a de facto aggregate.
2. **Expected-benefit mastership is the nearest thing to a contradiction.** Clause 9 says "Initiative-contained appraisal content"; clause 4 says appraisal values are release-local. Read literally at Initiative level, clause 9 creates cross-release appraisal content that clause 4 forbids. The scenario aggravates this: A and B share one expected-benefit fact, which must be singly addressable for the no-summation rule to be enforceable.
3. **The pin set has no declared master.** Clause 5 enumerates criteria set, horizon, currency, price base, valuation basis, metric revisions, method, uncertainty, but does not state whether a criteria set reused by BC-1 and BC-2 is copied content or a shared object. Shared and unmastered, it is a hidden aggregate.
4. **Option identity allocation scope is unstated.** Clause 4 asserts stability across releases without naming the allocator; BC-1 becomes the practical master and BC-2 rebinds by label matching.
5. **Funding state kind is not frozen.** Clause 8 separates authorization, allocation, release and availability; freezing only a WM-ECO-012 revision loses which state was bound at decision time.
6. **Rejection is under-specified.** Clause 11 says "rejection records" without typing them, leaving rejection non-reproducible while approval is fully specified.
7. **Realized benefit has no in-profile master.** Clause 9 forbids a Benefit root, clause 10 defers it post-delivery; nothing forbids accretion onto a formalized Initiative.

## Required holds
- **H1** Decision addressing resolves to REC-1; O-1 is the temporal anchor. "D-1" is a narrative alias only.
- **H2** Expected benefit shared across alternatives must be a pinned WM-KNW-015 reference; contained form is permitted only when scoped to one alternative's release-local appraisal. Restate clause 9 as "release-local within the containing Initiative."
- **H3** Criteria/pin sets are release-local copies or pinned external revisions; no unmastered cross-release object.
- **H4** Option identity is allocated at Initiative scope and referenced by key; label-based rebinding prohibited.
- **H5** REC-1 records funding state kind alongside the pinned revision or snapshot.
- **H6** Rejection issues a WM-REC-010 record under the same join discipline as approval.
- **H7** Realized benefit is explicitly out-of-profile, mastered by the clause-2 delivery identity; post-formalization Initiative accretes no delivery facts.
- **H8** Supersession is a directed link; no decision may resolve through a supersession chain. WM-ACT-029 portfolio decisions may not be retro-mapped to Initiative mandates.

## Scenario result
Passes under H1–H8. Reproducing D-1 returns BC-1 and its frozen join deterministically; external facts are pinned, not remastered, and live-only pointers fail closed. BC-2 carries stable option identities without retro-binding. A and B remain mutually exclusive and unsummable only under H2. The rejected Initiative stays addressable and mints no Project. Ticket, approval and funding facts mint no delivery identity.

## Identifier decision
No new runtime or model identifier. `newRuntimeId=false` upheld. No Decision, Benefit or CriteriaSet root is granted; option identity remains a contained Initiative-scoped key. No publication authority conferred.
