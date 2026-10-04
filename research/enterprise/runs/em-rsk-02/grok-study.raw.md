**Verdict.** Conditionally accept. Do not publish until the WM-ECO-035 / WM-ACT-033 dual-root is resolved by exclusive mastership plus commission composition, and ProcedureDefinition is assigned independent identity. Reject a merged Audit root, a third Audit master, same-instance dual mastership, and any close-path from task, corrective action, management response, or opinion.

**Strongest evidence.** A reusable ProcedureDefinition cited by two engagements and two performed tests must keep one identity and pinned criteria; each performed test then binds its own frame, method and sample. That split is the only way a later opinion can cite a stable design without treating one cell as the group.

**Strongest counterexample.** Engagement covers Process A and Process B at Site Y; Site X is excluded. One performed test hits only A/Y. Finding F is raised. Management response and a WM-ACT-006-profiled corrective action complete; the same actor “rechecks”; the opinion states group-wide conformity. That path collapses exclusion, frame gap, independence, closure and non-extrapolation at once.

**Identity / mastership.** Only ProcedureDefinition needs independent identity: it is the identifier-unassigned reusable candidate. A performed test is execution-local and must cite one mandate-authorized ProcedureDefinition version plus pinned criteria. AuditFinding reuses WM-ACT-033 production and aligns to WM-KNW-007 with no second identity; it is not WM-KNW-014. AssuranceOpinion is an engagement-scoped statement under WM-ECO-035, not a new model. CorrectiveAction profiles WM-ACT-006. “Audit” is a use-label, not an identity.

Resolve the dual-root by composition, not merge: WM-ECO-035 exclusively masters Engagement, Mandate, declared Scope/exclusions and AssuranceOpinion; WM-ACT-033 exclusively masters Execution, performed test, observation, evidence package and AuditFinding. Engagement commissions Execution; Execution reports findings into Engagement; Engagement issues the opinion over declared scope. One execution belongs to one engagement. Overlap attributes are owned once: engagement-level scope/exclusions on WM-ECO-035; test-level criteria application and sampling frame/method/sample on the performed test. Shared wording is reference, not dual storage of the same fact.

**Engagement / execution / procedure.** Execution cannot out-scope or outlive its commissioning engagement. ProcedureDefinition is catalog-level and not owned by one engagement or one execution. Cloning a definition into an execution is a modeling error. A performed test is not a ProcedureDefinition.

**Sampling / evidence.** Frame, method and sample are required on every performed test. Frame gaps are first-class. Evidence is bound to a performed test and a sampling cell (process × site × unit). An excluded site is not a cell and cannot receive evidence or an implied pass. Observation is not evidence. One-system or one-site evidence cannot support group-wide conformity. Criteria are pinned before evaluation; post-hoc change does not re-qualify existing evidence. A clean result on Process A does not fill a frame gap on Process B.

**Finding / issue / risk.** A finding requires pinned criteria, cell-bound evidence and evaluation. Observation alone is not a finding. Finding → WM-KNW-014 Issue is an explicit mapping, not identity merge. A finding may reference a control failure or risk exposure; it does not become the risk, the control or the task. Keep observation, evidence, finding, issue, risk and task distinct.

**Opinion / scope.** Opinion range is declared scope minus exclusions minus recorded frame gaps. The limitations set must list every exclusion and every frame gap. Opinion does not create evidence, does not close findings, does not enlarge execution scope and never proves general compliance.

**Corrective action / closure.** Management response attaches to the finding and answers it; the engagement may collect it by reference only. Corrective action references the finding and does not inherit its identity. Task completion, corrective-action completion and management response never close a finding. Closure requires an independent retest: a new performed test, same pinned criteria, same sampling cell unless a successor cell is declared, executor ≠ corrective-action actor. Failed retest keeps the finding open and adds evidence. The original performed test is immutable.

**Independence.** Opinion issuer is not management of the audited processes. Performed-test executor is not the process owner. Retest executor is not the corrective-action actor. Reuse of ProcedureDefinition does not confer performer independence.

**Scenario.** Engagement E (WM-ECO-035) mandates Process A and Process B at Site Y; Site X excluded; criteria C pinned. ProcedureDefinition PD is cited (independent identity, version authorized by the mandate). Execution X1 (WM-ACT-033) is commissioned and cannot add Site X. Performed test T1 applies PD to A/Y only; frame gaps name untested/undersampled B and excluded X. Observation yields evidence bound to cell A/Y; evaluation against C produces Finding F (WM-ACT-033 / WM-KNW-007 alignment; not WM-KNW-014; not risk; not task). Management response answers F. Corrective action remediates A/Y; the implement task completes; F stays open. Independent retest T2 is a new performed test on PD+C at A/Y by a different executor. Pass may close F; fail leaves F open. Opinion speaks only to tested cell A/Y and must state the X exclusion and B frame gap. One-system evidence is not group-wide conformity.

**Invariants.**
1. Observation ≠ evidence ≠ finding ≠ issue ≠ risk ≠ task ≠ opinion ≠ corrective action ≠ management response.
2. Engagement commissions execution; no subtype either way; no third Audit master; no same-instance dual master.
3. ProcedureDefinition has independent identity; a performed test is execution-local and cites one authorized version plus pinned criteria.
4. Frame, method and sample are required; frame gaps are first-class.
5. Evidence is cell-bound; no extrapolation across an exclusion or frame gap.
6. A finding requires criteria + cell-bound evidence + evaluation.
7. Finding identity is not issue identity; WM-KNW-007 alignment adds no second finding identity.
8. Finding is not a risk or control.
9. Task completion never closes a finding.
10. Corrective-action completion and management response never close a finding.
11. Closure requires an independent new performed test; executor ≠ corrective-action actor.
12. The original performed test is immutable.
13. Opinion range ⊆ scope \ exclusions \ frame gaps; limitations list every exclusion and gap.
14. Opinion never proves general compliance and never closes a finding.

**Minimum model set.** WM-ECO-035 (engagement, mandate, scope/exclusions, opinion); WM-ACT-033 (execution, observation, evidence, finding production); ProcedureDefinition (only new identity); performed test (execution-local); AuditFinding (no new identity; align WM-KNW-007); WM-KNW-014 (distinct issue); WM-ACT-006 profile (corrective action); management response (separate object); sampling frame/method/sample and frame-gap; pinned criteria; risk/control and task as boundaries only.

**Blockers.** Unadjudicated dual-root or same-instance dual mastership; ProcedureDefinition left identifier-unassigned; any close-path from task, corrective action, management response or opinion; retest by the corrective-action actor counted as independent; opinion without mandatory limitations; retest that changes criteria or cell yet closes the original finding; missing criteria, frame/method/sample or exclusions; any rule that lets one-system evidence support group-wide conformity.
