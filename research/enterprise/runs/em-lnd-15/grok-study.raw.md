**Verdict.** Accept the proposal with conditions. Neither RiskLandscape nor AssuranceCoverageView requires independent subject-model identity. RiskLandscape is a governed view definition with immutable snapshots. AssuranceCoverageView is a projection that is ill-formed without an explicit denominator. Applicability is an assessment. Coverage, compliance, assurance and residual risk stay distinct. Control existence, design, implementation, operation and effectiveness stay independent. Risk reduction requires current, same-scenario determinations. Exceptions retain scope and expiry; expired conclusions remain readable but not current. Aggregation requires comparable criteria and non-strippable caveats. Completed cards do not prove conformity. Control remains an identifier-unassigned candidate after WM-XCT-027; that is an implementability blocker for facet rules, not a grant of landscape subjecthood.

**Strongest evidence.** A landscape is a cut of a population. Giving the cut subject identity creates landscapes-of-landscapes, competing “the” landscapes, and double-count on aggregate. Coverage without a declared denominator is unreproducible. The required tests force the remaining cuts: a control can exist and be designed with no execution, so no facet entails another and no residual-risk credit follows; a requirement can exist with no applicability assessment, so missing applicability is undetermined, not N/A and not compliant; an expired exception must stay readable with scope intact and still cannot authorize live treatment. Observation masters evidence (WM-KNW-015 posture); activity completion (WM-ACT-033 posture) is not a conformity determination.

**Strongest counterexample.** A board-approved “Q3 risk landscape” with steward, effective dates and a duty to keep it current looks like a subject. That object is definition-plus-snapshot governance, already in the proposal. Citation and approval are not subjecthood. The harder counterexample is Control itself: the “control without execution” test cannot hang facets on an unidentifiable subject. That blocks closing control-facet implementability; it does not transfer subject identity onto the views.

**Identity / mastership.** Definition/registry identity ≠ subject-model identity. RiskLandscape may have a definition-id and snapshot-id for citation, approval and compare. AssuranceCoverageView may have a projection/run identity so a number cites its denominator. Neither is a subject that can bear obligations, own residual risk, or be the target of controls. Mastership stays with assessment, requirement, obligation and observation. Snapshots master nothing; they freeze references. Projections master nothing; they compute. Views must not mint Control as a resolved subject.

**Scope / requirements.** Scope lives in the view definition (population selector, taxonomy, scenario-set, criteria). A requirement is a master and is not in force for a unit until an applicability assessment relates it to that unit × time × scenario. Missing applicability excludes the requirement from that unit’s denominator and obligation set. Absence is not inapplicable.

**Risk / control boundary.** Views do not bear risk. Residual risk is a current risk determination after only current, in-scope, effective treatments. A control-like record does not rewrite inherent risk. Coverage of activity is not treatment. Exceptions can narrow obligation or applicability; they do not make a control effective and do not reduce residual risk by themselves. Do not park Control identity inside these views.

**Coverage / effectiveness.** One projection, one measure-type. Coverage is share of an explicit denominator meeting a numerator rule (assessment done, observation present)—not a quality judgment. Compliance requires a current applicability assessment first. Assurance is warranted confidence from an assurance activity with scope and criteria; coverage does not imply it. Residual risk is not a coverage percentage. Effectiveness is a time-and-scenario-bound determination. It is not implied by existence, design, implementation, operation, coverage, completed cards, or unexpired exceptions.

**Assessments / audits / findings.** Applicability, design, operation, effectiveness, compliance and residual risk are assessments (or conclusions of assessments), not attributes of the view. Observation masters evidence. Findings and completed cards remain observations. An audit is an assurance activity; its output does not convert coverage into assurance or cards into conformity.

**Exceptions / validity.** An exception is a scoped, time-bounded conclusion over a requirement or obligation. Essential: scope, cited obligation/requirement, stated effect, expiry, issuing assessment. Valid when in-scope, not expired, not superseded, and time/scenario-matched. After expiry the record stays readable and scope-retaining; it is not current and cannot authorize live treatment, coverage carve-out, or risk-reduction credit.

**Time / scenario.** Every current determination, snapshot and projection is parameterized by as-of time and scenario. Current means not superseded, not expired, and time/scenario-matched. Snapshots bind both and are immutable. Cross-scenario or cross-criteria aggregation is forbidden unless comparability is explicit.

**Scenario.** T0: Requirement R exists; no applicability assessment for unit U. Control C exists as a design record; no execution. Exception E granted for U×R with scope S and expiry t1. T1 (t < t1): R does not enter U’s denominator; absence ≠ inapplicable. C may have existence and design; implementation, operation and effectiveness remain undetermined; no residual-risk credit. E is current within S only. T2 (t > t1): E remains readable with S intact; E is not current; no carve-out. Still no execution ⇒ no operation/effectiveness for C. Still no applicability ⇒ R not binding on U. Cards completed at T1 do not prove conformity at T2.

**Invariants.**

1. View-not-subject: neither candidate is a subject master.
2. Snapshot immutability: no in-place update; body frozen.
3. Snapshot currency is derived at read time, never edited in.
4. Projection without explicit denominator is ill-formed.
5. Views are not obligation-targets and do not own residual risk.
6. Applicability is an assessment; missing ≠ inapplicable.
7. Coverage ≠ compliance ≠ assurance ≠ residual risk.
8. Control facets do not entail one another.
9. Risk reduction requires current, same-scenario determinations.
10. Exception scope and expiry are essential; expired ⇒ readable, not current.
11. Aggregation requires comparable criteria; caveats are non-strippable.
12. Completed cards do not prove conformity or effectiveness.
13. Views mint no subject facts.
14. Numerator items must sit in the declared denominator and have a current in-scope determination of the coverage criterion.
15. A determination without time/scenario is not current.
16. Undetermined is first-class; no coerce to 0, N/A, compliant or effective.
17. No view may treat Control as a resolved subject master.

**Minimum profile shape.**

- View definition: registry definition-id; version; steward; purpose; population selector; taxonomy ref; aggregation rules; caveat-retention rule; currency rule; time-basis; scenario-basis; allowed measure set (unmixed).
- Snapshot: snapshot-id; viewDef-version; taken-at; scenario; included-master refs; undetermined-applicability set; excluded+reason; caveats bound to each aggregate; frozen hash; current flag derived.
- Coverage projection: projection-id (cite-only); viewDef-version; explicit denominator spec (mandatory); numerator rule; single measure-type; as-of; scenario; counts; caveat set; completed-card-not-conformity rule.
- Exception: scope; obligation/requirement ref; effect; expiry; issuing assessment; current flag derived.
- Assessment: subject ref; criterion; time; scenario; conclusion; caveats.

**Blockers.** Control identity still unassigned after WM-XCT-027: facet independence is stateable but not implementable until Control is identified or facets are re-homed onto assigned masters (assessment, obligation, observation, or WM-ACT-033 activity). Denominator and snapshot must bind view-definition version. Currency rule must live on the landscape definition. Caveats must survive UI and export. Completed-card observations must not satisfy numerator rules that claim compliance, assurance or effectiveness. Expired exceptions must stay out of current denominators. Incomparable criteria block aggregation and trend-as-reduction.

**Identity decision.** Neither candidate requires independent subject-model identity. Registry and citation identity for definition, snapshot and projection-run are required for governance and are not subjecthood.
