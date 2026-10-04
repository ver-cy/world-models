# EM-LEG-03 local synthesis

## Disposition

- Create an **Enterprise internal-policy profile** over WM-KNW-012; no profile/runtime ID.
- Propose retirement of WM-ORG-019 as a semantic duplicate. Do not execute retirement while both bases remain reviewable drafts and the WM-KNW-012 boundary review is open.
- Raise **Acknowledgement / Policy Communication Event** as a new-model candidate with identifier unassigned.

## Boundary

WM-KNW-012 already owns policy work/expression/manifestation identity, authority and mandate, applicability, rule slots, inheritance, precedence, derogations, lifecycle, provenance and retention. WM-ORG-019 restates these at lower precision and has no distinct identity or lifecycle.

WM-ORG-019 implementation/control mapping belongs to the control model. Its release/acknowledgement residue is an event concerning a recipient, exact policy expression, channel and time; it must not live inside the policy aggregate.

Policy Version is a dated expression. Policy Exception is a registered bounded derogation. Policy Adoption is an adoption decision reference plus, for local scope, a local inheriting statement. None requires a new type here.

## Adoption, inheritance and exception

A local unit adopts a group policy through a local statement that references the group work, exact expression resolution policy, adoption decision and mandate. Local tailoring may only tighten under an explicit specificity/superiority edge. It never edits the group policy.

Resolution at an instant selects the applicable group expression, applies effective local tightening, then matching bounded derogations, while preserving a non-derogable superior floor. Unknown applicability and unresolved conflicts fail closed and produce an explicit report.

## Invariants

1. Every effective internal policy has a resolvable adopting authority, mandate, adoption decision and in-force instant.
2. Every exception has a separate granting authority, beneficiary/scope selector, bounded interval and compensating obligation or explicit reason for none.
3. Exception expiry changes the exception state, not the policy version.
4. Local policy may tighten but cannot silently weaken a superior rule.
5. Non-derogable rules cannot be relaxed by inheritance or exception.
6. Acknowledgement proves only communication of a pinned expression; it proves neither compliance nor control effectiveness.
7. Resolution returns one applicable rule set or an explicit unresolved result, never an enforcement decision.

## Acceptance result

At a selected date, the resolver chooses the pinned global expression, applies the local tightening and then a team-scoped temporary exception with compensating obligation. The exception cannot cross a superior non-derogable floor. After expiry, the local rule applies again without re-versioning the policy. Reading acknowledgement has no effect on the computed rule or control status.

## Holds

Both bases remain `publishableCanonical: false` and lack independent review. WM-KNW-012 entry-kind and relationship contracts are unsettled. Local scope-adoption semantics, delegation chains, multilingual acknowledgement and exception fixtures remain incomplete. Acknowledgement needs registry allocation and privacy/retention review. This checkpoint is not an installable release.
