# EM-TEC-05 local synthesis

## Disposition

- Reuse WM-ACT-020 for Cyber Incident and create an operational/service-incident profile over WM-ACT-019 after its emergency-focused legacy specification is rewritten.
- Profile reserved WM-KNW-014 as the persistent Problem master and reserved WM-SFT-014 as the versioned software Defect master.
- Reuse WM-ACT-006 Task for triage, containment, restoration and permanent remediation work. ResponseAction does not need a new model.
- Keep ImpactAssessment as an identified, revisioned assertion inside the incident aggregate.
- Give RootCauseClaim independent record identity and evidence lifecycle inside WM-KNW-014 Problem. Incidents reference it; it does not require a separate model ID.
- Allocate no runtime or model identifier.

## Identity and mastership

Operational incidents, cyber incidents, problems and defects remain distinct records with distinct authorities and lifecycles. Observation and event records stay mastered in observability or event stores and are referenced by membership assertions. An event becomes an incident only through a declaration decision carrying authority, definition binding, rationale, confidence and effective time.

A cyber incident additionally qualifies against a security definition concerning confidentiality, integrity, availability or authenticity, or a policy/legal effect. One occurrence may support both an operational incident and a cyber incident; the two records correlate without merging.

Problem is the persistent underlying condition and relates many-to-many with incidents. Defect is a fault in a versioned software artifact and may be the subject of a root-cause claim, but process, configuration and organizational causes need no defect. Task owns assignment, priority and completion. Restoration tasks reference incidents; permanent remediation tasks reference problems and, when relevant, defects.

## Impact and root cause

ImpactAssessment is incident-scoped and carries assessor, actual/potential status, domain, method, quantities and effective time. It is revisioned rather than overwritten.

RootCauseClaim carries a stable claim key, proposition, evidence references, confidence, claimant, timestamps and status such as proposed, supported, disputed, superseded or rejected. Competing claims coexist. Incident-local hypotheses may exist before a problem is opened; promotion to a problem preserves lineage and leaves incident references.

## Lifecycle and scenario

Incident lifecycle distinguishes reported, declared, contained, restored and closed. Problem lifecycle distinguishes open, cause-claimed, remediation-planned, remediated and closed. `restored_at` records service recovery and does not prove cause elimination.

Three incidents link to one problem. A temporary workaround restores and closes the incidents. Two competing cause claims remain, one supported and one disputed. A permanent remediation task referencing a defect stays open, so the problem remains open. Incident closure performs no cascade to the problem, claims, defect or tasks.

## Invariants

1. Every cause claim has evidence references and explicit confidence.
2. Competing claims coexist; supersession is recorded.
3. Incident closure never closes a problem, cancels a task or retracts a claim.
4. Problem closure requires a supported cause claim and terminal remediation tasks.
5. Severity is incident-owned; priority is task-owned; mappings are explicit but do not merge them.
6. Restoration and cause elimination have separate assertions and times.
7. Incident status requires a declaration decision with authority and definition.
8. Observations and events are referenced, not mastered inside incidents.

## Holds

WM-ACT-019 needs a rewritten current specification and downstream migration mapping; WM-KNW-014, WM-SFT-014 and WM-ACT-006 lack current specifications; the WM-ACT-020 compose edge conflicts with its intended reference boundary; WM-ACT-021 parentage is unresolved; incident/problem master systems and event/evidence references need allocation and pins; WM-ACT-020 still has an independent-review hold. This checkpoint makes no canonical completeness, installability or publication claim.
