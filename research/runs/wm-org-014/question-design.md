# WM-ORG-014 authored design

Preparation only: six bundles, twelve findings, thirty-six questions and explicit
answer groups. CRM relationship, not party, login or billing-account identity.

## 1 Customer role and commercial scope

### 1.1 Supplier-qualified relationship identity
1. Which master namespace and identifier distinguish this customer relationship from its party identity?
2. Which selling organization, business unit or service scope defines the relationship?
3. Which aliases and external customer IDs identify this same scoped record rather than another account of the party?
Answer groups: identity{master,id,partyRef}; commercialScope{sellerRef,unitRef,serviceScope}; aliases{system,identifier,scope,evidence}.

### 1.2 Account kind and participant roles
1. Does the source record represent a customer role, CRM account, individual contact or billing account?
2. Which parties act as buyer, payer, user, bill receiver or representative in this relationship?
3. Which authority evidence limits what each related contact can request without assuming purchasing power from a contact link?
Answer groups: kind{scheme,version,code,excludedKinds}; parties{partyRefs,roles,validTime}; authority{mandateRef,scope,evidenceStatus}.

## 2 Qualification and relationship lifecycle

### 2.1 Customer recognition and onboarding references
1. What evidence distinguishes a prospect record from an established customer relationship under the owner's definition?
2. Which onboarding or agreement records establish the current relationship without importing their workflows?
3. Which prerequisites remain unknown or unmet without turning that state into an automated eligibility or credit decision?
Answer groups: recognition{definition,evidence,prospectRef}; onboarding{processRef,agreementRefs,statusSource}; prerequisites{requirements,unknowns,decisionMaster}.

### 2.2 Commercial state and temporal history
1. Which source-qualified lifecycle state and reason describe this relationship at the effective time?
2. When were activation, dormancy, closure or reactivation observed and recorded, distinct from source effect?
3. Does record closure mean ended commercial relationship, CRM deactivation or data retirement, and which obligations remain elsewhere?
Answer groups: state{scheme,code,reason,validTime}; history{events,observedAt,recordedAt,precision}; closure{meaning,evidence,outstandingMasterRefs}.

## 3 Relationship structure and ownership

### 3.1 Account grouping and hierarchy
1. Which parent, group or subsidiary links are CRM organization conveniences versus legal-party relationships?
2. What scope, cardinality and validity qualify a group roll-up without assuming the source's one-parent rule is universal?
3. Which measures or records must not be double-counted or shared merely because accounts are grouped?
Answer groups: hierarchy{linkType,parentRef,legalRelationRef}; grouping{scope,cardinality,validity}; rollup{grain,exclusions,sharingPolicy}.

### 3.2 Account responsibility and service routing
1. Who stewards this relationship and which team or role owns each service responsibility?
2. Which assignment, territory or handover evidence limits the responsible person's authority and valid interval?
3. Where are unresolved support requests routed without duplicating case or grievance ownership?
Answer groups: ownership{steward,team,serviceRoles}; assignment{scope,evidence,validity}; routing{caseMaster,queueRef,unresolvedRefs}.

## 4 Commercial and communication bindings

### 4.1 Billing, agreement and entitlement references
1. Which billing accounts, contracts, subscriptions or service entitlements are related, with which master systems?
2. Which account or payment status can be displayed as an attributed snapshot but must not be interpreted as relationship truth?
3. Which operations remain exclusively with billing or service masters rather than the customer context record?
Answer groups: bindings{type,reference,master,role}; snapshots{value,source,asOf,limitations}; delegation{operation,master,excludedEffects}.

### 4.2 Contact channels and preference evidence
1. Which contact points and address roles are valid for this relationship and purpose, rather than global party attributes?
2. Which preferences or suppression flags are expressed, inferred or system defaults, and from which evidence?
3. Which separate consent or policy authority must be consulted before contact, regardless of a permissive default flag?
Answer groups: channels{contactRef,purpose,role,validity}; preferences{value,origin,evidence,asOf}; contactAuthority{policyRef,consentRef,scope,unknowns}.

## 5 Relationship observations and identity change

### 5.1 Interaction and assessment context
1. Which interaction, complaint or purchase references inform the customer relationship without copying their payloads?
2. Which classification or relationship-health assessment has a named method, time and uncertainty instead of an unexplained score?
3. Which information is excluded from profiling and downstream automated decisions under the governing policy?
Answer groups: observations{eventRefs,source,purpose}; assessment{scheme,method,asOf,uncertainty}; exclusions{dataClasses,uses,policyRef}.

### 5.2 Duplicate, merge and split lineage
1. Which evidence identifies duplicate relationship records while preserving distinct seller or service scopes?
2. Which authorized merge/split decision maps old identifiers and fields to surviving or new records?
3. How can a mistaken merge be corrected without losing source lineage, preferences or unrelated customer accounts?
Answer groups: duplicates{candidates,evidence,scopeTest}; change{decisionRef,idMapping,fieldProvenance}; recovery{compensation,priorRevisions,protectedLinks}.

## 6 Stewardship and interoperability

### 6.1 Mastership, access and retention
1. Which CRM is authoritative for each relationship field and which caches are stale or conflicting?
2. Which actors may read or update which fields without gaining access to private billing or identity data?
3. What retention and correction rules keep necessary history while avoiding unnecessary personal-data copies?
Answer groups: mastership{fieldMasters,freshness,conflicts}; access{actorRole,fieldScope,policy}; retention{rule,reviewDate,correction,disposition}.

### 6.2 Versioned mapping and agent acceptance
1. Which exact TMF629, CRM or billing-customer schema mappings preserve the declared record kind?
2. What identifiers, role meanings, hierarchy rules or preference defaults are lost or changed in a round trip?
3. Which authorized record operations and negative fixtures prevent contact, charging or eligibility changes as unintended effects?
Answer groups: mappings{schemaVersion,term,kindTest}; losses{fields,meaning,defaults,warning}; acceptance{operations,preconditions,fixtures,results}.

Proposed functions: resolve customer relationship; record role/scope; revise
source lifecycle; link commercial masters; propose duplicate reconciliation;
export permitted projection. No financial operation, marketing outreach or
adverse decision is executed by a relationship-model operation.
