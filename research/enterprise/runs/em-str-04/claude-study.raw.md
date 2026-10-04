## Verdict

**Reuse, profile, contain — no new root.** EM-STR-04 is served by profiling the complete WM-ACT-030 Initiative aggregate; none of the five candidates justifies an independent root.

- **Initiative** — *root*. Reuse WM-ACT-030 unchanged in kind (aggregate); add an EM-STR-04 investment-rationale profile.
- **BusinessCase** — *contained versioned release* under the Initiative root (the existing `case-for-change release` plus `versioned option set and appraisal`). No independent identity.
- **Alternative** — *contained record* inside the appraisal release; referenced (not re-mastered) by a decision when one occurs.
- **Assumption** — *reference* to WM-KNW-016 (entity). Not contained.
- **InvestmentDecision** — *profile*, not a root: a decision-type profile binding WM-KNW-010 (rationale content), WM-ACT-024 (approval occurrence), WM-REC-010 (issued record) and WM-ECO-012 (funding).
- **Hypothesis** — *reference* to WM-KNW-009 (entity).
- **Mandate** — *contained assertion* in WM-ACT-030 citing an external authority instrument; never a root, never funding.

No identifiers allocated.

## Evidence

WM-ACT-030's scope already owns originating problem evidence, case for change, mandate, sponsorship, options and hypotheses, exploratory guardrails, gates, lifecycle and formalization history, with every party, strategy, project, budget, risk, decision and observation master external. Its adjudication names one load-bearing invariant — *formalization mints a new master identity with typed derivation and handover* — asserted consistently across scope, boundary notes, patch rules, policies and adversarial checks, with no contradiction found. Its policies state an Initiative is not automatically a Project. WM-ACT-005 independently states that a project record is created only from an authorizing instrument and that informal task lists do not mint a project. Those two facts together dispose of the negative case without new structure.

Decision machinery is already partitioned three ways: WM-KNW-010 owns question, alternatives, criteria, evaluation, outcome and rationale as content; WM-ACT-024 owns the occurrence (authority, participation, quorum, modality); WM-REC-010 owns the issued, fixed, versioned record with `fn-evaluate-validity-as-of`. A fourth "InvestmentDecision" root would duplicate all three.

## Identity/mastership

Initiative identity is source-qualified: authoritative master-system identifier, then governed IRI, then Dimension UUID — never name, date or digest. The business-case release, option set, membership, gate, assignment and lifecycle event identities are distinct children under that root. Assumption, hypothesis, risk, budget, decision and project masters stay external and are bound by identity plus version. Mastership of the appraisal option set sits with the Initiative because options are appraised long before any decision occurrence exists; WM-KNW-010 registers those option identities by reference at decision time and may add decision-local alternatives (defer, revised do-nothing) under its own screening rules. That split needs a relation row (see Holds).

## Initiative transition

An idea, request or ticket is not an Initiative: registration requires resolvable identity, source profile, case for change, mandate and accountable sponsor. An Initiative is not a Project, Program, Portfolio or operation: formalization is a typed derivation and responsibility handover to a new master identity with scope mapping, effective time and residual obligations — never an in-place type change or identity reuse. Operational work is excluded by the same rule: an operation is a formalization target, not a renamed initiative. A tracker container never mints either (EM-WRK-02).

## Business case

The business case is a release, not an identity. Each release binds: problem/opportunity evidence and baseline, mandate and authority boundary, the option set with the no-change comparator, criteria and weights, assumptions and hypotheses by reference, expected results logic, cost and funding references, and uncertainty. Releases are immutable; corrections and profile-safe changes create successors with preserved provenance. Initiative identity survives every release; a release never survives as a substitute for it. On formalization the release is carried forward by reference into the Project's own investment-justification finding — not by identity reuse, which would create two masters.

## Alternative/assumption/hypothesis

**Fair comparison** requires, per release: one criteria set at a pinned version; a mandatory do-nothing / business-as-usual baseline appraised on the same terms; identical horizon, currency, price base and valuation basis; the same metric definitions at the same revision; declared method per criterion; and uncertainty as ranges or distributions with a stated basis, never a bare point. Mandatory pass/fail criteria are separated from compensatory ones. Ordinal bands are not multiplied without a documented, cited combination rule, and value and harm dimensions are not netted without an explicit commensuration method.

**Alternative ≠ rationale.** An alternative is a candidate with its own estimates and risk set; rationale is the reasoning connecting criteria and evidence to the chosen alternative and to each rejection. Rejections carry a recorded ground and, where relevant, the condition whose change would have made the option selectable.

**Assumption ≠ hypothesis ≠ forecast.** An assumption is a premise accepted for a bounded purpose with owner, validity window and defeat condition. A hypothesis is framed for evaluation with predictions and criteria. A forecast is a dated projection with method and confidence. None converts to another by relabelling, and acceptance is never truth.

## Decision/mandate/funding

Four separations hold. **Rationale** (WM-KNW-010) is content: question, options, criteria, evaluation round, outcome, conditions, reasons. **Occurrence** (WM-ACT-024) is the act: authority basis, delegation limits, participants, quorum, decided-at. **Record** (WM-REC-010) is the issued, fixed, attested expression with validity window and supersession. **Mandate** is prior and narrower — authority to explore and coordinate within guardrails; it authorizes neither delivery nor spend. Approval does not create a project, does not create funding availability, and does not prove benefit. Funding is WM-ECO-012: authorization, allocation, release and availability are distinct states, and source-side conservation applies across allocations (EM-FIN-01).

## Benefits/risks/costs

Expected benefit is a referenced intended-result node (EM-STR-02 Outcome and Benefit Realization, unassigned) with baseline, target, indicator revision and attribution limits. Two alternatives may reference **one** benefit identity while each carries its own forecast value, uncertainty and realisation window; they are alternatives, so their forecasts are mutually exclusive and are never summed. Risks are WM-KNW-015 references with declared likelihood and consequence scales, horizon and framing — per alternative, never inherited from the shared benefit. Costs are WM-ECO-012 references with currency, price base and basis. Activity, spend and output never establish outcome or causation.

## Time/version/review

Planned, decision, event, effective, observation, ingestion and knowledge times stay distinct, RFC 3339 with explicit offset. Business-case validity is an interval, not the issuance instant. Review triggers: defeated assumption, forecast or scenario divergence beyond a declared threshold, baseline or comparator change, criteria or metric-definition revision, cost-envelope or funding-source change, risk exposure breach, mandate or authority change, gate arrival, horizon expiry. Supersession is explicit and bidirectional; released history is never rewritten.

## Acceptance scenario

Options A and B share benefit **B1**; A carries risks R1/R2, B carries R3 with a wider consequence range. Release **BC-1** pins criteria C-v2, baseline **Do-Nothing**, horizon and price base; decision **D-1** (rationale) is taken at occurrence **O-1** and issued as record **REC-1**, selecting A, with B's rejection ground recorded. The B1 forecast then changes. This creates appraisal revision **BC-2** and, if material, a review trigger — it does **not** mutate BC-1, D-1 or REC-1. Asked "what was decided, and why, as of D-1's date", the system returns REC-1 plus BC-1's digested input package, C-v2, both option estimates and the rejection ground, unaffected by BC-2. A rejected Initiative is cancelled, not deleted: identity, case for change, option set, rationale and cancellation reason remain resolvable. A ticket raised in a tracker, and the approval of D-1 itself, create no Project; only a separate authorizing instrument and typed derivation do.

## Invariants

1. Initiative identity is never reused across the formalization boundary.
2. No ticket, request, approval or budget line mints a Project, Program or operation.
3. Business case is versioned; releases are immutable and superseded explicitly.
4. Business-case release is never a substitute for Initiative identity.
5. Every option set contains an explicit do-nothing baseline or a recorded reason for its absence.
6. Comparison requires one pinned criteria set, horizon, price base and metric revision.
7. Every estimate carries method, scale/unit version and uncertainty; no bare point values.
8. Ordinal bands are not combined arithmetically without a cited rule; value and harm are not netted without a declared commensuration method.
9. A rejected Initiative or alternative retains its basis, evidence and rejection ground.
10. Mandate ≠ approval ≠ funding availability ≠ benefit realisation.
11. Assumption, hypothesis and forecast are distinct and do not convert by relabelling.
12. Two alternatives may share one benefit identity; their forecasts are never summed.
13. A decision is reproducible as-of its date from a fixed, digested input package and pinned criteria.
14. Event, decision, effective, observation and knowledge times remain distinct.
15. Unallocated and blocked referents are never silently promoted.

## Minimal model set

WM-ACT-030 (root, profiled) · WM-KNW-010 + WM-ACT-024 + WM-REC-010 (InvestmentDecision profile) · WM-KNW-016 · WM-KNW-009 · WM-KNW-015 · WM-ECO-012 · WM-ACT-005 / WM-ACT-029 (formalization targets, referenced) · EM-STR-02 Outcome/Benefit and EM-DAT-05 Metric Definition (unassigned, referenced).

## Holds

WM-ACT-030, WM-ACT-029, WM-KNW-009, WM-KNW-016 and WM-ECO-012 are single-provider-waiver reviewable drafts with no independent external review; WM-KNW-010 and WM-KNW-015 are Claude-only with Grok waived. All carry `publishableCanonical: false`. WM-ACT-030 supplies no approved relation rows, and its registry Project parent link stands against its own Initiative-is-not-a-Project invariant. No relation row exists for Initiative→business-case, Initiative→decision, Initiative→budget or the option-mastership split asserted here. WM-ACT-030's coverage checklist must be downgraded to partial for composition and interoperability. Outcome/Benefit and Metric Definition are unallocated. Source and version pins (Green Book 2026, business-case guidance, ArchiMate target, ISO abstracts) are unverified; ISO support is abstract-level only. No crosswalk, mastership confirmation or fixtures exist. This adjudication asserts no canonical completeness, installability or publication readiness.
