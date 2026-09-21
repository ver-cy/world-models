END OF REMEDIATION AUDIT INPUT is visible. `test_authority.py` is truncated in this bundle after `test_no_authority`; later test bodies are not readable here. The companion, schema, acceptance harness, fixtures, machine spec fields, and claimed result files are present.

# Focused remediation audit — Enterprise Fact Authority 0.1.0

Reviewer, not approver. No tools. Prior frozen reviews remain research, not authorization.

## Machine identity (Claude B1)

Resolved inside this bounded package.

- Runtime id is `vr.profile.enterprise-fact-authority` in `spec.json`, `runtime-model.reference.json`, and acceptance `PROFILE_ID`.
- Parent install is `native=False` → `binding=None`, `installationMode: semantic-only`.
- Companion install is a separate native binding; `objectType` is `vr.profile.enterprise-fact-authority:authority-register`, not a 001 ControlRecord class.
- Acceptance pins both roots: parent `sha256:a09261ca…` semantic-only; companion spec `sha256:cf027b56…` native-binding.
- `publicationStatus: published` on the candidate releases is harness metadata so the composer will accept reviewable-draft bytes. `researchAssurance` stays `reviewable-draft`. That split is stated. It is not a claim that a public WM catalog row already exists.

Hosting URLs still sit under `wm-xct-001-ownership-stewardship/profiles/…` (`canonicalUrl`, schema `$id`, acceptance `sourceUrl`). That is residual association optics, disclosed, not a parent-native binding.

## Envelope authority (Claude B2)

Resolved for this reference.

Acceptance writes snapshot facts with `authority.source = urn:synthetic:register-operator` and `masterSystem = urn:synthetic:governance-register`, and asserts the operator is not an accountable party or steward. Companion `evaluate` never reads those envelope fields; domain precedence remains nested `MastershipRule` logic. Storage authority is not fact authority.

## M1–M5

**M1 `validate_extension`.** Implemented. Same header; each collection’s previous rows must be an exact encoded prefix; appended receipts must be later than the prior global head. Acceptance rebuilds fixtures through installed `admit`, stores snapshot-r1/r2 with `supersedes` and `previousSnapshotDigest`, and rejects a stored truncation that drops an observation. Completeness of the *first* snapshot is still outside the function. Disclosed.

**M2 replay.** Same `(id,revision)` compares payloads with `recordedAt` removed, returns the original ledger (original receipt kept). Authorization still runs first. A changed body still raises `Conflicting replay`.

**M3 writer rotation.** Observation stable anchors are now `subject` and `source` only. `writer` is per-revision attribution. A currently granted writer for that source can admit a later revision. Original writer remains on the prior row. I cannot see the new unit-test body because the test file is truncated here; the code path matches the disposition.

**M4 host boundary.** `Denied` is a sibling `ValueError`, not a subclass of `Invalid`. `admit` is documented as trusted-host-only and is not a service. The library still *returns* the full ledger to its Python caller. Preventing that leak is a host obligation, not an implemented projection. Disclosed limit, not a silent fix.

**M5 change kinds.** `change` is required: `genesis | correction | closure | retraction`. Genesis cannot be retracted. Closure must shorten `validUntil`, keep start/party/value (and clip nested part ends), and may only restamp revision/receipt/evidence/issuer-or-writer. Correction may still rewrite the whole term. That is labeled, not hidden.

## Observation retention and part pins (L1–L3 / prior Grok medium)

Resolved in `evaluate`.

Matching observations, evidence, and `observationPins` (`id`, `revision`, bare `sha256`) are built *before* the unknown / authority-contested returns. No value is selected in those branches. After a single authority is chosen, `rulePins` and `routePins` cite `partId + authorityId + authorityRevision + authoritySha256`. Multi-authority contest leaves rule/route pins empty rather than inventing a winner. That is consistent.

**L2.** Part ids cannot equal `issuedBy`, `accountable`, steward parties, rule/grant sources, or grant writers in that authority snapshot. They also cannot collide with record ids.

## Other listed items

| Item | Status in this freeze |
|---|---|
| L4 explicit self-grant | No implicit writer from governor/accountable. A governor may appear in an explicit `WriteGrant`. No dual-control policy claimed. |
| L5 edge labels | `discovery-association-and-selected-patterns`, `read-contract-patterns-only-not-write-grant`, `assertion-pattern-alignment`. WriteGrant remains original. |
| L6 clocks | Plan/policy windows use current UTC; fixture evaluate clocks stay `2026-09-21T12:00:00Z`. |
| L7 digests | `inputDigest` now covers `format`/`version`/`dimension` plus the known slice. Record pins are bare hex; native asset descriptors keep the `sha256:` prefix. |
| L8 config | Still trusted host data. Generic-error duty is documentary. |
| Overlapping grants | Still storeable; live `admit` fails closed. Now explicit. |
| Observation interval beyond policy | Still allowed. Selection without authority is `unknown` **with** retained observation pins. |
| Fixture semantics | `startup` equal-priority A/B; `group` source b priority 10; `ai-team` same value, empty stewardships. Unchanged and coherent. |

Claimed execution: `test-results.json` 53/53; acceptance 3/3 with truncation rejected and native/companion split preserved. This review did not re-run them.

## Internal contradiction versus disclosed hole

No remaining machine contradiction on the B1/B2 identity split, envelope operator, observation retention, or part pins.

These are still **disclosed deferrals**, not defects in the bounded trusted-host contract:

- independent assignment revision streams and cross-authority part reuse
- signed publication / policy clock distinct from receipt
- recursive delegation, connectors, subject/scope proof
- durable concurrent multi-record transfer
- fine-grained disclosure (all-or-deny only; host must not return `admit` ledgers to write-only callers)
- legal/domain conformance and inherited WM-XCT-001/002/012 source holds
- public resolver acceptance of `vr.profile.enterprise-fact-authority` as a canonical WM row
- associated hosting URI under the 001 path
- full-term `correction` can still change who was accountable for the whole interval under current knowledge
- `validate_extension` cannot authenticate an incomplete root
- this audit bundle truncates `test_authority.py`, so successor-writer / closure unit tests are not independently readable here

---

## Verdict

**ACCEPT WITH LIMITS**

B1, B2, M1–M5, and the observation-retention / part-pin findings are implemented in the revised companion. Own model id, own spec digest, semantic-only parent, and a register-operator envelope are consistent with each other. Remaining holes are the explicit deferrals above, not an unstated subtype of WM-XCT-001 and not a collapse of source precedence into write grants.

Do not treat reviewable-draft + candidate `publicationStatus: published` as production publication, parent conformance, or an authenticated service.
