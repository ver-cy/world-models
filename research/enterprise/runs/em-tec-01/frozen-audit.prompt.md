You are the single frozen no-tools semantic auditor for EM-TEC-01. Use only the frozen material below. Audit revision 2 for Product/AISMM identity, fact mastership, Source Repository identity/lifecycle, immutable build inputs, build/release/artifact/SBOM/deployment separation, delivery profiles, version evidence, stable rules and concrete fixtures. Confirm no identifier and no publication readiness. Return PASS or REVISE first, then one closed numbered defect checklist. Do not invent identifiers or another provider study.

===== provider-comparison.md =====
# EM-TEC-01 provider comparison

Claude and Grok agree on the complete boundary: narrow WM-SFT-001 to durable Software Product identity/classification/offering/support; bind AISMM 3.1.0 as an aligned context specification; master component/package in WM-SFT-007, build/release/artifact in WM-SFT-008, deployment in WM-SFT-009 and SBOM documents in WM-SFT-012; defer interface ownership until WM-SFT-003 has a usable specification; and create one identifier-unassigned Source Repository candidate.

Both require removal of duplicated child facts from WM-SFT-001, exact immutable repository revisions for builds, separate artifact digest versus semantic fingerprint, one product with many repositories, and reference-only HR/incident/dataset facts. Both find AISMM 3.2.0 unevidenced and pin the available source to 3.1.0.

The reconciled profile treats WM-SFT-003 as a pending neighbour rather than a base, WM-SFT-012 as a referenced document master, and all five delivery profiles as unexercised acceptance fixtures. No identifier or publication readiness is claimed.


===== claude-study.raw.md =====
# EM-TEC-01 — Independent review

## Verdict

**Conditional accept with mandatory scope narrowing.** The contour is coherent and the five candidate models are the right nucleus, but as the dossier stands WM-SFT-001 is written as an aggregate that masters release, artifact integrity, build provenance, deployed instances, hosting environment and effective configuration — the same facts WM-SFT-008 and WM-SFT-009 claim. That duplication, not AISMM, is the contour's real defect. Recommendation: keep one `SoftwareProduct` (WM-SFT-001) demoted to **identity, classification, offering lineage, licensing, support and conformity host**, and move release/build/artifact to WM-SFT-008, deployment to WM-SFT-009, component/package to WM-SFT-007, interface contract to WM-SFT-003. AISMM is bound as a **context specification** (ALIGN plus REFERENCE), never as a second product master. Two candidate types in the contour — `SourceRepository` and `SBOMReference` — have no owner inside the target set; the contour cannot close without resolving both. The negative case is rejected on evidence. No canonical completeness and no installability is claimed here.

## Evidence

Directly usable: WM-SFT-001 (266,670 B, dual-provider, `publishableCanonical: false`), WM-SFT-007 (266,377 B, dual-provider), WM-SFT-008 and WM-SFT-009 (single-provider waiver dated 2026-08-29, Grok waived by repository owner), the frozen registry rows, the six-row relations ledger, legacy N4, and the AISMM repository manifest at `fe40e61` (206 files). Not usable: **WM-SFT-003** — reserved, `existing_spec_ref` empty, `"Reserved candidate has no current specification file."` Every interface finding below is therefore a placement, not a review. WM-SFT-012 (SBOM) and WM-SFT-010 (runtime environment) are referenced by the ledger but are outside the target set; WM-SFT-002 is named as parent of WM-SFT-009 with no registry row in this dossier.

## WM-SFT-001/AISMM relationship

They are not two products; they are **subject model and context specification** on different planes. WM-SFT-001 states facts about one software product (identity, releases, obligations, exposure). AISMM states *how a product's knowledge is structured, classified and trusted*: `kind_class` (normative/descriptive/projection), the `00-meta` / `00-policies` / `aismm` split, `aismm.registry.json` with `product_id` and `model_instance_id`, the derivation and owner-validation gate, and conformance L1–L5. Legacy N4 already encodes the correct edge — `imports: aismm (ALIGN): whole-model binding … so a full AISMM product model can stand behind any record here`. Carry that forward as **WM-SFT-001 → ALIGN → AISMM 3.1.0** (whole-model), plus **REFERENCE** from a product record to its AISMM `product_id`/`model_instance_id`. No AISMM layer becomes a fact owner in the world-model plane; AISMM layers that look like duplicates (b3.303 build/deploy artifacts, b3.304 SBOM, b8.804 release, b6.601 runtime topology) are `projection` records of facts mastered by WM-SFT-008/009/012/010.

## Identity/mastership

One fact owner per internal, as the contour requires:

| Fact | Owner | Note |
|---|---|---|
| Product identity | WM-SFT-001 | `product-identity-record`, `identifier-coordinates-and-crosswalk`, family/edition/channel/SKU |
| Architecture / engineering context | **no registered owner** | product-level classification and delivery model stay in WM-SFT-001; internal decomposition is an AISMM b2 projection; declare the gap |
| Component / package | WM-SFT-007 | `entry_kind: entity`, project- and release-level identity in one entity |
| Repository | **no registered owner** | see below |
| Build | WM-SFT-008 | `build-run-record`, `build-definition-and-parameters`, `build-platform-identity` |
| Release | WM-SFT-008 | `release-identity`, `release-state-model`, `supersession-and-withdrawal` |
| Artifact | WM-SFT-008 | `artifact-descriptor-set`, `artifact-variants-and-roles` |
| SBOM document | WM-SFT-012 (out of set) | WM-SFT-008 keeps `sbom-reference-binding` only |
| Deployment | WM-SFT-009 | `fnd-deployment-identity`, state machine, currency resolution |
| Interface contract | WM-SFT-003 | placement only; no spec exists |

Required edits to WM-SFT-001, all of which contradict single ownership today: `release-record`, `artifact-integrity-and-signature`, `build-provenance-attestation`, `bill-of-materials-document`, `dependency-graph-and-resolution`, `deployed-instance-record`, `hosting-environment-and-platform` and `effective-configuration-state` must become typed references to WM-SFT-008 / WM-SFT-012 / WM-SFT-009 / WM-SFT-010 rather than owned findings. WM-SFT-001's remaining aggregate justification (independently-lifecycled children anchored to one identity) survives on offering lineage, licensing, support/EOL, advisory exposure and conformity.

## Component/repository

WM-SFT-007 is the correct package master and the `WM-SFT-001 COMPOSE WM-SFT-007` row is the only product-to-internals edge in the frozen ledger. **Repository has no master.** WM-SFT-007 carries `f-source-linkage` (component → `de-vcs-url`, `de-source-revision`, verification status) and WM-SFT-008 carries `source-revision-binding` (build → one repository URI, revision digest, subpath, cardinality 1), and both explicitly push repository, branch and review process to an unregistered sibling. Consequence for the acceptance scenario: **one product with several repositories is representable, but only derivatively** — the product fans out to many components (COMPOSE) and many builds, each of which pins exactly one revision, so the multi-repository fact is a computed union, never a stored product→repository edge. That is defensible, but it means `SourceRepository` in `candidate_types` is unfulfilled and must either be registered as a sibling or struck from the contour.

## Build/release/artifact/SBOM

The four are distinguishable on the dossier's own elements, which is the contour's strongest result:

- **Build** = an execution: `build-invocation-id`, `build-started-on`/`build-finished-on`, `builder-id`, byproducts. WM-SFT-008's own adjudication defers whether a build run belongs inside the release aggregate at all, since a run may produce no release or feed several.
- **Release** = a publishable state: `release-identifier`, version designation with scheme and precedence, `release-state-code`, supersession, withdrawal, support period.
- **Artifact** = bytes: `artifact-descriptor-set`, `artifact-digest-set`, `artifact-authoritative-algorithm`, variants and roles.
- **SBOM** = an authored document about a release, owned by WM-SFT-012; WM-SFT-008's boundary note is explicit that SLSA `resolvedDependencies` is a best-effort fetch record and *not* an SBOM. `SBOMReference` in `candidate_types` is satisfied only as a reference element, not as a model in this set.

## Deployment boundary

WM-SFT-009 reifies release × environment as an occurrence with its own identity, state history and outcome, precisely because the same release may be deployed to the same target repeatedly. Its ledger edges (`REFERENCE WM-SFT-008`, `REFERENCE WM-SFT-010`) are right and it holds no release content beyond a pinned reference, artifact coordinate and binding digest. Two boundary defects to fix before adoption: (1) the CHILD edge to WM-SFT-002 and the OTA/fleet EXTEND accommodation exist in prose but not in the relations ledger, and WM-SFT-002 has no registry row here; (2) the model's own audit records that currency never terminates when a referenced environment is withdrawn, which blocks disposition. Also register `alternate_names` ("deployment occurrence", "deployment record") — the bare name collides with the Kubernetes controller object.

## Five delivery profiles

Run against the target set, with the outcome stated honestly:

1. **SaaS** — passes structurally, untested. WM-SFT-001's service boundary note degrades release and integrity to service-version records; its own publication hold demands this degradation be *exercised*, not asserted. WM-SFT-008 requires `artifact-descriptor` at 1..n, which a no-artifact offering cannot satisfy — an explicit SaaS profile is needed.
2. **Library** — passes. WM-SFT-007 covers purl coordinates, registry of record, yank/unpublish window, name-reuse and archive copy.
3. **On-prem** — passes with a seam to watch: WM-SFT-008 places SWID corpus (pre-install) on the release side and primary/patch tags on the deployment side; WM-SFT-009 references install evidence for correlation. Joint SWID review is already deferred in both.
4. **Container** — passes. WM-SFT-007 EXTENDs to OCI descriptor addressing (digest, not mutable tag); WM-SFT-008 carries `variant-index-ref` and OCI annotation projection — but its two OCI sources are pinned to a moving `main` branch.
5. **Firmware** — **weakest**. `component-type-code` admits firmware and `delivery-model-code` admits embedded, but WM-SFT-008 lists firmware/OTA as a declared omission likely needing a sibling model, and WM-SFT-009's fleet/OTA EXTEND is not in the ledger. Treat firmware as accommodated in principle, unvalidated in structure.

**Negative case rejected.** A regional deploy creates a WM-SFT-009 record with `de-placement-regions` against one unchanged product identity; `hosting-location` in WM-SFT-001 is an attribute of an instance, never a new `product-key`.

## AISMM version finding

The contour's question "What does AISMM 3.2.0 change relative to runtime 3.1.0?" **cannot be answered from this dossier and must be restated.** The repository at `fe40e61` is consistently 3.1.0: README badge `AISMM-v3.1.0`, `aismm-versioning-and-conformance.md` `spec_version: 3.1.0` with "Current version: AISMM 3.1.0", `RELEASE_NOTES_v3.1.0.md` dated 2026-06-27, and the latest migration `migration.aismm_v3_0_to_v3_1.external_model_binding.json`. No 3.2.0 artifact, release note or migration appears in the 206-file manifest. Reconciliation: record the repository version as **3.1.0**, mark 3.2.0 as an **unevidenced claim** in the contour, and re-scope the question to "what changes between the runtime-pinned AISMM version and the repository version, and is there a 3.2.0 line at all?" This is the same defect the blocking decision already names ("runtime and repository versions of AISMM/PLMM … compatibility is not proven"); note also that AISMM's own text renames AIPLMM to PLMM, so ELMM's role is documented but not demonstrated.

## Invariants

1. **Release ≠ deployment.** A release is publishable state (WM-SFT-008); a deployment is an occurrence of installing it (WM-SFT-009). N releases → M deployments; redeploying the same release to the same target yields a new record.
2. **Artifact digest ≠ semantic fingerprint.** `artifact-digest-set` hashes released bytes and answers "are these the same bytes". AISMM v3.1's adopted Meta-Universe Semantic Fingerprint (ARCH-009) hashes a canonicalized *shape* and answers "is this the same meaning". Neither substitutes for the other; an unchanged fingerprint across two differing digests is expected, not an error.
3. **One fact owner per internal**, per the table above — currently violated by WM-SFT-001 in eight findings.
4. **No HR, incident or dataset facts copied into AISMM.** WM-SFT-001 already puts organization records, dataset records and CVE records out of scope, keeping role edges and identifiers only; WM-SFT-007 keeps "only the role edge". Bind the same rule to AISMM: b11 holds ownership *edges*, not personnel master data; b6.603 holds incident *references*, not the incident record; b10 holds data contracts and model registry entries that reference, not restate, dataset masters. Any such AISMM record must carry `kind_class: projection`, a `derivation` block, and pass the owner-validation gate before it is trusted. A copied record is a defect, detectable as a projection with no `derived_from`/`ingested_from` edge.

## Minimal composition

```
WM-SFT-001 SoftwareProduct        (identity, offering, licensing, support, exposure)
  ├─ COMPOSE   → WM-SFT-007       (component / package)          [in ledger]
  ├─ REFERENCE → WM-SFT-008       (release / build / artifact)   [ledger row missing]
  ├─ REFERENCE → WM-SFT-003       (interface contract)           [no spec]
  └─ ALIGN     → AISMM 3.1.0      (whole-model context spec)     [from legacy N4]
WM-SFT-007 ─ REFERENCE → WM-SFT-012 (SBOM)                       [in ledger]
WM-SFT-008 ─ REFERENCE → WM-SFT-012, WM-SFT-015                  [in ledger]
WM-SFT-009 ─ REFERENCE → WM-SFT-008, WM-SFT-010                  [in ledger]
(unregistered) SourceRepository ← referenced by WM-SFT-007, WM-SFT-008
```

Registry parentage (`007 ⊂ 001`, `008 ⊂ 007`, `009 ⊂ 002`) is a record-plane statement and must not be published as a subject-plane contract without ledger rows. Note the inconsistency: WM-SFT-008's spec asserts CHILD to WM-SFT-007 while WM-SFT-009's asserts CHILD to WM-SFT-002 — two different parents for two siblings of the same release/deploy pair.

## Holds

1. **WM-SFT-003 blocks closure.** No specification exists; interface/API facts are placed, not decided.
2. **Single-provider waiver** on WM-SFT-008 and WM-SFT-009 (Grok waived 2026-08-29). Both remain reviewable drafts with no cross-provider corroboration; `add_functions` is contractually empty, so five missing WM-SFT-009 functions and four missing WM-SFT-008 functions are unaddressed.
3. **No target model is canonical.** All four available specs carry `publishableCanonical: false` and live source/version verification holds (SLSA v1.2 status, ECMA-427 edition, TUF pin, CDEvents and OCI citations pinned to moving `main`, paywalled ISO clauses read only as abstracts).
4. **Ledger gaps**: no `001→008` row; CHILD and EXTEND edges asserted in prose only; WM-SFT-002 unregistered; no repository model; WM-SFT-012 and WM-SFT-010 outside the target set.
5. **AISMM 3.2.0 is unevidenced** at `fe40e61`; the contour text must be corrected before the comparison question is answerable.
6. **Profiles are asserted, not exercised.** SaaS degradation and firmware/OTA in particular are untested against fixtures; the acceptance scenario's five-profile run has not been performed by this review.
7. **Semantic crosswalk, rights and source mastership** remain unconfirmed per the contour's own blocking decisions; `published` status on any WM-SFT record does not imply completed independent expertise.


===== grok-study.raw.md =====
# Grok independent study — EM-TEC-01

## Verdict
Accept the proposed boundary with holds. WM-SFT-001 is Software Product identity master; AISMM 3.1.0 is aligned product-knowledge/context, not a second product. Child facts move to specialised models. The card remains non-canonical and no identifier is minted.

## Product / AISMM
WM-SFT-001 owns master identifier, canonical name, namespace, producer, family/edition/channel/SKU, classification, stewardship and product-level support window, independent of release, package, repository or deployment. AISMM describes structured context for one product/system under product_id and model_instance_id. Bind by ALIGN/external binding. AISMM b3/b8 references build, SBOM and release masters; b6/b10/b11 reference operations, data and organization and never copy their facts.

## Fact mastership
Keep product identity/crosswalk, family/edition/SKU, classification/stewardship and support lifecycle on WM-SFT-001. Remove release/distribution, composition/supply-chain and deployment/operation child facts. WM-SFT-007 owns component/package, WM-SFT-008 build/release/artifact, WM-SFT-009 deployment occurrence, WM-SFT-003 interface contract once specified, WM-SFT-012 SBOM document, and one identifier-unassigned Source Repository candidate owns repository identity. AISMM repository fields are locators, not repository identity.

## Build / release / artifact / SBOM
WM-SFT-008 owns release identity, version, artifacts, build definitions/runs, exact source revision, attestations and publication state. Artifact digest is not AISMM semantic fingerprint. WM-SFT-012 owns versioned signable SBOM document, inventory, relationship graph, completeness and authenticity. WM-SFT-001 may cite release/SBOM existence but never restates manifest, component graph or attestation.

## Deployment
WM-SFT-009 owns deployment occurrence: pinned release, target scope, intent, state and evidence. It is distinct from deployable object, pipeline run and running instance. Regional or tenant deployment never creates a new Software Product.

## Delivery profiles
One product meaning covers SaaS, library, on-prem, container and firmware. Delivery model is classification, not identity fork. SaaS may have no distributable artifact and must use an explicit degradation profile. Libraries use package/release. On-prem, container and firmware share product identity while artifacts/deployments differ. One product may bind many Source Repositories. These profiles are acceptance scenarios and not yet exercised.

## Version finding
Only AISMM 3.1.0 is evidenced in the available repository and Vercy runtime. No 3.2.0 artifact, migration or release note is evidenced. Bind 3.1.0 and do not claim a 3.2.0 delta.

## Invariants
Release is not deployment. Artifact digest is not semantic fingerprint. Each internal fact has one owner. AISMM is not a second product. Regional deployment is not a new product. One product may bind many repositories. SBOM, product and component identities differ. Product support statement is not deployed observation. Interface contracts are not owned by WM-SFT-001. HR, incident and dataset facts are referenced, never copied.

## Blockers
WM-SFT-003 lacks a written specification. Source Repository is unassigned. WM-SFT-001 still embeds child bundles. Bases remain reviewable drafts with live-source/provider holds; SBOM CHILD versus REFERENCE wording is open. Delivery profiles are unexercised. AISMM 3.2.0 is unevidenced. Crosswalk and residual licence/quality seams remain open. No canonical completeness.


===== candidate-allocation-offline\allocation-candidate.json =====
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-TEC-01",
  "proposedName": "Source Repository",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NEW MODEL CANDIDATE",
  "canonicalPublishable": false,
  "candidateRevision": 2,
  "identityTest": {
    "stableIdentity": "A governed Source Repository remains identifiable across provider migration, namespace/locator change, default-branch change, product bindings, transfer and archival.",
    "versionIdentity": "Repository policy, ownership, namespace and access changes append effective revisions; source commits keep native immutable identity.",
    "independentLifecycle": [
      "proposed",
      "provisioned",
      "active",
      "read-only",
      "archived",
      "retired",
      "transferred"
    ],
    "mastership": "source-code management or engineering platform authority"
  },
  "boundary": {
    "owns": [
      "stable repository identity",
      "effective hosting locators and namespace",
      "ownership/stewardship lifecycle",
      "branch/tag alias namespace",
      "access-policy references and visibility",
      "transfer/archive/tombstone history"
    ],
    "references": [
      {
        "target": "WM-SFT-001",
        "purpose": "Software Products using the repository"
      },
      {
        "target": "WM-SFT-007",
        "purpose": "components/packages linked to paths and revisions"
      },
      {
        "target": "WM-SFT-008",
        "purpose": "build inputs pinned to immutable revisions"
      },
      {
        "target": "WM-SFT-009",
        "purpose": "deployment provenance through release/artifact lineage"
      },
      {
        "target": "WM-SFT-012",
        "purpose": "SBOM source provenance"
      }
    ],
    "excludes": [
      "product/component/package identity",
      "build/release/artifact lifecycle",
      "deployment/runtime state",
      "source bytes or secrets",
      "IAM grants and credentials",
      "SBOM document identity"
    ]
  },
  "objects": {
    "SourceRepository": {
      "identity": [
        "sourceRepositoryId"
      ],
      "required": [
        "ownerRef",
        "hostRef",
        "namespace",
        "status"
      ],
      "optional": [
        "defaultBranchRef",
        "visibilityClass",
        "successorRef",
        "retiredAt"
      ]
    },
    "RepositoryRevision": {
      "identity": [
        "sourceRepositoryId",
        "revisionId"
      ],
      "required": [
        "nativeRevision",
        "contentDigest",
        "committedAt",
        "provenanceRef"
      ],
      "optional": [
        "parentRevisionRefs",
        "signatureRef",
        "treeDigest"
      ]
    },
    "RepositoryLocator": {
      "identity": [
        "sourceRepositoryId",
        "effectiveFrom"
      ],
      "required": [
        "providerRef",
        "locator",
        "effectiveFrom"
      ],
      "optional": [
        "effectiveTo",
        "redirectRef"
      ]
    },
    "RepositoryReference": {
      "identity": [
        "sourceRepositoryId",
        "referenceName",
        "effectiveFrom"
      ],
      "required": [
        "referenceKind",
        "targetRevisionRef",
        "effectiveFrom"
      ],
      "optional": [
        "effectiveTo",
        "protected",
        "policyRef"
      ]
    }
  },
  "invariantRules": [
    {
      "id": "EM-TEC-01.SR-01",
      "text": "Source Repository identity is independent of hosting URL, provider, namespace locator, default branch and associated Software Product."
    },
    {
      "id": "EM-TEC-01.SR-02",
      "text": "A fork or independently governed mirror receives a distinct repository identity and records provenance to its source."
    },
    {
      "id": "EM-TEC-01.SR-03",
      "text": "Hosting migration changes effective locators without rewriting repository or native source-revision identity."
    },
    {
      "id": "EM-TEC-01.SR-04",
      "text": "Each immutable Repository Revision records native revision, content digest, commit time and provenance and is never replaced in place."
    },
    {
      "id": "EM-TEC-01.SR-05",
      "text": "Branch and tag references are mutable aliases and never satisfy reproducible build input without resolution to an immutable revision."
    },
    {
      "id": "EM-TEC-01.SR-06",
      "text": "Every build input pins Source Repository, immutable revision and subpath where applicable."
    },
    {
      "id": "EM-TEC-01.SR-07",
      "text": "One Software Product may reference many repositories and one repository may support many products without identity merging."
    },
    {
      "id": "EM-TEC-01.SR-08",
      "text": "Repository access policy grants no product, runtime, release or deployment authority by implication."
    },
    {
      "id": "EM-TEC-01.SR-09",
      "text": "Repository records and projections contain no credential, private key, token, secret or reversible secret representation."
    },
    {
      "id": "EM-TEC-01.SR-10",
      "text": "Repository transfer, archive, retirement and tombstone history preserve revision resolution and provenance."
    },
    {
      "id": "EM-TEC-01.SR-11",
      "text": "Repository ownership/stewardship changes are effective-dated and never mutate immutable revisions."
    },
    {
      "id": "EM-TEC-01.SR-12",
      "text": "Retired Source Repository identifiers remain resolvable and are never recycled."
    }
  ],
  "holds": [
    "No registry identifier is allocated or guessed.",
    "Repository-to-component and build-input relations are unapproved.",
    "Canonical base completion, rights controls, package conversion and live conformance remain pending."
  ],
  "publicationStatement": "Research candidate only; not canonically publishable, installable, allocated or verified."
}


===== candidate-allocation-offline\profile-candidate.json =====
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-TEC-01",
  "name": "Enterprise Software Product and Provenance",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "candidateRevision": 2,
  "canonicalPublishable": false,
  "bases": [
    "WM-SFT-001",
    "WM-SFT-007",
    "WM-SFT-008",
    "WM-SFT-009"
  ],
  "references": [
    "AISMM-3.1.0",
    "WM-SFT-012"
  ],
  "pendingNeighbours": [
    {
      "id": "WM-SFT-003",
      "reason": "reserved but no usable specification"
    }
  ],
  "constraintRules": [
    {
      "id": "EM-TEC-01.EP-01",
      "text": "WM-SFT-001 owns durable Software Product identity, classification, offering/licence context and support lifecycle only."
    },
    {
      "id": "EM-TEC-01.EP-02",
      "text": "Release/distribution, composition/supply-chain and deployment/operation child facts are removed from WM-SFT-001 and replaced by typed references."
    },
    {
      "id": "EM-TEC-01.EP-03",
      "text": "AISMM 3.1.0 is an ALIGN/external context binding keyed to product_id/model_instance_id and never a second Software Product master."
    },
    {
      "id": "EM-TEC-01.EP-04",
      "text": "AISMM projections cite owner facts and never copy HR, incident or dataset master records."
    },
    {
      "id": "EM-TEC-01.EP-05",
      "text": "WM-SFT-007 owns Component/Package; WM-SFT-008 owns Build/Release/Artifact; WM-SFT-009 owns Deployment occurrence."
    },
    {
      "id": "EM-TEC-01.EP-06",
      "text": "WM-SFT-003 is a pending Interface Contract neighbour and cannot be profiled or treated as complete until a usable specification exists."
    },
    {
      "id": "EM-TEC-01.EP-07",
      "text": "WM-SFT-012 remains SBOM document master and all product/release bindings are references; CHILD versus REFERENCE stays unresolved."
    },
    {
      "id": "EM-TEC-01.EP-08",
      "text": "Artifact digest identifies released bytes and never substitutes for AISMM semantic fingerprint."
    },
    {
      "id": "EM-TEC-01.EP-09",
      "text": "Regional/tenant deployment and repeated deployment never fork Software Product identity."
    },
    {
      "id": "EM-TEC-01.EP-10",
      "text": "SaaS, library, on-prem, container and firmware share product identity while delivery-specific artifacts/deployments remain external."
    },
    {
      "id": "EM-TEC-01.EP-11",
      "text": "SaaS without distributable artifact uses an explicit degradation profile and never fabricates a package."
    },
    {
      "id": "EM-TEC-01.EP-12",
      "text": "Available AISMM is pinned to 3.1.0 and no 3.2.0 delta is asserted without evidence."
    }
  ],
  "holds": [
    "All bases remain non-canonical reviewable drafts; WM-SFT-008/009 have provider waivers.",
    "WM-SFT-001 still embeds duplicated child bundles.",
    "WM-SFT-003 specification, ledger gaps and SBOM relation semantics remain open.",
    "Five delivery profiles and one-product-to-many-repositories are not yet exercised.",
    "AISMM 3.2.0 is unevidenced.",
    "No semantic crosswalk or canonical publication readiness is claimed."
  ],
  "publicationStatement": "Research candidate only; not canonically publishable, installable, allocated or verified."
}


===== candidate-allocation-offline\fixtures.json =====
{
  "format": "vercy-enterprise-allocation-fixtures/v1",
  "contourId": "EM-TEC-01",
  "companionArtifacts": [
    "allocation-candidate.json",
    "profile-candidate.json"
  ],
  "candidateName": "Source Repository",
  "candidateRevision": 2,
  "canonicalPublishable": false,
  "executable": false,
  "publicationStatement": "Research candidate only; not canonically publishable, installable, allocated or verified.",
  "cases": [
    {
      "id": "EM-TEC-01.FX-001",
      "kind": "negative",
      "input": "Repository moves from host A URL U1 to host B URL U2 and importer creates a new repository ID.",
      "expect": "Reject under EM-TEC-01.SR-01.",
      "rules": [
        "EM-TEC-01.SR-01"
      ]
    },
    {
      "id": "EM-TEC-01.FX-002",
      "kind": "negative",
      "input": "An independently governed fork reuses the source repository ID.",
      "expect": "Reject under EM-TEC-01.SR-02.",
      "rules": [
        "EM-TEC-01.SR-02"
      ]
    },
    {
      "id": "EM-TEC-01.FX-003",
      "kind": "negative",
      "input": "Hosting migration rewrites every historical commit identifier.",
      "expect": "Reject under EM-TEC-01.SR-03.",
      "rules": [
        "EM-TEC-01.SR-03"
      ]
    },
    {
      "id": "EM-TEC-01.FX-004",
      "kind": "negative",
      "input": "Revision R is replaced in place with different bytes.",
      "expect": "Reject under EM-TEC-01.SR-04.",
      "rules": [
        "EM-TEC-01.SR-04"
      ]
    },
    {
      "id": "EM-TEC-01.FX-005",
      "kind": "negative",
      "input": "Build B records only mutable branch main.",
      "expect": "Reject under EM-TEC-01.SR-05.",
      "rules": [
        "EM-TEC-01.SR-05"
      ]
    },
    {
      "id": "EM-TEC-01.FX-006",
      "kind": "negative",
      "input": "Build B omits repository revision and subpath.",
      "expect": "Reject under EM-TEC-01.SR-06.",
      "rules": [
        "EM-TEC-01.SR-06"
      ]
    },
    {
      "id": "EM-TEC-01.FX-007",
      "kind": "negative",
      "input": "Product P references repositories R1/R2 and system merges them; R1 also serves P2 and merges products.",
      "expect": "Reject under EM-TEC-01.SR-07.",
      "rules": [
        "EM-TEC-01.SR-07"
      ]
    },
    {
      "id": "EM-TEC-01.FX-008",
      "kind": "negative",
      "input": "Repository read permission is treated as deployment authority.",
      "expect": "Reject under EM-TEC-01.SR-08.",
      "rules": [
        "EM-TEC-01.SR-08"
      ]
    },
    {
      "id": "EM-TEC-01.FX-009",
      "kind": "negative",
      "input": "Repository projection stores API token and reversible encrypted key.",
      "expect": "Reject under EM-TEC-01.SR-09.",
      "rules": [
        "EM-TEC-01.SR-09"
      ]
    },
    {
      "id": "EM-TEC-01.FX-010",
      "kind": "negative",
      "input": "Archival deletes revision-resolution and provenance history.",
      "expect": "Reject under EM-TEC-01.SR-10.",
      "rules": [
        "EM-TEC-01.SR-10"
      ]
    },
    {
      "id": "EM-TEC-01.FX-011",
      "kind": "negative",
      "input": "Owner change mutates old commits.",
      "expect": "Reject under EM-TEC-01.SR-11.",
      "rules": [
        "EM-TEC-01.SR-11"
      ]
    },
    {
      "id": "EM-TEC-01.FX-012",
      "kind": "negative",
      "input": "Retired repository ID is assigned to another namespace.",
      "expect": "Reject under EM-TEC-01.SR-12.",
      "rules": [
        "EM-TEC-01.SR-12"
      ]
    },
    {
      "id": "EM-TEC-01.FX-013",
      "kind": "positive",
      "input": "Product P stores only identity/classification/support facts.",
      "expect": "Accept under EM-TEC-01.EP-01.",
      "rules": [
        "EM-TEC-01.EP-01"
      ]
    },
    {
      "id": "EM-TEC-01.FX-014",
      "kind": "positive",
      "input": "P references external component, release and deployment records.",
      "expect": "Accept under EM-TEC-01.EP-02.",
      "rules": [
        "EM-TEC-01.EP-02"
      ]
    },
    {
      "id": "EM-TEC-01.FX-015",
      "kind": "positive",
      "input": "AISMM 3.1 instance binds P by product_id and remains context only.",
      "expect": "Accept under EM-TEC-01.EP-03.",
      "rules": [
        "EM-TEC-01.EP-03"
      ]
    },
    {
      "id": "EM-TEC-01.FX-016",
      "kind": "positive",
      "input": "AISMM holds references to HR case, incident and dataset without copying payloads.",
      "expect": "Accept under EM-TEC-01.EP-04.",
      "rules": [
        "EM-TEC-01.EP-04"
      ]
    },
    {
      "id": "EM-TEC-01.FX-017",
      "kind": "positive",
      "input": "Package C, Release R and Deployment D remain separately mastered.",
      "expect": "Accept under EM-TEC-01.EP-05.",
      "rules": [
        "EM-TEC-01.EP-05"
      ]
    },
    {
      "id": "EM-TEC-01.FX-018",
      "kind": "positive",
      "input": "Interface facts are held pending WM-SFT-003 specification.",
      "expect": "Accept under EM-TEC-01.EP-06.",
      "rules": [
        "EM-TEC-01.EP-06"
      ]
    },
    {
      "id": "EM-TEC-01.FX-019",
      "kind": "positive",
      "input": "SBOM S remains WM-SFT-012 and P/R only cite S.",
      "expect": "Accept under EM-TEC-01.EP-07.",
      "rules": [
        "EM-TEC-01.EP-07"
      ]
    },
    {
      "id": "EM-TEC-01.FX-020",
      "kind": "positive",
      "input": "Artifact digest changes while semantic fingerprint remains stable.",
      "expect": "Accept under EM-TEC-01.EP-08.",
      "rules": [
        "EM-TEC-01.EP-08"
      ]
    },
    {
      "id": "EM-TEC-01.FX-021",
      "kind": "positive",
      "input": "Two tenant deploys reference the same Product P.",
      "expect": "Accept under EM-TEC-01.EP-09.",
      "rules": [
        "EM-TEC-01.EP-09"
      ]
    },
    {
      "id": "EM-TEC-01.FX-022",
      "kind": "positive",
      "input": "SaaS/library/on-prem/container/firmware profiles all reference P.",
      "expect": "Accept under EM-TEC-01.EP-10.",
      "rules": [
        "EM-TEC-01.EP-10"
      ]
    },
    {
      "id": "EM-TEC-01.FX-023",
      "kind": "positive",
      "input": "SaaS profile records no-artifact degradation.",
      "expect": "Accept under EM-TEC-01.EP-11.",
      "rules": [
        "EM-TEC-01.EP-11"
      ]
    },
    {
      "id": "EM-TEC-01.FX-024",
      "kind": "positive",
      "input": "Binding states AISMM 3.1 and rejects claimed 3.2 delta.",
      "expect": "Accept under EM-TEC-01.EP-12.",
      "rules": [
        "EM-TEC-01.EP-12"
      ]
    }
  ]
}
