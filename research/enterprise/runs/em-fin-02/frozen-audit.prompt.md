# Frozen audit prompt — EM-FIN-02

Audit only the frozen material below. Use no tools and no outside knowledge. Do not invent identifiers or claim standards compliance.

Return a concise verdict and enumerate only material defects. Check anti-dual-mastership, Ledger Account versus Financial Account identity, Chart and policy lifecycle, effective revision pinning, ledger adoption cardinality, currency roles, balancing scope and tolerance, external-event correlation, sibling divergence, append-only correction, hard-close behavior, WM-ECO-017 immutability, correspondence-only profile and fixture traceability. For each defect give the smallest remediation. End with the exact additional fixtures required. This is the one frozen audit; do not request a second audit.

## LOCAL EVIDENCE

```
# EM-FIN-02 local synthesis

## Disposition

- Reuse WM-ECO-015 only for externally serviced Financial Accounts such as bank and custody accounts.
- Reuse WM-ECO-016 for ledger-local Financial Transaction / Journal Entry and contained Posting lines.
- Reuse WM-ECO-017 for derived, time-bound balances and positions; treasury position and GL balance remain distinct.
- Introduce an identifier-unassigned **Chart of Accounts / Accounting Policy** candidate that masters CoA versions, Ledger Accounts, ledger adoption and effective accounting rules.
- Define a thin correspondence-only Enterprise Financial Event and Multi-Ledger Binding profile. It allocates no identity or runtime ID.

## Identity and mastership

Financial Account identity is issuer/custodian plus external identifier and is mastered by WM-ECO-015. Ledger Account identity is ledger plus effective Chart node/version and interval and is mastered only by the unassigned candidate. WM-ECO-016 owns one-ledger entries and their posting lines. WM-ECO-017 owns balances qualified by ledger, account, currency, scope and as-of time. External events, payments and invoices keep their own masters and are referenced only by pinned correlation.

## Boundary rules

A posting target is always a Ledger Account, never a raw WM-ECO-015 Financial Account. A Ledger Account may optionally map to at most one externally serviced backing account for a declared context and interval; the mapping is not identity. Account codes are never global and code equality across ledgers or chart revisions proves no equivalence.

One external event may correlate to sibling entries in several ledgers. Every sibling belongs to one ledger, cites the event, records a divergence reason when amount, timing, account, policy or currency differs, and balances independently. No cross-ledger netting, plugging, tolerance or correction is permitted.

## Currency, close and correction

Balancing is evaluated only within one ledger, declared balancing currency role, scope and tolerance. Settlement currency, transaction currency, functional currency and presentation currency remain explicit roles. Translation residuals post inside the same ledger.

Posted entries and lines are immutable. A correction appends a linked same-ledger entry. An open book reverses or adjusts in an open period. A hard-closed book uses the earliest permitted later period or an explicitly authorised hard-close exception. Correcting one sibling does not change another. Closed WM-ECO-017 balances remain immutable and successor balance assertions carry their own as-of time.

## Provider reconciliation

Grok conditionally accepted the reuse split but rejected Ledger Account as a WM-ECO-015 profile. The reconciled candidate owns Ledger Account under the Chart-of-Accounts lifecycle. The profile now records only source-pinned correspondence and optional backing mappings and cannot master or mutate any source object.

## Holds

The candidate has no registry allocation. WM-ECO-015/016/017 remain reviewable drafts with contradictory ownership text. Financial Transaction naming, currency roles, scope dimensions, tolerance units, CoA-to-ledger cardinality and hard-close policy need canonical adjudication. No publication or installability claim is made.

```

## PROVIDER COMPARISON

```
# EM-FIN-02 provider comparison

Claude and Grok agree that WM-ECO-015 owns externally serviced bank and custody accounts, WM-ECO-016 owns journal entries and posting lines, WM-ECO-017 owns time-bound per-ledger balances, and external payment, invoice or economic-event identities remain correlation references. Both require ledger-local balancing, immutable posted history, append-only corrections, explicit hard-close handling and an identifier-unassigned Chart of Accounts / Accounting Policy candidate.

Grok exposes one material defect in the initial Claude synthesis: Ledger Account cannot safely profile WM-ECO-015. Its identity is ledger, effective Chart-of-Accounts node and interval; a Financial Account is identified by issuer or custodian and an external account identifier. Their intersection is a mapping, never subtype identity. The reconciled candidate therefore masters Ledger Account as a governed Chart node. WM-ECO-015 owns no CoA membership, hierarchy, rollup or posting eligibility.

The Enterprise profile is correspondence-only. It records pinned external-event correlation, sibling-entry grouping, divergence reasons, optional Financial-Account backing and cross-ledger mapping evidence. It mints no account, ledger, entry, posting, balance, policy or event identity and performs no balancing. Each entry balances only inside one ledger, currency role, scope and tolerance. Corrections are same-ledger successor entries; a hard-closed book accepts only a next-period correction or an explicitly authorised exception. Closed WM-ECO-017 balances remain immutable.

No identifier or runtime ID is allocated. The candidate and profile remain non-publishable while registry allocation, base contradictions, currency-role semantics, CoA-to-ledger cardinality, hard-close policy and executable fixtures remain unresolved.

```

## ALLOCATION CANDIDATE

```json
{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-FIN-02",
  "proposedName": "Chart of Accounts / Accounting Policy",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NEW MODEL",
  "canonicalPublishable": false,
  "identityTest": {
    "stableIdentity": "A governed Chart of Accounts, its Ledger Accounts and accounting-policy basis remain identifiable across hierarchy revisions, ledger adoption, recognition changes and reporting periods.",
    "versionIdentity": "Taxonomy, hierarchy, Ledger Account, mapping, recognition, measurement, currency or close-policy changes create immutable effective-dated revisions with predecessor lineage.",
    "independentLifecycle": [
      "draft",
      "approved",
      "effective",
      "suspended",
      "superseded",
      "retired"
    ],
    "mastership": "accounting-policy and finance-governance authority"
  },
  "boundary": {
    "owns": [
      "stable Chart-of-Accounts identity and immutable revisions",
      "Ledger Account identity, hierarchy, posting eligibility and effective intervals",
      "accounting-policy identity and immutable recognition, measurement, currency and close rules",
      "explicit ledger adoption of one effective chart revision",
      "cross-ledger mapping definitions and divergence semantics",
      "authorised hard-close exception policy"
    ],
    "references": [
      {
        "target": "WM-ECO-015",
        "purpose": "Optional externally serviced Financial Account backing, never Ledger Account identity"
      },
      {
        "target": "WM-ECO-016",
        "purpose": "Entries and postings evaluated against pinned effective Ledger Account and policy revisions"
      },
      {
        "target": "WM-ECO-017",
        "purpose": "Derived per-ledger balance assertions"
      },
      {
        "target": "WM-ECO-008",
        "purpose": "Invoice correlation only"
      },
      {
        "target": "WM-ECO-009",
        "purpose": "Payment correlation only"
      },
      {
        "target": "WM-XCT-014",
        "purpose": "Monetary, currency and rate context where applicable"
      }
    ],
    "excludes": [
      "bank or custody Financial Account identity",
      "journal-entry and posting occurrence identity",
      "external event, invoice or payment identity",
      "balance and position mastership",
      "cross-ledger balancing or netting",
      "automatic accounting conclusion without effective policy and authority"
    ]
  },
  "objects": {
    "ChartOfAccounts": {
      "identity": [
        "chartOfAccountsId"
      ],
      "required": [
        "name",
        "ownerRef",
        "status",
        "currentRevisionRef"
      ],
      "optional": [
        "regimeRef",
        "successorRef"
      ],
      "lifecycle": [
        "draft",
        "approved",
        "effective",
        "suspended",
        "superseded",
        "retired"
      ]
    },
    "ChartRevision": {
      "identity": [
        "chartOfAccountsId",
        "revision"
      ],
      "required": [
        "taxonomy",
        "hierarchy",
        "ledgerAccountNodes",
        "contentDigest",
        "effectiveFrom"
      ],
      "optional": [
        "effectiveTo",
        "supersedesRevision"
      ]
    },
    "LedgerAccount": {
      "identity": [
        "ledgerRef",
        "chartRevisionRef",
        "nodeId",
        "effectiveFrom"
      ],
      "required": [
        "accountCode",
        "postingEligibility",
        "effectiveFrom",
        "policyRevisionRef"
      ],
      "optional": [
        "effectiveTo",
        "financialAccountBackingRef",
        "predecessorRef"
      ]
    },
    "AccountingPolicy": {
      "identity": [
        "accountingPolicyId"
      ],
      "required": [
        "policyKind",
        "authorityRef",
        "status",
        "currentRevisionRef"
      ],
      "optional": [
        "regimeRef",
        "successorRef"
      ]
    },
    "AccountingPolicyRevision": {
      "identity": [
        "accountingPolicyId",
        "revision"
      ],
      "required": [
        "recognitionRules",
        "measurementRules",
        "currencyRoles",
        "balancingScope",
        "tolerance",
        "closeRules",
        "contentDigest",
        "effectiveFrom"
      ],
      "optional": [
        "effectiveTo",
        "supersedesRevision"
      ]
    },
    "LedgerAdoption": {
      "identity": [
        "ledgerRef",
        "chartOfAccountsId",
        "effectiveFrom"
      ],
      "required": [
        "chartRevisionRef",
        "policyRevisionRef",
        "effectiveFrom",
        "authorityRef"
      ],
      "optional": [
        "effectiveTo",
        "revocationRef"
      ]
    }
  },
  "invariants": [
    "Financial Account, Ledger Account, Chart, Policy, Journal Entry, Posting, external event and Balance retain distinct identities.",
    "WM-ECO-015 owns no Chart membership, hierarchy, rollup or posting eligibility.",
    "Every Ledger Account belongs to exactly one ledger and one effective Chart revision at a posting instant.",
    "Account code equality never proves identity across ledgers or Chart revisions.",
    "Every posting pins the Ledger Account and policy revisions effective on its accounting date.",
    "A Ledger Account may reference at most one WM-ECO-015 backing account per declared context and interval; the reference is never identity.",
    "Each Journal Entry belongs to one ledger and balances only in that ledger's declared currency, scope and tolerance.",
    "Cross-ledger siblings correlate through a pinned external event and divergence reason and never balance, net or plug one another.",
    "Settlement, transaction, functional and presentation currencies remain explicit roles.",
    "Posted entries and lines are immutable; correction appends a linked same-ledger entry.",
    "Hard close permits only a next-period correction or explicitly authorised exception and never silent mutation.",
    "Correcting one sibling neither corrects nor freezes another ledger's sibling.",
    "Closed WM-ECO-017 balances remain immutable; later corrections produce successor balance assertions.",
    "WM-ECO-017 never nets across ledgers and never fuses treasury position with GL balance.",
    "External event identity is not Journal Entry identity and is never a balancing key.",
    "Retired Chart, policy and Ledger Account identifiers and revisions remain resolvable and are never recycled."
  ],
  "holds": [
    "Registry namespace and identifier allocation are pending and no identifier may be guessed.",
    "WM-ECO-015/016/017 ownership contradictions require canonical reconciliation.",
    "Currency roles, balancing scope, tolerance units, CoA-to-ledger cardinality and hard-close policy require frozen audit and canonical adjudication.",
    "Base models remain reviewable drafts; executable fixtures and live verification are pending.",
    "Package is declarative and non-publishable."
  ],
  "candidateRevision": 2,
  "candidateStatus": "provider-reconciled-awaiting-single-frozen-audit",
  "publishable": false,
  "identityConclusion": "Ledger Account is independently mastered under the Chart-of-Accounts lifecycle and cannot profile WM-ECO-015. Identifier remains unassigned pending registry adjudication."
}
```

## PROFILE CANDIDATE

```json
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-FIN-02",
  "name": "Enterprise Financial Event and Multi-Ledger Binding",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": [
    "WM-ECO-015",
    "WM-ECO-016",
    "WM-ECO-017",
    "WM-ECO-008",
    "WM-ECO-009",
    "WM-XCT-014"
  ],
  "constraints": [
    "Profile is correspondence-only and mints no account, chart, policy, ledger, entry, posting, balance, event, invoice or payment identity.",
    "WM-ECO-015 exclusively owns externally serviced Financial Accounts; Ledger Account is never its subtype or profile.",
    "The unassigned Chart of Accounts / Accounting Policy candidate exclusively owns Ledger Account identity and posting eligibility.",
    "WM-ECO-016 exclusively owns ledger-local Journal Entry and Posting occurrence identity.",
    "WM-ECO-017 exclusively owns qualified balance and position assertions.",
    "External events, WM-ECO-008 invoices and WM-ECO-009 payments remain externally mastered correlation references.",
    "Every binding pins source identity plus revision, valid time or as-of time and is append-only with supersession.",
    "Sibling entries share a pinned external-event reference and record divergence reason when amount, timing, account, policy or currency differs.",
    "No profile relation participates in balancing, netting, plugging, tolerance or correction arithmetic.",
    "Each entry balances inside exactly one ledger, declared currency role, scope and tolerance.",
    "Optional Financial Account backing is context- and interval-qualified, at most one, and never Ledger Account identity.",
    "Corrections append same-ledger successor entries and never mutate original entries, lines or closed balances.",
    "Hard-close handling is next-period correction or explicit authorised exception; silent reopen is forbidden.",
    "Correcting one sibling does not mutate, freeze or automatically correct another ledger's sibling.",
    "Profile cannot cascade-delete or mutate any upstream master."
  ],
  "holds": [
    "Chart of Accounts / Accounting Policy has no registry allocation.",
    "Base ownership contradictions and currency/close semantics remain unresolved.",
    "Independent Grok review is reconciled; one frozen audit is pending.",
    "No runtime ID, registry allocation or publication is allowed."
  ],
  "candidateRevision": 2,
  "candidateStatus": "provider-reconciled-awaiting-single-frozen-audit",
  "publishable": false,
  "profileRole": "correspondence-only, non-mastering subject seam"
}
```

## FIXTURES

```json
{
  "format": "vercy-enterprise-allocation-fixtures/v1",
  "candidateName": "Chart of Accounts / Accounting Policy",
  "cases": [
    {
      "id": "statutory-management-divergence",
      "kind": "positive",
      "covers": [
        "I07",
        "I08",
        "I09"
      ],
      "input": "One settlement produces a statutory EUR entry and management USD entry with different accounts and recognition dates.",
      "expect": "Both entries balance independently, share only pinned event correlation and record basis, FX and classification divergence."
    },
    {
      "id": "hard-close-restricted-cash-correction",
      "kind": "positive",
      "covers": [
        "I10",
        "I11",
        "I12",
        "I13"
      ],
      "input": "After the statutory ledger hard-closes, Cash-GL must be reclassified to Restricted-Cash while management is correct.",
      "expect": "A linked statutory correction posts in the earliest permitted later period or under an explicit exception; original entry and closed balance remain immutable; management is unchanged."
    },
    {
      "id": "open-period-correction",
      "kind": "positive",
      "covers": [
        "I10"
      ],
      "input": "A posting error is found while the ledger period remains open.",
      "expect": "A linked reversal or adjustment is appended in the same ledger; original lines are unchanged."
    },
    {
      "id": "chart-successor",
      "kind": "positive",
      "covers": [
        "I03",
        "I04",
        "I05",
        "I16"
      ],
      "input": "Account hierarchy is reorganised for the next fiscal year.",
      "expect": "A successor Chart revision and effective Ledger Accounts preserve predecessor paths and historical interpretation."
    },
    {
      "id": "optional-financial-backing",
      "kind": "positive",
      "covers": [
        "I06"
      ],
      "input": "A statutory cash Ledger Account maps to one bank Financial Account for a declared entity and interval.",
      "expect": "Mapping is stored as context-qualified correspondence and does not merge identities."
    },
    {
      "id": "global-account-code",
      "kind": "negative",
      "covers": [
        "I03",
        "I04"
      ],
      "input": "Code 4000 is treated as globally identical across statutory and management ledgers.",
      "expect": "Rejected because Ledger Account identity is ledger-, Chart-revision- and interval-scoped."
    },
    {
      "id": "raw-financial-account-posting",
      "kind": "negative",
      "covers": [
        "I01",
        "I02"
      ],
      "input": "A Posting targets a WM-ECO-015 bank account directly.",
      "expect": "Rejected; Posting must target a Ledger Account governed by the effective Chart revision."
    },
    {
      "id": "cross-ledger-balance",
      "kind": "negative",
      "covers": [
        "I07",
        "I08"
      ],
      "input": "A statutory debit offsets a management credit to satisfy balancing.",
      "expect": "Rejected because no balancing scope spans ledgers."
    },
    {
      "id": "cross-ledger-tolerance-plug",
      "kind": "negative",
      "covers": [
        "I08"
      ],
      "input": "A statutory residual is plugged into a management entry.",
      "expect": "Rejected; residuals post inside the same ledger under its pinned policy."
    },
    {
      "id": "event-as-entry-identity",
      "kind": "negative",
      "covers": [
        "I15"
      ],
      "input": "The external settlement identifier is reused as the Journal Entry identity in two ledgers.",
      "expect": "Rejected; correlation never replaces ledger-local entry identity."
    },
    {
      "id": "policy-rewrites-entry",
      "kind": "negative",
      "covers": [
        "I05",
        "I10"
      ],
      "input": "A successor accounting policy rewrites prior posted lines.",
      "expect": "Rejected; the new policy is effective-dated and history changes only through linked corrections or restatement."
    },
    {
      "id": "hard-close-silent-reopen",
      "kind": "negative",
      "covers": [
        "I11"
      ],
      "input": "A closed statutory period is silently reopened and the original entry edited.",
      "expect": "Rejected; explicit exception or later-period correction is required."
    },
    {
      "id": "sibling-auto-correction",
      "kind": "negative",
      "covers": [
        "I12"
      ],
      "input": "Correcting the statutory sibling automatically changes management.",
      "expect": "Rejected; correction authority and timing are per ledger."
    },
    {
      "id": "closed-balance-mutation",
      "kind": "negative",
      "covers": [
        "I13",
        "I14"
      ],
      "input": "A correction overwrites the closed-period WM-ECO-017 balance.",
      "expect": "Rejected; closed balance is immutable and later assertions carry new as-of context."
    },
    {
      "id": "treasury-gl-fusion",
      "kind": "negative",
      "covers": [
        "I01",
        "I14"
      ],
      "input": "Bank position and GL balance are stored as one authoritative object.",
      "expect": "Rejected; treasury/custody position and per-ledger GL balance remain distinct."
    },
    {
      "id": "profile-mints-ledger-account",
      "kind": "negative",
      "covers": [
        "I01",
        "I02"
      ],
      "input": "The Enterprise profile creates a Ledger Account key.",
      "expect": "Rejected as stealth mastership."
    },
    {
      "id": "cascade-delete",
      "kind": "negative",
      "covers": [
        "I16"
      ],
      "input": "Deleting a correspondence removes a source entry or account.",
      "expect": "Rejected; profile bindings never cascade-delete masters."
    }
  ]
}
```
