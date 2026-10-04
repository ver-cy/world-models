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
