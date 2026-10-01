# Frozen no-tools semantic audit — EM-LND-04

## Verdict

**REVISE.**

The disposition is right: PROFILE/projection, no new business identity. **No runtime/model identifier is justified** — `newRuntimeId: false` is correct and must stay false. StrategyLandscape and StrategicAlignment project masters that already hold the identity (WM-KNW-011 objectives/targets, WM-MAT-008 + WM-XCT-025 measurement, WM-ACT-030 initiatives/hypotheses, WM-ACT-029/005 portfolio/project, WM-ACT-034 assessment); minting a third alignment record would create exactly the divergent copy the measure-binding rationale forbids.

REVISE rather than ACCEPT WITH LIMITS is not about the base and registry gaps — those are holds. It is because the candidate's own constraint list is under-specified in ways that permit a *conformant* implementation to produce authoritative facts: unjustified expert judgment as alignment basis, confirmed benefit on an unallocated placeholder, uncapped attribution, retroactive rewriting, and a collapsed time model. The synthesis and both studies state these rules; the normative candidate drops them. The gap is between the reasoning and the artifact that will be read.

## Material defects

1. **Expert judgment is attributable but not justified.** Constraint 3 accepts "attributable expert judgment" with no recorded justification. WM-KNW-011 permits qualitative basis only with recorded justification. As written, naming a person is sufficient basis, so any edge is mintable at will. This is the single largest hole.
2. **Causal promotion may land on an unallocated referent.** Constraint 5 allows a pinned WM-ACT-034 assessment to promote a hypothesis, but Outcome/Benefit is identifier-unassigned (hold 1). A promoted "confirmed benefit" on a view-local placeholder is de facto benefit identity minted by the view. Confirmed status must attach to the assessment, not the placeholder.
3. **No attribution cap.** Synthesis invariant 8 (shares ≤ 1 per benefit and period, no portfolio/constituent double-count) is absent from the candidate. Portfolio and project claims can each take full credit.
4. **No positive realization test.** Constraint 4 states only what does *not* prove realization. The requirement — final or amended qualified observations whose phenomenon time falls inside the declared realization window, plus adjudicated attribution — is missing, so "realized" is unbounded from the positive side.
5. **No non-retroactivity rule.** Nothing forbids realization overwriting expected history, or confirmation rewriting state at an earlier knowledge time. Replay integrity depends on this.
6. **Time model collapsed.** Constraint 6 names view classes only. Node/edge effective interval, assertion knowledge time, and measurement phenomenon/result/ingestion time are separate axes; a view can satisfy constraint 6 while fusing them, which makes replay unsound and absence indistinguishable from late ingestion.
7. **WM-ACT-001 is listed as a base.** It appears in `bases` while hold 2 declares its semantics blocked. Any consumer counting satisfied dependencies reads it as reused and specified. A blocked referent is not a base.
8. **WM-XCT-025 host requirement not declared.** It is a mixin with no record identity; listed flat, it permits an identity-less measurement with value, unit and method and no WM-MAT-008 host.
9. **Objective/portfolio distinctness missing.** Constraint 4 separates output/outcome/benefit but not objective from portfolio, so a governed collection can be cited as the satisfied objective.
10. **Findings are unconstrained.** Gap questions are core output, yet no constraint says a finding is a non-authoritative claim *about the record*, addressed to an owner resolved from the master, and that a recorded non-practicability justification with qualitative criteria is not a defect.
11. **Open deny-list and stale holds.** "Tags, budgets and membership are insufficient" is a deny-list; completion/status is omitted there, and novel pseudo-bases (naming similarity, roadmap adjacency, org proximity) are unaddressed — it must be a closed allow-list of basis kinds. Blocked referents also lack a "never deleted, view marked degraded, never ranked authoritatively" rule. Separately, hold 3 still lists independent Grok review and frozen audit as pending, and the candidate carries no explicit "no canonical completeness, installability or publication claim" hold.

## Required fixes

1. Constraint 3: require, for expert judgment, a named accountable party **and** a recorded justification; otherwise the edge is not stored and becomes a finding.
2. Constraint 5: forbid promotion of a causal hypothesis whose outcome or benefit referent is `declared-unallocated` or `blocked`; confirmed determinations are held on the WM-ACT-034 assessment.
3. Add: adjudicated attribution shares sum ≤ 1 per benefit and period; portfolio and constituent claims never double-count.
4. Constraint 4: add the positive realization test (qualified observations, phenomenon time inside the declared window, adjudicated attribution).
5. Add: expected and realized coexist; realization never overwrites expected history; confirmation never rewrites state at an earlier knowledge time.
6. Constraint 6: enumerate effective interval, knowledge time, and phenomenon/result/ingestion time as separate, non-collapsible axes.
7. Move WM-ACT-001 out of `bases` into a distinct `blockedReferents` field; keep hold 2 verbatim.
8. Declare WM-XCT-025 a mixin requiring a WM-MAT-008 host.
9. Constraint 4: add objective ≠ portfolio; a portfolio is never the satisfied objective.
10. Add a findings constraint: non-authoritative claim about the record, owner resolved from the master, carrying rule, subject, as-of, evidence and severity; a justified qualitative criterion is not a defect.
11. Restate constraint 3 as a closed allow-list of basis kinds (assessment | observation | justified attributable judgment); add the blocked-referent rule (visible, unenforceable, never deleted, view degraded, never ranked); refresh hold 3 and add the no-publication/no-installability hold.

## Additional fixtures

```json
[
  {"id":"unjustified-expert-judgment","kind":"negative","input":{"edge":"supports","from":"initiative:I","to":"objective:O","basis":{"kind":"expert-judgment","party":"person:P","justification":null}},"expect":{"stored":false,"findingEmitted":true},"expectedCode":"E_UNJUSTIFIED_EXPERT_JUDGMENT"},
  {"id":"justified-expert-judgment","kind":"positive","input":{"edge":"supports","from":"initiative:I","to":"objective:O","basis":{"kind":"expert-judgment","party":"person:P","justification":"recorded rationale"}},"expect":{"stored":true,"basisKind":"expert-judgment","provenanceRetained":true}},
  {"id":"confirm-on-unallocated-benefit","kind":"negative","input":{"edge":"causal-hypothesis","to":{"kind":"benefit","state":"declared-unallocated","placeholderKey":"ph:benefit-1"},"promoteTo":"confirmed","assessmentRef":"wm-act-034:A"},"expect":{"promoted":false,"determinationHeldOn":"wm-act-034:A"},"expectedCode":"E_PROMOTION_ON_UNALLOCATED_REFERENT"},
  {"id":"attribution-over-one","kind":"negative","input":{"benefit":"ph:benefit-1","period":"2026-Q1","shares":[{"claimant":"project:P","share":0.7},{"claimant":"portfolio:F","share":0.6}]},"expect":{"accepted":false},"expectedCode":"E_ATTRIBUTION_SHARE_EXCEEDED"},
  {"id":"attribution-split-valid","kind":"positive","input":{"benefit":"ph:benefit-1","period":"2026-Q1","shares":[{"claimant":"project:P","share":0.6},{"claimant":"project:Q","share":0.4}],"adjudicated":true},"expect":{"accepted":true,"sum":1.0}},
  {"id":"observation-outside-window","kind":"negative","input":{"benefit":"ph:benefit-1","window":{"from":"2026-01-01","to":"2026-03-31"},"observation":{"phenomenonTime":"2026-05-02","quality":"final"}},"expect":{"realized":false},"expectedCode":"E_OBSERVATION_OUTSIDE_WINDOW"},
  {"id":"retroactive-confirmation","kind":"negative","input":{"assessment":{"ref":"wm-act-034:A","knowledgeTime":"2026-09-01"},"writeAtKnowledgeTime":"2026-04-01"},"expect":{"accepted":false,"priorReplayUnchanged":true},"expectedCode":"E_RETROACTIVE_KNOWLEDGE_TIME"},
  {"id":"replay-preserves-knowledge-time","kind":"positive","input":{"viewClass":"as-of-replay","knowledgeTime":"2026-04-01","laterConfirmations":["wm-act-034:A"]},"expect":{"confirmationsExcluded":true,"axesSeparate":["effective","knowledge","phenomenon","result","ingestion"]}},
  {"id":"collapsed-time-axes","kind":"negative","input":{"measurement":"wm-mat-008:M","phenomenonTime":"2026-02-01","ingestionTime":"2026-02-01","axesDeclared":["timestamp"]},"expect":{"accepted":false},"expectedCode":"E_TIME_AXIS_COLLAPSED"},
  {"id":"portfolio-as-objective","kind":"negative","input":{"edge":"supports","from":"project:P","to":"portfolio:F","assertedAs":"satisfied-objective"},"expect":{"stored":false},"expectedCode":"E_PORTFOLIO_AS_OBJECTIVE"},
  {"id":"unhosted-measurement-mixin","kind":"negative","input":{"measurement":{"mixin":"WM-XCT-025","value":12,"unit":"count","host":null}},"expect":{"accepted":false},"expectedCode":"E_UNHOSTED_MEASUREMENT_MIXIN"},
  {"id":"novel-basis-kind","kind":"negative","input":{"edge":"supports","from":"project:P","to":"objective:O","basis":{"kind":"roadmap-adjacency"}},"expect":{"stored":false,"allowedBasisKinds":["assessment","observation","justified-judgment"]},"expectedCode":"E_BASIS_KIND_NOT_ALLOWED"},
  {"id":"completion-as-alignment","kind":"negative","input":{"edge":"supports","from":"project:P","to":"objective:O","basis":{"kind":"status","value":"complete"}},"expect":{"stored":false},"expectedCode":"E_BASIS_KIND_NOT_ALLOWED"},
  {"id":"blocked-capability-constraint-ranked","kind":"negative","input":{"edge":"constrains","from":{"kind":"capability","state":"blocked","base":"WM-ACT-001"},"to":"objective:O","rank":1,"enforced":true},"expect":{"enforced":false,"deleted":false,"viewDegraded":true,"rankSuppressed":true},"expectedCode":"E_BLOCKED_REFERENT_ENFORCED"},
  {"id":"contradictions-netted","kind":"negative","input":{"edge":"causal-hypothesis","supporting":[{"confidence":0.8}],"contradicting":[{"confidence":0.6}],"presentation":"net"},"expect":{"accepted":false,"bothSidesVisible":true},"expectedCode":"E_CONTRADICTION_NETTED"},
  {"id":"justified-qualitative-criterion","kind":"positive","input":{"objective":"O","measureBinding":null,"nonPracticabilityJustification":"recorded","qualitativeCriterion":"stated"},"expect":{"finding":false,"renderedAs":"qualitatively-criterion-bound"}}
]
```

## Freeze decision

**The audit is frozen and final; the profile is not.** No further audit is owed or will be given.

Freeze the candidate once fixes 1–11 are applied verbatim and all existing plus added fixtures pass. That application is mechanical conformance checking against this record, not a re-audit, and needs no new reviewer.

Holds remain holds and do not block the PROFILE disposition: non-canonical bases with `publishableCanonical: false`, single-provider waivers, empty relationship contracts, unallocated Strategy and Outcome/Benefit, the unproven EM-STR-03 capability crosswalk, and unavailable WM-ACT-001. Hold 3 should be updated to record this audit and the independent review as delivered, with relationship contracts and causal fixtures still pending.

**No publication authority is granted.** No canonical completeness, installability, or publication claim is supported, and no identifier is allocated.
