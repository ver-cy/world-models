# WM-ORG-015 authored supplier/partner design

Preparation, not yet validated or published. Relationship context, not party
identity, purchase transaction or a legal partnership determination.

## 1 Counterparty role and supply scope

### 1.1 Buyer-scoped relationship identity
1. Which master-qualified relationship identifier links which buyer or collaboration owner to which counterparty?
2. Which scheme distinguishes supplier, subcontractor, reseller or alliance partner from the underlying party?
3. Which aliases refer to this relationship without collapsing different buyers, sites or commercial scopes?
Answer groups: identity{master,id,ownerRef,partyRef}; role{scheme,version,code,scope}; aliases{system,id,scope,evidence}.

### 1.2 Supplied capabilities and participation
1. Which goods, services or collaboration contributions are within the declared relationship scope?
2. Which locations, organizational units and delivery roles are covered by that scope?
3. Which consortium, prime or sub-tier participant references preserve responsibility without inferring legal control?
Answer groups: capability{categoryRefs,contribution,limitations}; coverage{siteRefs,unitRefs,roles,validity}; participation{linkType,partyRefs,responsibility,evidence}.

## 2 Qualification and authorization

### 2.1 Qualification evidence and freshness
1. Which qualification criteria and scheme version apply to the relevant category and buying scope?
2. Which claims are supplier-declared versus independently assessed, with which supporting references?
3. When do qualifications expire or require review and which missing evidence remains unknown?
Answer groups: criteria{scheme,version,category,buyerScope}; evidence{claim,attribution,assessor,refs}; freshness{validity,reviewDue,unknowns}.

### 2.2 Registration and approved-use boundaries
1. Which source status distinguishes registration, qualification and authorization for specified commercial uses?
2. Who approved which scope under which policy and with which limitations or exceptions?
3. Which separate transaction authority remains necessary despite an approved supplier status?
Answer groups: state{source,scheme,status,meaning}; approval{authorityRef,scope,policy,exceptions}; transactionBoundary{operation,master,requiredAuthority}.

## 3 Commercial bindings and accountability

### 3.1 Agreement and procurement references
1. Which agreements, awards or purchase relationships provide the commercial basis without duplicating their terms?
2. Which party is seller, invoice issuer, payee or service performer in each referenced context?
3. Which contractual limits remain authoritative elsewhere when a relationship record changes?
Answer groups: basis{typedRefs,master,scope}; commercialRoles{partyRefs,role,context}; limits{contractRef,obligationMaster,excludedEffects}.

### 3.2 Relationship stewardship and interfaces
1. Which accountable owner, category manager and partner representatives steward the relationship?
2. Which contact and exchange interfaces have scoped delegated authority rather than inferred permissions?
3. Which handover or escalation process owns unresolved issues and disputed responsibility?
Answer groups: stewardship{ownerRef,managerRef,representatives}; interfaces{contactRefs,protocol,scope,authority}; escalation{processRef,issueRefs,disputes}.

## 4 Risk and performance evidence

### 4.1 Attributed supplier-risk assessments
1. Which assessed risks have a named method, evidence, time and uncertainty for the relevant supply scope?
2. Which critical dependencies, concentration or sub-tier visibility gaps affect this assessment?
3. Which mitigations and review decisions are merely referenced rather than automated supplier exclusion?
Answer groups: assessment{method,evidence,asOf,uncertainty}; dependency{criticality,refs,concentration,unknowns}; response{mitigationRefs,reviewDecision,authority}.

### 4.2 Performance and issue context
1. Which delivery, quality or service observations support the relationship assessment without copying transaction payloads?
2. Which metric definition, denominator, period and source make performance comparisons meaningful?
3. Which incidents, corrective actions or disputed observations need follow-up by their authoritative owners?
Answer groups: observations{eventRefs,source,scope}; metrics{definition,denominator,period,method}; issues{incidentRefs,actionRefs,owner,dispute}.

## 5 Change and continuity

### 5.1 Relationship changes and review triggers
1. Which scope, ownership or service changes trigger a relationship review without automatically transferring approval?
2. What effective, observed and recorded times qualify each lifecycle change?
3. How are conflicting source statuses and mistaken updates preserved and corrected?
Answer groups: triggers{change,evidence,policy,reviewRef}; time{effective,observed,recorded,precision}; correction{contestedStates,priorRevision,compensation}.

### 5.2 Suspension, exit and continuity
1. Which authorized scope is suspended or ended, for what attributed reason and interval?
2. Which outstanding obligations, access-removal and handover tasks remain with contract or operational masters?
3. Which continuity dependencies and reinstatement evidence must be reviewed without silently cancelling contracts?
Answer groups: exit{scope,reason,decisionRef,validity}; handover{obligationRefs,accessTaskRefs,owner}; continuity{dependencies,planRef,reinstatementCriteria}.

## 6 Governed knowledge exchange

### 6.1 Mastership, disclosure and retention
1. Which systems master identity, qualification, approval and assessment fields and how stale are cached assertions?
2. Who may read or change each field without obtaining bank details, credentials or unrelated confidential evidence?
3. Which correction and retention policies preserve justified lineage while minimizing private supplier data?
Answer groups: masters{fieldMasters,freshness,conflicts}; access{actorRole,fieldScope,policy}; retention{rule,reviewDate,correction,disposition}.

### 6.2 Mappings and safe agent operations
1. Which pinned OCDS, UBL or PartyRole mapping preserves role, buyer scope and source status meaning?
2. Which information or authority distinctions are lost during import or export and require a warning or refusal?
3. Which negative fixtures prevent record maintenance from causing payment, outreach, exclusion or purchase commitments?
Answer groups: mapping{profile,version,roleMap,scopeMap}; loss{fields,meaning,warning,refusal}; acceptance{operation,preconditions,fixtures,results}.

Proposed functions: resolve scoped relationship; record qualification evidence;
revise attributed authorization; link commercial masters; record review/exit
context; export permitted projection. None executes procurement or exclusion.
