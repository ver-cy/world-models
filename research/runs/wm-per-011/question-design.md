# Interpersonal Relationship: authored question design

Preparation only. Root kind relationship, not person or a global social graph.
Private attributed statements may disagree. Proposed fields are not universal
psychological measures, factual conclusions about private people or legal advice.

## 1 Relationship identity and participants

### 1.1 Scoped relationship identity
1. Which master-qualified identifier distinguishes this relationship from either participant and its individual assertions?
2. Which two person references and owning context define the record boundary?
3. Which identity ambiguity prevents linking or merging records safely?
Answer groups: identity{master,id,namespace}; endpoints{personA,personB,context}; ambiguity{candidates,evidence,resolutionState}.

### 1.2 Type and role direction
1. Which versioned relationship type and participant roles are asserted?
2. What direction, inverse or symmetry does that specific vocabulary define?
3. Which overlapping types or culturally specific labels must remain distinct?
Answer groups: typing{scheme,version,type,roles}; direction{source,target,inverse,symmetry}; distinctions{parallelTypes,labels,locale,limits}.

## 2 Recognition and attributed perspectives

### 2.1 Assertion and evidence basis
1. Who states that the relationship exists, using what source and method?
2. What observation or statement supports the claim without importing unnecessary private content?
3. Which confidence and limitations distinguish reported belief from verified status?
Answer groups: attribution{author,source,method}; evidence{references,observedAt,minimization}; assurance{claimKind,confidence,verificationScope,limits}.

### 2.2 Reciprocity and disagreement
1. Which participant perspectives are available and which are unknown?
2. What evidence supports reciprocal recognition for this specific type rather than unilateral assertion?
3. Which denial, correction or dispute must coexist without declaring one person's account universal truth?
Answer groups: perspectives{participant,assertionRefs,unknowns}; reciprocity{typeRule,evidence,status}; disputes{claims,responses,authorityScope,resolution}.

## 3 Roles, expectations and boundaries

### 3.1 Role scope and commitments
1. Which social, care, professional or family role is relevant in this context?
2. Which mutually agreed commitments or separately evidenced mandates are referenced?
3. Which limits prevent a role label from implying legal representation, duties or access rights?
Answer groups: contextRole{role,scope,contextRef}; commitments{agreementRefs,mandateRefs,evidence}; limits{excludedPowers,unknowns,profile}.

### 3.2 Contact and interaction boundaries
1. Which participant-stated contact preferences and boundaries apply in this context?
2. Which separate authorization is required before contacting or disclosing information to a related person?
3. Which restriction, withdrawal or unknown preference requires withholding an automated action?
Answer groups: preferences{author,channels,purposes,validity}; authority{policyRef,permission,scope}; restrictions{status,reasonRef,uncertainty,safeAction}.

## 4 Shared context and change

### 4.1 Encounters and shared activities
1. Which authorized encounters, activities or shared contexts are linked to this relationship?
2. Which source and period qualify each link without treating co-occurrence as proof of friendship or intimacy?
3. Which summaries can be retained without copying another person's protected messages or files?
Answer groups: contextLinks{activityRefs,eventRefs}; qualification{source,period,claimLimits}; summary{allowedFields,provenance,retention}.

### 4.2 Relationship episodes and transitions
1. Which start, end or uncertain interval is asserted for each role or relationship episode?
2. Which attributed event supports a change, pause or ending without inventing emotional state?
3. Which continuation or renewed episode should remain separate from a corrected historical claim?
Answer groups: validity{start,end,precision,assertionRef}; transition{eventRef,author,previous,next}; episodes{predecessor,renewal,correction,reason}.

## 5 Privacy and contested memory

### 5.1 Purpose and minimum disclosure
1. For which explicit purpose and authority may these relationship details be held?
2. Which fields and participant references may each recipient see without leaking the relationship itself?
3. Which sensitive detail is unnecessary or must remain only in its authorized master?
Answer groups: purpose{purpose,authorityRef,owner}; disclosure{recipient,fields,scope,relationshipVisibility}; minimization{excludedFields,masterRefs,rationale}.

### 5.2 Correction, retention and retirement
1. Which participant request or steward decision triggers review or correction of an assertion?
2. What retention or legal-hold policy governs each piece of evidence and its access restrictions?
3. How is a local record retired or erased without claiming that the real-world relationship ceased or leaking deleted details in a tombstone?
Answer groups: correction{requestRef,decision,assertionRefs}; retention{policy,period,hold,restrictions}; retirement{action,authority,minimalTombstone,externalMeaningLimits}.

## 6 Interoperable and safe agent use

### 6.1 Qualified mappings
1. Which selected fields map to a pinned relationship vocabulary or domain profile?
2. What direction, perspective, temporal or privacy meaning would be lost by exporting a simple edge?
3. Which mapping must be refused when the target cannot preserve required qualifiers?
Answer groups: mapping{profile,version,fields}; losses{direction,perspective,time,privacy}; refusal{reason,requiredQualifiers,alternative}.

### 6.2 Validation and permitted operations
1. Which fixtures detect reversed roles, unsupported reciprocity and conflated episodes?
2. Which authorization, expected revision and protected references must be checked before updating memory?
3. Which failure or uncertainty requires safe refusal rather than identity merging, outreach or sensitive inference?
Answer groups: fixtures{cases,results,limits}; writeGate{authority,expectedHead,referenceAccess}; safeFailure{condition,refusal,recovery}.

Six bundles, twelve layers/findings, thirty-six questions. Proposed functions:
resolve_relationship, append_relationship_assertion, record_perspective,
link_context_evidence, record_episode_change, export_minimized_projection.
No autonomous messaging, intimacy inference, trust scoring or legal determination.
Physical measurements belong to person/place models. Executable nested-field
schemas and profile-specific negative tests remain to be implemented.
