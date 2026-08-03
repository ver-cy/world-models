# H1 Person

This meta-model describes the natural person as a civil identity and as the subject of a life course: the registered identity with its documents and identifiers, civil status and legal capacity, and the anchor point to which life events, relations and personal data attach. It is its own model because the person is the most referenced entity in the whole catalogue and must therefore carry a stable identity core, strict subject ownership of personal data, and nothing else, so every other model can reference persons without copying them.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:h1"
  csn: world.person
  version: 0.2.0
  displayName: Person
  description: The natural person as civil identity, life-course subject and owner of personal data.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.person
bundles:
  - csn: world.person.civilIdentity
    displayName: Civil identity
    layers:
      - world.person.civilIdentity.identityCore
      - world.person.civilIdentity.identityDocument
      - world.person.civilIdentity.identifierScheme
  - csn: world.person.lifeCourse
    displayName: Life course
    layers:
      - world.person.lifeCourse.lifeEvent
      - world.person.lifeCourse.capacityAndGuardianship
  - csn: world.person.personalSphere
    displayName: Personal sphere
    layers:
      - world.person.personalSphere.contactAndPresence
      - world.person.personalSphere.selfDeclaredAttributes
imports:
  - source: schema-org-person
    version: "*"
  - source: iso-iec-24760
    version: "*"
  - source: oasis-ciq
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `civilIdentity` | The registered identity and its evidence | `identityCore`: legal name, birth facts, civil status Â· `identityDocument`: documents evidencing identity Â· `identifierScheme`: identifiers assigned under named schemes |
| `lifeCourse` | The person through time as a legal subject | `lifeEvent`: anchors to vital and registered life events Â· `capacityAndGuardianship`: legal capacity, guardianship, emancipation |
| `personalSphere` | What the person declares and controls | `contactAndPresence`: contact points and declared residence pointer Â· `selfDeclaredAttributes`: preferences and self-declared facts under the person's sole control |

## Objects

- `person`: the natural person as a stable identity; key attributes: canonical identifier, status (living, deceased), registration authority reference
- `personName`: a structured name with validity period; key attributes: given, family, ordering convention, script, validity
- `identityDocument`: an issued document evidencing identity; key attributes: type, number reference, issuer reference, validity, revocation state
- `identifierAssignment`: an identifier under a named scheme; key attributes: scheme, value pointer, assigning authority, validity
- `civilStatus`: the registered civil state; key attributes: status value, effective date, registering authority
- `capacityState`: legal capacity at a point in time; key attributes: capacity class, basis, effective period
- `guardianshipTie`: a guardianship or representation arrangement; key attributes: guardian reference, scope, basis, period
- `contactPoint`: a person-controlled contact channel; key attributes: channel type, value pointer, visibility setting
- `lifeEventRef`: an anchor to a life event recorded in another model; key attributes: event type, source model, event identifier, date

## Relationships

- `person` -> namedBy -> `personName` (1..n): names are versioned facts, not fixed attributes
- `person` -> evidencedBy -> `identityDocument` (1..n): documents evidence but never constitute the identity
- `person` -> holds -> `identifierAssignment` (1..n): scheme-qualified identifiers attach to the person without becoming the person
- `person` -> hasStatus -> `civilStatus` (1..1): one current status, with history carried by events
- `guardianshipTie` -> places -> `person` (n..1): a person may be under guardianship; the guardian is another person or organization
- `person` -> memberOf -> `household` (n..m): household membership resolves in H2
- `lifeEventRef` -> anchors -> `person` (n..1): life events recorded across the catalogue anchor back to the person

## Events

- `birthRegistered`: a person's identity was created by civil registration
- `nameChanged`: a new legal name took effect
- `documentIssued`: an identity document was issued
- `documentRevoked`: an identity document was invalidated before expiry
- `civilStatusChanged`: the registered civil status changed
- `capacityChanged`: legal capacity was established, restricted or restored
- `guardianshipEstablished`: a guardianship arrangement took effect
- `deathRegistered`: the identity was closed by death registration

## Contracts

- `identityVerificationContract`: attribute verification answered as confirmation only, without disclosing underlying data
- `personalDataConsent`: the person's standing grants over personal-sphere and identity attributes, grounded in S1
- `vitalStatisticsExtract`: anonymized aggregates of registrations released to the statistics office

## Projections

- `verifiedIdentityView`: the minimal attribute set needed for a given verification; omits everything not asked
- `publicRecordExtract`: only what registration law makes public; omits the entire personal sphere
- `selfView`: the person's own complete view of every record and grant concerning them

## Composition

- REFERENCE `world.household` (H2): household and family membership lives in the household model and points here
- REFERENCE `world.populationGroup` (H3): group and community membership resolves against the person identifier
- REFERENCE `world.educationQualification` (H4): earned credentials anchor to the person as holder
- REFERENCE `world.organization` (O1): issuing authorities, employers and guardians-as-organizations are organizations
- imports: schema.org Person (ALIGN): public projection typing for person data
- imports: ISO/IEC 24760 (ALIGN): identity, identifier and identity-assurance vocabulary
- imports: OASIS CIQ (EMBED): structured name and address value shapes reused rather than re-invented

## Stewardship

The civil registrar owns the registered identity record (identity core, documents, civil status); the person owns all personal-sphere data and every consent over it via S1. Any access to person data is granted by the respective owner through S1/S2 and leaves an audit trail via S4.
