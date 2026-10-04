## Verdict

**PROFILE.** EM-LEG-03 is a constrained profile of **WM-KNW-012 Policy / Rule**; it receives **no new registry ID**. Nothing in the contour requires an identity or lifecycle that WM-KNW-012's statement aggregate (work → dated expression → rule slot → manifestation, plus registered derogation) does not already root.

Two carve-outs, stated as decisions rather than deferrals:

1. **WM-ORG-019 Organization Policy is a duplicate in substance** of WM-KNW-012 across ten of its twelve layers, at strictly weaker structure. Direction: **retire / supersede into the profile**, not preserve in parallel.
2. **Acknowledgement is not a policy** and is not present in WM-KNW-012 at all. It has independent identity and lifecycle and therefore qualifies for its own registry allocation — as a separate request, not under EM-LEG-03, and not inside this profile.

## Boundary and duplicate analysis

Each WM-ORG-019 layer against WM-KNW-012: `policy-identity` → work/expression/manifestation identity (WM-ORG-019 lacks the FRBR split, so it is a lossy subset); `policy-approval` → issuing authority + mandate basis + adoption decision reference; `policy-scope`/`policy-applicability` → applicability scope + context conditions; `policy-clauses` → rule-slot inventory + deontic modality; `policy-precedence` → combining strategy, superiority edges, unresolved-conflict record; `policy-exceptions` → derogation declaration (WM-KNW-012 is materially stronger: beneficiary, scope selector, bounded interval, compensating obligation, derogation instrument artifact); `policy-review` → lifecycle states, amendment/supersession/repeal; `policy-mastership` → record classification and retention; `policy-mapping` → standard alignment with divergence notes. No duplicated layer contributes a distinct identity or lifecycle; all are the same statement record viewed twice.

Two WM-ORG-019 layers are **not** duplicates and must be re-homed rather than merged:

- `policy-implementation` (clause → procedure/control/role, assurance, failure mode) is **out of scope for EM-LEG-03 entirely**. WM-KNW-012 correctly disclaims control effectiveness and compliance handling. This belongs to the control model; carrying it here is the exact leak the contour's negative case warns about.
- `policy-release` (release + acknowledgement + `communicationLimits`) is the only genuinely non-duplicated content. Its identity is `(recipient, released expression/manifestation, channel, instant)` — a personal-data communication event with its own retention and erasure path, unrelated to the statement's version chain.

So WM-ORG-019 does not survive as a peer of WM-KNW-012. It survives only as the acknowledgement/release residue, which should be renamed and re-scoped or folded into a new acknowledgement entry. Because both records are `publishableCanonical: false` reviewable drafts, the retirement is a **registry proposal, not an executed supersession**.

Candidate-type test: **Policy** = WM-KNW-012 work (reuse). **PolicyVersion** = expression with version designator, last-modified instant, consolidated-expression artifact (reuse). **PolicyException** = registered derogation (reuse exactly; keep the rule that expiry is a dated event on the derogation, never on the statement). **Acknowledgement** = distinct, out of the profile. **PolicyAdoption** is two different things conflated: (a) the *enactment decision* — already a reference to a decision record owned elsewhere, no new type; (b) the *scope adoption* of a group work by a local unit — **currently unmodelled**. WM-KNW-012's `inheritFrom` and policy-set containment are statement-to-statement, never statement-to-org-scope. This is the profile's one real construction obligation.

## Adoption/inheritance/exception rules

- Adoption authority = the party holding a resolvable mandate basis; the adoption decision reference becomes required. Revocation = `repeal`, `replace` or `suspend` lifecycle transitions, each carrying an approval decision reference. Multi-step delegation is a declared WM-KNW-012 gap and must be recorded as an open question, not assumed.
- Group inheritance is expressed as a **local statement** with `inherit-from` → group work, a superiority edge with `override ground = specificity`, and a profile-mandated `tightening` direction plus a restrictiveness assertion. A local unit never edits the group work; revoking local adoption ends the local statement's efficacy and leaves the group chain untouched.
- Resolution at date *t*: (1) resolve the group expression via the named temporal dimension, capturing any gap/ambiguity report; (2) collect local statements inheriting from that work whose efficacy covers *t*; (3) apply declared precedence with recorded grounds; (4) apply derogations whose bounded validity interval covers *t* and whose beneficiary/scope selector matches; (5) check the non-derogable floor before emitting.

## Required profile

No new ID. Constraints on WM-KNW-012: instrument genre restricted to internal directive; `mandate basis reference` and `adoption decision reference` raised to required 1..n / 1; `review due` carried as a profile field that never terminates in-force or efficacy; derogation validity interval **must be bounded** (open-ended forbidden for internal exceptions) with compensating obligation present or an explicit "none" plus reason; `unresolved reference handling = fail-closed` for prohibition slots; a per-slot `non_derogable` flag sourced from the superior instrument reference; acknowledgement forbidden inside the statement record, reference-only to an external register; implementation/control mapping excluded by reference.

## Invariants

1. Every statement has a resolvable adopting authority, an adoption decision and an in-force instant.
2. Every derogation has a granting authority distinct from the beneficiary, an explicit scope and a bounded expiry.
3. A derogation's expiry is a dated event on the derogation record; it never versions the statement.
4. No derogation and no local statement may relax a slot flagged non-derogable by a superior instrument; such a combination emits an unresolved-conflict record and escalates.
5. A local statement inheriting from a group work may only tighten; a non-tightening local statement is invalid, not silently winning.
6. Acknowledgement contributes zero terms to any compliance or control-effectiveness query.
7. Unknown applicability is not permission.
8. Resolution at *t* returns exactly one rule set or an explicit unresolved report — never a decision, permit or deny.

## Scenario walkthrough

**Negative.** Recipient R acknowledges expression E on 2026-09-10. Query "is control C satisfied for R at 2026-10-01" must fail to resolve: the acknowledgement carries no modality, discharges no obligation, and cannot be joined to the control model. The only permissible inference is "R was informed of E, subject to `communicationLimits` (access, translation, unknowns)." A fixture must assert that this join fails.

**Acceptance.** Group work G, expression GE3 in force from 2026-06-01. Local statement LS1 (unit L) inherits from G, ground = specificity, direction = tightening, in force from 2026-08-01. Derogation X suspends slot s2 of LS1 for team T, 2026-09-01 → 2026-12-31, with a compensating obligation. At 2026-10-01 for a T member: resolve GE3; LS1 supersedes on specificity; X suspends LS1.s2, falling back to GE3.s2 — **not** below the statutory floor referenced as a dependency; had X gone below it, X does not apply and an unresolved conflict escalates. At 2027-01-01, X has expired and LS1 applies unchanged, with no re-versioning of LS1. Both dates yield one computable rule set.

## Gaps and publication holds

No canonical publication from this contour. Both source records are reviewable drafts under single-provider waivers with no independent review — WM-ORG-019 Codex-only (Claude and Grok waived), WM-KNW-012 Claude-only (Grok waived) — and both crosswalks are `conceptual-candidate` at index-and-publication-metadata depth only. Hold until a full semantic crosswalk is evidenced. WM-KNW-012's entry-kind reclassification (entity → aggregate) and `boundary-review-required` are unsettled, and the retirement of WM-ORG-019 depends on that boundary review. Open items: the scope-adoption construct has no source-grounded structure yet; delegation chains are a declared WM-KNW-012 gap and directly block "who may adopt and revoke"; the open-ended retention floor collides with acknowledgement erasure; multilingual authenticity is deferred and bears on acknowledging a translation; nested-member schemas, exception-profile tests and round-trip fixtures are unimplemented in both. The Acknowledgement registry allocation remains an unfiled request.
