# EM-TEC-01 local synthesis

## Disposition

- Narrow WM-SFT-001 to the Software Product master: durable identity, classification, delivery model, offering lineage, licensing, support/EOL, criticality and conformity context.
- Bind AISMM 3.1.0 as the product knowledge/context specification by ALIGN plus a product-instance REFERENCE. AISMM structures projections and traceability; it is never a second product master.
- Complete/reuse WM-SFT-007 for Component / Package, WM-SFT-008 for Build / Release / Artifact provenance and WM-SFT-009 for Deployment occurrence. Remove duplicate ownership of those facts from WM-SFT-001.
- Complete reserved WM-SFT-003 as the independent API / Interface contract after its missing specification is written.
- Add one identifier-unassigned **Source Repository** candidate because repository identity, ownership, branches, access and lifecycle exist independently of components, builds and products.
- Reference WM-SFT-012 as the SBOM document master. SBOM Reference remains a typed reference, not a model.

WM-SFT-001 owns what the software product is. AISMM owns how complete product knowledge is organised, classified, validated and traced. AISMM b2/b3/b6/b8/b9 records are projections or context records whose `derived_from` / `ingested_from` links resolve back to source masters. HR, incident and dataset facts remain in their own models; AISMM holds typed references and derived projections only.

Build is an execution using source revisions and a build definition. Release is a governed publishable state that selects build outputs. Artifact is immutable bytes identified by media type, role, digest and provenance. Deployment is a separate occurrence installing or activating a release in an environment. Artifact digest proves byte identity; a semantic fingerprint identifies canonical model meaning and cannot substitute for it.

## Delivery profiles

- SaaS: product and service-version lineage with optional/no distributable artifact; deployments reference runtime environments.
- Library: package coordinates and versions in WM-SFT-007; releases select registry artifacts.
- On-prem: release/artifact package plus customer-environment deployment and install evidence.
- Container: OCI digest-addressed component/artifact; mutable tags remain aliases.
- Firmware: product/component/release/deployment shape is plausible but OTA/fleet semantics remain unvalidated.

Regional deployments create new WM-SFT-009 occurrences, never new Software Product identities. One product references multiple repositories through explicit source bindings on components/builds; the product-to-repository set may be derived but repository facts remain repository-mastered.

## Invariants

1. Software Product identity is independent of region, deployment and artifact digest.
2. Release is not deployment; redeployment creates a new occurrence.
3. Build execution, release state and artifact bytes remain distinct.
4. Artifact digest is not a semantic fingerprint.
5. Each internal fact has one authoritative model owner.
6. SBOM is an authored document, not a dependency-fetch log.
7. Repository revision pins are immutable inputs to builds.
8. AISMM projections carry provenance and do not copy external HR, incident or dataset masters.
9. API/interface contracts have independent versions, providers and consumers.
10. Retired products, releases, components and deployments remain resolvable.

## AISMM version finding

The available AISMM repository at commit `fe40e61` declares 3.1.0 throughout its release notes and versioning documents. Its complete 206-file manifest was pinned. No 3.2.0 artifact or migration exists in the supplied repository, so the requested 3.2.0-versus-runtime-3.1.0 comparison is unevidenced and must remain a hold.

## Holds

WM-SFT-003 lacks a specification; Source Repository lacks registry allocation; ledger parent/reference edges conflict or are missing; WM-SFT-001 still duplicates child facts; all available WM-SFT publications are non-canonical, and WM-SFT-008/009 use provider waivers. SaaS no-artifact and firmware/OTA fixtures, AISMM version reconciliation, source pins and crosswalks remain incomplete. No runtime or installability claim is made.
