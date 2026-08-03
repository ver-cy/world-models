# M9 Cultural Artifact & Heritage

This meta-model describes artifacts of cultural and historical significance: the object itself with its materials and making, the provenance chain and attribution research that establish what it is and where it has been, and the designation, conservation and custody apparatus that protects it. It is its own model because for heritage objects the history of the object is as much the subject as the object, and because designation and repatriation semantics exist for no other item family.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:m9"
  csn: world.culturalArtifact
  version: 0.2.0
  displayName: "Cultural Artifact & Heritage"
  description: Heritage objects with provenance, attribution, designation, conservation, custody and loan semantics.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.culturalArtifact
bundles:
  - csn: world.culturalArtifact.object
    displayName: Object
    layers:
      - world.culturalArtifact.object.artifactIdentity
      - world.culturalArtifact.object.materialsAndTechnique
      - world.culturalArtifact.object.significance
  - csn: world.culturalArtifact.provenance
    displayName: Provenance
    layers:
      - world.culturalArtifact.provenance.provenanceChain
      - world.culturalArtifact.provenance.attributionResearch
  - csn: world.culturalArtifact.care
    displayName: Care
    layers:
      - world.culturalArtifact.care.conservationCondition
      - world.culturalArtifact.care.custodyAndLoan
  - csn: world.culturalArtifact.protection
    displayName: Protection
    layers:
      - world.culturalArtifact.protection.heritageDesignation
imports:
  - source: cidoc-crm
    version: "*"
  - source: lido
    version: "*"
  - source: spectrum
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `object` | What the artifact is | `artifactIdentity`: titles, accession numbers, physical description, measurements Â· `materialsAndTechnique`: materials, techniques and marks of making Â· `significance`: assessed cultural and historical significance with basis and assessor |
| `provenance` | How we know its history | `provenanceChain`: chronological record of making, ownership, transfer and discovery episodes Â· `attributionResearch`: maker, date and origin hypotheses with evidence and standing |
| `care` | Keeping the artifact safe and whole | `conservationCondition`: condition surveys and treatments Â· `custodyAndLoan`: current custodian, collection membership, loans and movements |
| `protection` | Public protection standing | `heritageDesignation`: listings, protection categories, export restrictions and their basis |

## Objects

- `artifact`: one heritage object; key attributes: title, accession reference, description, measurements.
- `provenanceEntry`: one episode in the object's history; key attributes: episode kind, period, parties involved, evidence reference.
- `attribution`: a maker, date or origin claim; key attributes: claim, basis, researcher reference, standing (accepted, disputed, rejected).
- `significanceAssessment`: an assessed statement of significance; key attributes: dimension, statement, assessor reference, date.
- `heritageDesignation`: a protection listing; key attributes: scheme, category, jurisdiction, effective period, restrictions.
- `conservationRecord`: a condition survey or treatment; key attributes: record kind, findings, treatment applied, conservator reference.
- `custodyRecord`: a period of custody; key attributes: custodian reference, basis (ownership, deposit, seizure), period.
- `loan`: a temporary movement under agreement; key attributes: borrower reference, purpose, period, conditions.

## Relationships

- `artifact` -> documentedBy -> `provenanceEntry` (0..*, chronologically ordered): the provenance chain of the object.
- `artifact` -> attributedTo -> `attribution` (0..*): competing attributions coexist with their standing recorded.
- `artifact` -> assessedAs -> `significanceAssessment` (0..*): significance is stated, dated and attributable, never implicit.
- `artifact` -> designatedUnder -> `heritageDesignation` (0..*): protection standings per scheme and jurisdiction.
- `artifact` -> conditionRecordedIn -> `conservationRecord` (0..*): the care history of the object.
- `artifact` -> inCustodyOf -> `custodyRecord` (exactly one current, 0..* historical): who holds the object now and before.
- `artifact` -> movedUnder -> `loan` (0..*): loans overlay custody without transferring it.
- `artifact` -> partOf -> `artifact` (0..1): sets, series and composite objects.

## Events

- `artifactAccessioned`: the object entered documented custody with an accession identity.
- `provenanceEntryAdded`: research added or corrected an episode in the provenance chain.
- `attributionRevised`: an attribution changed standing on new evidence.
- `designationGranted`: a protection listing took effect for the object.
- `conservationTreatmentCompleted`: a treatment or survey was completed and recorded.
- `loanStarted`: the object left its custodian under a loan agreement.
- `loanReturned`: the object returned from loan and the overlay closed.
- `artifactRepatriated`: custody transferred to a claimant community or origin custodian.

## Contracts

- `researchAccess`: custodian-granted access to provenance and attribution layers for named researchers.
- `exhibitionLoanAgreement`: the data counterpart of a loan, defining what object data travels with the loan and who may see it.
- `reproductionLicence`: permission to reproduce images and descriptions of the object under stated terms.
- `provenanceDisclosure`: disclosure of the custody and provenance chain to a claimant, court or diligence party.

## Projections

- `publicCatalogueView`: identity, description, imagery references and accepted attribution; omits location, security and loan details.
- `scholarlyView`: full provenance chain, attribution research and conservation history; omits security logistics.
- `custodyAuditView`: custody records, loans and designations; omits research content.

## Composition

- EXTEND `world.physicalItem` (M2): an artifact is an item; instance identity, condition and custody mechanics are inherited and deepened.
- REFERENCE `world.materialSubstance` (M1): materials and technique media resolve to substance and material classes.
- REFERENCE `world.person` (H1): makers, previous owners and researchers resolve to person identities.
- REFERENCE `world.organization` (O1): museums, galleries and custodian institutions resolve to organization identities.
- REFERENCE `world.place` (P1): find sites, origin regions and display locations resolve to place identities.
- imports: cidoc-crm (ALIGN): event-centred documentation semantics for provenance and custody.
- imports: lido (ALIGN): exchange format alignment for object descriptions.
- imports: spectrum (ALIGN): collections management procedure alignment for accession, loan and condition workflows.

## Stewardship

Each artifact record is stewarded by its custodian, with a heritage authority archetype stewarding the designation layer; all research, loan and disclosure access is granted by the record owner through the catalogue's S1/S2 ownership and access models, and custody movements are traceable via S4 audit.
