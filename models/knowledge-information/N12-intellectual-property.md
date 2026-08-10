# N12 Intellectual Property

This meta-model describes intellectual property as registered and exploited rights: patents, trademarks, copyrights and designs with their scope, territory and term, the applications and examinations that create them, the registers that record them, and the licenses, assignments and oppositions through which they live in the economy. It is its own model because IP rights are legal objects with their own lifecycle (file, publish, grant, renew, lapse) distinct from the creative or technical subject matter they protect.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:n12"
  csn: world.intellectualProperty
  version: 0.2.0
  displayName: "Intellectual Property"
  description: "Patents, trademarks, copyright and designs with applications, registers, licensing and disputes."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.intellectualProperty
bundles:
  - csn: world.intellectualProperty.right
    displayName: "Right"
    layers:
      - world.intellectualProperty.right.rightTypology
      - world.intellectualProperty.right.scopeAndTerm
  - csn: world.intellectualProperty.register
    displayName: "Register"
    layers:
      - world.intellectualProperty.register.applicationAndExamination
      - world.intellectualProperty.register.registerRecord
  - csn: world.intellectualProperty.exploitation
    displayName: "Exploitation"
    layers:
      - world.intellectualProperty.exploitation.licensingAndAssignment
      - world.intellectualProperty.exploitation.disputeAndOpposition
imports:
  - source: wipo-standards
    version: "*"
  - source: spdx-license-list
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `right` | What is protected and how far | `rightTypology`: patent, trademark, copyright, design, related rights · `scopeAndTerm`: claims, classes, territory, duration |
| `register` | How rights come into being and are recorded | `applicationAndExamination`: filings, priority, examination · `registerRecord`: registrations, status, renewals |
| `exploitation` | How rights are used and contested | `licensingAndAssignment`: licenses and transfers · `disputeAndOpposition`: oppositions, challenges, outcomes |

## Objects

- `ipRight`: a protected right over subject matter; key attributes: rightType, subjectMatterRef, territory, term, status.
- `ipApplication`: a filing seeking a right; key attributes: applicationNumber, filedAt, officeRef, claimsCount.
- `registration`: the register record of a granted right; key attributes: registrationNumber, grantedAt, registerRef, nextRenewalDue.
- `priorityClaim`: a claim to an earlier filing date; key attributes: priorityDate, priorApplicationRef, conventionBasis.
- `license`: a permission to use a right; key attributes: licensorRef, licenseeRef, scope, exclusivity, royaltyBasis.
- `assignment`: a transfer of a right between holders; key attributes: assignorRef, assigneeRef, effectiveAt, recordedAt.
- `opposition`: a challenge to a registration; key attributes: opponentRef, grounds, filedAt, outcome.
- `renewal`: a maintenance act extending a registration; key attributes: renewedAt, feePaid, newExpiry.

## Relationships

- `ipApplication` -> seeks -> `ipRight` (1:1): the filing that would create the right.
- `registration` -> establishes -> `ipRight` (1:1): the register record that makes the right effective.
- `priorityClaim` -> claimsPriorityFor -> `ipApplication` (N:1): earlier-date claims under convention rules.
- `license` -> grantsUseOf -> `ipRight` (N:N): permitted use without transfer of ownership.
- `assignment` -> transfers -> `ipRight` (N:1): change of holder recorded on the register.
- `opposition` -> challenges -> `registration` (N:1): contest against a recorded grant.
- `renewal` -> extends -> `registration` (N:1): maintenance keeping the right alive.

## Events

- `applicationFiled`: a filing seeking a right was received by an office.
- `applicationPublished`: the filing became publicly visible.
- `rightGranted`: examination concluded and the right was registered.
- `rightRefused`: the application was rejected.
- `oppositionFiled`: a third party challenged a registration.
- `rightAssigned`: the right changed holder on the register.
- `rightLapsed`: the right expired or was abandoned for non-renewal.

## Contracts

- `registerAccessContract`: terms for searching and extracting the public register.
- `licensingContract`: the license instrument itself, scoping use, territory, exclusivity and royalties.
- `watchServiceContract`: monitoring terms for new filings, oppositions and expiries affecting a portfolio.

## Projections

- `publicRegisterView`: registered rights, holders of record and status; omits license commercial terms.
- `holderPortfolioView`: one holder's rights, licenses, renewals and disputes; omits other parties' portfolios.
- `expiryWatchlist`: upcoming renewal and lapse dates across watched rights; omits substantive claim content.

## Composition

- REFERENCE `world.person` (H1): inventors, creators and individual holders.
- REFERENCE `world.organization` (O1): corporate holders and IP offices.
- REFERENCE `world.creativeWork` (N5): copyright and related-rights subject matter lives there.
- REFERENCE `world.softwareProduct` (N4): software subject matter and its licensing context.
- COMPOSE `world.documentRecord` (N1): filings, certificates and license deeds are governed documents.
- REFERENCE `world.identifierNaming` (N8): application and registration numbering schemes.
- imports: wipo-standards (ALIGN): register data and document formats of the WIPO standards family.
- imports: spdx-license-list (REFERENCE): standard identifiers for public software and content licenses.

## Stewardship

The neutral owner archetype is the right holder, who owns the right and its exploitation records, while the IP registrar keeps the public register as custodian of record. Access beyond the public register is always granted by the holder through the catalogue's S1/S2 ownership and access models, with register extracts and watch services audited via S4.
