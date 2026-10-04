# Administrative Procedure / Case: authored question design

One administrative case instance. Procedure templates, court litigation,
authority records and individual applications/decisions stay referenced.

## 1 Case identity and applicable procedure
### 1.1 Docket and matter
1. Which authority-qualified case identifier and matter description distinguish this instance from an application or court case?
2. Which linked, joined, split or transferred cases retain separate identities and evidence?
3. Which record source and ambiguity checks prevent merging different proceedings concerning the same person or object?
Answer groups: identity{authorityNamespace,caseId,matter,revision} related{caseRefs,relationType,basisRef,period} matching{sourceRef,candidates,decision,unknownReason}
### 1.2 Procedure profile and competence
1. Which procedure definition, jurisdiction, version and legal basis apply to this case at the relevant time?
2. Which competent authority and delegated officer roles are evidenced rather than inferred from assignment?
3. Which competence disputes, exceptions or missing legal-profile rules prevent operational reliance?
Answer groups: profile{procedureRef,version,jurisdiction,basisRef,effectivePeriod} competence{authorityRef,delegationRef,officerRoleRef,scope} limits{disputeRefs,exceptions,missingRules,reviewer}

## 2 Initiation and participants
### 2.1 Opening and intake
1. Was the proceeding initiated by application, referral, official initiative or another legally defined trigger?
2. Which submission, receipt, registration and legally relevant commencement times are supported by evidence?
3. What admissibility or completeness assessment records missing material without treating intake as approval?
Answer groups: trigger{kind,applicationRef,referralRef,exOfficioBasis} intake{sentAt,receivedAt,registeredAt,commencementAt,sourceRef} admission{assessmentRef,missingItems,status,reason}
### 2.2 Parties representation and impartiality
1. Which applicants, affected parties and other participants have what source-qualified procedural standing?
2. Which representatives have evidenced authority, scope and validity for this case?
3. Which conflicts of interest, exclusions or recusals are recorded without publicly disclosing unnecessary personal details?
Answer groups: parties{partyRefs,standing,basisRef,period} representation{representativeRef,mandateRef,scope,validity} impartiality{conflictRef,restrictedReason,recusalDecision,accessPolicy}

## 3 File evidence and participation
### 3.1 Evidence and factual findings
1. Which requirements and disputed facts are addressed by each submitted or obtained evidence reference?
2. Who supplied, obtained or transformed the evidence, and what integrity, date and access qualifiers are known?
3. Which evidence remains missing, disputed, superseded or unevaluated rather than automatically accepted as true?
Answer groups: support{requirementRefs,factRefs,evidenceRefs} provenance{sourceAgent,activityRef,observedAt,digest,accessRef} evaluation{status,contradictions,missingEvidence,reviewRef}
### 3.2 Hearing file access and statements
1. Which opportunities to be heard or submit statements apply under the case's actual legal profile?
2. Which invitations, responses, waivers or justified exceptions evidence participation without assuming silence is consent?
3. Which file-access and confidentiality decisions define each participant's permitted view separately from public disclosure?
Answer groups: participation{rightBasis,partyRef,scope,profileRef} hearing{noticeRef,responseRef,exceptionBasis,recordedAt} access{requestRef,decisionRef,redactions,recipientScope}

## 4 Progress and time controls
### 4.1 Activities and procedural events
1. Which procedural stages, tasks and milestones were planned and which actually occurred?
2. What evidence supports transfers, consultations, suspensions or resumptions and their effect on the case?
3. Which task or case states must remain separate from a legally effective final decision?
Answer groups: plan{definitionRef,plannedItems,actualEvents} transitions{eventType,basisRef,effectiveAt,actorRef} state{workflowState,legalStatus,sourceRef,unresolvedReason}
### 4.2 Deadlines and delay
1. Which specific rule, triggering event and calendar govern each deadline relevant to the proceeding?
2. What evidence supports extensions, pauses, restarts and different receipt or service dates?
3. Which disputed calculation or administrative-silence consequence requires competent review rather than automatic inference?
Answer groups: deadline{ruleRef,triggerRef,calendarRef,dueValue,precision} adjustments{extensionRef,pauseIntervals,restartBasis,receiptEvidence} uncertainty{calculationStatus,silenceRuleRef,dispute,reviewRef}

## 5 Determination and communication
### 5.1 Decision reasons and alternatives
1. Which decision or other outcome reference records the competent actor, disposition and applicable legal basis?
2. Which factual findings, evidence and reasons support that particular outcome while retaining disputed assertions?
3. Which conditions, partial determinations, withdrawals or public-law agreement outcomes are relevant without forcing one universal closure path?
Answer groups: outcome{decisionRef,actorRef,disposition,basisRef} reasons{findingRefs,evidenceRefs,rationaleRef,contestedFacts,reasonExceptionBasis} variants{conditions,partialScope,withdrawalRef,agreementRef}
### 5.2 Notification effect and remedies
1. Which recipient, channel and delivery evidence distinguish dispatch, receipt, notification and asserted legal effect?
2. Which remedy instructions name the competent review body, route and time rule actually applicable?
3. Which uncertainty about service, enforceability or suspensive effects must remain explicit before relying on the decision?
Answer groups: notification{recipientRef,channel,sentAt,receivedAt,serviceAt,effectAt,evidenceRef} remedies{routeRef,bodyRef,timeRule,noticeRef} effectiveness{status,basisRef,suspensionRef,unknowns}

## 6 Review closure and record continuity
### 6.1 Review reopening and linked litigation
1. Which administrative review, correction or reopening proceeding changes this case under an evidenced basis?
2. Which court challenge is a separate linked case rather than a silent continuation of this administrative record?
3. What closure and residual-obligation evidence distinguishes administrative completion from finality or exhaustion of remedies?
Answer groups: review{processRef,decisionRef,basisRef,revision} litigation{courtCaseRef,relationship,sourceRef,scope} closure{status,residualDuties,finalityBasis,unknowns}
### 6.2 Retention projection and acceptance
1. Which custodian, retention schedule and legal holds govern the case file and its authorized local copies?
2. Which pinned target model maps case, evidence and decision references without losing authority, time or disclosure qualifiers?
3. Which validation fixtures, missing legal profiles and independent reviews remain outstanding before operational use?
Answer groups: custody{custodianRef,retentionPolicy,legalHold,disposalScope,tombstone} projection{profileRef,version,fieldMap,losses,refusalReason} acceptance{testRefs,missingRules,reviewer,assuranceHolds}
