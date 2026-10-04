# EM-TEC-03 — Interface, API and Integration

## Verdict
**Reuse/extend, with one gap.** Complete reserved **WM-SFT-003 API / Interface** as the versioned *logical* interface contract; do not mint `InterfaceContract` or `APIVersion` as new types — `APIVersion` is a revision designation of WM-SFT-003, not an entity. **EndpointBinding** stays *inside* WM-SFT-003 as a dependent, effective-dated link to **WM-SFT-018**; it gets no independent identity. **Integration** does **not** belong inside the contract: it needs its own identity, owner and lifecycle, and the dossier holds no reservation for it — the registry must issue one; I will not invent an id. **ExchangeEvent** is rejected as a type: an exchange occurrence is **WM-ACT-015** (undirected) or **WM-REC-003** (addressed, delivery obligation), carrying references to revision, binding and integration. **WM-DAT-004** keeps payload semantics/constraints; **WM-SFT-018** keeps logical connectivity/address/exposure. Boundary decision for the contour: reuse/extend, not new.

## Evidence
- Reservation `vr.wm-sft-003` states the purpose exactly as required — "a versioned machine or human interface contract with independent provider-consumer lifecycle" — and carries `validation_flags: KEEP-STANDALONE: API contract has independent version, owner and consumers`, `review_state: first-pass-reviewed`. `missing_specs` records only the absent spec file, not a rejected boundary.
- `prior_adjudication.EM-TEC-01`: "Complete WM-SFT-003 as the independent API / Interface contract after its missing specification is written." EM-TEC-02: keep logical system, product, runtime and deployment identities separate — the same separation applied here to contract vs binding.
- WM-DAT-004 boundary note (API/interface, OpenAPI/AsyncAPI): "Interface contracts own operations, transport, endpoints and status codes. This model owns payload structure and meaning. The overlap is the message payload schema, which should be defined once here and referenced by the interface model rather than duplicated." Its composition entry to the interface model is `ALIGN`, not merge.
- Binding precedent: WM-DAT-004 `af-binding-descriptor` identity = "contract identifier plus environment identifier from the infrastructure system of record" — a dependent key, not an independent one.
- Consumer-pin precedent: `de-consumer-registration` / `af-consumer-register` — "a consumer registered against a specific contract version, with role and effective period… used to drive impact assessment and notification".
- WM-REC-003 boundary note (event/activity): "An event becomes in-scope only when it is transported as an addressed message." WM-ACT-015 boundary note (CloudEvents): envelope `id/source/type/time` are "a projection of this model's identity, typing and event-time semantics, not additional semantics."
- Declaration vs measurement is already settled twice (WM-DAT-004 policy; its adjudication "Declaration versus measurement boundary… retained from base, reinforced by Grok").

## Identity/mastership
| Thing | Identity | Master (candidate) |
|---|---|---|
| Logical contract | WM-SFT-003 contract id | software catalogue / contract registry |
| Contract revision | contract id **+** version designation | Git / CI-CD |
| Consumer pin | consumer party **+** contract id **+** revision | contract registry |
| Integration | own id (**unreserved**) | service/integration register |
| Endpoint binding | contract id **+** revision **+** WM-SFT-018 endpoint **+** environment **+** period | CMDB / deployment |
| Exchange occurrence | WM-ACT-015 / WM-REC-003 identity rules | observability / message store |
| Data schema | WM-DAT-004 | data steward |
| Transport/address | WM-SFT-018 | service owner |
A version, a URL, a date or a fingerprint is never identity on its own.

## Contract/version/consumer pin
Contract = stable logical surface (owner, purpose, declared specification/dialect, status, compatibility mode, operation and error vocabulary, auth scheme *declared* only). Revision = immutable published designation under a declared scheme; a correction is a new revision, never an edit. Consumer pin = a consumer bound to **exactly one** revision with role and effective period; resolving a contract without a revision must return and state the revision resolved. Pins, not addresses, drive impact assessment, notice and sunset.

## Integration
A governed producer–consumer relationship: parties, purpose, `flow_direction`, `delivery_semantics`, `freshness_target`, owners, data scope (by reference to WM-DAT-004 — never a copied dataset). It composes contract revisions, consumer pins and endpoint bindings; it survives every revision and every address change. This is why it cannot live inside the contract: one contract has many consumers, and one integration may span several contracts and directions. Its identity is a registry gap, not a modelling choice.

## Endpoint binding
Dependent link: revision × WM-SFT-018 endpoint × environment × effective period, plus protocol and media type. Mastered outside the contract registry (CMDB/deployment), so it changes on its own cadence. No credentials or secrets are held here — referenced indirectly only. Multiple concurrent bindings per revision are normal (environments); a binding never re-versions the contract.

## Message/event/exchange
No new type. An exchange occurrence is: **WM-REC-003 Message** when addressed to identified recipients with delivery obligation, status and disposition evidence; otherwise **WM-ACT-015 Occurrence** (envelope attributes are a projection). EM-TEC-03 contributes only a correlation facet — inline references from the occurrence to `contract revision`, `endpoint binding`, `integration` and validating `schema` — plus `mapping_ref`, which belongs to WM-DAT-004 transform/projection, not here. Observed freshness, latency and delivery counts are measurement and belong to the observation sibling; the contract holds the declared target.

## Compatibility and migration
Inherit WM-DAT-004's evolution layer verbatim: declared mode recorded **on the revision** (backward / forward / full, transitive variants, none); backward ⇒ consumers upgrade first, forward ⇒ producers first; transitive checks the recorded version range. Breaking regardless of any syntactic pass: removing a required element or operation, narrowing a type outside the permitted promotion set, adding an element required on read without a default, changing the meaning of an existing element without renaming. Each candidate revision carries a compatibility check record or a recorded, expiring exception; each publication carries impact assessment against registered pins, a notice period, and on retirement a deprecation notice with sunset instant and successor.

## Invariants
1. An endpoint binding has exactly one environment and one effective period.
2. An address change alone never increments the contract revision.
3. A revision change alone never requires a new binding unless the revision is encoded in the address — then the binding change is a consequence, not a cause.
4. Integration identity is invariant under revision and binding change.
5. A consumer pin names exactly one revision; unpinned resolution must report the revision used.
6. Payload is defined once in WM-DAT-004 and referenced; the integration duplicates no dataset or schema.
7. A published revision is immutable.
8. No revision is published without an owner, a declared compatibility mode and a resolvable schema reference.
9. An exchange occurrence references revision, binding and integration; it never bears contract identity.
10. Syntactic compatibility pass is necessary, never sufficient.

## Scenarios
**Endpoint URL changes, contract unchanged.** New binding revision with effective period; prior binding deprecated with sunset. Contract revision, schema, pins and integration identity all unchanged; no compatibility check; notice scoped to consumers bound in that environment. The negative case — "a new URL is a new business integration" — is refused by invariants 2 and 4.

**Incompatible payload change, URL unchanged.** Major revision of the contract, with compatibility check record, impact assessment against pins, notice period, deprecation of the prior revision with successor reference; each consumer re-pins; schema change is mastered in WM-DAT-004 but the migration is driven by the contract revision. Binding unchanged. Different action set, different owner, different clock — the acceptance scenario holds.

## Minimal completion shape
WM-SFT-003 needs six areas: (1) contract identity and governance; (2) interface surface — operations/resources/channels, parameters, error vocabulary, declared auth, payload `REFERENCE` WM-DAT-004; (3) revision series and compatibility; (4) consumption — pins, obligations, declared service levels including `freshness_target`; (5) binding and exposure — `REFERENCE` WM-SFT-018 with environment and period; (6) exchange correlation — `REFERENCE` WM-ACT-015 / WM-REC-003, observation excluded. Relations: WM-SFT-003 `REFERENCE` WM-DAT-004; WM-SFT-003 `REFERENCE` WM-SFT-018; Integration `COMPOSE` WM-SFT-003 once its id exists.

## Holds
Not canonically complete and not installable. Outstanding: WM-SFT-003 and WM-SFT-018 have no specification files; Integration has no reserved registry id; operation-level compatibility rests only on WM-DAT-004's secondhand OpenAPI citation, so the interface-surface ladder is a gap; WM-DAT-004's own publication holds (ODCS repinning, `dataProduct` status) are inherited by anything referencing it; comparison tracks (ArchiMate, CSDM runtime instance, OpenTelemetry) are unexamined; all `candidate_properties_from_v1` remain candidate-not-normative; fixtures and immutable-ref checks have not been run; the contour's `boundary_decision` stays pending until the two specs exist.
