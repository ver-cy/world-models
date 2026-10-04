# WM-POL-009 Codex pre-provider boundary

Status: local preparation only. This is not provider output or publication evidence.

## Frozen identity

- Registry: `vr.wm-pol-009`
- Model: `WM-POL-009`
- Name: Court / Arbitration Case
- Candidate kind: aggregate case
- Legacy alias: `A19`
- Approved candidate children: `WM-POL-019`, `WM-POL-020`, `WM-POL-021`

## Boundary hypothesis

The aggregate represents one dispute-resolution proceeding before a qualified forum. It owns case identity, procedural state, forum assignment, party roles, claim references, docket, schedule, hearings, procedural orders and child-record composition. Filings, evidence items and judgments retain their own identities and lifecycles. Forum organizations, parties, representation engagements, underlying disputes, remedies and enforcement also remain external masters.

## Required distinctions

- case versus court, tribunal or arbitral institution;
- dispute and claim versus case and proceeding;
- party identity versus procedural role and representation;
- filing, evidence item and judgment as child models rather than embedded payloads;
- allegation and evidence versus finding of fact;
- procedural order versus final judgment or award;
- decision finality versus appeal, review, set-aside, recognition and enforcement;
- public court record versus confidential or private arbitration record;
- capability, state, transition, affordance, operation, permission, constraint and failure mode.

No model operation may adjudicate a dispute, predict a legally correct outcome or represent a case record as legal advice.
