# Verdict

**Reuse WM-KNW-015 as the risk entity.** Its declared root — a persistent item with identity separate from assessment revisions, gated lifecycle, single accountable owner, and survival through re-estimation, split, merge and closure — is exactly the risk entity EM-RSK-01 needs. No new identifier is justified.

**Profile WM-XCT-027, do not reuse as published.** Retain it as the host mixin for *assessment context* only (its bundles 1–3 and 7–9). Its control-authoring bundles (4–6) are excluded by its own `scope_statement`, `out_of_scope` list and boundary note 2, and its adjudication already records `status: split`. A profile that keeps binding/framing/estimation/residual/comparability/governance and reduces all control content to citation is the defensible EM-RSK-01 base.

**Identifier-unassigned candidates required for three planes** (independent identity, lifecycle and mastership in each case, none satisfiable by a host-scoped field group): control (design + implementation state), control assessment (test activity + effectiveness determination), and treatment (decision + action). Evidence, appetite/tolerance and acceptance-decision planes are already named as external in both specs; reference them, do not author them.

**Treatment ownership is a live boundary conflict:** EM-RSK-01 lists `RiskTreatment` among candidate types while EM-RSK-02 exists as a related contour. Settle which contour masters treatment before either claims it.

# Evidence

Both bases are `published` but `adjudicationStatus: reviewable-draft`, `publishableCanonical: false`, `providerMode: single-provider-waiver` with Grok waived (authorised 2026-08-29T09:06:27Z). Evidence depth on both registry candidates is `index-and-publication-metadata`; `mapping_status` is `conceptual-candidate`; `review_state` is `boundary-review-required` on both. Specs were pinned by digest (WM-KNW-015 `6725…3ccd`; WM-XCT-027 `4abb…5928`). The only ratified relation in the pack is WM-AI-008 → WM-KNW-015 `REFERENCE` (`candidate`). WM-ACT-017 parenthood is asserted in registry `parent_ids` and boundary notes but is explicitly held unratified. Both packs carry unretrieved primary-text holds (ISO 31000/31073/Guide 73, ISO/IEC 27001/27002, COSO, Basel OPE10) and unverified source pins. No semantic crosswalk is verified. Nothing below rests on sources beyond this dossier.

# Identity/mastership

| Plane | Master | Basis |
|---|---|---|
| Risk entity | WM-KNW-015 | identity persists across revisions, register membership, closure |
| Assessment context/result | WM-XCT-027 profile (host-scoped) | no identity independent of host; revision-pinned binding |
| Treatment decision/action | identifier-unassigned candidate (or EM-RSK-02) | own owner, schedule, milestones, closure; outlives the assessment |
| Control design | identifier-unassigned candidate | a control exists and is owned without any risk; catalogue/parameter lifecycle |
| Control implementation/execution | same control candidate for implementation state; **execution occurrences referenced** from operational masters (GRC/SIEM/service desk) | occurrence volume, retention and custody are not governable in a mixin |
| Control test/effectiveness determination | identifier-unassigned candidate | determinations are cited, expire, and are invalidated independently of any risk |
| Evidence | external evidence model (identifier-unassigned in both specs) | custody, digest, availability, lawful destruction |
| Appetite/tolerance | enterprise governance, referenced | authored and approved elsewhere; versioned |
| Residual-risk acceptance | decision/authority model, referenced | authorisation act, not an estimate |

**Resolving WM-XCT-027's ownership split.** Remain in the mixin: `rctl-risk-*` in full — risk reference, revision pin, statement digest, `binding-validity-state`, anchors, causal anchors, taxonomy pin, scope/horizon/as-of/recorded/validity times, criteria-method-expression pins, likelihood and consequence dimension declarations, inherent estimate with its exclusion statement, assumptions/basis/uncertainty, residual value, `relied-on-control-reference`, `cited-effectiveness-determination-reference`, `reliance-without-determination-flag`, `changed-dimension`, `residual-change-explanation`, appetite reference and `comparison-outcome`, comparability verdicts/caveats/scenario; plus `rctl-gov-*` stamps, provenance, sensitivity, evidence-integrity refs and retention refs **scoped to the binding only**.

Move to the external control/assessment masters: `rctl-control-catalogue-binding`, `-objective-classification`, `-applicability-scope`, `-accountability-references` (including `rctl-gov-de-control-owner-ref`), `-design-assertion`, `-implementation-assertion`, `-operating-cadence`, `-assessment-evidence-binding`, `-effectiveness-conclusion`, `-crosswalk-alignment`, and `-coverage-dependency` (cross-record state a host mixin cannot own — retain the traversal query, drop the authored matrix). `rctl-control-link-record` becomes a contained collection under the single host-scoped context root, not a second root. `rctl-control-residual-contribution` splits: the attribution *claim* is authored by the control assessment master; `attribution-status` (accepted/rejected/suspended) is the risk owner's, held with the risk entity.

# Assessment and comparability

Comparison is gated, never normalised. Every estimate carries criteria-set + version, method + version, expression mode, scale reference, scope, exclusions, horizon, as-of and recorded times. `rctl-risk-fn-check-comparability` returns `comparable` / `comparable-with-caveats` / `not-comparable` plus `mismatched-pin-list`; aggregation requires WM-KNW-015 `de-aggregation-eligibility` true **and** a comparability verdict, and caveats are non-strippable. Ordinal bands are stored as codes: no difference, product or mean is defined under qualitative, ordinal or scenario modes — the inherent→residual comparison records changed dimensions and direction, computing magnitude only where the pinned mode admits it. Cross-horizon comparison is refused unless horizons match or a declared conversion exists; `case-basis` (expected / most likely / worst credible) must match; records pinned to withdrawn criteria are handled by `superseded-criteria-handling`, not silently re-scored.

# Control design/execution/effectiveness

Four separate states, each with its own determining party and event time: design adequacy (would achieve objective if operated as prescribed); implementation (is in place, with deviations, exceptions, expiry, compensating controls); operation (operating / suspended / not operating, with expected vs observed occurrences by reference); effectiveness (a conclusion on a named vocabulary whose **only** permitted basis is assessment method + coverage + evidence bindings, carrying confidence, validity expiry and invalidation triggers). Design status never implies implementation; implementation never implies operation; none of the three implies effectiveness. An expired conclusion degrades to unknown, not to effective.

# Treatment/residual risk

Response option selection and rationale sit with the risk entity; plans, milestones and closure sit with the treatment master; residual estimate and appetite comparison sit in the assessment context; acceptance is a referenced decision with required authority level, threshold-table version and authorisation time. Residual must state grounds: relied-on controls, their cited determinations, changed dimensions and an explanation. Reliance on a control with no current determination sets `reliance-without-determination-flag` and bars any residual reduction attribution.

# Shared cause

Two risks share a cause when they cite the same `risk-source-reference` / threat-catalogue identifier, the same `predisposing-condition-statement`, the same held-fixed `context-condition-statement`, or the same relied-on control or control dependency. Shared cause is recorded as a declared correlation and a `aggregation-caveat`; it never licenses summation, and it never merges identities. Common dependence on one control is the strongest form: it makes simultaneous degradation plausible and must appear as a caveat on any roll-up.

# Invariants

1. Every estimate carries scale, expression mode, horizon, as-of time and criteria version; otherwise it is unusable, not merely unvalidated.
2. Control existence, documentation, mapping, policy status or incident absence never yield an effectiveness value.
3. A policy or requirement status never transitions a risk lifecycle state or closes a risk.
4. Residual risk without recorded grounds and a cited determination is invalid.
5. Acceptance requires a referenced decision and sufficient recorded authority.
6. Aggregation requires an explicit comparability verdict; caveats travel with the aggregate.
7. Item identity is independent of assessment revision and register membership.
8. Assessment context has no identity independent of its host and its pinned risk revision.
9. Event time, observation/as-of time and record time are distinct and never substituted.
10. Superseded upstream risk revision marks the binding stale; the mechanism must be named (currently a declared gap).

# Scenario

Control C is cited by contexts for R1, R2, R3. A failed execution of C is recorded in the executing system. Effect:

- **R1** — cites determination D over a period covering the failure; C's claimed mechanism is likelihood reduction on the same population; evidence reference resolves with a matching digest. The failure invalidates D via a fired reassessment trigger; currency becomes invalidated, `reliance-without-determination-flag` set, residual estimate reopened, `changed-dimension` recorded. Assessment changes.
- **R2** — relies on C for a consequence dimension and population outside the failed occurrence's covered scope. No causal link; reliance note recorded, currency unchanged. No assessment change.
- **R3** — links C by coverage/crosswalk with no cited determination. The flag was already true; the failure adds a coverage-gap finding. No assessment change, because there was no effectiveness claim to falsify.

Negative case: a green policy status on C closes none of R1–R3 and alters no estimate.

# Minimal profile/candidate shape

Reuse WM-KNW-015 unchanged. WM-XCT-027 profile: one host-scoped assessment-context root; retained field groups as listed; control content citation-only; contained risk↔control edge collection; comparability gate mandatory; coverage matrix and control-authoring artifacts removed. Three identifier-unassigned candidates: control (design + implementation), control assessment (test + effectiveness determination), treatment (decision + action) — each pending an identity, lifecycle and mastership justification of its own. Evidence, appetite, acceptance-decision, party, criteria/method registry and execution telemetry: reference only.

# Holds

Single-provider waiver on both bases; no independent second-provider corroboration. WM-XCT-027's split is unresolved upstream and this review's resolution is a recommendation, not a ratified boundary. Crosswalk, rights and source mastership unconfirmed; `published` does not mean independently reviewed. Unretrieved primary texts and unverified source/version pins on both packs. Composition-link counts in both packs are unsupported by delivered structure. Upstream-supersession detection is undefined. WM-ACT-017 parenthood unratified. Registry defects open: empty `namespace_uri`, vague `owner_or_maintainer`, adverse-only purpose line on WM-KNW-015. No claim of canonical completeness and no claim of installability is made here; immutable refs and fixture checks remain outstanding per the contour's blocking decisions.
