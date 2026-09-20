# WM-ACT-020 Cyber Incident local preflight

Status: local preparation for later independent Claude research. This file is not provider evidence, a synthesis, or a publication artifact.

Sequence: 93

## Frozen boundary decision

The aggregate root should be a cyber incident: an occurrence or linked set of occurrences determined to have actually or imminently jeopardized the confidentiality, integrity, availability, authenticity, or lawful operation of in-scope digital systems, information, services, networks, or computer-controlled infrastructure. The incident owns its identity, declaration basis, observed chronology, affected-scope assertions, impact assessments, classification, status, incident-to-event grouping, evidence references, and outcome facts.

The model must not absorb:

- generic vulnerability lifecycle or remediation, which remains a reference to WM-SFT-006;
- response-case workflow, responder tasks, containment/recovery actions, notifications, playbooks, or lessons-learned execution, which remain in WM-ACT-042;
- generic threat actor, campaign, indicator, control-baseline, asset, software, person, organization, access-control, audit, or evidence-record lifecycles;
- legal conclusions or regime-specific reporting workflows. The incident may carry classifications and obligation bindings by reference, with provenance and jurisdiction.

The frozen `COMPOSE` edge to WM-ACT-042 conflicts with the stated instance semantics, "is handled by", and with an independently governed response case. Claude must test whether the edge should remain COMPOSE, be treated as a one-way case binding, or be held for registry reconciliation. No local retyping is authorized.

## Proposed coverage structure

1. Identity and declaration
   - incident identity and aliases
   - event-to-incident determination and declaration authority
   - duplicate, merge, split, supersession, and reopen identity rules
2. Occurrence and chronology
   - constituent cyber events and causal/temporal ordering
   - occurrence, detection, observation, declaration, and knowledge times
   - ongoing, intermittent, recurring, and imminent incidents
3. Affected scope
   - affected systems, services, information, identities, organizations, and locations by reference
   - dependency and supply-chain reach
   - confirmed, suspected, and disproven affected-scope assertions
4. Security effect and impact
   - confidentiality, integrity, availability, authenticity, policy, and lawful-operation effects
   - operational, safety, privacy, financial, societal, and cross-border impact assertions
   - severity/classification scheme bindings with method, version, assessor, confidence, and effective time
5. Cause, mechanism, and attribution assertions
   - exploit/vulnerability references without owning vulnerability lifecycle
   - observed vectors, techniques, indicators, and threat/campaign references
   - hypothesis, confidence, competing explanations, and revision history
6. Evidence and provenance
   - observations, reports, technical artifacts, custody/preservation references, and source reliability
   - fact versus assessment versus allegation
   - redaction, disclosure marking, retention binding, and provenance chain
7. Incident state and resolution facts
   - declared state vocabulary distinct from response workflow state
   - impact cessation, persistence, recurrence, and residual exposure
   - closure/reclassification basis as incident facts, while action execution stays in WM-ACT-042

Each later finding should contain at least three discriminating questions and choose exactly one representation: owned artifact(s), or a substantive inline-only rationale.

## Candidate artifacts

- incident record and stable identifier assertion
- declaration and reclassification record
- constituent-event map and incident chronology
- affected-scope assessment
- impact and severity assessment
- cause/mechanism hypothesis set
- incident evidence index containing references, not target-owned evidence payloads
- incident status and resolution statement

Artifact ownership must be tested against WM-ACT-042. Response plans, action logs, situation reports, regulator submissions, recovery verification, and lessons-learned records are not owned here.

## Candidate functions

- register incident
- declare or revoke incident determination
- link or unlink constituent event
- revise affected scope
- assess impact and severity
- record causal or attribution hypothesis
- merge, split, or supersede incident identity
- transition incident factual state
- bind response case by reference
- issue incident fact projection subject to access and disclosure policy

Functions must mutate incident-owned state only. They must not execute response, remediation, enforcement, notification, access evaluation, or audit persistence.

## Primary source set for Claude verification

- NIST SP 800-61 Rev. 3, April 2025: https://doi.org/10.6028/NIST.SP.800-61r3
- NIST CSRC Cybersecurity Incident glossary entry: https://csrc.nist.gov/glossary/term/Cybersecurity_Incident
- IETF RFC 7970, IODEF Version 2: https://www.rfc-editor.org/rfc/rfc7970
- OASIS STIX Version 2.1, Incident object and relationship semantics: https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html
- EU Directive 2022/2555 (NIS2), incident and significant-incident definitions and Article 23: https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- EU Regulation 2016/679 (GDPR), personal data breach definition and Articles 33-34: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- CISA National Cyber Incident Response Plan and severity schema: https://www.cisa.gov/sites/default/files/ncirp/National_Cyber_Incident_Response_Plan.pdf
- FIRST Common Vulnerability Scoring System v4.0 specification, for the boundary between vulnerability severity and incident impact: https://www.first.org/cvss/v4.0/specification-document

Live resolution, exact versions, clause support, and independent-organization diversity must be checked again by Claude. The local pass verified discoverability only for the NIST, RFC Editor, ENISA/CISA surfaces; it does not claim that every normative body above was fully extracted.

## Required adversarial checks for the later Claude pass

- Do event, adverse event, alert, compromise, breach, security incident, cyber incident, crisis, and response case remain distinct?
- Can one incident contain multiple events and can one event participate in more than one incident assessment without corrupting identity?
- Are observation time, occurrence time, detection time, declaration time, awareness time, and reporting-clock starts kept separate?
- Are severity and impact versioned assessments rather than immutable incident identity fields?
- Are unconfirmed scope, cause, attribution, and victim assertions explicitly epistemic and reversible?
- Does every response-oriented field belong instead to WM-ACT-042?
- Does every vulnerability-specific field belong instead to WM-SFT-006?
- Are confidentiality restrictions and disclosure markings prevented from becoming authorization decisions owned by this model?
- Are closure and resolution defined as incident facts rather than proof that remediation or recovery work succeeded?

## Holds carried forward

- Single-provider hold remains mandatory after Claude because Grok is waived.
- Independent-review hold remains mandatory; the later no-tools adjudication cannot add facts or substitute for a second provider.
- Boundary hold on the frozen COMPOSE relation to WM-ACT-042.
- Migration hold because the previous S8 card combines vulnerability, threat, incident, response, controls, and posture that now belong to separate models.
- Source-verification hold until every cited URL, version, and clause is re-resolved in the provider pass.
## Agent-native five-facet applicability

Roadmap authority: R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\docs\roadmap\VERCY-AGENT-NATIVE-REALITY-2026-09-05.md.

| Facet | Applicability | Reason |
| --- | --- | --- |
| 1. Identity and class | required | WM-ACT-020 needs stable instance identity, master-system provenance, class/subclass criteria, definition version, composition boundary and distinguishing characteristics. |
| 2. Direct properties | required | The subject is non-physical or primarily relational/event/informational. Record its own legal, logical, organizational, computational or informational properties; do not invent geometry, mass, colour, material or other physical fields. |
| 3. Recognition and observation | required | An agent must know the necessary/sufficient recognition signals, confusable classes, observation method and conditions, confidence, uncertainty and supporting evidence. External recognizers or datasets are referenced rather than embedding model weights. |
| 4. Capabilities, behavior and possible actions | required | The model is active, event-like, process-like or executable. It must distinguish what the subject can do or undergo, observed behavior, state, transition, allowed action, preconditions, effects, reversibility, permission, constraints, hazards and failure modes. |
| 5. Context and evidence | required | Creation/origin, owner/steward, place or jurisdiction, history, relationships, applicable rules, access, privacy, retention, source, observation time, trust, freshness and canonical master system are needed for safe agent use. |

Abstract-object rule: physical measurements are not applicable unless the assertion explicitly concerns a referenced physical subject. Numeric values still require unit or code system, method, effective/observation time, uncertainty and provenance where meaningful.

### Action-semantics gate

Claude and the later adjudicator must keep these concepts separate:

- capability: what the subject can intrinsically do or undergo;
- behavior: what is observed under stated conditions;
- state: a condition at a time, not an action;
- transition: a governed state change with trigger and prior/next state;
- affordance or admissible action: what an agent or actor can attempt with the subject;
- operation: declared inputs, tools, preconditions, effects and result;
- precondition: what must already hold;
- effect: the intended and collateral state changes;
- reversibility: whether and how effects can be undone or compensated;
- permission: who is authorized, by which policy or mandate, and whether confirmation is required;
- constraint: compatibility, invariant, limit or prohibition;
- hazard: a condition with potential harm, distinct from an observed failure;
- failure mode: how capability or operation fails and how failure is detected, contained and evidenced.

Every autonomous operation must be classified as autonomous, propose, confirm or forbidden by the adopting Dimension policy. Publication, wider disclosure, deletion and irreversible or high-impact action default to confirmation unless a narrower explicit delegation exists.

### Model AGENTS.md acceptance requirements

The generated model AGENTS.md must route an agent through purpose, boundary, version, Bundle -> Layer -> Finding -> Questions -> Artifacts, this five-facet matrix, fact/assumption/unknown handling, fill, extend, patch, edit, validate and retirement procedures, child/master-system resolution, autonomy classes, and pre/post-write checks. It must reference https://ver.cy/model-agent-protocol.md after that public protocol is published; until then the unavailable-link hold remains visible.
