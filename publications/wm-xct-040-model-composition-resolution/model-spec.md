# Model Composition Resolution / Композиция моделей Измерения

Catalogue identity: WM-XCT-040, registry `vr.wm-xct-040`, version 0.1.0. A reusable contract aggregate above the existing Vercy kernel. It does not own organizations, people, products or their facts. Its subject is one reviewable resolution episode: which exact model releases may be assembled for one Dimension, under which local authority, with which readiness evidence.

## Boundary decision

Create one bounded contract pattern. Reuse the Dimension identity, owner, provenance, immutable record envelope and policies. A ResolutionPlan is the main document of this aggregate; release references, mandatory and optional edges, byte descriptors, compatibility decisions and binding references are owned values. RuntimeBinding retains an independent URI and version because one semantic release may have several representations. A staging receipt is an immutable execution artifact, not another authoritative model lock. KernelBoundaryDecision is a governance artifact, not an installable kernel. Existing asynchronous ResolutionRequest and its API UUID are reused; this contract starts after exact candidate selection.

The first executable profile is `exact-closure-v1`. It accepts a fixed set of release references and independently supplied trusted policy plus current lock bytes. It checks them offline and stages the minimal mandatory closure. It is not a package version range solver, ELMM Minimal Version Selection, online catalogue discovery, authenticity service or business-data writer. Exact versions are intentionally a small common denominator. Same name, newer SemVer or matching bytes never establish semantic equivalence.

The current Vercy 0.4 downloader/validator mismatch is preserved as evidence. This package supplies an additive route for NEW Dimensions: semantic-only packages go into `registries/semantic-models.yaml`; explicit native bindings go into `registries/meta-models.yaml` with all V1 fields. Both are pinned in `vercy.lock`, with different readiness. Existing Dimensions and published specifications are never rewritten by this adapter. The native validator is unchanged.

## Identity and cardinalities

| Type | Identity | Ownership and multiplicity |
|---|---|---|
| CompositionResolution / ResolutionPlan | Issuer-qualified planId; revision has a different planId and explicit supersedes | One Dimension, one purpose and actor, one supplied policy, one starting lock digest; one or more roots and releases |
| ModelReleaseReference | modelId + exact version, additionally pinned to specification bytes | One selected version per model ID in this profile; changing bytes at the same version is a conflict |
| DependencyEdge | Ordered source release, target release and edge kind within the plan | Zero or more requires and references; required target must exist exactly; optional references do not pull packages |
| ContentDescriptor | Asset path within the transport package plus SHA-256 and byte size | Exactly one agents and specification descriptor per release; paths are carriers, never model identities |
| RuntimeBinding | Issuer-qualified binding URI and version, exact target specification digest | Zero or one selected binding per release; more alternatives require a new selection plan |
| CompatibilityDecision | Evidence URI, reviewer and observation time scoped to a release | Exactly one accepted decision per selected release; unknown or rejected cannot be applied |
| AuthoritySnapshot | Policy reference and digest, actor, owner, purpose, effective policy interval | The external trusted policy is authoritative; the plan snapshot cannot authorize itself |
| InstallationReceipt | Installer-generated UUID plus exact plan digest | A committed staging artifact; repeated identical staging reuses it; runtime and nested validation results are separate |
| KernelBoundaryDecision | Governance record URI and source comparisons | Records reuse/defer choices; no package installation authority |

`schemaVersion=1.0.0` is the instance contract, model release `0.1.0` is the specification, `revision` is the plan revision, publication status is the release lifecycle, and research assurance describes review evidence. None substitutes for another. Model IDs are publisher-qualified registry identifiers. Object/plan/binding/policy/evidence identifiers are absolute URIs. Unknown fingerprints are null; missing authority or exact dependencies causes refusal. A digest verifies bytes and does not authenticate their publisher.

## Fields and semantics

The complete field types, nullability, enum values, cardinalities and additional-property rules are in `composition-plan.schema.json` and `policy.schema.json`. `field-catalog.json` adds semantic ownership and sensitivity per field. Required null values, including an absent semantic fingerprint or binding, mean explicitly unknown/not-selected, never a default successful result. Paths use the declared portable relative-path profile, not URLs or executable commands.

Roots and required references use exact `(modelId, version)`. `references` is an informational package relation; it is not an instance relationship. `namespace` is a selected export namespace, not a filesystem folder or a legal ownership claim. `semanticFingerprint` carries an algorithm identifier when supplied; this profile preserves it but does not calculate or certify semantic equivalence. Compatibility `scope` and evidence are mandatory; the verifier checks reviewer allowlisting, not the truth of the review assertion.

Binding `scope` states exactly which paths are implemented. A binding's `forSpecificationDigest` prevents attaching a schema to the wrong release. A native binding contains a nonempty Vercy runtime path contract. Structured values require both a closed JSON Schema 2020-12 schema and a companion semantic validator descriptor. Arbitrary network schema references, custom vocabularies and dynamic references are outside this first profile. Downloaded validator code is never executed by the composer. Native V3 validates envelopes and top-level types/units; the selected trusted companion must check nested and graph semantics separately. A bootstrap pass with zero records is a control-package test, not evidence that company data exists.

## State machine and effects

1. **Scoped**: owner or delegated curator defines purpose and roots. Missing model requests remain in the existing Vercy API workflow.
2. **Resolved candidate**: exact releases and descriptors are selected; all required edges are known. No write authority is inferred.
3. **Verified**: schema, graph, policy, time, lock precondition, compatibility assertions, paths and asset bytes pass. This is a computed result for one evaluation time.
4. **Refused**: any guard fails. Return a stable error category, keep source and target unchanged. A false assertion is not repaired by invention.
5. **Assets staged**: one new directory contains verified bytes, the frozen plan and receipt. A sibling creation lease excludes cooperating writers. An incomplete temporary directory is not a committed result. Crash leftovers require inspection; no blind lease stealing.
6. **Dimension bootstrapped**: the NEW-Dimension adapter creates owner controls, separate semantic/native registries and lock; runs unchanged V1-V3 validation before activation. No facts are invented. A final directory rename is the activation point on the tested local filesystem, not a distributed transaction or power-loss durability guarantee.
7. **Instance validated**: a separate evidence record names the exact data, runtime validator and companion validation scope. It does not retroactively change the staging receipt.
8. **Superseded**: a new plan identifies its predecessor. Applying changed versions, downgrades, changed bytes or migration of an existing Dimension is refused by this implementation. Historical validation can use an explicit evaluation time; historical time cannot authorize staging through either the CLI or the Python library.

The caller supplies owner policy from a trusted location. The adapter rechecks policy and lock bytes before activation. It does not install a trust policy from downloaded text, execute package hooks, call corporate systems, change user access controls or send instance data to the catalogue. Filename/case collisions and symbolic-link/junction traversal are rejected. Physical storage permissions and policy authentication are the adopting environment's responsibility.

## Invariants and evidence

The executable rule categories are SCHEMA, POLICY, POLICY-DIGEST, TIME, STALE, OWNER, AUTHORITY, DENIED, ASSURANCE, REVISION, VERSION, NAMESPACE, ROOT, LIFECYCLE, COMPATIBILITY, KERNEL, EDGE, READINESS, ORIGIN, COLLISION, PATH, ASSET, DIGEST, AGENTS, SPEC, BINDING, FACT-PATH, NESTED, DIALECT, SCHEMA-REF, CLOSURE, CYCLE, MINIMAL, LOCK, MIGRATION, TARGET, BUSY, STAGE and NEW-ONLY. Syntax is checked by a real JSON Schema 2020-12 implementation; graph and state rules are Python checks. These categories are not claims of security certification.

Key requirements: unique selected IDs and namespaces; one release version per ID; all plan-declared mandatory targets present; no mandatory cycles; no packages extraneous to the plan-declared closure; no domain imports from a kernel-role node; only published releases; explicit permission for research drafts; independent owner/actor/purpose checks; fresh policy and plan; unchanged starting lock; exact specification and AGENTS bytes; portable contained paths; binding-to-spec match; nonempty native paths; no duplicate path owners; mandatory nested schema/companion descriptor presence for structured snapshots; execution remains a separate step-7 obligation recorded in composition/plan.json; no implicit upgrade/downgrade; repeat staging unchanged; failure cannot replace an existing target under cooperating writers on the tested Windows filesystem.

## Mastership, time, conflicts and projections

The publisher masters specification and release metadata. The Dimension owner masters installation policy and selected pins. A domain or binding maintainer masters the meaning of runtime paths. The executing agent records observations and receipts but cannot grant itself access. `createdAt` and `provenance.recordedAt` are knowledge timestamps; plan and policy effective intervals gate execution. A historical correction uses a new plan revision, not a silent overwrite. Equal-authority conflicting proposals remain separate candidates; this profile refuses ambiguous selected versions instead of choosing the latest timestamp.

Public specifications and fictional acceptance fixtures may be disclosed. Real model selections can reveal technology or organizational structure and are private by default. A projection of a plan describes that one plan; a dashboard spanning installations is a context pack of separately permitted projections. The portable implementation records classifications and checks installation policy; it is not an IAM/read-side enforcement engine. A successful install grants no new right to read personnel or contract facts. Retention of receipts and invalidation history follows local policy; automated deletion and retrospective erasure are outside this package.

## Whole-object coverage

`whole-object-coverage.json` supplies a distinct row for every exported type. Identity, direct properties, observation, possible actions and provenance are assessed per type. No abstract plan, release or receipt acquires mass, geometry or legal personality. The runtime code is an implementation artifact of a contract, not evidence that the contract has acted. A receipt states observed outcome, while a plan describes a proposed operation.

## Three adoption profiles

**Startup**: use this contract with one Organization semantic specification. A minimal optional Organization identity binding contains the reviewed name fact only. No Employee, Employment, HRIS, ERP or legal-registration record is required merely to collaborate. Unknown legal form remains unknown.

**Group**: select Organization and Organizational Unit packages in separate export namespaces, using this contract. Package selection does not create a subsidiary, employment relationship or reporting line. Those remain explicitly authored instance records in their subject models. Test a valid multi-root closure and reject namespace and version collisions.

**AI organization**: select the published Performance Objective / Review model with its explicit reference binding and companion validator as a representative structured snapshot. The use case tests data structure and composition, not real employment decisions or productivity evaluation. Malformed nested context must fail its companion even when the outer native record passes V3.

## ELMM and neighbouring models

ELMM's repository proposal composes contexts using an MMDG profile, minimum-version selection and semantic fingerprints. Its kernel has no outgoing domain composition edges. Vercy's public installation index uses exact byte digests and presently does not offer ELMM as an installable model. Adopt the separation of domain ownership and composition; do not label this exact-closure profile as an implementation of ELMM, MVS, context budgeting or all ARCH/FED gates. Enterprise Landscape remains a separate domain-level composition. PLMM's legacy runtime status and AISMM's release/version differences require explicit future migration; the three acronyms are not interchangeable.

WM-XCT-037 Dependency / Impact overlaps typed edge description, but its public package carries unresolved boundary, identity and composition holds. It is not a dependency of this contract, and no claim of exact equivalence is made. WM-XCT-011 Identifier Scheme describes schemes; this contract uses existing qualified registry IDs rather than importing the scheme catalogue into the kernel. Crosswalk entries record pins, overlap, loss and chosen action.

## Migration, recovery and limits

New Dimensions can use the supplied bootstrap adapter. Existing installations must first retain a recoverable copy, inspect current pins and runtime bindings, and prepare a separate migration; the adapter intentionally refuses to update them. Semantic-only to native-bound is not a status toggle: bind the exact specification, provide runtime paths and additional validators, validate representative facts, then record a new receipt. Downgrades require a loss analysis and explicit data conversion; unsupported cases are refused.

A failed staging/bootstrap attempt removes only its task-created temporary directory and lease during normal exception handling. A process crash may leave a staging directory or lease: inspect recorded ownership and committed receipt before recovery. The implementation does not claim power-loss durability, adversarial multi-user filesystem isolation or distributed locking. No model is certified universally compatible, and source provenance alone never proves a factual assertion true.

Published artifacts include independent provider memos, the reconciliation and frozen review, full schemas, source comparisons, whole-object and field coverage, code, fixtures and actual results. Research assurance and publication lifecycle remain separate. Numeric test counts are taken from reports, not this document.

## Bounded file and schema profile

Specification bytes must be JSON or JSON with one leading `#` header line (the current Vercy JSON-compatible YAML projection). General YAML is refused. The three published package specifications used in acceptance were fetched from ver.cy and matched byte-for-byte. Only the commercial-company preset is supported by the new-Dimension adapter. JSON Schema closure checks require a closed root object and closed object-capable type nodes (including type lists) and properties-defined object nodes; patternProperties is refused; this static gate is not a proof that every possible composed schema is semantically complete. Publication status and compatibility remain supplied assertions checked against owner policy, not digitally authenticated publisher/reviewer statements.

A release must have publicationStatus=published. allowReviewableDrafts only admits the separate researchAssurance=reviewable-draft state of an already published release; it never permits an unpublished draft. Runtime bindings and semantic fingerprints are preserved with explicit scopes. No automatic execution of a companion follows from including its descriptor.

Closure and minimality are computed only over dependencies declared in the plan. Dependencies are plan assertions and are not extracted from specification bytes. Untyped nodes and boolean-true subschemas can remain open; the companion validator must enforce their domain semantics. The bounded static walk may conservatively reject valid schemas when annotation values resemble schema keywords. Python 3.12+ is required for the documented junction checks. Atomic activation claims apply to the tested Windows filesystem and cooperating writers; non-cooperating POSIX writers can race a directory rename. The examples are directly reproducible only until 2026-12-31; regenerate policy and plan afterwards.

Provenance of example artifacts: Organization, Organizational Unit and Performance semantic specs and agent guides are copies of published releases. The one-name Organization runtime binding is authored for this contract and published with it. The Performance runtime/schema/companion is copied from the already published reference binding, with its original limitations. Upstream verification names every fetched asset. Native bootstrap observations are stored in composition/bootstrap-observation.json, not presented as native event instances.
