# WM-ACT-049 bounded provider focus

Research a governed aggregate that keeps a CarePlan planning record and an
EpisodeOfCare responsibility-tracking record distinct while connecting goals,
care-team participation, planned requests, performed activity references,
progress evidence and transitions of care. Do not collapse the plan, episode,
encounter, clinical assessment, condition, goal, care team, request, task or
performed event into one lifecycle.

Use current official primary sources. At minimum inspect the permanent HL7
FHIR R5 CarePlan, EpisodeOfCare, Goal, CareTeam, RequestOrchestration,
PlanDefinition, Task, Workflow and ClinicalImpression pages. Cross-check
continuity and person-centred planning against WHO guidance, shared decisions
against NICE NG197, care-plan exchange against IHE Dynamic Care Planning and
workflow expressivity against the retired openEHR Task Planning specification.
Record exact versions, maturity and retirement status rather than implying
normative or current conformance.

Stress-test these semantics:

- a CarePlan describes intended coordinated care, while EpisodeOfCare tracks
  an association and responsibility period; neither is an Encounter;
- a plan may group goals, participants and activity requests, but the request,
  task and performed-event models retain their own identities and states;
- goal lifecycle, achievement and target evaluation are separate from plan
  status and from observations used to evaluate progress;
- plan author, custodian, contributors, care-team members, episode manager and
  managing organization are distinct roles with effective periods;
- reusable protocols and order sets remain PlanDefinition-like external
  definitions; this model records versioned instantiation links and deviations;
- planned, scheduled, authorized, accepted, performed, not-done and evaluated
  are separate assertions with independent sources and times;
- transfers, handoffs and referrals preserve responsibility, pending work,
  discrepancies, participant acknowledgement and communication evidence;
- completion of a plan or episode does not prove that every activity occurred,
  every goal was achieved, care was effective or no harm occurred;
- corrections create successor lineage and do not rewrite released history.

Treat the three ledger relations as candidate metadata. The model may retain
typed references to disease or condition, procedure and medication records,
but it must not approve containment, import their lifecycles or authorize
cascade mutation. The result remains reviewable-draft unless independent
review and release-pinned mappings clear the recorded holds.
