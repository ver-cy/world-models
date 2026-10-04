# EM-ORG-07 — Independent review (no tools; frozen dossier only)

## Verdict
Reuse with profiles. No new model identifier is warranted and none is allocated.

- **StakeholderInterest** → reuse **WM-ORG-013** (`entry_kind: relationship`) as master, under an enterprise profile. Its `stake-identity`, `interest-attribution` and `impact-rights` layers already carry the scoped party↔subject stake.
- **Expectation** → profile, not new: an attributed **WM-KNW-007** claim (anticipatory/deontic, with explicit non-acceptance marker) bound into `interest-attribution`. WM-ORG-013 already pairs "interests and expectations" in one layer, so a sibling subject would duplicate it.
- **StakeholderAssessment** → profile of **WM-ACT-034**, subject = the stake relation (never the party). WM-ORG-013 `influence-assessment` is demoted to a binding layer, not the master of the assessment occasion.
- **EngagementPlan** → profile of **WM-ACT-008**, with WM-ORG-013 `engagement-purpose` supplying the decision-interface binding. Engagement *execution* stays out (WM-ORG-013 explicitly excludes outreach; `link-response` performs no sending).

Independent identity and lifecycle test: the stake relation, the assessment occasion, and the dated plan each have distinct identity, distinct revision cadence and distinct terminal states, so they must not collapse into one record; none of the four needs identity independent of an existing master.

## Evidence
WM-ORG-013 is `publishableCanonical: false`, `adjudicationStatus: reviewable-draft`, single-provider Codex with Claude and Grok waived, `validation` dimension a declared gap, no executable schemas or privacy/negative fixtures, and `review_state: boundary-review-required`. The queue records `mapping_status: conceptual-candidate`, `evidence_depth: index-and-publication-metadata` — the EM-ORG-07↔WM-ORG-013 crosswalk is unverified. WM-ACT-034 and WM-KNW-007/010 are single-provider with publication holds (WM-ACT-034's `access` dimension is self-audited as over-claimed; retention has no sourced periods). WM-ACT-008, WM-ORG-001 and WM-PER-001 are dual-provider drafts. The dossier `relations` array contains **no row for WM-ORG-013**, so every composition below is a proposal.

Two contradictions found independently:
1. Registry `vr.wm-org-013` sets `parent_ids: WM-ORG-001`, while the spec's own composition makes WM-ORG-001 a non-required `REFERENCE` and its boundary note forbids remastering the party. A relationship cannot be structurally owned by one endpoint (same seam as EM-ORG-01). Must be resolved before publication.
2. `candidate_properties_from_v1` carries `influence` as a bare `code` on ORG-09. That shape is incompatible with the invariant that influence is a dated assessment; it must not survive as a party or relation attribute.

## Identity/mastership
Distinct identities: party (WM-PER-001 / WM-ORG-001) · stake relation (WM-ORG-013) · interest assertion · expectation claim (WM-KNW-007) · assessment occasion (WM-ACT-034) · plan and planned engagement action (WM-ACT-008) · engagement response link · decision/perimeter (WM-KNW-010) · evidence item (WM-KNW-008).

Mastership: WM-ORG-013 masters scope-qualified stake identity, attributed interest, affectedness, representation and participation conditions. WM-ACT-034 masters criteria, method, results, decision rule, assessor competence/impartiality and validity. WM-ACT-008 masters engagement intent, timing, commitment and baseline. WM-KNW-010 masters the decision perimeter, question, version and rationale; its `affected subjects` field is a derived index over stake relations, never a second stakeholder map. Party masters (corporate registry, HRIS, legal-entity registers) keep identity, names, form and status; no stakeholder record may write them.

## Stakeholder context
Stake is contextual participation, not a party trait. Every role, interest, influence, impact, expectation and engagement approach requires: subject matter reference; decision/project perimeter (WM-KNW-010 or project reference); viewpoint (whose attribution — self-expressed, representative, analyst hypothesis); period (valid interval plus recorded time); evidence reference (WM-KNW-008) or an explicit unknown. Missing any of these blocks promotion out of draft.

Distinctions asked: **client** = counterparty to an agreement; **owner** = equity/control endpoint in WM-ORG-001; **executor** = assignee/participant in WM-ACT-006/WM-ACT-008. Each may also hold a stake, but none implies one, and a stake implies none of them. WM-ORG-013's boundary note is correct that stake ≠ shares, control or power, and that low influence does not remove affectedness.

## Interest and expectation
An interest is an append-only assertion with attribution mode (declared vs inferred), scope, language tag, valid interval and evidence. Inferred concern is never self-expression. Absent, withheld and not-yet-heard must not be coerced to "no interest" or to consent. A subject may hold several, including mutually inconsistent, interests and expectations within one perimeter, and different ones across perimeters; conflict is registered as typed relations (WM-KNW-007), not adjudicated here. Expectations carry addressee, modality and an acceptance state; acceptance requires a decision (WM-KNW-010) plus its authorised occurrence (WM-ACT-024), never attendance or silence.

## Assessment
Influence, impact and priority are WM-ACT-034 assessments whose subject is the pinned stake relation: criteria and scale bound at version, method and depth declared before results, raw and normalised values, stated uncertainty, decision rule with guard bands and abstention, assessor identity plus impartiality declaration, validity window, and a re-assessment trigger. Indeterminate must be representable and must never be scored as low. Published ratings travel with scale, aggregation model and rule. Generalisation beyond the declared perimeter, viewpoint and period is prohibited, which is what defeats the negative case.

## Engagement plan
A WM-ACT-008 plan with declared intent mode (proposal/option ≠ authorisation), planned engagement actions carrying `engagement_mode` as a coded action kind, accessibility and safe-participation conditions from WM-ORG-013 `participation-conditions`, participants by reference, commitments to named beneficiaries with consequence and release, disclosure class, and baseline plus change log with reason codes. Registration creates no outreach entitlement.

## Conflict and contestability
Representative mandate is scope-bound, narrower than the group, and contestable; contested mandate produces a contested set under reviewer policy, never a silent overwrite. Dissent, objections and minority positions are retained and attributable. Recusal/conflict-of-interest uses WM-KNW-010 governance (declared interest → determination by a distinct party → recusal action with effective instant → restated thresholds), which that model itself marks a **gap** — so this is a declared weak point, not settled structure. Update triggers: perimeter change, decision version change, mandate change, evidence supersession, assessment expiry, withdrawal of engagement (which does not end an underlying impact).

## Privacy
Deny by default; stakeholder status is not permission. Personal data by reference to WM-PER-001 with minimisation and predicate-first disclosure; no inference of sensitive attributes, political affiliation or personality from an interest; public role does not waive protection of a private concern; confidential concerns and identities may be withheld while identifier, scope and withholding fact remain reconcilable. Exports are minimised projections with loss warnings or refusal. Deleting a record cannot extinguish a right or grievance.

## Time/version/scenario
RFC 3339 with seconds and explicit offset; uncertain effective dates preserved separately; valid interval distinct from recorded/knowledge time. Revisions are append-only with expected-head checks; corrections are compensating revisions. Assessments are versioned occasions, never recomputed in place. Plans carry baselines; scenario variants are separate plan/assessment versions, not edits.

## Acceptance scenario
One counterparty, two projects: a single party record; two decision perimeters; two stake relations with different interests, expectations, assessments and plans. Reassessment in project A issues a successor assessment citing the prior one, retaining its basis, method, evidence and result. Project B is untouched. An attempt to attach "low influence" to the party, or to inherit A's rating into B, is rejected: no party attribute exists to hold it, and the assessment's scope bars the extrapolation.

## Invariants
1. Party identity and stake participation are separate records; stake never remasters a party.
2. Every role, interest, influence, impact, expectation and engagement approach binds subject, perimeter, viewpoint, period and evidence or explicit unknown.
3. Influence/impact are dated assessments with scale, method, uncertainty and validity; no permanent traits.
4. No assessment, rating or label generalises beyond its declared scope.
5. One subject may hold conflicting interests and expectations; conflict is registered, not resolved.
6. Affectedness and rights are independent of influence and of engagement participation.
7. Mandate is scope-bound and contestable; silence, attendance and acknowledgement never establish consent.
8. Registration authorises no outreach, disclosure or persuasion.
9. Dissent, objections and grievances are retained; deletion extinguishes no right.
10. Perimeter or decision change triggers review; stale maps are marked, not silently reused.

## Minimal model set
WM-ORG-013 (master) · WM-ORG-001 · WM-PER-001 · WM-ACT-034 · WM-ACT-008 · WM-KNW-007 · WM-KNW-010 · WM-KNW-008 (evidence, by reference) · WM-ACT-024 (approval occurrence, by reference).

## Holds
All bases are non-canonical reviewable drafts. WM-ORG-013 has no independent external review, no relation rows in this dossier, an unresolved `parent_ids` conflict with its own reference boundary, an unverified crosswalk to EM-ORG-07, and no fixtures. WM-ACT-034's access claim and WM-KNW-010's conflict-of-interest structure are self-declared weak. This is a boundary and profile decision only: no identifiers allocated, no canonical completeness claimed, not installable, not publication-ready.

*(~1,180 words)*
