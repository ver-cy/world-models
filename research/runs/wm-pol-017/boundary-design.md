# Boundary and serialization handoff

Proposed entry_kind: entity. Root is a persistent administrative case instance,
with referenced process definition and chronological procedural events. Do not
choose aggregate solely because a case has several records, and do not call it
an event merely because its lifecycle involves acts.

Candidate composition:
- WM-ACT-021: ALIGN generic case context; no ratified inheritance.
- WM-REC-009: optional REFERENCE to application/request record. Registry COMPOSE
  candidate must not force an application on ex officio cases.
- WM-REC-010: optional REFERENCE to decision/approval record; active cases may
  have no decision, and some outcomes require other record types.
- WM-POL-016: REFERENCE to competent institution, subject to verified boundary.
- CMMN, CPSV-AP and PROV-O: selected ALIGN mappings only; no runtime conformance.

Potential six local record functions: resolve-case-reference, record-intake,
link-case-evidence, record-procedural-event, record-outcome-reference,
export-authorized-case-projection. All must have authority, source, expected-head
where writing, effects and refusal conditions. None files an application, serves
a notice, issues a decision, starts an appeal or decides rights.

Required service guards: master-qualified case IDs before UUID fallback; RFC
3339 seconds and offset for recording instants, preserving separate date-only
legal times; uncertainty in service/deadline calculations; restricted participant
views; no personal identifiers in filenames; retention/legal holds; local erasure
does not annul decisions. All eight service sections and AGENTS.md required.

Publication holds: absent external review if both attempts fail; selected legal
sources and German/EU scope, outdated data-protection cross-reference in Code,
failed US source fetches, no full deadline/appeal engine, nested-schema and
mapping gaps. Evidence attribution is not truth or legal admissibility.
