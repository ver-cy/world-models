# Independent review request: EM-LEG-03 Internal policies and exceptions

Review this Enterprise boundary independently. Use public policy-governance and rule-model practice where useful. Distinguish source evidence from design inference. Do not invent a Vercy identifier.

Candidates:

- WM-KNW-012 Policy / Rule owns statement work/expression/manifestation identity, authority, applicability, rule slots, inheritance, precedence, exceptions, lifecycle and provenance.
- WM-ORG-019 Organization Policy owns nearly the same identity, approval, scope, clauses, precedence, exceptions, release and review semantics, but at lower precision.
- Both are published reviewable drafts with publication holds.

Proposed decision: **PROFILE** over WM-KNW-012, no new profile ID. Propose WM-ORG-019 retirement as a semantic duplicate after boundary review. Rehome its implementation/control mapping to the control model. Treat its acknowledgement/release residue as a separate **Acknowledgement / Policy Communication Event** candidate with identifier unassigned, because `(recipient, pinned expression, channel, instant)` has a lifecycle independent of the policy.

Proposed rules:

- Policy Version is a dated expression; Policy Exception is a bounded derogation.
- A local unit adopts a group policy through a local statement referencing the group work, adoption decision and mandate.
- Local tailoring may only tighten under an explicit precedence edge.
- Resolution at date t applies the global expression, local tightening and matching bounded exceptions, while preserving non-derogable superior floors.
- Unknown applicability and conflicts produce an unresolved result.
- Acknowledgement proves communication only, never compliance or control effectiveness.

Test:

1. An employee reads a policy; a system incorrectly marks a control satisfied.
2. Global policy + local tightening + team exception with expiry and compensating obligation.
3. Local rule attempts to weaken a non-derogable superior rule.
4. Group policy changes while a local adoption and exception remain active.

Return at most 1000 words with: Verdict; duplicate/retirement analysis; adoption/inheritance/exception rules; whether Acknowledgement needs an independent aggregate; required constraints; scenario results; publication blockers.
