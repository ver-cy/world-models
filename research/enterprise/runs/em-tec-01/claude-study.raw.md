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
