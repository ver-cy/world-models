# Organization Policy: subject design

Preparation, not a validated specification. Policy is an identifiable normative
information object with approved versions, not an engine or enacted statute.
These questions and answer groups are Vercy design proposals, not quotations
or a claim that any cited standard mandates this entire structure.

## 1 Policy identity and authority

### 1.1 Identity and normative standing
1. Which master-qualified policy identifier persists across versions and translations?
2. What makes this an organizational policy rather than guidance, a procedure, law or control implementation?
3. Which organization and policy family own its normative scope?
Answer groups: identity{master,id,aliases}; standing{kind,recognitionEvidence,limits}; owner{organizationRef,family,namespace}.

### 1.2 Approval and delegated mandate
1. Who was authorized to approve this version and where is the delegation recorded?
2. Which decision and approved text digest establish approval rather than a draft or proposal?
3. Which reservations or approval conditions limit its standing?
Answer groups: authority{partyRef,mandateRef}; approval{decisionRef,versionRef,digest,time}; conditions{scope,reservations,evidence}.

## 2 Purpose and applicability

### 2.1 Objectives and coverage
1. Which organizational outcome or risk motivates this policy?
2. Which people, activities, locations and resources are included or excluded?
3. Which definitions and vocabulary versions disambiguate the scope?
Answer groups: rationale{objective,riskRef}; scope{subjects,activities,territory,exclusions}; vocabulary{terms,scheme,version}.

### 2.2 Conditions and unresolved applicability
1. Which facts and effective period must hold for the rule to apply to a case?
2. Which actor, method, evidence and observation time support an applicability assessment?
3. Which missing or conflicting facts leave applicability unknown and require escalation?
Answer groups: conditions{predicates,timeWindow,requiredFacts}; assessment{actor,method,evidence,observedAt}; uncertainty{unknowns,conflicts,escalationRef}.

## 3 Normative content and interpretation

### 3.1 Clauses and rule meaning
1. Which stable clause states an obligation, prohibition, permission or nonbinding explanation?
2. Which actor, action, target and conditions delimit the statement?
3. Which authoritative text and interpretation preserve nuance not captured by structured fields?
Answer groups: clause{clauseId,modality}; rule{actor,action,target,conditions}; interpretation{textRef,language,authority,limitations}.

### 3.2 Dependencies and precedence
1. Which superior instruments or related policies constrain interpretation?
2. Which approved precedence or combination rule governs a particular overlap?
3. Which unresolved conflict remains visible without inventing a universal winner?
Answer groups: dependencies{instrumentRefs,versions,relation}; precedence{rule,approver,scope}; conflicts{clauseRefs,status,evidence,escalation}.

## 4 Exceptions and implementation

### 4.1 Authorized deviations
1. Which clause and case does a requested exception concern and why?
2. Who approved or rejected it within what mandate, period and conditions?
3. What evidence distinguishes expiry, revocation, pending approval and active deviation?
Answer groups: request{clauseRef,caseRef,rationale}; decision{authorizer,mandateRef,outcome,validity,conditions}; exceptionState{status,eventRef,evidence}.

### 4.2 Procedures and safeguards
1. Which procedures, controls and responsible roles implement each policy clause?
2. Which implementation evidence or test supports the mapping without equating intention with compliance?
3. Which failure modes, consequences and safe escalation paths are documented?
Answer groups: implementation{clauseRef,procedureRefs,controlRefs,roles}; assurance{testRef,result,evidence,limits}; failure{mode,harm,escalation,recoveryRef}.

## 5 Dissemination and lifecycle

### 5.1 Release and acknowledgement
1. Which approved version, language and audience were published through which channel?
2. Which receipt, acknowledgement or training evidence exists for a recipient?
3. Which access or translation limitations prevent treating receipt as understanding, consent or compliance?
Answer groups: release{version,language,audience,channel,time}; acknowledgement{recipient,evidence,type,time}; communicationLimits{access,translation,unknowns}.

### 5.2 Review, supersession and retirement
1. Which review schedule or triggering event applies and who owns the review?
2. Which revision replaces which predecessor with what effective interval and transition arrangements?
3. Which withdrawal or retirement decision ends applicability while preserving historical evidence?
Answer groups: review{owner,frequency,triggers,lastReview}; revision{predecessor,successor,effectivePeriod,transition}; retirement{decisionRef,end,reason,recordRetentionRef}.

## 6 Policy memory and interoperability

### 6.1 Mastership and controlled evidence
1. Which master copy, version digest and provenance distinguish authoritative text from projections?
2. Which roles may read or change drafts, approved text, exceptions and personal acknowledgements?
3. Which retention, legal hold and correction rules preserve evidence without silently rewriting history?
Answer groups: mastership{master,version,digest,provenance}; access{scope,roles,exceptions}; recordRules{retention,hold,correction,tombstone}.

### 6.2 Machine interpretation and acceptance
1. Which versioned external policy profile maps selected clauses and what meaning remains unmapped?
2. Which fixtures test ambiguous scope, expired exceptions, contradictory rules and stale versions?
3. Which permissions and validated adapter are required before any proposed record operation affects an external system?
Answer groups: mapping{profile,version,clauseMappings,losses}; validation{fixtures,result,limits}; executionBoundary{permission,adapter,preconditions,rollback}.

Six bundles, twelve layers/findings, thirty-six questions. Proposed functions:
resolve_policy_version, record_approval, assess_applicability_record,
record_exception_decision, link_implementation_evidence, export_policy_projection.
All are record operations; none grants permission or executes sanctions.
Physical parameters belong to referenced physical subjects, not this information
object. Nested schemas and executable acceptance fixtures are not yet supplied.
