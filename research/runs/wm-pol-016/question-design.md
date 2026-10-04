# Public Authority / Institution: proposed question design

One institution, not a country, officeholder, building or service catalogue.
Source-qualified legal/personality facts and unknowns must be expressible.

## 1 Institutional identity
### 1.1 Identity and recognition
1. Which authoritative institution identifier and official names identify this body across languages and name changes?
2. What evidence distinguishes this institution from similarly named offices, buildings or websites?
3. Which asserted legal-personality status and public-body classification apply under which dated jurisdictional definition?
Answer groups: identity{masterId,namespace,names,language,aliasPeriods} recognition{registerRef,sourceAsOf,ambiguity,reviewer} classification{legalPersonality,bodyType,definitionRef,jurisdiction,unknownReason}
### 1.2 Institutional scope and boundaries
1. Which governmental level, parent relationships and separate institutional units are evidenced?
2. Which administrative and statistical classifications describe the institution without determining its powers?
3. Which apparent duplicates or predecessor records require unresolved identity decisions rather than automatic merges?
Answer groups: scope{level,parentRefs,unitRefs,validPeriod} sectors{administrativeType,statisticalSector,classificationAuthority,asOf} duplicates{candidateRefs,identityDecision,evidenceRef,unresolvedReason}

## 2 Foundation and competence
### 2.1 Establishment and legal basis
1. Which legislation, charter or other authorized framework established this institution and when did it take effect?
2. Which instrument provisions define its purpose, duties and limitations, including uncertain interpretations?
3. Which amendments, repeals or contested sources alter the asserted institutional basis over time?
Answer groups: foundation{eventRef,instrumentRef,provisionRef,effectiveAt} mandate{purpose,dutyRefs,limits,interpretationStatus} amendments{instrumentVersions,changeRefs,conflicts,sourcePriority}
### 2.2 Competence jurisdiction and delegation
1. Which subject-matter, territorial, personal and temporal limits qualify each asserted competence?
2. Which delegated powers name a delegator, recipient, legal basis and limits without confusing delegation with reporting?
3. What evidence or authorized interpretation is still missing before relying on the institution's power in a concrete matter?
Answer groups: competence{functionRef,territoryRef,subjectScope,validPeriod,basisRef} delegation{delegatorRef,recipientRef,instrumentRef,limits,revocationRef} reliance{intendedMatter,evidenceRefs,reviewAuthority,unknowns}

## 3 Governance and institutional relationships
### 3.1 Organs posts and representation
1. Which governing organs, organizational units and posts belong to this institution during the relevant period?
2. Which appointment or representation references distinguish a post from its current holder and authorized actions?
3. Which vacancies, acting appointments or competing claims require explicit uncertainty instead of inferred representation?
Answer groups: structure{organRefs,unitRefs,postRefs,validPeriod} representation{holderRef,appointmentRef,authorityScope,start,end} uncertainty{vacancy,actingBasis,contestedClaims,reviewRef}
### 3.2 Oversight and resources
1. Which bodies supervise, sponsor, audit or receive reports from this institution under distinct mandates?
2. Which budget, funding and resource masters are referenced without equating financing with legal control?
3. Which independence guarantees and control assessments coexist under their respective definitions?
Answer groups: oversight{bodyRef,relationType,basisRef,reportRef} resources{budgetRefs,funderRefs,resourceMaster,period} independence{guaranteeRefs,controlAssessment,definitionRef,limitations}

## 4 Functions services and public interface
### 4.1 Functions and delivery responsibility
1. Which public functions and service references are attributed to the institution by authoritative sources?
2. Which services are delivered directly or by another provider while responsibility remains separately recorded?
3. Which service status, eligibility or output details belong to referenced service models rather than institution identity?
Answer groups: functions{functionCodes,serviceRefs,basisRef} delivery{competentAuthorityRef,providerRefs,arrangementRef,period} serviceBoundary{serviceMasterRefs,delegatedFields,mappingLimits}
### 4.2 Locations and contact channels
1. Which official sites, contact points and accessible channels are associated with the institution?
2. Which service territory or jurisdiction differs from office location or correspondence address?
3. How are contact authenticity, availability and publication permission checked without initiating contact?
Answer groups: channels{siteRefs,contactRefs,accessibility,availability} geography{officeLocation,serviceTerritory,jurisdictionRef} verification{officialSource,checkedAt,disclosurePolicy,noContactAction}

## 5 Accountability and information custody
### 5.1 Decisions reports and transparency
1. Which decision registers, reports, publication schemes and oversight records are authoritative references?
2. What information is proactively publishable under which policy, with what exclusions and review dates?
3. Which complaint or review routes are available without assuming that every institution uses the same procedure?
Answer groups: records{decisionRegister,reportRefs,publicationScheme} transparency{policyRef,allowedClasses,exclusions,reviewAt} remedies{processRefs,responsibleBody,scope,limitations}
### 5.2 Provenance correction and custody
1. Which source, steward and effective time support each material institutional assertion?
2. How are conflicting mandate or identity claims corrected without overwriting source history?
3. Which access, retention, legal-hold and custody policies govern institutional evidence and retirement of local copies?
Answer groups: provenance{sourceRef,steward,observedAt,effectivePeriod} correction{claimRefs,expectedHead,reason,reviewOutcome} custody{custodianRef,accessPolicy,retentionPolicy,holdRef,tombstoneScope}

## 6 Institutional change and interoperability
### 6.1 Reorganization and succession
1. Which establishment, merger, split, transfer or abolition event changed the institution's identity or responsibilities?
2. Which instrument and effective dates link predecessor and successor institutions without treating renaming as automatic replacement?
3. Where do unresolved obligations, service responsibilities and records custody pass according to explicit evidence?
Answer groups: change{eventType,originalRefs,resultingRefs,identityDecision} basis{instrumentRef,provisionRef,effectiveAt,recordedAt} succession{obligationRefs,serviceTransfers,custodyTransfers,unknowns}
### 6.2 Mapping and acceptance
1. Which pinned organization or service vocabulary maps the institutional record and with what semantic limits?
2. Which lost authority, time, identity or disclosure qualifiers make a projection unacceptable?
3. Which executable tests and legal-profile reviews remain necessary before operational reliance?
Answer groups: mapping{profileRef,version,fieldMap,relationLimits} loss{requiredQualifiers,unmappedFields,refusalReason} acceptance{testRefs,reviewer,openHolds,relianceDecision}
