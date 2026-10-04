# Complete field contract

Every schema object is closed. All table fields are required; explicit null alternatives are shown. A required nullable reference preserves unknown/absent distinctly from a fabricated default. Arrays preserve supplied order, including labels and duplicates; membership semantics are explicitly documented for scopes. Sensitivity is host-governed restricted context by default; declaration catalogs may be projected publicly only with separate authority.

## ActionDefinition

Master/writer: Definition steward / trusted admitting host. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| format | `{"enum":["enterprise-action-definition/0.1.0"]}` | Exact wire format/version discriminator; unknown formats are refused. |
| definitionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Stable governed identity of the operation, independent of its revision. |
| version | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"}` | Immutable semantic definition revision; same ID/version cannot change bytes. |
| name | `{"type":"string","minLength":1,"maxLength":2048}` | Human-readable label; not an identity or execution instruction. |
| description | `{"type":"string","minLength":1,"maxLength":2048}` | Explanatory text; never changes the selected adapter effect or grants rights. |
| mode | `{"enum":["synthetic-executable","descriptive-only"]}` | Whether a definition is descriptive-only or admitted to the closed synthetic adapter. |
| parameterContract | `{"anyOf":[{"enum":["ordered-label-list/1"]},{"type":"object","properties":{"uri":{"type":"string","pattern":"^(urn:\|https://)[!-~]+$","maxLength":512},"revision":{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"},"sha256":{"type":"string","pattern":"^[a-f0-9]{64}$"}},"required":["uri","revision","sha256"],"additionalProperties":false}]}` | Exact labels-contract identifier for execution, or opaque pinned external parameter document for descriptive use. |
| targetType | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Declared target class; executable definitions require the synthetic ordered-label resource. |
| precondition | `{"type":"string","minLength":1,"maxLength":2048}` | Fixed guard identifier for executable definitions; descriptive text for external-only use. |
| effectBoundary | `{"type":"string","minLength":1,"maxLength":2048}` | Fixed local effect identifier for executable definitions; descriptive text for external-only use. |
| adapter | `{"enum":["local-sqlite-ordered-labels/1","none"]}` | Only local-sqlite-ordered-labels/1 executes; none is descriptive-only. |
| validFrom | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Inclusive beginning of definition/scope validity, integer UTC epoch seconds. |
| validUntil | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Exclusive end of definition/scope validity, integer UTC epoch seconds. |
| purposes | `{"type":"array","items":{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"},"minItems":1,"maxItems":16,"uniqueItems":true}` | Exact case-sensitive allowed definition purposes; no wildcards or purpose inference. |
| authorityRequirement | `{"enum":["current-exact-principal-and-actor-scope"]}` | Explicit requirement for current exact principal and actor scope; not a grant. |
| compensation | `{"enum":["new-request-restores-before-labels-at-exact-after-revision","external-unspecified"]}` | Selected compensation contract, or external-unspecified for descriptive definitions. |
| stewardId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Accountable semantic steward asserted by the admitting host; no automatic execution authority. |
| masterId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Declared definition master; host verifies the source before admitting this snapshot. |
| legacyCrosswalk | `{"anyOf":[{"type":"object","properties":{"uri":{"type":"string","pattern":"^(urn:\|https://)[!-~]+$","maxLength":512},"revision":{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"},"sha256":{"type":"string","pattern":"^[a-f0-9]{64}$"}},"required":["uri","revision","sha256"],"additionalProperties":false},{"type":"null"}]}` | Optional descriptive legacy alignment Pin; null means no alignment claimed. |

## ActionRequestSnapshot

Master/writer: Requesting principal for intent; host for admission and derived fields. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| requestId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Host-minted immutable request identity; deliberately outside the client intent bytes. |
| keyHash | `{"type":"string","pattern":"^[a-f0-9]{64}$"}` | Digest of authenticated actor ID and exact retry key within one Dimension store; retained for nonreuse. |
| intentDigest | `{"type":"string","pattern":"^[a-f0-9]{64}$"}` | SHA-256 under the bounded Python encoding of the complete immutable intent. |
| intent | `{"type":"closed object","children":"expanded below"}` | One immutable statement of requested effect and context. |
| intent.format | `{"enum":["enterprise-action-intent/0.1.0"]}` | Exact wire format/version discriminator; unknown formats are refused. |
| intent.dimensionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Owning Dimension namespace; exact match against trusted store required. |
| intent.definition | `{"type":"closed object","children":"expanded below"}` | Exact definition identity/version/content hash used for this intent. |
| intent.definition.definitionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Stable governed identity of the operation, independent of its revision. |
| intent.definition.version | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"}` | Immutable semantic definition revision; same ID/version cannot change bytes. |
| intent.definition.sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}$"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |
| intent.resourceId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Existing synthetic target resource identity; no URL or executable command. |
| intent.expectedRevision | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Required target version before the first effect; optimistic concurrency, not a timestamp. |
| intent.parameters | `{"type":"closed object","children":"expanded below"}` | Closed ordered-label payload; arbitrary action parameters are unsupported by the executor. |
| intent.parameters.labels | `{"type":"array","items":{"type":"string","maxLength":200},"minItems":0,"maxItems":32}` | Replacement list; order and duplicates are meaningful, Unicode is not normalized. |
| intent.actorId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Executor identity that must match the separately authenticated host actor. |
| intent.principalId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Party represented; distinct from actor in direct-representation mode. |
| intent.purpose | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"}` | Exact intended use; participates in both scope checks and definition purposes. |
| intent.audience | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Exact intended executor/host audience; unknown or mismatched audience denies. |
| intent.expiresAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Exclusive deadline for a first effect while pending; does not expire committed receipts. |
| intent.compensatesReceiptId | `{"anyOf":[{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"},{"type":"null"}]}` | Optional retained prior receipt to compensate; context and revision guards apply. |
| submittedAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Host admission time, integer UTC epoch seconds. |
| submissionEventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Exactly one native submission Event belonging to this request. |
| state | `{"enum":["pending","committed","cancelled","expired","rejected-precondition"]}` | Derived execution state from retained history; never native object state or caller-editable intent. |
| receiptId | `{"anyOf":[{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"},{"type":"null"}]}` | Derived committed receipt Event ID; null if no effect committed. |
| keyRetired | `{"type":"boolean"}` | Derived retained-key marker, permitted only after a terminal state. |

## Intent

Master/writer: Authenticated requesting actor; immutable after host admission. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| format | `{"enum":["enterprise-action-intent/0.1.0"]}` | Exact wire format/version discriminator; unknown formats are refused. |
| dimensionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Owning Dimension namespace; exact match against trusted store required. |
| definition | `{"type":"closed object","children":"expanded below"}` | Exact definition identity/version/content hash used for this intent. |
| definition.definitionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Stable governed identity of the operation, independent of its revision. |
| definition.version | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"}` | Immutable semantic definition revision; same ID/version cannot change bytes. |
| definition.sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}$"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |
| resourceId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Existing synthetic target resource identity; no URL or executable command. |
| expectedRevision | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Required target version before the first effect; optimistic concurrency, not a timestamp. |
| parameters | `{"type":"closed object","children":"expanded below"}` | Closed ordered-label payload; arbitrary action parameters are unsupported by the executor. |
| parameters.labels | `{"type":"array","items":{"type":"string","maxLength":200},"minItems":0,"maxItems":32}` | Replacement list; order and duplicates are meaningful, Unicode is not normalized. |
| actorId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Executor identity that must match the separately authenticated host actor. |
| principalId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Party represented; distinct from actor in direct-representation mode. |
| purpose | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"}` | Exact intended use; participates in both scope checks and definition purposes. |
| audience | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Exact intended executor/host audience; unknown or mismatched audience denies. |
| expiresAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Exclusive deadline for a first effect while pending; does not expire committed receipts. |
| compensatesReceiptId | `{"anyOf":[{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"},{"type":"null"}]}` | Optional retained prior receipt to compensate; context and revision guards apply. |

## submission Event

Master/writer: Serialized host issuer; observation claim belongs to identified observer. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| eventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Immutable native occurrence/evidence identity, not the logical request ID. |
| sequence | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Contiguous host event order beginning at 1. |
| controlSequence | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Serialized host transaction order covering policy/retirement/tries at equal clock seconds. |
| kind | `{"enum":["submission"]}` | Exact event-profile discriminator. |
| requestId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Host-minted immutable request identity; deliberately outside the client intent bytes. |
| recordedAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Trusted local capture time, integer UTC epoch seconds; native encoding uses RFC3339. |
| issuerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Host that asserts/captures the event or supplies standing evidence; distinct from request actor. |
| payload | `{"type":"closed object","children":"expanded below"}` | Closed kind-specific semantic payload. |
| payload.intentDigest | `{"type":"string","pattern":"^[a-f0-9]{64}$"}` | SHA-256 under the bounded Python encoding of the complete immutable intent. |

## delivery Event

Master/writer: Serialized host issuer; observation claim belongs to identified observer. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| eventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Immutable native occurrence/evidence identity, not the logical request ID. |
| sequence | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Contiguous host event order beginning at 1. |
| controlSequence | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Serialized host transaction order covering policy/retirement/tries at equal clock seconds. |
| kind | `{"enum":["delivery"]}` | Exact event-profile discriminator. |
| requestId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Host-minted immutable request identity; deliberately outside the client intent bytes. |
| recordedAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Trusted local capture time, integer UTC epoch seconds; native encoding uses RFC3339. |
| issuerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Host that asserts/captures the event or supplies standing evidence; distinct from request actor. |
| payload | `{"type":"closed object","children":"expanded below"}` | Closed kind-specific semantic payload. |
| payload.intentDigest | `{"type":"string","pattern":"^[a-f0-9]{64}$"}` | SHA-256 under the bounded Python encoding of the complete immutable intent. |

## try Event

Master/writer: Serialized host issuer; observation claim belongs to identified observer. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| eventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Immutable native occurrence/evidence identity, not the logical request ID. |
| sequence | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Contiguous host event order beginning at 1. |
| controlSequence | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Serialized host transaction order covering policy/retirement/tries at equal clock seconds. |
| kind | `{"enum":["try"]}` | Exact event-profile discriminator. |
| requestId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Host-minted immutable request identity; deliberately outside the client intent bytes. |
| recordedAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Trusted local capture time, integer UTC epoch seconds; native encoding uses RFC3339. |
| issuerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Host that asserts/captures the event or supplies standing evidence; distinct from request actor. |
| payload | `{"type":"closed object","children":"expanded below"}` | Closed kind-specific semantic payload. |
| payload.decision | `{"type":"closed object","children":"expanded below"}` | Fresh host scope evaluation retained outside immutable request identity. |
| payload.decision.action | `{"enum":["execute","cancel","observe"]}` | Operation being evaluated: execute, cancel or observe. |
| payload.decision.policyRevision | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Exact current-at-control-sequence host policy snapshot used in the decision. |
| payload.decision.allowed | `{"type":"boolean"}` | Computed scope result, additionally requiring definition availability for execute. |
| payload.decision.matchedRuleDigests | `{"type":"array","items":{"type":"string","pattern":"^[a-f0-9]{64}$"},"minItems":0,"maxItems":128,"uniqueItems":true}` | Exact matching complete rule digests; one rule must contain both scopes. |
| payload.decision.definitionAvailable | `{"type":"boolean"}` | Host-computed definition validity/retirement status at this try. |

## receipt Event

Master/writer: Serialized host issuer; observation claim belongs to identified observer. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| eventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Immutable native occurrence/evidence identity, not the logical request ID. |
| sequence | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Contiguous host event order beginning at 1. |
| controlSequence | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Serialized host transaction order covering policy/retirement/tries at equal clock seconds. |
| kind | `{"enum":["receipt"]}` | Exact event-profile discriminator. |
| requestId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Host-minted immutable request identity; deliberately outside the client intent bytes. |
| recordedAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Trusted local capture time, integer UTC epoch seconds; native encoding uses RFC3339. |
| issuerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Host that asserts/captures the event or supplies standing evidence; distinct from request actor. |
| payload | `{"type":"closed object","children":"expanded below"}` | Closed kind-specific semantic payload. |
| payload.definition | `{"type":"closed object","children":"expanded below"}` | Exact definition identity/version/content hash used for this intent. |
| payload.definition.definitionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Stable governed identity of the operation, independent of its revision. |
| payload.definition.version | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"}` | Immutable semantic definition revision; same ID/version cannot change bytes. |
| payload.definition.sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}$"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |
| payload.resourceId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Existing synthetic target resource identity; no URL or executable command. |
| payload.beforeRevision | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Resource revision consumed by the effect. |
| payload.afterRevision | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Resource revision produced; exactly beforeRevision+1. |
| payload.beforeLabels | `{"type":"array","items":{"type":"string","maxLength":200},"minItems":0,"maxItems":32}` | Exact retained target list before the effect. |
| payload.afterLabels | `{"type":"array","items":{"type":"string","maxLength":200},"minItems":0,"maxItems":32}` | Exact target list after the effect, equal to request parameters. |
| payload.compensatesReceiptId | `{"anyOf":[{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"},{"type":"null"}]}` | Optional retained prior receipt to compensate; context and revision guards apply. |
| payload.tryEventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Causal same-request/same-transaction Try Event; cannot be reused for another downstream result. |

## disposition Event

Master/writer: Serialized host issuer; observation claim belongs to identified observer. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| eventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Immutable native occurrence/evidence identity, not the logical request ID. |
| sequence | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Contiguous host event order beginning at 1. |
| controlSequence | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Serialized host transaction order covering policy/retirement/tries at equal clock seconds. |
| kind | `{"enum":["disposition"]}` | Exact event-profile discriminator. |
| requestId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Host-minted immutable request identity; deliberately outside the client intent bytes. |
| recordedAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Trusted local capture time, integer UTC epoch seconds; native encoding uses RFC3339. |
| issuerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Host that asserts/captures the event or supplies standing evidence; distinct from request actor. |
| payload | `{"type":"closed object","children":"expanded below"}` | Closed kind-specific semantic payload. |
| payload.from | `{"enum":["pending"]}` | Disposition source must be pending. |
| payload.to | `{"enum":["cancelled","expired","rejected-precondition"]}` | Terminal target: cancelled, expired or rejected-precondition; never committed through this profile. |
| payload.reason | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"}` | Guard reason token for a disposition, or explanatory observation/correction text. |
| payload.tryEventId | `{"anyOf":[{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"},{"type":"null"}]}` | Causal same-request/same-transaction Try Event; cannot be reused for another downstream result. |

## observation Event

Master/writer: Serialized host issuer; observation claim belongs to identified observer. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| eventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Immutable native occurrence/evidence identity, not the logical request ID. |
| sequence | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Contiguous host event order beginning at 1. |
| controlSequence | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Serialized host transaction order covering policy/retirement/tries at equal clock seconds. |
| kind | `{"enum":["observation"]}` | Exact event-profile discriminator. |
| requestId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Host-minted immutable request identity; deliberately outside the client intent bytes. |
| recordedAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Trusted local capture time, integer UTC epoch seconds; native encoding uses RFC3339. |
| issuerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Host that asserts/captures the event or supplies standing evidence; distinct from request actor. |
| payload | `{"type":"closed object","children":"expanded below"}` | Closed kind-specific semantic payload. |
| payload.observerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Authenticated actor whose knowledge is claimed; correction preserves the observer. |
| payload.claim | `{"enum":["caller-unknown","caller-observed-success","caller-observed-failure"]}` | Caller knowledge only; cannot alter authoritative execution state. |
| payload.reason | `{"type":"string","minLength":1,"maxLength":2048}` | Guard reason token for a disposition, or explanatory observation/correction text. |
| payload.correctsEventId | `{"anyOf":[{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"},{"type":"null"}]}` | Optional earlier same-observer/request observation, with at most one direct correction. |
| payload.tryEventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Causal same-request/same-transaction Try Event; cannot be reused for another downstream result. |

## key-retirement Event

Master/writer: Serialized host issuer; observation claim belongs to identified observer. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| eventId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Immutable native occurrence/evidence identity, not the logical request ID. |
| sequence | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Contiguous host event order beginning at 1. |
| controlSequence | `{"type":"integer","minimum":0,"maximum":9007199254740991}` | Serialized host transaction order covering policy/retirement/tries at equal clock seconds. |
| kind | `{"enum":["key-retirement"]}` | Exact event-profile discriminator. |
| requestId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Host-minted immutable request identity; deliberately outside the client intent bytes. |
| recordedAt | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Trusted local capture time, integer UTC epoch seconds; native encoding uses RFC3339. |
| issuerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Host that asserts/captures the event or supplies standing evidence; distinct from request actor. |
| payload | `{"type":"closed object","children":"expanded below"}` | Closed kind-specific semantic payload. |
| payload.retained | `{"enum":[true]}` | True marker preserving the key and complete evidence; not an erasure statement. |

## Pin (supporting value, not separate model)

Master/writer: Trusted host context builder. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| uri | `{"type":"string","pattern":"^(urn:\|https://)[!-~]+$","maxLength":512}` | Opaque exact urn/https evidence reference; not fetched, resolved or normalized here. |
| revision | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"}` | Opaque exact evidence revision; or a host sequence in auxiliary storage. |
| sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}$"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |

## DefinitionRef (supporting value, not separate model)

Master/writer: Trusted host context builder. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| definitionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Stable governed identity of the operation, independent of its revision. |
| version | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"}` | Immutable semantic definition revision; same ID/version cannot change bytes. |
| sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}$"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |

## Scope (supporting value, not separate model)

Master/writer: Trusted host context builder. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| dimensionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Owning Dimension namespace; exact match against trusted store required. |
| definition | `{"type":"closed object","children":"expanded below"}` | Exact definition identity/version/content hash used for this intent. |
| definition.definitionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Stable governed identity of the operation, independent of its revision. |
| definition.version | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"}` | Immutable semantic definition revision; same ID/version cannot change bytes. |
| definition.sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}$"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |
| resourceId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Existing synthetic target resource identity; no URL or executable command. |
| purpose | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"}` | Exact intended use; participates in both scope checks and definition purposes. |
| audience | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Exact intended executor/host audience; unknown or mismatched audience denies. |
| actions | `{"type":"array","items":{"enum":["submit","execute","read","cancel","observe"]},"minItems":0,"maxItems":5,"uniqueItems":true}` | Exact operation memberships inside one scope; not inherited from a role. |
| validFrom | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Inclusive beginning of definition/scope validity, integer UTC epoch seconds. |
| validUntil | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Exclusive end of definition/scope validity, integer UTC epoch seconds. |

## Rule (supporting value, not separate model)

Master/writer: Trusted host context builder. Every read/export requires the relevant host disclosure policy. Retain immutable versions/occurrences; no silent field overwrite.

| Field | Shape and cardinality | Meaning |
|---|---|---|
| actorId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Executor identity that must match the separately authenticated host actor. |
| principalId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Party represented; distinct from actor in direct-representation mode. |
| mode | `{"enum":["self","direct-representation"]}` | Self requires actor==principal; direct-representation requires distinct actor/principal and forbids further delegation. |
| issuerId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Host that asserts/captures the event or supplies standing evidence; distinct from request actor. |
| issuerStanding | `{"type":"closed object","children":"expanded below"}` | Host-verified reference evidence that the issuer may supply this authority basis. |
| issuerStanding.uri | `{"type":"string","pattern":"^(urn:\|https://)[!-~]+$","maxLength":512}` | Opaque exact urn/https evidence reference; not fetched, resolved or normalized here. |
| issuerStanding.revision | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"}` | Opaque exact evidence revision; or a host sequence in auxiliary storage. |
| issuerStanding.sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}$"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |
| basis | `{"type":"closed object","children":"expanded below"}` | External host-owned mandate/control basis Pin; not a new canonical mandate record. |
| basis.uri | `{"type":"string","pattern":"^(urn:\|https://)[!-~]+$","maxLength":512}` | Opaque exact urn/https evidence reference; not fetched, resolved or normalized here. |
| basis.revision | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"}` | Opaque exact evidence revision; or a host sequence in auxiliary storage. |
| basis.sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}$"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |
| principalScope | `{"type":"closed object","children":"expanded below"}` | Complete scope held by the principal and verified by the host. |
| principalScope.dimensionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Owning Dimension namespace; exact match against trusted store required. |
| principalScope.definition | `{"type":"closed object","children":"expanded below"}` | Exact definition identity/version/content hash used for this intent. |
| principalScope.definition.definitionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Stable governed identity of the operation, independent of its revision. |
| principalScope.definition.version | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"}` | Immutable semantic definition revision; same ID/version cannot change bytes. |
| principalScope.definition.sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}$"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |
| principalScope.resourceId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Existing synthetic target resource identity; no URL or executable command. |
| principalScope.purpose | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"}` | Exact intended use; participates in both scope checks and definition purposes. |
| principalScope.audience | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Exact intended executor/host audience; unknown or mismatched audience denies. |
| principalScope.actions | `{"type":"array","items":{"enum":["submit","execute","read","cancel","observe"]},"minItems":0,"maxItems":5,"uniqueItems":true}` | Exact operation memberships inside one scope; not inherited from a role. |
| principalScope.validFrom | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Inclusive beginning of definition/scope validity, integer UTC epoch seconds. |
| principalScope.validUntil | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Exclusive end of definition/scope validity, integer UTC epoch seconds. |
| delegateScope | `{"type":"closed object","children":"expanded below"}` | Complete scope permitted to this actor; must independently contain the request context. |
| delegateScope.dimensionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Owning Dimension namespace; exact match against trusted store required. |
| delegateScope.definition | `{"type":"closed object","children":"expanded below"}` | Exact definition identity/version/content hash used for this intent. |
| delegateScope.definition.definitionId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Stable governed identity of the operation, independent of its revision. |
| delegateScope.definition.version | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"}` | Immutable semantic definition revision; same ID/version cannot change bytes. |
| delegateScope.definition.sha256 | `{"type":"string","pattern":"^[a-f0-9]{64}$"}` | Upstream evidence byte hash in a Pin, or exact local definition-content digest in DefinitionRef. |
| delegateScope.resourceId | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Existing synthetic target resource identity; no URL or executable command. |
| delegateScope.purpose | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"}` | Exact intended use; participates in both scope checks and definition purposes. |
| delegateScope.audience | `{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$"}` | Exact intended executor/host audience; unknown or mismatched audience denies. |
| delegateScope.actions | `{"type":"array","items":{"enum":["submit","execute","read","cancel","observe"]},"minItems":0,"maxItems":5,"uniqueItems":true}` | Exact operation memberships inside one scope; not inherited from a role. |
| delegateScope.validFrom | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Inclusive beginning of definition/scope validity, integer UTC epoch seconds. |
| delegateScope.validUntil | `{"type":"integer","minimum":946684800,"maximum":4102444800}` | Exclusive end of definition/scope validity, integer UTC epoch seconds. |

Derived fields: requestId/keyHash/intentDigest/submissionEventId are minted/calculated at admission; state/receiptId/keyRetired are projections; all event IDs/sequences/times/decision/receipt fields are generated from the trusted host transaction. Intent fields and definition content are asserted inputs subject to validation. No physical units apply except UTC epoch-second time. Full guards, conflict rules and byte identity are in model-spec.md.
