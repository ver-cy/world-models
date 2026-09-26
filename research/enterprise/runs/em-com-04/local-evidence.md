# EM-COM-04 local evidence review

## Strong reuse baseline

The complete WM-ACT-021 contract already covers nearly all of EM-COM-04:

- `register-case` creates an attributable case with explicit unknowns.
- `link-or-merge-case` preserves predecessor identities and history.
- `record-case-communication` updates case chronology while the message system remains master.
- `resolve-close-or-cancel-case` keeps resolution, acceptance, closure and cancellation distinct.
- the boundary decision keeps incident, defect, problem and affected object identity outside the case.
- the root-cause/remedy finding references investigation, problem and corrective-action records.

This rules out `NEW MODEL` unless an independent reviewer finds a material contradiction.

## Narrow unresolved semantic

The requester assertion is required with cardinality `1`, but it may carry an explicit unknown. The contract does not distinguish:

- identity is presently unknown;
- requester intentionally withheld identity;
- the intake policy permits an anonymous case;
- the requester is pseudonymous but consistently addressable.

Those states have different consequences for contactability, disclosure, acceptance solicitation and later identity claims. A local intake policy could encode them, but the consequences cross several WM-ACT-021 functions. This is the strongest argument for a small application profile rather than a note.

## Relationship holds

- WM-ACT-021 now has candidate outgoing relation-ledger edges. They remain provisional until canonical registry approval.
- WM-KNW-014 `0.3.1-research.1` replaces the contradictory CHILD direction with an optional non-owning REFERENCE.
- WM-ACT-027 `0.3.1-research.1` makes the aggregate-level permission reference optional and retains a conditional requirement for outbound contact that needs permission or lawful-basis evidence.
- WM-ACT-007 is a suitable referenced execution authority for remedy work and must not be imported into case state.

## Final disposition after independent Grok review

`PROFILE`, no new aggregate and no runtime ID. Claude and Grok independently agree that the smallest useful profile adds only a governed requester-presence assertion and rules for how it affects party minting, registration, communication and acceptance. Merge, incident linkage, work execution and closure semantics are inherited from WM-ACT-021 by exact version/digest rather than restated.

The published artifact is a declarative Enterprise adoption binding. It defines portable requester-presence semantics while permitting local code mappings, pins provisional sibling relations without approving the shared relation ledger, and includes adversarial fixtures. The parent remains non-canonical, so the profile is explicitly reviewable research rather than an installable or canonical model.
