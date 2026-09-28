**Verdict.** PROFILE over WM-KNW-012. No new profile ID. Policy Version, Policy Adoption and Policy Exception stay inside 012 as dated expression, adoption statement and bounded derogation. WM-ORG-019 is a lower-precision restatement of the same statement core and should be retired only after residue is rehomed. Until then mark it deprecated-pending-rehome, not deleted. Do not invent a Vercy identifier. This is standards alignment, not legal advice.

**Duplicate / retirement analysis.** Source evidence: both models are published reviewable drafts with holds. 012 is an aggregate that already owns work / expression / manifestation identity, authority, applicability, rule slots, acyclic inheritance and precedence, derogations, lifecycle and provenance, and explicitly delegates runtime evaluation and enforcement. 019 is an entity framed as a “descriptive record, not an executable or universally mandatory rule,” covering identity, approval, scope, clauses, precedence, exceptions, release and review at lower precision.

The statement core is a semantic duplicate. 019 unique residue is not:
1. Release / acknowledgement / training evidence.
2. Procedure / control / role implementation mapping.
3. Org-purpose and risk-motivation framing (keep as PROFILE metadata on 012, not a second model).

Conditional retirement requires all of: field-level 019→012 crosswalk; control-mapping fields pointed at the existing control family named by EM-RSK-01 (012 keeps typed control-refs only); acknowledgement parked as an unassigned event candidate; 019 identifier retained as an alias, not a live owner; both drafts’ publication holds left visible. WM-XCT-027 is a mixin that cites effectiveness; it is not the control register. WM-KNW-013 treats policies, controls, exceptions and enforcement as external masters and must not absorb PolicyException.

**Adoption / inheritance / exception rules.** Design inference from 012’s work/expression and inheritance graph, labelled as such.

- A Policy Version is a dated, immutable expression of a work. New content is a new expression. A consolidated text is a derived projection.
- A local unit adopts a group policy through a local 012 statement that references the group work, the adoption decision and the mandate. Default: the adoption floats to the current in-force expression unless an expression is pinned. Revoking adoption does not delete the group work.
- Inheritance is an explicit acyclic edge. Containment is not a silent copy of clause text.
- Local tailoring is a separate local expression with a precedence edge of type tighten-only against named superior rule slots. Weakening a non-derogable superior floor is refused or unresolved; it is not stored as a successful override.
- A Policy Exception is a bounded derogation child of 012, not a new work. Required: target slot or expression-id, subject/scope, authority, effective interval with mandatory expiry, compensating-obligation reference, state. An exception with no expiry is invalid. It does not edit approved expression text. After expiry or revocation the superior and local tightening resume without a further act.
- Resolution at date *t* applies the in-force global expression, still-effective local adoption, tighten-only local expressions, and matching in-force exceptions, while preserving non-derogable superior floors. Unknown applicability or conflict yields unresolved — not a silent permit or deny. Point-in-time reconstruction remains possible because expressions are immutable. XACML combining algorithms and OPA package composition are alignments for conflict handling, not owners of the internal-policy record.

**Does Acknowledgement need an independent aggregate?** Yes as an event kind; no new catalogue ID in this review. Grain is `(recipient, pinned expression, channel, instant)` and that lifecycle is independent of the policy work. It must not be an attribute on the expression (that mix invites “read ⇒ executed”). First test a PROFILE of existing WM-ACT-027 plus a pinned 012 expression-id. WM-ACT-040 may cite such events during onboarding; it does not own the policy. If 027 cannot carry communication-only meaning with no control side-effect, leave **Acknowledgement / Policy Communication Event** unassigned. That is a hold, not an invented identifier.

ISO 37301 and COSO alignment, not a legal conclusion: communication / awareness evidence is distinct from control operation and from performance evaluation. Acknowledgement proves notice or receipt only. It never writes control-satisfied, risk-closed or exception-granted.

**Required constraints.**
- No new profile ID and no invented acknowledgement or control ID.
- 012 never stores per-recipient receipt or control-effectiveness state.
- No write path from acknowledgement to ControlExecution or risk closure.
- Tighten-only local tailoring unless the superior slot is explicitly derogable and a valid exception exists.
- Exception expiry mandatory; compensating obligation referenced, not stored as effectiveness.
- Unknown or conflict → unresolved.
- Group expression change never mutates prior expressions, adoptions or exception history.
- Enforcement-check results stay with the control model. The card already states this.

**Scenario results.**

1. *Employee reads a policy; a system marks a control satisfied.* Record one communication event pinned to that expression. Control remains unsatisfied. Marking ControlExecution or effectiveness “pass” from the read fails the card negative case and the EM-RSK-01 rule that presence of a control does not prove effectiveness.

2. *Global policy + local tightening + team exception with expiry and compensating obligation.* Inside the window: resolved set is global expression plus local tightening, minus the scoped derogation, with the compensating obligation still due. After expiry the exception drops; tightening and the global floor remain. If applicability is unknown, result is unresolved.

3. *Local rule attempts to weaken a non-derogable superior.* Conflict recorded. Result is rejected or unresolved. The local text may exist as a proposed expression; it does not become in-force against the floor.

4. *Group policy changes while local adoption and exception remain active.* New group expression does not overwrite the prior one. Floating adoption now resolves against the new in-force expression; local tightening must be re-validated, not auto-rewritten. An exception pinned to the old expression does not automatically apply to the new one: still-valid, expired, must-reauthorize, or unresolved. Historical query at *t_old* still uses the old expression and the then-active exception.

**Publication blockers.**
- Field-level 019→012 crosswalk and source mastership still open in brief.json.
- 019 retirement is blocked until control-mapping and acknowledgement residues have explicit owners.
- Floating versus pinned adoption default is not yet a written PROFILE constraint.
- Tighten-versus-weaken and exception-reauthorization-on-group-change have no fixtures.
- 012 single-provider hold and 019 Codex-only hold remain; ISO 37301 on 012 is paywalled/unverified.
- Acknowledgement host (027 PROFILE versus unassigned candidate) is unresolved.
- WM-XCT-027 must not be treated as the control register.
- Alignments to ISO 37301, COSO, XACML and OPA are alignments only, not conformance claims.
