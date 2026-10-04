# WM-ACT-021 pre-Claude research pack

Status: local preparation only. This is not provider output, adjudication,
synthesis or publication evidence. Claude must independently check the frozen
boundary and live sources while the shared lease is held.

## Frozen boundary

- Registry identity: `vr.wm-act-021`
- Model identity: `WM-ACT-021`
- Registered name: Service Case / Ticket
- Record-plane kind: `standalone-mm`
- Candidate subject-model kind: `aggregate`, because a case is the stable root
  for participants, communications, classifications, status history, evidence,
  service commitments and resolution outcome.
- Known-relation contract: empty. Proposed composition below is therefore
  provisional and must not be represented as registered.
- Previous-version material: none registered.

The model owns the governed case record and its case-specific lifecycle. It does
not own generic person or organization identity, communication transport,
generic documents, service-level policy design, work execution, audit-log
machinery, access-policy evaluation or knowledge articles. Those concepts are
references or future relationship proposals.

## Primary evidence ledger

| ID | Authority and source | Version or date | Use in this model |
| --- | --- | --- | --- |
| SRC-001 | ISO, [ISO 10002:2018](https://www.iso.org/standard/71580.html) | Edition 3, confirmed 2023 | Complaint receipt, tracking, acknowledgement, assessment, resolution, feedback, analysis and process review; excludes external dispute resolution and employment disputes. |
| SRC-002 | Microsoft, [Case-to-resolution introduction](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/case-to-resolution-introduction) | Live guidance, accessed 2026-09-04 | Multi-channel intake, customer identification, case logging, queue assignment and case-to-resolution operating flow. |
| SRC-003 | Microsoft, [Resolve, cancel, and reassign cases](https://learn.microsoft.com/en-us/dynamics365/customer-service/use/customer-service-hub-user-guide-resolve-cancel-reassign-a-case) | Updated 2026-07-30 | Resolution, cancellation, reassignment, parent-child cases and resolution history. |
| SRC-004 | Microsoft, [Overview of service-level agreements](https://learn.microsoft.com/en-us/dynamics365/customer-service/use/overview-service-level-agreements) | Updated 2026-08-25 | Entitlement-linked support terms, response and resolution KPIs, warning and breach states, and business schedules. |
| SRC-005 | Atlassian, [Jira Cloud REST API v3: Issues](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/) | Live API v3, accessed 2026-09-04 | Create, edit, assign, transition, archive, retrieve and inspect changelogs for an issue-like case aggregate. |
| SRC-006 | Zendesk, [Tickets API](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/) | Live API, accessed 2026-09-04 | Requester versus submitter, assignee, collaborators, public visibility, priority, status categories, comments, safe updates and restricted access. |
| SRC-007 | W3C, [PROV-O](https://www.w3.org/TR/prov-o/) | Recommendation, 2013-04-30 | Portable provenance alignment for entity, activity, agent, attribution, association and derivation. |
| SRC-008 | IETF, [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) | RFC 3339, 2002-07 | Timestamp representation with explicit timezone offset; event and observation or ingestion times remain distinct. |

All eight sources are authoritative first-party or standards-organization
sources. Vendor sources show interoperable common practice, not universal
normative semantics. ISO 10002 applies specifically to complaints and therefore
supports a profile of the broader case model rather than defining every case.

## Proposed context structure

1. Case identity and classification
   - Identity: authoritative case number, governed global identifier, local UUID
     or ULID, source channel, tenant or jurisdiction scope.
   - Classification: case type, category, subject, description, severity,
     impact, urgency and priority with scheme identifiers and versions.
   - Relationships: duplicate, related, parent, child, originating interaction,
     affected subject and external references.
2. Parties, ownership and participation
   - Originator roles: requester, submitter and represented party must remain
     distinguishable.
   - Handling roles: owner, queue, assignee, collaborators and accountable
     service owner, all by reference.
   - Contact and visibility: preferred channel, public versus restricted
     communications and party-specific disclosure constraints.
3. Intake and triage
   - Intake: channel, received time, occurrence time, acknowledgement and
     completeness checks.
   - Triage: routing decision, priority rationale, duplicate detection and
     acceptance, rejection or redirection.
   - Entitlement: applicable support entitlement, service commitment and
     business-calendar references, without owning the policies themselves.
4. Case lifecycle and coordination
   - Status: proposed normalized categories `new`, `open`, `pending`, `hold`,
     `resolved`, `closed`, `cancelled`, with adopting-Dimension extensions.
   - Transition history: from and to status, actor, authority, reason, event
     time, recorded time and immutable provenance.
   - Assignment and escalation: assignment history and escalation requests;
     downstream work execution and generic workflow engines remain out of scope.
5. Communications, evidence and knowledge
   - Case communications: message references, author role, audience, public or
     restricted flag and chronology; transport remains external.
   - Evidence: attachment or document references, integrity value, provenance,
     sensitivity, collection context and retention class.
   - Knowledge: knowledge-item references, suggested answer and applicability;
     content lifecycle remains external.
6. Service commitments and outcome
   - SLA instances: policy and entitlement references, KPI target, start,
     warning, due, pause intervals and attained or breached result.
   - Resolution: resolution category, explanation, supplied remedy, resolver,
     resolution time and linked evidence.
   - Closure and reopening: acceptance or confirmation, closure reason,
     reopened-from relation and new evidence or changed circumstance.
   - Feedback: satisfaction or appeal reference and improvement signal, without
     owning external dispute or corrective-action processes.
7. Governance, retention and interoperability
   - Access: deny by default; grants at bundle, layer, finding and artifact
     scope; field or comment visibility can further restrict access.
   - Retention: retention class, legal or investigation hold, disposition due
     time, tombstone and deletion authority. An adopting-Dimension retention
     service executes disposition.
   - Integrity and provenance: version or etag, safe-update precondition,
     content hashes and W3C PROV alignment.
   - Interoperability: external system and field mappings are versioned
     projections; no vendor's statuses become universal Vercy semantics.

## Candidate functions

- Register a case from an authorized intake event.
- Validate required identity, classification and party references.
- Classify and prioritize using a named governed scheme.
- Link duplicates, parent-child cases and related records without merging their
  identities silently.
- Assign or reassign the case and preserve assignment history.
- Apply an authorized lifecycle transition with preconditions and reason.
- Record a case communication or evidence reference with visibility metadata.
- Evaluate case-specific SLA clocks from referenced policy and calendar inputs;
  policy design and scheduling engines remain external.
- Escalate by emitting a governed escalation request.
- Record resolution, closure, cancellation or reopening with provenance.
- Export a permission-filtered projection with mapping version and provenance.
- Apply retention disposition only through the referenced policy authority.

## Adversarial questions for Claude

- Is `aggregate` justified, or should the semantic root be a narrower `entity`
  with comments, evidence and SLA instances entirely external?
- Can a generic lifecycle be stated without conflating incident management,
  customer support, complaints, legal cases and internal work items?
- Which status distinctions are semantic and which are vendor projections?
- Does SLA evaluation belong here, or only the bindings and observed KPI state?
- Are requester, submitter, affected party and beneficiary sufficiently distinct?
- How are confidential comments and attachments protected when a case itself is
  visible to a broader audience?
- What prevents closing a case from being interpreted as factual resolution or
  customer acceptance?
- How are duplicate linking and merging represented without losing identifiers,
  provenance, holds, permissions or appeal rights?
- Which deletion operations must become tombstones because evidence, legal hold
  or audit requirements prevent erasure?
- Which proposed sibling-model links are defensible despite the frozen empty
  relationship ledger, and must therefore remain explicit holds?

## Coverage and holds

Identity, lifecycle, relationships, temporal, provenance, ownership,
validation, access, retention and deletion, and interoperability are all
represented in the proposed structure. Spatial context is optional and belongs
as a reference to the affected subject or location when relevant.

Open holds:

- Claude independent research and no-tools adversarial adjudication have not run.
- Live source versions and detailed field mappings require provider verification.
- The frozen relationship contract is empty; all composition links are proposals.
- Cross-domain profiles for complaint, incident, request, defect and regulatory
  case require separate validation before any completeness claim.
- Jurisdiction-specific confidentiality, evidence, appeal and retention rules
  remain adopting-Dimension policy.


## Agent-native five-facet gate

This gate applies the owner-approved Agent-Native Reality direction dated
2026-09-05. Claude must adjudicate each status and may narrow it only with an
explicit boundary reason.

1. Identity and class - required: stable identity, master system, class and
   subclass criteria, part-whole boundary, class-definition version and
   instance-distinguishing features.
2. Direct properties - required: direct properties are the subject-specific legal, logical, informational, organizational or computational facts; fictitious physical fields are forbidden.
3. Recognition and observation - optional: define logical or evidential recognition criteria when instances can be confused; otherwise explain why authoritative identity is sufficient.
4. Capabilities, behaviour and possible actions - required: distinguish what the subject can do or undergo, its observed behaviour and state, and what an authorized agent can do with it.
5. Context and evidence - required: creation or origin, owner and steward,
   location or logical environment, history, events, applicable rules, access,
   retention, source, observation time, confidence, freshness and mastership.

Abstract-object gate: use only meaningful domain metrics with named scale or unit, method, uncertainty and observation time. Geometry, mass, color or other physical properties must not be fabricated.

The semantic review must keep these terms separate:

- capability: an intrinsic capacity of the subject;
- behaviour: an observed or expected response under stated conditions;
- state: a condition at a point or interval;
- transition: an authorized or observed change between states;
- affordance: an action available to an external actor or agent;
- operation: an action contract with inputs, tools, preconditions and outputs;
- effect: the asserted postcondition, including side effects;
- reversibility: whether and how effects can be undone or compensated;
- permission: authority for an actor to attempt an operation;
- constraint: a limit, compatibility rule or prohibition;
- hazard: a condition with potential harm;
- failure mode: how intended capability or operation fails and how failure is
  detected, contained and recovered.

The eventual model AGENTS.md must route an agent through filling, extension,
patching, editing, validation and retirement, define pre-write and post-write
checks, identify autonomous versus confirmation-required operations, resolve
child models and master systems instead of duplicating them, and link
https://ver.cy/model-agent-protocol.md after that protocol is published.