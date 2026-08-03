# O1 Organization

This meta-model describes any organization on Earth: companies, non-profits, communities, institutions, cooperatives, clubs and other collectives that act under a shared name. It is its own model because organizational identity (who an organization is, how it is named, registered and classified, and how it comes into being, transforms and ceases) is referenced by nearly every other model in the catalogue while depending on none of them.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:o1"
  csn: world.organization
  version: 0.2.0
  displayName: "Organization"
  description: "Identity, legal form, registration, classification, purpose and lifecycle of any organization."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.organization
bundles:
  - csn: world.organization.identity
    displayName: "Identity"
    layers:
      - world.organization.identity.naming
      - world.organization.identity.identifiers
      - world.organization.identity.classification
  - csn: world.organization.registration
    displayName: "Registration"
    layers:
      - world.organization.registration.incorporation
      - world.organization.registration.standing
      - world.organization.registration.succession
  - csn: world.organization.profile
    displayName: "Profile"
    layers:
      - world.organization.profile.purposeAndActivity
      - world.organization.profile.presence
imports:
  - source: w3c-org
    version: "*"
  - source: iso-17442-lei
    version: "*"
  - source: nace
    version: "*"
  - source: iso-20275-elf
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `identity` | Who the organization is | `naming`: legal, trading and former names over time Â· `identifiers`: registry numbers, LEI and other identifier schemes Â· `classification`: legal form and activity codes |
| `registration` | The organization's standing in registers | `incorporation`: founding act and registry entries Â· `standing`: current status such as active, suspended or struck off Â· `succession`: mergers, splits, conversions and successor links |
| `profile` | What the organization declares about itself | `purposeAndActivity`: stated purpose and lines of activity Â· `presence`: sites, addresses and contact channels |

## Objects

- `organization`: the subject itself; key attributes: canonical id, founding date, home jurisdiction, current status.
- `organizationName`: a legal, trading or former name; key attributes: name string, kind, language, validity period.
- `organizationIdentifier`: an identifier issued under a scheme; key attributes: scheme (LEI, national registry), value, issue date.
- `legalForm`: a code drawn from a legal form scheme (ISO 20275 ELF or a national list); key attributes: scheme, code, jurisdiction.
- `registryEntry`: the organization's record in a public or private register; key attributes: register, entry number, entry date, extract reference.
- `activityClassification`: an activity code assignment (NACE or a comparable scheme); key attributes: scheme, code, primary flag.
- `purposeStatement`: a declared mission or object clause; key attributes: text, source (charter or self-declared), declaration date.
- `presencePoint`: a site, address or channel; key attributes: kind (registered office, branch, web), locator, validity period.

## Relationships

- `organization` -> knownAs -> `organizationName` (1:n): all names the organization has carried, with validity.
- `organization` -> identifiedBy -> `organizationIdentifier` (1:n): scheme-issued identifiers resolving to this subject.
- `organization` -> hasLegalForm -> `legalForm` (n:1): the legal form under its home jurisdiction.
- `organization` -> recordedIn -> `registryEntry` (1:n): entries in the registers that know this organization.
- `organization` -> classifiedAs -> `activityClassification` (1:n): declared or registered lines of activity.
- `organization` -> successorOf -> `organization` (n:m): lineage through mergers, splits and conversions.

## Events

- `organizationFounded`: the organization came into existence as a subject.
- `organizationRegistered`: a register accepted an entry for the organization.
- `nameChanged`: a legal or trading name was adopted or retired.
- `legalFormChanged`: the organization converted to a different legal form.
- `statusChanged`: registered standing moved, for example active to suspended.
- `organizationsMerged`: two or more organizations combined into a successor.
- `organizationDissolved`: the organization ceased to exist as a subject.

## Contracts

- `registryExtract`: on-demand disclosure of core registered facts to a requester admitted by the owner or the register.
- `identifierResolution`: resolving an identifier to the canonical organization record with a minimal profile in return.
- `directorySyndication`: a licensed bulk feed of public profile fields for directories and analytics.

## Projections

- `publicDirectoryCard`: name, legal form, status, primary activity and public presence; omits identifier history and internal declarations.
- `complianceProfile`: identifiers, registry entries and standing for onboarding checks; omits purpose narrative and presence detail.
- `lineageView`: the succession chain of predecessors and successors; omits all profile content.

## Composition

- REFERENCE `world.organizationalUnit` (O2): internal structure is modelled there and resolves back to this organization identity.
- REFERENCE `world.charter` (O4): constitutive rules behind the purpose statements and powers.
- REFERENCE `world.employment` (O3): person-to-organization relations resolve against identities kept here.
- REFERENCE `world.publicRegister` (A12): registry entries anchor to publicly kept registers.
- REFERENCE `world.stewardship` (S1) and `world.accessGrant` (S2): ownership records and access grants over organization data.
- MIX-IN `world.auditTrail` (S4): audit facets on all lifecycle events.
- imports: w3c-org (ALIGN): organizational ontology vocabulary for organization, site and classification.
- imports: iso-17442-lei (REFERENCE): the global legal entity identifier scheme.
- imports: nace (REFERENCE): activity classification code list.
- imports: iso-20275-elf (REFERENCE): entity legal form code list.

## Stewardship

The organization itself, acting through its officers, is the steward of its own record; registers hold their entries as registrar-stewarded copies. All access is granted by the owner under the S1/S2 models of this catalogue.
