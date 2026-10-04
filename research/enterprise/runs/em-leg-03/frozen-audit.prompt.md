# Frozen semantic audit request — EM-LEG-03

You are the single independent frozen semantic auditor. Use only this prompt. Do not browse, use tools, execute code, invent identifiers, or authorize publication. Audit the reconciled candidate for identity/lifecycle integrity, duplicate retirement safety, policy resolution correctness, acknowledgement/control separation, registry discipline, fixtures and publication holds. Return PASS or REVISE, then findings, required deterministic remediation, identifier discipline, and publication decision. This audit runs exactly once.

## Reconciled profile candidate

```
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-LEG-03",
  "name": "Enterprise Internal Policy",
  "candidateRevision": 2,
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": [
    "WM-KNW-012"
  ],
  "duplicateRetirementProposal": {
    "modelId": "WM-ORG-019",
    "state": "deprecated-pending-rehome",
    "aliasPreserved": true,
    "preconditions": [
      "field-level WM-ORG-019 to WM-KNW-012 crosswalk is ratified",
      "control and implementation mappings have an explicit external owner",
      "policy communication and acknowledgement residue has an explicit owner",
      "both parent publication holds remain visible"
    ]
  },
  "ownedSemantics": {
    "policyVersion": "immutable dated expression of one policy work; consolidated text is a derived projection",
    "policyAdoption": "local statement referencing group work, adoption decision, mandate and an explicit floating-or-pinned expression policy",
    "policyException": "bounded derogation child targeting a rule slot or expression, never a second policy work"
  },
  "constraints": [
    "Every effective policy resolves adopting authority, mandate, adoption decision and in-force instant.",
    "Every adoption explicitly declares whether it floats to the current in-force expression or pins an exact expression.",
    "A group expression change never mutates prior expressions, adoptions, exceptions or their history.",
    "Floating adoption resolves to the new in-force expression while local tailoring is revalidated rather than rewritten.",
    "An exception pinned to an earlier expression does not automatically apply to a successor expression and requires an explicit validity or reauthorization result.",
    "Inheritance is an explicit acyclic edge and never silently copies clause text.",
    "Local tailoring is a separate local expression and may tighten only under an explicit precedence edge.",
    "A local weakening of a non-derogable superior floor is rejected or unresolved and never becomes an effective override.",
    "Every exception identifies target slot or expression, scope, authority, effective interval, mandatory expiry, state and compensating-obligation reference.",
    "Exception expiry or revocation restores the superior and local tightening without changing policy expressions.",
    "Unknown applicability and unresolved conflicts produce an explicit unresolved result.",
    "WM-KNW-012 never stores per-recipient receipt, control-execution or control-effectiveness state.",
    "Acknowledgement pins the exact expression and proves communication only, never comprehension, consent, compliance, risk closure or control effectiveness.",
    "There is no write path from acknowledgement to a control execution, effectiveness or exception decision.",
    "Control mappings are typed references to an external control authority; WM-XCT-027 is not treated as a control register.",
    "Retirement of WM-ORG-019 preserves its identifier as an alias and does not hide either source model's publication holds."
  ],
  "holds": [
    "Both parent models remain non-canonical reviewable drafts.",
    "Field-level duplicate crosswalk and source mastership are not ratified.",
    "The explicit control-register owner is unresolved.",
    "Policy Communication Event remains identifier-unassigned pending a reuse test against WM-ACT-027.",
    "Floating and pinned adoption, exception reauthorization and tighten-versus-weaken fixtures are not canonical.",
    "Privacy, retention, multilingual and delegated-recipient semantics require validation.",
    "No package conversion or live publication is authorized."
  ]
}

```

## Identifier-unassigned communication candidate

```
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-LEG-03",
  "proposedName": "Policy Communication Event",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned-pending-reuse-test",
  "decision": "NEW MODEL",
  "canonicalPublishable": false,
  "identityTest": {
    "stableIdentity": "A communication occurrence is identified independently from the policy and recipient by its pinned expression, intended recipient, channel, occurrence time and source authority; retries and acknowledgements remain linked events rather than policy mutations.",
    "versionIdentity": "An event is immutable after recording; corrections append a superseding record, while delivery attempts and acknowledgements retain their own timestamps and evidence.",
    "independentLifecycle": [
      "planned",
      "dispatched",
      "delivered",
      "failed",
      "acknowledged",
      "superseded",
      "retained",
      "disposed"
    ],
    "mastership": "policy communication and acknowledgement record authority",
    "reuseTest": "First test whether WM-ACT-027 can host a communication-only event pinned to WM-KNW-012 without control or permission side effects. Allocate only if that test fails and registry authority approves."
  },
  "boundary": {
    "owns": [
      "policy communication occurrence identity",
      "exact policy-expression reference and digest communicated",
      "intended recipient reference and recipient kind",
      "channel, dispatch and delivery timestamps",
      "delivery outcome and retry lineage",
      "acknowledgement act, timestamp and evidence reference",
      "privacy, retention and disposal classification"
    ],
    "references": [
      {
        "target": "WM-KNW-012",
        "purpose": "Policy work and exact expression communicated"
      },
      {
        "target": "WM-PER-001",
        "purpose": "Person recipient identity"
      },
      {
        "target": "WM-ORG-001",
        "purpose": "Organization recipient identity"
      },
      {
        "target": "WM-ORG-002",
        "purpose": "Organizational-unit recipient or applicability scope"
      }
    ],
    "excludes": [
      "policy identity, versioning, authority or applicability",
      "policy adoption, exception or precedence resolution",
      "recipient identity or contact-endpoint normalization",
      "compliance, understanding, consent or control-effectiveness determination",
      "access authorization or enforcement decisions"
    ]
  },
  "objects": {
    "PolicyCommunicationEvent": {
      "identity": [
        "communicationEventId"
      ],
      "required": [
        "policyExpressionRef",
        "expressionDigest",
        "recipientRef",
        "recipientKind",
        "channel",
        "occurredAt",
        "authorityRef",
        "status"
      ],
      "optional": [
        "supersedesEventRef",
        "retentionClassRef"
      ],
      "lifecycle": [
        "planned",
        "dispatched",
        "delivered",
        "failed",
        "superseded"
      ]
    },
    "DeliveryAttempt": {
      "identity": [
        "deliveryAttemptId"
      ],
      "required": [
        "communicationEventRef",
        "attemptedAt",
        "channel",
        "outcome"
      ],
      "optional": [
        "endpointRef",
        "providerEvidenceRef",
        "failureReason"
      ]
    },
    "AcknowledgementAct": {
      "identity": [
        "acknowledgementId"
      ],
      "required": [
        "communicationEventRef",
        "actorRef",
        "acknowledgedAt",
        "acknowledgementKind",
        "evidenceRef"
      ],
      "optional": [
        "locale",
        "deviceOrSessionRef",
        "supersedesAcknowledgementRef"
      ]
    }
  },
  "invariants": [
    "Every event pins one exact policy expression and immutable digest.",
    "A mutable URL, latest alias or policy-work reference alone cannot prove what was communicated.",
    "Recipient identity and recipient kind are explicit and never inferred from a delivery endpoint.",
    "Delivery, opening, reading and acknowledgement are distinct outcomes.",
    "Acknowledgement proves only the recorded act concerning the pinned expression.",
    "Acknowledgement never proves comprehension, consent, compliance or control effectiveness.",
    "A retry creates a new delivery attempt and never overwrites a failed attempt.",
    "A corrected communication record supersedes rather than mutates the prior event.",
    "Policy revision or exception expiry never rewrites prior communication history.",
    "Organization or unit recipients do not imply that every member received or acknowledged the policy.",
    "Retention and disposal are explicit and preserve required audit evidence without indefinite personal-data retention.",
    "Unknown delivery or acknowledgement status remains unknown and is never promoted to success."
  ],
  "holds": [
    "Independent Grok review completed; it requires a WM-ACT-027 reuse test before allocation.",
    "Registry identifier allocation remains pending and no identifier may be guessed.",
    "WM-KNW-012 remains non-canonical and its boundary review is open.",
    "Privacy, retention, multilingual and delegated-recipient semantics require validation.",
    "No write path to control execution, risk closure or policy resolution may exist.",
    "One frozen semantic audit is pending after provider reconciliation.",
    "Package conversion and live verification are pending."
  ],
  "candidateRevision": 2
}

```

## Fixtures

```
{
  "format": "vercy-enterprise-profile-fixtures/v1",
  "contourId": "EM-LEG-03",
  "candidateRevision": 2,
  "cases": [
    {
      "id": "acknowledgement-not-control",
      "kind": "negative",
      "input": "An employee acknowledges one pinned policy expression and a system marks its mapped control effective.",
      "expect": "Communication evidence is recorded; the control write is rejected."
    },
    {
      "id": "bounded-team-exception",
      "kind": "positive",
      "input": "A global expression, local tightening and team exception with expiry and compensating obligation are effective at t.",
      "expect": "Resolution applies the global floor, tightening and only the matching bounded derogation; compensation remains due."
    },
    {
      "id": "expired-exception",
      "kind": "positive",
      "input": "The same exception is queried after expiry.",
      "expect": "The exception is absent and the superior plus local tightening resume without policy re-versioning."
    },
    {
      "id": "weaken-nonderogable-floor",
      "kind": "negative",
      "input": "A local expression weakens a named non-derogable superior rule slot.",
      "expect": "The weakening is rejected or unresolved and never enters the effective rule set."
    },
    {
      "id": "floating-adoption-successor",
      "kind": "positive",
      "input": "A floating local adoption remains active when a new group expression becomes in force.",
      "expect": "The adoption resolves to the successor expression; local tailoring is revalidated and history remains immutable."
    },
    {
      "id": "pinned-adoption-successor",
      "kind": "positive",
      "input": "A pinned local adoption remains active when a new group expression becomes in force.",
      "expect": "The adoption continues to resolve its exact pinned expression until an explicit adoption change."
    },
    {
      "id": "old-expression-exception",
      "kind": "negative",
      "input": "An exception pinned to the old group expression is silently carried to the successor expression.",
      "expect": "Automatic carry-forward is rejected; an explicit validity or reauthorization result is required."
    },
    {
      "id": "unknown-applicability",
      "kind": "negative",
      "input": "The recipient or territorial applicability cannot be resolved.",
      "expect": "The resolver returns unresolved and does not silently permit or deny."
    },
    {
      "id": "missing-exception-expiry",
      "kind": "negative",
      "input": "An exception has authority and scope but no expiry.",
      "expect": "The exception is invalid and cannot affect resolution."
    },
    {
      "id": "silent-clause-copy",
      "kind": "negative",
      "input": "A local policy copies superior clause text without an explicit inheritance edge or source locator.",
      "expect": "The copied text cannot establish inheritance or precedence."
    },
    {
      "id": "org019-retirement-before-rehome",
      "kind": "negative",
      "input": "WM-ORG-019 is retired before control mapping and communication residue receive owners.",
      "expect": "Retirement is blocked and the identifier remains a deprecated-pending-rehome alias."
    },
    {
      "id": "wm-act-027-reuse",
      "kind": "review",
      "input": "WM-ACT-027 is proposed as the acknowledgement host.",
      "expect": "Accept only if it represents communication-only events with a pinned expression and no control or permission side effects; otherwise keep the candidate unassigned."
    }
  ]
}

```

## Provider comparison

```
# EM-LEG-03 provider comparison

Claude and Grok independently select **PROFILE** over WM-KNW-012 with no profile or runtime identifier. Both identify WM-ORG-019 as a lower-precision duplicate whose retirement is conditional on a field-level crosswalk and rehoming of control-mapping and communication residue.

Both preserve Policy Version as an immutable dated expression, Policy Adoption as a local statement citing authority, decision and mandate, and Policy Exception as a bounded derogation. Local tailoring is tighten-only unless an explicitly derogable superior slot and valid exception permit otherwise. Unknown applicability or unresolved conflict yields an explicit unresolved result.

Both separate acknowledgement from policy identity and from compliance or control effectiveness. Claude supports an independently allocated communication-event candidate. Grok agrees on independent event grain but requires a reuse test against WM-ACT-027 before allocation. The reconciled result therefore keeps **Policy Communication Event** identifier-unassigned and adds the reuse test as a publication hold; WM-XCT-027 is never treated as the control register.

Grok adds floating-versus-pinned adoption semantics, mandatory revalidation of local tightening after a group-policy change, exception reauthorization rules, alias preservation for retired WM-ORG-019, and explicit separation of control execution from communication evidence.

```

## Claude boundary study

```
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

```

## Grok boundary study

```
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

```

## Frozen dossier

```
{
  "contour": {
    "id": "EM-LEG-03",
    "name": "Внутренние политики и исключения",
    "domain": "LEG",
    "kind": "subject",
    "wave": "W1",
    "scope": "Внутренние правила, принятие, применимость, исключения и ознакомление. Результат проверки исполнения принадлежит модели контроля.",
    "candidate_types": [
      "Policy",
      "PolicyVersion",
      "PolicyAdoption",
      "PolicyException",
      "Acknowledgement"
    ],
    "specific_questions": [
      "Кто может принять и отменить правило?",
      "Как наследовать правило в группе с локальным исключением?",
      "Как отличить ознакомление от выполнения?"
    ],
    "proposed_invariants": [
      "Правило имеет орган принятия и срок",
      "Исключение имеет область и истечение",
      "Ознакомление не доказательство исполнения"
    ],
    "negative_case": "Прочитанный сотрудником документ означает выполненный контроль.",
    "acceptance_scenario": "Глобальная политика, локальное ужесточение и ограниченное исключение дают однозначное правило на заданную дату.",
    "comparison_tracks": [
      "OASIS UBL/FIBO: соглашения, стороны и обязательства",
      "ODRL: разрешение, запрет, обязанность и ограничение",
      "Первичные юридические источники выбранных юрисдикций; обязательна предметная проверка применимости"
    ],
    "vercy_candidates": [
      {
        "model_id": "WM-ORG-019",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "index-and-publication-metadata",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      },
      {
        "model_id": "WM-KNW-012",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "index-and-publication-metadata",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      }
    ],
    "candidate_properties_from_v1": [
      {
        "predecessor": "LEG-04",
        "fields": [
          {
            "name": "policy_text",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "scope",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "effective_period",
            "value_type": "interval",
            "status": "candidate-not-normative"
          },
          {
            "name": "review_due",
            "value_type": "date",
            "status": "candidate-not-normative"
          }
        ]
      }
    ],
    "suggested_owner": "Юридическая функция / владелец договора",
    "candidate_master_systems": "CLM, подписанные документы, нормативные источники",
    "related_research_contours": [
      "EM-LEG-02"
    ],
    "blocking_decisions": [
      "Установить границу и решение reuse/extend/new по действующим спецификациям.",
      "Подтвердить semantic crosswalk, права и source mastership.",
      "Выбрать immutable refs; провести проверки fixtures до заявления о публикационной готовности."
    ]
  },
  "registry_policy": {
    "reserved_candidates": [
      "WM-ORG-019",
      "WM-KNW-012"
    ],
    "rule": "No new ID without independent identity/lifecycle and registry allocation."
  },
  "models": {
    "organization_policy": {
      "publication": {
        "status": "published",
        "adjudicationStatus": "reviewable-draft",
        "publishableCanonical": false,
        "generatedAt": "2026-09-09T22:25:41Z",
        "synthesisSha256": "67adf1aaa240a246e0c79d57d6a1b691eb2e1e65bdde2e1347d9cb696ea27823",
        "providerMode": "single-provider-waiver",
        "providers": [
          "Codex"
        ],
        "waivedProviders": [
          "Claude",
          "Grok"
        ]
      },
      "model": {
        "registry_id": "vr.wm-org-019",
        "model_id": "WM-ORG-019",
        "name": "Organization Policy",
        "entry_kind": "entity",
        "purpose": "Describe an organizational normative policy through scope, approved versions and lifecycle evidence.",
        "scope_statement": "Identifiable normative information object with approved versions and explicitly distinguished drafts, statements, interpretations and implementation references.",
        "in_scope": [
          "Policy identity, authority, approval, purpose and applicability",
          "Clauses, conflicts, exception records and procedure mappings",
          "Release, review, supersession and controlled provenance"
        ],
        "out_of_scope": [
          "Enacting law or determining legal enforceability",
          "Executing permissions, discipline, sanctions or controls",
          "Automatic lossless prose compilation to a policy engine"
        ],
        "boundary_notes": [
          {
            "neighbor": "Mandate / Charter",
            "distinction": "Authority instrument is referenced; parent_ids is not proof that every policy is a charter subtype.",
            "source_refs": [
              "SRC-002",
              "SRC-005"
            ]
          },
          {
            "neighbor": "Procedure and implementation",
            "distinction": "Prescriptive policy and implementing procedure or observed compliance are separate.",
            "source_refs": [
              "SRC-002",
              "SRC-004"
            ]
          },
          {
            "neighbor": "Law and external regulation",
            "distinction": "Policy may reference legal constraints but is not a legal opinion or statutory instrument.",
            "source_refs": [
              "SRC-002",
              "SRC-005"
            ]
          },
          {
            "neighbor": "Machine access policy",
            "distinction": "Only selected statements may map to a named profile; no general engine or automatic grant.",
            "source_refs": [
              "SRC-001",
              "SRC-003"
            ]
          }
        ]
      },
      "selected_findings": [
        {
          "bundle": {
            "id": "policy-policy-identity-and-authority",
            "name": "Policy identity and authority",
            "description": "Organization-policy policy identity and authority."
          },
          "layer": {
            "id": "policy-identity",
            "name": "Identity and normative standing",
            "description": "Authored policy-context design for identity and normative standing, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule."
          },
          "finding": {
            "id": "policy-identity-record",
            "name": "Identity and normative standing record",
            "description": "Authored policy-context design for identity and normative standing, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule.",
            "source_refs": [
              "SRC-001",
              "SRC-005",
              "SRC-006"
            ],
            "questions": [
              {
                "id": "policy-identity-q01",
                "text": "Which master-qualified policy identifier persists across versions and translations?",
                "kind": "identity",
                "answer_data": [
                  "policy-identity-identity"
                ]
              },
              {
                "id": "policy-identity-q02",
                "text": "What makes this an organizational policy rather than guidance, a procedure, law or control implementation?",
                "kind": "classification",
                "answer_data": [
                  "policy-identity-standing"
                ]
              },
              {
                "id": "policy-identity-q03",
                "text": "Which organization and policy family own its normative scope?",
                "kind": "ownership",
                "answer_data": [
                  "policy-identity-owner"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "policy-identity-identity",
                "name": "identity",
                "description": "Proposed answer members: master,id,aliases. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-005",
                  "SRC-006"
                ]
              },
              {
                "id": "policy-identity-standing",
                "name": "standing",
                "description": "Proposed answer members: kind,recognitionEvidence,limits. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-005",
                  "SRC-006"
                ]
              },
              {
                "id": "policy-identity-owner",
                "name": "owner",
                "description": "Proposed answer members: organizationRef,family,namespace. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-005",
                  "SRC-006"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "policy-identity-evidence",
                "name": "Identity and normative standing evidence",
                "description": "Versioned policy assertion and minimum authorized evidence references; restricted text and personal acknowledgements remain in protected masters.",
                "media_or_form": [
                  "text/markdown",
                  "application/json",
                  "application/yaml",
                  "external reference"
                ],
                "serial": true,
                "identity_strategy": "Authoritative master-qualified ID, otherwise governed URI or Dimension UUID; immutable revision and digest separate from time.",
                "source_refs": [
                  "SRC-001",
                  "SRC-005",
                  "SRC-006"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "policy-policy-identity-and-authority",
            "name": "Policy identity and authority",
            "description": "Organization-policy policy identity and authority."
          },
          "layer": {
            "id": "policy-approval",
            "name": "Approval and delegated mandate",
            "description": "Authored policy-context design for approval and delegated mandate, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule."
          },
          "finding": {
            "id": "policy-approval-record",
            "name": "Approval and delegated mandate record",
            "description": "Authored policy-context design for approval and delegated mandate, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule.",
            "source_refs": [
              "SRC-005",
              "SRC-006"
            ],
            "questions": [
              {
                "id": "policy-approval-q01",
                "text": "Who was authorized to approve this version and where is the delegation recorded?",
                "kind": "authority",
                "answer_data": [
                  "policy-approval-authority"
                ]
              },
              {
                "id": "policy-approval-q02",
                "text": "Which decision and approved text digest establish approval rather than a draft or proposal?",
                "kind": "evidence",
                "answer_data": [
                  "policy-approval-approval"
                ]
              },
              {
                "id": "policy-approval-q03",
                "text": "Which reservations or approval conditions limit its standing?",
                "kind": "constraint",
                "answer_data": [
                  "policy-approval-conditions"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "policy-approval-authority",
                "name": "authority",
                "description": "Proposed answer members: partyRef,mandateRef. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-005",
                  "SRC-006"
                ]
              },
              {
                "id": "policy-approval-approval",
                "name": "approval",
                "description": "Proposed answer members: decisionRef,versionRef,digest,time. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-005",
                  "SRC-006"
                ]
              },
              {
                "id": "policy-approval-conditions",
                "name": "conditions",
                "description": "Proposed answer members: scope,reservations,evidence. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-005",
                  "SRC-006"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "policy-approval-evidence",
                "name": "Approval and delegated mandate evidence",
                "description": "Versioned policy assertion and minimum authorized evidence references; restricted text and personal acknowledgements remain in protected masters.",
                "media_or_form": [
                  "text/markdown",
                  "application/json",
                  "application/yaml",
                  "external reference"
                ],
                "serial": true,
                "identity_strategy": "Authoritative master-qualified ID, otherwise governed URI or Dimension UUID; immutable revision and digest separate from time.",
                "source_refs": [
                  "SRC-005",
                  "SRC-006"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "policy-purpose-and-applicability",
            "name": "Purpose and applicability",
            "description": "Organization-policy purpose and applicability."
          },
          "layer": {
            "id": "policy-scope",
            "name": "Objectives and coverage",
            "description": "Authored policy-context design for objectives and coverage, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule."
          },
          "finding": {
            "id": "policy-scope-record",
            "name": "Objectives and coverage record",
            "description": "Authored policy-context design for objectives and coverage, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule.",
            "source_refs": [
              "SRC-002",
              "SRC-005"
            ],
            "questions": [
              {
                "id": "policy-scope-q01",
                "text": "Which organizational outcome or risk motivates this policy?",
                "kind": "definition",
                "answer_data": [
                  "policy-scope-rationale"
                ]
              },
              {
                "id": "policy-scope-q02",
                "text": "Which people, activities, locations and resources are included or excluded?",
                "kind": "constraint",
                "answer_data": [
                  "policy-scope-scope"
                ]
              },
              {
                "id": "policy-scope-q03",
                "text": "Which definitions and vocabulary versions disambiguate the scope?",
                "kind": "definition",
                "answer_data": [
                  "policy-scope-vocabulary"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "policy-scope-rationale",
                "name": "rationale",
                "description": "Proposed answer members: objective,riskRef. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-005"
                ]
              },
              {
                "id": "policy-scope-scope",
                "name": "scope",
                "description": "Proposed answer members: subjects,activities,territory,exclusions. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-005"
                ]
              },
              {
                "id": "policy-scope-vocabulary",
                "name": "vocabulary",
                "description": "Proposed answer members: terms,scheme,version. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-005"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "policy-scope-evidence",
                "name": "Objectives and coverage evidence",
                "description": "Versioned policy assertion and minimum authorized evidence references; restricted text and personal acknowledgements remain in protected masters.",
                "media_or_form": [
                  "text/markdown",
                  "application/json",
                  "application/yaml",
                  "external reference"
                ],
                "serial": true,
                "identity_strategy": "Authoritative master-qualified ID, otherwise governed URI or Dimension UUID; immutable revision and digest separate from time.",
                "source_refs": [
                  "SRC-002",
                  "SRC-005"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "policy-purpose-and-applicability",
            "name": "Purpose and applicability",
            "description": "Organization-policy purpose and applicability."
          },
          "layer": {
            "id": "policy-applicability",
            "name": "Conditions and unresolved applicability",
            "description": "Authored policy-context design for conditions and unresolved applicability, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule."
          },
          "finding": {
            "id": "policy-applicability-record",
            "name": "Conditions and unresolved applicability record",
            "description": "Authored policy-context design for conditions and unresolved applicability, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule.",
            "source_refs": [
              "SRC-002",
              "SRC-003",
              "SRC-005"
            ],
            "questions": [
              {
                "id": "policy-applicability-q01",
                "text": "Which facts and effective period must hold for the rule to apply to a case?",
                "kind": "constraint",
                "answer_data": [
                  "policy-applicability-conditions"
                ]
              },
              {
                "id": "policy-applicability-q02",
                "text": "Which actor, method, evidence and observation time support an applicability assessment?",
                "kind": "evidence",
                "answer_data": [
                  "policy-applicability-assessment"
                ]
              },
              {
                "id": "policy-applicability-q03",
                "text": "Which missing or conflicting facts leave applicability unknown and require escalation?",
                "kind": "exception",
                "answer_data": [
                  "policy-applicability-uncertainty"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "policy-applicability-conditions",
                "name": "conditions",
                "description": "Proposed answer members: predicates,timeWindow,requiredFacts. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-003",
                  "SRC-005"
                ]
              },
              {
                "id": "policy-applicability-assessment",
                "name": "assessment",
                "description": "Proposed answer members: actor,method,evidence,observedAt. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-003",
                  "SRC-005"
                ]
              },
              {
                "id": "policy-applicability-uncertainty",
                "name": "uncertainty",
                "description": "Proposed answer members: unknowns,conflicts,escalationRef. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-003",
                  "SRC-005"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "policy-applicability-evidence",
                "name": "Conditions and unresolved applicability evidence",
                "description": "Versioned policy assertion and minimum authorized evidence references; restricted text and personal acknowledgements remain in protected masters.",
                "media_or_form": [
                  "text/markdown",
                  "application/json",
                  "application/yaml",
                  "external reference"
                ],
                "serial": true,
                "identity_strategy": "Authoritative master-qualified ID, otherwise governed URI or Dimension UUID; immutable revision and digest separate from time.",
                "source_refs": [
                  "SRC-002",
                  "SRC-003",
                  "SRC-005"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "policy-normative-content-and-interpretation",
            "name": "Normative content and interpretation",
            "description": "Organization-policy normative content and interpretation."
          },
          "layer": {
            "id": "policy-clauses",
            "name": "Clauses and rule meaning",
            "description": "Authored policy-context design for clauses and rule meaning, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule."
          },
          "finding": {
            "id": "policy-clauses-record",
            "name": "Clauses and rule meaning record",
            "description": "Authored policy-context design for clauses and rule meaning, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule.",
            "source_refs": [
              "SRC-001",
              "SRC-005"
            ],
            "questions": [
              {
                "id": "policy-clauses-q01",
                "text": "Which stable clause states an obligation, prohibition, permission or nonbinding explanation?",
                "kind": "classification",
                "answer_data": [
                  "policy-clauses-clause"
                ]
              },
              {
                "id": "policy-clauses-q02",
                "text": "Which actor, action, target and conditions delimit the statement?",
                "kind": "definition",
                "answer_data": [
                  "policy-clauses-rule"
                ]
              },
              {
                "id": "policy-clauses-q03",
                "text": "Which authoritative text and interpretation preserve nuance not captured by structured fields?",
                "kind": "provenance",
                "answer_data": [
                  "policy-clauses-interpretation"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "policy-clauses-clause",
                "name": "clause",
                "description": "Proposed answer members: clauseId,modality. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-005"
                ]
              },
              {
                "id": "policy-clauses-rule",
                "name": "rule",
                "description": "Proposed answer members: actor,action,target,conditions. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-005"
                ]
              },
              {
                "id": "policy-clauses-interpretation",
                "name": "interpretation",
                "description": "Proposed answer members: textRef,language,authority,limitations. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-005"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "policy-clauses-evidence",
                "name": "Clauses and rule meaning evidence",
                "description": "Versioned policy assertion and minimum authorized evidence references; restricted text and personal acknowledgements remain in protected masters.",
                "media_or_form": [
                  "text/markdown",
                  "application/json",
                  "application/yaml",
                  "external reference"
                ],
                "serial": true,
                "identity_strategy": "Authoritative master-qualified ID, otherwise governed URI or Dimension UUID; immutable revision and digest separate from time.",
                "source_refs": [
                  "SRC-001",
                  "SRC-005"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "policy-normative-content-and-interpretation",
            "name": "Normative content and interpretation",
            "description": "Organization-policy normative content and interpretation."
          },
          "layer": {
            "id": "policy-precedence",
            "name": "Dependencies and precedence",
            "description": "Authored policy-context design for dependencies and precedence, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule."
          },
          "finding": {
            "id": "policy-precedence-record",
            "name": "Dependencies and precedence record",
            "description": "Authored policy-context design for dependencies and precedence, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-003"
            ],
            "questions": [
              {
                "id": "policy-precedence-q01",
                "text": "Which superior instruments or related policies constrain interpretation?",
                "kind": "relationship",
                "answer_data": [
                  "policy-precedence-dependencies"
                ]
              },
              {
                "id": "policy-precedence-q02",
                "text": "Which approved precedence or combination rule governs a particular overlap?",
                "kind": "authority",
                "answer_data": [
                  "policy-precedence-precedence"
                ]
              },
              {
                "id": "policy-precedence-q03",
                "text": "Which unresolved conflict remains visible without inventing a universal winner?",
                "kind": "exception",
                "answer_data": [
                  "policy-precedence-conflicts"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "policy-precedence-dependencies",
                "name": "dependencies",
                "description": "Proposed answer members: instrumentRefs,versions,relation. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-002",
                  "SRC-003"
                ]
              },
              {
                "id": "policy-precedence-precedence",
                "name": "precedence",
                "description": "Proposed answer members: rule,approver,scope. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-002",
                  "SRC-003"
                ]
              },
              {
                "id": "policy-precedence-conflicts",
                "name": "conflicts",
                "description": "Proposed answer members: clauseRefs,status,evidence,escalation. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-002",
                  "SRC-003"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "policy-precedence-evidence",
                "name": "Dependencies and precedence evidence",
                "description": "Versioned policy assertion and minimum authorized evidence references; restricted text and personal acknowledgements remain in protected masters.",
                "media_or_form": [
                  "text/markdown",
                  "application/json",
                  "application/yaml",
                  "external reference"
                ],
                "serial": true,
                "identity_strategy": "Authoritative master-qualified ID, otherwise governed URI or Dimension UUID; immutable revision and digest separate from time.",
                "source_refs": [
                  "SRC-001",
                  "SRC-002",
                  "SRC-003"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "policy-exceptions-and-implementation",
            "name": "Exceptions and implementation",
            "description": "Organization-policy exceptions and implementation."
          },
          "layer": {
            "id": "policy-exceptions",
            "name": "Authorized deviations",
            "description": "Authored policy-context design for authorized deviations, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule."
          },
          "finding": {
            "id": "policy-exceptions-record",
            "name": "Authorized deviations record",
            "description": "Authored policy-context design for authorized deviations, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule.",
            "source_refs": [
              "SRC-002",
              "SRC-004",
              "SRC-005"
            ],
            "questions": [
              {
                "id": "policy-exceptions-q01",
                "text": "Which clause and case does a requested exception concern and why?",
                "kind": "exception",
                "answer_data": [
                  "policy-exceptions-request"
                ]
              },
              {
                "id": "policy-exceptions-q02",
                "text": "Who approved or rejected it within what mandate, period and conditions?",
                "kind": "decision",
                "answer_data": [
                  "policy-exceptions-decision"
                ]
              },
              {
                "id": "policy-exceptions-q03",
                "text": "What evidence distinguishes expiry, revocation, pending approval and active deviation?",
                "kind": "state",
                "answer_data": [
                  "policy-exceptions-exceptionstate"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "policy-exceptions-request",
                "name": "request",
                "description": "Proposed answer members: clauseRef,caseRef,rationale. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-004",
                  "SRC-005"
                ]
              },
              {
                "id": "policy-exceptions-decision",
                "name": "decision",
                "description": "Proposed answer members: authorizer,mandateRef,outcome,validity,conditions. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-004",
                  "SRC-005"
                ]
              },
              {
                "id": "policy-exceptions-exceptionstate",
                "name": "exceptionState",
                "description": "Proposed answer members: status,eventRef,evidence. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-004",
                  "SRC-005"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "policy-exceptions-evidence",
                "name": "Authorized deviations evidence",
                "description": "Versioned policy assertion and minimum authorized evidence references; restricted text and personal acknowledgements remain in protected masters.",
                "media_or_form": [
                  "text/markdown",
                  "application/json",
                  "application/yaml",
                  "external reference"
                ],
                "serial": true,
                "identity_strategy": "Authoritative master-qualified ID, otherwise governed URI or Dimension UUID; immutable revision and digest separate from time.",
                "source_refs": [
                  "SRC-002",
                  "SRC-004",
                  "SRC-005"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "policy-exceptions-and-implementation",
            "name": "Exceptions and implementation",
            "description": "Organization-policy exceptions and implementation."
          },
          "layer": {
            "id": "policy-implementation",
            "name": "Procedures and safeguards",
            "description": "Authored policy-context design for procedures and safeguards, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule."
          },
          "finding": {
            "id": "policy-implementation-record",
            "name": "Procedures and safeguards record",
            "description": "Authored policy-context design for procedures and safeguards, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule.",
            "source_refs": [
              "SRC-002",
              "SRC-004",
              "SRC-005"
            ],
            "questions": [
              {
                "id": "policy-implementation-q01",
                "text": "Which procedures, controls and responsible roles implement each policy clause?",
                "kind": "relationship",
                "answer_data": [
                  "policy-implementation-implementation"
                ]
              },
              {
                "id": "policy-implementation-q02",
                "text": "Which implementation evidence or test supports the mapping without equating intention with compliance?",
                "kind": "evidence",
                "answer_data": [
                  "policy-implementation-assurance"
                ]
              },
              {
                "id": "policy-implementation-q03",
                "text": "Which failure modes, consequences and safe escalation paths are documented?",
                "kind": "constraint",
                "answer_data": [
                  "policy-implementation-failure"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "policy-implementation-implementation",
                "name": "implementation",
                "description": "Proposed answer members: clauseRef,procedureRefs,controlRefs,roles. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-004",
                  "SRC-005"
                ]
              },
              {
                "id": "policy-implementation-assurance",
                "name": "assurance",
                "description": "Proposed answer members: testRef,result,evidence,limits. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-004",
                  "SRC-005"
                ]
              },
              {
                "id": "policy-implementation-failure",
                "name": "failure",
                "description": "Proposed answer members: mode,harm,escalation,recoveryRef. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-004",
                  "SRC-005"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "policy-implementation-evidence",
                "name": "Procedures and safeguards evidence",
                "description": "Versioned policy assertion and minimum authorized evidence references; restricted text and personal acknowledgements remain in protected masters.",
                "media_or_form": [
                  "text/markdown",
                  "application/json",
                  "application/yaml",
                  "external reference"
                ],
                "serial": true,
                "identity_strategy": "Authoritative master-qualified ID, otherwise governed URI or Dimension UUID; immutable revision and digest separate from time.",
                "source_refs": [
                  "SRC-002",
                  "SRC-004",
                  "SRC-005"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "policy-dissemination-and-lifecycle",
            "name": "Dissemination and lifecycle",
            "description": "Organization-policy dissemination and lifecycle."
          },
          "layer": {
            "id": "policy-release",
            "name": "Release and acknowledgement",
            "description": "Authored policy-context design for release and acknowledgement, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule."
          },
          "finding": {
            "id": "policy-release-record",
            "name": "Release and acknowledgement record",
            "description": "Authored policy-context design for release and acknowledgement, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule.",
            "source_refs": [
              "SRC-002",
              "SRC-005"
            ],
            "questions": [
              {
                "id": "policy-release-q01",
                "text": "Which approved version, language and audience were published through which channel?",
                "kind": "event",
                "answer_data": [
                  "policy-release-release"
                ]
              },
              {
                "id": "policy-release-q02",
                "text": "Which receipt, acknowledgement or training evidence exists for a recipient?",
                "kind": "evidence",
                "answer_data": [
                  "policy-release-acknowledgement"
                ]
              },
              {
                "id": "policy-release-q03",
                "text": "Which access or translation limitations prevent treating receipt as understanding, consent or compliance?",
                "kind": "constraint",
                "answer_data": [
                  "policy-release-communicationlimits"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "policy-release-release",
                "name": "release",
                "description": "Proposed answer members: version,language,audience,channel,time. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-005"
                ]
              },
              {
                "id": "policy-release-acknowledgement",
                "name": "acknowledgement",
                "description": "Proposed answer members: recipient,evidence,type,time. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-005"
                ]
              },
              {
                "id": "policy-release-communicationlimits",
                "name": "communicationLimits",
                "description": "Proposed answer members: access,translation,unknowns. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-005"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "policy-release-evidence",
                "name": "Release and acknowledgement evidence",
                "description": "Versioned policy assertion and minimum authorized evidence references; restricted text and personal acknowledgements remain in protected masters.",
                "media_or_form": [
                  "text/markdown",
                  "application/json",
                  "application/yaml",
                  "external reference"
                ],
                "serial": true,
                "identity_strategy": "Authoritative master-qualified ID, otherwise governed URI or Dimension UUID; immutable revision and digest separate from time.",
                "source_refs": [
                  "SRC-002",
                  "SRC-005"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "policy-dissemination-and-lifecycle",
            "name": "Dissemination and lifecycle",
            "description": "Organization-policy dissemination and lifecycle."
          },
          "layer": {
            "id": "policy-review",
            "name": "Review, supersession and retirement",
            "description": "Authored policy-context design for review, supersession and retirement, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule."
          },
          "finding": {
            "id": "policy-review-record",
            "name": "Review, supersession and retirement record",
            "description": "Authored policy-context design for review, supersession and retirement, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule.",
            "source_refs": [
              "SRC-002",
              "SRC-005",
              "SRC-006"
            ],
            "questions": [
              {
                "id": "policy-review-q01",
                "text": "Which review schedule or triggering event applies and who owns the review?",
                "kind": "process",
                "answer_data": [
                  "policy-review-review"
                ]
              },
              {
                "id": "policy-review-q02",
                "text": "Which revision replaces which predecessor with what effective interval and transition arrangements?",
                "kind": "lifecycle",
                "answer_data": [
                  "policy-review-revision"
                ]
              },
              {
                "id": "policy-review-q03",
                "text": "Which withdrawal or retirement decision ends applicability while preserving historical evidence?",
                "kind": "lifecycle",
                "answer_data": [
                  "policy-review-retirement"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "policy-review-review",
                "name": "review",
                "description": "Proposed answer members: owner,frequency,triggers,lastReview. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-005",
                  "SRC-006"
                ]
              },
              {
                "id": "policy-review-revision",
                "name": "revision",
                "description": "Proposed answer members: predecessor,successor,effectivePeriod,transition. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-005",
                  "SRC-006"
                ]
              },
              {
                "id": "policy-review-retirement",
                "name": "retirement",
                "description": "Proposed answer members: decisionRef,end,reason,recordRetentionRef. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-005",
                  "SRC-006"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "policy-review-evidence",
                "name": "Review, supersession and retirement evidence",
                "description": "Versioned policy assertion and minimum authorized evidence references; restricted text and personal acknowledgements remain in protected masters.",
                "media_or_form": [
                  "text/markdown",
                  "application/json",
                  "application/yaml",
                  "external reference"
                ],
                "serial": true,
                "identity_strategy": "Authoritative master-qualified ID, otherwise governed URI or Dimension UUID; immutable revision and digest separate from time.",
                "source_refs": [
                  "SRC-002",
                  "SRC-005",
                  "SRC-006"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "policy-policy-memory-and-interoperability",
            "name": "Policy memory and interoperability",
            "description": "Organization-policy policy memory and interoperability."
          },
          "layer": {
            "id": "policy-mastership",
            "name": "Mastership and controlled evidence",
            "description": "Authored policy-context design for mastership and controlled evidence, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule."
          },
          "finding": {
            "id": "policy-mastership-record",
            "name": "Mastership and controlled evidence record",
            "description": "Authored policy-context design for mastership and controlled evidence, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule.",
            "source_refs": [
              "SRC-004",
              "SRC-006"
            ],
            "questions": [
              {
                "id": "policy-mastership-q01",
                "text": "Which master copy, version digest and provenance distinguish authoritative text from projections?",
                "kind": "provenance",
                "answer_data": [
                  "policy-mastership-mastership"
                ]
              },
              {
                "id": "policy-mastership-q02",
                "text": "Which roles may read or change drafts, approved text, exceptions and personal acknowledgements?",
                "kind": "access",
                "answer_data": [
                  "policy-mastership-access"
                ]
              },
              {
                "id": "policy-mastership-q03",
                "text": "Which retention, legal hold and correction rules preserve evidence without silently rewriting history?",
                "kind": "retention",
                "answer_data": [
                  "policy-mastership-recordrules"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "policy-mastership-mastership",
                "name": "mastership",
                "description": "Proposed answer members: master,version,digest,provenance. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-004",
                  "SRC-006"
                ]
              },
              {
                "id": "policy-mastership-access",
                "name": "access",
                "description": "Proposed answer members: scope,roles,exceptions. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-004",
                  "SRC-006"
                ]
              },
              {
                "id": "policy-mastership-recordrules",
                "name": "recordRules",
                "description": "Proposed answer members: retention,hold,correction,tombstone. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-004",
                  "SRC-006"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "policy-mastership-evidence",
                "name": "Mastership and controlled evidence evidence",
                "description": "Versioned policy assertion and minimum authorized evidence references; restricted text and personal acknowledgements remain in protected masters.",
                "media_or_form": [
                  "text/markdown",
                  "application/json",
                  "application/yaml",
                  "external reference"
                ],
                "serial": true,
                "identity_strategy": "Authoritative master-qualified ID, otherwise governed URI or Dimension UUID; immutable revision and digest separate from time.",
                "source_refs": [
                  "SRC-004",
                  "SRC-006"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "policy-policy-memory-and-interoperability",
            "name": "Policy memory and interoperability",
            "description": "Organization-policy policy memory and interoperability."
          },
          "layer": {
            "id": "policy-mapping",
            "name": "Machine interpretation and acceptance",
            "description": "Authored policy-context design for machine interpretation and acceptance, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule."
          },
          "finding": {
            "id": "policy-mapping-record",
            "name": "Machine interpretation and acceptance record",
            "description": "Authored policy-context design for machine interpretation and acceptance, retaining authority, version and evidence. Descriptive record, not an executable or universally mandatory rule.",
            "source_refs": [
              "SRC-001",
              "SRC-003",
              "SRC-006"
            ],
            "questions": [
              {
                "id": "policy-mapping-q01",
                "text": "Which versioned external policy profile maps selected clauses and what meaning remains unmapped?",
                "kind": "interoperability",
                "answer_data": [
                  "policy-mapping-mapping"
                ]
              },
              {
                "id": "policy-mapping-q02",
                "text": "Which fixtures test ambiguous scope, expired exceptions, contradictory rules and stale versions?",
                "kind": "validation",
                "answer_data": [
                  "policy-mapping-validation"
                ]
              },
              {
                "id": "policy-mapping-q03",
                "text": "Which permissions and validated adapter are required before any proposed record operation affects an external system?",
                "kind": "authority",
                "answer_data": [
                  "policy-mapping-executionboundary"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "policy-mapping-mapping",
                "name": "mapping",
                "description": "Proposed answer members: profile,version,clauseMappings,losses. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-003",
                  "SRC-006"
                ]
              },
              {
                "id": "policy-mapping-validation",
                "name": "validation",
                "description": "Proposed answer members: fixtures,result,limits. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-003",
                  "SRC-006"
                ]
              },
              {
                "id": "policy-mapping-executionboundary",
                "name": "executionBoundary",
                "description": "Proposed answer members: permission,adapter,preconditions,rollback. Preserve explicit unknowns and provenance. Nested member schemas and runtime fixtures remain a declared gap.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-003",
                  "SRC-006"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "policy-mapping-evidence",
                "name": "Machine interpretation and acceptance evidence",
                "description": "Versioned policy assertion and minimum authorized evidence references; restricted text and personal acknowledgements remain in protected masters.",
                "media_or_form": [
                  "text/markdown",
                  "application/json",
                  "application/yaml",
                  "external reference"
                ],
                "serial": true,
                "identity_strategy": "Authoritative master-qualified ID, otherwise governed URI or Dimension UUID; immutable revision and digest separate from time.",
                "source_refs": [
                  "SRC-001",
                  "SRC-003",
                  "SRC-006"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        }
      ],
      "functions": [
        {
          "id": "resolve-policy-version",
          "name": "Resolve policy version",
          "description": "Proposed record operation: resolve policy version. Not an implemented autonomous policy executor.",
          "inputs": [
            "Qualified policy ID",
            "Case time and organization"
          ],
          "outputs": [
            "Version reference or unresolved candidates"
          ],
          "preconditions": [
            "Read scope",
            "Known time precision"
          ],
          "effects": [
            "Read-only, no permission decision"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-005",
            "SRC-006"
          ]
        },
        {
          "id": "record-policy-approval",
          "name": "Record approval evidence",
          "description": "Proposed record operation: record approval evidence. Not an implemented autonomous policy executor.",
          "inputs": [
            "Decision and mandate refs",
            "Approved digest",
            "Expected revision"
          ],
          "outputs": [
            "Attributed approval record or unresolved evidence"
          ],
          "preconditions": [
            "Write scope",
            "Approval evidence available"
          ],
          "effects": [
            "No approval itself conferred"
          ],
          "source_refs": [
            "SRC-005",
            "SRC-006"
          ]
        },
        {
          "id": "record-applicability",
          "name": "Record applicability assessment",
          "description": "Proposed record operation: record applicability assessment. Not an implemented autonomous policy executor.",
          "inputs": [
            "Case facts and evidence",
            "Policy version",
            "Named evaluation profile"
          ],
          "outputs": [
            "Assessment with uncertainty and method"
          ],
          "preconditions": [
            "Authorized read/write scope",
            "Missing facts preserved"
          ],
          "effects": [
            "No enforcement or automatic permit"
          ],
          "source_refs": [
            "SRC-002",
            "SRC-003",
            "SRC-005"
          ]
        },
        {
          "id": "record-policy-exception",
          "name": "Record exception decision",
          "description": "Proposed record operation: record exception decision. Not an implemented autonomous policy executor.",
          "inputs": [
            "Clause and case refs",
            "Authority decision",
            "Validity and conditions"
          ],
          "outputs": [
            "Scoped exception assertion"
          ],
          "preconditions": [
            "Write authority",
            "Decision distinct from request"
          ],
          "effects": [
            "No legal waiver or access change executed"
          ],
          "source_refs": [
            "SRC-002",
            "SRC-004",
            "SRC-005"
          ]
        },
        {
          "id": "link-policy-implementation",
          "name": "Link implementation evidence",
          "description": "Proposed record operation: link implementation evidence. Not an implemented autonomous policy executor.",
          "inputs": [
            "Clause refs",
            "Procedure/control refs",
            "Observation or test evidence"
          ],
          "outputs": [
            "Qualified mapping with assurance limits"
          ],
          "preconditions": [
            "Disclosure and write authority",
            "Evidence provenance retained"
          ],
          "effects": [
            "No compliance certification or control execution"
          ],
          "source_refs": [
            "SRC-002",
            "SRC-004",
            "SRC-005"
          ]
        },
        {
          "id": "export-policy-projection",
          "name": "Export policy projection",
          "description": "Proposed record operation: export policy projection. Not an implemented autonomous policy executor.",
          "inputs": [
            "Allowed fields",
            "Target profile/version",
            "Loss annotations"
          ],
          "outputs": [
            "Projection or refusal"
          ],
          "preconditions": [
            "Disclosure authority",
            "Unmapped meaning visible"
          ],
          "effects": [
            "No external release without authorization or engine deployment"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-003",
            "SRC-006"
          ]
        }
      ],
      "composition": [
        {
          "target": "WM-ORG-007",
          "relation": "REFERENCE",
          "purpose": "Proposed authority-instrument reference, not charter inheritance.",
          "required": false,
          "source_refs": [
            "SRC-002",
            "SRC-005"
          ]
        },
        {
          "target": "WM-ORG-018",
          "relation": "REFERENCE",
          "purpose": "Proposed approving-body reference with separate mandate evidence.",
          "required": false,
          "source_refs": [
            "SRC-005"
          ]
        },
        {
          "target": "https://www.w3.org/TR/2018/REC-odrl-model-20180215/",
          "relation": "ALIGN",
          "purpose": "Limited clause projection; unmapped meaning and profile rules retained.",
          "required": false,
          "source_refs": [
            "SRC-001"
          ]
        },
        {
          "target": "https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html",
          "relation": "ALIGN",
          "purpose": "Candidate evaluation-profile mapping, not a decision point implementation.",
          "required": false,
          "source_refs": [
            "SRC-003"
          ]
        },
        {
          "target": "https://www.w3.org/TR/prov-o/",
          "relation": "ALIGN",
          "purpose": "Revision provenance, not proof of approval.",
          "required": false,
          "source_refs": [
            "SRC-006"
          ]
        }
      ],
      "researchAdjudication": {
        "providerMode": "single-provider-waiver",
        "activeProviders": [
          "codex"
        ],
        "waivedProviders": [
          "claude",
          "grok"
        ],
        "providerPolicy": {
          "contract_version": "1.0.0",
          "mode": "single-provider-waiver",
          "effective_at": "2026-09-06T00:00:00Z",
          "scope": "Canonical single-stream subject-model research after the six-workstream consolidation",
          "active_providers": [
            "codex"
          ],
          "waived_providers": [
            {
              "provider": "claude",
              "authorized_by": "repository owner",
              "authorized_at": "2026-09-06T00:00:00Z",
              "reason": "Claude produced no result on prior 1800-second and 900-second attempts and again timed out on bounded 600-second Sonnet and 300-second Haiku passes. The owner prioritized completion over provider availability."
            },
            {
              "provider": "grok",
              "authorized_by": "repository owner",
              "authorized_at": "2026-09-06T00:00:00Z",
              "reason": "The repository owner authorized completion without Grok when Grok is unavailable, slow or schema-invalid. Grok may still be attempted as a bounded supplemental reviewer, but its failure never blocks a valid Claude plus no-tools result."
            }
          ],
          "review_rule": "Codex may complete source-grounded fallback research after bounded Claude and Grok attempts fail. It requires a separate no-tools adversarial audit and remains reviewable-draft with a visible absence-of-external-review hold.",
          "supplemental_provider_attempts": [
            {
              "provider": "claude",
              "required": false,
              "maximum_attempts": 1,
              "failure_policy": "record-and-continue",
              "admission_rule": "Use only a locally schema-valid result whose sources and boundaries survive adjudication."
            },
            {
              "provider": "grok",
              "required": false,
              "maximum_attempts": 1,
              "failure_policy": "record-and-continue",
              "admission_rule": "Use only a locally schema-valid result whose sources and boundaries survive adjudication."
            }
          ]
        },
        "boundaryDecision": {
          "entry_kind": "entity",
          "status": "accepted",
          "rationale": "An identifiable normative information object with distinct approved versions and drafts; law, procedure and enforcement remain separate."
        },
        "decisions": [
          {
            "concept": "Policy identity",
            "disposition": "accepted",
            "rationale": "Policy, version, translation and approval evidence are separate."
          },
          {
            "concept": "Temporal standing",
            "disposition": "accepted",
            "rationale": "Review due date is not expiry; approval, issue and effect are not conflated."
          },
          {
            "concept": "Applicability and conflicts",
            "disposition": "accepted with limitations",
            "rationale": "Unknown is not permission; named profile rules are not universal precedence."
          },
          {
            "concept": "Exceptions and implementation",
            "disposition": "accepted with limitations",
            "rationale": "Evidence records do not grant exceptions or certify compliance; profile fixtures remain missing."
          },
          {
            "concept": "Composition",
            "disposition": "deferred",
            "rationale": "Proposed authority references and lossy profile alignments are not ratified inheritance or conformance."
          },
          {
            "concept": "Independent review",
            "disposition": "accepted with mandatory hold",
            "rationale": "Both providers timed out once; same-agent frozen self-audit is not independent review."
          }
        ],
        "publicationHolds": [
          "Codex-only after Claude and Grok timeouts; frozen self-audit is not independent review. Assurance remains reviewable-draft.",
          "Selected source clauses only; exact release currency, dated pins and reuse licenses require review. Historical Edinburgh policy is not current law.",
          "ISO HEAD unavailable although PDF text was readable; transport limitation remains visible.",
          "Nested-member schemas, exception-profile tests and executable policy/round-trip fixtures are not implemented.",
          "Proposed composition is not ratified; no lossless prose compilation, legal enforceability or external policy execution is claimed.",
          "Independent external review was explicitly waived by the repository owner; this codex-only result remains a reviewable draft."
        ],
        "deferredResearch": [
          "Independent source/profile/license review.",
          "Executable nested schemas and ambiguity/exception fixtures.",
          "Ratified composition and loss-aware machine policy adapters."
        ]
      }
    },
    "policy_rule": {
      "publication": {
        "status": "published",
        "adjudicationStatus": "reviewable-draft",
        "publishableCanonical": false,
        "generatedAt": "2026-09-02T20:13:47Z",
        "synthesisSha256": "a5fd245ed310d3e3e1edc919f30a25a0b9859b5df9ea68536f3b730ce43fec5c",
        "providerMode": "single-provider-waiver",
        "providers": [
          "Claude"
        ],
        "waivedProviders": [
          "Grok"
        ]
      },
      "model": {
        "registry_id": "vr.wm-knw-012",
        "model_id": "WM-KNW-012",
        "name": "Policy / Rule",
        "entry_kind": "aggregate",
        "purpose": "Provide the format-neutral context an agent needs to identify, classify, compose, govern, version and interpret an executable or interpretable normative statement, while delegating condition expression, runtime evaluation, enforcement and governed-process semantics to referenced models.",
        "scope_statement": "Describes an individual normative statement (policy, policy set, or atomic rule slot) as a governed record: identity and version identity, deontic or alethic force, issuing authority and mandate, applicability scope, rule-slot structure, declared precedence and conflict strategy, registered derogations, lifecycle and temporal validity, provenance and source-provision mapping, declared standard alignments, and record classification and retention. Storage- and interface-neutral: JSON, YAML, Markdown, XML, RDF, Git trees, MCP surfaces and document databases are manifestations of one record. Carries references and binding metadata for constraint expressions but never the expression grammar, and never renders, executes, enforces or logs a decision.",
        "in_scope": [
          "Identity, naming, citation forms and version identity, separated into abstract work, dated expression and rendered manifestation.",
          "Deontic modality (obligation, permission, prohibition, right), alethic-versus-deontic classification, enforcement level and defeasibility.",
          "Instrument genre and binding form: legislation, regulation, standard, internal directive, set, offer, agreement.",
          "Issuing authority, mandate, adoption-decision reference, and post-issuance record ownership and stewardship roles.",
          "Applicability scope: jurisdiction, territory, subject-matter competence, in-scope parties, target resources, governed actions and contextual conditions.",
          "Rule-slot inventory, atomicity, policy-set containment and inheritance.",
          "References and binding metadata for externally owned constraint or rule expressions, plus subject-specific parameter values and tailoring.",
          "Declared precedence: combining or hit-policy strategy identifiers, conflict terms and pairwise superiority relations.",
          "Registered exceptions, waivers and derogations, and recorded alternative interpretations and known contradictions.",
          "Lifecycle states, amendment, supersession and repeal; in-force, efficacy and applicability intervals with event time and record time.",
          "Provenance, derivation, attribution and mapping from rule slots to authoritative source provisions.",
          "Declared standard alignments, structural well-formedness requirements, manifestation integrity, record classification, retention declaration and disposition class."
        ],
        "out_of_scope": [
          "Constraint and rule expression grammar, operator and operand vocabularies, and logical composition semantics (WM-KNW-013).",
          "Runtime policy evaluation, decision rendering, obligation discharge, enforcement actions and decision results (referenced decision or enforcement runtime).",
          "Audit-trail entities, event streams and log storage for evaluation, enforcement or access.",
          "Process, activity and task definitions and their execution state (WM-ACT-003).",
          "Projection, disclosure and output-shape semantics of specialised disclosure policies (WM-XCT-003).",
          "Party, organisation, resource and place master data.",
          "Compliance risk assessment, control-effectiveness measurement and non-compliance case handling.",
          "Sanction computation, penalty scales and litigation records.",
          "Storage engines, serialization formats, access interfaces and repository mechanics.",
          "Cryptographic signing ceremonies and PKI trust management."
        ],
        "boundary_notes": [
          {
            "neighbor": "WM-KNW-013 Constraint / Rule expression",
            "distinction": "The condition itself (left operand, operator, right operand, logical operands, refinements) and its own lifecycle are owned there. This model carries only the reference, the binding point, the expression-language reference and subject-specific parameter values.",
            "source_refs": [
              "SRC-001",
              "SRC-002"
            ]
          },
          {
            "neighbor": "Referenced decision or enforcement runtime (XACML PDP/PEP, ABAC access decision function)",
            "distinction": "Evaluation, decision rendering, obligation discharge and decision logging are runtime concerns. This model declares which combining or hit-policy strategy applies and where its normative definition lives; it never evaluates or enforces.",
            "source_refs": [
              "SRC-002",
              "SRC-007"
            ]
          },
          {
            "neighbor": "WM-ACT-003 Process",
            "distinction": "Activities, tasks, sequence and execution state are owned there. The governance edge is authored by WM-ACT-003; this model only records applicability pointers to governed processes.",
            "source_refs": [
              "SRC-006",
              "SRC-007"
            ]
          },
          {
            "neighbor": "WM-XCT-003 Projection / disclosure policy",
            "distinction": "Output-shape, redaction-transform and disclosure-projection semantics are specialised there. Generic identity, authority, lifecycle and conflict machinery is retained here, as the relation rationale requires.",
            "source_refs": [
              "SRC-001",
              "SRC-002"
            ]
          },
          {
            "neighbor": "Compliance management system (obligations monitoring)",
            "distinction": "Compliance risk evaluation, monitoring, reporting and non-compliance handling sit in a compliance management model. This model holds the obligation statement and its governance metadata only.",
            "source_refs": [
              "SRC-013"
            ]
          },
          {
            "neighbor": "Records and document management",
            "distinction": "Manifestation storage, format conversion, digital preservation and disposal execution belong to records management. This model holds work/expression identity, retention declaration, disposition class and tombstone.",
            "source_refs": [
              "SRC-004",
              "SRC-011"
            ]
          },
          {
            "neighbor": "WM-POL-001 parent policy domain",
            "distinction": "Domain grouping, portfolio taxonomy and cross-policy programme governance sit with the parent. This model describes one normative statement instance.",
            "source_refs": [
              "SRC-002",
              "SRC-013"
            ]
          }
        ]
      },
      "selected_findings": [
        {
          "bundle": {
            "id": "normative-identity-and-classification",
            "name": "Normative identity and classification",
            "description": "What the statement is, how it is durably identified and versioned, and what normative force it carries."
          },
          "layer": {
            "id": "identity-and-designation",
            "name": "Identity and designation",
            "description": "Durable identification, naming, citation and version identity of the statement, independent of storage format."
          },
          "finding": {
            "id": "statement-identifier-and-naming",
            "name": "Statement identifier and naming",
            "description": "How a normative statement and its contained rule slots are uniquely identified, titled and cited across systems.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-004",
              "SRC-011"
            ],
            "questions": [
              {
                "id": "q-master-identifier",
                "text": "Which authoritative master-system identifier designates this statement, and which system issues it?",
                "kind": "identity",
                "answer_data": [
                  "issuing system of record reference",
                  "master identifier value",
                  "identifier scheme code"
                ]
              },
              {
                "id": "q-global-iri",
                "text": "Which governed global identifier or IRI resolves this statement for external citation?",
                "kind": "interoperability",
                "answer_data": [
                  "statement IRI",
                  "resolution service reference",
                  "persistence commitment"
                ]
              },
              {
                "id": "q-container-versus-slot-id",
                "text": "How are the statement container and its contained rule slots identified separately?",
                "kind": "composition",
                "answer_data": [
                  "container identifier",
                  "rule slot identifiers",
                  "containment relation"
                ]
              },
              {
                "id": "q-titles-and-citation",
                "text": "Which official titles, short titles and citation forms are registered, and in which languages?",
                "kind": "definition",
                "answer_data": [
                  "official title with language tag",
                  "short title",
                  "conventional citation form"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-master-identifier",
                "name": "statement master identifier",
                "description": "Identifier assigned by the authoritative system of record for the statement.",
                "value_kind": "identifier",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-010"
                ]
              },
              {
                "id": "de-statement-iri",
                "name": "statement IRI",
                "description": "Governed global identifier resolving the abstract statement.",
                "value_kind": "identifier",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-011"
                ]
              },
              {
                "id": "de-official-title",
                "name": "official title",
                "description": "Registered title with language tag; may repeat per authentic language.",
                "value_kind": "text",
                "cardinality": "1..n",
                "required": true,
                "source_refs": [
                  "SRC-004",
                  "SRC-011"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Identifiers, titles and citation forms are reference values carried directly on the statement record; answering these questions produces no rendered or media-bearing artifact, and the identifier scheme itself is governed by an external registry rather than produced here."
          }
        },
        {
          "bundle": {
            "id": "normative-identity-and-classification",
            "name": "Normative identity and classification",
            "description": "What the statement is, how it is durably identified and versioned, and what normative force it carries."
          },
          "layer": {
            "id": "identity-and-designation",
            "name": "Identity and designation",
            "description": "Durable identification, naming, citation and version identity of the statement, independent of storage format."
          },
          "finding": {
            "id": "version-identity-and-point-in-time",
            "name": "Version identity and point-in-time expression",
            "description": "Separation of the abstract work from its dated expressions and rendered manifestations, and the identity of each version.",
            "source_refs": [
              "SRC-002",
              "SRC-004",
              "SRC-010",
              "SRC-011"
            ],
            "questions": [
              {
                "id": "q-work-expression-split",
                "text": "How is the abstract statement distinguished from its dated versions and its rendered manifestations?",
                "kind": "classification",
                "answer_data": [
                  "work identifier",
                  "expression identifier",
                  "manifestation identifier"
                ]
              },
              {
                "id": "q-version-designator",
                "text": "What version designator is assigned to each expression, and how is version ordering determined?",
                "kind": "identity",
                "answer_data": [
                  "version designator",
                  "ordering rule",
                  "version match expression"
                ]
              },
              {
                "id": "q-current-consolidation",
                "text": "Which expression is the current consolidated one, and which are historical point-in-time versions?",
                "kind": "state",
                "answer_data": [
                  "consolidation status code",
                  "superseded expression list",
                  "currency assertion"
                ]
              },
              {
                "id": "q-change-obligation",
                "text": "What must change on the record whenever the content of an expression changes?",
                "kind": "constraint",
                "answer_data": [
                  "new record UUID",
                  "new last-modified instant",
                  "new version designator"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-work-identifier",
                "name": "work identifier",
                "description": "Stable identifier of the abstract statement across all its versions.",
                "value_kind": "identifier",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-004",
                  "SRC-011"
                ]
              },
              {
                "id": "de-expression-version",
                "name": "expression version designator",
                "description": "Version label assigned to a dated expression of the statement.",
                "value_kind": "text",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-010"
                ]
              },
              {
                "id": "de-expression-last-modified",
                "name": "expression last-modified instant",
                "description": "Instant at which the expression record last changed.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-009",
                  "SRC-010"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "consolidated-expression",
                "name": "Consolidated point-in-time expression",
                "description": "A dated, citable rendering of the statement as it stood over a specific interval, produced by consolidating applied modifications.",
                "media_or_form": [
                  "structured legal or policy document",
                  "serialized machine-readable expression",
                  "rendered human-readable text"
                ],
                "serial": true,
                "identity_strategy": "Authoritative expression identifier from the publishing system of record; otherwise the governed work IRI plus the version designator; otherwise a UUID minted by the adopting Dimension with the fallback reason recorded.",
                "source_refs": [
                  "SRC-004",
                  "SRC-010",
                  "SRC-011"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "normative-identity-and-classification",
            "name": "Normative identity and classification",
            "description": "What the statement is, how it is durably identified and versioned, and what normative force it carries."
          },
          "layer": {
            "id": "normative-classification",
            "name": "Normative classification",
            "description": "The force, modality, defeasibility and instrument genre of the statement."
          },
          "finding": {
            "id": "deontic-modality-force-and-defeasibility",
            "name": "Deontic modality, force and defeasibility",
            "description": "Which normative modality each rule slot carries, whether it can be violated, how severely, and whether it can be defeated.",
            "source_refs": [
              "SRC-001",
              "SRC-003",
              "SRC-005"
            ],
            "questions": [
              {
                "id": "q-modality-per-slot",
                "text": "Which deontic modality does each rule slot carry: obligation, permission, prohibition or right?",
                "kind": "classification",
                "answer_data": [
                  "deontic modality code per slot",
                  "modality vocabulary reference"
                ]
              },
              {
                "id": "q-alethic-or-deontic",
                "text": "Is the statement an alethic necessity that cannot be violated, or a deontic obligation that can be?",
                "kind": "definition",
                "answer_data": [
                  "modality family code",
                  "justification note"
                ]
              },
              {
                "id": "q-enforcement-level",
                "text": "What enforcement level on the graded severity scale applies when the statement is violated?",
                "kind": "measurement",
                "answer_data": [
                  "enforcement level code",
                  "ordinal position on the declared scale",
                  "scale definition reference"
                ]
              },
              {
                "id": "q-defeasibility",
                "text": "Is the statement defeasible, and by which declared mechanism may it be defeated?",
                "kind": "constraint",
                "answer_data": [
                  "defeasibility flag",
                  "defeat mechanism reference"
                ]
              },
              {
                "id": "q-strong-permission",
                "text": "Does the statement express a strong permission acting as an explicit exception to a prohibition?",
                "kind": "exception",
                "answer_data": [
                  "permission strength code",
                  "prohibition excepted reference"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-deontic-modality",
                "name": "deontic modality code",
                "description": "Obligation, permission, prohibition or right, asserted per rule slot.",
                "value_kind": "code",
                "cardinality": "1..n",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-003",
                  "SRC-005"
                ]
              },
              {
                "id": "de-modality-family",
                "name": "modality family code",
                "description": "Alethic or deontic classification of the statement.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-005"
                ]
              },
              {
                "id": "de-enforcement-level",
                "name": "enforcement level code",
                "description": "Position on the graded severity scale for violation of a behavioural rule.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-005"
                ]
              },
              {
                "id": "de-defeasibility-flag",
                "name": "defeasibility flag",
                "description": "Whether the statement admits defeat by a superior or more specific statement.",
                "value_kind": "boolean",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-003"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Modality, enforcement level and defeasibility are coded assertions on the statement record resolved against externally governed vocabularies; the normative text that carries them is held by the authoritative source instrument declared under the provenance layer, so declaring a second artifact here would duplicate it."
          }
        },
        {
          "bundle": {
            "id": "authority-and-applicability",
            "name": "Authority and applicability",
            "description": "Who issued the statement, under what mandate, who now owns the record, and over what it claims to apply."
          },
          "layer": {
            "id": "authority-and-accountability",
            "name": "Authority and accountability",
            "description": "Issuing authority and mandate at origin, and accountable ownership of the record afterwards."
          },
          "finding": {
            "id": "issuing-authority-and-mandate",
            "name": "Issuing authority and mandate",
            "description": "Which party issued the statement, under what legal or organisational competence, and by which recorded adoption decision.",
            "source_refs": [
              "SRC-002",
              "SRC-003",
              "SRC-004"
            ],
            "questions": [
              {
                "id": "q-issuing-party",
                "text": "Which party issued the statement, and under what legal or organisational mandate?",
                "kind": "authority",
                "answer_data": [
                  "issuing authority reference",
                  "mandate basis reference",
                  "mandate type code"
                ]
              },
              {
                "id": "q-adoption-decision",
                "text": "Which body formally adopted the statement, and by which recorded decision?",
                "kind": "decision",
                "answer_data": [
                  "adopting body reference",
                  "adoption decision reference",
                  "adoption instant"
                ]
              },
              {
                "id": "q-competence-bounds",
                "text": "Within what competence is the issuing authority empowered to bind?",
                "kind": "constraint",
                "answer_data": [
                  "competence scope description",
                  "enabling instrument reference",
                  "ultra vires risk note"
                ]
              },
              {
                "id": "q-authority-evidence",
                "text": "What evidence supports the authority claim, and where does that evidence record live?",
                "kind": "evidence",
                "answer_data": [
                  "evidence record reference",
                  "evidence custodian reference",
                  "evidence sufficiency note"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-issuing-authority",
                "name": "issuing authority reference",
                "description": "Reference to the party record of the issuing authority.",
                "value_kind": "reference",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-003"
                ]
              },
              {
                "id": "de-mandate-basis",
                "name": "mandate basis reference",
                "description": "Reference to the enabling instrument conferring authority to issue.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-003"
                ]
              },
              {
                "id": "de-adoption-decision",
                "name": "adoption decision reference",
                "description": "Reference to the record of the formal adoption or enactment decision.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-004"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Authority, mandate and adoption are carried as references to party records and decision records owned by other models; reproducing them here would duplicate externally owned evidence and drift toward owning an approval audit trail that this model explicitly disclaims."
          }
        },
        {
          "bundle": {
            "id": "authority-and-applicability",
            "name": "Authority and applicability",
            "description": "Who issued the statement, under what mandate, who now owns the record, and over what it claims to apply."
          },
          "layer": {
            "id": "applicability-scope",
            "name": "Applicability scope",
            "description": "Where, to whom, to what and under which conditions the statement claims to apply."
          },
          "finding": {
            "id": "subject-target-action-and-context-scope",
            "name": "Subject, target, action and context scope",
            "description": "The parties, resources, actions and contextual conditions that bring the statement into application, expressed as references into models that own those things.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-006",
              "SRC-007"
            ],
            "questions": [
              {
                "id": "q-in-scope-parties",
                "text": "Which parties, roles or subject attributes fall within the statement's application?",
                "kind": "relationship",
                "answer_data": [
                  "party or role reference",
                  "subject attribute selector",
                  "party collection refinement reference"
                ]
              },
              {
                "id": "q-in-scope-targets",
                "text": "Which resources or object classes are the target of each rule slot?",
                "kind": "composition",
                "answer_data": [
                  "target resource reference",
                  "resource collection reference",
                  "per-slot target mapping"
                ]
              },
              {
                "id": "q-governed-actions",
                "text": "Which actions or operations does each rule slot govern, and from which action vocabulary?",
                "kind": "interoperability",
                "answer_data": [
                  "action code",
                  "action vocabulary reference",
                  "action implication set"
                ]
              },
              {
                "id": "q-context-conditions",
                "text": "Which environmental or contextual conditions must hold for the statement to be applicable?",
                "kind": "constraint",
                "answer_data": [
                  "context condition reference",
                  "environment attribute selector"
                ]
              },
              {
                "id": "q-governed-artefacts",
                "text": "Which processes, systems or datasets declare themselves governed by this statement?",
                "kind": "relationship",
                "answer_data": [
                  "governed item reference",
                  "declaring model identifier",
                  "edge direction note"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-in-scope-party",
                "name": "in-scope party reference",
                "description": "Reference to a party, role or attribute selector in application scope.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-002"
                ]
              },
              {
                "id": "de-in-scope-target",
                "name": "in-scope target reference",
                "description": "Reference to a resource or resource collection targeted by a rule slot.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              },
              {
                "id": "de-governed-action",
                "name": "governed action code",
                "description": "Coded action governed by a rule slot, drawn from a named action vocabulary.",
                "value_kind": "code",
                "cardinality": "1..n",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-002"
                ]
              },
              {
                "id": "de-context-condition-reference",
                "name": "applicability context reference",
                "description": "Reference to a contextual or environmental condition record.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-003",
                  "SRC-007"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Scope is a set of typed references into party, resource, action-vocabulary and process models that own those entities; materialising them as a local artifact would copy master data this model explicitly places out of scope."
          }
        },
        {
          "bundle": {
            "id": "normative-content-and-composition",
            "name": "Normative content and composition",
            "description": "The internal structure of the statement, how it composes into and inherits from larger statements, and how it binds to externally owned condition expressions and defined terms."
          },
          "layer": {
            "id": "rule-structure-and-composition",
            "name": "Rule structure and composition",
            "description": "Rule-slot inventory, atomicity, containment in policy sets and inheritance from parent statements."
          },
          "finding": {
            "id": "rule-slot-inventory-and-atomicity",
            "name": "Rule-slot inventory and atomicity",
            "description": "The complete set of rule slots a statement contains, whether each is atomic, and which duties, remedies or consequences attach to them.",
            "source_refs": [
              "SRC-001",
              "SRC-002"
            ],
            "questions": [
              {
                "id": "q-slot-inventory",
                "text": "What is the complete inventory of rule slots the statement contains, and is each one atomic?",
                "kind": "composition",
                "answer_data": [
                  "rule slot list",
                  "atomicity status per slot",
                  "slot identifier"
                ]
              },
              {
                "id": "q-minimum-slot-requirement",
                "text": "Must the statement contain at least one rule slot to be valid?",
                "kind": "requirement",
                "answer_data": [
                  "minimum cardinality rule",
                  "validity consequence of an empty statement"
                ]
              },
              {
                "id": "q-compact-expansion",
                "text": "How is a compact statement expanded into atomic rule slots without changing meaning?",
                "kind": "process",
                "answer_data": [
                  "shared property list",
                  "expansion rule reference",
                  "expanded slot set"
                ]
              },
              {
                "id": "q-attached-duties",
                "text": "Which duties, remedies or consequences attach to a given permission or prohibition slot?",
                "kind": "relationship",
                "answer_data": [
                  "attached duty reference",
                  "attachment role code",
                  "chained consequence reference"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-rule-slot",
                "name": "rule slot",
                "description": "A single normative slot with modality, action, target and party function.",
                "value_kind": "collection",
                "cardinality": "1..n",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-002"
                ]
              },
              {
                "id": "de-rule-slot-identifier",
                "name": "rule slot identifier",
                "description": "Identifier of an individual rule slot within the statement.",
                "value_kind": "identifier",
                "cardinality": "1..n",
                "required": true,
                "source_refs": [
                  "SRC-002"
                ]
              },
              {
                "id": "de-attached-duty-reference",
                "name": "attached duty reference",
                "description": "Reference to a duty, remedy or consequence attached to a slot.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "The rule-slot inventory is the structured body of the statement record itself and is answered entirely from inline structured fields; the rendered form of that body is already covered by the consolidated expression artifact under version identity."
          }
        },
        {
          "bundle": {
            "id": "normative-content-and-composition",
            "name": "Normative content and composition",
            "description": "The internal structure of the statement, how it composes into and inherits from larger statements, and how it binds to externally owned condition expressions and defined terms."
          },
          "layer": {
            "id": "rule-structure-and-composition",
            "name": "Rule structure and composition",
            "description": "Rule-slot inventory, atomicity, containment in policy sets and inheritance from parent statements."
          },
          "finding": {
            "id": "policy-set-containment-and-inheritance",
            "name": "Policy-set containment and inheritance",
            "description": "How the statement nests inside larger policy sets and inherits rules or properties from parent statements without circularity.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-010"
            ],
            "questions": [
              {
                "id": "q-containment-path",
                "text": "Is the statement contained in a larger policy set, and what is the containment path?",
                "kind": "composition",
                "answer_data": [
                  "containing set reference",
                  "containment path",
                  "containment depth"
                ]
              },
              {
                "id": "q-inheritance-parents",
                "text": "From which parent statements does this one inherit rules or properties?",
                "kind": "relationship",
                "answer_data": [
                  "parent statement reference",
                  "inherited property list"
                ]
              },
              {
                "id": "q-circularity-check",
                "text": "How is circularity in the inheritance graph prevented and detected?",
                "kind": "validation",
                "answer_data": [
                  "acyclicity assertion",
                  "detection method reference",
                  "detected cycle record"
                ]
              },
              {
                "id": "q-non-inherited",
                "text": "Which parent properties are explicitly not transferred to the child statement?",
                "kind": "constraint",
                "answer_data": [
                  "non-inherited property code",
                  "exclusion basis note"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-containing-set-reference",
                "name": "containing policy set reference",
                "description": "Reference to a policy set that contains this statement.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-002"
                ]
              },
              {
                "id": "de-inherit-from-reference",
                "name": "inherit-from reference",
                "description": "Reference to a parent statement from which rules or properties are inherited.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              },
              {
                "id": "de-non-inherited-property",
                "name": "non-inherited property code",
                "description": "Property explicitly excluded from inheritance.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Containment and inheritance are graph edges between statement records; they are fully answerable from inline reference fields and an acyclicity assertion, and materialising the resolved graph would be a derived view rather than a governed artifact."
          }
        },
        {
          "bundle": {
            "id": "normative-content-and-composition",
            "name": "Normative content and composition",
            "description": "The internal structure of the statement, how it composes into and inherits from larger statements, and how it binds to externally owned condition expressions and defined terms."
          },
          "layer": {
            "id": "condition-binding-and-interpretation",
            "name": "Condition binding and interpretation",
            "description": "References to externally owned condition expressions, the parameter values this subject sets, and the vocabulary that fixes the meaning of terms."
          },
          "finding": {
            "id": "constraint-expression-binding",
            "name": "Constraint expression binding",
            "description": "How each rule slot points at a constraint or rule expression owned by the referenced constraint model, and what binding metadata travels with the pointer.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-006"
            ],
            "questions": [
              {
                "id": "q-bound-expression",
                "text": "Which externally owned constraint or rule expression does each rule slot bind to?",
                "kind": "relationship",
                "answer_data": [
                  "constraint expression reference",
                  "owning model identifier",
                  "binding cardinality"
                ]
              },
              {
                "id": "q-binding-point",
                "text": "At which binding point does the expression attach: rule condition, action refinement, or collection refinement?",
                "kind": "composition",
                "answer_data": [
                  "binding point code",
                  "attachment target identifier"
                ]
              },
              {
                "id": "q-expression-language",
                "text": "Which expression language and version is the referenced constraint written in?",
                "kind": "interoperability",
                "answer_data": [
                  "expression language reference",
                  "language version",
                  "profile identifier"
                ]
              },
              {
                "id": "q-unresolved-reference",
                "text": "What happens to the statement when a referenced expression is unavailable or not understood?",
                "kind": "exception",
                "answer_data": [
                  "unresolved reference handling code",
                  "fail-closed or fail-open declaration",
                  "escalation contact reference"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-constraint-expression-reference",
                "name": "constraint expression reference",
                "description": "Pointer to an expression record owned by the referenced constraint model.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-002"
                ]
              },
              {
                "id": "de-binding-point",
                "name": "binding point code",
                "description": "Where the referenced expression attaches within the rule slot.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              },
              {
                "id": "de-unresolved-reference-handling",
                "name": "unresolved reference handling code",
                "description": "Declared behaviour when a bound expression cannot be resolved or understood.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "This finding deliberately carries only pointers and binding metadata. The constraint expression, its operators, operands and logical composition are owned by WM-KNW-013, so declaring an expression artifact here would reproduce a target model's content and violate the reference boundary."
          }
        },
        {
          "bundle": {
            "id": "precedence-conflict-and-exceptions",
            "name": "Precedence, conflict and exceptions",
            "description": "How the statement declares its precedence relative to other statements, how conflicts are named, and which derogations and open interpretations are on record."
          },
          "layer": {
            "id": "precedence-and-conflict-declaration",
            "name": "Precedence and conflict declaration",
            "description": "Declared strategy identifiers and pairwise superiority relations that determine which statement prevails."
          },
          "finding": {
            "id": "combining-and-hit-policy-declaration",
            "name": "Combining and hit-policy declaration",
            "description": "The strategy identifier the statement declares for reconciling multiple applicable rule slots, and where the normative definition of that strategy lives.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-006"
            ],
            "questions": [
              {
                "id": "q-declared-strategy",
                "text": "Which combining or hit-policy strategy identifier does the statement declare for its rule slots?",
                "kind": "decision",
                "answer_data": [
                  "strategy identifier",
                  "strategy family code",
                  "scope of the declaration"
                ]
              },
              {
                "id": "q-strategy-definition-owner",
                "text": "Where is the normative definition of that strategy published, and who owns its execution?",
                "kind": "authority",
                "answer_data": [
                  "strategy definition reference",
                  "executing runtime reference",
                  "ownership disclaimer note"
                ]
              },
              {
                "id": "q-order-sensitivity",
                "text": "Is the declared strategy order-sensitive, and if so what fixes the order?",
                "kind": "constraint",
                "answer_data": [
                  "order sensitivity flag",
                  "ordering basis",
                  "ordered slot sequence"
                ]
              },
              {
                "id": "q-conflict-term",
                "text": "Which conflict term applies when a permission and a prohibition both match?",
                "kind": "exception",
                "answer_data": [
                  "conflict term code",
                  "voiding consequence",
                  "merge conflict handling note"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-combining-strategy-identifier",
                "name": "combining strategy identifier",
                "description": "Declared identifier of the combining or hit-policy strategy.",
                "value_kind": "identifier",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-002",
                  "SRC-006"
                ]
              },
              {
                "id": "de-strategy-definition-reference",
                "name": "strategy definition reference",
                "description": "Pointer to the specification defining the declared strategy.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-002"
                ]
              },
              {
                "id": "de-conflict-term",
                "name": "conflict term code",
                "description": "Declared policy-level conflict resolution term.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "These are coded declarations pointing at strategies defined in external specifications. The evaluation that applies a combining algorithm or hit policy belongs to a referenced decision runtime, so this model produces no artifact and asserts no execution semantics here."
          }
        },
        {
          "bundle": {
            "id": "precedence-conflict-and-exceptions",
            "name": "Precedence, conflict and exceptions",
            "description": "How the statement declares its precedence relative to other statements, how conflicts are named, and which derogations and open interpretations are on record."
          },
          "layer": {
            "id": "precedence-and-conflict-declaration",
            "name": "Precedence and conflict declaration",
            "description": "Declared strategy identifiers and pairwise superiority relations that determine which statement prevails."
          },
          "finding": {
            "id": "override-and-superiority-relations",
            "name": "Override and superiority relations",
            "description": "Pairwise precedence between this statement and others, the ground on which precedence rests, and what is recorded when nothing resolves a conflict.",
            "source_refs": [
              "SRC-003",
              "SRC-012"
            ],
            "questions": [
              {
                "id": "q-override-edges",
                "text": "Which other statements does this one override, and which override it?",
                "kind": "relationship",
                "answer_data": [
                  "overrides reference",
                  "overridden-by reference",
                  "edge scope"
                ]
              },
              {
                "id": "q-override-ground",
                "text": "On what declared ground does an override rest, such as specificity, recency or hierarchy of authority?",
                "kind": "authority",
                "answer_data": [
                  "override ground code",
                  "supporting authority reference"
                ]
              },
              {
                "id": "q-precedence-acyclicity",
                "text": "Is the resulting precedence graph acyclic, and how is that checked?",
                "kind": "validation",
                "answer_data": [
                  "acyclicity assertion",
                  "check method reference",
                  "detected cycle list"
                ]
              },
              {
                "id": "q-unresolved-conflict",
                "text": "What is recorded when a conflict is detected but no superiority relation resolves it?",
                "kind": "exception",
                "answer_data": [
                  "unresolved conflict record",
                  "escalation route reference",
                  "interim handling note"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-overrides-reference",
                "name": "overrides reference",
                "description": "Statement over which this one takes precedence.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-003"
                ]
              },
              {
                "id": "de-overridden-by-reference",
                "name": "overridden-by reference",
                "description": "Statement that takes precedence over this one.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-003"
                ]
              },
              {
                "id": "de-override-ground",
                "name": "override ground code",
                "description": "Declared basis for the superiority relation.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-003"
                ]
              },
              {
                "id": "de-unresolved-conflict-record",
                "name": "unresolved conflict record",
                "description": "Record naming a detected but unresolved conflict and its escalation route.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-003",
                  "SRC-012"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Superiority relations are typed edges between statement records with a declared ground; they are answered from inline reference fields, and the model records rather than resolves conflicts, so no adjudication document is produced."
          }
        },
        {
          "bundle": {
            "id": "precedence-conflict-and-exceptions",
            "name": "Precedence, conflict and exceptions",
            "description": "How the statement declares its precedence relative to other statements, how conflicts are named, and which derogations and open interpretations are on record."
          },
          "layer": {
            "id": "exceptions-and-open-interpretations",
            "name": "Exceptions and open interpretations",
            "description": "Registered derogations from the statement and formally recorded competing readings of it."
          },
          "finding": {
            "id": "derogation-and-waiver-declaration",
            "name": "Derogation and waiver declaration",
            "description": "Registered exceptions, waivers and derogations from the statement, their granting authority, scope, period and compensating obligations.",
            "source_refs": [
              "SRC-001",
              "SRC-003",
              "SRC-013"
            ],
            "questions": [
              {
                "id": "q-registered-derogations",
                "text": "Which exceptions, waivers or derogations from this statement are currently registered?",
                "kind": "exception",
                "answer_data": [
                  "derogation record reference",
                  "affected rule slot reference",
                  "derogation status"
                ]
              },
              {
                "id": "q-granting-authority",
                "text": "Which authority may grant a derogation, and is that authority distinct from the issuer?",
                "kind": "authority",
                "answer_data": [
                  "granting authority reference",
                  "distinctness assertion",
                  "granting mandate reference"
                ]
              },
              {
                "id": "q-derogation-scope-and-period",
                "text": "For which parties, resources or period does each derogation hold?",
                "kind": "temporal",
                "answer_data": [
                  "beneficiary reference",
                  "scope selector",
                  "validity interval"
                ]
              },
              {
                "id": "q-compensating-obligation",
                "text": "Which compensating obligation or remedy attaches to a granted derogation?",
                "kind": "requirement",
                "answer_data": [
                  "compensating obligation reference",
                  "remedy description",
                  "monitoring pointer"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-derogation-record-reference",
                "name": "derogation record reference",
                "description": "Reference to a registered derogation, waiver or exception.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-003",
                  "SRC-013"
                ]
              },
              {
                "id": "de-granting-authority",
                "name": "granting authority reference",
                "description": "Party empowered to grant the derogation.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-003"
                ]
              },
              {
                "id": "de-derogation-validity-interval",
                "name": "derogation validity interval",
                "description": "Start and end instants over which the derogation holds.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-009",
                  "SRC-003"
                ]
              },
              {
                "id": "de-compensating-obligation",
                "name": "compensating obligation reference",
                "description": "Obligation attached as a condition of the derogation.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "derogation-instrument",
                "name": "Granted derogation or waiver instrument",
                "description": "The instrument by which a competent authority grants a time-bounded exception from named rule slots, with its scope and any compensating obligations.",
                "media_or_form": [
                  "signed instrument",
                  "register entry",
                  "structured decision record"
                ],
                "serial": true,
                "identity_strategy": "Authoritative derogation register number issued by the granting authority's system of record; otherwise a governed IRI minted for the derogation; otherwise a ULID minted by the adopting Dimension with the fallback reason recorded.",
                "source_refs": [
                  "SRC-003",
                  "SRC-013"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "precedence-conflict-and-exceptions",
            "name": "Precedence, conflict and exceptions",
            "description": "How the statement declares its precedence relative to other statements, how conflicts are named, and which derogations and open interpretations are on record."
          },
          "layer": {
            "id": "exceptions-and-open-interpretations",
            "name": "Exceptions and open interpretations",
            "description": "Registered derogations from the statement and formally recorded competing readings of it."
          },
          "finding": {
            "id": "declared-conflicts-and-alternatives",
            "name": "Declared conflicts and alternative interpretations",
            "description": "Competing readings, known contradictions and semantic gaps recorded against the statement so that consumers are not misled into assuming settled meaning.",
            "source_refs": [
              "SRC-003",
              "SRC-012"
            ],
            "questions": [
              {
                "id": "q-recorded-alternatives",
                "text": "Which competing interpretations of the statement are formally recorded as alternatives?",
                "kind": "quality",
                "answer_data": [
                  "alternative interpretation record",
                  "proposing party reference",
                  "status of the alternative"
                ]
              },
              {
                "id": "q-known-contradictions",
                "text": "Which contradictions with other statements are identified but not yet resolved?",
                "kind": "validation",
                "answer_data": [
                  "contradicting statement reference",
                  "contradiction description",
                  "resolution owner reference"
                ]
              },
              {
                "id": "q-semantic-gaps",
                "text": "Which parts of the applicable standard's semantics are non-normative or incomplete for this statement?",
                "kind": "interoperability",
                "answer_data": [
                  "semantic gap note",
                  "affected standard reference",
                  "claim limitation"
                ]
              },
              {
                "id": "q-interpretation-decision",
                "text": "Who decides between recorded alternatives, and how is that decision captured?",
                "kind": "decision",
                "answer_data": [
                  "deciding authority reference",
                  "interpretation decision reference",
                  "effective instant of the decision"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-alternative-interpretation",
                "name": "alternative interpretation record",
                "description": "A recorded competing reading with its proposer and status.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-003"
                ]
              },
              {
                "id": "de-known-contradiction-note",
                "name": "known contradiction note",
                "description": "Narrative record of an unresolved contradiction with another statement.",
                "value_kind": "text",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-003",
                  "SRC-012"
                ]
              },
              {
                "id": "de-semantic-gap-note",
                "name": "semantic gap note",
                "description": "Recorded incompleteness in an aligned standard's semantics.",
                "value_kind": "text",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-012"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Alternatives, contradictions and semantic gaps are narrative and reference annotations attached to the statement record; they are consumed as inline caveats and would lose their binding to the specific rule slot if separated into a standalone document."
          }
        },
        {
          "bundle": {
            "id": "lifecycle-time-and-provenance",
            "name": "Lifecycle, time and provenance",
            "description": "How the statement record moves through its states, over which intervals it is in force and efficacious, and where its content came from."
          },
          "layer": {
            "id": "lifecycle-and-supersession",
            "name": "Lifecycle and supersession",
            "description": "Permitted states of the statement record and the amendment, replacement and repeal relations between statements."
          },
          "finding": {
            "id": "policy-lifecycle-state-model",
            "name": "Statement lifecycle state model",
            "description": "The permitted lifecycle states of the statement record, the transitions between them, and which transitions depend on an external approval decision.",
            "source_refs": [
              "SRC-003",
              "SRC-004",
              "SRC-013"
            ],
            "questions": [
              {
                "id": "q-permitted-states",
                "text": "What are the permitted lifecycle states of the statement record, from draft to repealed?",
                "kind": "lifecycle",
                "answer_data": [
                  "lifecycle state code",
                  "state definition",
                  "terminal state list"
                ]
              },
              {
                "id": "q-transition-approvals",
                "text": "Which transitions are permitted, and which require an external approval decision?",
                "kind": "state",
                "answer_data": [
                  "permitted transition pair",
                  "approval requirement flag",
                  "approval decision reference"
                ]
              },
              {
                "id": "q-suspension-effect",
                "text": "How is suspension recorded, and what does it change about applicability while it lasts?",
                "kind": "process",
                "answer_data": [
                  "suspension record",
                  "suspension interval",
                  "applicability effect note"
                ]
              },
              {
                "id": "q-dated-events",
                "text": "Which lifecycle events must carry a date, and which are merely recorded?",
                "kind": "event",
                "answer_data": [
                  "event type code",
                  "date requirement flag",
                  "recorded event instant"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-lifecycle-state",
                "name": "lifecycle state code",
                "description": "Current state of the statement record.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-004",
                  "SRC-013"
                ]
              },
              {
                "id": "de-permitted-transition",
                "name": "permitted transition",
                "description": "Allowed from-state to to-state pair with any approval requirement.",
                "value_kind": "collection",
                "cardinality": "1..n",
                "required": true,
                "source_refs": [
                  "SRC-004"
                ]
              },
              {
                "id": "de-suspension-record",
                "name": "suspension record",
                "description": "Recorded suspension with its interval and granting authority.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-003"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Lifecycle states and transitions are structured state data on the statement record. The approval decisions that authorise transitions live in decision records owned elsewhere, and this model references them rather than reproducing an approval dossier."
          }
        },
        {
          "bundle": {
            "id": "lifecycle-time-and-provenance",
            "name": "Lifecycle, time and provenance",
            "description": "How the statement record moves through its states, over which intervals it is in force and efficacious, and where its content came from."
          },
          "layer": {
            "id": "lifecycle-and-supersession",
            "name": "Lifecycle and supersession",
            "description": "Permitted states of the statement record and the amendment, replacement and repeal relations between statements."
          },
          "finding": {
            "id": "amendment-supersession-and-repeal",
            "name": "Amendment, supersession and repeal",
            "description": "Which statements this one amends, replaces or repeals, at what provision granularity, and what a processor must do when replacement is declared.",
            "source_refs": [
              "SRC-001",
              "SRC-003",
              "SRC-004",
              "SRC-011"
            ],
            "questions": [
              {
                "id": "q-modification-targets",
                "text": "Which statements does this one amend, replace or repeal, and at which provision granularity?",
                "kind": "relationship",
                "answer_data": [
                  "amended statement reference",
                  "affected provision anchor",
                  "modification scope"
                ]
              },
              {
                "id": "q-amending-instrument",
                "text": "Which amending instrument produced the current consolidated expression?",
                "kind": "provenance",
                "answer_data": [
                  "amending instrument reference",
                  "application instant",
                  "consolidation note"
                ]
              },
              {
                "id": "q-replacement-obligation",
                "text": "What must a processor do when the statement declares that it has been replaced?",
                "kind": "requirement",
                "answer_data": [
                  "replacement handling rule",
                  "replacement target reference",
                  "voiding consequence"
                ]
              },
              {
                "id": "q-partial-versus-full-repeal",
                "text": "How is a partial repeal distinguished from a full repeal in the record?",
                "kind": "classification",
                "answer_data": [
                  "modification type code",
                  "repealed provision list",
                  "residual validity note"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-amends-reference",
                "name": "amends reference",
                "description": "Statement amended, replaced or repealed by this one.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-004",
                  "SRC-011"
                ]
              },
              {
                "id": "de-replaced-by-reference",
                "name": "replaced-by reference",
                "description": "Statement that replaces this one.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-011"
                ]
              },
              {
                "id": "de-modification-type",
                "name": "modification type code",
                "description": "Amendment, partial repeal, full repeal or consolidation.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-004"
                ]
              },
              {
                "id": "de-affected-provision-anchor",
                "name": "affected provision anchor",
                "description": "Pointer to the specific provision changed by a modification.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-004",
                  "SRC-003"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "amending-instrument",
                "name": "Amending or repealing instrument",
                "description": "The instrument that changes or removes provisions of a statement, carrying the modification set and the provisions it affects.",
                "media_or_form": [
                  "legislative or directive instrument",
                  "structured modification set",
                  "published amendment record"
                ],
                "serial": true,
                "identity_strategy": "Authoritative instrument identifier issued by the enacting or publishing system of record; otherwise the governed instrument IRI; otherwise a UUID minted by the adopting Dimension with the fallback reason recorded.",
                "source_refs": [
                  "SRC-004",
                  "SRC-011"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "lifecycle-time-and-provenance",
            "name": "Lifecycle, time and provenance",
            "description": "How the statement record moves through its states, over which intervals it is in force and efficacious, and where its content came from."
          },
          "layer": {
            "id": "temporal-validity",
            "name": "Temporal validity",
            "description": "The intervals over which the statement is in force, efficacious and applicable, and the separation of event time from record time."
          },
          "finding": {
            "id": "validity-intervals-and-record-time",
            "name": "Validity intervals and record time",
            "description": "Distinct in-force, efficacy and applicability intervals, expressed as RFC 3339 instants, with event time kept separate from observation or ingestion time.",
            "source_refs": [
              "SRC-003",
              "SRC-004",
              "SRC-009",
              "SRC-010"
            ],
            "questions": [
              {
                "id": "q-entry-into-force",
                "text": "When does the statement enter into force, and is that distinct from when it was adopted?",
                "kind": "temporal",
                "answer_data": [
                  "entry-into-force instant",
                  "adoption instant",
                  "distinctness note"
                ]
              },
              {
                "id": "q-efficacy-interval",
                "text": "Over which interval is the statement efficacious, and can efficacy begin after entry into force?",
                "kind": "state",
                "answer_data": [
                  "efficacy start instant",
                  "efficacy end instant",
                  "deferred efficacy note"
                ]
              },
              {
                "id": "q-applicability-interval",
                "text": "To which facts or periods does the statement apply, as distinct from when it is in force?",
                "kind": "constraint",
                "answer_data": [
                  "applicability interval",
                  "retroactivity flag",
                  "transitional provision reference"
                ]
              },
              {
                "id": "q-event-versus-record-time",
                "text": "What is the observation or ingestion instant at which each dated occurrence was captured in the register?",
                "kind": "provenance",
                "answer_data": [
                  "event time",
                  "record ingestion time",
                  "capturing system reference"
                ]
              },
              {
                "id": "q-unknown-offset",
                "text": "How is an instant with an unknown local offset represented without falsely asserting UTC local time?",
                "kind": "requirement",
                "answer_data": [
                  "offset-known flag",
                  "negative-zero offset usage rule",
                  "ordering basis code"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-entry-into-force-instant",
                "name": "entry-into-force instant",
                "description": "RFC 3339 instant at which the statement enters into force.",
                "value_kind": "timestamp",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-003",
                  "SRC-009"
                ]
              },
              {
                "id": "de-efficacy-interval",
                "name": "efficacy interval",
                "description": "Start and end instants over which the statement is efficacious.",
                "value_kind": "object",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-003",
                  "SRC-004"
                ]
              },
              {
                "id": "de-applicability-interval",
                "name": "applicability interval",
                "description": "Period of facts to which the statement applies, which may precede entry into force.",
                "value_kind": "object",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-003"
                ]
              },
              {
                "id": "de-record-ingestion-time",
                "name": "record ingestion time",
                "description": "Instant at which the register captured the occurrence, distinct from event time.",
                "value_kind": "timestamp",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-009",
                  "SRC-010"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Validity intervals and timestamps are scalar and interval values on the statement record; they are consumed by point-in-time resolution and carry no rendered form, so no artifact is declared and none is required to answer the questions."
          }
        }
      ],
      "functions": [
        {
          "id": "register-normative-statement",
          "name": "Register a normative statement",
          "description": "Create a governed record for a normative statement with an identifier, an issuing authority, an instrument genre and at least one rule slot.",
          "inputs": [
            "draft statement content or reference",
            "issuing authority reference",
            "instrument genre code",
            "jurisdiction reference",
            "initial rule slot set"
          ],
          "outputs": [
            "registered statement record",
            "assigned master identifier or minted fallback identifier",
            "initial lifecycle state"
          ],
          "preconditions": [
            "An issuing authority reference resolves in the party model",
            "At least one rule slot with a deontic modality and a governed action is supplied",
            "The identity priority has been applied and any fallback reason recorded"
          ],
          "effects": [
            "Statement identifier is reserved and made resolvable",
            "Adoption event time and register ingestion time are recorded separately",
            "Provenance attribution for the initial expression is recorded"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-003",
            "SRC-008",
            "SRC-011"
          ]
        },
        {
          "id": "issue-version-expression",
          "name": "Issue a new version expression",
          "description": "Create a new dated expression of an existing statement work and link it to the expression it supersedes.",
          "inputs": [
            "work identifier",
            "changed content",
            "modification type code",
            "effective instants"
          ],
          "outputs": [
            "new expression record with version designator",
            "supersession link",
            "new record UUID and last-modified instant"
          ],
          "preconditions": [
            "The work identifier resolves",
            "The prior expression is in a state that permits supersession",
            "The modification type is declared"
          ],
          "effects": [
            "Prior expression is marked superseded with an end of currency",
            "Work identifier remains stable across expressions",
            "Point-in-time resolution over the version chain becomes possible"
          ],
          "source_refs": [
            "SRC-002",
            "SRC-004",
            "SRC-010",
            "SRC-011"
          ]
        },
        {
          "id": "declare-applicability-scope",
          "name": "Declare applicability scope",
          "description": "Record the jurisdictions, parties, targets, actions and contextual conditions that bring the statement into application.",
          "inputs": [
            "jurisdiction references",
            "party and target references",
            "governed action codes",
            "context condition references"
          ],
          "outputs": [
            "applicability scope declaration attached to the statement or a named rule slot"
          ],
          "preconditions": [
            "Referenced party, resource, action-vocabulary and context records resolve in their owning models",
            "Subject-matter competence is within the issuing authority's mandate"
          ],
          "effects": [
            "Scope becomes queryable without copying party or resource master data",
            "Overlapping jurisdictional claims are surfaced for precedence declaration"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-003",
            "SRC-011"
          ]
        },
        {
          "id": "bind-constraint-reference",
          "name": "Bind a constraint expression reference",
          "description": "Attach a reference to an externally owned constraint or rule expression at a named binding point, with its expression language and unresolved-reference handling.",
          "inputs": [
            "rule slot identifier",
            "constraint expression reference",
            "binding point code",
            "expression language reference"
          ],
          "outputs": [
            "binding record on the rule slot"
          ],
          "preconditions": [
            "The referenced expression resolves in the constraint model",
            "The binding point is valid for the slot type",
            "The expression language is declared with a version"
          ],
          "effects": [
            "The slot gains a resolvable condition pointer without importing any expression grammar",
            "Unresolved-reference handling is fixed before any consumer interprets the slot"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-006"
          ]
        },
        {
          "id": "declare-precedence-and-conflict-strategy",
          "name": "Declare precedence and conflict strategy",
          "description": "Record the combining or hit-policy strategy identifier, the conflict term, and pairwise superiority relations against other statements.",
          "inputs": [
            "strategy identifier",
            "conflict term code",
            "superiority relation pairs and grounds"
          ],
          "outputs": [
            "precedence declaration",
            "superiority edge set",
            "acyclicity assertion"
          ],
          "preconditions": [
            "The strategy identifier resolves to a published normative definition",
            "Each superiority relation names a ground and a resolvable counterpart statement"
          ],
          "effects": [
            "Precedence becomes inspectable ahead of any evaluation",
            "Cycles in the precedence graph are detected and recorded as unresolved conflicts",
            "Execution of the declared strategy remains with the referenced decision runtime"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-003",
            "SRC-006"
          ]
        },
        {
          "id": "record-lifecycle-transition",
          "name": "Record a lifecycle transition",
          "description": "Record a transition of the statement record such as approval, publication, entry into force, suspension, amendment or repeal.",
          "inputs": [
            "statement or expression identifier",
            "target lifecycle state",
            "event instant",
            "approval decision reference"
          ],
          "outputs": [
            "updated lifecycle state",
            "dated lifecycle event record"
          ],
          "preconditions": [
            "The transition is in the permitted transition set",
            "Any required approval decision reference resolves",
            "Event instant is RFC 3339 with seconds and an explicit offset"
          ],
          "effects": [
            "Event time and register ingestion time are stored separately",
            "Temporal validity intervals are updated where the transition changes force or efficacy"
          ],
          "source_refs": [
            "SRC-003",
            "SRC-004",
            "SRC-009",
            "SRC-013"
          ]
        },
        {
          "id": "resolve-point-in-time-expression",
          "name": "Resolve the expression applicable at an instant",
          "description": "Given a work identifier and an instant, return the expression that was in force, efficacious or applicable at that instant.",
          "inputs": [
            "work identifier",
            "query instant",
            "temporal dimension selector"
          ],
          "outputs": [
            "applicable expression reference",
            "selected validity interval",
            "gap or ambiguity report"
          ],
          "preconditions": [
            "Superseded expressions are retained and resolvable",
            "Validity intervals are recorded on each expression"
          ],
          "effects": [
            "Returns the applicable normative text and never a decision, permission or denial",
            "Records any temporal gap or overlap encountered during resolution"
          ],
          "source_refs": [
            "SRC-003",
            "SRC-004",
            "SRC-011"
          ]
        },
        {
          "id": "register-derogation",
          "name": "Register a derogation",
          "description": "Record a waiver, exception or derogation from named rule slots, with its granting authority, beneficiaries, period and compensating obligations.",
          "inputs": [
            "affected statement and rule slot references",
            "granting authority reference",
            "beneficiary and scope selectors",
            "validity interval",
            "compensating obligation reference"
          ],
          "outputs": [
            "derogation record",
            "derogation instrument reference",
            "updated exception index on the statement"
          ],
          "preconditions": [
            "The granting authority has a recorded mandate to derogate",
            "The affected rule slots resolve",
            "The validity interval is bounded or its open-endedness is declared"
          ],
          "effects": [
            "The statement exposes its live derogations without altering its own version chain",
            "Expiry of a derogation is a dated event on the derogation record, not on the statement"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-003",
            "SRC-013"
          ]
        },
        {
          "id": "declare-standard-alignment",
          "name": "Declare a standard alignment",
          "description": "Record an alignment to an external standard or profile, with evidence, scope and any semantic divergence, without asserting conformance.",
          "inputs": [
            "aligned standard reference",
            "alignment scope",
            "supporting evidence reference",
            "known divergences"
          ],
          "outputs": [
            "alignment declaration",
            "divergence notes",
            "conformance-versus-alignment flag"
          ],
          "preconditions": [
            "The aligned standard is cited with a version or date",
            "Any conformance claim carries a cited test result or certification"
          ],
          "effects": [
            "Alignment is published as a claim with stated limits rather than as conformance",
            "Unmappable constructs are recorded so downstream projections do not assume fidelity"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-003",
            "SRC-012"
          ]
        }
      ],
      "composition": [
        {
          "target": "WM-POL-001",
          "relation": "CHILD",
          "purpose": "This model is the instance-level normative statement within the parent policy domain, which retains portfolio taxonomy and cross-policy programme governance.",
          "required": true,
          "source_refs": [
            "SRC-002",
            "SRC-013"
          ]
        },
        {
          "target": "WM-KNW-013",
          "relation": "REFERENCE",
          "purpose": "Bind rule slots to constraint or rule expressions owned there. This model carries the reference, the binding point, the expression-language reference and subject-specific parameter values only, and reproduces neither the expression grammar nor that model's lifecycle or operational functions.",
          "required": false,
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-006"
          ]
        },
        {
          "target": "WM-ACT-003",
          "relation": "REFERENCE",
          "purpose": "Carry applicability pointers to governed processes. The governance edge is authored by WM-ACT-003; no activity, task, sequence or execution state is modelled here.",
          "required": false,
          "source_refs": [
            "SRC-006",
            "SRC-007"
          ]
        },
        {
          "target": "WM-XCT-003",
          "relation": "EXTEND",
          "purpose": "Incoming specialisation: projection and disclosure policies specialise this model with output-shape semantics. Generic identity, authority, lifecycle and conflict machinery is retained here per the relation rationale, and output-shape semantics are not modelled here.",
          "required": false,
          "source_refs": [
            "SRC-001",
            "SRC-002"
          ]
        },
        {
          "target": "Referenced decision or enforcement runtime (XACML PDP/PEP or ABAC access decision function)",
          "relation": "REFERENCE",
          "purpose": "Name the runtime that evaluates and enforces this statement. This model owns no evaluation, execution, enforcement or audit-trail semantics and stores no decision result or decision log.",
          "required": false,
          "source_refs": [
            "SRC-002",
            "SRC-007",
            "SRC-012"
          ]
        },
        {
          "target": "Party / Agent model (adopting-Dimension registry target unresolved)",
          "relation": "REFERENCE",
          "purpose": "Resolve issuing authority, adopting body, assigner, assignee, bearer and responsible-party references; party master data is not held here.",
          "required": true,
          "source_refs": [
            "SRC-001",
            "SRC-003",
            "SRC-010"
          ]
        },
        {
          "target": "Resource / Asset model (adopting-Dimension registry target unresolved)",
          "relation": "REFERENCE",
          "purpose": "Resolve rule-slot targets and target collections; resource master data is not held here.",
          "required": false,
          "source_refs": [
            "SRC-001"
          ]
        },
        {
          "target": "Jurisdiction / Place model (adopting-Dimension registry target unresolved)",
          "relation": "REFERENCE",
          "purpose": "Resolve jurisdiction and territorial coverage references used by applicability scope.",
          "required": false,
          "source_refs": [
            "SRC-003",
            "SRC-011"
          ]
        },
        {
          "target": "ODRL Information Model 2.2 (W3C)",
          "relation": "ALIGN",
          "purpose": "Alignment for policy and rule structure, action and target relations, constraint placement, conflict term, inheritFrom and profile conformance. Recorded as alignment, not conformance.",
          "required": false,
          "source_refs": [
            "SRC-001"
          ]
        },
        {
          "target": "XACML 3.0 (OASIS) and LegalRuleML 1.0 (OASIS)",
          "relation": "ALIGN",
          "purpose": "Alignment for policy-set containment, required identifiers and versions, combining algorithm declaration, deontic operators, superiority relations and temporal characteristics. Recorded as alignment, not conformance.",
          "required": false,
          "source_refs": [
            "SRC-002",
            "SRC-003"
          ]
        },
        {
          "target": "Akoma Ntoso 1.0 (OASIS) and European Legislation Identifier (Publications Office of the EU)",
          "relation": "ALIGN",
          "purpose": "Alignment for FRBR work/expression/manifestation identity, IRI naming, dated lifecycle events and point-in-time consolidation.",
          "required": false,
          "source_refs": [
            "SRC-004",
            "SRC-011"
          ]
        },
        {
          "target": "PROV-O (W3C)",
          "relation": "ALIGN",
          "purpose": "Alignment for attribution, derivation, revision, generation and invalidation of statement expressions.",
          "required": false,
          "source_refs": [
            "SRC-008"
          ]
        },
        {
          "target": "SBVR 1.5 (OMG)",
          "relation": "MIX-IN",
          "purpose": "Supplies the alethic-versus-deontic modality distinction, enforcement level as a graded severity scale, and the governed-vocabulary binding used to fix the meaning of terms.",
          "required": false,
          "source_refs": [
            "SRC-005"
          ]
        }
      ],
      "researchAdjudication": {
        "providerMode": "single-provider-waiver",
        "activeProviders": [
          "claude"
        ],
        "waivedProviders": [
          "grok"
        ],
        "providerPolicy": {
          "contract_version": "1.0.0",
          "mode": "single-provider-waiver",
          "effective_at": "2026-08-29T09:06:27Z",
          "scope": "Queued subject-model research from WM-XCT-013 onward",
          "active_providers": [
            "claude"
          ],
          "waived_providers": [
            {
              "provider": "grok",
              "authorized_by": "repository owner",
              "authorized_at": "2026-08-29T09:06:27Z",
              "reason": "The repository owner explicitly instructed the research queue to continue without Grok after repeated structured-output failures."
            }
          ],
          "review_rule": "Claude-only results require a separate no-tools adversarial audit and remain reviewable drafts with a visible single-provider hold."
        },
        "boundaryDecision": {
          "entry_kind": "aggregate",
          "status": "reclassified",
          "rationale": "Two axes must not be conflated. Record plane: the frozen registry value 'standalone-mm' classifies how vr.wm-knw-012 sits in the Vercy registry — a standalone meta-model record rather than a profile or mixin of another record — and is retained unchanged; it is not a subject-model kind and must never be copied into boundary_decision.entry_kind. Subject-model plane: the thing modelled is not a lone identified object but a consistency boundary rooted on the abstract statement work, with dated expressions, contained rule slots and published manifestations that have no independent publication lifecycle of their own. The compatibility rules make removing a rule slot, changing a deontic modality, changing the combining strategy or changing the conflict term breaking at the container version; CRUD forbids creating a statement without at least one rule slot; canonicalization digests ordered slots and bindings as one canonical form; patch rules forbid mutating a published expression in place; and the Dimension layer forbids splitting identifier minting for a single statement work across packages. Those are aggregate-root invariants, so Claude's 'entity' understates the boundary that the service layers actually enforce. Fallback instruction for the synthesizer: if the schema reserves 'aggregate' for multi-model clusters rather than intra-model composition, degrade to 'entity' and carry the composition invariants as an explicit aggregate-root note — do not silently re-adopt the record-plane value."
        },
        "decisions": [
          {
            "concept": "Subject-model entry kind versus frozen registry record-plane value",
            "disposition": "reclassified — entity to aggregate; registry 'standalone-mm' retained on the record plane",
            "rationale": "The registry classifies the record, the boundary decision classifies the subject. Claude's 'entity' is not wrong so much as under-specified: the enforced invariants (minimum one rule slot, slot removal breaking at container version, single minting authority per work, digest over ordered slots) describe an aggregate root over work, expressions, slots and manifestations."
          },
          {
            "concept": "Aggregate root identity — stable work identifier plus per-expression record UUID",
            "disposition": "accepted",
            "rationale": "The declared OSCAL-versus-FRBR conflict is resolved by keeping both a stable work identifier across expressions and a per-expression record UUID, and the identity_priority correctly orders master-system identifier, governed IRI, then minted UUID/ULID with a recorded fallback reason. This is the only coherent root identity for the aggregate and it is stated explicitly rather than assumed."
          },
          {
            "concept": "WM-KNW-013 composition relation — pointer-only constraint binding",
            "disposition": "accepted",
            "rationale": "The frozen contract types this edge REFERENCE even though its free-text rationale says 'Normative composition'; the typed relation prevails over the prose. The constraint-expression-binding finding carries only a bound-expression reference, binding point, expression-language reference and unresolved-reference handling, with a deliberately empty artifacts array, so no expression grammar, operator or operand vocabulary leaks across the boundary."
          },
          {
            "concept": "Appeal to the relation ledger inside parameterization-and-tailoring-values",
            "disposition": "structure accepted; ledger justification rejected and must be re-grounded on SRC-010",
            "rationale": "The inline rationale asserts that 'the relation ledger permits this model to carry subject-specific parameters', but the frozen three-row contract says nothing of the kind. Carrying parameter definitions and set values is independently defensible on OSCAL set-parameter grounds, so the structure survives; the unsupported citation of the ledger must be struck before publication or it invites adopters to over-read the contract."
          },
          {
            "concept": "Governed vocabulary artifact versus out-of-scope operand vocabulary",
            "disposition": "accepted with the boundary line recorded explicitly",
            "rationale": "The out_of_scope list excludes operator and operand vocabularies, yet this model declares a governed vocabulary artifact including a locally held glossary. The distinction holds on SBVR grounds: term and definition vocabulary that fixes the meaning of words used in the statement is bindable here, while operator and operand vocabularies that make a condition evaluable stay with WM-KNW-013. The synthesizer must publish that line, not leave it inferred."
          },
          {
            "concept": "Runtime and decision non-ownership, including resolve-point-in-time-expression",
            "disposition": "accepted",
            "rationale": "No permit/deny result, obligation discharge, decision record or evaluation semantics appears anywhere in the structure or the nine functions. The combining and hit-policy finding declares a strategy identifier and points at where its normative definition lives; q-strategy-definition-owner asks who owns execution rather than executing. The point-in-time resolver returns an expression, not a decision, which is a read operation over the aggregate."
          },
          {
            "concept": "Audit-trail non-ownership under access.audit_requirements",
            "disposition": "accepted",
            "rationale": "Access and lifecycle logging are stated as obligations placed on the adopting Dimension's logging service, disposition audit stays with the retention authority, and identifier-minting provenance is deliberately kept on the record itself so identity does not depend on an external log. No audit entity, event stream or log artifact is declared, so the disclaimed boundary is actually held rather than merely asserted."
          },
          {
            "concept": "access.scopes stated in the record plane (bundle, layer, finding, artifact)",
            "disposition": "deferred — subject-plane mapping required before freeze",
            "rationale": "The default_rule and exceptions gate reads of statements, expressions, normative bodies and derogation instruments, but the scopes enumerate the research-structure planes instead. If the schema fixes that enum, the synthesizer must publish an explicit mapping from work/expression/rule-slot/manifestation onto those four scopes; otherwise adopters will implement access control against the wrong plane."
          },
          {
            "concept": "Retention floor derived from an open-ended applicability window",
            "disposition": "deferred",
            "rationale": "Retention is defined as at least the period needed to reconstruct any instant within the applicability window, but the model itself lists open-ended validity as in scope, which makes the floor unbounded and therefore not schedulable. It also collides with the delegated privacy-erasure path, where this model records that a removal occurred but not the workflow. The declaration is publishable; the unbounded case needs a stated resolution."
          },
          {
            "concept": "serial_naming_rule applied to externally issued instruments",
            "disposition": "deferred — explicit carve-out required for authoritative source, amending and derogation instruments",
            "rationale": "Three of the four serial artifact classes are issued by external publishers or granting authorities that this model explicitly does not own. Prefixing them with the local statement identifier produces a second citation form for an instrument that already has an official one, which sits badly beside q-titles-and-citation and the primary-versus-compilation preference. Identity is unaffected because identity_priority correctly puts the master-system identifier first."
          },
          {
            "concept": "Splitting record-classification-access-and-retention into separate findings",
            "disposition": "deferred to next revision; not a publication blocker",
            "rationale": "One finding with five questions carries classification, publication audience, redaction, retention period and disposition, and is the only finding in its layer while every comparable layer holds two. Retention, disposition class and tombstone are a distinct governance concern from sensitivity and audience, but splitting after freeze churns stable identifiers for no correctness gain in a reviewable draft."
          },
          {
            "concept": "Redaction-with-citability versus the WM-XCT-003 EXTEND boundary",
            "disposition": "accepted with the line stated",
            "rationale": "q-redaction-and-citability edges toward output shaping, which the EXTEND rationale assigns to WM-XCT-003. The defensible line, which the model states and which should be published rather than left implicit, is that redaction permission and residual citability are properties of the record, while redaction transforms and disclosure projections are the specialising model's."
          },
          {
            "concept": "Identifier drift — policy-lifecycle-state-model id versus 'Statement' name, and parameterization/Parameterisation spelling",
            "disposition": "accepted as-is; no post-freeze rename",
            "rationale": "The model was written in en-GB and renamed policy to statement in its finding names, leaving two identifiers behind. These are stable reference keys and renaming them after freeze breaks inbound citations for a purely cosmetic gain, so the drift is recorded in the draft notes rather than corrected."
          },
          {
            "concept": "SRC-012 as structural support (non-normative ODRL Formal Semantics editor's draft)",
            "disposition": "accepted, constrained",
            "rationale": "Both findings citing SRC-012 also cite tier-1 primary SRC-003, so no structural node rests on a non-normative draft alone, which is what the model's own gap policy requires. The constraint must be made explicit in the synthesis so a later revision does not promote SRC-012 to sole support for a precedence or alignment node."
          },
          {
            "concept": "Three-way incompatibility of conflict-resolution models carried unmapped",
            "disposition": "accepted; explicitly not a critical conflict",
            "rationale": "ODRL's static policy-level term, XACML's per-container combining algorithms and LegalRuleML's pairwise superiority relations are genuinely not interchangeable, and the model carries all three separately while asserting no mapping and claiming no conformance. Declaring an unresolved cross-standard divergence honestly is correct modelling, not a defect blocking a reviewable draft."
          },
          {
            "concept": "Missing function surface for classification, retention declaration, tailoring and defect recording",
            "disposition": "deferred — add_functions barred in single-provider mode",
            "rationale": "The policies forbid publishing a statement without a record classification, and the patch rules make parameter tailoring a distinct change type, yet neither has a function; recorded defects and alternative interpretations likewise have none. Proposing function text here would be this auditor inventing content with no second provider to source it against, so the gap is logged for the next research pass instead."
          }
        ],
        "publicationHolds": [
          "Live source and version verification hold: before publication, confirm every accepted source URL resolves and pin a version for the three access-dated entries that currently carry no version token — SRC-010 (OSCAL catalog concepts), SRC-011 (ELI framework pages) and SRC-012 (ODRL Formal Semantics editor's draft, non-normative). Any source that cannot be resolved and pinned must be downgraded and the nodes resting on it re-checked for remaining primary support.",
          "Single-provider hold: every publication artifact must carry a visible notice that this result was produced by Claude alone and received no independent second-provider review, naming the repository owner's waiver of Grok effective 2026-08-29T09:06:27Z and its stated reason (repeated structured-output failures). The artifact stays a reviewable draft, not a validated model, for as long as that waiver stands.",
          "Timestamp-rule verification hold: SRC-009 is registered as RFC 3339 'updated by RFC 9557', but RFC 9557 is not itself a registered source while the canonicalization and artifact timestamp rules depend on the exact unknown-local-offset clause. Either register the updating RFC and confirm the -00:00 convention survives it, or restate the rule against the pinned RFC 3339 text before freezing the hashing rule.",
          "Boundary-review hold: the frozen registry carries status 'candidate' and review_state 'boundary-review-required', and this audit reclassifies the subject-model entry kind from entity to aggregate on the strength of the service-layer invariants. Publication must surface both the outstanding boundary review and the reclassification, so no downstream consumer treats the entry kind as settled.",
          "Paywalled-source hold: SRC-013 (ISO 37301:2021) grounds lifecycle currency, ownership and compliance-boundary claims but is behind a paywall. Confirm that the cited structure is supported by publicly verifiable scope material or by a licensed reading on record; if neither, downgrade the affected notes to partial support rather than leaving an uncheckable tier-1 citation in a public draft.",
          "Independent second-provider review was explicitly waived by the repository owner; this Claude-only result remains a reviewable draft."
        ],
        "deferredResearch": [
          "Multilingual authenticity: equivalence, precedence and divergence between authentic language versions of one statement, and the authority that certifies a translation. Declared as a gap with no cited source fixing the structure; needs a primary source before any structure is invented.",
          "Delegation chains where an authority empowers a subordinate body to issue statements. Only a single mandate-basis reference is modelled, which cannot express multi-step delegated rule-making or the ultra vires consequences of a broken chain.",
          "Retention floor when the applicability window is open-ended, and its interaction with the delegated privacy-erasure path where this model records only that a removal occurred. Needs a resolution rule that keeps point-in-time reconstruction reproducible without asserting unbounded retention.",
          "Function-surface completion for record classification, retention declaration, parameter tailoring and defect or alternative-interpretation recording, each of which is required or distinguished by the service layers but has no function. Deferred because add_functions is barred in single-provider mode and inventing them here would be unsourced.",
          "Customary, religious and indigenous normative orders whose authority structures do not resolve to an identifiable issuing body with a dated enactment, and the related regional assumption that ELI and Akoma Ntoso drafting practice generalises beyond European and Commonwealth orders.",
          "Whether the access scope vocabulary should name subject-plane scopes (work, expression, rule slot, manifestation) or publish an explicit mapping onto the fixed record-plane scopes, and whether record-classification-access-and-retention should split into separate classification and retention findings at the next revision."
        ]
      }
    }
  }
}

```

