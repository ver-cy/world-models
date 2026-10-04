# WM-ORG-013 authored design

Preparation only. Model is a scoped stakeholder-interest relationship, not the
person/group itself. Proposed six bundles, twelve records and thirty-six
questions. Answer groups are candidates requiring later schema serialization.

## 1 Stake identity and affected subject

### 1.1 Scoped stakeholder identity
1. Which master-qualified identifier distinguishes this stakeholder relationship from the party's identity?
2. Which organization, project, decision or impact is the subject of the stake?
3. Which party or collective is referenced, and which membership/identity uncertainty remains?
Answer groups: identity{master,id,revision}; subject{kind,reference,scope}; party{reference,collectiveScope,uncertainty}.

### 1.2 Identification and coverage boundaries
1. Which definition and discovery method identified this party as affected, potentially affected or interested?
2. Which geographic, temporal and value-chain boundaries qualify the assessment?
3. Which unrepresented or undiscovered groups remain plausible gaps, and when will identification be reviewed?
Answer groups: discovery{definition,method,category,evidence}; boundary{geography,time,valueChain}; gaps{groups,rationale,reviewDue}.

## 2 Interests, impacts and rights

### 2.1 Attributed interests and expectations
1. What valued outcome, concern or expectation does the stakeholder express about the subject?
2. Is this self-reported, represented or inferred, by whom and from which evidence?
3. Which distinct or conflicting interests coexist without reducing the stakeholder to one preference?
Answer groups: interest{statement,topic,desiredOutcome}; attribution{mode,assertor,evidence,confidence}; plurality{interestRefs,conflicts,unknowns}.

### 2.2 Affectedness and rights basis
1. Which actual or potential positive/negative impacts connect the subject to this stakeholder?
2. Which impact severity, likelihood, duration and reversibility assessments are referenced with method and uncertainty?
3. Which asserted rights or applicable obligations require attention independently of stakeholder influence?
Answer groups: affectedness{impactRefs,pathway,actuality,direction}; assessment{method,severity,likelihood,duration,reversibility,uncertainty}; rights{basisRef,jurisdiction,claimStatus}.

## 3 Representation and participation conditions

### 3.1 Representative scope and legitimacy evidence
1. Who claims to represent the stakeholder and by which mandate, selection or other evidenced basis?
2. Which people, interests, decisions and valid interval fall inside that representative's scope?
3. Which dissent, competing representation or mandate limitation must remain visible?
Answer groups: representation{representative,basis,evidence}; mandate{coveredGroup,topics,decisions,validTime}; contest{dissent,alternatives,limitations}.

### 3.2 Access barriers and safe participation
1. Which language, disability, cultural, time or digital-access barriers hinder participation?
2. What accommodations or safe channels are requested, with only necessary sensitive data recorded?
3. Which retaliation, confidentiality or power-imbalance risks require protected engagement arrangements?
Answer groups: barriers{type,evidence,scope}; accommodation{request,channel,minimizedData}; safety{risk,protectionRef,disclosureRestriction}.

## 4 Influence, prioritization and engagement scope

### 4.1 Influence and priority assessments
1. What ability to affect the subject is evidenced, by which mechanism rather than a guessed personality score?
2. Which named scale, method, assessor and time qualify influence or engagement-priority ratings?
3. How does the prioritization preserve attention to severely affected low-influence groups and avoid treating scores as rights?
Answer groups: influence{mechanism,evidence,scope}; rating{scale,method,assessor,asOf,uncertainty}; safeguards{impactPriority,rightsSeparation,review}.

### 4.2 Engagement purpose and decision interface
1. Is the planned engagement information, consultation, participation or another explicitly defined level?
2. What decision can actually be influenced, by when, and which limits must be communicated?
3. Which responsible owner and engagement-plan references govern frequency, channels and resources?
Answer groups: purpose{level,definition,objectives}; decisionInterface{decisionRef,window,limits}; plan{owner,planRef,frequency,channels,resources}.

## 5 Voice, response and change history

### 5.1 Feedback and response traceability
1. Which attributable feedback or concern was received through which authorized engagement record?
2. What response, decision rationale or commitment addresses it, and where is that record mastered?
3. How was the outcome communicated, while distinguishing notification, acknowledgement, agreement and consent?
Answer groups: feedback{recordRef,source,channel,receivedAt}; response{decisionRef,rationaleRef,commitmentRef,master}; outcome{communicationRef,acknowledgement,agreement,consentEvidence}.

### 5.2 Relationship review and lifecycle
1. When did the stake become relevant and when was that assertion observed or recorded?
2. What change in subject, impact, interest or representation triggers reassessment rather than silent overwrite?
3. Does closure mean ended relevance, withdrawal from engagement or record retirement, and which concerns remain unresolved?
Answer groups: time{validInterval,observedAt,recordedAt,precision}; reassessment{trigger,priorRevision,newEvidence}; closure{meaning,reason,unresolvedRefs}.

## 6 Governed evidence and exchange

### 6.1 Stewardship, confidentiality and retention
1. Which Dimension and steward master these interest assertions rather than the party or grievance workflow?
2. Which field-level restrictions prevent disclosure of private concerns, identities or vulnerable-group membership?
3. What correction, retention and disposal rules preserve justified evidence without keeping unnecessary personal data?
Answer groups: stewardship{dimension,master,steward,delegatedRefs}; access{fields,policy,purpose,redaction}; retention{rule,reviewDue,correction,dispositionAuthority}.

### 6.2 Mapping and safe agent use
1. Which versioned GRI, ESS10 or participation-profile definitions align with this record and which differ in scope?
2. Which evidence and negative fixtures test that export preserves attribution, impact, representation and unknowns?
3. Which agent operations may maintain the local record without contacting stakeholders, inferring consent or changing their rights?
Answer groups: mapping{sourceVersion,targetTerm,scopeDifference,loss}; validation{fixtures,evidence,results}; operations{delegation,preconditions,excludedEffects,recovery}.

Six proposed record operations: identify scoped stake; record attributed interest;
assess coverage gaps; link engagement response; revise relevance/representation;
export minimized projection. No contact, persuasion, rights determination or
automatic prioritization of individuals is authorized by this specification.
