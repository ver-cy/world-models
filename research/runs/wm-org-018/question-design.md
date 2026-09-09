# Authored governance-body design

Preparation only. An enduring constituted body, distinct from its meetings,
members and decisions. No universal quorum, voting or legal validity rule.

## 1 Constitution and jurisdiction

### 1.1 Body identity and establishment
1. Which stable master-qualified identifier distinguishes the body from its parent, secretariat and individual meetings?
2. Which establishing instrument created it and who had authority to establish it?
3. Which body class and organizational context distinguish a governing board, advisory committee or temporary panel?
Answer groups: identity{master,id,parentRef,aliases}; establishment{instrumentRef,issuer,effectiveDate}; classification{scheme,code,context,limits}.

### 1.2 Mandate and delegation limits
1. Which topics, entities, territory or resources fall within the body's mandate?
2. Which powers are advisory, delegated or reserved elsewhere under the governing instrument?
3. Which reporting and escalation relationships preserve retained accountability without assuming unlimited subdelegation?
Answer groups: mandate{scope,instrumentRef,validity}; powers{power,kind,limits,reservedAuthority}; accountability{reportsTo,escalation,delegationRule}.

## 2 Composition and office

### 2.1 Seats, membership and terms
1. Which seats and membership classes exist independently of their current holders?
2. Which appointment, election or ex-officio evidence links a member to a seat for a valid term?
3. Which vacancies, substitutions or disputed appointments affect participation under the applicable rules?
Answer groups: seats{seatIds,classes,eligibilityRules}; membership{partyRef,seatRef,basis,validity}; exceptions{vacancies,substitutes,disputes,ruleRef}.

### 2.2 Chair, officers and secretariat
1. Which chair, deputy and secretary roles exist and who currently holds each role?
2. Which procedural and administrative responsibilities are delegated without adding substantive decision powers?
3. Which succession or temporary-cover rules apply when an officer is absent or conflicted?
Answer groups: officers{role,holderRef,term}; responsibilities{role,scope,authorityRef}; cover{trigger,substituteRule,evidence}.

## 3 Participation and decision rules

### 3.1 Eligibility, interests and recusal
1. Which participants may attend, speak, advise or vote, and for which matters?
2. Which declared conflicts and management decisions restrict a participant for a specific agenda item?
3. How do recusals or exclusions affect quorum and voting denominators under the pinned rule version?
Answer groups: eligibility{participantClass,rights,matterScope}; interests{declarationRef,decisionRef,restriction}; recusalEffect{ruleVersion,quorumEffect,voteEffect,unknowns}.

### 3.2 Procedure, quorum and decision methods
1. Which rule version governs notice, meeting modes, written procedure and decision categories?
2. Which quorum formula, eligible population and time-of-check apply to each type of decision?
3. Which consensus, voting, abstention, tie or dissent rules determine the recorded outcome without assuming simple majority?
Answer groups: procedure{instrumentVersion,notice,modes,categories}; quorum{formula,population,checkTime,exceptions}; decisionMethod{method,threshold,abstention,tie,dissent}.

## 4 Deliberation and decision evidence

### 4.1 Sessions, agendas and materials
1. Which meeting-session references and agenda items fall within this body's business?
2. Which versions of papers or expert advice were made available to authorized participants?
3. Which material-access restrictions or late changes must be visible without copying confidential payloads?
Answer groups: sessions{meetingRefs,agendaRefs,scope}; materials{refs,versions,availability}; restrictions{fieldScope,policy,changes}.

### 4.2 Outcomes, minutes and follow-up
1. Which decisions or recommendations reference the rule version, meeting and evidential record used?
2. Are minutes draft, approved or contested, and how are objections and corrections preserved?
3. Which action owners, reporting duties or review routes follow from the recorded outcome without execution by this model?
Answer groups: outcomes{decisionRefs,ruleVersion,sessionRef,evidence}; minutes{recordRef,status,approval,objections}; followup{actionRefs,owners,reporting,reviewRoute}.

## 5 Accountability and lifecycle

### 5.1 Reporting and effectiveness review
1. Which oversight recipient receives reports and what information is required at what cadence?
2. Which attendance, workload or effectiveness assessments have an explicit method and limitations?
3. Which recommendations to revise mandate, membership or procedures remain pending with the competent authority?
Answer groups: reporting{recipient,requirements,cadence}; evaluation{method,evidence,period,limitations}; recommendations{changeRefs,authority,status}.

### 5.2 Renewal, succession and dissolution
1. Which review, sunset or renewal conditions govern the continued existence of the body?
2. Which authorized change replaces, merges or dissolves it while preserving identifier and mandate history?
3. Where do outstanding matters, records and responsibilities transfer without silently transferring decision authority?
Answer groups: continuation{reviewDate,sunset,renewalRule}; transition{decisionRef,type,priorIds,validity}; handover{matterRefs,recordsCustodian,responsibility,authorityLimits}.

## 6 Governed records and interoperability

### 6.1 Mastership, access and retention
1. Which systems master constitution, membership, rules and decision evidence and which cached versions are stale?
2. Which actors may read or change each record without acquiring membership, voting rights or access to unrelated private data?
3. Which retention and correction policies preserve justified records while controlling confidential member information?
Answer groups: masters{fieldMasters,revisions,freshness}; access{actorRole,fieldScope,policy}; retention{rule,correction,disposition,holds}.

### 6.2 Mapping and agent acceptance
1. Which ORG membership, role and post mappings preserve body identity and temporal scope without claiming complete authority semantics?
2. Which rule distinctions are lost in an external representation and require a warning or refusal?
3. Which negative fixtures prevent record updates from appointing members, casting votes or declaring a decision legally valid?
Answer groups: mapping{profile,version,termMap,scope}; losses{distinction,warning,refusal}; acceptance{operations,preconditions,fixtures,results}.

Functions: resolve body; record mandate evidence; record membership assertion;
link rule/decision evidence; record review or lifecycle transition; export
authorized projection. No appointment, vote, meeting invitation or legal ruling.
