The team recommendations converge. I am writing the independent research brief from the retrieved sources and those locked decisions.

# EM-XCT-07 — Action, authority and agent delegation

**Independent research brief · reviewable-draft · not an implementation approval**  
Catalogue contour: `EM-XCT-07` · public card: https://ver.cy/enterprise/models/em-xct-07/  
Proposed companion identity: `vr.profile.enterprise-action-authority`  
Assurance: research/design only. No package is published. This brief does not approve code, claim OAuth / ODRL / XACML / PROV / Cedar / AWS conformance, or assert agreement with any other provider.

---

## 1. Retrieval record and source status

Independently retrieved (this study):

| Source | Status | URL |
|---|---|---|
| EM-XCT-07 public card | Queued / being researched; no package | https://ver.cy/enterprise/models/em-xct-07/ |
| WM-XCT-002 Access Contract / Consent spec.yaml | Mixin 0.3.0-research.1; READ/DISCLOSE only | https://ver.cy/models/wm-xct-002-access-contract-consent/spec.yaml |
| WM-XCT-029 Obligation / Commitment spec.yaml | Mixin 0.3.0-research.1; duty, not execution | https://ver.cy/models/wm-xct-029-obligation-commitment/spec.yaml |
| WM-XCT-023 Party Role | Role assertion ≠ system permission | https://ver.cy/models/wm-xct-023-party-role/ |
| EM-XCT-02 Fact Authority (style neighbour) | Listed actions confer no permission | https://ver.cy/models/enterprise-fact-authority/ |
| MMAS-Core | Architecture draft | https://ver.cy/spec/docs/02-architecture/MMAS-Core.md |
| MMAS Event | Working Draft 2.0 | https://ver.cy/spec/docs/04-core-concepts/Event.md |
| MMAS Contract | Working Draft 2.0 | https://ver.cy/spec/docs/04-core-concepts/Contract.md |
| MMAS-Interchange | Working Draft 2.0 | https://ver.cy/spec/docs/02-architecture/MMAS-Interchange.md |
| RFC 8693 | Standards Track, Jan 2020 | https://www.rfc-editor.org/rfc/rfc8693.html |
| RFC 9110 §9.2.2 | Internet Standard, June 2022 | https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2 |
| ODRL Information Model 2.2 | W3C Recommendation, 15 Feb 2018 | https://www.w3.org/TR/odrl-model/ |
| PROV-O | W3C Recommendation, 30 Apr 2013 | https://www.w3.org/TR/prov-o/ |
| AWS EC2 idempotency | Vendor practice | https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html |
| Cedar authorization | Vendor language | https://docs.cedarpolicy.com/auth/authorization.html |
| Stripe idempotent requests | Vendor practice (contrast) | https://docs.stripe.com/api/idempotent_requests |
| IETF idempotency-key header | Expired draft, not an RFC | https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/ |

**SHA mismatch (disclose, do not paper over).** The brief supplied SHA-256 `9085d977567f3e1fc0b9bb27c6a7c517139f5972a1b95bf4a2bedccdb10bf2db` for WM-XCT-002 and `33b9845b2b334949d5538c1c859dbb41c23872577ae6d3502cd48267f17a8e2a` for WM-XCT-029. Independently retrieved publication metadata shows `synthesisSha256` `478f7f042a8e07f35841d570a062d74561e5bb0eaefc1644c7a1b370177a7abb` (XCT-002) and `20847999df73be6906086dcc4432bec3ab21101c4041ce5f318ebe6633f6cc9e` (XCT-029). Bytes were not re-hashed here. Treat the brief hashes as unverified. Source-inventory reading does not verify every external parent citation.

**Not independently retrieved (limits of this study):**

- Full public WM-XCT-001 Ownership / Delegation specification (referenced by many siblings; no complete public spec body retrieved in this pass).
- Native Vercy file-runtime 1.0.0 schema file itself (event field constraints taken from the supplied brief, not verified against a public repository).
- ISO paid clauses already flagged as unretrieved in the parent obligation spec.
- AWS official ClientToken TTL / retention period (not stated on the EC2 idempotency page).
- Live byte verification of parent spec SHA-256 values.
- EDPB Guidelines 05/2020 and other parent-held sources.

Parent resemblance is not an exact match and not a runtime import.

**Parent tensions this contour must not inherit silently:**

- XCT-002 excludes write / modify / delete; its normative core is read / disclosure. It is not the write-permission instrument.
- Consent is one legal basis, not a universal gate.
- Emergency / break-glass is both listed and deferred in XCT-002 — **defer here**; do not mint backdated authority.
- XCT-002 access layer is deny-by-default; a neighbouring “read CRUD offers an unlisted role a validity token” tension is **not** imported. This contour is default-deny.
- XCT-029 boundary allows statutory / voluntary duties without an agreement, while composition text marks an Agreement reference required. **Do not force that inconsistent Agreement dependency into this package.**
- Delegating performance does not transfer the duty or accountability.
- A performed action does not prove fulfilment or acceptance of a duty.
- A corrected observation does not undo an effect.
- Diagnostics and fingerprints must not be disclosed to an unauthorized reader.

---

## 2. Candidate decisions

The four candidate names on the public card are questions, not four object masters.

| Candidate | Decision | Kind | What it becomes |
|---|---|---|---|
| **ActionContract** | Reject as a master name | **PROFILE + NEW small object** | Split. **ActionDefinition** is a new versioned catalogue object (action meaning, payload schema, effect class, reversibility, required role kinds). Semantic-license terms (parties, purpose, scope, validity, revocation) are a **PROFILE / REFERENCE** of MMAS Contract. Durable READ grants stay in WM-XCT-002 by reference. Duties stay in WM-XCT-029 by reference. Naming “ActionContract” would collide with Access Contract and MMAS Contract. |
| **ActionRequest** | Accept as one new object | **NEW object** | Minted **only on ACCEPT**. Content immutable. **ActionProposal** is an embedded draft value: no `requestId`, no retry key, not an Event. |
| **ActionResult** | Reject as a master | **PROFILE of Event** | Observed result / effect is an Event (`recordType=event`) with a governed `eventType` and an embedded result value in `payload`. No parallel Event universe. |
| **AuthorityBinding** | Reject as a master | **EMBEDDED value + REFERENCE** | **AuthorityDecision** = evaluation snapshot pinned to a request or attempt. **DelegationMandate** = new small depth-1 instrument. Roles by reference to WM-XCT-023. Ownership / durable delegation registry by reference to WM-XCT-001 (unretrieved in full — composition gap). A named permission, boolean or hash is not authenticated authority. |

Additional proposed types:

| Type | Decision |
|---|---|
| ActionProposal | Embedded value (draft intent). Not a master. |
| ActionAttempt | Event profile (`attempt-recorded`). Separate identity from request and effect. |
| ActionObservation | Event profile covering `effect-observed`, `effect-unknown`, `effect-compensated`, `observation-corrected`. |
| RetryKeyRecord | New Dimension-local dedup object, not an enterprise master. Host table with tombstone. |
| DelegationMandate | New small object, depth-1 only. |
| CompensationRequest | Deferred as a first-class type. Increment-1 records a compensation-needed Event and requires a **new** request with a **new** key. |
| ImpersonationToken / multi-hop chain / break-glass grant | Deferred. |
| Credential / token verifier | Deferred to the trusted host. |
| Policy engine / PEP / XACML obligation executor | Deferred. XCT-029 already rejected a PEP function; XACML obligations remain a CROSSWALK only. |

A schema shape or enum is not itself a metamodel or master.

---

## 3. Smallest coherent package boundary

**Name.** Enterprise Action Authority · companion profile of EM-XCT-07 · proposed `0.1.0-research`.  
Not a subtype of WM-XCT-002 or WM-XCT-029. Not a universal execution platform.

**What an adopting Dimension can install and use now**

1. Closed schemas for ActionDefinition, ActionProposal, ActionRequest, AuthorityDecision, DelegationMandate, RetryKeyRecord, and the Event-profile vocabulary.
2. A companion semantic validator. Native envelope validation is insufficient (same host rule as EM-XCT-02).
3. Three synthetic Dimension fixtures (founder, matrix, AI service) plus the document-text negative.
4. A deterministic pure reducer: validate → decide → plan. No side effect.
5. One transactional local adapter: reversible **SET-TO-DECLARED-VALUE** of a demo workspace field, under an explicit trusted-host flag.
6. Documentation of host responsibilities, invariants, and deferred increments.

**What the package must not do**

- Arbitrary command execution, network side effect, credential handling, token exchange, or shell.
- Evaluate production authorization (it records an AuthorityDecision shape; the host fills it).
- Claim globally exactly-once external effects from an idempotency table or a local file lock.
- Treat labels, model text, AGENTS instructions, or a document containing “Publish” as a grant.
- Import XCT-002 as a write grant or XCT-029 as an execution engine.

**What production deployment must supply**

| Concern | Owner |
|---|---|
| Authentication of acting identity | Host |
| Resolution of principal, owner, executor, issuer in named master systems | Host + WM-XCT-001 / party registry (neighbour) |
| Current authority evaluation, default deny, fail-closed on unevaluable | Host PDP; package only stores the snapshot |
| Real credential / token verification | Host |
| File lock / durable store / RFC 3339 clock with explicit offset | Host runtime |
| Invocation of the companion validator | Host |
| Fresh READ / DISCLOSE check before returning a cached result | Host + WM-XCT-002 surface |
| Retry-key retention, purge and tombstone | Host |
| Reconciliation of unknown outcomes | Host |
| Any effect other than the local synthetic field write | Out of increment |

Five distinct planes must stay separate: **semantic contract** (schema / validator), **host authorization**, **storage / lock**, **effect transaction**, **emitted evidence**. Crossing them is how this design fails.

---

## 4. Identity and lifecycle boundary

Seven identities must never collapse:

```
actionDefinitionId+version
  ≠ proposalId
  ≠ requestId
  ≠ authorityDecisionId
  ≠ attemptEventId
  ≠ effectEventId
  ≠ dutyId
```

| Thing | Identity | Mutability | When it exists |
|---|---|---|---|
| Versioned action definition | `actionDefinitionId` + `definitionVersion` | New version on change; old versions remain resolvable | Catalogue |
| Proposed intent | `proposalId` | Mutable / withdrawable | Before accept |
| Accepted request | `requestId` | Immutable after accept | After validate + current allow + lock intent |
| Authority decision | `authorityDecisionId` | Snapshot; not updated in place | At accept and again at attempt |
| Transport / apply attempt | `attemptEventId` | Immutable Event | Each try |
| Observed effect | `effectEventId` | Immutable Event | First successful apply only (or unknown / compensated / corrected successors) |
| Underlying duty | `dutyId` in WM-XCT-029 | Owned by that mixin | Optional reference; never implied |

A repeated request, a new attempt and a new effect are not the same identity.

- **Retry of a successful request** returns the same `requestId` and the same `effectEventId`. No second effect.
- **New attempt** of the same request always mints a new Event. Logging an attempt is a side effect RFC 9110 explicitly allows on an idempotent intended effect.
- **New effect** is minted only on first apply. A later attempt of a committed request must not mint a second effect.
- A retry cannot resurrect a withdrawn proposal, skip a policy that changed after accept-but-before-apply, or leak cached payload without a fresh disclosure check.

**Why ActionRequest is not an Event subclass.** The native event envelope (from the supplied runtime brief) requires `recordType=event`, `schemaVersion=1.0.0`, `eventId`, `eventType`, nonempty unique `subjectIds`, `occurredAt`, `recordedAt`, `actorId`, `payload`, `provenance`; top-level rejects other fields. Request fields (retry key, payload schema, authority snapshot, expiry) do not fit that envelope. Store acceptance, attempts and observations as Events that *cite* the request. Do not encode every action as a fake host object merely to pass an installer.

**Why ActionResult is an Event.** MMAS Event is already “an independently identified immutable asserted occurrence” with occurrence time ≠ assertion time, provenance, and append-only correction. That is the observation. Inventing a parallel result universe would duplicate Event.

**Why the Interchange fingerprint is not the retry digest.** MMAS-Interchange sorts arrays as sets and drops descriptive fields (`displayName`, `description`, `assertedAt`, keys beginning `_` or `x-ui`, nulls / empty objects). An idempotency digest must be an ordered byte contract over effect-affecting fields. Use `payloadCanonicalization = em-xct-07-ordered-v1` (UTF-8 JSON, declared key order, arrays **not** sorted, explicit nulls, no dropped effect-affecting fields, SHA-256 over those bytes).

---

## 5. Party separation

Labels are not roles. Every accepted request carries these as **distinct references**, not display strings.

| Role | Meaning | Must not be |
|---|---|---|
| **actingIdentity** | Authenticated caller / agent who submits or applies. RFC 8693 current actor (`act`). | The principal, the owner, or “the system”. |
| **representedPrincipal** | Party on whose behalf the action is taken. RFC 8693 subject; PROV `actedOnBehalfOf` target. | Collapsed into the actor. |
| **issuer** | Who minted the ActionDefinition, DelegationMandate or AuthorityDecision. | The actor by default. |
| **executorAudience** | Intended executor and Dimension / tenant where the request is valid. Wrong audience is a different key space. | Inferred from the actor. |
| **accountableOwner** | Who remains answerable. XCT-029: delegating performance does not move the duty. PROV: the agent acted-for retains some responsibility. | Replaced by the bot that typed. |
| **observer** | `actorId` of the observation Event. May differ from the acting identity. | Assumed equal to the actor. |
| **masterSystem** | Per-identifier scheme and issuer (EM-XCT-01 invariant). | A bare string ID. |

When there is no delegation, `actingIdentity` and `representedPrincipal` MAY be the same party, but both fields remain present. When there is delegation, they MUST differ, and a DelegationMandate MUST be cited.

RFC 8693 §1.1: impersonation makes A indistinguishable from B in a rights context; delegation keeps A’s identity and records that A represents B. §4.1: consumers MUST consider only top-level claims and the current actor; nested `act` claims are informational history, not current authority. This brief **aligns with those distinctions as a design choice**. It does not implement token exchange and does not claim OAuth conformance.

PROV-O `actedOnBehalfOf` / qualified Delegation is descriptive provenance of responsibility for an Activity. It is not a grant.

WM-XCT-023 already models player / role / capacity, `on_behalf_of` / ultimate party, and states that a role assertion grants no system permission. Reference it. Do not copy it.

---

## 6. Schema outline

Cardinalities: `1` required, `0..1` optional, `0..n` / `1..n` repeating. Identifiers are scheme-qualified.

### 6.1 ActionDefinition — NEW object (catalogue)

**Identity / essence.** `actionDefinitionId` (1), `definitionVersion` (1), `actionCode` (1, vocabulary-ref, never locally minted except in a marked extension namespace), `effectClass` (1: `local-synthetic-set` | `read-only` | `external-deferred`), `reversibilityClass` (1: `reversible-declared-inverse` | `irreversible` | `unknown`), `payloadSchemaRef` (1), `idempotencyClass` (1: `put-declared-value` | `non-idempotent-deferred`). Increment-1 permits only `local-synthetic-set` + `reversible-declared-inverse` + `put-declared-value`.

**Lifecycle / time.** `effectiveFrom` (1), `effectiveTo` (0..1), `definitionState` (1: `draft` | `active` | `superseded` | `retired`), `supersedesDefinitionVersion` (0..1). A new version does not rewrite an old request that pinned the previous version.

**Relations / context.** `resourceTypeRefs` (1..n), `requiredRoleKinds` (0..n, references into WM-XCT-023), `purposeVocabularyRef` (1), `dutyTemplateRefs` (0..n, references into WM-XCT-029; optional; not an Agreement import), `inverseActionDefinitionRef` (0..1, required when reversibilityClass = reversible).

**Governance / authority.** `issuerId` (1), `owningDimensionId` (1), `approvalInstrumentRef` (0..1). Listing an action in a catalogue, document or AGENTS file confers no permission.

**Evidence / representation.** `schemaDigest` (1), `canonicalFormRef` (1), `changeNote` (0..1). Descriptive text is not part of the retry digest.

### 6.2 ActionProposal — EMBEDDED value

**Identity / essence.** `proposalId` (1), no `requestId`, no retry key. `actionDefinitionId+version` (1), `payload` (1).

**Lifecycle / time.** `proposalState` (1: `open` | `withdrawn` | `accepted-consumed` | `rejected`). `proposedAt` (1). Withdrawal is allowed until accept.

**Relations / context.** Party tuple (all seven roles, some may be unbound until accept), `resourceRef+version` (1), `purpose` (1).

**Governance / authority.** May cite a draft mandate. Citation is not a decision.

**Evidence / representation.** Proposal bytes are not the retry digest. Accept copies a frozen payload into the request.

### 6.3 ActionRequest — NEW object (accepted, immutable)

**Identity / essence.** `requestId` (1, minted on accept), `actionDefinitionId+version` (1), `resourceId+resourceVersion` (1), `purpose` (1), `payload` (1, frozen), `orderedPayloadDigest` (1), `retryKey` (1).

**Lifecycle / time.** `acceptedAt` (1), `requestExpiresAt` (1), `requestState` (1: `accepted` | `in-flight` | `committed` | `unknown` | `rejected-pre-accept` is not a request). No in-place mutation.

**Relations / context.** Full party tuple (all seven). `proposalId` (0..1). `delegationMandateId` (0..1). `dutyRefs` (0..n). `compensatesRequestId` (0..1). `subjectIds` for the Events that will cite this request.

**Governance / authority.** `authorityDecisionId` (1) at accept. Attempt-time re-evaluation is a new snapshot, stored on the attempt Event.

**Evidence / representation.** Acceptance Event cites `requestId`. The request record is the intent-record; Events are occurrences about it.

### 6.4 AuthorityDecision — EMBEDDED value

**Identity / essence.** `authorityDecisionId` (1), `outcome` (1: `allow` | `deny` | `unevaluable`), `actionDefinitionId+version` (1), `resourceId+version` (1), `actingIdentity` (1), `representedPrincipal` (1), `purpose` (1).

**Lifecycle / time.** `evaluatedAt` (1), `validityHorizon` (1). Reuse after horizon is deny.

**Relations / context.** `policyPinRefs` (0..n), `mandateRef` (0..1), `obligationsNoted` (0..n, advisory CROSSWALK only; not executed).

**Governance / authority.** `decisionIssuer` (1). Default deny. Unevaluable ⇒ no effect (design choice: fail-closed, closer to XCT-002 than Cedar skip-on-error).

**Evidence / representation.** Snapshot bytes. Diagnostics stay on the host; they are not a reader-facing field. A named permission reference, asserted boolean or hash is not this object and is not authority.

### 6.5 DelegationMandate — NEW small object (depth-1)

**Identity / essence.** `mandateId` (1), `mandateVersion` (1), `delegatorPrincipalId` (1), `delegateActingId` (1). The two MUST differ.

**Lifecycle / time.** `validFrom` (1), `validTo` (1), `mandateState` (1: `active` | `suspended` | `revoked` | `expired`). Revocation does not rewrite history.

**Relations / context.** Bounds, all required: `actionDefinitionId+version` (1), `resourceId+version` (1), `purpose` (1), `executorAudienceId` (1), `dimensionId` (1). `chainDepth` (1, must equal 1).

**Governance / authority.** Narrowing only: the mandate MUST be a subset of the principal’s current authority at evaluation time. Widening is invalid. Sub-delegation forbidden. Impersonation forbidden (`actingIdentity` remains visible).

**Evidence / representation.** Instrument digest. PROV `actedOnBehalfOf` may be *projected* as descriptive provenance; it is not the mandate.

### 6.6 RetryKeyRecord — Dimension-local dedup object

See §8 for the exact bound field set.

### 6.7 ActionObservation / ActionAttempt — Event PROFILE

Native Event fields plus governed `eventType`:

- `attempt-recorded`
- `effect-observed`
- `effect-unknown`
- `effect-compensated`
- `observation-corrected`

`payload` carries the embedded result value: `effectStatus`, `workspaceFieldRef`, `declaredValue`, `observedValue`, `unknownReason`, `correctsEventId`, `compensatesRequestId`. Correction appends. Correction does not delete or rewrite the prior Event and does not undo the world effect.

---

## 7. Lifecycle and state transitions

```
ActionDefinition:  draft → active → superseded|retired
                   draft → retired
ActionProposal:    open → withdrawn
                   open → rejected          (no request minted)
                   open → accepted-consumed (request minted)
ActionRequest:     [minted already accepted]
                   accepted → in-flight → committed
                   accepted → in-flight → unknown
                   accepted → rejected is forbidden
                   unknown → committed | unknown   (only via reconcile Event)
DelegationMandate: active → suspended → active
                   active → revoked|expired
RetryKeyRecord:    reserved → in-flight → committed|unknown
                   * → retired-tombstone
```

**Rejected transitions cause no effect.** A proposal that fails validation or authority remains a proposal or is marked rejected; no `requestId`, no retry reservation that can later apply an effect.

**Unknown stays unknown** until a reconcile Event cites evidence. The reducer must not invent success or failure.

**Cancellation.** Open proposals and not-yet-committed accepts may be withdrawn. A committed request is not cancelled by mutation. Compensation is a **new** ActionDefinition / new request / new key, linked by `compensatesRequestId`. The original effect Event remains.

---

## 8. Retry key — exact immutable content

A retry key is a client-supplied opaque identifier in a declared namespace. The server additionally binds a fingerprint of the accepted request. This is a **design choice**, citing RFC 9110 for intended-effect retries, AWS ClientToken for parameter-mismatch conflict, and Stripe for purge-is-a-new-request as contrast. It is not RFC 9110 conformance, not AWS conformance, and not adoption of the expired IETF header draft.

**RetryKeyRecord fields (bound content in bold):**

| Field | Card. | Role |
|---|---|---|
| **retryKey** | 1 | Client-supplied opaque string. No PII. |
| **keyNamespace** | 1 | `vercy.em-xct-07.retry/v1` |
| **dimensionId** | 1 | Keys are not portable across Dimensions. |
| **executorId** | 1 | Runtime that will apply the effect. |
| **actionDefinitionId** | 1 | Versioned action type. |
| **actionDefinitionVersion** | 1 | |
| **resourceId** | 1 | |
| **resourceVersion** | 1 | Stale resource conflicts. |
| **actorId** | 1 | Acting identity. |
| **principalId** | 1 | Represented principal. Both retained. |
| **purpose** | 1 | Exact purpose string / code. |
| **payloadCanonicalization** | 1 | `em-xct-07-ordered-v1` |
| **orderedPayloadDigest** | 1 | SHA-256 of the ordered byte contract. |
| **requestExpiresAt** | 1 | |
| **authorityDecisionId** | 1 | Freshness of the accept-time decision. |
| **authorityEvaluatedAt** | 1 | |
| requestId | 1 | Set at accept. |
| firstAttemptEventId | 0..1 | |
| effectEventId | 0..1 | |
| state | 1 | `reserved` \| `in-flight` \| `committed` \| `unknown` \| `retired-tombstone` |
| retiredAt | 0..1 | |

**Conflict rule.** Same `retryKey` in the same (`keyNamespace`, `dimensionId`, `executorId`) with any bound field from action definition through authority freshness different ⇒ `RetryKeyConflict`. No effect. This follows the AWS `IdempotentParameterMismatch` *practice* (same token + different parameters fails) as a design analogue, not a port of EC2.

**Same key + same bound bytes.** Return existing `requestId` and, if committed, `effectEventId`. No new effect. The HTTP response body MAY differ (RFC 9110). Disclosure of the cached payload is a **new READ** and needs a current XCT-002-class allow.

**Expiration.** A key past `requestExpiresAt` that never committed is not a licence to apply later. It is expired. A committed record remains the name of that historical request.

**Purge.** Retention expiry MUST write `retired-tombstone` carrying key + digest + `retiredAt`. Reuse of a purged key without tombstone would mint a new effect — forbidden. Reuse against a tombstone ⇒ `RetryKeyRetired`. This is **stricter than Stripe**, which treats prune-then-reuse as a new request. Stripe is vendor practice; our choice is the opposite, because silent reuse after purge is the exact failure the brief forbids.

**Why request ≠ attempt ≠ effect, restated for the key.**

- The key names the **accepted request**.
- Each retry is a new **attempt Event** of that request.
- The **effect Event** is minted at most once for a committed put.
- A changed payload under a retained key is not a retry; it is a conflict.
- A new tenant, executor, action version, resource version, actor, principal, purpose or authority snapshot is not the same request.

RFC 9110 §9.2.2: a method is idempotent if the *intended effect* of multiple identical requests equals the effect of one; the server may log each request and keep revision history; the response may differ; clients may retry after a lost response. That justifies retry of a put. It does not justify a second world change, identical response bytes, or globally exactly-once external effects.

AWS ClientToken is regional / zonal, case-sensitive, ≤64 ASCII, and conflicts on parameter change. Scope is not global. TTL is not specified on that page. Later reuse against a terminated instance has broken “always succeed” in the wild (widely reported client issues). Vendor practice is not a theorem.

---

## 9. Authority, delegation, TOCTOU

### 9.1 Smallest useful delegation subset (increment-1)

**In:**

- Depth 1 only.
- Acting identity always present and distinct from the principal when a mandate exists.
- Bounds required: action definition + version, resource + version, purpose, time window, executor / audience, Dimension.
- Narrowing only (intersection with the principal’s current authority). Widening is invalid.
- Accountable owner remains the principal / owner. Performance does not move the duty.
- Current AuthorityDecision required at accept **and** at attempt.

**Deferred:**

- Impersonation (A indistinguishable from B).
- Chains of depth ≥ 2. Nested historical actors are provenance only (RFC 8693 §4.1 alignment, not conformance).
- Emergency / break-glass.
- Real credential or token verification.
- Collective / group consent-as-delegation.
- Sub-delegation / `may_act` token exchange.
- Widening via document text, labels, model instructions, or “Publish” appearing in a file.

### 9.2 Execution authority ≠ disclosure authority

Even a cached committed result requires a fresh read / disclose check before the payload is shown. XCT-002 owns that surface. An execution allow at t0 is not a disclosure allow at t2.

### 9.3 Chosen transaction boundary

Increment-1 boundary = **accept-and-commit of the local synthetic put**, under one host file lock.

```
host authenticates
  → companion validator
  → evaluate current authority (outside lock; advisory only)
  → acquire file lock
  → re-check authority + resource version + retry-key inside lock
  → reserve RetryKeyRecord (state=in-flight) OR conflict/retire
  → apply SET-TO-DECLARED-VALUE OR refuse
  → persist request + attempt Event + effect Event + retry record atomically
  → release lock
```

| Situation | Rule |
|---|---|
| Authority revoked before commit | No effect. |
| Authority revoked after commit | Effect stands. Compensation is a new request. Cached payload may no longer be disclosed. |
| Authority evaluated only outside the lock | Stale. Must re-check inside. |
| Timeout after lock, before durable visibility | `unknown`. Do not invent success. |
| In-flight retry of same key | Second process sees reserved / in-flight record; does not apply. |
| Cancellation of committed work | New compensation request. |
| Reconciliation | Reads request / attempt / effect / retry records. If none, same key may proceed as first accept. If request exists, replay the recorded decision. |
| Dedup purge | Tombstone. Never a blank safe key. |

A local file lock is not a distributed transaction with arbitrary external effects. An idempotency table does not create globally exactly-once effects outside this host.

### 9.4 Cedar, used as contrast not as engine

Cedar: default deny; forbid overrides permit; skip-on-error (an errored policy is ignored; diagnostics are returned so an *application* may fail closed). **Do not describe “deny on any diagnostic” as Cedar’s default.** This increment’s design choice is fail-closed on missing or unevaluable authority, and diagnostics are host-only.

### 9.5 ODRL, used as CROSSWALK not as executor

ODRL Permission allows an Action, with refinements satisfied, if constraints are satisfied and duties fulfilled. Duty is the obligation to exercise an Action. `andSequence` preserves list order and can deadlock. An ODRL Validator checks expression conformance, not runtime execution. Action refinement is not execution. This package may cite ODRL action / constraint terms; it does not run an ODRL evaluator as a PEP.

---

## 10. Bounded executable acceptance

**Effect class permitted in increment-1:** reversible LOCAL SYNTHETIC put of one declared workspace field to a declared value, under an explicit trusted-host flag.

- Not increment, not toggle, not append-only counter. Those are not idempotent puts; they are the counterexample in §16.
- Inverse is a recorded compensation request that sets the previous declared value, and appends `effect-compensated`. History is not deleted.
- No command execution, no network, no credential.

**Reducer (pure).** Inputs: proposal or retry, ActionDefinition, resource version, party tuple, AuthorityDecision, RetryKeyRecord. Outputs: `accept` | `reject` | `conflict` | `replay` | `unknown-needs-reconcile`. No I/O.

**Adapter (transactional, local).** Runs only after `accept` inside the lock. Writes the field, then the evidence, or neither.

**Rejected / unevaluable / conflict:** no field write, no effect Event.

Users can therefore describe and validate their organisation’s action catalogue, party split, depth-1 mandates and request lifecycle **now**. They cannot deploy this package as an execution plane for production side effects.

---

## 11. Mastership and rights

| Record | Master | Who may write | Who may read |
|---|---|---|---|
| ActionDefinition | Adopting Dimension catalogue | Definition steward after host authn + current allow | Catalogue readers under XCT-002 |
| ActionProposal | Proposer’s store / Dimension | Proposer; withdrawal by proposer or principal | Parties on the proposal, under disclosure check |
| ActionRequest | Dimension request store | Minted only by the trusted-host adapter | Parties + auditors, payload under fresh read check |
| AuthorityDecision | Embedded on request / attempt | Written by host PDP at evaluation | Restricted; no diagnostics to unauthorized reader |
| DelegationMandate | Dimension mandate store (pending XCT-001 neighbour) | Delegator / mandate steward | Delegate + auditor; not a public token |
| RetryKeyRecord | Dimension dedup table | Adapter only | Host internals; not a disclosure object |
| Events | Event store | Adapter / observer | Subject to XCT-002 |

Listed actions, catalogue entries, document instructions and AGENTS text confer no operational permission. That sentence is already the published EM-XCT-02 rule and is adopted here as an invariant, not as a subtype claim.

---

## 12. Reference and clock semantics

- All timestamps are RFC 3339 with explicit offset or `Z`. No timestamp is an identifier.
- `occurredAt` ≠ `recordedAt` ≠ `evaluatedAt` ≠ `acceptedAt` ≠ `requestExpiresAt` ≠ `validityHorizon`.
- Resource references pin `resourceVersion`. A later revision is a different bound field.
- Action definitions pin `definitionVersion`. Requests do not float to a newer definition.
- Party identifiers are scheme-qualified and resolved in a named master system. Unresolved identity ⇒ unevaluable ⇒ no effect.
- Duty references, if present, are optional pointers into WM-XCT-029. Presence of an effect Event is not fulfilment.
- Clocks are the host’s responsibility. The package records times; it does not certify them.

---

## 13. Invariants (falsifiable)

**I1** Labels, model text, document instructions and AGENTS files do not grant permission.

**I2** A named permission reference, asserted boolean or hash is not authenticated authority.

**I3** A DelegationMandate cannot widen the principal’s effective authority.

**I4** `definitionRev`, `proposalId`, `requestId`, `authorityDecisionId`, `attemptEventId`, `effectEventId` and `dutyId` are pairwise distinct kinds.

**I5** Same retry key + different bound content ⇒ conflict and zero effect.

**I6** Disclosure of a cached result requires a current read allow, even if execution previously succeeded.

**I7** A rejected or unevaluable transition writes no workspace field and mints no effect Event.

**I8** An `observation-corrected` Event does not delete, rewrite or undo a prior effect identity.

**I9** A purged retry key leaves a tombstone; reuse is `RetryKeyRetired`, never a blank safe key.

**I10** An unknown outcome remains unknown until a reconcile Event cites evidence.

**I11** Under delegation, `actingIdentity` and `representedPrincipal` are both present and different.

**I12** An `effect-observed` Event does not imply WM-XCT-029 fulfilment or acceptance.

**I13** Nested historical actors are not current authority.

**I14** Increment-1 `effectClass` is `local-synthetic-set` of a declared value; increment and toggle are rejected as non-idempotent.

**I15** Default deny. Fail-closed on unevaluable. No validity token for an unlisted role.

---

## 14. Bundles, layers, and Finding → Question → Artifact → Action

Fifteen-plus routes. Listed actions in this table still confer no permission.

### Bundle AA — Action identity and catalogue

**Layer AA-DEF · Definition versus permission**

1. **F** `description-is-not-permission` → **Q** Does a catalogue entry, document heading or AGENTS verb grant execute rights? → **A** ActionDefinition + negative fixture → **Act** `reject-unauthenticated-intent` (no effect).
2. **F** `definition-version-pin` → **Q** Which definition version did the request pin, and did it float? → **A** `actionDefinitionId+version` on the request → **Act** `reject-unpinned-or-floated-definition`.

**Layer AA-LIFE · Proposal versus request**

3. **F** `proposal-is-not-request` → **Q** Was a `requestId` minted before accept? → **A** ActionProposal value with empty requestId → **Act** `refuse-retry-key-on-proposal`.
4. **F** `withdrawn-proposal-not-resurrected` → **Q** Can a retry recreate a withdrawn proposal as an effect? → **A** proposalState=withdrawn → **Act** `reject-resurrection`.

### Bundle AR — Request, retry and effect identity

**Layer AR-KEY · Idempotency contract**

5. **F** `retry-one-effect` → **Q** What exact bytes does the retry key bind, and is the digest ordered? → **A** RetryKeyRecord + `em-xct-07-ordered-v1` spec → **Act** `replay-or-conflict`.
6. **F** `changed-payload-same-key` → **Q** Does any bound field differ? → **A** mismatch report → **Act** `RetryKeyConflict` (no effect).
7. **F** `fingerprint-is-not-digest` → **Q** Was the Interchange semantic fingerprint used as the idempotency digest? → **A** canonicalization code check → **Act** `reject-interchange-fingerprint-as-retry-digest`.
8. **F** `purge-not-blank` → **Q** Does a retained tombstone exist for this key? → **A** retired-tombstone row → **Act** `RetryKeyRetired`.

**Layer AR-OUTCOME · Attempt versus effect versus unknown**

9. **F** `request-neq-attempt-neq-effect` → **Q** Which of the three identities does this record claim? → **A** request / attempt Event / effect Event triple → **Act** `mint-attempt-always; mint-effect-at-most-once`.
10. **F** `unknown-stays-unknown` → **Q** Is there durable evidence of apply or of non-apply? → **A** `effect-unknown` Event → **Act** `reconcile-only-with-evidence`.
11. **F** `correction-does-not-undo` → **Q** Does a later correction retract the prior effect identity? → **A** `observation-corrected` Event with `correctsEventId` → **Act** `append-only`.

### Bundle AU — Authority and delegation

**Layer AU-NOW · Current decision**

12. **F** `role-label-is-not-grant` → **Q** What instrument and current decision are required? → **A** DelegationMandate + AuthorityDecision → **Act** `validate-current-authority`.
13. **F** `boolean-or-hash-is-not-authority` → **Q** Is the caller presenting a permission name, flag or digest in place of a decision snapshot? → **A** rejected input shape → **Act** `deny-unevaluable`.
14. **F** `stale-decision` → **Q** Is `evaluatedAt` inside `validityHorizon` and is the mandate unrevoked **inside the lock**? → **A** decision snapshot + mandate state → **Act** `re-evaluate-or-deny`.
15. **F** `execution-vs-disclosure` → **Q** May this reader see the cached observation payload now? → **A** fresh XCT-002-class coverage decision → **Act** `project-or-deny`.

**Layer AU-SCOPE · Delegation bounds**

16. **F** `impersonation-forbidden` → **Q** Are acting and principal both recorded and, under mandate, different? → **A** party tuple → **Act** `reject-if-actor-omitted-or-collapsed`.
17. **F** `depth-1-only` → **Q** Is `chainDepth > 1` or is a nested mandate present? → **A** `mandate.chainDepth` → **Act** `reject-depth-gt-1`.
18. **F** `narrowing-only` → **Q** Is every bound a subset of the principal’s current authority? → **A** scope-diff → **Act** `reject-widening`.
19. **F** `wrong-audience-or-tenant` → **Q** Does `dimensionId` / `executorId` match the key space? → **A** RetryKeyRecord namespace fields → **Act** `reject-wrong-audience`.
20. **F** `duty-not-transferred-by-performance` → **Q** Who remains accountable after the executor applies? → **A** `accountableOwner` → **Act** `retain-owner`.

### Bundle AE — Effect, compensation, host limits

**Layer AE-LOCAL · Synthetic put**

21. **F** `only-declared-put` → **Q** Is `effectClass` anything other than `local-synthetic-set` of a declared value? → **A** ActionDefinition.effectClass → **Act** `reject-increment-toggle-external`.
22. **F** `compensation-is-new-request` → **Q** Is cancellation being attempted by mutating the committed request? → **A** new request with `compensatesRequestId` → **Act** `refuse-in-place-cancel`.
23. **F** `stale-resource` → **Q** Does `resourceVersion` still match the locked current revision? → **A** resource pin → **Act** `reject-stale-resource`.

---

## 15. Three synthetic profiles and one negative

All names, units and identifiers below are invented.

### (a) Founder — reversible demo workspace update

Founder `F` is acting identity = principal = owner = executor in Dimension `dim-demo-co`.  
ActionDefinition `workspace.field.set` v1, `effectClass=local-synthetic-set`, resource `DemoCoWorkspace@rev12`, purpose `demo-setup`, payload `{ "path": "displayName", "value": "Demo Co" }`.  
Host authenticates `F`. AuthorityDecision `allow` at t0, horizon 10 minutes. Adapter sets the field. Emits accepted-request Event + `effect-observed`. Compensation is a new request that sets the previous declared value and emits `effect-compensated`. History remains.

**Shows:** collapsed party roles are legal when they are in fact the same party, but the seven fields still exist. Testers must not stop at this profile.

### (b) Matrix — four distinct parties

Employee `E` proposes. Represented principal = unit `Finance-EMEA`. Executor = `SharedServicesBot`. Accountable owner = `VP-Finance`.  
DelegationMandate depth-1 from `VP-Finance` to `SharedServicesBot`: action `cost-center.relabel` v2, resource `CC-441@v3`, purpose `close-books`, audience `erp-adapter` (in increment-1 the adapter is still the local synthetic stand-in), window 48 hours.  
`E` may propose. The bot may execute only inside the mandate. The VP remains accountable. A work-assignment record describing `E`’s post is not a grant to the bot.

**Shows:** the party split the founder profile hides.

### (c) AI service — tightly scoped delegated context

User `U` issues DelegationMandate to service `S`: action `record.annotate` v1, resource `Record-77@v5`, purpose `suggest-tags`, audience `annotator-runtime`, window 15 minutes, payload class `annotation-draft`.  
`S` proposes. Accepted request stores a draft annotation. `S` cannot publish, cannot change resource, cannot change purpose, cannot extend the window, cannot sub-delegate.

**Shows:** an AI proposer with a current, narrow, time-boxed mandate. Nested `act` history, if recorded for provenance, is not authority.

### Negative — document text is not a grant

Agent `A` reads a document that contains the heading “Publish” and an ActionDefinition name. `A` submits an ActionRequest `publish` with no current AuthorityDecision and no DelegationMandate. Validator rejects. No field write. No effect Event. A rejected proposal may remain as evidence of the attempt to treat text as a grant.

Aligns with EM-XCT-02: listed actions confer no permission.

---

## 16. Test matrix — increment versus host

| Case | First increment (validator + synthetic adapter) | External host must supply |
|---|---|---|
| Retry with one effect | Same key + same digest → replay `requestId` + `effectEventId`, no second put | Durable retry table across processes |
| Changed payload / same key | `RetryKeyConflict`, no effect | — |
| Wrong audience / tenant | Reject | Tenant isolation of the store |
| Authority expiry / revocation before commit | Deny inside lock, no effect | Live revocation signal |
| Authority revocation after commit | Effect stands; compensation is a new request | Revocation bus |
| Stale resource | Reject on version mismatch | Current resource revision |
| Concurrent / reordered delivery | File lock serialises one process | Multi-host consensus; file lock is local only |
| Unknown outcome | `effect-unknown`; no invented success | Reconcile procedure + operator authority |
| Cached-result disclosure denial | Schema requires a disclosure-check slot | Actual XCT-002 coverage evaluation |
| Cancellation / compensation | New request + `effect-compensated`; no history delete | External compensating actions |
| Corrected history | Append `observation-corrected` | — |
| Document-text negative | Reject, no effect | — |
| Increment / toggle definition | Rejected by `effectClass` | — |
| Purged key reuse | `RetryKeyRetired` if tombstone present | Tombstone retention job |
| In-flight second waiter | Sees `in-flight`, does not apply | Cross-process lock |

---

## 17. Migration and compatibility

- No existing EM-XCT-07 package. First published companion would be `0.1.0-research`.
- Do not treat published WM-XCT-002 or WM-XCT-029 as completed coverage of this card. The public card already says a published parent does not complete it.
- Requests pin definition and resource versions. A later catalogue version does not mutate historical requests.
- Event `eventType` vocabulary is additive. Unknown types are unevaluable, not silently ignored as permits.
- If WM-XCT-001 later publishes a durable delegation registry, DelegationMandate becomes a reference or a profile — not a second master. That composition is currently a gap because XCT-001 was not fully retrieved.
- Do not migrate XCT-002 consent instruments into write grants.
- Do not migrate XCT-029 duties into an execution engine, and do not require an Agreement object to exist before an ActionDefinition can be catalogued.

---

## 18. Limits and deferred increments

Deferred on purpose:

- Multi-hop delegation, impersonation, `may_act` token exchange, OAuth / RFC 8693 implementation.
- Emergency / break-glass.
- Real credential verification, policy engines, XACML PEP, Cedar evaluation as the PDP.
- Arbitrary external effects, command execution, network I/O.
- Globally exactly-once semantics.
- Collective consent-as-delegation.
- Duty fulfilment / acceptance engine (stays in XCT-029).
- Compensation of non-synthetic effects as a first-class type.
- Distributed transactions.
- Using MMAS-Interchange fingerprint as an idempotency digest.

---

## 19. Strongest counterexample to this design

Two related holes. Either is enough to refuse an implementation approval.

**Hole A — crash between put and evidence.**  
The adapter writes the workspace field, then crashes before RetryKeyRecord and the effect Event are durable. Restart sees no request. The client retries the same key. If the effect class were increment or toggle, the second apply is a **new effect under the same key**. Even with SET-TO-DECLARED-VALUE, a crash after a *different* interleaving (request reserved, field not written, reservation lost) yields `unknown`, not success. A file lock plus an idempotency table does not make that crash globally exactly-once. The honest state is `unknown` plus an explicit reconcile Event. Any brief that treats “accepted” as “effected” invents a false effect.

**Hole B — retry hit without fresh authority.**  
A depth-1 mandate is accepted at t0. The principal’s underlying policy is revoked at t1. At t2 someone retries the same key, or merely reads the cached observation. If the increment treats a RetryKey hit as “return cached effect and payload” without (i) distinguishing replay of identity from disclosure of payload and (ii) re-checking authority before a *first* apply of an in-flight request, it both resurrects execution authority and leaks output. Execution allow is not disclosure allow.

Mitigations already written into the increment: put-only effect class; reserve the retry record inside the lock before apply; `unknown` rather than guessed success; replay returns identifiers; payload disclosure is a new READ; attempt-time re-evaluation before first effect; tombstones on purge. Residual risk remains at any host that skips those steps, and at every effect that leaves this process.

---

## 20. Remaining uncertainty

- WM-XCT-001 Ownership / Delegation spec was not independently retrieved in full. Mastership of DelegationMandate versus that neighbour is a declared gap.
- Native runtime 1.0.0 schema file was not fetched; event constraints are taken from the supplied brief.
- Parent SHA-256 values in the brief do not match live `synthesisSha256`. Bytes were not re-hashed.
- AWS ClientToken retention is unpublished on the cited page.
- Interchange canonicalization was retrieved as a Working Draft; a public byte-level test vector for `em-xct-07-ordered-v1` does not yet exist and must be published with any later package.
- Composition field-for-field with MMAS Contract was verified against the Working Draft, not against a frozen 1.0 contract schema.
- Jurisdiction, collective principals, and credential assurance levels remain host and neighbour problems.

---

## 21. Implementation-ready recommendation

Publish this contour as a **reviewable-draft companion profile**, not as a world-model subtype and not as an execution platform.

**Accept now (design):** ActionDefinition (new small catalogue), ActionProposal (embedded draft), ActionRequest (new, minted on accept), AuthorityDecision (embedded snapshot), DelegationMandate (depth-1, narrowing), RetryKeyRecord (Dimension-local, ordered digest, tombstone), ActionAttempt / ActionObservation (Event profiles), local synthetic SET-TO-DECLARED-VALUE adapter under an explicit trusted host, companion validator, three synthetic fixtures plus the document-text negative.

**Reject now:** four independent masters named ActionContract / ActionRequest / ActionResult / AuthorityBinding; ActionResult as a parallel Event universe; Interchange fingerprint as a retry digest; XCT-002 as a write grant; XCT-029 Agreement as a required import; impersonation; multi-hop; break-glass; PEP; exactly-once claims; increment / toggle as increment-1 effects.

**Do not issue an implementation approval.** Subsequent work is implement → test → independently audit → publish the accepted increment in English, with host responsibilities stated on the package door. No OAuth, ODRL, XACML, PROV, Cedar or AWS conformance claim is warranted by this brief.
