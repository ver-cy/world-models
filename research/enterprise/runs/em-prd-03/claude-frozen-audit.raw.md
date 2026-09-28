# Frozen Semantic Audit — EM-PRD-03 (WM-REC-006 Requirement aggregate)

**Verdict: REVISE**

## Critical findings

1. **Hidden aggregates despite `newRuntimeId=false`.** Two of the four "contained records" are not instance-contained. Requirement Baseline is declared population-level and scoped to the *repository/model boundary*, not to an owning Requirement instance (7), while also receiving family-plus-successor identity, independent authority, purpose, effectivity, digest, and readable predecessors (8) — exactly the identity semantics granted to Requirement itself (1). A record with its own immutable lineage and no owning instance is an aggregate root, not a contained record with a local scoped address. The preamble's containment claim and item 7's scope directly contradict each other.
2. **Requirement Conflict has no owner.** An equal-authority conflict (15) holds between two Requirement families. A pairwise record cannot have a single local scoped address. Ownership, addressing, and lifecycle are unspecified, making this a second latent aggregate.
3. **Local tolerance override atop a Rule pin is unblocked.** Item 6 permits revising "the criterion and Requirement without mutating the Rule," but does not forbid a Rule-pinned criterion carrying a local tolerance override. That silently shadows WM-KNW-013's evaluation contract (5) while still appearing Rule-governed.
4. **Intra-boundary trace duplication.** Outbound-only ownership (10) is undefined for Requirement→Requirement links inside WM-REC-006, where one association is outbound from the source and inbound at the target. Risk of mirrored records and divergent suspect state.
5. **Baseline digest may be read as sealing verdicts.** Nothing states that a sealed Baseline pins identities only. A frozen satisfaction status would become a stale pass, defeating 13.
6. **Redaction can imply completeness.** Intersection access (16) can render a partial Baseline or result set that reads as complete — false coverage proof.

Revision, satisfaction, failure, and waiver semantics are otherwise sound: append-only revisions, no overwrite on supersession (3), Done proves nothing (12), absence is never pass, failures persist (13), waivers never rewrite evidence (14).

## Required holds

- Resolve Baseline addressing: either extract as its own reserved boundary or demote to a derived, non-authoritative view. Do not publish either way.
- Assign Conflict ownership and addressing explicitly.
- Prohibit local tolerance overrides on Rule-pinned criteria; require re-pin or explicit, provenance-recorded conversion to a one-off informal condition.
- State that Baselines pin identities and digests only, never satisfaction verdicts; diffs are derived, not stored records.
- Define single-owner rule for intra-boundary trace; forbid mirrored inbound records.
- Mark redacted populations as incomplete without disclosing withheld content.
- Standing base holds carried unchanged: WM-KNW-013 parent signal, external-master joins, held bases.

## Scenario result

Semantically correct as narrated: R@rev1 stays unsatisfied/inconclusive (three Done tasks and a failed F cannot yield pass); B1 remains immutable; F stays visible against B1 and does not transfer to R@rev2; B2 requires fresh qualified result and evidence pinned to rev2. It is **not safely executable** under current wording, because B1, B2, and the diff artifact have no defined owner or address.

## Identifier decision

Uphold `newRuntimeId=false` for the Requirement aggregate on reserved WM-REC-006. Allocate nothing. Baseline and Conflict as specified cannot be addressed without either a reserved identity space or demotion; flag both for reservation review. Publication remains held.
