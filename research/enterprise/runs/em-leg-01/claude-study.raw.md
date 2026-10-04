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
