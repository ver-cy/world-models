# EM-TEC-02 local synthesis

## Disposition

- Complete and rename reserved WM-SFT-002 as **Software System and Business Application**, the operator-side aggregate for logical systems and their organizational use.
- Keep WM-SFT-001 as the producer-side Software Product master, WM-SFT-009 as Deployment occurrence and WM-SFT-010 as Runtime / Compute Environment.
- Treat a purchased licence or entitlement as a separate commercial fact. No reservation is available in this dossier, so that candidate remains identifier-unassigned.
- Split the shared N4 legacy specification before advancement: WM-SFT-001 and WM-SFT-002 currently cite the same document and claim overlapping runtime facts.
- Do not allocate a new model or runtime identifier.

WM-SFT-002 owns an operator-governed logical boundary. A **SoftwareSystem** is a bounded assembly of product releases managed as one technical whole. A **BusinessApplication** is an organization-side unit of managed software capability with its own key, business purpose, accountable owner and criticality. One application may span several systems or installations, and one installation may support several applications. An **ApplicationUsage** binds an application to an organizational unit, process, site or user population for a validity window. An **ApplicationModule** remains scoped inside its product or system until explicit promotion to an independently governed application.

## Identity and mastership

| Layer | Identity and owner |
|---|---|
| Vendor product and release | WM-SFT-001; producer catalogue |
| Purchased licence / entitlement | Commercial record; identifier-unassigned candidate |
| Software system and business application | WM-SFT-002; operator software catalogue / CMDB |
| Runtime environment | WM-SFT-010; CMDB / platform inventory |
| Deployment occurrence | WM-SFT-009; CI/CD or deployment ledger |
| Installation | Resolved standing state from current deployment plus runtime environment |
| Application usage | WM-SFT-002 organizational usage record |

Purchase authorizes use but creates neither an installation nor an application. Deployment is an occurrence; installation is the standing resolved state. A hosted application may have organizational usage without a local installation, and that absence must be explicit.

## Boundary tests

A multi-product assembly receives one SoftwareSystem identity only when it has a named accountable owner, an enumerated contained set, a system-level criticality and coordinated change decisions. Integration alone creates a dependency, not a new system.

A module becomes an independently governed BusinessApplication only by an explicit, dated promotion with its own application key, purpose and owner. Independent criticality, deployment and usage strengthen the evidence. Separate licensing alone is insufficient.

## ERP acceptance scenario

One vendor ERP product has two releases. Two runtime environments and their deployment histories resolve to two installations. Three BusinessApplications—Finance, Procurement and HR/Payroll—have distinct application keys, purposes, owners or criticality. Procurement spans both installations for different organizational contexts. The product, two installations, three applications and their usage records remain separately identifiable; none derives its identity from the vendor product name.

## Invariants

1. Every SoftwareSystem has an enumerated boundary and accountable owner.
2. Every ApplicationUsage has organizational context and a validity window.
3. A purchase or entitlement never implies an installation.
4. A vendor product name is not a key for a system, installation, application, module or usage.
5. Product-to-application and application-to-installation mappings are many-to-many.
6. Module promotion requires an application key, owner and effective date; it is never inferred.
7. Hosted delivery without a local installation is represented explicitly.
8. Each layer has one authoritative master and does not mint another layer's identity.

## Holds

The shared N4 specification must be split; WM-SFT-001 runtime findings must be reconciled with WM-SFT-002 and WM-SFT-010; WM-SFT-010 has no complete current specification; parent/reference edges are absent or only asserted in prose; the overlap score must be recomputed; purchased licence/entitlement lacks a registry reservation. ArchiMate, CSDM, SPDX, OpenTelemetry and Google SRE comparisons remain unverified. This checkpoint makes no canonical completeness, installability or publication claim.
