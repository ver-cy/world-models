# Frozen no-tools semantic audit — EM-LEG-01

Use only this frozen packet. Do not browse, call tools, invent identifiers, mutate registry reservations or grant publication authority.

Disposition: PROFILE over WM-ECO-006 and WM-XCT-029; no new ID. Audit semantics only.

Return at most 600 words with exactly: Verdict (ACCEPT WITH LIMITS, REVISE, or REJECT); Critical findings; Required holds; Scenario result; Identifier decisions.

## Profile candidate

{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-LEG-01",
  "name": "Enterprise Contract, Obligation and SLA",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": [
    "WM-ECO-006",
    "WM-XCT-029"
  ],
  "constraints": [
    "WM-ECO-006 masters agreement identity, party positions and execution-time occupancy, formation, immutable executed expressions, clause work identifiers, amendments, termination, survival and contract-record governance.",
    "WM-XCT-029 masters each duty's modality, obligor, obligee and enforcer roles, conditions, due basis, fulfilment criteria and progress, outstanding quantity, evidence status, per-duty dispute, breach, cure, excuse, waiver and consequences.",
    "A duty cites stable clause work ID plus exact expression ID and locator; it never restates authoritative clause text beyond controlled-term encoding and an auditable non-normative narrative.",
    "WM-ECO-006 stores no live duty state, quantities, evidence status or per-duty dispute; contract-level avoidance, termination, fundamental-breach classification and exclusive-remedy election reference WM-XCT-029 determinations without restating them.",
    "Every executed expression is immutable with digest, signature package and validation report; an amendment is a new executed child instrument producing a successor expression while signed predecessors and redirects remain resolvable.",
    "A conformed contract text is a derived projection with its own identifier and never overwrites an executed expression.",
    "Execution-time party occupancy is frozen on WM-ECO-006; current obligor is a WM-XCT-029 role binding to the contract position and current occupant.",
    "Delegation or third-party performance neither changes execution occupancy nor discharges the original obligor; transfer, novation and new agreement are typed before occupancy or duty identity changes.",
    "Partial fulfilment accumulates accepted quantity and preserves outstanding quantity as-of; acceptance with reservation, unconditional discharge and provisional disputed performance remain distinct.",
    "Fulfilment evidence records issuer attestation and status under WM-XCT-029 while document or observation payload, digest and custody remain externally mastered; evidence revocation appends reopening without erasing prior acceptance.",
    "Legal-effect time and observation time remain separate on every transition; transition, evidence, acceptance and dispute histories are append-only.",
    "A contractual SLA is an executed WM-ECO-006 clause set plus WM-XCT-029 duties with obligee, enforceable criteria and consequences; an internal SLO, OLA or dashboard metric has no contractual force without executed incorporation.",
    "WM-SFT-016 may later own SLI specification, target, measurement window, observations and error budgets only; it never owns contractual obligees, enforceability, remedies, service credits or breach.",
    "Service credits are typed WM-XCT-029 consequences with regime-qualified class remedy, liquidated-damages, penalty, price-adjustment or other; this profile makes no jurisdictional enforceability conclusion.",
    "Duty dispute remains WM-XCT-029-owned while forum, claim file and adjudication remain external case-model concerns; contested performance blocks automatic disposition.",
    "Contract Amendment, Fulfilment Evidence and SLA have no independent aggregate identity in this contour and create no new catalogue or runtime identifier."
  ],
  "candidateRevision": 2,
  "references": [
    "WM-SFT-016",
    "WM-XCT-028",
    "EM-TEC-06",
    "EM-LEG-05"
  ],
  "holds": [
    "WM-ECO-006 and WM-XCT-029 remain non-canonical reviewable drafts and the profile cannot promote ahead of them.",
    "The field-level crosswalk for obligation, breach/remedy, amendment and evidence overlap is not ratified in the base contracts.",
    "Delegation and third-party-performance typing is missing from WM-ECO-006 change events.",
    "Reserved acceptance versus unconditional discharge and recomputation after revoked evidence require ratified semantics.",
    "WM-SFT-016 remains an uninstalled boundary-review stub and is reference-only.",
    "Writing-form rules, service-credit classification, implied duties, set-off and withholding require governing-regime profiles and primary-source verification.",
    "UBL, FIBO, ODRL, LegalRuleML and ISO/IEC 19086 are alignment targets only, not conformance claims.",
    "Canonical package and live verification remain held."
  ]
}


## Fixtures

{
  "format": "vercy-enterprise-profile-fixtures/v1",
  "profileName": "Enterprise Contract, Obligation and SLA",
  "cases": [
    {
      "id": "two-amendments",
      "kind": "positive",
      "input": "An agreement receives two executed amendments.",
      "expect": "Original and two amendment instruments plus three expressions remain resolvable; clause work IDs persist and affected duties rebind without rewriting predecessors."
    },
    {
      "id": "partial-performance",
      "kind": "positive",
      "input": "An obligor performs part of a quantified duty.",
      "expect": "Accepted quantity accumulates, outstanding quantity remains derivable as-of, and unconditional discharge is not inferred."
    },
    {
      "id": "disputed-sla",
      "kind": "positive",
      "input": "A contractual SLA measurement is challenged.",
      "expect": "WM-XCT-029 keeps a provisional contested state, evidence history and outstanding consequence state while disposition is blocked."
    },
    {
      "id": "delegation",
      "kind": "positive",
      "input": "A third party performs a delegated duty.",
      "expect": "Execution occupancy and original obligor remain; performer is recorded separately unless an authorized transfer or novation occurs."
    },
    {
      "id": "novation",
      "kind": "positive",
      "input": "Parties execute a release-and-substitute novation.",
      "expect": "A successor duty or new agreement is explicitly linked; the old execution snapshot and surviving duties remain resolvable."
    },
    {
      "id": "evidence-revoked",
      "kind": "positive",
      "input": "Fulfilment evidence is revoked after acceptance.",
      "expect": "A status event reopens the duty, prior acceptance stays in the log, outstanding quantity is recomputed from surviving accepted evidence and dispute state persists."
    },
    {
      "id": "service-credit",
      "kind": "positive",
      "input": "A service-level miss triggers a credit.",
      "expect": "A secondary duty records the credit and a governing-regime profile supplies its legal class; no model-level enforceability conclusion is made."
    },
    {
      "id": "internal-slo-as-guarantee",
      "kind": "negative",
      "input": "An internal dashboard SLO is presented as a contractual guarantee without incorporation.",
      "expect": "The inference is rejected because no executed clause, obligee, enforceable criterion or consequence exists."
    },
    {
      "id": "amendment-overwrites",
      "kind": "negative",
      "input": "An amendment overwrites the prior signed expression.",
      "expect": "Validation rejects mutation and requires a new instrument, successor expression and preserved predecessor."
    },
    {
      "id": "delegation-discharges",
      "kind": "negative",
      "input": "Delegation automatically discharges the original obligor and changes execution occupancy.",
      "expect": "Validation rejects both effects without typed transfer, consent or novation."
    },
    {
      "id": "contract-stores-duty-state",
      "kind": "negative",
      "input": "The contract expression stores live outstanding quantity and per-duty dispute state.",
      "expect": "Validation rejects dual mastership; those facts belong to WM-XCT-029."
    },
    {
      "id": "revocation-deletes-acceptance",
      "kind": "negative",
      "input": "Revoked evidence deletes the earlier acceptance event.",
      "expect": "Deletion is rejected and reopening must append."
    },
    {
      "id": "credit-is-always-penalty",
      "kind": "negative",
      "input": "Every service credit is classified as an unenforceable penalty.",
      "expect": "The jurisdiction-free conclusion is rejected and requires a governing-regime profile."
    }
  ]
}


## Local evidence

# EM-LEG-01 local synthesis

## Disposition

- Create an **Enterprise contract, obligation and SLA profile** over WM-ECO-006 and WM-XCT-029.
- Do not create a catalogue/runtime identifier.
- Contract Amendment, Fulfilment Evidence and Service Level Agreement remain owned structures; none proves an independent lifecycle here.

## Ownership boundary

WM-ECO-006 masters the agreement instrument: identity, party positions, formation, execution, clause tree, authentic signed expressions, amendments, termination and contract-record governance. WM-XCT-029 masters each duty: modality, obligor/obligee, antecedent, due basis, fulfilment criteria, progress, evidence status, breach, cure and consequence obligations.

The contract derives obligation records from stable clause work identifiers. It never writes obligation state. The obligation references its source clause but never becomes a second store for normative clause text.

Per-obligation non-performance belongs to WM-XCT-029. Contract-level fundamental breach, avoidance, termination and remedy election belong to WM-ECO-006 and reference the underlying determinations.

## SLA/SLO rule

A contractual SLA is an executed clause set plus directed obligations with an obligee, enforceable performance criteria and contractual consequences. An operational SLO is a target sourced from internal policy or operational governance. It has no contractual force unless an executed agreement or amendment incorporates it.

Reserved candidate WM-SFT-016 may later own metric/SLO definitions, observations and error budgets. It must not own contractual obligees, enforceability, remedies or breach. EM-LEG-01 cannot depend on it while its boundary remains under review.

## Invariants

1. Party identity and authority evidence are pinned at execution time; later changes never overwrite history.
2. An amendment creates a new expression and preserves signed predecessors.
3. Amendment, novation and a new contract are distinct: term change, released party substitution and new agreement identity respectively.
4. Every obligation has an obligor, action/forbearance and fulfilment criterion.
5. Partial fulfilment accumulates and leaves an explicit outstanding quantity.
6. Evidence revocation appends a reopening transition; it never edits prior acceptance or fulfilment findings.
7. Contested performance is explicit, blocks disposition and cannot auto-resolve.
8. No target becomes a contractual guarantee without a source clause, obligee and enforcing party.

## Acceptance result

Expressions E1, E2 and E3 preserve the original agreement and two amendments. Changed clauses invalidate and rederive affected obligations without erasing prior versions. Partial performance remains measurable and incomplete. A disputed SLA observation stays provisional with its evidence and challenge history. The internal-SLO negative case is rejected because it lacks contractual incorporation and counterparty enforcement.

## Holds

Both parents remain `publishableCanonical: false`. SLA semantics rely on an under-grounded performance-standard finding; the WM-SFT-016 boundary is unresolved; relations and field-level crosswalks across obligation, breach/remedy, amendment and evidence remain unapproved. Jurisdiction-specific treatment of implied terms, service credits, set-off and penalties requires legal review. This checkpoint is not an installable release.


## Claude study

## Verdict

**PROFILE.** EM‑LEG‑01 is fully served by composing two already‑reserved entries: **WM‑ECO‑006 Commercial Contract** (aggregate) as the host instrument and **WM‑XCT‑029 Obligation/Commitment** (mixin) applied per duty. No candidate type in the contour survives the registry test of independent identity plus independent lifecycle, so **no new ID is allocated** — the profile is named (`EM-LEG-01 contract/obligation/SLA profile`) and carries no registry_id. Pure REUSE ONLY is not sufficient: the two models overlap on breach, remedy, amendment and evidence, and nothing today adjudicates which one writes. That adjudication is the profile's reason to exist.

## Boundary

Single‑writer split, to be asserted normatively by the profile:

- **WM‑ECO‑006 owns the instrument**: agreement identity and instance kind, party positions and occupancy, formation, execution and signature evidence, the addressable clause tree and executed‑expression digests, precedence and authentic language, amendment instruments and consolidated expressions, termination and survival, retention/disposition of the record.
- **WM‑XCT‑029 owns the duty**: modality and violability, bearer/obligee/beneficiary roles for one commitment, antecedent and detachment, due basis, lifecycle states with dual timestamps, fulfilment criteria and quantity accumulation, fulfilment evidence and its status, per‑obligation breach determination, excuse, cure and secondary obligations.
- **The seam**: ECO‑006 `derive-obligation-set` emits records that mix in XCT‑029; the link is `clauseWorkId` ↔ `source-citation`, so an obligation survives renumbering. ECO‑006 never stores obligation state; XCT‑029 never stores clause text beyond the auditable `action-narrative` extract.
- **Breach is two‑level and must not double‑chain.** XCT‑029 declares non‑performance of one duty. ECO‑006 owns contract‑level consequences — fundamental‑breach classification, Nachfrist, avoidance, termination. Profile rule: at most one remedy election per contractual claim; ECO‑006's breach record references the XCT‑029 determinations it aggregates and does not restate them.
- **Assignment/novation**: ECO‑006 owns the party‑position change and consent; XCT‑029 owns whether duty identity continues (delegation) or is superseded (release‑and‑substitute).

## SLA/SLO split

A **contractual SLA** is a clause‑set plus a cluster of obligations: `clauseClass = service-level`, XCT‑029 `performance-standard` (threshold, unit, measurement window, method, conformity assessor) with a named obligee, and service credits modelled as XCT‑029 secondary/consequence obligations. An **operational SLO** is a target with no obligee, no enforcing party, no source clause: representable as XCT‑029 with `directedness = at-large`, `origin = voluntary`, `source_kind = internal policy` — or not as an obligation at all, merely a metric.

WM‑SFT‑016 is a **candidate under boundary review** and must be treated as an optional REFERENCE for metric definition, measurement series and error budget only. The profile must be publishable without it, with metric identifier and method held inline under `performance-standard`. Before WM‑SFT‑016 leaves candidate status it must be checked not to carry obligee, enforceability, remedy or breach fields; if it does, that is a boundary conflict with this contour, not a mapping detail.

## Required profile

No new ID; the profile fixes bindings and tightens cardinalities:

1. Elevate to required for the SLA case: `source_instrument_ref` + `source_citation`, `obligee_ref`, `performance_standard_ref` or `threshold_value`, `measurement_method`, `conformity_assessor_ref`.
2. Bind v1 candidate fields as **aliases only** (they remain candidate‑not‑normative): `agreement_number`→`agreementIdentifier`; `agreement_kind`→subject‑matter class; `effective_period`→`effectiveDate`+`endEffectiveTime`; `governing_law`→governing‑law declaration; `obligation_text`→`action-narrative`; `trigger`→`antecedent-expression`; `due_at`→`due-at`; `fulfilment_criteria`→`fulfilment-criteria`.
3. Evidence discipline: ECO‑006 `art-acceptance-certificate` records the obligee's **legal act** of acceptance; XCT‑029 `fulfilment-evidence-package` records the issuer's **attestation**. One underlying document, one digest, two roles, no second chain.
4. Vocabulary: one clause‑class value for service level; one discharge‑mode enumeration; one dispute‑status enumeration shared across both models.

**Aggregate tests.** *ContractAmendment* — no. Identity is agreement id + non‑reusable sequence; no lifecycle apart from the agreement. Serial artifact in ECO‑006. *FulfilmentEvidence* — no. Issuer‑assigned identity and revocation status are the issuer's lifecycle, not the contour's; already owned by XCT‑029. *SLA* — no. An annex addressed by expression IRI plus annex identifier; it cannot be amended, breached or terminated independently of its contract.

## Invariants

1. Party identity is fixed as at signing: `identityVerificationTime ≤ executionTime`; later identity change is an event, never an overwrite; `partyPositionId` persists.
2. An amendment never rewrites signed text: superseded expression retained and addressable, new expression IRI, amendment sequence never reused, work→expression map keeps old citations resolvable.
3. Amendment ≠ novation ≠ new contract: same positions + changed terms = amendment; occupant substituted with release = novation (successor obligation + supersession link); new subject matter or new agreement identifier = new instance with `parentAgreementRef`.
4. Every obligation has bearer, action term and fulfilment criterion; alethic statements are rejected.
5. Partial fulfilment is an accumulation: outstanding quantity derivable at any instant; partial tender never yields `fulfilled`; acceptance‑with‑reservation is a distinct state.
6. No terminal state is immune to evidence revocation: revocation reopens by a new transition with event and observation times, never by mutation.
7. Disputed performance is first class: contested determinations hold a provisional state, block disposition, and never auto‑transition.
8. No obligation carries contractual force toward a counterparty without clause locator + obligee + enforcing party.
9. Executed text and signature evidence are never hard‑deleted while any retention, limitation or hold runs.

## Scenario walkthrough

**Negative.** An internal SLO is declared a contractual guarantee. It fails invariant 8 (no clause locator, no obligee) and ECO‑006's variation formality (`amd-q-formality`, no‑oral‑modification): a dashboard target is not an amendment. Registration as a contractual SLA is refused; it is registered as `directedness = at-large`, `origin = voluntary`, with no remedy chain.

**Acceptance.** Contract executed as expression E1 with digest fixed. Amendment A1 changes payment terms → E2; E1 retained; affected obligations invalidated and re‑derived with version labels. Amendment A2 raises an SLA threshold → E3; `q-standard-change` decides whether open occurrences take the new threshold. Delivery reaches 60% of the owed quantity: fulfilled quantity accumulates, outstanding is derivable, partial tender refusal is assessed, no discharge. The SLA measurement is contested: `dispute-status = contested`, provisional state, disposition blocked, evidence status monitored for revocation. Legal history (E1–E3, signature packages) and operational history (measurement and transition logs) both survive, in separate owners.

## Gaps and publication holds

- Both models are `publishableCanonical: false` / `reviewable-draft`. The profile inherits every existing hold and cannot be called publication‑ready.
- `vercy_candidates` are `conceptual-candidate` at index‑and‑publication‑metadata depth. **Field‑level semantic crosswalk on the four overlap surfaces (obligation, breach/remedy, amendment, evidence) is a blocking prerequisite to asserting reuse.**
- XCT‑029's `performance-standard` finding is explicitly under‑grounded (ISO/IEC 19086‑1 unreachable). This is the weakest load‑bearing element for any SLA profile; publish thresholds as generic structure, labelled.
- WM‑SFT‑016 cannot be a required composition while `boundary-review-required`.
- Open deferrals that bite here: whether an obligation's source may be a legal norm rather than a clause (implied service levels, statutory duties); set‑off and withholding, unowned by either model and needed to characterise service credits; liquidated‑damages versus penalty treatment of credits across jurisdictions.


## Grok study

**Verdict.** PROFILE over WM-ECO-006 and WM-XCT-029. No new catalogue or runtime ID. ContractAmendment, FulfilmentEvidence and ServiceLevelAgreement stay child records or profiles of those two models. Reserved WM-SFT-016 is not promoted into this card. This is standards alignment, not legal advice and not a jurisdiction conclusion.

**Ownership boundary.** WM-ECO-006 owns agreement identity, party positions, formation, executed clause text, signed expressions, amendments, termination and contract-record governance. An amendment is a new executed instrument of the same agreement work: it produces a successor expression and never overwrites a prior signed expression. A conformed text is a derived projection with its own identifier. Rescission-and-replacement or a substitute bargain is a new 006 instance with a successor link, not an amendment.

WM-XCT-029 owns one duty: modality, obligor/obligee/enforcer, conditions, due basis, fulfilment criteria and progress, outstanding quantity, evidence status, breach, cure, excuse, waiver and per-duty consequences. Obligation identity survives amendment and is distinct from the creating instrument and from each dated occurrence.

The contract derives obligation records from stable clause work identifiers. The contract never stores obligation state. An obligation cites work-id plus expression-id and never restates normative clause text. Per-duty non-performance belongs to 029. Contract-level avoidance, termination and remedy election belong to 006.

No independent aggregates:
- ContractAmendment: child instrument of 006.
- FulfilmentEvidence: child event of 029 plus the existing WM-XCT-028 mixin for item identity, digest, custody, contest and withdrawal. Payload stays with the document or observation owner.
- SLA: executed clause set on 006 plus duties with an obligee, enforceable criteria and consequences on 029.

**SLA/SLO split.** A contractual SLA is an executed clause set plus 029 duties. An internal SLO or OLA has no contractual force unless incorporated by an executed contract or amendment. A dashboard metric is not a commitment. EM-TEC-06 already states that SLA and SLO have different grounds; that split is kept. WM-SFT-016 remains reserved, unversioned and not installed. If later written, it may own SLI specification, target, window, observations and error budgets only — never contractual obligees, enforceability, remedies or breach.

ISO/IEC 19086 supplies metric-model alignment for how a measurement is specified; it does not move obligees or remedies into a software-reliability model.

**Required constraints.**
- Every executed expression is immutable (digest, signature package, validation report). Later change is a new instrument.
- Clause work identifiers persist across amendments; expression locators pin text inside one signed expression. Renumbering redirects; it does not mutate history.
- 006 `obligations-and-performance` must stop holding live duty state, quantities, evidence status or per-duty dispute.
- 029 “statement of obligated action” is constrained to locator plus controlled-term encoding of duty content. Predecessor field `obligation_text` is not promoted.
- Execution occupancy on 006 is frozen as of signature. Current obligor is a 029 role binding that references the contract position plus current occupant.
- Delegation / third-party performance does not change 006 party-position occupancy and does not discharge the original obligor. Transfer, novation and new agreement must be typed before occupancy changes.
- Acceptance and evidence revocation are events on 029. They never amend signed clause text.
- Dual timestamps: legal-effect time versus observation time. Transition log is append-only.
- Service credits are typed 029 consequences with an open class slot {remedy | liquidated-damages | penalty | price-adjustment | other}. The slot is filled by a governing-regime profile, not by this card. Exclusive-remedy election, if any, lives on 006.
- Dispute on a duty stays on 029. Forum, claim file and decision remain EM-LEG-05 / neighbouring case models.

**Corrected invariants.**
1. Party occupancy at execution is frozen on 006; current obligor is a 029 binding.
2. An amendment is a new executed instrument of the same agreement; it never overwrites a prior signed expression.
3. A duty has obligor, obligee, subject and fulfilment criterion; it cites clause work-id plus expression-id and does not restate signed text.
4. Obligation state, outstanding quantity, evidence status and per-duty dispute never live on the contract expression.
5. Internal SLO, OLA or dashboard metric is not a contractual guarantee without incorporation.
6. Evidence revocation after acceptance appends a status event and may reopen the duty; prior acceptance remains in the log.
7. Delegation does not change party-position occupancy; transfer, novation or new agreement must be typed first.
8. Service-credit class is a regime-profile parameter, not a model-level legal conclusion.

**Scenario results.**

1. *Internal dashboard SLO presented as a contractual guarantee without incorporation.* Fail the negative case. No 006 incorporation, no 029 contractual duty, no obligee, no enforceable criterion, no consequence. The observation may exist as an SLO/SLI record under EM-TEC-06 later; it has no contractual force.

2. *Contract with two amendments, partial performance and a disputed SLA measurement.* Preserve the original expression plus two amendment instruments and two successor expressions. Obligation records persist via work-id. Partial quantities, measurement-dispute flag and provisional state sit on 029. Observations are cited, not copied. Contract-level remedy election appears on 006 only if an election is recorded. Signed text, execution-time parties, clause locators, outstanding quantities, evidence history and dispute state are all preserved.

3. *Party substituted.* Classify first. Delegation: agreement identity and execution parties unchanged; performer may be distinct; original obligor remains bound. Transfer of obligations / assignment of contract with consent: agreement continues; execution snapshot frozen; current occupant updates; discharge of the original is an explicit indicator, otherwise residual liability remains. Novation or new agreement: new 006 instance, new execution snapshot; old contract closed except surviving duties the new instrument states. Wrong class is an invariant failure.

4. *Fulfilment evidence revoked after acceptance.* Keep the evidence-item identity. Append revoked / insufficient / superseded with authorising role, reason and effective instant. 029 reopens the duty without erasing the prior acceptance event. Outstanding quantity is recomputed from the surviving accepted set. A replacement certificate is a new item bound to the same duty. Dispute remains until resolved. No mutation of 006 expressions.

5. *Service credits.* Record them as 029 secondary obligations triggered by a typed consequence. Whether a given regime treats the credit as a remedy, liquidated damages, an unenforceable penalty or a price-adjustment mechanism is a profile parameter requiring subject-matter verification of applicability. This card does not decide enforceability. 006 records only a contract-level exclusive-remedy or election clause if one was executed. SFT-016 never owns credits.

**Publication blockers.**
- 006/029 overlap is not yet written as enforceable PROFILE constraints.
- Semantic crosswalk, rights and source mastership remain open in brief.json.
- Delegation / third-party-performance type is missing on 006 change events.
- Writing-rule hold on 006 (CISG Art. 11 / 12–96 reservations versus UCC §2-201 / §2-209) stays co-recorded; it must not be collapsed.
- No fixtures for tests 1–5, especially two-amendment plus disputed measurement, and acceptance then revocation then reopen with preserved log and recomputed quantity.
- Reserved-acceptance versus unconditional discharge is untested.
- WM-SFT-016 is a stub; EM-TEC-06 must keep SLA/SLO grounds split. Do not invent a SFT-016 runtime version.
- Alignments to UBL, FIBO, ODRL, LegalRuleML and ISO/IEC 19086 are alignments only, not conformance claims.
- Primary legal sources of a chosen jurisdiction still require subject-matter verification before any regime profile is published.


## Provider comparison

# EM-LEG-01 provider comparison

Claude and Grok independently select **PROFILE** over WM-ECO-006 and WM-XCT-029 with no new catalogue or runtime identifier. Contract Amendment remains an agreement-owned instrument, Fulfilment Evidence remains duty-owned status plus externally mastered payload, and contractual SLA is an executed clause set plus enforceable duties.

Both providers assign immutable agreement identity, signed expressions, clause work IDs, amendments, termination and contract-record governance to WM-ECO-006. WM-XCT-029 owns live duty roles, conditions, fulfilment, outstanding quantity, evidence status, dispute, breach, cure and consequences. Contract state never duplicates duty state; duty records cite exact clause work and expression locators without restating normative text.

Both distinguish contractual SLA from internal SLO. WM-SFT-016 remains reference-only and may later own measurement and error-budget semantics, never contractual standing, remedies or breach. Grok strengthens execution-time occupancy, delegation/novation typing, evidence-revocation reopening and regime-qualified service-credit classification.

Canonical publication remains held by non-canonical bases, unratified overlap crosswalks, missing delegation types, unresolved acceptance/discharge semantics, the WM-SFT-016 stub and jurisdiction-specific legal rules.
