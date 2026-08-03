# N1 Document & Record

This meta-model describes documents as governed records: information objects with a stable identity that outlives any single file, carried through versions and renditions, made trustworthy by signatures and custody trails, and disposed of under retention rules. It is its own model because recordkeeping semantics (versioning, authenticity, retention, holds) recur across every domain that produces paperwork, from contracts to certificates, and deserve one shared vocabulary rather than per-domain reinvention.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:n1"
  csn: world.documentRecord
  version: 0.2.0
  displayName: "Document & Record"
  description: "Documents as governed records with versions, renditions, signatures, custody and retention."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.documentRecord
bundles:
  - csn: world.documentRecord.identityAndContent
    displayName: "Identity and content"
    layers:
      - world.documentRecord.identityAndContent.identity
      - world.documentRecord.identityAndContent.content
      - world.documentRecord.identityAndContent.versioning
  - csn: world.documentRecord.authenticity
    displayName: "Authenticity"
    layers:
      - world.documentRecord.authenticity.signatureAndSeal
      - world.documentRecord.authenticity.custodyAndProvenance
  - csn: world.documentRecord.recordkeeping
    displayName: "Recordkeeping"
    layers:
      - world.documentRecord.recordkeeping.retentionAndDisposition
      - world.documentRecord.recordkeeping.classificationAndHolds
imports:
  - source: dublin-core
    version: "*"
  - source: iso-15489
    version: "*"
  - source: premis
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `identityAndContent` | What the document is and what it says | `identity`: stable document identity, class, issuer Â· `content`: body, formats, renditions Â· `versioning`: immutable version states and supersession |
| `authenticity` | Why the record can be trusted | `signatureAndSeal`: signatures, seals, attestations on versions Â· `custodyAndProvenance`: chain of custody and origin |
| `recordkeeping` | How long the record lives and under what marking | `retentionAndDisposition`: schedules, triggers, disposition Â· `classificationAndHolds`: confidentiality marking and legal holds |

## Objects

- `document`: a governed information object with identity independent of any single file; key attributes: documentId, title, documentClass, status, issuerRef.
- `documentVersion`: an immutable state of a document's content at a point in time; key attributes: versionNumber, contentHash, createdAt, changeNote.
- `rendition`: a format-specific realization of a version; key attributes: mediaType, byteSize, checksum, storageRef.
- `signature`: a signature, seal or attestation applied to a version; key attributes: signerRef, method, signedAt, validityStatus.
- `retentionRule`: an assigned retention schedule; key attributes: retentionClass, triggerEvent, retentionPeriod, dispositionAction.
- `legalHold`: a suspension of disposition pending proceedings; key attributes: holdReason, placedBy, placedAt, releasedAt.
- `registerEntry`: the listing of a document in a custodial register; key attributes: registerRef, entryNumber, registeredAt.

## Relationships

- `document` -> hasVersion -> `documentVersion` (1:N): the version chain of the record.
- `documentVersion` -> renderedAs -> `rendition` (1:N): one content state, many formats.
- `signature` -> signs -> `documentVersion` (N:1): authenticity attaches to a specific version.
- `document` -> governedBy -> `retentionRule` (N:1): the schedule that decides the record's fate.
- `legalHold` -> suspends -> `retentionRule` (N:N): holds override disposition until released.
- `document` -> supersedes -> `document` (N:1): a new record replacing an older one.
- `registerEntry` -> registers -> `document` (1:1): the custodial register anchors the record.

## Events

- `documentCreated`: a new governed document came into existence.
- `versionIssued`: a new immutable content state was fixed.
- `documentSigned`: a signature or seal was applied to a version.
- `documentRegistered`: the document was entered into a custodial register.
- `holdPlaced`: disposition was suspended by a legal hold.
- `holdReleased`: a legal hold was lifted.
- `documentDisposed`: the disposition action of the retention rule was executed.

## Contracts

- `recordAccessContract`: terms under which a requester may read a record or its metadata.
- `certifiedCopyContract`: issuance of certified copies or extracts with authenticity guarantees.
- `retentionComplianceContract`: obligations between owner and custodian covering schedules, holds and disposition evidence.

## Projections

- `registerListing`: existence-level metadata (identity, class, dates); omits content and signer details.
- `evidentiaryView`: full version chain with signatures and custody trail for legal use; omits unrelated register context.
- `dispositionWorklist`: records due for disposition with applicable rules and holds; omits content bodies.

## Composition

- REFERENCE `world.person` (H1): authors, signers and custodial officers are persons governed elsewhere.
- REFERENCE `world.organization` (O1): issuing organizations and custodians.
- REFERENCE `world.identifierNaming` (N8): document numbers and register identifiers are drawn from registered schemes.
- REFERENCE `world.timeCalendar` (N11): retention triggers and periods anchor to calendar and working-day rules.
- COMPOSE `world.messageCommunication` (N7): message attachments resolve to governed documents held here.
- imports: dublin-core (MIX-IN): descriptive metadata facet applied to every document.
- imports: iso-15489 (ALIGN): records management lifecycle vocabulary.
- imports: premis (ALIGN): preservation event semantics for long-term custody.

## Stewardship

The neutral owner archetype is the author or issuing organization; a registrar or custodian may maintain the register on the owner's behalf without acquiring ownership. Access to record content and metadata is always granted by the owner through the catalogue's ownership and access models (S1/S2), with use recorded for audit via S4.
