## Verdict

**Conditional — not publishable as a normative decision.** The spine is sound: profiling Task onto WM-ACT-006 rather than minting a WorkItem identifier, making WM-XCT-021 the sole current transition authority, demoting WM-ACT-003 to deferred, and separating native status / canonical state / outcome evidence are all defensible and internally consistent. The failure is under-specification, not error: several load-bearing terms are used as if defined when they are not, and three required areas (deletion/retention, access control, round-trip) are absent entirely. Publishable as a **draft, non-normative decision record** with the defect list attached; not as settled semantics.

Labels below are audit-local, not model identifiers.

## Blocking defects

**D1 — Identity arbitration unstated.** "Reuse WM-ACT-006 identity" and "tracker-native identity is source namespace + native item ID" are two identity claims with no stated relation. Which is the identity of record, and what is the uniqueness constraint?

**D2 — Native identity is not stable.** Human-readable tracker keys mutate on project move and are reused after delete/recreate. Namespace + native item ID is a natural key only if the native ID is the tracker's immutable internal ID. As written, a project move silently forks or merges identity — and it also mutates the referenced-master relationship (D9).

**D3 — Alias role vocabulary is ungoverned and non-temporal.** originating/master/mirror gets narrative treatment while WorkItemType gets scheme/version/code. No cardinality rule (may two aliases assert master?), no validity interval (mastership moves over time), no uniqueness scope.

**D4 — Transition-event identity undefined — and idempotence is at risk from crosswalk pinning.** If the key includes canonical from/to states, re-pinning the crosswalk changes the key and re-import duplicates history. Transition identity must be expressed in source-native terms only, preferring a source-supplied changelog event ID.

**D5 — Ordering is unspecified under coarse or tied timestamps.** Append-only does not imply ordered. Second-granular sources and same-instant ties need a source-supplied ordinal; occurrence time and observation time are not distinguished anywhere.

**D6 — Lifecycle-version selection for historical transitions.** Pinning "the" lifecycle definition version at migration time mis-maps transitions that occurred under an earlier version. Either map by occurrence-time-valid version or mark the mapping as retrospective.

**D7 — Outcome retraction and evidence semantics missing.** Reopen-after-accepted, mutual exclusivity of cancelled/rejected, and who asserted an outcome on what basis are all undefined. Absence of evidence must not be readable as a negative outcome; the model currently permits a closed-world reading.

**D8 — Crosswalk succession is pinning, not succession.** No rule distinguishes a compatible refinement from a breaking remap, no requirement that stored mapped values carry the producing crosswalk version, and no prohibition on silent re-derivation. Unmapped loss is recorded but must be first-class and queryable, never defaulted to a canonical state.

**D9 — Backlog/Iteration demotion is self-undermining.** Backlog rank is per-(context, item), not derivable from Task — an irreducible mastered fact by the decision's own test. Iteration carries timebox dates, commitment-at-start, and time-varying membership; as a "correlation alias" there is nowhere for historical sprint membership to live. Either state explicitly that rank and membership are mastered on the correlation without independent identity, or the demotion fails its own criterion. Separately, "Plan" is used as a referent with no binding — three unbound terms (Backlog, Iteration, Plan) now circulate; they need a lexical register so they are not later mistaken for concepts.

**D10 — Deletion/retention absent.** No tombstone semantics, no rule that omission from an export is not deletion, no reconciliation of append-only history with erasure obligations over actor references, no retention class for loss records.

**D11 — Access control absent.** Every import is a partial observation under a credential scope. Without recording that scope, a missing field is indistinguishable from an empty one, and canonical state derived from a restricted view is silently wrong. Mirror aliases must inherit the originating source's policy.

**D12 — Round-trip undefined.** "Never overwrite equal-authority conflicts" leaves the conflict unresolved *and* unsurfaced. No write-provenance tagging, so re-importing our own write-back counts as a fresh source assertion (echo loop).

**D13 — Estimate unit is an ungoverned vocabulary.** Points/hours/t-shirt revisions are incomparable across a unit change; asserter and estimate-of-what (original vs remaining) are unstated. "Actual effort separately mastered" names no master and no grain.

## Remediation

Per defect, minimally: D1 declare WM-ACT-006 identity canonical and native identity a natural key resolving to it; D2 require an immutable native ID, demote keys to historical aliases; D3 govern the role vocabulary by scheme/version/code with at-most-one-master-per-interval; D4 key transitions on source-native terms, source event ID preferred; D5 add occurrence/observation bitemporality plus source ordinal; D6 select lifecycle version by occurrence time; D7 outcomes become append-only assertions with asserter, time, evidence reference and explicit supersession, open-world; D8 stamp mapped values with producing crosswalk version, add a compatible/breaking succession declaration, forbid in-place re-derivation; D9 state the rank/membership mastership exception explicitly and register the three unbound terms as non-normative; D10 add observed-deletion tombstones and actor-redaction-preserving-event-identity; D11 record observing scope on every assertion, forbid absent⇒empty; D12 declare round-trip out of scope *or* add write-provenance and surfaced conflict records; D13 govern the estimate unit vocabulary and name the actual-effort master.

## Required fixtures

Re-run same export twice (zero churn); crosswalk version bump (event identity stable, mapping re-derived not overwritten); two transitions in one second; project move/key change; two sources both claiming master; native Closed with no acceptance evidence; reopen after accepted; unmapped native status; restricted field absent vs empty; item omitted from export vs observed deletion; item ranked in two backlogs; Kanban source with no iteration (full state and outcomes derivable); estimate unit change across revisions; write-back then re-import (echo); historical transition predating the pinned lifecycle version.

## Publication disposition

Withholding the canonical-completeness and publication claim is correct — keep it withheld. Publish at run scope EM-WRK-01 as a draft decision record carrying D1–D13 as open defects. Promotion to normative requires D1–D6 and D10–D12 closed and the corresponding fixtures green; D9 is a gate on the Backlog/Iteration section specifically and blocks that section alone.
