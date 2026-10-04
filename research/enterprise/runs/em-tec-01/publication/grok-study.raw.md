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
