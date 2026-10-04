Independent study of EM-KRN-01. Evidence only: no catalogue ID, no publication authority, no certification. The smaller boundary is a shared contract over existing kernel files, not seven models and not an installable ELMM.

The full text is also saved as `EM-KRN-01-composition-installation-contract.md` (~3,800 words).

# EM-KRN-01 Independent Study

**Subject:** Domain-neutral Composition Resolution / Model Installation Contract  
**Researcher:** Grok (independent; output is evidence, not publication authority)  
**Read date:** 2026-09-21  
**Brief:** EM-KRN-01, status `queued`  
**Protocol:** Research Protocol v2.1, 21 September 2026  
**Form:** shared contract / facet over existing kernel artifacts  
**Assurance:** research-accepted boundary with specified fixtures; **not** publication-candidate; **not** installation-tested; **no** catalogue ID  
**Fictional ids only:** `dim.fictional.aurora`, `vr.example.stock-policy`, `vr.example.unit-of-measure`, `vr.example.case-review`

This study does not publish to ver.cy and does not certify legal, security, or operational fitness.

---

## 0. Boundary challenge

The prompt lists seven candidate concepts. Official `brief.json` lists two: `CompositionResolutionContract` and `KernelBoundaryDecision`. Protocol §1 says `candidate_types` is a working vocabulary, not seven meta-models.

**Reject** seven standalone kernel models. **Reject** ELMM as an installable Dimension package. **Reject** kernel imports of Employee, SoftwareProduct, or Contract.

**Accept** one shared contract, `CompositionResolutionContract` (alias: Model Installation Contract), that completes `vercy.lock`, `registries/meta-models.yaml`, `registries/model-requests.yaml`, `registries/model-links.yaml`, and `registries/events.yaml`.

**Accept** `KernelBoundaryDecision` as a durable Dimension-local governance record with `notInstallable: true` — an event/decision in `registries/`, never a meta-model id.

A smaller contract that existing validators can refuse is better than a universal composition kernel.

---

## 1. Object boundary and reuse / extend / new

### What the kernel already owns

Observed, `https://ver.cy/presets/kernel.yaml` 0.1.0-draft.1: kernel `selectable: false`; “Keep the kernel free of domain-specific facts”; required artifacts already include `AGENTS.md`, `dimension.yaml`, registries, policies, `vercy.lock`; required declarations already include installed model versions, URLs and digests.

Observed, `https://ver.cy/AGENTS.md`: `vercy.lock` pins versions and is **never** a writer mutex. Writers use `.vercy/write.lock` plus an expected object head. Draft / legacy / todo / digestless entries are never autonomous installs. Pending resolve results live in `registries/model-requests.yaml` as `vercy-pending-model/v1`. Storage is a binding, not identity.

Observed, `https://ver.cy/models/runtime-index.json` (`vercy: 0.2-draft`, generated 2026-09-21T14:14:59Z): auto-install = published + local AGENTS.md/spec.yaml + verified digest + resolved required closure. Required relation: `requires`. Optional: `parent`, `contains`, `aligned`. Index entries have **no** `runtimeSchema` field. 404 models, 200 published/installable. PLMM `0.1.0-legacy` is not installable. AISMM `3.1.0` is published and is a software meta-model, not a composition kernel.

### What ELMM is

Observed, `https://ver.cy/conformance/` plus `https://github.com/ver-cy/registry` README (v0.3.0 working draft, Apache-2.0): the GitHub repo is “the running instance” of the ELMM profile whose SoR is `ver-cy/elmm`. Kernel node `vercy.elmm` 0.1.0 has empty requires and no outgoing edges. Edge vocabulary: `composes`, `references`, `masters-link`, `deprecated-in-favor-of`. “One git registry with CI… zero long-running services.” Useful CI ideas (`ELMM-I7`/`I44` zero-change kernel, `I16` acyclic composes, `I17` unique ids, `I18` kernel isolation, `I19` referential integrity, `I11` export coverage) are **repository lessons**, not Dimension types. No ELMM row exists in `runtime-index.json`.

### Decision table

| Candidate | Form | Reason |
|---|---|---|
| CompositionResolutionContract | **shared contract** | One resolution episode; kernel-owned control plane |
| ModelReleaseReference | **nested value object** | OCI-like descriptor; identity = `(modelId, version, specDigest)` |
| DependencyEdge | **nested edge** | Package graph only |
| ResolutionRequest | **reuse** | Already `model-requests.yaml` + API ResolutionNeed |
| ResolutionPlan | **nested document** | Persist on apply/deny/stale-compare |
| RuntimeBinding | **split** from release | Published index has no binding; local overlay only |
| InstallationReceipt | **nested outcome + event** | Not a second lock |
| KernelBoundaryDecision | **governance record, notInstallable** | Brief candidate; must not look like kernel runtime authority |
| ELMM / Enterprise Landscape | **defer as runtime** | Repo/CI profile; landscape stays above kernel |
| Employee, SoftwareProduct, Contract | **refuse kernel import** | Brief negative case |

Predecessor KRN-01 fields `model_ref`, `semantic_fingerprint`, `resolution_policy`, `context_budget` are `candidate-not-normative`. Semantic fingerprint ≠ spec-bytes digest.

### Three graphs

1. **Package / spec dependency graph** — this contract. Mandatory `requires` must be a DAG of published digest-verified nodes.
2. **Object relationship graph** — Dimension `data/` facts and relations. Business cycles may be legal; they are not package cycles.
3. **Deployment / file graph** — `models/<slug>/<version>/…`. Location is a binding (`kernel.yaml`).

Cardinalities: Dimension 1—* contracts; contract 1—1 request, 1—0..1 plan, 1—* bindings, 1—0..1 receipt; modelId 1—0..1 current pin. Lifecycle: `requested → planned → applying → applied | applied-unchanged | refused | rolled-back → stale | superseded`. Receipts are append-only.

---

## 2. Questions, routes, profiles

| ID | Question | Artifact → action if unknown |
|---|---|---|
| Q13 brief | Which primitives already belong to the kernel? | `kernel.yaml` + control files → reuse, do not duplicate |
| Q14 brief | Is a separate ELMM needed, and with what authority? | runtime-index vs GitHub registry → defer as Dimension package |
| Q15 brief | How to reconcile contradictory public texts? | source ledger; prefer installer/validator bytes → record the contradiction |
| Q1 | Object vs record vs carrier? | §1 table → stop; do not mint a seventh model |
| Q2 | Identity after rename/move/owner change? | `(modelId, version, specDigest)` vs path → refuse path-as-identity |
| Q3 | Create / split / merge / succeed events? | receipt + `models-reconciled` / `model-pin-migrated` / `model-pin-refused` → no silent overwrite |
| Q4 | Direct vs computed vs asserted vs contested? | digest match computed; readiness asserted; two pins for one id contested |
| Q5 | Who owns meaning / who may write? | catalogue owns spec bytes; Dimension owner owns apply; kernel owns contract schema |
| Q6 | Master system per field? | index for published coordinates; lock for pin; local registry for runtime path |
| Q7 | Valid time vs knowledge time? | `receipt.validTime` vs `knowledgeTime=createdAt` |
| Q8 | States, guards, authority? | §4 machine → refuse unguarded apply |
| Q9 | Required links, deletion? | `requires` must resolve; pins are superseded, not deleted while facts use their paths |
| Q10 | Role / purpose / external visibility? | `install-published-compatible`; no instance data on resolve API |
| Q11 | Minimal vs extended? | profiles below |
| Q12 | Missing context route? | `unknown/insufficient-context`; pending `202`; never invent an empty runtime schema |
| Q16 | When is a package native-ready? | local runtime schema + optional companion validator → never infer from `status=published` |
| Q17 | Two families, no collision? | `namespaceScopes[]` + slug-collision refuse |
| Q18 | Same SemVer, different bytes? | digest identity → N1 |

**Minimal profile (startup, no HR/ERP):** one published model; success = `readiness=semantic-installed` + lock pin. V3 fact validation is not claimed.

**Extended profile (two families):** two closures, scoped namespaces, refuse path and slug collisions. Each family may stay semantic-only.

**Native-structured profile (AI org):** nested snapshot allowed as semantic pin. `native-bound` needs a real local runtime schema. `domain-validated` needs the companion validator. V3 still checks only top-level type and unit. Bypassing the companion is non-conforming (WM-ORG-017 `NATIVE-REFERENCE.md`, observed).

---

## 3. Fields and example

Five version axes must not be collapsed:

| Axis | Meaning | Example |
|---|---|---|
| Specification version | Immutable subject `spec.yaml` | `vr.example.stock-policy` `1.2.0` |
| Contract version | This shared schema | `0.1.0-research.1` |
| Object revision | This resolution record | `rev-3` |
| Release lifecycle | Research/publication stage of *this* contract | `research-accepted` |
| Research assurance | Review depth | `reviewable-draft; not-canonical` |

**Envelope:** `format=vercy-composition-resolution-contract`, `contractVersion`, `specificationVersion`, `objectRevision`, `releaseLifecycle`, `researchAssurance`, `dimensionId`, `contractId`, `previousContractId`, `createdAt`/`knowledgeTime`.

**Request:** `requestedModels[]`, `need?`, `actor`, `policySnapshot{autonomyEnabled, allowedActions[], allowedStatuses[], requireDigest, allowDowngrade, installationRoot}`, `indexOrigin`, `indexDigest`.

**Plan:** `algorithm`, `inputsHash`, `nodes[]`, `edges[]`, `cycleCheck`, `namespaceScopes[]`, `staleIf`.

**ModelReleaseReference:** `modelId`, `version`, `status`, `installable`, `specUrl`, `agentsUrl`, `specDigest`, `specSize`, `agentsDigest?`, `mediaType`, `issuer`, `requires[]`, `optionalRelations[]`, `unresolvedRequires[]`.

**DependencyEdge:** `from`, `to`, `relationType∈{requires,parent,contains,aligned}`, `optionality`, `cycleClass`.

**Binding:** `modelId`, `readiness∈{pending,semantic-installed,native-bound,domain-validated,refused}`, `runtimeSchemaPath?`, `runtimeSchemaDigest?`, `companionValidator?`, `factPaths[]`. Empty `factPaths` cannot upgrade readiness to native-bound.

**Receipt:** `outcome∈{applied,applied-unchanged,refused,rolled-back}`, `changed`, `refusedReasons[]`, `writtenPaths[]`, `previousPins[]`, `migrationRequired`, `writerLeaseId`, `eventId`, `validTime`.

```json
{
  "format": "vercy-composition-resolution-contract",
  "contractVersion": "0.1.0-research.1",
  "specificationVersion": "0.1.0-research.1",
  "objectRevision": "rev-1",
  "releaseLifecycle": "research-accepted",
  "researchAssurance": "reviewable-draft; not-canonical; not-installation-tested",
  "dimensionId": "dim.fictional.aurora",
  "contractId": "dim.fictional.aurora:crc:2026-09-21T14:32:11Z",
  "previousContractId": null,
  "createdAt": "2026-09-21T14:32:11Z",
  "knowledgeTime": "2026-09-21T14:32:11Z",
  "request": {
    "requestedModels": [{"key": "vr.example.stock-policy", "asOf": "2026-09-21T14:32:11Z"}],
    "need": null,
    "actor": "agent:vercy-skill",
    "policySnapshot": {
      "autonomyEnabled": true,
      "allowedActions": ["install-published-compatible"],
      "allowedStatuses": ["published"],
      "requireDigest": true,
      "allowDowngrade": false,
      "installationRoot": "models"
    },
    "indexOrigin": "https://ver.cy/models/runtime-index.json",
    "indexDigest": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  },
  "plan": {
    "algorithm": "runtime-index-requires-closure-v1",
    "inputsHash": "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
    "cycleCheck": {"ok": true, "path": []},
    "namespaceScopes": [{"prefix": "example.stock.", "ownerFamily": "example"}],
    "staleIf": {"indexDigestChanges": true, "policyChanges": true},
    "nodes": [
      {
        "modelId": "vr.example.stock-policy",
        "version": "1.2.0",
        "status": "published",
        "installable": true,
        "specUrl": "https://example.invalid/models/stock-policy/spec.yaml",
        "agentsUrl": "https://example.invalid/models/stock-policy/AGENTS.md",
        "specDigest": "sha256:cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc",
        "specSize": 4096,
        "agentsDigest": "sha256:dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
        "mediaType": "application/yaml",
        "issuer": "https://example.invalid/models/runtime-index.json",
        "requires": ["vr.example.unit-of-measure"],
        "optionalRelations": [{"type": "aligned", "target": "vr.example.quantity"}],
        "unresolvedRequires": []
      },
      {
        "modelId": "vr.example.unit-of-measure",
        "version": "1.0.1",
        "status": "published",
        "installable": true,
        "specUrl": "https://example.invalid/models/uom/spec.yaml",
        "agentsUrl": "https://example.invalid/models/uom/AGENTS.md",
        "specDigest": "sha256:eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
        "specSize": 1024,
        "agentsDigest": null,
        "mediaType": "application/yaml",
        "issuer": "https://example.invalid/models/runtime-index.json",
        "requires": [],
        "optionalRelations": [],
        "unresolvedRequires": []
      }
    ],
    "edges": [
      {
        "from": "vr.example.stock-policy",
        "to": "vr.example.unit-of-measure",
        "relationType": "requires",
        "optionality": "required",
        "cycleClass": "package-requires"
      }
    ]
  },
  "bindings": [
    {
      "modelId": "vr.example.stock-policy",
      "readiness": "semantic-installed",
      "runtimeSchemaPath": null,
      "runtimeSchemaDigest": null,
      "companionValidator": null,
      "factPaths": []
    },
    {
      "modelId": "vr.example.unit-of-measure",
      "readiness": "semantic-installed",
      "runtimeSchemaPath": null,
      "runtimeSchemaDigest": null,
      "companionValidator": null,
      "factPaths": []
    }
  ],
  "receipt": {
    "outcome": "applied",
    "changed": true,
    "refusedReasons": [],
    "writtenPaths": [
      "models/stock-policy/1.2.0/AGENTS.md",
      "models/stock-policy/1.2.0/spec.yaml",
      "models/unit-of-measure/1.0.1/AGENTS.md",
      "models/unit-of-measure/1.0.1/spec.yaml",
      "vercy.lock",
      "registries/meta-models.yaml",
      "registries/model-links.yaml",
      "registries/events.yaml"
    ],
    "previousPins": [],
    "migrationRequired": false,
    "writerLeaseId": "lease:dim.fictional.aurora:install:2026-09-21T14:32:11Z",
    "eventId": "dim.fictional.aurora:event:model-reconcile:2026-09-21T14:32:11Z",
    "validTime": "2026-09-21T14:32:11Z"
  }
}
```

A native-bound row adds a real local `runtimeSchemaPath` + digest + fact paths. It does not invent `{ "paths": {} }`.

---

## 4. State machine, mastership, facets

```
requested → planned → applying → applied | applied-unchanged | refused | rolled-back
applied* / refused → stale     (indexDigest or policy change)
applied → superseded           (explicit migrate; previousContractId set)
```

Always refuse: draft/legacy/todo/digestless node; HTTP(S) stored as a V3 local runtime reference; `requireDigest=false`; missing `install-published-compatible`; sanitized-slug collision; same `(modelId, version)` with different `specDigest`; downgrade unless `allowDowngrade`; pin by mutable alias; kernel field typed as Employee / SoftwareProduct / Contract; path traversal; concurrent install lease.

Install lease is `.vercy/install.lock` keyed on expected `vercy.lock` digest. Object writers keep `.vercy/write.lock` keyed on expected object head. Do not overload one mutex. `vercy.lock` remains not a mutex (AGENTS.md).

| Fact | Owner | Master | Writer | Valid / knowledge time | Conflict |
|---|---|---|---|---|---|
| Pin `(id,version,digest)` | Dimension owner | `vercy.lock` | installer + install lease | receipt.validTime / receipt clock | equal-authority disagreement stays visible |
| Local runtime path | Dimension owner | `meta-models.yaml` | installer only after a real binding | binding adoption | incompatible path contracts fail |
| Published spec bytes | Catalogue publisher | trusted index origin | nobody local | publisher release | different bytes ⇒ different release |
| Policy allow-list | Dimension owner | `policies/*` | owner, confirm level | declared validFrom | installer refuses, does not override |
| Pending 202 | resolve API | `model-requests.yaml` | resolver | acceptedAt | never treat as published |
| Instance facts | subject-model owner | declared master system | object writer + write.lock | fact.validFrom/To | contested set remains; provenance ≠ truth |

### Five-facet coverage (per type)

Protocol forbids one blanket “covered” row. Physical mass/geometry is not-applicable on abstract contracts.

**CompositionResolutionContract** — identity required (`contractId`, Dimension, revision); direct-properties required (request, plan hash, readiness, outcome); recognition optional (inputs hash); capabilities required (plan/apply/refuse/rollback; hazard = partial write or fake schema); context-evidence required (actor, origin, policy, eventId).

**ModelReleaseReference** — identity required `(modelId, version, specDigest)`; direct-properties required (URLs, size, mediaType); recognition required (digest verify); capabilities not-applicable; context-evidence required (issuer).

**DependencyEdge** — identity required (from, to, type); direct-properties required (optionality, cycleClass); recognition/capabilities not-applicable; context optional.

**RuntimeBinding** — identity required (modelId + schema digest); direct-properties required (paths, readiness); recognition required (schema validates against `runtime-model.schema.json`); capabilities delegated to companion validator when nested; context required (local path).

**InstallationReceipt** — identity required (`eventId`); direct-properties required (outcome, paths, reasons); capabilities not-applicable; context required.

**KernelBoundaryDecision** — identity required; direct-properties required (`decision`, `notInstallable`); capabilities not-applicable at runtime; context required. Not an installable type.

---

## 5. Invariants and fixtures

Specified, not executed in this session. JSON Schema cannot carry graph, policy, or digest predicates. They sit beside it.

### Positive

| ID | Case | Expect |
|---|---|---|
| P1 | Startup, one model, no HR/ERP | `semantic-installed`; no invented runtimeSchema; V3 failure on that row stays visible |
| P2 | Two families, scoped namespaces | two closures; no path or slug collision |
| P3 | Nested snapshot + companion | native-bound after real schema; domain-validated only after companion exit 0 |
| P4 | Repeated identical import | `applied-unchanged`, `changed=false`, same lock-head |
| P5 | Historical correction | new revision; `previousContractId` set; old receipt bytes unchanged |
| P6 | Offline verify | rehash local spec against lock digest; no network if `indexDigest` pinned |
| P7 | Explicit 1.2.0 → 1.3.0 | `migrationRequired=true`; both version dirs remain; event `model-pin-migrated` |

### Negative (≥10 nontrivial)

| ID | Fixture | Refuse code | Why nontrivial |
|---|---|---|---|
| N1 | Same version, changed spec bytes | same-version-changed-bytes | SemVer 2.0 rule 3 forbids mutation but cannot detect it |
| N2 | `{paths:{}}` claimed native-ready | empty-runtime-schema | Passes current V3 JSON Schema |
| N3 | `https://…` as local runtimeSchema | V2-MODEL-RUNTIME | Validator already rejects; successor must not write it |
| N4 | Fetched spec ≠ index digest | digest-mismatch | Current installer checks spec only |
| N5 | `status=legacy` or `unresolvedRequires` | not-autonomous-install | Real index rows look like this |
| N6 | Two ids sanitize to one slug | slug-collision | Public slugs `wm-liv-003`/`004` already share `world-p6-flora-and-vegetation` |
| N7 | Apply while install lease held | concurrent-install | Current script has no shared lock |
| N8 | Downgrade 2.0.0 → 1.4.0 | downgrade-denied | |
| N9 | Pin `@latest` | mutable-alias | Aliases are search keys |
| N10 | Kernel field typed Employee / SoftwareProduct / Contract | kernel-domain-import | Brief negative case |
| N11 | A requires B requires A | cyclic-required-dependency | Current `closure()` stops via a set but emits no cycle path |
| N12 | `requireDigest=false` or autonomy off | policy-denial | Script exit 4; keep fail-closed |
| N13 | Lock written, registry still thin, no receipt | partial-write | Four sequential `write_atomic` calls today |
| N14 | Reuse plan after `indexDigest` change | stale-plan | |
| N15 | `models/../../etc/passwd/1.0.0` | path-traversal | Sanitize is not enough; resolve-inside-root required |
| N16 | Profile 3 snapshot claimed domain-validated without companion | companion-skipped | WM-ORG-017 |
| N17 | `http://` origin off allowlist | untrusted-origin | Current `fetch()` allows `http` |
| N18 | Empty AGENTS.md, spec digest matches | empty-agents | Current script already refuses empty AGENTS |

Round-trip: write contract → apply → re-read lock/registry/receipt → compare `inputsHash` and `specDigest`. Drift is failure.

Explicit migration: semantic-installed → native-bound only by adding a local binding file and a new revision. In-place `spec.yaml` rewrite refused. Empty schema promotion refused (N2).

---

## 6. Semantic-only versus native-ready

Public `runtime-index.json` correctly lists 200 published/installable models **without** `runtimeSchema`. That catalogue listing must continue. The danger is Dimension-local `registries/meta-models.yaml` presenting the same packages as V3-complete by inventing `agents` / `specification` / `runtimeSchema` / `specificationDigest`.

Observed skew, raw scripts + `NATIVE-REFERENCE.md`:

- Installer writes `{id, name, version, status, location}`.
- Validator requires `{id, version, agents, specification, runtimeSchema, specificationDigest}` as local files.
- First four-package install failed V3. “Keep that failure visible; do not report every published package as runtime-ready.”

### Where records live

| Concern | Home |
|---|---|
| Pending 202 | `registries/model-requests.yaml` |
| Plan | contract document |
| Pin URL / version / spec digest / location / readiness | `vercy.lock` |
| Native six-field row | `meta-models.yaml` **only after a real local binding** |
| Package edges | `registries/model-links.yaml` |
| Outcome | events + receipt |
| Kernel boundary memo | governance record, `notInstallable: true` |
| Nested snapshot validity | companion validator, not V3 |

### Two successor designs that preserve V3 strength

**A (preferred).** Split lists: `semanticModels[]` (thin, honest) and `nativeModels[]` (six V1 fields). V3 walks only `nativeModels[]`.

**B.** Documented validator migration: a row may declare `readiness=semantic-installed` without the four local-file fields; any native claim still faces today’s hard checks. Record in `compatibility.yaml` (`migrationPolicy: explicit-only`). Silent relaxation refused.

Do not write empty runtime schemas.

Lock fields after successor: `id, version, status, specUrl, agentsUrl, specDigest, location, readiness, planInputsHash, indexDigest`. Optional `agentsDigest`, `runtimeSchemaDigest`, `contractId`. Readiness is a field, not inferred from `status=published` or `installable=true`.

Readiness evidence is scoped: semantic-installed = spec digest + non-empty AGENTS + in-Dimension location; native-bound = that plus valid local runtime schema, matching `modelId`, declared paths if facts will be written, no path collision; domain-validated = companion digest + exit 0 on that snapshot class. V3 remains type+unit only.

### Transaction

Today: `mkdtemp`+`os.replace` for model dirs; four JSON files written sequentially; rollback deletes created dirs only; no install lease.

Successor: acquire `.vercy/install.lock` with expected lock-head → fetch and digest all bytes before mutation → refuse slug collision and same-version-different-bytes → journal lock+registry+links+events+receipt → replace → release. Leftover `.vercy-stage-*` is garbage. Incomplete journal = `rolled-back`. Offline verify never needs the network when local bytes and `specDigest` exist.

---

## 7. Source ledger

Labels: **observed** = this author read the URL; **source-asserted**; **inference**; **proposal**; **unverified**.

| Source | Version / part | Status | Use |
|---|---|---|---|
| https://ver.cy/enterprise/models/em-krn-01/brief.json | EM-KRN-01 queued | observed, full JSON | two official candidates; ELMM not installable; negative case |
| https://ver.cy/enterprise/RESEARCH-PROTOCOL.md | v2.1, 21 Sep 2026, 113 lines | observed complete | working vocabulary; three graphs; 15 questions; five facets |
| https://ver.cy/AGENTS.md | 300 lines, read 2026-09-21 | observed complete | lock ≠ mutex; write.lock; no auto-install draft/legacy/todo |
| https://ver.cy/model-agent-protocol.md | 104 lines | observed complete | resolve API; digest closure; AGENTS first |
| https://ver.cy/models/runtime-index.json | 0.2-draft, 2026-09-21T14:14:59Z | observed structure+policy+many entries | no runtimeSchema field; 200 installable |
| https://ver.cy/skills/vercy/scripts/reconcile_models.py | Last-Modified 2026-09-05; 277 lines raw | observed complete | spec digest only; thin registry; four sequential writes |
| https://ver.cy/skills/vercy/scripts/validate_dimension.py | 268 lines raw | observed complete | six required fields; local files; type+unit |
| https://ver.cy/schemas/dimension/1.0/runtime-model.schema.json | 1.0.0, JSON Schema 2020-12 | observed complete | paths.valueTypes + units; additionalProperties false |
| https://ver.cy/models/wm-org-017-performance-objective-review/NATIVE-REFERENCE.md | binding 0.1.0, 19 lines | observed complete | keep V3 failure visible; companion validator |
| https://ver.cy/presets/kernel.yaml | 0.1.0-draft.1 | observed complete | no domain facts; pins are kernel declarations |
| https://ver.cy/object-description-profile.yaml | 1.0.0-draft | observed | five facets |
| https://ver.cy/schemas/dimension/1.0/compatibility.schema.json | 1.0.0 | observed | explicit-only / manual-only |
| https://ver.cy/conformance/ | undated | observed via page extract | ELMM-I* as CI gates |
| https://github.com/ver-cy/registry | README v0.3.0 WD, Apache-2.0 | observed 2026-09-21 | running ELMM instance; `vercy.elmm` 0.1.0; not a Dimension package |
| https://ver.cy/spec/docs/02-architecture/MMAS-Core.md | 2.0 Draft | partial | hierarchy; no installer; no ELMM |
| https://ver.cy/spec/docs/01-constitution/Meta-Universe-Constitution.md | 2.0 Draft Apache-2.0 | partial (head, Arts. 1–4) | identity stable; names may change |
| https://ver.cy/llms.txt | 2026-09-21 | observed | specs Apache-2.0 |
| https://ver.cy/models/composer-index.json | 1.0-draft | observed header+sample | pin specUrl+version+digest; no ELMM |
| JSON Schema 2020-12 Core | json-schema.org draft/2020-12 | observed | `$id` ≠ locator; `$ref` static; `$dynamicRef` instance scope. Spec repo license BSD-3-Clause OR AFL-3.0 — do not copy schema text |
| OCI descriptor / manifest / index | image-spec descriptor.md | observed sections | MUST `mediaType`, `digest`, `size`; tags mutable; digest is identity |
| W3C PROV-DM / PROV-O | REC 30 Apr 2013 | partial | Entity/Activity/Agent; no crypto integrity |
| npm / Cargo / go.sum / pip hashes | package-manager docs | observed | version + origin + hash; frozen apply analogue |
| SemVer 2.0.0 | spec rule 3 | observed via comparison sources | released contents MUST NOT change; SemVer ≠ byte identity |
| https://ver.cy/examples/reference-workshop/ | — | **inaccessible-detail** | page exists; lock bytes not extracted |
| https://ver.cy/api/openapi.yaml | 1.1.0 cited | **unverified here** | ResolutionNeed asserted by protocol text |
| github.com/ver-cy/elmm schema files | SoR per registry README | **unverified** | not imported |

### Comparison theses

1. **JSON Schema 2020-12** — accept as the syntax dialect already used. Accept finite preloaded `$ref` closure. Reject network `$ref` at install time. Reject `$dynamicRef` as a package resolver. Missing `$ref` = hard fail.
2. **OCI descriptors** — accept `{mediaType, digest, size, origin}` as ModelReleaseReference. Reject image layers/platforms in the kernel.
3. **Lockfiles** — accept exact version + content hash + origin + frozen apply. Reject SemVer ranges as pins. Reject mutable tags.
4. **PROV** — accept Activity=apply, Entity=pinned bytes/receipt, Agent=actor. Reject PROV as integrity. AGENTS.md: provenance does not decide truth.
5. **ELMM CI** — accept zero-change kernel, isolation, acyclicity as *ideas*. Reject importing node/edge schemas.

Digest detects bit-flip and same-version mutation. It does not prove publisher authenticity. Trusted origin = allowlist + TLS + digest. No installer signatures were observed.

Licensing: Vercy specs Apache-2.0. Do not copy JSON Schema, OCI, or PROV schema documents into a Vercy package. Write original fields.

---

## 8. Weaknesses and smallest implementation

Most dangerous:

1. Installer/validator schema skew — **demonstrated**.
2. Empty/permissive runtime schema as a V3 pass — current schema allows it.
3. Same-version different bytes plus silent lock overwrite of an existing `modelId`. Current event type is only `models-reconciled`.
4. Slug collision after sanitize — public index already shows the shape.
5. Partial four-file commit, no install lease, lock documented as not a mutex.
6. Digest without authenticity; `http` fetch allowed.
7. Treating ELMM CI as a Dimension kernel — recreates the brief’s negative case.
8. Stale plans and mutable aliases.
9. Cycle handling that terminates but does not explain.
10. Object writers and installer interleaving on registries.

None of this is a certification failure. Nothing here is certified.

**Smallest credible publishable unit** — not a new `vr.*` subject, not ELMM, not seven types:

1. Original JSON Schema 2020-12 for the §3 envelope (Apache-2.0).
2. Successor installer: keep `closure()` refuses; add cycle path, optional `agentsDigest`, `.vercy/install.lock`, slug-collision check, same-version-digest check, journaled control-file write.
3. Registry writer with split lists or an explicit readiness field plus a documented validator migration. No empty runtime schemas.
4. Fixtures P1–P7 and N1–N18 on `file:` origins.
5. KernelBoundaryDecision record: reuse kernel artifacts; extend lock/registry; defer ELMM; refuse domain imports; refuse seven-model split; `notInstallable: true`.
6. `compatibility.yaml` note for any validator change.

Call it implementation-validated only after the fixture runner is green on a synthetic Dimension. Publication-candidate still needs an assigned ID, immutable refs, licence scan, and catalogue read-back. This study has none of those.

**Demonstrated today:** kernel substrate; digest-pinned `requires` closure; V3 type+unit checks; semantic install ≠ native validation; ELMM as a git/CI profile.

**Not demonstrated:** V3-valid multi-model install from the generic reconciler; publisher signatures; cross-family isolation in the installer; multi-record native transactions; ELMM as an installable package; this contract installed anywhere.

HRIS, ERP, OCI registries, SPDX SBOMs, and organizational landscape graphs may *use* pins this contract records. They must not become imports of it.

---

## KernelBoundaryDecision

- **Subject:** kernel vs ELMM vs Enterprise Landscape vs installation contract  
- **Decision:** reuse kernel artifacts; extend with CompositionResolutionContract; persist this decision as a local governance record with `notInstallable: true`; defer ELMM as runtime; refuse domain-subject imports; refuse seven standalone models  
- **Effective from:** 2026-09-21  
- **Authority:** this study only  
- **Revisit when:** a catalogue ID is assigned; the validator gains an official semantic-only profile; or ELMM ships `spec.yaml` + digest + a published runtime-index row