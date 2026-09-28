## Verdict

**ACCEPT WITH LIMITS.** The decomposition is sound and no new identity kind is warranted, but two constraints are not yet adjudicable and fixture coverage is materially incomplete. Research-profile tier only.

## Critical findings

1. **Designation-preference conflict unretracted.** Constraint 4 (scheme-local preferred/admitted/deprecated selection) is correct, but WM-KNW-006 still asserts preferred-designation uniqueness per language as *concept-global*. The candidate never retracts it. Until it does, `scheme-local-preference` is indeterminate, not passing.
2. **"Declared significant properties" has no master.** Both migration fixtures pivot on this predicate, yet no constraint says who declares the property set, against which release it is pinned, or whether redeclaration is retroactive. Version-versus-instantiation is therefore undecidable at the boundary the profile most needs to decide.
3. **Authorship conflated with mastership.** The intrinsic/scope-note split is right, but a scheme-authored genus-differentia definition satisfies the survives-deletion test while originating in a release. Constraint 5 must state that provenance never confers mastership and that such definitions migrate to concept ownership on publication.
4. **Dual-role text unstated.** A definition republished as a glossary page is one concept-owned value *and* one record of those bytes. Both studies note it; no constraint or fixture encodes it, leaving a plausible route to re-mastering definitions as records.
5. **Alternate identifiers and signature binding dropped.** Local evidence requires the target system key to be a qualified alias with assertion provenance, and signatures to stay bound to original bytes rather than migrate. Neither survives into the constraint set.
6. **Fixture gaps.** Missing: release attempting to overwrite an intrinsic definition (negative); re-entry into a later release after withdrawal; renumbering or silent repointing of a published version sequence or release (constraint 14 untested); digest *mismatch* raising an integrity event (only the equality limb is tested); merge, split, redirect and tombstone resolvability; disputed definition triggering deprecation or redirect (negative); access-scoped licensed definition; Knowledge Article genre resolved through a pinned vocabulary release.

## Required holds

All seven candidate holds stand and remain sufficient to block canonical publication: non-canonical bases; reciprocal 006/018 scope amendments removing dual mastership; scheme-less bound-release cardinality; WM-KNW-002/018 parentage and the reversed WM-XCT-020 relationship; unratified definition access and dispute semantics and classification-release pins; unpinned standard editions and clause crosswalks; EM-KNW-02 delegation. Add: **(8)** retract concept-global preferred-designation uniqueness in WM-KNW-006; **(9)** pin the significant-properties declaration to an owner and release; **(10)** state provenance-is-not-mastership for definitions; **(11)** close the fixture gaps above before any conformance claim.

## Scenario result

Eleven positive and four negative cases are adjudicable under the stated constraints and resolve as expected, with three exceptions. `format-migration-preserved` and `transformative-migration` are **indeterminate** pending finding 2 — the constraints distinguish the outcomes but not the trigger. `scheme-local-preference` is **indeterminate** pending finding 1. `identifier-reuse`, `dual-editable-master`, `label-only-classification` and `digest-equals-identity` reject cleanly on the stated text. `scheme-less-concept` passes only if hold 3 lands; as frozen, the base cardinality contradicts the fixture. No fixture exercises append-only violation, integrity mismatch, or merge/split, so the append-only and lifecycle constraints are asserted but unverified.

## Identifier decisions

PROFILE over WM-REC-001, WM-KNW-006 and WM-KNW-018. No new catalogue or runtime identifier allocated, requested or implied. WM-XCT-020 remains referenced, not re-mastered, and its reversed-parent hold is inherited. Knowledge Article, Document Revision and Term Definition correctly receive no identity. Assertion and decision identity stays delegated to EM-KNW-02. No registry reservation is mutated; `candidateRevision: 2` remains research-tier. Identifier allocation and registry mutation remain holds, unexercised here.
