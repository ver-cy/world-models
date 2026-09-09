# WM-ORG-012 authored subject design

Preparation only, not validated output. Six bundles, twelve findings and thirty-six
questions. Each finding must serialize three explicit answer groups, not a
generic repeated fields list. Proposed structure is Vercy design, not a claim
that any cited standard prescribes these six bundles.

## 1 Relationship identity and endpoint semantics

### 1.1 Source-qualified relationship identity
1. Which master namespace and identifier distinguish this relationship from
   another relationship between the same organizations?
2. Which versioned kind definition makes it partnership, affiliation, supply,
   control or another relation, and which near-neighbour kinds are excluded?
3. Which scope qualifier distinguishes parallel relationships by service,
   geography, business unit or agreement without overwriting one another?
Answer groups: identity{namespace,id,master}; kind{scheme,version,code,exclusions};
scope{dimensions,values,parallelRelationshipRefs}.

### 1.2 Participants, direction and multiplicity
1. Which organization references occupy each endpoint role and which identity
   resolution remains unknown or disputed?
2. Is the relation directional, reciprocal or symmetric under its kind, and
   what inverse label preserves rather than changes its meaning?
3. Is this a bilateral relation or a multi-party arrangement, and what is lost
   if its membership is exported as pairwise edges?
Answer groups: participants{orgRefs,roles,resolution}; direction{kind,inverse};
arity{arrangementRef,participantSet,pairwiseLoss}.

## 2 Relationship basis and domain extent

### 2.1 Basis, recognition and authority
1. What evidence establishes the claimed relation rather than merely common
   branding, a shared address or an unverified marketing statement?
2. Who asserts or recognizes it, in which capacity, and does the other party
   confirm, contest or have no recorded position?
3. Which governing instrument and jurisdiction qualify the assertion without
   transferring contract ownership or legal adjudication to this record?
Answer groups: recognition{signals,counterexamples,evidenceRefs}; positions
{claimant,capacity,counterpartyPosition}; basis{instrumentRefs,jurisdiction}.

### 2.2 Control and ownership interpretation
1. Does the relation concern accounting consolidation, equity, votes, other
   control or beneficial interest, and which definition applies?
2. What share, range, denominator, class, date and uncertainty qualify a
   quantitative interest instead of an unqualified percentage?
3. Is direct or indirect control explicitly evidenced, which intermediate
   records support it, and which inference rules are prohibited?
Answer groups: controlBasis{type,definition,accountingStandard}; interest
{value,min,max,denominator,class,asOf,uncertainty}; chain{directness,components,
derivationRule,prohibitedInferences}. Ownership masters are referenced.

## 3 Collaboration and exchange boundaries

### 3.1 Partnership purpose and responsibilities
1. What jointly stated purpose and activity scope belong to this collaboration?
2. Which responsibilities are attributed to each party and where are their
   governing mandates mastered?
3. What limits distinguish the collaboration from a newly formed legal entity
   or permission for an agent to bind either party?
Answer groups: purpose{statement,scope,evidence}; responsibilities{party,role,
mandateRef}; boundary{entityFormationRef,excludedAuthorities}.

### 3.2 Supply and service linkage
1. Which party supplies and which receives what defined service or product
   scope, without importing orders, delivery events or payments here?
2. Is the linkage prospective, awarded, observed or terminated, and what
   process-qualified evidence establishes that state?
3. Which customer/account or supplier-qualification models master the detailed
   commercial lifecycle and which fields must not be duplicated here?
Answer groups: exchange{provider,recipient,scopeRefs}; commercialAssertion
{stage,evidenceRef,processRef}; delegation{modelRefs,masterFields,excludedFields}.

## 4 Time, lifecycle and graph interpretation

### 4.1 Effective interval and record history
1. When did the relationship take effect and cease, at what precision, and
   are interval endpoints known, estimated or open?
2. When was the assertion observed, recorded and published, distinct from its
   effective interval, and which revision supersedes it?
3. Does closure mean real-world termination, publisher record retirement or
   correction of erroneous data, and how is that distinction retained?
Answer groups: validTime{start,end,precision,uncertainty}; knowledgeTime
{observedAt,recordedAt,publishedAt,supersedes}; closure{meaning,reason,evidence}.

### 4.2 Graph derivation and structural constraints
1. Which kind-specific constraints permit or forbid self-links, cycles and
   multiple parents without imposing one universal organization tree?
2. Which direct records, time slice and rule generated an indirect relation,
   and can the derived edge be reproduced separately from asserted data?
3. What ambiguity or information loss arises from merging conflicting,
   incomplete or differently scoped relationship graphs?
Answer groups: graphRules{profile,cardinality,cyclePolicy,selfLinkPolicy};
derivation{inputRefs,asOf,ruleVersion,outputKind}; graphLoss{gaps,conflicts,scope}.

## 5 Evidence, dispute and stewardship

### 5.1 Evidence quality and counterclaims
1. Which attributable source, exact record and retrieval context support each
   relationship assertion, and what validation has actually occurred?
2. Which contradictory assertions coexist and who may resolve their conflict
   under the Dimension policy rather than overwrite inconvenient evidence?
3. Does missing data mean unknown, withheld, not reported, expired or explicit
   non-existence within a defined search scope?
Answer groups: evidence{source,recordRef,retrievedAt,validation}; dispute
{claims,resolutionAuthority,status}; absence{reason,coverageScope,searchTime}.

### 5.2 Mastership, freshness and permitted disclosure
1. Which system and role master this relationship record and when is review due?
2. Which fields or endpoints are confidential, redacted or publicly reusable
   under a stated access policy and source license?
3. How does a redacted projection preserve the distinction between withheld
   and absent information while retaining an authorized evidence trail?
Answer groups: stewardship{master,steward,reviewDue}; disclosure{fieldClasses,
policyRef,licenseRef}; projection{redactions,reasonCodes,auditRef}.

## 6 Exchange and operational acceptance

### 6.1 Versioned external mappings
1. Which exact relationship kinds map to ORG, GLEIF RR-CDF, BODS or OCDS,
   and which merely have broader or narrower correspondence?
2. What qualifiers, time precision, multi-party structure or assertion status
   would be lost in each export?
3. Which pinned schema/profile and round-trip fixtures demonstrate accepted
   mappings rather than an unsupported conformance claim?
Answer groups: mapping{sourcePath,targetTerm,relationType,version}; losses
{fields,meaning,requiredWarnings}; acceptance{schemaDigest,fixtures,result}.

### 6.2 Safe relationship maintenance operations
1. Which policy permits an agent to record, revise, dispute or retire the
   local assertion without creating or ending the real-world relationship?
2. Which expected revision and graph checks must pass before an append,
   and what conflict response preserves concurrent evidence?
3. What post-write checks and compensating revision restore correctness
   without deleting provenance or silently widening disclosure?
Answer groups: operationAuthority{operation,policy,delegation,excludedEffects};
preconditions{expectedHead,graphChecks,onConflict}; recovery{postChecks,
compensationRef,provenancePreservation}.

Proposed six functions: resolve relation identity; inspect qualified graph;
record attributed assertion; append lifecycle revision; register dispute;
export permitted loss-aware projection. Each needs inputs, outputs,
preconditions, effects, failure modes and explicit authority in serialization.

Physical measurements not applicable: direct properties are endpoint roles,
kind, direction, scope, qualified interest and time. Organization properties
and contract actions remain delegated. Missing ledger edges stay proposed.
