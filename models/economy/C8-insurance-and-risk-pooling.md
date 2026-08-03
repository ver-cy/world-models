# C8 Insurance & Risk Pooling

This meta-model describes how risks are shared: policies that promise to make losses good, premiums that fund the promise, pools and reinsurance that spread the exposure, and claims that call the promise in. It is its own model because the policy is a bilateral record with a lifecycle of its own, while pooling and claims settlement follow rules that no general agreement model captures.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:c8"
  csn: world.insurance
  version: 0.2.0
  displayName: "Insurance & Risk Pooling"
  description: "Policies, premiums, pools, reinsurance and claims from cover to settlement."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.insurance
bundles:
  - csn: world.insurance.cover
    displayName: "Cover"
    layers:
      - world.insurance.cover.policyTerms
      - world.insurance.cover.underwriting
  - csn: world.insurance.pooling
    displayName: "Pooling"
    layers:
      - world.insurance.pooling.participation
      - world.insurance.pooling.reserves
  - csn: world.insurance.claims
    displayName: "Claims"
    layers:
      - world.insurance.claims.assessment
      - world.insurance.claims.settlement
imports:
  - source: acord
    version: "*"
  - source: iso-4217
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `cover` | What is promised and at what price | `policyTerms`: cover, exclusions and insured interests Â· `underwriting`: risk assessment and premium setting |
| `pooling` | How exposure is spread | `participation`: pool membership, cessions and reinsurance Â· `reserves`: funding, reserves and solvency snapshots |
| `claims` | How losses are made good | `assessment`: notification, documentation and loss evaluation Â· `settlement`: payout, denial and subrogation |

## Objects

- `policy`: the insurance promise; key attributes: line of business, inception date, expiry, status.
- `insuredInterest`: what is covered; key attributes: interest kind, sum insured, referent link, exclusion notes.
- `premiumSchedule`: the agreed payments; key attributes: amount, currency, frequency, payment status.
- `riskAssessment`: the underwriting judgment; key attributes: rated peril set, rating factors, assessment date.
- `riskPool`: a pooling arrangement; key attributes: pool kind (mutual pool, reinsurance treaty), coverage scope, period.
- `poolParticipation`: a share in a pool; key attributes: participant reference, share, attachment terms.
- `claim`: a call on the promise; key attributes: notification date, peril, claimed amount, status.
- `lossAssessment`: the evaluation of a claim; key attributes: assessed amount, assessor reference, findings summary.
- `settlement`: the resolution of a claim; key attributes: outcome (paid, partly paid, denied), amount, date, subrogation flag.

## Relationships

- `policy` -> covers -> `insuredInterest` (1:n): the interests a policy protects.
- `insuredInterest` -> attachesTo -> `world.landParcel` (n:1): the external referent, for example property (P2), a person (H1) or an organization asset (O1).
- `policy` -> heldBy -> `world.organization` (n:1): the policyholder, an organization (O1) or a person (H1).
- `premiumSchedule` -> funds -> `policy` (1:1): the payment side of the promise.
- `poolParticipation` -> cedes -> `riskPool` (n:m): shares of policies or portfolios ceded into pools and treaties.
- `claim` -> madeUnder -> `policy` (n:1): the promise the claim invokes.
- `lossAssessment` -> evaluates -> `claim` (1:1): the judgment on the loss.
- `settlement` -> resolves -> `claim` (1:1): the terminal outcome of the claim.

## Events

- `policyIssued`: cover took effect between insurer and insured.
- `coverAmended`: interests, sums or exclusions changed mid-term.
- `premiumCollected`: a scheduled payment was received.
- `riskCeded`: exposure was passed into a pool or reinsurance treaty.
- `claimNotified`: the insured reported a loss.
- `lossAssessed`: the loss was evaluated.
- `claimSettled`: the claim was paid, partly paid or denied.
- `policyLapsed`: cover ended by expiry, cancellation or non-payment.

## Contracts

- `policyMirror`: insurer and insured hold the identical policy and claim record as a bilateral mirror.
- `claimsHistoryDisclosure`: consented disclosure of a holder's claims experience to another insurer or broker.
- `poolAccounts`: participants receive periodic pool composition, exposure and reserve reports.

## Projections

- `coverCertificate`: proof of cover for third parties; omits premium and underwriting detail.
- `claimsExperience`: per-holder loss history summary; omits assessment working papers.
- `poolExposureView`: aggregate exposure and reserve adequacy for a pool; omits individual policies.

## Composition

- EXTEND `world.commercialContract` (O5): a policy is a specialized agreement with insurance-specific obligations and lifecycle.
- REFERENCE `world.priceValuation` (C7): insured values and loss quantification rely on appraisals and indices.
- REFERENCE `world.organization` (O1) and `world.person` (H1): insurers, holders and beneficiaries.
- REFERENCE `world.landParcel` (P2): insured property interests resolve to parcels and buildings.
- REFERENCE `world.disputeResolution` (A19): contested claims escalate there.
- REFERENCE `world.stewardship` (S1) and `world.accessGrant` (S2): ownership and access grants over policy, pool and claim records.
- MIX-IN `world.auditTrail` (S4): audit facets on issuance, cession and settlement events.
- imports: acord (ALIGN): insurance data interchange vocabulary across cover, pooling and claims.
- imports: iso-4217 (REFERENCE): currency codes on premiums, reserves and settlements.

## Stewardship

Policy and claim records are bilateral, owned jointly by insurer and insured; pool records are stewarded by the pool operator for its participants. Access is granted by the owners under the S1/S2 models of this catalogue.
