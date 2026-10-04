# Professional License / Credential: authored question design

Boundary: an individual awarded credential record, not its scheme, bearer,
cryptographic envelope or an automatic permission to practise. The following
is Vercy design informed by selected sources, not copied normative requirements.

## 1 Award identity and classification
### 1.1 Award and subject binding
1. Which issuer-qualified award identifier and revision identify this credential rather than its certificate file?
2. Who is the credential subject, and is the presenter or repository holder a different party?
3. What evidence resolves duplicates, namesakes or replacement documents without merging distinct awards?
Answer groups: identity{issuerNamespace,awardId,revision,replacesRef} subject{personRef,holderRef,bindingEvidence,unknownReason} matching{candidateRefs,decision,reviewer,evidenceRef}
### 1.2 Scheme and credential kind
1. Is this a license, certification, qualification or membership under which versioned scheme?
2. Which awarding body, regulator and scheme owner have separately evidenced authority?
3. Which professional class, specialty and level are asserted without assuming equivalent legal effects?
Answer groups: kind{code,vocabulary,schemeRef,schemeVersion} authority{issuerRef,regulatorRef,schemeOwnerRef,basisRef} classification{professionCode,specialty,level,mappingLimits}

## 2 Award basis and permitted scope
### 2.1 Eligibility and assessment basis
1. Which eligibility and assessment requirements applied to this award at the decision date?
2. Which authorized evidence references support satisfaction, exemption or unknown assessment outcomes?
3. Who made the award decision and what issuance, effective and recording dates were stated?
Answer groups: eligibility{requirementRefs,profileVersion,applicabilityDate} evidence{assessmentRefs,exemptions,outcome,accessPolicy} decision{authorityRef,decisionRef,issuedAt,effectiveFrom,recordedAt}
### 2.2 Jurisdiction and practice conditions
1. In which jurisdiction and activity scope is this credential asserted to be applicable?
2. Which restrictions, supervision requirements or organization-specific permissions remain separate?
3. What competent-authority evidence is needed before a relying party can assess permission for the intended work?
Answer groups: scope{jurisdictionRefs,activityCodes,effectivePeriod} conditions{restrictionRefs,supervisionRef,organizationPermissionRef} reliance{intendedUse,authorityEvidence,policyRef,outcomeOrUnknown}

## 3 Validity and continuing requirements
### 3.1 Validity intervals and observations
1. What are the credential effective interval, precision and source, including unknown or open-ended expiry?
2. How are digital envelope validity, credential status and a local record active flag kept distinct?
3. At what observation time and under which freshness policy was the latest status usable?
Answer groups: interval{validFrom,validUntil,precision,sourceRef,unknownReason} states{envelopePeriod,awardStatus,recordActive,practiceAssessmentRef} freshness{observedAt,sourceAsOf,refreshBy,policyRef,staleFlag}
### 3.2 Renewal and revalidation
1. Which renewal or continuing-development obligations apply under the credential's own scheme?
2. Which evidence and decisions show compliance, exemption, pending review or unmet requirements?
3. Does the next renewal preserve the award identity or create a successor according to issuer rules?
Answer groups: obligations{requirementRefs,interval,dueDate,schemeVersion} compliance{evidenceRefs,reviewOutcome,exemptionRef,pendingReason} continuity{renewalRef,identityRule,successorRef,decisionAt}

## 4 Status changes and remedies
### 4.1 Suspension revocation and restoration
1. Which authority reported suspension, revocation, expiry, surrender or restoration, and for what scope?
2. What effective and recorded times, reasons and evidence qualify each transition?
3. How are contradictory, stale or unavailable status reports preserved without inferring good standing?
Answer groups: transition{kind,authorityRef,affectedScope,priorRevision} timing{effectiveAt,recordedAt,reasonRef,evidenceRef} disagreement{assertionRefs,sourcePriority,unresolvedReason,reviewRef}
### 4.2 Correction appeal and record retirement
1. Which correction or appeal process and responsible authority are referenced for this credential?
2. What decision, replacement or pending outcome changes the record without silently reversing a regulator's action?
3. What retention, legal-hold and privacy policy governs removal of local evidence and permitted tombstones?
Answer groups: remedy{processRef,authorityRef,caseRef,deadlinePrecision} outcome{decisionRef,status,replacementRef,expectedHead} retirement{retentionPolicy,holdRef,erasureScope,minimalTombstone}

## 5 Verification and disclosure
### 5.1 Evidence and status verification
1. Which official register or issuer evidence was checked, with what subject binding and source time?
2. Which checks separately cover proof integrity, issuer trust, status and claim applicability?
3. If a status-list source is used, what purpose, validity and refresh information prevent stale or misinterpreted results?
Answer groups: observation{registerRef,subjectMatch,checkedAt,sourceAsOf,resultOrUnknown} checks{proofResult,issuerTrust,awardStatus,applicability,policyRef} statusList{listRef,purpose,indexRef,listValidity,ttlMillis,refreshPolicy}
### 5.2 Privacy-aware presentation
1. Which minimum credential fields may be disclosed to which relying party for the stated purpose?
2. How are restricted assessment, disciplinary and identity evidence references protected during presentation?
3. What presentation audit or correction trail can be retained without retaining unnecessary personal evidence?
Answer groups: disclosure{purpose,recipientScope,allowedFields,authorityRef} protection{evidenceAccess,redactionRules,correlationRisks} audit{operationRef,revisionRef,retentionPolicy,redactedOutcome}

## 6 Recognition and interoperability
### 6.1 Recognition in another context
1. Which destination jurisdiction and intended activity require a separate recognition assessment?
2. What competent-authority decision, conditions or outstanding steps support recognition rather than mere similarity?
3. Which vocabulary translations or claimed equivalences remain unratified or narrower than permission to practise?
Answer groups: destination{jurisdictionRef,activity,authorityRef} recognition{decisionRef,conditions,pendingSteps,effectivePeriod} mapping{sourceTerm,targetTerm,relation,verificationLimits}
### 6.2 Projection and acceptance
1. Which pinned target profile maps the award, scheme, subject, status and scope without collapsing their identities?
2. Which unsupported qualifiers or required-field losses must cause export refusal?
3. Which negative tests and authorized reviewer decisions are still required before operational reliance?
Answer groups: projection{profileRef,version,fieldMap,sourceRevision} loss{unsupportedFields,requiredQualifiers,refusalReason} acceptance{testRefs,reviewer,unresolvedHolds,relianceDecision}
