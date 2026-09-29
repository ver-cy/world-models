# Frozen audit request: EM-TEC-02

Perform one no-tools semantic audit. Return ACCEPT or REVISE and a closed defect checklist. Check identity/lifecycle/mastership, rule decidability, fixture discrimination, reserved-ID safety, allocation safety and publication claims. Do not invent identifiers.


## Claude study
# Verdict

**Complete and rename WM-SFT-002** as the operator-side host for EM-TEC-02, rather than reuse it under its current name or open a new host. Decision: *reuse-with-extend + rename*, contingent on splitting the shared legacy spec.

The dossier's own coordinates support this over the display name. `nav_path` is `NAV.INF.SFT.SYS` and `domain_tags` `INF.SFT.SYS` — a *system* slot, not a deployment slot. Both declared children (WM-SFT-009 `DEP`, WM-SFT-010 `RUN`) name WM-SFT-002 as `parent_ids`, which only coheres if the parent is a system-level host and not itself one installation. Conversely, WM-SFT-009's boundary note reads WM-SFT-002 as "parent software product or service model" owning "product identity, ownership and commercial context" — wider than the registry name and already owned by WM-SFT-001. The name "Deployed System" is therefore narrower than its nav slot and its children, while one neighbour reads it wider than its registry record. Neither reading is EM-TEC-02.

Recommended name: **Software System and Business Application** (operator-side). Vendor product stays WM-SFT-001; deployment occurrence stays WM-SFT-009; execution context stays WM-SFT-010.

# Evidence

1. **Shared-spec collision.** WM-SFT-001 and WM-SFT-002 carry the same `existing_spec_ref` (`N4-software-product-and-system.md`), same `legacy_alias` N4, same `purpose` string, same `source_version_or_year`. One 5,589-byte legacy document backs two reservations.
2. **Triple claim on the runtime side.** WM-SFT-001's published draft lists in scope "Deployed instances, hosting environments, effective configuration and exposed interfaces" with findings `deployed-instance-record`, `hosting-environment-and-platform`, `effective-configuration-state`. WM-SFT-002 is *named* Deployed System. WM-SFT-010 owns runtime environments. Three reservations, one referent.
3. **Ledger asymmetry.** WM-SFT-002 has empty `contains_ids`, empty `relations_ref`, and zero rows among the three supplied relations. Its claimed children assert parentage from their side only; WM-SFT-009's adjudication already flags the CHILD edge as prose, not contract.
4. **Owner-field contradiction.** WM-SFT-002's `owner_or_maintainer` is "producing organization", while the legacy N4 stewardship section assigns deployed systems to the *operator*, and the contour's `suggested_owner` is CTO/CIO/service owner. The registry field contradicts both.
5. **Overlap factor unverified.** `factor_overlap` 0.09 with `priority_confidence` low cannot survive (1) and (2); it was not computed against the published WM-SFT-001 draft.
6. **Homeless referent.** WM-SFT-001 explicitly excludes "Commercial contracts, pricing and entitlement fulfilment mechanics". Purchased licence has no reservation in this dossier.

# Identity/mastership

One master per layer, single writer, no cross-minting:

| Layer | Identity | Candidate master |
|---|---|---|
| Vendor product / release | product + version coordinates (WM-SFT-001) | producer catalogue; Git, CI/CD for build side |
| Entitlement / purchased licence | contract line + entitled quantity | **no reservation — declared gap** |
| Software system | system key + owner | CMDB / software catalogue |
| Business application | `application_key` | Каталог ПО (software catalogue) |
| Application module | module key, scoped inside its product release | producer catalogue, mirrored in the software catalogue |
| Runtime environment | environment key (WM-SFT-010) | CMDB, observability |
| Deployment occurrence | deployment id (WM-SFT-009) | CI/CD |
| Installation (standing) | derived: environment ref + current-deployment resolution | resolved, not minted |
| Usage | application + organizational context + window | software catalogue / service owner |

WM-SFT-002 masters system, business application, module placement and usage. It **references** installations rather than re-mastering them: WM-SFT-009 already owns current-deployment resolution and WM-SFT-010 owns the target. This avoids creating a fourth claimant on the runtime side.

# Product/licence/system/runtime/deployment

- **Product** — what a producer offers; identity independent of any buyer. Naming an ERP product says nothing about who runs it.
- **Purchased licence/entitlement** — a commercial fact between two organizations. It authorises installation and use; it creates neither. No installation, application or usage record may be derived from it.
- **Logical system** — an operator-scoped bounded assembly of one or more product releases, managed as one technical whole under one accountable owner.
- **Runtime installation** — a standing installed state of a system or module in one runtime environment; exists only where a deployment record resolves as current against that environment.
- **Deployment occurrence** — the repeatable act/record of installing a release to a target. Repeated deploys of the same release to the same target are distinct records and do not multiply installations.

# Business application and usage

**BusinessApplication** is an organization-side unit of managed software capability: `application_key`, `business_purpose`, named owner, `criticality`, `hosting_strategy` (all four candidate-not-normative). It is realised by one or more modules or systems, and realises one or more business functions. It is not the product, not the installation, and not the licence.

A product supports several business applications whenever distinct business purposes are separately owned and separately rated for criticality on the same product base — the ERP case. The mapping is many-to-many in both directions: one application may span several installations (regional entities), one installation may carry several applications.

**ApplicationUsage** binds a business application to an organizational context — org unit, business process, site, user population, validity window, and the entitlement relied upon. Usage is a record about the organization, never a substitute for the application. A hosted application can have usage with no local installation and no deployment record; that absence is recorded explicitly.

# Module/system boundary

A module is identified *inside* its containing product release. It becomes an independently managed application when a majority of these hold, with the promotion dated:

1. Its own `application_key` in the software catalogue.
2. A distinct `business_purpose` and a named accountable owner different from its siblings'.
3. Its own `criticality` rating driving its own availability commitments.
4. It can be withdrawn or upgraded without changing sibling availability — evidenced by deployment records that target it alone.
5. Its own usage records with independent organizational context.

Separate licensing alone is **not** sufficient: metering is a commercial fact, not a management boundary. Shared-schema coupling alone is not disqualifying if 1–5 hold; the test is management independence, not technical isolation.

# Integrated system boundary

A multi-product assembly earns a system identity when all four hold: one named accountable owner; an enumerated set of contained product releases; a system-level criticality and change decision surface (releases coordinated as a whole); and removal of any contained product changes the delivered capability. Evidence: the enumerated contained set, coordinated deployment records across the members, a single service identity in observability, and one CMDB owner. Integration alone — two independently owned products exchanging messages — creates a dependency, not a system.

# Invariants

1. Every system states a boundary as an enumerated contained set plus a named owner; unbounded system records are invalid.
2. Every usage carries organizational context and a validity window.
3. No entitlement or purchase creates or implies an installation; installation requires a current deployment against a runtime environment.
4. A vendor product name is never a key for a system, installation, application, module or usage.
5. product↔application and application↔installation are both many-to-many; neither may be collapsed to 1:1.
6. Module→application promotion requires a distinct application key, a named owner and a promotion date; it is never inferred.
7. Absence of installation for hosted delivery is recorded explicitly, not inferred from silence.
8. Each layer has exactly one master; keys are never minted in another layer's master.

# Scenario

- **P1** — one vendor ERP product (WM-SFT-001), releases R1, R2.
- **E1, E2** — two runtime environments (WM-SFT-010); **D1…Dn** deployment records (WM-SFT-009). Installations **I1** (E1, current = R2) and **I2** (E2, current = R1) resolve from those records.
- **S1** — system spanning P1 plus a reporting product; boundary enumerated; one owner.
- **BA-Finance** (I1), **BA-Procurement** (I1 and I2, split by legal entity), **BA-HR-Payroll** (I2). Three application keys, three purposes, three criticality ratings.
- **Usages** — one per org unit/process/window, ≥3.

Non-merge check: products 1, installations 2, applications 3, usages ≥3 — twelve-plus distinct keys, none derived from the product name. Buying entity B's licence yields an entitlement row; I2 appears only when D-k targets E2. Upgrading I1 to R2 leaves BA-Procurement's I2 leg on R1 without splitting the application identity. Invariants 3, 4 and 5 fail closed against the negative case.

# Minimal completion shape

Rename; correct `owner_or_maintainer` to the operating organization; split N4 so `existing_spec_ref` is unshared; scope and out-of-scope statements; boundary notes against WM-SFT-001, WM-SFT-009, WM-SFT-010 and the unregistered entitlement referent; findings for BusinessApplication, SoftwareSystem, ApplicationModule, ApplicationUsage, system-boundary justification and module-promotion; `contains_ids` and relation rows for the two children plus a REFERENCE to WM-SFT-001; the eight invariants as checkable rules; mastership table; the four v1 fields carried as candidate-not-normative.

# Holds

Shared N4 spec must be split before either WM-SFT-002 or WM-SFT-001 advances. WM-SFT-001's deployed-instance, hosting-environment and effective-configuration findings need an overlap adjudication against WM-SFT-010 and WM-SFT-002. WM-SFT-010 has no spec in this dossier. The 009/010 parentage and any 002 edge are absent from the relation ledger. `factor_overlap` must be recomputed. Purchased licence/entitlement needs a reservation the owner must mint; no identifier is proposed here. Comparison tracks (ArchiMate, CSDM, SPDX, OpenTelemetry, Google SRE) are unverified in this review — alignment only, no conformance. No canonical completeness and no installability is claimed; this is a boundary decision for owner adjudication.


## Grok study
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


## Reserved candidate
{
  "format": "vercy-world-model-candidate/v1",
  "contourId": "EM-TEC-02",
  "modelId": "WM-SFT-002",
  "registryId": "vr.wm-sft-002",
  "name": "Software System / Business Application",
  "version": "0.1.0-candidate.1",
  "entryKind": "operator-software-aggregate",
  "status": "research-candidate",
  "canonicalPublishable": false,
  "purpose": "Represent operator-governed logical software systems, business applications and effective-dated organizational usage without absorbing vendor product, entitlement, deployment or runtime identity.",
  "boundary": {
    "owns": [
      "stable software-system identity and enumerated technical boundary",
      "stable business-application identity, purpose, accountable owner and criticality",
      "many-to-many product, system and application mappings",
      "effective-dated ApplicationUsage by organizational context",
      "explicit module promotion into independently governed application identity"
    ],
    "delegates": [
      "vendor software-product and release identity to WM-SFT-001",
      "deployment occurrence and activation evidence to WM-SFT-009",
      "runtime environment, infrastructure resource and hosting topology to WM-SFT-010",
      "purchased licence and usage entitlement to an identifier-unassigned commercial candidate"
    ],
    "excludes": [
      "vendor product catalogue and release lifecycle",
      "purchase, contract, licence or entitlement lifecycle",
      "deployment execution and runtime health",
      "automatic identity from product name, installation, region or module"
    ]
  },
  "objects": {
    "SoftwareSystem": {
      "identity": ["softwareSystemId"],
      "required": ["name", "ownerRef", "containedReleaseRefs", "criticality", "status"],
      "optional": ["successorRef", "retiredAt"],
      "lifecycle": ["proposed", "approved", "active", "restricted", "retired", "superseded"]
    },
    "BusinessApplication": {
      "identity": ["applicationKey"],
      "required": ["businessPurpose", "ownerRef", "criticality", "status"],
      "optional": ["systemRefs", "productRefs", "successorRef"],
      "lifecycle": ["proposed", "approved", "active", "restricted", "retired", "superseded"]
    },
    "ApplicationUsage": {
      "identity": ["applicationUsageId"],
      "required": ["applicationRef", "organizationalContextRef", "validFrom", "deliveryMode"],
      "optional": ["validTo", "installationRefs", "userPopulationRef", "siteRef"]
    }
  },
  "relations": [
    {"target":"WM-SFT-001","relation":"REFERENCE","purpose":"Vendor product and release master"},
    {"target":"WM-SFT-009","relation":"REFERENCE","purpose":"Deployment occurrence and activation evidence"},
    {"target":"WM-SFT-010","relation":"REFERENCE","purpose":"Runtime environment and hosting topology"},
    {"target":"WM-ORG-001","relation":"REFERENCE","purpose":"Accountable organizational owner and usage context"}
  ],
  "invariants": [
    "Every SoftwareSystem has an enumerated technical boundary and accountable owner.",
    "Every BusinessApplication has a stable application key, business purpose, owner and criticality.",
    "Every ApplicationUsage states organizational context, delivery mode and a validity window.",
    "A purchase, licence or entitlement never implies an installation, system or application identity.",
    "A vendor product name is never a key for a system, installation, application, module or usage record.",
    "Product-to-application and application-to-installation mappings remain many-to-many.",
    "A module becomes a BusinessApplication only through an explicit dated promotion with its own key and owner.",
    "Separate licensing alone never promotes a module to application identity.",
    "Hosted delivery without a local installation is represented explicitly rather than treated as missing data.",
    "Deployment is an occurrence while installation is a resolved standing state from deployment and runtime evidence.",
    "Regional deployment creates a new WM-SFT-009 occurrence and never a new product, system or application identity.",
    "Each layer retains one authoritative master and never mints another layer's identity.",
    "Retired identifiers and historical mappings remain resolvable and are never recycled."
  ],
  "holds": [
    "The shared legacy N4 specification must be split from WM-SFT-001.",
    "Registry relation rows and overlap evidence require reconciliation.",
    "Purchased Licence / Entitlement remains identifier-unassigned.",
    "Independent Grok review and one frozen semantic audit remain pending.",
    "Package conversion and live verification are pending."
  ]
}


## Reserved fixtures
{
  "format": "vercy-world-model-fixtures/v1",
  "modelId": "WM-SFT-002",
  "version": "0.1.0-candidate.1",
  "cases": [
    {"id":"erp-three-applications","kind":"positive","input":"One ERP product has Finance, Procurement and HR applications with distinct keys, owners and criticality.","expect":"Three BusinessApplication identities reference the shared product without identity collapse."},
    {"id":"procurement-two-installations","kind":"positive","input":"Procurement spans two installations for different organizational contexts.","expect":"One application has two effective usage or installation bindings and retains one application identity."},
    {"id":"hosted-no-installation","kind":"positive","input":"A SaaS application is used by one business unit with no local installation.","expect":"ApplicationUsage records hosted delivery explicitly and no local installation is fabricated."},
    {"id":"purchase-implies-installation","kind":"negative","input":"A purchased licence automatically creates an installation and application record.","expect":"The inference is rejected because entitlement, deployment and application are separate lifecycles."},
    {"id":"product-name-key","kind":"negative","input":"The vendor product name is reused as system, application and installation key.","expect":"The records are rejected until each governed layer has its own identity and master."},
    {"id":"module-auto-promotion","kind":"negative","input":"A separately licensed module is automatically promoted to a BusinessApplication.","expect":"Promotion is blocked until a dated decision assigns its own application key, purpose and owner."},
    {"id":"regional-product-clone","kind":"negative","input":"Deploying the same release in a second region creates a second Software Product and BusinessApplication.","expect":"The clones are rejected; only a new deployment occurrence and runtime binding are created."}
  ]
}


## Allocation candidate
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-TEC-02",
  "proposedName": "Purchased Licence / Entitlement",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NEW MODEL",
  "canonicalPublishable": false,
  "identityTest": {
    "stableIdentity": "A purchased software licence or entitlement remains identifiable across assignment, consumption, renewal, suspension, product upgrades and installation changes.",
    "versionIdentity": "Changes to licensed product scope, metric, quantity, territory, term, permitted use or assignment rules create effective-dated entitlement revisions while preserving commercial history.",
    "independentLifecycle": ["requested", "ordered", "provisioned", "active", "suspended", "expired", "terminated", "renewed", "superseded"],
    "mastership": "software asset management, procurement or licensing authority"
  },
  "boundary": {
    "owns": [
      "stable purchased-entitlement identity",
      "licensed product or edition scope",
      "licence metric, quantity, territory and term",
      "permitted-use and assignment constraints",
      "effective allocation to organizational consumers or managed systems",
      "provisioning, suspension, expiry, termination and renewal state",
      "consumption and compliance references without owning observations"
    ],
    "references": [
      {"target":"WM-SFT-001","purpose":"Licensed vendor product, edition or release family"},
      {"target":"WM-SFT-002","purpose":"Operator system or business application consuming the entitlement"},
      {"target":"WM-ECO-006","purpose":"Commercial agreement or licence instrument"},
      {"target":"WM-XCT-029","purpose":"Duties, restrictions and surviving obligations"}
    ],
    "excludes": [
      "software-product, system, application or installation identity",
      "deployment occurrence and runtime environment lifecycle",
      "contract and obligation mastership",
      "payment, invoice or accounting lifecycle",
      "usage observation and compliance-assessment identity"
    ]
  },
  "objects": {
    "PurchasedEntitlement": {
      "identity": ["entitlementId"],
      "required": ["agreementRef", "productScopeRef", "licenceMetric", "quantity", "validFrom", "status"],
      "optional": ["validTo", "territory", "permittedUse", "assignmentRule", "successorRef"],
      "lifecycle": ["requested", "ordered", "provisioned", "active", "suspended", "expired", "terminated", "renewed", "superseded"]
    },
    "EntitlementAllocation": {
      "identity": ["entitlementAllocationId"],
      "required": ["entitlementRef", "consumerRef", "quantity", "effectiveFrom", "status"],
      "optional": ["effectiveTo", "systemRef", "applicationRef", "justification", "successorRef"]
    }
  },
  "invariants": [
    "Purchase, licence or entitlement never implies an installation, deployment, system or application identity.",
    "Every entitlement references an authoritative agreement or licence instrument and an explicit product scope.",
    "Licence metric, quantity, territory, term and permitted-use constraints remain versioned and historically resolvable.",
    "Allocation never exceeds the effective entitlement quantity under its declared metric.",
    "Assignment or reallocation changes entitlement usage without changing software-product or application identity.",
    "Product upgrade eligibility never rewrites the identity of historical licensed scope.",
    "Suspension, expiry and termination stop effective use but preserve commercial and compliance history.",
    "Renewal creates a successor period or revision and never silently extends an expired term.",
    "Observed use and compliance verdicts remain external evidence and never become entitlement state by inference.",
    "Hosted delivery may have an entitlement without a local installation and that absence is explicit.",
    "Contract duties and surviving restrictions remain externally mastered after entitlement termination.",
    "Retired entitlement and allocation identifiers remain resolvable and are never recycled."
  ],
  "holds": [
    "Independent Grok review is pending.",
    "Registry namespace and identifier allocation are pending and no identifier may be guessed.",
    "Agreement, obligation and usage-observation crosswalks require frozen audit.",
    "Licence metric and product-scope code lists remain unresolved.",
    "Package conversion and live verification are pending."
  ]
}


## Binding profile
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-TEC-02",
  "name": "Enterprise Software System and Entitlement Binding",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": ["WM-SFT-001", "WM-SFT-002", "WM-SFT-009", "WM-SFT-010", "WM-ECO-006", "WM-XCT-029"],
  "constraints": [
    "Vendor Product, operator Software System, Business Application, Deployment and Runtime Environment remain separate masters.",
    "Entitlement authorizes bounded use but never creates an installation, deployment or application.",
    "ApplicationUsage may reference entitlement allocation while retaining its organizational validity window.",
    "Hosted applications may have entitlement and usage without any local installation.",
    "Agreement and surviving obligation semantics remain outside the entitlement aggregate."
  ],
  "holds": [
    "WM-SFT-002 canonical completion and legacy N4 split remain pending.",
    "Licence metric and agreement crosswalks remain incomplete.",
    "Independent Grok review and frozen audit remain pending."
  ]
}


## Allocation fixtures
{
  "format": "vercy-enterprise-allocation-fixtures/v1",
  "candidateName": "Purchased Licence / Entitlement",
  "cases": [
    {"id":"saas-no-installation","kind":"positive","input":"A business unit purchases 500 SaaS seats and uses the application without a local installation.","expect":"The entitlement and application usage are valid while local installation remains explicitly absent."},
    {"id":"reallocation","kind":"positive","input":"Fifty seats move from one business unit to another within the same effective entitlement.","expect":"Successor allocation records preserve history without changing product or application identity."},
    {"id":"renewal","kind":"positive","input":"An annual entitlement is renewed with a higher quantity and a successor term.","expect":"A successor entitlement period or revision is linked; the expired period remains resolvable."},
    {"id":"purchase-creates-installation","kind":"negative","input":"A purchase order automatically creates an installation and active deployment.","expect":"The inference is rejected because commercial authorization and technical deployment are separate lifecycles."},
    {"id":"over-allocation","kind":"negative","input":"Six hundred seats are allocated from a 500-seat entitlement.","expect":"The allocation is rejected or held as non-compliant; entitlement quantity is not silently expanded."},
    {"id":"silent-extension","kind":"negative","input":"An expired licence remains active because the application is still running.","expect":"Effective entitlement is expired; observed running state does not extend the commercial term."},
    {"id":"product-upgrade-rewrite","kind":"negative","input":"Upgrade rights cause the old licensed product scope to be overwritten with a new release.","expect":"The rewrite is rejected; historical scope remains intact and upgrade eligibility is recorded separately."}
  ]
}
