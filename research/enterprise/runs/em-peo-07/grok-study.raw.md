Verdict: Conditionally acceptable. The proposed separations hold if Absence, Worklog and Timesheet receive independent identity, Time Approval stays an append-only decision inside Timesheet, and Work Calendar and Availability remain derived projections. Capacity must be closed on contractual pattern, calendar, absence and allocation only. Worklog must not enter residual capacity and must not be treated as proof of presence or quality. Blockers below prevent unconditional acceptance.

Strongest evidence: The proposal already separates contractual pattern, calendar, absence, planned availability, assignment allocation and actual work, and it states the rules that keep those separations intact: missing is unknown not zero; medical reason is excluded from ordinary availability; every interval carries offset, timezone and ruleset release; nominal and exact durations stay distinct; overlaps are retained and flagged; approved periods are immutable and corrections are additive. WM-ACT-008 is correctly held reference-only. Work Calendar profiling WM-XCT-009 as a projection, and Availability as a projection, match those boundaries.

Strongest counterexample: Half-time engagement (0.5 contractual pattern) with two project allocations that together equal that pattern, on a DST fall-back day with a repeated local hour. Two worklogs both claim the repeated hour and overlap. An already-approved timesheet is then “corrected” by rewriting the approved interval, and residual capacity is recomputed by subtracting worklog exact duration from nominal availability. The result is either double capacity (both worklogs summed into the repeated hour) or a negative residual. That fails missing=unknown, nominal≠exact, overlap retention, approved immutability, additive correction, and the ban on worklog as presence or quality evidence.

Identity/mastership: Independent identity is required for Absence, Worklog and Timesheet. They are identifier-unassigned new-model candidates with their own lifecycles (fact, reported observation, period container) and cannot be projections of person, employment, assignment, task, WM-XCT-009 or WM-ACT-008. Time Approval does not require a peer model identity; it is an append-only decision identified inside Timesheet (timesheet identity plus sequence). Work Calendar does not; it profiles WM-XCT-009. Availability does not; it is computed. No identifiers are assigned here.

Calendar/pattern: Contractual pattern is the employment-scoped nominal commitment (for example half-time). Work Calendar is a derived profile of WM-XCT-009: offset, timezone, ruleset release, and the distinction between nominal and exact duration. It does not own pattern, absence or allocation. WM-ACT-008 remains a plan/schedule reference, not the master of these facts.

Absence/privacy: Absence is an independent person/employment-scoped fact. Medical reason is structurally excluded from ordinary availability, not merely hidden by policy. An ordinary availability view may see that capacity is reduced; it must not see the medical reason. Missing absence is unknown, not zero.

Availability/allocation: Availability is the derived projection of pattern ∩ calendar − ordinary absence, bounded by assignment allocation. Two project allocations may partition that residual; they must not exceed it. Worklog does not consume residual. Allocation is planned commitment, not actual work.

Worklog: Worklog is an independent reported observation of actual work against an assignment or task. It is not proof of presence, productivity or quality. Overlaps are retained and flagged, not collapsed. A missing worklog is unknown, not zero hours. Exact duration is stored separately from nominal duration.

Timesheet/approval: Timesheet is an independent period container that references worklogs and the planned allocations in scope. Time Approval is an append-only decision inside that container. An approved slice is immutable. A later decision does not rewrite it.

DST/overlap: Every interval binds offset, timezone and ruleset release, so a skipped hour (spring-forward) and a repeated hour (fall-back) are unambiguous. Nominal duration is not rewritten to equal exact duration. Overlapping worklogs on the repeated hour stay flagged observations; they are not additive capacity.

Corrections: Approved periods are immutable. A correction is a new additive decision that references the prior approval. It does not delete, overwrite or negate history in place. Residual capacity is recomputed from pattern, calendar, absence and allocation, not by rewriting the approved snapshot.

Scenario: Person under a half-time contractual pattern, Europe/Athens, ruleset release fixed. Spring-forward day has 23 exact hours and a shorter nominal window. Two assignments each take half of the 0.5 pattern, so residual after allocation is zero. No ordinary absence. Two worklogs overlap on the transition and are retained and flagged; they do not change availability or residual. Timesheet aggregates the reported observations for the period. Approval freezes that slice. A later correction is appended and linked; the approved slice is unchanged; residual stays non-negative and is not double-counted. The same rules hold on a fall-back repeated hour.

Invariants:

1. Missing is unknown, never zero.
2. Worklog is observation only, not proof of presence, productivity or quality.
3. Medical reason is excluded from ordinary availability.
4. Every interval carries offset, timezone and ruleset release.
5. Nominal duration and exact duration remain distinct.
6. Overlaps are retained and flagged, never silently collapsed.
7. Approved periods are immutable.
8. Corrections are additive and reference the prior approval.
9. Availability is derived, not a master.
10. Work Calendar profiles WM-XCT-009 and has no independent mastership.
11. Allocation cannot exceed pattern residual after ordinary absence.
12. Worklog sum does not consume contractual capacity.
13. Time Approval identity is scoped inside Timesheet.
14. Residual capacity is never negative and never double-counted.
15. WM-ACT-008 is reference-only.

Minimum model set: Contractual pattern (employment boundary); Work Calendar as derived profile of WM-XCT-009; Absence (independent identity); assignment allocation (assignment boundary); Availability (derived); Worklog (independent identity); Timesheet (independent identity); Time Approval as append-only decision inside Timesheet. WM-ACT-008 reference-only. Person, employment, assignment, task and observation remain boundary types, not substitutes for the three new identities.

Blockers: Identifiers for Absence, Worklog and Timesheet are still unassigned, so master references cannot be closed. The non-negative residual rule is not yet specified as pattern ∩ calendar − ordinary absence − allocation, with overlap flags non-summable and worklog excluded. Medical exclusion must be structural. Approved immutability needs an explicit supersession link that does not rewrite history. Until those four are closed, the DST, half-time, dual-allocation, overlap and correction cases are not safe.
