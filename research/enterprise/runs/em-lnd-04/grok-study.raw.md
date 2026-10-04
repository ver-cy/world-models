Verdict: Accept the proposal with the constraints below. Neither the Strategy candidate nor the Outcome/Benefit candidate requires independent identity. Both are read-only profile/projection constructs. EM-LND-04 covers StrategyLandscape and StrategicAlignment and supplies no target model IDs; allocating a new business ID would invent mastership the landscape does not have.

Strongest evidence: The proposal treats tags, budgets, completion, and portfolio membership as non-probative for alignment and benefit, and it keeps unallocated and blocked referents visible. Missing measurements become owner-addressed findings rather than zeros. Alignment and causal confirmation are tied to assessment, observation, or attributable justified expert judgment, not to membership.

Strongest counterexample: A project that is tagged strategy, budgeted, completed, and a member of a portfolio, with no objective link and no assessment. If a view treated that tag, budget, completion, or membership as alignment or benefit, the proposal would fail. Under the proposal it remains visible and unaligned, and any output→outcome→benefit edge stays a hypothesis.

Identity/mastership: Neither candidate requires independent identity. StrategyLandscape and StrategicAlignment project existing masters only: objectives and targets on WM-KNW-011; measurements on WM-MAT-008 and WM-XCT-025; initiatives and hypotheses on WM-ACT-030; portfolio and project on WM-ACT-029/005; assessments on WM-ACT-034. Strategy and Outcome/Benefit remain unallocated. Reserved WM-ACT-001 Capability has no usable specification and is not a usable master. A profile element has no business identifier distinct from its source master element.

Strategic elements: Objectives and targets come from WM-KNW-011. Initiatives and hypotheses come from WM-ACT-030. Portfolio and project come from WM-ACT-029/005. A project tagged strategy is a tagged project, not a strategic element and not an alignment. An initiative with no objective remains an initiative and is shown as unlinked.

Alignment/causality: An alignment edge exists only when an assessment, an observation, or an attributable justified expert judgment names the pair. Absent that source, the landscape shows the elements as unassessed or unaligned. Causal output→outcome→benefit edges remain hypotheses until a method-bound assessment states the method, the evidence, and the result. Confirmation does not rewrite prior knowledge time. Tags, budgets, completion, and portfolio membership prove neither alignment nor benefit.

Output/outcome/benefit: Output is what an initiative or project produces on WM-ACT-030 or WM-ACT-029/005. Outcome is a change relative to an objective or target on WM-KNW-011. Benefit is a valued consequence of that outcome. None of the three is created by the profile. Outcome and Benefit stay unallocated projections. An unconfirmed chain is shown as a hypothesis, not as an established benefit.

Capability constraint: A constraining capability that points at reserved WM-ACT-001, which has no usable specification, remains visible and blocked. The constraint is not enforceable, not satisfied, and not dropped. No substitute specification is assumed.

Time/scenario: Views separate effective time, knowledge time, and measurement time, and separate authoritative, replay, and scenario classes. Replay reconstructs what was known at a knowledge time; it does not create alignment. A scenario may show a hypothesized alignment or benefit and must not overwrite the authoritative landscape or backdate knowledge.

Findings: An initiative without an objective is a visible gap, not an implied strategy link. An objective without a WM-MAT-008 or WM-XCT-025 measurement produces an owner-addressed finding, never a zero or an inferred score. A strategy-tagged project without an assessment is a non-alignment finding. Unallocated Strategy and Outcome/Benefit referents, and the blocked WM-ACT-001 referent, remain visible findings in every class.

Scenario: Initiative I has no WM-KNW-011 objective link. Objective O has no measurement. Capability C is constraining but blocked because WM-ACT-001 has no usable specification. Project P is tagged strategy, budgeted, completed, and a portfolio member, with no assessment. Expected: all four remain visible; none of tag, budget, completion, or membership creates alignment or benefit; the missing measurement is an owner-addressed finding, not zero; the capability constraint is blocked and unenforceable; any benefit edge stays a hypothesis; a scenario view may hypothesize a link but does not change the authoritative class.

Invariants:

1. Neither Strategy nor Outcome/Benefit profile allocates a new business ID.
2. A profile element has no business identifier distinct from its source master element.
3. Unallocated Strategy and Outcome/Benefit referents remain visible as unallocated.
4. A WM-ACT-001 referent with no usable specification remains visible as blocked.
5. An alignment edge exists only if sourced from an assessment, an observation, or an attributable justified expert judgment.
6. A tag does not prove alignment or benefit.
7. A budget does not prove alignment or benefit.
8. Completion does not prove alignment or benefit.
9. Portfolio membership on WM-ACT-029/005 does not prove alignment or benefit.
10. An output→outcome→benefit edge remains a hypothesis until a method-bound assessment confirms it.
11. An initiative on WM-ACT-030 may exist with no WM-KNW-011 objective and is then shown unlinked, not implicitly strategic.
12. An objective with no WM-MAT-008 or WM-XCT-025 measurement yields an owner-addressed finding, never a zero.
13. A constraining-but-blocked capability is recorded as unenforceable and is not deleted.
14. Effective time, knowledge time, and measurement time are distinct and are not collapsed.
15. Authoritative, replay, and scenario classes are distinct; scenario does not overwrite authoritative status.
16. Confirmation of a hypothesis does not rewrite history at an earlier knowledge time.

Minimum profile shape: A read-only projection that references only the listed master elements; an optional alignment slot typed as assessment, observation, or attributable justified expert judgment; a causality slot typed as hypothesis until a method-bound assessment confirms it; a visibility flag for unallocated and blocked; a time triple of effective, knowledge, and measurement; a class of authoritative, replay, or scenario; and a finding list. No independent Strategy or Benefit identifier.

Blockers: EM-LND-04 has no target model IDs, so the profiles cannot be bound to a new master. Strategy and Outcome/Benefit are unallocated, so a confirmed benefit has no master to land on beyond the confirming assessment. WM-ACT-001 is reserved and has no usable specification, so capability constraints cannot be evaluated. Any consumer that treats tag, budget, completion, or portfolio membership as proof violates the proposal.
