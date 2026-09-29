# Independent review: EM-TEC-02 Software System and Business Application

Review of reserved WM-SFT-002 only. Existing identifiers used as named in the brief. No new codes. No claim of canonical completeness.

## Verdict

**Conditional accept; not complete.** Completing and renaming reserved WM-SFT-002 as the operator-side Software System and Business Application aggregate is the right mastership cut. Keep WM-SFT-001 as vendor Software Product, WM-SFT-009 as Deployment occurrence, and WM-SFT-010 as Runtime Environment. Licence/entitlement remains an identifier-unassigned commercial candidate and must never create an installation. Installation remains resolved from current deployment plus runtime environment, not a stored first-class key. The cut is valid only if the shared N4 spec, missing WM-SFT-010 spec, ledger gaps, and product/runtime overlap are closed.

## Identity and mastership

- WM-SFT-001 owns vendor Software Product as acquired deliverable; it must not own operator system, BusinessApplication, usage, deployment, runtime or licence.
- WM-SFT-002 owns logical system boundary, BusinessApplication, contained module placement, ApplicationUsage, and many-to-many product/application and application/installation mappings. It must not own vendor product, licence, deployment occurrence or runtime identity.
- WM-SFT-009 owns Deployment occurrence.
- WM-SFT-010 owns Runtime Environment, but its specification is missing.
- Licence/entitlement is an identifier-unassigned commercial candidate and owns none of installation, application, system or usage.

002 must not mint or reuse 001 identifiers. 001 must not master operator application, system, or usage. Dual mastership through a shared N4 type is a collision.

## Product / licence / system / runtime / deployment

Product is the vendor deliverable. Licence is a commercial event and never mints an application, system, deployment, runtime, usage or installation. System is the operator logical envelope and may contain several products and applications. Deployment is an occurrence, not an environment or standing installation. Runtime is the operator-controlled execution context; vendor-controlled SaaS tenancy is not by default an operator runtime. Installation exists only as the derived current deployment plus current runtime join; missing either side means no installation.

A product that provides a runtime class remains a product. The operator-controlled platform instance is runtime, not a second product. Vendor-hosted execution is neither operator runtime nor a product instance.

## Application and usage

BusinessApplication is the organisation's named capability-facing application, distinct from SKU, deployment, runtime and licence. ApplicationUsage is a stored organisational fact on WM-SFT-002 with actor or unit, purpose and validity period. It may exist with zero local deployments; usage is derived from neither licence nor installation. Product/application and application/installation mappings are many-to-many and never reuse product or runtime IDs as application IDs.

## Module and system-boundary tests

Contained module placement is operator composition on WM-SFT-002; vendor module packaging stays on WM-SFT-001. Promotion to BusinessApplication creates a distinct application identity, preserves placement history, and does not create product or deployment identity. A multi-product system has an accountable owner, enumerated contained set, system-level criticality and coordinated change surface; integration alone is only a dependency. Hosted use permits application and usage with no operator deployment/runtime join and forbids dummy installation.

## ERP scenario

One ERP product and a database product sit within one operator system. Finance, Procurement and HR are three applications. Two deployment/runtime pairs resolve to two installations. Finance maps to both installations, Procurement to one, and hosted HR to none. HR module promotion creates the third application without new product or deployment. Licence purchase precedes these facts but creates none of them. Product, system, applications, deployments, runtimes, derived installations, entitlement, usages and original placement remain distinct.

## Invariants

1. Installation exists only as current WM-SFT-009 × WM-SFT-010; missing either side means no installation.
2. Licence never creates installation, application, system or usage.
3. ApplicationUsage is stored on WM-SFT-002 independently of licence and installation.
4. Module placement differs from BusinessApplication until explicit promotion.
5. Promotion does not mint product or deployment and preserves placement history.
6. WM-SFT-002 never masters product; WM-SFT-001 never masters operator application, system or usage.
7. A BusinessApplication may have zero, one or many resolved installations.
8. A logical system may contain many products and many applications and is neither.
9. A product providing a runtime class is not the runtime; vendor execution is not operator runtime.
10. Hosted and installed uses may coexist without deleting other installation mappings.
11. No identifier reuse across classes.

## Blockers

The shared N4 spec must be partitioned into common and exclusive product/system/runtime shapes. WM-SFT-010 needs identity, cardinality, lifecycle and hosted-default rules before it can serve as the installation join key. The ledger must project ApplicationUsage, placement, promotion, membership and the negative commercial join. Product/runtime overlap requires an explicit catalogue-versus-operator-context rule with no shared identifier. Licence remains unallocated. Comparison tracks are unverified. The reserved cut is sound but must not be marked complete, canonical or installable.
