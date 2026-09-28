# Frozen semantic audit request — EM-LND-05

You are the single independent frozen semantic auditor. Use only this prompt. Do not browse, use tools, execute code, invent identifiers, or authorize publication. Audit the reconciled candidate for identity/lifecycle integrity, source mastership, membership and allocation semantics, cost and benefit deduplication, scenario discipline, fixture sufficiency and publication holds. Return PASS or REVISE, then critical findings, required deterministic remediation, fixture gaps, identifier discipline and publication decision. This audit runs exactly once.

## Reconciled profile candidate

```json
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-LND-05",
  "name": "Project, Program and Portfolio Landscape",
  "candidateRevision": 2,
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": [
    {
      "model_id": "WM-ACT-029",
      "registry_id": "vr.wm-act-029",
      "synthesisSha256": "563b0f71214287d6b4e6d4ed7e4e786749b07272494cfd61d8282d288e14dd84"
    },
    {
      "model_id": "WM-ACT-005",
      "registry_id": "vr.wm-act-005",
      "synthesisSha256": "c1104b3d02abd63ae671e3d463be18a591c2ade178464f0f5aa1e3e4f35e0585"
    }
  ],
  "proposedHostBinding": {
    "value": "vr.wm-act-029#profile/project-program-portfolio-landscape",
    "allocationStatus": "not-allocated",
    "note": "proposal only; registry-owner decision required"
  },
  "constructs": {
    "DeliveryLandscape": {
      "kind": "projection-specification",
      "identity": [
        "landscapeId",
        "specVersion"
      ],
      "versionAttributes": [
        "rootSet",
        "membershipRoleSet",
        "fiscalPeriod",
        "costDimension",
        "currency",
        "priceBase",
        "dataDate",
        "scenarioClass"
      ],
      "writes": []
    },
    "DeliveryScope": {
      "kind": "owned-source-scope",
      "ownerByRootKind": {
        "project": "WM-ACT-005",
        "program": "WM-ACT-029",
        "portfolio": "WM-ACT-029"
      },
      "independentIdentity": false
    },
    "DeliveryView": {
      "kind": "generated-artifact",
      "identity": "digest of canonical projection manifest and source pins",
      "lifecycle": [
        "created",
        "retained",
        "tombstoned"
      ],
      "mutable": false,
      "reimportAsMaster": false
    },
    "TrackerAdapterBinding": {
      "kind": "reference-binding",
      "targetModels": [
        "WM-ACT-005",
        "WM-ACT-029"
      ],
      "unresolvedCode": "UNRESOLVED_ADAPTER",
      "ownsDeliveryIdentity": false
    }
  },
  "membership": {
    "owner": "WM-ACT-029",
    "roles": [
      "financial-consolidating",
      "coordination-only",
      "reporting-only"
    ],
    "roleCardinality": "exactly one role per membership assertion",
    "financialUniquenessKey": [
      "projectId",
      "fiscalPeriod",
      "costDimension"
    ],
    "financialUniqueness": "at most one active financial-consolidating membership per uniqueness key",
    "conflictOutcome": "UNRESOLVED_FINANCIAL_PARENT",
    "componentIdentity": "reference-only; component masters remain external"
  },
  "costFact": {
    "owner": "WM-ACT-005",
    "pin": [
      "projectId",
      "baselineId",
      "period",
      "currency",
      "priceBase",
      "dataDate"
    ],
    "deduplicationKey": "the complete pin",
    "viewRule": "deduplicate source facts before applying financial-consolidating shares",
    "viewOwnsCost": false
  },
  "allocationAxes": {
    "product": {
      "relation": "Project-Product",
      "cardinality": "many-to-many",
      "measure": "cost share",
      "shareBound": "0 <= sum(shares) <= 1 per source fact, period and dimension"
    },
    "team": {
      "relation": "Project-Team",
      "cardinality": "many-to-many",
      "measure": "capacity or effort share",
      "shareBound": "0 <= sum(shares) <= 1 per commitment, period and unit"
    },
    "crossAxisAddition": "forbidden",
    "unallocatedRemainder": "explicit"
  },
  "benefitClaims": {
    "master": "external EM-STR-02 benefit/outcome authority",
    "exclusive-attribution": "additive shares per benefit identity, period and measure; total <= 1",
    "contribution": "non-additive enabling claim",
    "plannedForecastVsRealized": "distinct"
  },
  "viewClasses": [
    "authoritative-actuals",
    "baseline",
    "forecast",
    "scenario"
  ],
  "constraints": [
    "The profile is read-only and never creates or edits project, program, portfolio, product, team, resource, cost, benefit or outcome masters.",
    "DeliveryLandscape versions a projection specification only; DeliveryScope remains owned by WM-ACT-005 or WM-ACT-029 and has no third lifecycle.",
    "Every delivery node resolves to an authoritative WM-ACT-005 or WM-ACT-029 identity.",
    "A tracker board, folder, epic tree or vendor project is an adapter only; unresolved adapters receive no cost fact, membership role or benefit claim.",
    "Each WM-ACT-029 membership assertion carries exactly one role from financial-consolidating, coordination-only or reporting-only.",
    "At most one active financial-consolidating membership exists per project, fiscal period and cost dimension; a second is unresolved and yields no financial total.",
    "Different accounting dimensions may each have one consolidating parent but are never silently merged.",
    "Coordination-only and reporting-only memberships contribute no money.",
    "Cost is asserted exactly once by WM-ACT-005 for a complete project, baseline, period, currency, price-base and data-date pin.",
    "Every view deduplicates the complete source cost-fact pin before applying financial-consolidating allocation shares.",
    "Path multiplicity never multiplies a cost, commitment or benefit fact.",
    "Project-Product and Project-Team are many-to-many references, never containment and never independent ledgers.",
    "Product and team shares are separate axes with named measures and units; totals across axes are never added.",
    "Allocation shares total at most one within one source fact, period, dimension and axis; any remainder stays explicit.",
    "Money, effort and capacity retain their source units and are never summed without an explicit conversion rule.",
    "Resource overcommitment is a derived conflict over pinned demand and owner capacity; the landscape never rewrites commitments or resolves the conflict.",
    "Exclusive benefit attribution is additive only within one benefit identity, period and measure and totals at most one.",
    "Contribution claims are non-additive and never converted to exclusive attribution by a view.",
    "Planned or forecast benefit is never represented as realized benefit.",
    "Every generated view declares scenarioClass and dataDate; missing scenarioClass is refused or unknown and never defaults to authoritative actuals.",
    "Forecast and scenario projections never write into source baselines, aggregate actuals or realized benefits.",
    "Generated views are immutable digest-identified artifacts, never overwritten or re-imported as masters.",
    "EM-WRK-04 remains selection and prioritization neighbour; this landscape does not absorb prioritization decisions.",
    "No DeliveryLandscape, DeliveryScope, view, adapter or profile runtime identifier is allocated by this candidate."
  ],
  "holds": [
    "WM-ACT-005 and WM-ACT-029 remain reviewable drafts with publishableCanonical=false and this profile cannot exceed their publication ceiling.",
    "WM-ACT-029 has no approved WM-ACT-005 relation rows in the frozen relation ledger.",
    "Membership roles and the cross-root financial uniqueness key are profile constraints not yet ratified on WM-ACT-029.",
    "Cross-root deduplication scope, allocation dimensions and source mastership require an approved semantic crosswalk.",
    "Programme/program spelling and profile-token normalization remain unresolved on WM-ACT-029.",
    "ISO 21504, PMI and ISO 42010 references are alignments only, not conformance claims.",
    "The proposed host binding is not allocated and requires registry-owner action.",
    "Fixtures are structurally specified but no executable landscape generator exists.",
    "No package conversion, live verification, canonical publication or registry mutation is authorized."
  ]
}
```

## Structured fixtures

```json
{
  "format": "vercy-enterprise-profile-fixtures/v2",
  "contourId": "EM-LND-05",
  "candidateRevision": 2,
  "executionStatus": "not-executed-no-generator",
  "cases": [
    {
      "id": "diamond-deduplicated",
      "kind": "positive",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "project": "P1",
        "portfolioPaths": [
          "X/P1",
          "X/G/P1"
        ],
        "financialRoles": [
          "G/P1"
        ],
        "otherRoles": [
          "X/P1:reporting-only"
        ],
        "costFact": "CF1"
      },
      "expected": {
        "outcome": "view-created",
        "code": "COST_FACT_INCLUDED_ONCE"
      }
    },
    {
      "id": "diamond-dual-financial-parent",
      "kind": "negative",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "project": "P1",
        "financialRoles": [
          "G/P1",
          "X/P1"
        ],
        "sameKey": true
      },
      "expected": {
        "outcome": "refusal-record",
        "code": "UNRESOLVED_FINANCIAL_PARENT"
      }
    },
    {
      "id": "coordination-no-money",
      "kind": "positive",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "membership": "X/P1",
        "role": "coordination-only",
        "costFact": "CF1"
      },
      "expected": {
        "outcome": "view-created",
        "code": "TOPOLOGY_ONLY"
      }
    },
    {
      "id": "reporting-no-money",
      "kind": "positive",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "membership": "X/P1",
        "role": "reporting-only",
        "costFact": "CF1"
      },
      "expected": {
        "outcome": "view-created",
        "code": "TOPOLOGY_ONLY"
      }
    },
    {
      "id": "one-project-two-products",
      "kind": "positive",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "project": "P1",
        "costFact": "CF1",
        "productShares": {
          "A": 0.6,
          "B": 0.4
        }
      },
      "expected": {
        "outcome": "view-created",
        "code": "PRODUCT_SHARES_ONE_FACT"
      }
    },
    {
      "id": "four-teams-effort-axis",
      "kind": "positive",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "project": "P1",
        "teams": [
          "T1",
          "T2",
          "T3",
          "T4"
        ],
        "measure": "FTE",
        "shares": [
          0.2,
          0.3,
          0.3,
          0.2
        ]
      },
      "expected": {
        "outcome": "view-created",
        "code": "TEAM_AXIS_SEPARATE"
      }
    },
    {
      "id": "sum-product-and-team",
      "kind": "negative",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "project": "P1",
        "attempt": "product total + team total"
      },
      "expected": {
        "outcome": "refusal-record",
        "code": "ORTHOGONAL_AXES_NOT_ADDITIVE"
      }
    },
    {
      "id": "product-share-over-one",
      "kind": "negative",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "project": "P1",
        "productShares": {
          "A": 0.7,
          "B": 0.5
        }
      },
      "expected": {
        "outcome": "refusal-record",
        "code": "ALLOCATION_SHARE_EXCEEDS_ONE"
      }
    },
    {
      "id": "explicit-unallocated-remainder",
      "kind": "positive",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "project": "P1",
        "productShares": {
          "A": 0.6,
          "B": 0.3
        },
        "remainder": 0.1
      },
      "expected": {
        "outcome": "view-created",
        "code": "REMAINDER_VISIBLE"
      }
    },
    {
      "id": "team-overcommit",
      "kind": "negative",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "team": "T3",
        "capacity": {
          "value": 1.0,
          "unit": "FTE"
        },
        "demands": [
          {
            "project": "P1",
            "value": 0.8
          },
          {
            "project": "P2",
            "value": 0.5
          }
        ]
      },
      "expected": {
        "outcome": "conflict-record",
        "code": "RESOURCE_OVERCOMMITTED"
      }
    },
    {
      "id": "money-effort-added",
      "kind": "negative",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "attempt": "EUR + FTE"
      },
      "expected": {
        "outcome": "refusal-record",
        "code": "INCOMMENSURATE_MEASURES"
      }
    },
    {
      "id": "exclusive-benefit-valid",
      "kind": "positive",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "benefit": "B1",
        "claims": [
          {
            "project": "P1",
            "share": 0.6
          },
          {
            "project": "P2",
            "share": 0.4
          }
        ],
        "claimClass": "exclusive-attribution"
      },
      "expected": {
        "outcome": "view-created",
        "code": "EXCLUSIVE_ATTRIBUTION_VALID"
      }
    },
    {
      "id": "exclusive-benefit-over-one",
      "kind": "negative",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "benefit": "B1",
        "claims": [
          {
            "project": "P1",
            "share": 0.7
          },
          {
            "project": "P2",
            "share": 0.6
          }
        ],
        "claimClass": "exclusive-attribution"
      },
      "expected": {
        "outcome": "refusal-record",
        "code": "BENEFIT_ATTRIBUTION_EXCEEDS_ONE"
      }
    },
    {
      "id": "contribution-not-summed",
      "kind": "positive",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "benefit": "B1",
        "claimClass": "contribution",
        "contributors": [
          "P1",
          "P2",
          "P3"
        ]
      },
      "expected": {
        "outcome": "view-created",
        "code": "CONTRIBUTION_NON_ADDITIVE"
      }
    },
    {
      "id": "unresolved-tracker",
      "kind": "negative",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "trackerKey": "JIRA-X",
        "binding": null
      },
      "expected": {
        "outcome": "omission-record",
        "code": "UNRESOLVED_ADAPTER"
      }
    },
    {
      "id": "scenario-as-actual",
      "kind": "negative",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "scenarioClass": "scenario",
        "attempt": "write aggregate actuals"
      },
      "expected": {
        "outcome": "refusal-record",
        "code": "SCENARIO_NOT_ACTUAL"
      }
    },
    {
      "id": "missing-scenario-class",
      "kind": "negative",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "scenarioClass": null
      },
      "expected": {
        "outcome": "refusal-record",
        "code": "SCENARIO_CLASS_REQUIRED"
      }
    },
    {
      "id": "view-reimport",
      "kind": "negative",
      "context": {
        "landscapeId": "LANDSCAPE-PLACEHOLDER",
        "specVersion": "SPEC-V2",
        "viewClass": "authoritative-actuals",
        "fiscalPeriod": "2026-Q3",
        "costDimension": "management-book",
        "currency": "EUR",
        "priceBase": "nominal",
        "dataDate": "2026-09-28T00:00:00Z",
        "sourcePins": [
          {
            "sourceId": "WM-ACT-005",
            "version": "VERSION-PLACEHOLDER-005",
            "digest": "DIGEST-PLACEHOLDER-005"
          },
          {
            "sourceId": "WM-ACT-029",
            "version": "VERSION-PLACEHOLDER-029",
            "digest": "DIGEST-PLACEHOLDER-029"
          }
        ]
      },
      "records": {
        "artifact": "VIEW-DIGEST-1",
        "attempt": "create project master"
      },
      "expected": {
        "outcome": "refusal-record",
        "code": "PROJECTION_REIMPORT_FORBIDDEN"
      }
    }
  ]
}
```

## Provider comparison

# EM-LND-05 provider comparison

Claude and Grok independently select **PROFILE** over WM-ACT-005 and WM-ACT-029 and reject a new catalogue or runtime identifier. DeliveryLandscape is a read-only projection specification with generated views. DeliveryScope stays with the owning Project, Program or Portfolio root. A tracker container is an adapter and enters the landscape only through an authoritative binding.

Both providers require component identity to remain external, one source cost fact on WM-ACT-005, cross-path deduplication before allocation, M:N Project–Product and Project–Team references, separate product and team axes, non-additive contribution claims and strict separation of scenario projections from actuals.

Grok strengthens the candidate with a complete cost pin, three explicit membership roles, a uniqueness key per project/fiscal-period/cost-dimension, unresolved outcome for dual consolidating parents, explicit remainders, view classes and an adapter-resolution failure code. Claude adds that the membership assertion remains parent-owned by WM-ACT-029 and resource contention remains owned by the capacity authority.

The reconciled candidate adopts both sets. It does not treat the Grok result as approval of currently held relation rows, and it retains all parent publication holds and non-conformance labels.


## Initial Claude boundary study

# Verdict

**PROFILE.** EM-LND-05 is admitted as a named, read-only **projection profile over WM-ACT-029**, resolving components through WM-ACT-005. No new registry ID. Neither `DeliveryLandscape` nor `DeliveryScope` is admitted as a subject-model type; both are view names, not masters.

The independent-identity test fails on all three limbs. (1) *Identity*: a landscape instance is keyed by view definition + `as_of` + `scenario` + knowledge time — a derived key over existing roots, not an independently mintable identifier. (2) *Lifecycle*: every state change a landscape could undergo is already an appended event in 029's `component-admission-removal-priority-change-successor-and-history` or `programme-sequencing-or-portfolio-selection-prioritization-balancing-and-reallocation`. A landscape has no authorization, no mandate, no closure of its own. (3) *Invariants*: the double-count rule lives in 029's `metric-definition…-and-aggregation` (aggregation and deduplication) and `benefit-owner…-and-attribution-limit`; cost single-source lives in WM-ACT-005's `a-cost-baseline` and `de-actual-cost-to-date`. A landscape enforcing them would duplicate, not add.

`DeliveryScope` fails an additional test: 029 owns `scope-inclusion-exclusion-assumption-constraint-context-and-success` and 005 owns `de-scope-statement` with exclusions and confirmation. A third scope holder creates a second authoritative scope statement inside the same graph.

# Boundary

The landscape owns **nothing**. It owns no membership assertion (029, parent-side, per 005's explicit "must not be duplicated as a child edge here"), no component master, no cost fact, no benefit master, no resource capacity.

It owns only a **viewpoint specification** in the ISO 42010 sense: stakeholder, concerns, admitted model kinds, correspondence rules, and the loss declaration for the projection. A viewpoint is a specification artifact, not an aggregate root. Under Vercy composition/whole-object, 029 already delegates to component masters; the landscape must delegate identically and terminate — it adds one level of read, zero levels of ownership.

Boundary against a tracker container: a Jira/ADO project, board or epic tree is a workspace of a tooling system. Under 005 `f-project-identity`, the master system issues the authoritative identifier; a tracker key is admissible only as `de-alternate-identifier` bound to its issuing system and resolution target. A tracker container that resolves to no WM-ACT-005 authoritative identifier is not a landscape node at all.

# Membership/allocation semantics

**M:N across management views.** 029 places no single-parent constraint on components: N roots may each assert membership over the same project identifier, each with its own admission basis, effective interval, status and authority. This is sufficient for one project sitting simultaneously in a funding portfolio, a coordination program, a product-line view and a geographic view. What 029 does *not* supply is a **membership role discriminator**, and its absence is exactly where duplicate budget enters. The profile must require, on each membership assertion, one of: `financial-consolidating`, `coordination-only`, `reporting-only`.

**Project–Product–Team.** All three edges are M:N and all resolve outward: products to the product master, teams to the resource/organization master via 005 `de-allocation-owner-ref`. The landscape never stores team composition or product definition.

**Shared resource conflict.** Contention is a property of the *resource owner's capacity*, not of any view. It surfaces through 029 `resource-capability-capacity-demand-allocation-utilization-gap-and-conflict` and is arbitrated through 005 `q-resource-contention`. A landscape may display a conflict; it may not declare or resolve one.

**Cost single source.** One cost fact per `(project, baseline version, period, currency, price base, data date)`, held by 005. Every view figure is an allocation share applied to that fact. No view stores a monetary value; no roll-up is persisted.

**Benefit attribution.** Two claim kinds, never mixed: `exclusive-attribution` (share-weighted, additive, shares sum ≤ 1.0 per benefit/period/measure across *all* claiming roots) and `contribution-claim` (non-additive by construction, bounded by 029's declared causal limit, never summed).

# Required profile

A **projection profile**, delivered through 029's existing `project-validate-correct-retain-and-audit` function. It must **not** be added as a value of 029's required program/portfolio discriminator: that discriminator sits inside the artifact identity tuple, and 029 already holds an unresolved supersession rule for profile-unsafe change — adding a third value would be breaking.

V1 candidate fields become **projection parameters**, retaining `candidate-not-normative`: `portfolio_scope` → 029 scope finding reference; `as_of` → the (effective time, knowledge time) pair, mandatory; `priority_policy` → pinned criteria-and-weights version reference; `scenario` → 029 balancing-function scenario code, required and non-null for any non-authoritative view.

Three view classes, mutually exclusive: **authoritative** (no scenario code; bitemporal current-state), **as-of replay** (knowledge time pinned; immutable), **scenario** (scenario code required; may never feed benefit realization, cost actuals or published reporting).

# Invariants

1. A landscape node resolves to an authoritative WM-ACT-005 or WM-ACT-029 identifier; a tracker container is not a project.
2. At most one `financial-consolidating` membership per `(project, fiscal period, cost dimension)` across all roots.
3. No monetary or benefit value is stored on a view; every figure is computed from a source fact plus a declared allocation share.
4. Roll-up deduplicates on the source fact key before summation; path multiplicity never multiplies value.
5. Allocation shares sum to ≤ 1.0 per `(fact, period, dimension)`; orthogonal decompositions (product view, team view) are never summed with each other.
6. Contribution claims are non-additive and carry 029's attribution limit; only exclusive-attribution claims aggregate.
7. Project↔Product and Project↔Team are M:N with no exclusivity; membership is asserted parent-side only.
8. Every published view declares its class, `as_of`, knowledge time and criteria version; a scenario view is never published as authoritative.
9. Resource conflict is recorded against owner capacity, not against the view.

# Scenario walkthrough

**Negative — duplicate budget.** Project P is a direct component of portfolio X and also of program G, itself a component of X; P also appears in a product-line view. Naive traversal returns P's budget three times. Three independent failures: traversal with no role filter (blocked by invariants 2 and 4), no allocation share (invariant 5), and reading budget from the view rather than from 005's cost baseline (invariant 3). With the profile applied, X's figure resolves to one cost fact; G's membership is `coordination-only`; the product-line view is `reporting-only`; the deduplicated roll-up equals one budget.

**Acceptance — one project, two products, four teams.** P delivers to products A and B; teams T1–T4 are allocated through 005 `de-resource-allocation` with quantity, unit, period and owning party. Cost: one fact at P's data date against a named baseline version. Product view allocates it 60/40 — summing to exactly one fact, not a re-measurement. Team view decomposes the same fact by effort share — a second, orthogonal decomposition that must not be added to the product view. Benefits: A's benefit is exclusive-attribution at 0.6; B's a contribution-claim, non-additive, reported separately. T3 is also committed 0.5 FTE to another project in the same period against 0.8 here: capacity exceeded, surfaced as a 029 conflict, arbitrated by the owning party, recorded against capacity. M:N holds throughout; the cost fact is asserted once.

# Gaps and publication holds

- **Inherited holds bind.** WM-ACT-029 is `reviewable-draft`, `publishableCanonical: false`, under a single-provider waiver with Claude and Grok waived; WM-ACT-005 is `reviewable-draft` with ~30 unverified URLs. EM-LND-05 cannot be published above reviewable-draft.
- **Relation rows held.** 029's registry Project parent link and all proposed component relations are on hold with no approved rows. The landscape's entire traversal contract is unverifiable until those rows exist. **This is the hard blocker.**
- **Membership role discriminator is unsourced.** Neither model supplies it, and no source in either pack governs cross-root financial consolidation. Deferred research, not an assertion.
- **Cross-root deduplication scope unconfirmed.** 029's aggregation-and-deduplication element may cover only intra-root aggregation. Confirm before invariant 4 is claimed as reuse rather than extension.
- **Crosswalk incomplete.** Both candidates are `conceptual-candidate`; `published` ≠ independent expertise. Full semantic crosswalk remains a precondition.
- **Spelling normalization.** 029's unresolved programme/program token conflict propagates to any landscape artifact naming; block artifact minting until normalized.
- **No independent review.** This review is a boundary opinion on a frozen dossier, not external provider adjudication.


## Grok independent review

**Verdict.** PROFILE over WM-ACT-005 and WM-ACT-029. No new catalogue or runtime ID. DeliveryLandscape is a read-only projection specification plus generated views. DeliveryScope stays with the owning 005 or 029 root. A tracker container is not a project unless it resolves to an authoritative 005 or 029 identity. Cost is asserted once on the project. This is standards alignment, not a second delivery ledger.

**Identity / lifecycle test.** Source facts: 005 owns project identity, authorized scope, immutable cost/schedule/scope baselines and time-phased cost facts. 029 owns program or portfolio identity, component membership without absorbing component masters, allocation decisions and benefit logic. EM-WRK-01 already states that a tracker container is not a project. ISO 21504 / PMI alignment: a portfolio is a collection of components grouped to meet strategy; a program coordinates related work for benefits not available from any one project; components keep their own identity. ISO 42010 alignment, as on EM-LND-01: a view is not a second system of interest.

- **DeliveryLandscape.** Identity: landscape-id + spec version + root set + view policy (membership roles included, fiscal period, cost dimension, currency, data-date, scenario class). Lifecycle versions the spec. Spec change does not rewrite 005/029 records. Writes: none. Fail-to-new-aggregate if the landscape authors membership, stores a second budget, assigns identity to a tracker folder, or is re-imported as a project or portfolio.

- **DeliveryScope.** On 005: authorized scope of that project. On 029: program or portfolio scope plus the membership set it governs. A view may display the union of scopes for a root; it does not own them. Fail-to-new-aggregate if DeliveryScope becomes a third record kind with its own lifecycle.

- **Tracker container.** A Jira, Azure DevOps or GitHub “project” is an adapter. It enters the landscape only after it binds to a 005 or 029 identity. Unresolved adapter IDs are omitted or flagged `unresolved-adapter`. They receive no cost fact, membership role or benefit claim.

**Membership / allocation semantics.** Design inference from 029 membership plus the card’s anti-double-count invariant, labelled as such.

A project may belong to several 029 roots. Each membership carries exactly one role:

1. `financial-consolidating` — roll-up parent for a named fiscal period and cost dimension. The project’s single cost fact is included once in that root’s financial view after any declared share.
2. `coordination-only` — dependency, sequencing or interface. Visible in the graph; contributes no money.
3. `reporting-only` — dashboard inclusion. No financial roll-up, no coordination authority.

Constraint: at most one financial-consolidating membership per project per fiscal period per cost dimension. A second consolidating edge in the same key is `unresolved`, not a silent double count. Different dimensions (statutory book versus management book) may each have one consolidating parent.

Typical but not hard-coded pattern: program membership consolidates delivery budget; portfolio consolidates the already-deduplicated program view; a direct portfolio→project edge in the same period and dimension is coordination- or reporting-only. The PROFILE enforces uniqueness and refuses naive nested sums; it does not freeze that topology.

Project–Product and Project–Team are M:N references, not containment and not cost ledgers. Allocation *shares* live on those edges. Product shares decompose the single project cost fact on the product axis. Team shares decompose capacity or effort. Shares on one axis should sum to ≤ 1; remainder stays explicit. Product totals and team totals must not be added.

**Cost and benefit rules.** Cost is asserted once on 005 for the pin `(project-id, baseline-id, period, currency, price-base, data-date)`. 029 and the landscape never mint a second cost fact.

Every view: collect membership edges; deduplicate source cost facts by project identity and pin; apply allocation shares only on financial-consolidating memberships for that period and dimension; leave coordination and reporting edges as topology.

Product allocation and team allocation are orthogonal decompositions of the same cost fact. Adding them double-counts. Unallocated remainder on either axis stays visible, in the same spirit as EM-LND-10.

Benefits distinguish two claim kinds that must not be mixed in one sum:

- **Exclusive attribution** — additive shares of one benefit identity; shares across claimants ≤ 1 for a period.
- **Contribution** — non-additive enabling claim; several projects may contribute to one outcome and must not be summed as if exclusive.

EM-STR-02 remains the benefit master. Planned or forecast benefit is not realized benefit.

**Scenario results.**

1. *Portfolio contains a project directly and through a program.* Identify the unique 005 cost fact. Deduplicate by project identity before any share. If both paths are financial-consolidating in the same period and dimension → unresolved, no total. If the program path consolidates and the direct edge is reporting- or coordination-only → include the project once via the program. A view that adds nested references fails the card negative case.

2. *One project, two products, four teams, one cost fact.* 005 holds one assertion. Two product edges carry product shares. Four team edges carry capacity or effort shares and do not split the cost ledger unless a named cost-to-team rule is declared. The view may present a product breakdown or a team breakdown, never their arithmetic sum. Neither product nor team absorbs the project.

3. *A team is overcommitted across projects.* Landscape surfaces a derived conflict: sum of pinned demand versus declared capacity for period and unit, after deduplicating the same commitment fact. Result: overcommit flag, residual (may be negative), contributing project-ids. Landscape does not rewrite 005 commitments or invent a team-level cost fact. Money and effort stay in their own units.

4. *A scenario view is mistaken for authoritative actuals.* Every view pins `scenario-class` ∈ {authoritative-actuals | baseline | forecast | scenario} plus data-date. A scenario or forecast projection cannot be read as actuals. Missing class → refuse or unknown, never default to actuals. Writing a scenario total back onto the 005 baseline or 029 aggregate actuals fails this test and the EM-STR-02 negative case.

**Missing relations / fields** (named constraints on existing models, not new IDs): membership.role; membership.fiscalPeriod and costDimension; allocation.share, allocation.dimension and unallocated remainder; 005 cost-fact pin; benefit claim class {exclusive-attribution | contribution}; view scenario-class and data-date; tracker-adapter binding to 005/029 or `unresolved`.

**Publication blockers.**
- 029 frozen relation ledger has no approved 005 edges; membership-role and uniqueness key are not yet on the published model.
- Financial-consolidating uniqueness is a PROFILE constraint, not an existing 029 invariant.
- No fixtures for the diamond path, product-share + team-share non-additivity, team overcommit, or scenario-class refusal.
- 005 and 029 remain reviewable drafts with source-pin, ISO-text and second-provider holds. 029 has no approved project relation rows.
- EM-WRK-04 stays the selection-subject neighbor; this landscape must not absorb prioritization.
- Alignments to PMI, ISO 21504 and ISO 42010 are alignments only.
- Do not invent a DeliveryLandscape or DeliveryScope runtime identifier.

## Frozen dossier

```json
{
  "contour": {
    "id": "EM-LND-05",
    "name": "Ландшафт проектов, программ и портфелей",
    "domain": "LND",
    "kind": "landscape",
    "wave": "W1",
    "scope": "Состав управленческих инициатив, зависимости, ресурсы и ожидаемые выгоды через самостоятельные объекты.",
    "candidate_types": [
      "DeliveryLandscape",
      "DeliveryScope"
    ],
    "specific_questions": [
      "Как один проект участвует в нескольких управленческих срезах?",
      "Где общий ресурс создаёт конфликт?",
      "Как исключить двойной счёт выгод?"
    ],
    "proposed_invariants": [
      "Контейнер трекера не проект",
      "Project-Product-Team допускает M:N",
      "Суммирование требует правила аллокации"
    ],
    "negative_case": "Портфель равен сумме бюджетов всех вложенных ссылок с повторами.",
    "acceptance_scenario": "Один проект, два продукта и четыре команды сохраняют M:N и один факт затрат.",
    "comparison_tracks": [
      "Vercy composition и whole-object: отдельный объект ландшафта и делегирование",
      "ArchiMate/ISO 42010: виды, вопросы и правила представления",
      "Сравнить предметные модели участников и практическую сборку разрешённого контекста"
    ],
    "vercy_candidates": [
      {
        "model_id": "WM-ACT-029",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "boundary-reviewed",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      },
      {
        "model_id": "WM-ACT-005",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "boundary-reviewed",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      }
    ],
    "candidate_properties_from_v1": [
      {
        "predecessor": "LND-05",
        "fields": [
          {
            "name": "portfolio_scope",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "as_of",
            "value_type": "datetime",
            "status": "candidate-not-normative"
          },
          {
            "name": "priority_policy",
            "value_type": "text",
            "status": "candidate-not-normative"
          },
          {
            "name": "scenario",
            "value_type": "code",
            "status": "candidate-not-normative"
          }
        ]
      }
    ],
    "suggested_owner": "Куратор мета-моделей Vercy",
    "candidate_master_systems": "Реестр моделей, sources.yaml, vercy.lock, политики",
    "related_research_contours": [],
    "blocking_decisions": [
      "Установить границу и решение reuse/extend/new по действующим спецификациям.",
      "Подтвердить semantic crosswalk, права и source mastership.",
      "Выбрать immutable refs; провести проверки fixtures до заявления о публикационной готовности."
    ]
  },
  "registry_policy": {
    "reserved_candidates": [
      "WM-ACT-029",
      "WM-ACT-005"
    ],
    "rule": "No new ID without independent identity/lifecycle and registry allocation."
  },
  "models": {
    "program_portfolio": {
      "publication": {
        "status": "published",
        "adjudicationStatus": "reviewable-draft",
        "publishableCanonical": false,
        "generatedAt": "2026-09-06T05:47:45Z",
        "synthesisSha256": "563b0f71214287d6b4e6d4ed7e4e786749b07272494cfd61d8282d288e14dd84",
        "providerMode": "single-provider-waiver",
        "providers": [
          "Codex"
        ],
        "waivedProviders": [
          "Claude",
          "Grok"
        ]
      },
      "model": {
        "registry_id": "vr.wm-act-029",
        "model_id": "WM-ACT-029",
        "name": "Program / Portfolio",
        "entry_kind": "aggregate",
        "purpose": "Represent a governed program or portfolio that coordinates or selects components to advance strategy and realize outcomes or value while preserving the identity and lifecycle of every component master.",
        "scope_statement": "Owns the program-or-portfolio root and lineage, required profile discriminator, mandate and governance, strategy alignment, aggregate scope, component membership and dependencies, outcome and benefit logic, roadmaps or horizons, aggregate assignments and allocation decisions, prioritization or sequencing, lifecycle, metrics and aggregate evaluation, projections, access and retention. Party, strategy, objective, project, program-as-component, product, operation, benefit, resource, budget, contract, risk, issue, decision, observation, dataset, policy and generic audit masters remain external.",
        "in_scope": [
          "Program or portfolio identity, profile, mandate, governance, strategy alignment, scope, component membership, dependencies and decision rights",
          "Objectives, outputs, capabilities, outcomes, benefits, disbenefits, impacts, roadmaps, tranches or horizons, transition, resources, funding references, prioritization, balancing and controls",
          "Authorization, component changes, start, pause, rebalance, termination, closure, metrics, observations, evaluation, learning, interoperability, access, retention and agent operations"
        ],
        "out_of_scope": [
          "Party, strategy, objective, project, product, operation, benefit, resource, budget, contract, risk, issue, decision, observation, dataset, policy or audit-log master lifecycle",
          "Treating Program and Portfolio as synonyms, admitting an instance without a profile, or inferring outcome, benefit or causal impact from completion, spending or output alone",
          "Implementing scheduling, portfolio optimization, financial accounting, procurement, workforce management, risk engines, analytics platforms or universal legal compliance and claiming full ISO conformance from public abstracts"
        ],
        "boundary_notes": [
          {
            "neighbor": "Program versus Portfolio",
            "distinction": "A program coordinates related components to deliver outcomes and realize benefits; a portfolio selects, prioritizes and balances investments aligned to strategy, and components need not be related. The root is shared only under a required profile and profile-specific rules.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-003",
              "SRC-006",
              "SRC-013"
            ]
          },
          {
            "neighbor": "Project / Component / Operation / Product",
            "distinction": "The aggregate owns membership and coordination or selection assertions, while each external component keeps its own purpose, owner, lifecycle, plan, resources and evidence.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-003",
              "SRC-005"
            ]
          },
          {
            "neighbor": "Strategy / Objective / Policy",
            "distinction": "The aggregate records versioned alignment and contribution claims; authoritative strategy, objective and policy masters remain external.",
            "source_refs": [
              "SRC-001",
              "SRC-003",
              "SRC-006",
              "SRC-009"
            ]
          },
          {
            "neighbor": "Outcome / Benefit / Disbenefit / Impact",
            "distinction": "The aggregate owns its results logic and realization plan, while observed results and benefit masters remain source-qualified and completion does not establish causation.",
            "source_refs": [
              "SRC-007",
              "SRC-008",
              "SRC-009",
              "SRC-011"
            ]
          },
          {
            "neighbor": "Finance / Resource / Risk / Decision / Observation",
            "distinction": "The aggregate owns scoped assignments, rankings, allocations, control and evaluation views; source systems retain authoritative transactions, capacities, risks, decisions and observations.",
            "source_refs": [
              "SRC-004",
              "SRC-006",
              "SRC-010",
              "SRC-011"
            ]
          }
        ]
      },
      "selected_findings": [
        {
          "bundle": {
            "id": "identity-profile-mandate-and-governance",
            "name": "Identity, profile, mandate and governance",
            "description": "Defines the aggregate root and the authority under which it is governed."
          },
          "layer": {
            "id": "profile-definition-and-identity",
            "name": "Profile definition and identity",
            "description": "Pins the kind, identity, version and source lineage of the aggregate."
          },
          "finding": {
            "id": "program-or-portfolio-definition-profile-and-neighbor-boundary",
            "name": "Program or portfolio definition, profile and neighbor boundary",
            "description": "Required profile discriminator, inclusion and exclusion tests, lifecycle vocabulary and distinctions from project, operation, product, campaign and strategy masters.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-003",
              "SRC-005",
              "SRC-013"
            ],
            "questions": [
              {
                "id": "program-or-portfolio-definition-profile-and-neighbor-boundary-q01",
                "text": "What identities, types, roles, scope, versions and explicit values define program or portfolio definition, profile and neighbor boundary?",
                "kind": "classification",
                "answer_data": [
                  "identifiers and classifications",
                  "roles and scope",
                  "versions and validity",
                  "values and explicit unknowns"
                ]
              },
              {
                "id": "program-or-portfolio-definition-profile-and-neighbor-boundary-q02",
                "text": "Which authority, source, method, evidence, event time and knowledge time support program or portfolio definition, profile and neighbor boundary?",
                "kind": "provenance",
                "answer_data": [
                  "authority",
                  "source and method",
                  "supporting and contradicting evidence",
                  "event and knowledge time",
                  "confidence and uncertainty"
                ]
              },
              {
                "id": "program-or-portfolio-definition-profile-and-neighbor-boundary-q03",
                "text": "How is program or portfolio definition, profile and neighbor boundary validated, accessed, changed, contested, corrected and retained?",
                "kind": "validation",
                "answer_data": [
                  "validation and profile rules",
                  "access and disclosure",
                  "change and dispute",
                  "lineage",
                  "retention and disposition"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "program-or-portfolio-definition-profile-and-neighbor-boundary-data",
                "name": "Program or portfolio definition, profile and neighbor boundary data",
                "description": "Structured programme or portfolio data for program or portfolio definition, profile and neighbor boundary.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-002",
                  "SRC-003",
                  "SRC-005",
                  "SRC-013"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "program-or-portfolio-definition-profile-and-neighbor-boundary-record",
                "name": "Program or portfolio definition, profile and neighbor boundary record",
                "description": "Versioned evidence-bearing program or portfolio record for program or portfolio definition, profile and neighbor boundary with authority, time, provenance and access marking.",
                "media_or_form": [
                  "logical program or portfolio assertion",
                  "plan, assignment, decision, event, observation or evidence reference"
                ],
                "serial": true,
                "identity_strategy": "Aggregate identifier plus program-or-portfolio profile plus program-or-portfolio-definition-profile-and-neighbor-boundary assertion, artifact or event identifier; name, date, timestamp and digest never identify the aggregate alone.",
                "source_refs": [
                  "SRC-001",
                  "SRC-002",
                  "SRC-003",
                  "SRC-005",
                  "SRC-013"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "identity-profile-mandate-and-governance",
            "name": "Identity, profile, mandate and governance",
            "description": "Defines the aggregate root and the authority under which it is governed."
          },
          "layer": {
            "id": "profile-definition-and-identity",
            "name": "Profile definition and identity",
            "description": "Pins the kind, identity, version and source lineage of the aggregate."
          },
          "finding": {
            "id": "aggregate-identifier-name-alias-version-source-and-lineage",
            "name": "Aggregate identifier, name, alias, version, source and lineage",
            "description": "Authoritative identifier, governed names and aliases, profile and schema versions, source system, predecessor, successor and duplicate assertions.",
            "source_refs": [
              "SRC-001",
              "SRC-010"
            ],
            "questions": [
              {
                "id": "aggregate-identifier-name-alias-version-source-and-lineage-q01",
                "text": "What identities, types, roles, scope, versions and explicit values define aggregate identifier, name, alias, version, source and lineage?",
                "kind": "identity",
                "answer_data": [
                  "identifiers and classifications",
                  "roles and scope",
                  "versions and validity",
                  "values and explicit unknowns"
                ]
              },
              {
                "id": "aggregate-identifier-name-alias-version-source-and-lineage-q02",
                "text": "Which authority, source, method, evidence, event time and knowledge time support aggregate identifier, name, alias, version, source and lineage?",
                "kind": "provenance",
                "answer_data": [
                  "authority",
                  "source and method",
                  "supporting and contradicting evidence",
                  "event and knowledge time",
                  "confidence and uncertainty"
                ]
              },
              {
                "id": "aggregate-identifier-name-alias-version-source-and-lineage-q03",
                "text": "How is aggregate identifier, name, alias, version, source and lineage validated, accessed, changed, contested, corrected and retained?",
                "kind": "validation",
                "answer_data": [
                  "validation and profile rules",
                  "access and disclosure",
                  "change and dispute",
                  "lineage",
                  "retention and disposition"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "aggregate-identifier-name-alias-version-source-and-lineage-data",
                "name": "Aggregate identifier, name, alias, version, source and lineage data",
                "description": "Structured programme or portfolio data for aggregate identifier, name, alias, version, source and lineage.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-010"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "aggregate-identifier-name-alias-version-source-and-lineage-record",
                "name": "Aggregate identifier, name, alias, version, source and lineage record",
                "description": "Versioned evidence-bearing program or portfolio record for aggregate identifier, name, alias, version, source and lineage with authority, time, provenance and access marking.",
                "media_or_form": [
                  "logical program or portfolio assertion",
                  "plan, assignment, decision, event, observation or evidence reference"
                ],
                "serial": true,
                "identity_strategy": "Aggregate identifier plus program-or-portfolio profile plus aggregate-identifier-name-alias-version-source-and-lineage assertion, artifact or event identifier; name, date, timestamp and digest never identify the aggregate alone.",
                "source_refs": [
                  "SRC-001",
                  "SRC-010"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "strategy-scope-components-and-dependencies",
            "name": "Strategy, scope, components and dependencies",
            "description": "Connects the governed aggregate to strategy and to the components it coordinates or selects."
          },
          "layer": {
            "id": "strategy-objectives-and-scope",
            "name": "Strategy, objectives and scope",
            "description": "Defines strategic purpose, success conditions and the controlled boundary."
          },
          "finding": {
            "id": "strategy-policy-need-objective-alignment-thesis-and-priority",
            "name": "Strategy, policy, need, objective, alignment, thesis and priority",
            "description": "External strategy and policy references, evidenced need, objective hierarchy, alignment assertion, investment thesis, priority and trade-off.",
            "source_refs": [
              "SRC-002",
              "SRC-003",
              "SRC-006",
              "SRC-009"
            ],
            "questions": [
              {
                "id": "strategy-policy-need-objective-alignment-thesis-and-priority-q01",
                "text": "What identities, types, roles, scope, versions and explicit values define strategy, policy, need, objective, alignment, thesis and priority?",
                "kind": "requirement",
                "answer_data": [
                  "identifiers and classifications",
                  "roles and scope",
                  "versions and validity",
                  "values and explicit unknowns"
                ]
              },
              {
                "id": "strategy-policy-need-objective-alignment-thesis-and-priority-q02",
                "text": "Which authority, source, method, evidence, event time and knowledge time support strategy, policy, need, objective, alignment, thesis and priority?",
                "kind": "provenance",
                "answer_data": [
                  "authority",
                  "source and method",
                  "supporting and contradicting evidence",
                  "event and knowledge time",
                  "confidence and uncertainty"
                ]
              },
              {
                "id": "strategy-policy-need-objective-alignment-thesis-and-priority-q03",
                "text": "How is strategy, policy, need, objective, alignment, thesis and priority validated, accessed, changed, contested, corrected and retained?",
                "kind": "validation",
                "answer_data": [
                  "validation and profile rules",
                  "access and disclosure",
                  "change and dispute",
                  "lineage",
                  "retention and disposition"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "strategy-policy-need-objective-alignment-thesis-and-priority-data",
                "name": "Strategy, policy, need, objective, alignment, thesis and priority data",
                "description": "Structured programme or portfolio data for strategy, policy, need, objective, alignment, thesis and priority.",
                "value_kind": "collection",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-003",
                  "SRC-006",
                  "SRC-009"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "strategy-policy-need-objective-alignment-thesis-and-priority-record",
                "name": "Strategy, policy, need, objective, alignment, thesis and priority record",
                "description": "Versioned evidence-bearing program or portfolio record for strategy, policy, need, objective, alignment, thesis and priority with authority, time, provenance and access marking.",
                "media_or_form": [
                  "logical program or portfolio assertion",
                  "plan, assignment, decision, event, observation or evidence reference"
                ],
                "serial": true,
                "identity_strategy": "Aggregate identifier plus program-or-portfolio profile plus strategy-policy-need-objective-alignment-thesis-and-priority assertion, artifact or event identifier; name, date, timestamp and digest never identify the aggregate alone.",
                "source_refs": [
                  "SRC-002",
                  "SRC-003",
                  "SRC-006",
                  "SRC-009"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "strategy-scope-components-and-dependencies",
            "name": "Strategy, scope, components and dependencies",
            "description": "Connects the governed aggregate to strategy and to the components it coordinates or selects."
          },
          "layer": {
            "id": "strategy-objectives-and-scope",
            "name": "Strategy, objectives and scope",
            "description": "Defines strategic purpose, success conditions and the controlled boundary."
          },
          "finding": {
            "id": "scope-inclusion-exclusion-assumption-constraint-context-and-success",
            "name": "Scope, inclusion, exclusion, assumption, constraint, context and success",
            "description": "Declared scope, boundary criteria, assumptions, constraints, operating context, acceptance tests and success conditions.",
            "source_refs": [
              "SRC-002",
              "SRC-003",
              "SRC-006"
            ],
            "questions": [
              {
                "id": "scope-inclusion-exclusion-assumption-constraint-context-and-success-q01",
                "text": "What identities, types, roles, scope, versions and explicit values define scope, inclusion, exclusion, assumption, constraint, context and success?",
                "kind": "definition",
                "answer_data": [
                  "identifiers and classifications",
                  "roles and scope",
                  "versions and validity",
                  "values and explicit unknowns"
                ]
              },
              {
                "id": "scope-inclusion-exclusion-assumption-constraint-context-and-success-q02",
                "text": "Which authority, source, method, evidence, event time and knowledge time support scope, inclusion, exclusion, assumption, constraint, context and success?",
                "kind": "provenance",
                "answer_data": [
                  "authority",
                  "source and method",
                  "supporting and contradicting evidence",
                  "event and knowledge time",
                  "confidence and uncertainty"
                ]
              },
              {
                "id": "scope-inclusion-exclusion-assumption-constraint-context-and-success-q03",
                "text": "How is scope, inclusion, exclusion, assumption, constraint, context and success validated, accessed, changed, contested, corrected and retained?",
                "kind": "validation",
                "answer_data": [
                  "validation and profile rules",
                  "access and disclosure",
                  "change and dispute",
                  "lineage",
                  "retention and disposition"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "scope-inclusion-exclusion-assumption-constraint-context-and-success-data",
                "name": "Scope, inclusion, exclusion, assumption, constraint, context and success data",
                "description": "Structured programme or portfolio data for scope, inclusion, exclusion, assumption, constraint, context and success.",
                "value_kind": "collection",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-003",
                  "SRC-006"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "scope-inclusion-exclusion-assumption-constraint-context-and-success-record",
                "name": "Scope, inclusion, exclusion, assumption, constraint, context and success record",
                "description": "Versioned evidence-bearing program or portfolio record for scope, inclusion, exclusion, assumption, constraint, context and success with authority, time, provenance and access marking.",
                "media_or_form": [
                  "logical program or portfolio assertion",
                  "plan, assignment, decision, event, observation or evidence reference"
                ],
                "serial": true,
                "identity_strategy": "Aggregate identifier plus program-or-portfolio profile plus scope-inclusion-exclusion-assumption-constraint-context-and-success assertion, artifact or event identifier; name, date, timestamp and digest never identify the aggregate alone.",
                "source_refs": [
                  "SRC-002",
                  "SRC-003",
                  "SRC-006"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "strategy-scope-components-and-dependencies",
            "name": "Strategy, scope, components and dependencies",
            "description": "Connects the governed aggregate to strategy and to the components it coordinates or selects."
          },
          "layer": {
            "id": "component-membership-and-dependency",
            "name": "Component membership and dependency",
            "description": "Represents membership without absorbing project, programme, product or operational masters."
          },
          "finding": {
            "id": "component-identity-type-membership-basis-status-and-accountability",
            "name": "Component identity, type, membership, basis, status and accountability",
            "description": "External component ID and type, membership assertion, admission basis, effective interval, status, component owner and source authority.",
            "source_refs": [
              "SRC-002",
              "SRC-003",
              "SRC-005",
              "SRC-010"
            ],
            "questions": [
              {
                "id": "component-identity-type-membership-basis-status-and-accountability-q01",
                "text": "What identities, types, roles, scope, versions and explicit values define component identity, type, membership, basis, status and accountability?",
                "kind": "composition",
                "answer_data": [
                  "identifiers and classifications",
                  "roles and scope",
                  "versions and validity",
                  "values and explicit unknowns"
                ]
              },
              {
                "id": "component-identity-type-membership-basis-status-and-accountability-q02",
                "text": "Which authority, source, method, evidence, event time and knowledge time support component identity, type, membership, basis, status and accountability?",
                "kind": "provenance",
                "answer_data": [
                  "authority",
                  "source and method",
                  "supporting and contradicting evidence",
                  "event and knowledge time",
                  "confidence and uncertainty"
                ]
              },
              {
                "id": "component-identity-type-membership-basis-status-and-accountability-q03",
                "text": "How is component identity, type, membership, basis, status and accountability validated, accessed, changed, contested, corrected and retained?",
                "kind": "validation",
                "answer_data": [
                  "validation and profile rules",
                  "access and disclosure",
                  "change and dispute",
                  "lineage",
                  "retention and disposition"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "component-identity-type-membership-basis-status-and-accountability-data",
                "name": "Component identity, type, membership, basis, status and accountability data",
                "description": "Structured programme or portfolio data for component identity, type, membership, basis, status and accountability.",
                "value_kind": "collection",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-003",
                  "SRC-005",
                  "SRC-010"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "component-identity-type-membership-basis-status-and-accountability-record",
                "name": "Component identity, type, membership, basis, status and accountability record",
                "description": "Versioned evidence-bearing program or portfolio record for component identity, type, membership, basis, status and accountability with authority, time, provenance and access marking.",
                "media_or_form": [
                  "logical program or portfolio assertion",
                  "plan, assignment, decision, event, observation or evidence reference"
                ],
                "serial": true,
                "identity_strategy": "Aggregate identifier plus program-or-portfolio profile plus component-identity-type-membership-basis-status-and-accountability assertion, artifact or event identifier; name, date, timestamp and digest never identify the aggregate alone.",
                "source_refs": [
                  "SRC-002",
                  "SRC-003",
                  "SRC-005",
                  "SRC-010"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "strategy-scope-components-and-dependencies",
            "name": "Strategy, scope, components and dependencies",
            "description": "Connects the governed aggregate to strategy and to the components it coordinates or selects."
          },
          "layer": {
            "id": "component-membership-and-dependency",
            "name": "Component membership and dependency",
            "description": "Represents membership without absorbing project, programme, product or operational masters."
          },
          "finding": {
            "id": "dependency-interface-shared-change-sequencing-conflict-and-external-relation",
            "name": "Dependency, interface, shared change, sequencing, conflict and external relation",
            "description": "Typed component dependencies, interfaces, shared capabilities, change coupling, sequencing, conflicts, assumptions and external relationships.",
            "source_refs": [
              "SRC-002",
              "SRC-003",
              "SRC-006"
            ],
            "questions": [
              {
                "id": "dependency-interface-shared-change-sequencing-conflict-and-external-relation-q01",
                "text": "What identities, types, roles, scope, versions and explicit values define dependency, interface, shared change, sequencing, conflict and external relation?",
                "kind": "relationship",
                "answer_data": [
                  "identifiers and classifications",
                  "roles and scope",
                  "versions and validity",
                  "values and explicit unknowns"
                ]
              },
              {
                "id": "dependency-interface-shared-change-sequencing-conflict-and-external-relation-q02",
                "text": "Which authority, source, method, evidence, event time and knowledge time support dependency, interface, shared change, sequencing, conflict and external relation?",
                "kind": "provenance",
                "answer_data": [
                  "authority",
                  "source and method",
                  "supporting and contradicting evidence",
                  "event and knowledge time",
                  "confidence and uncertainty"
                ]
              },
              {
                "id": "dependency-interface-shared-change-sequencing-conflict-and-external-relation-q03",
                "text": "How is dependency, interface, shared change, sequencing, conflict and external relation validated, accessed, changed, contested, corrected and retained?",
                "kind": "validation",
                "answer_data": [
                  "validation and profile rules",
                  "access and disclosure",
                  "change and dispute",
                  "lineage",
                  "retention and disposition"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "dependency-interface-shared-change-sequencing-conflict-and-external-relation-data",
                "name": "Dependency, interface, shared change, sequencing, conflict and external relation data",
                "description": "Structured programme or portfolio data for dependency, interface, shared change, sequencing, conflict and external relation.",
                "value_kind": "collection",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-003",
                  "SRC-006"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "dependency-interface-shared-change-sequencing-conflict-and-external-relation-record",
                "name": "Dependency, interface, shared change, sequencing, conflict and external relation record",
                "description": "Versioned evidence-bearing program or portfolio record for dependency, interface, shared change, sequencing, conflict and external relation with authority, time, provenance and access marking.",
                "media_or_form": [
                  "logical program or portfolio assertion",
                  "plan, assignment, decision, event, observation or evidence reference"
                ],
                "serial": true,
                "identity_strategy": "Aggregate identifier plus program-or-portfolio profile plus dependency-interface-shared-change-sequencing-conflict-and-external-relation assertion, artifact or event identifier; name, date, timestamp and digest never identify the aggregate alone.",
                "source_refs": [
                  "SRC-002",
                  "SRC-003",
                  "SRC-006"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "outcomes-benefits-roadmaps-and-transition",
            "name": "Outcomes, benefits, roadmaps and transition",
            "description": "Models intended change and how it is expected to become operational and produce measurable value."
          },
          "layer": {
            "id": "results-chain-and-benefit-realization",
            "name": "Results chain and benefit realization",
            "description": "Defines the change logic and benefit ownership with measurable evidence."
          },
          "finding": {
            "id": "input-activity-output-capability-outcome-benefit-disbenefit-impact-and-causal-link",
            "name": "Input, activity, output, capability, outcome, benefit, disbenefit, impact and causal link",
            "description": "Typed results-chain nodes and links with intended or unintended direction, affected stakeholder, assumptions, dependencies, evidence and uncertainty.",
            "source_refs": [
              "SRC-007",
              "SRC-008",
              "SRC-009"
            ],
            "questions": [
              {
                "id": "input-activity-output-capability-outcome-benefit-disbenefit-impact-and-causal-link-q01",
                "text": "What identities, types, roles, scope, versions and explicit values define input, activity, output, capability, outcome, benefit, disbenefit, impact and causal link?",
                "kind": "relationship",
                "answer_data": [
                  "identifiers and classifications",
                  "roles and scope",
                  "versions and validity",
                  "values and explicit unknowns"
                ]
              },
              {
                "id": "input-activity-output-capability-outcome-benefit-disbenefit-impact-and-causal-link-q02",
                "text": "Which authority, source, method, evidence, event time and knowledge time support input, activity, output, capability, outcome, benefit, disbenefit, impact and causal link?",
                "kind": "provenance",
                "answer_data": [
                  "authority",
                  "source and method",
                  "supporting and contradicting evidence",
                  "event and knowledge time",
                  "confidence and uncertainty"
                ]
              },
              {
                "id": "input-activity-output-capability-outcome-benefit-disbenefit-impact-and-causal-link-q03",
                "text": "How is input, activity, output, capability, outcome, benefit, disbenefit, impact and causal link validated, accessed, changed, contested, corrected and retained?",
                "kind": "validation",
                "answer_data": [
                  "validation and profile rules",
                  "access and disclosure",
                  "change and dispute",
                  "lineage",
                  "retention and disposition"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "input-activity-output-capability-outcome-benefit-disbenefit-impact-and-causal-link-data",
                "name": "Input, activity, output, capability, outcome, benefit, disbenefit, impact and causal link data",
                "description": "Structured programme or portfolio data for input, activity, output, capability, outcome, benefit, disbenefit, impact and causal link.",
                "value_kind": "collection",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-007",
                  "SRC-008",
                  "SRC-009"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "input-activity-output-capability-outcome-benefit-disbenefit-impact-and-causal-link-record",
                "name": "Input, activity, output, capability, outcome, benefit, disbenefit, impact and causal link record",
                "description": "Versioned evidence-bearing program or portfolio record for input, activity, output, capability, outcome, benefit, disbenefit, impact and causal link with authority, time, provenance and access marking.",
                "media_or_form": [
                  "logical program or portfolio assertion",
                  "plan, assignment, decision, event, observation or evidence reference"
                ],
                "serial": true,
                "identity_strategy": "Aggregate identifier plus program-or-portfolio profile plus input-activity-output-capability-outcome-benefit-disbenefit-impact-and-causal-link assertion, artifact or event identifier; name, date, timestamp and digest never identify the aggregate alone.",
                "source_refs": [
                  "SRC-007",
                  "SRC-008",
                  "SRC-009"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "outcomes-benefits-roadmaps-and-transition",
            "name": "Outcomes, benefits, roadmaps and transition",
            "description": "Models intended change and how it is expected to become operational and produce measurable value."
          },
          "layer": {
            "id": "results-chain-and-benefit-realization",
            "name": "Results chain and benefit realization",
            "description": "Defines the change logic and benefit ownership with measurable evidence."
          },
          "finding": {
            "id": "benefit-owner-baseline-target-indicator-realization-plan-and-attribution-limit",
            "name": "Benefit owner, baseline, target, indicator, realization plan and attribution limit",
            "description": "Benefit or disbenefit owner, baseline, target, indicator, realization activity, forecast and actual period, method, contribution claim and causal limit.",
            "source_refs": [
              "SRC-007",
              "SRC-008",
              "SRC-009",
              "SRC-011"
            ],
            "questions": [
              {
                "id": "benefit-owner-baseline-target-indicator-realization-plan-and-attribution-limit-q01",
                "text": "What identities, types, roles, scope, versions and explicit values define benefit owner, baseline, target, indicator, realization plan and attribution limit?",
                "kind": "measurement",
                "answer_data": [
                  "identifiers and classifications",
                  "roles and scope",
                  "versions and validity",
                  "values and explicit unknowns"
                ]
              },
              {
                "id": "benefit-owner-baseline-target-indicator-realization-plan-and-attribution-limit-q02",
                "text": "Which authority, source, method, evidence, event time and knowledge time support benefit owner, baseline, target, indicator, realization plan and attribution limit?",
                "kind": "provenance",
                "answer_data": [
                  "authority",
                  "source and method",
                  "supporting and contradicting evidence",
                  "event and knowledge time",
                  "confidence and uncertainty"
                ]
              },
              {
                "id": "benefit-owner-baseline-target-indicator-realization-plan-and-attribution-limit-q03",
                "text": "How is benefit owner, baseline, target, indicator, realization plan and attribution limit validated, accessed, changed, contested, corrected and retained?",
                "kind": "validation",
                "answer_data": [
                  "validation and profile rules",
                  "access and disclosure",
                  "change and dispute",
                  "lineage",
                  "retention and disposition"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "benefit-owner-baseline-target-indicator-realization-plan-and-attribution-limit-data",
                "name": "Benefit owner, baseline, target, indicator, realization plan and attribution limit data",
                "description": "Structured programme or portfolio data for benefit owner, baseline, target, indicator, realization plan and attribution limit.",
                "value_kind": "collection",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-007",
                  "SRC-008",
                  "SRC-009",
                  "SRC-011"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "benefit-owner-baseline-target-indicator-realization-plan-and-attribution-limit-record",
                "name": "Benefit owner, baseline, target, indicator, realization plan and attribution limit record",
                "description": "Versioned evidence-bearing program or portfolio record for benefit owner, baseline, target, indicator, realization plan and attribution limit with authority, time, provenance and access marking.",
                "media_or_form": [
                  "logical program or portfolio assertion",
                  "plan, assignment, decision, event, observation or evidence reference"
                ],
                "serial": true,
                "identity_strategy": "Aggregate identifier plus program-or-portfolio profile plus benefit-owner-baseline-target-indicator-realization-plan-and-attribution-limit assertion, artifact or event identifier; name, date, timestamp and digest never identify the aggregate alone.",
                "source_refs": [
                  "SRC-007",
                  "SRC-008",
                  "SRC-009",
                  "SRC-011"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "investment-resources-prioritization-and-control",
            "name": "Investment, resources, prioritization and control",
            "description": "Governs allocation decisions and the constraints that affect delivery and value."
          },
          "layer": {
            "id": "investment-funding-and-capacity",
            "name": "Investment, funding and capacity",
            "description": "References money and capacity without replacing their source systems."
          },
          "finding": {
            "id": "funding-budget-investment-cost-forecast-actual-commitment-and-value-reference",
            "name": "Funding, budget, investment, cost, forecast, actual, commitment and value reference",
            "description": "Currency-qualified approved envelope and external funding, budget, contract, commitment, cost, forecast, actual and value references with valuation basis.",
            "source_refs": [
              "SRC-003",
              "SRC-006"
            ],
            "questions": [
              {
                "id": "funding-budget-investment-cost-forecast-actual-commitment-and-value-reference-q01",
                "text": "What identities, types, roles, scope, versions and explicit values define funding, budget, investment, cost, forecast, actual, commitment and value reference?",
                "kind": "measurement",
                "answer_data": [
                  "identifiers and classifications",
                  "roles and scope",
                  "versions and validity",
                  "values and explicit unknowns"
                ]
              },
              {
                "id": "funding-budget-investment-cost-forecast-actual-commitment-and-value-reference-q02",
                "text": "Which authority, source, method, evidence, event time and knowledge time support funding, budget, investment, cost, forecast, actual, commitment and value reference?",
                "kind": "provenance",
                "answer_data": [
                  "authority",
                  "source and method",
                  "supporting and contradicting evidence",
                  "event and knowledge time",
                  "confidence and uncertainty"
                ]
              },
              {
                "id": "funding-budget-investment-cost-forecast-actual-commitment-and-value-reference-q03",
                "text": "How is funding, budget, investment, cost, forecast, actual, commitment and value reference validated, accessed, changed, contested, corrected and retained?",
                "kind": "validation",
                "answer_data": [
                  "validation and profile rules",
                  "access and disclosure",
                  "change and dispute",
                  "lineage",
                  "retention and disposition"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "funding-budget-investment-cost-forecast-actual-commitment-and-value-reference-data",
                "name": "Funding, budget, investment, cost, forecast, actual, commitment and value reference data",
                "description": "Structured programme or portfolio data for funding, budget, investment, cost, forecast, actual, commitment and value reference.",
                "value_kind": "collection",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-003",
                  "SRC-006"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "funding-budget-investment-cost-forecast-actual-commitment-and-value-reference-record",
                "name": "Funding, budget, investment, cost, forecast, actual, commitment and value reference record",
                "description": "Versioned evidence-bearing program or portfolio record for funding, budget, investment, cost, forecast, actual, commitment and value reference with authority, time, provenance and access marking.",
                "media_or_form": [
                  "logical program or portfolio assertion",
                  "plan, assignment, decision, event, observation or evidence reference"
                ],
                "serial": true,
                "identity_strategy": "Aggregate identifier plus program-or-portfolio profile plus funding-budget-investment-cost-forecast-actual-commitment-and-value-reference assertion, artifact or event identifier; name, date, timestamp and digest never identify the aggregate alone.",
                "source_refs": [
                  "SRC-003",
                  "SRC-006"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "investment-resources-prioritization-and-control",
            "name": "Investment, resources, prioritization and control",
            "description": "Governs allocation decisions and the constraints that affect delivery and value."
          },
          "layer": {
            "id": "investment-funding-and-capacity",
            "name": "Investment, funding and capacity",
            "description": "References money and capacity without replacing their source systems."
          },
          "finding": {
            "id": "resource-capability-capacity-demand-allocation-utilization-gap-and-conflict",
            "name": "Resource, capability, capacity, demand, allocation, utilization, gap and conflict",
            "description": "External resource or capability ID, time-bounded demand, capacity, assignment, utilization, shortage, contention and resolution decision.",
            "source_refs": [
              "SRC-002",
              "SRC-003",
              "SRC-006"
            ],
            "questions": [
              {
                "id": "resource-capability-capacity-demand-allocation-utilization-gap-and-conflict-q01",
                "text": "What identities, types, roles, scope, versions and explicit values define resource, capability, capacity, demand, allocation, utilization, gap and conflict?",
                "kind": "composition",
                "answer_data": [
                  "identifiers and classifications",
                  "roles and scope",
                  "versions and validity",
                  "values and explicit unknowns"
                ]
              },
              {
                "id": "resource-capability-capacity-demand-allocation-utilization-gap-and-conflict-q02",
                "text": "Which authority, source, method, evidence, event time and knowledge time support resource, capability, capacity, demand, allocation, utilization, gap and conflict?",
                "kind": "provenance",
                "answer_data": [
                  "authority",
                  "source and method",
                  "supporting and contradicting evidence",
                  "event and knowledge time",
                  "confidence and uncertainty"
                ]
              },
              {
                "id": "resource-capability-capacity-demand-allocation-utilization-gap-and-conflict-q03",
                "text": "How is resource, capability, capacity, demand, allocation, utilization, gap and conflict validated, accessed, changed, contested, corrected and retained?",
                "kind": "validation",
                "answer_data": [
                  "validation and profile rules",
                  "access and disclosure",
                  "change and dispute",
                  "lineage",
                  "retention and disposition"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "resource-capability-capacity-demand-allocation-utilization-gap-and-conflict-data",
                "name": "Resource, capability, capacity, demand, allocation, utilization, gap and conflict data",
                "description": "Structured programme or portfolio data for resource, capability, capacity, demand, allocation, utilization, gap and conflict.",
                "value_kind": "collection",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-002",
                  "SRC-003",
                  "SRC-006"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "resource-capability-capacity-demand-allocation-utilization-gap-and-conflict-record",
                "name": "Resource, capability, capacity, demand, allocation, utilization, gap and conflict record",
                "description": "Versioned evidence-bearing program or portfolio record for resource, capability, capacity, demand, allocation, utilization, gap and conflict with authority, time, provenance and access marking.",
                "media_or_form": [
                  "logical program or portfolio assertion",
                  "plan, assignment, decision, event, observation or evidence reference"
                ],
                "serial": true,
                "identity_strategy": "Aggregate identifier plus program-or-portfolio profile plus resource-capability-capacity-demand-allocation-utilization-gap-and-conflict assertion, artifact or event identifier; name, date, timestamp and digest never identify the aggregate alone.",
                "source_refs": [
                  "SRC-002",
                  "SRC-003",
                  "SRC-006"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "investment-resources-prioritization-and-control",
            "name": "Investment, resources, prioritization and control",
            "description": "Governs allocation decisions and the constraints that affect delivery and value."
          },
          "layer": {
            "id": "selection-sequencing-risk-and-change-control",
            "name": "Selection, sequencing, risk and change control",
            "description": "Applies profile-specific prioritization and common control evidence."
          },
          "finding": {
            "id": "programme-sequencing-or-portfolio-selection-prioritization-balancing-and-reallocation",
            "name": "Programme sequencing or portfolio selection, prioritization, balancing and reallocation",
            "description": "For programmes, dependency-led sequencing and coordination; for portfolios, criteria-based selection, ranking, balance, scenario and allocation decisions with rationale.",
            "source_refs": [
              "SRC-002",
              "SRC-003",
              "SRC-004",
              "SRC-006"
            ],
            "questions": [
              {
                "id": "programme-sequencing-or-portfolio-selection-prioritization-balancing-and-reallocation-q01",
                "text": "What identities, types, roles, scope, versions and explicit values define programme sequencing or portfolio selection, prioritization, balancing and reallocation?",
                "kind": "decision",
                "answer_data": [
                  "identifiers and classifications",
                  "roles and scope",
                  "versions and validity",
                  "values and explicit unknowns"
                ]
              },
              {
                "id": "programme-sequencing-or-portfolio-selection-prioritization-balancing-and-reallocation-q02",
                "text": "Which authority, source, method, evidence, event time and knowledge time support programme sequencing or portfolio selection, prioritization, balancing and reallocation?",
                "kind": "provenance",
                "answer_data": [
                  "authority",
                  "source and method",
                  "supporting and contradicting evidence",
                  "event and knowledge time",
                  "confidence and uncertainty"
                ]
              },
              {
                "id": "programme-sequencing-or-portfolio-selection-prioritization-balancing-and-reallocation-q03",
                "text": "How is programme sequencing or portfolio selection, prioritization, balancing and reallocation validated, accessed, changed, contested, corrected and retained?",
                "kind": "validation",
                "answer_data": [
                  "validation and profile rules",
                  "access and disclosure",
                  "change and dispute",
                  "lineage",
                  "retention and disposition"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "programme-sequencing-or-portfolio-selection-prioritization-balancing-and-reallocation-data",
                "name": "Programme sequencing or portfolio selection, prioritization, balancing and reallocation data",
                "description": "Structured programme or portfolio data for programme sequencing or portfolio selection, prioritization, balancing and reallocation.",
                "value_kind": "collection",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-003",
                  "SRC-004",
                  "SRC-006"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "programme-sequencing-or-portfolio-selection-prioritization-balancing-and-reallocation-record",
                "name": "Programme sequencing or portfolio selection, prioritization, balancing and reallocation record",
                "description": "Versioned evidence-bearing program or portfolio record for programme sequencing or portfolio selection, prioritization, balancing and reallocation with authority, time, provenance and access marking.",
                "media_or_form": [
                  "logical program or portfolio assertion",
                  "plan, assignment, decision, event, observation or evidence reference"
                ],
                "serial": true,
                "identity_strategy": "Aggregate identifier plus program-or-portfolio profile plus programme-sequencing-or-portfolio-selection-prioritization-balancing-and-reallocation assertion, artifact or event identifier; name, date, timestamp and digest never identify the aggregate alone.",
                "source_refs": [
                  "SRC-002",
                  "SRC-003",
                  "SRC-004",
                  "SRC-006"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "lifecycle-decisions-performance-and-learning",
            "name": "Lifecycle, decisions, performance and learning",
            "description": "Preserves authorized state changes and source-qualified evidence of performance and value."
          },
          "layer": {
            "id": "lifecycle-membership-and-decision-history",
            "name": "Lifecycle, membership and decision history",
            "description": "Records transitions and component changes without rewriting history."
          },
          "finding": {
            "id": "component-admission-removal-priority-change-successor-and-history",
            "name": "Component admission, removal, priority change, successor and history",
            "description": "Immutable membership or priority event, component, criteria version, alternatives, decision, effective interval, predecessor, successor and downstream effect.",
            "source_refs": [
              "SRC-003",
              "SRC-004",
              "SRC-006",
              "SRC-010"
            ],
            "questions": [
              {
                "id": "component-admission-removal-priority-change-successor-and-history-q01",
                "text": "What identities, types, roles, scope, versions and explicit values define component admission, removal, priority change, successor and history?",
                "kind": "lifecycle",
                "answer_data": [
                  "identifiers and classifications",
                  "roles and scope",
                  "versions and validity",
                  "values and explicit unknowns"
                ]
              },
              {
                "id": "component-admission-removal-priority-change-successor-and-history-q02",
                "text": "Which authority, source, method, evidence, event time and knowledge time support component admission, removal, priority change, successor and history?",
                "kind": "provenance",
                "answer_data": [
                  "authority",
                  "source and method",
                  "supporting and contradicting evidence",
                  "event and knowledge time",
                  "confidence and uncertainty"
                ]
              },
              {
                "id": "component-admission-removal-priority-change-successor-and-history-q03",
                "text": "How is component admission, removal, priority change, successor and history validated, accessed, changed, contested, corrected and retained?",
                "kind": "validation",
                "answer_data": [
                  "validation and profile rules",
                  "access and disclosure",
                  "change and dispute",
                  "lineage",
                  "retention and disposition"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "component-admission-removal-priority-change-successor-and-history-data",
                "name": "Component admission, removal, priority change, successor and history data",
                "description": "Structured programme or portfolio data for component admission, removal, priority change, successor and history.",
                "value_kind": "collection",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-003",
                  "SRC-004",
                  "SRC-006",
                  "SRC-010"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "component-admission-removal-priority-change-successor-and-history-record",
                "name": "Component admission, removal, priority change, successor and history record",
                "description": "Versioned evidence-bearing program or portfolio record for component admission, removal, priority change, successor and history with authority, time, provenance and access marking.",
                "media_or_form": [
                  "logical program or portfolio assertion",
                  "plan, assignment, decision, event, observation or evidence reference"
                ],
                "serial": true,
                "identity_strategy": "Aggregate identifier plus program-or-portfolio profile plus component-admission-removal-priority-change-successor-and-history assertion, artifact or event identifier; name, date, timestamp and digest never identify the aggregate alone.",
                "source_refs": [
                  "SRC-003",
                  "SRC-004",
                  "SRC-006",
                  "SRC-010"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "lifecycle-decisions-performance-and-learning",
            "name": "Lifecycle, decisions, performance and learning",
            "description": "Preserves authorized state changes and source-qualified evidence of performance and value."
          },
          "layer": {
            "id": "measurement-evaluation-and-learning",
            "name": "Measurement, evaluation and learning",
            "description": "Separates metric definitions, observations, conclusions and learning."
          },
          "finding": {
            "id": "metric-definition-formula-unit-dimension-baseline-target-forecast-actual-and-aggregation",
            "name": "Metric definition, formula, unit, dimension, baseline, target, forecast, actual and aggregation",
            "description": "Metric ID and version, definition, formula, unit, dimensions, numerator and denominator, baseline, target, forecast, observation link, aggregation and deduplication.",
            "source_refs": [
              "SRC-007",
              "SRC-009",
              "SRC-011"
            ],
            "questions": [
              {
                "id": "metric-definition-formula-unit-dimension-baseline-target-forecast-actual-and-aggregation-q01",
                "text": "What identities, types, roles, scope, versions and explicit values define metric definition, formula, unit, dimension, baseline, target, forecast, actual and aggregation?",
                "kind": "classification",
                "answer_data": [
                  "identifiers and classifications",
                  "roles and scope",
                  "versions and validity",
                  "values and explicit unknowns"
                ]
              },
              {
                "id": "metric-definition-formula-unit-dimension-baseline-target-forecast-actual-and-aggregation-q02",
                "text": "Which authority, source, method, evidence, event time and knowledge time support metric definition, formula, unit, dimension, baseline, target, forecast, actual and aggregation?",
                "kind": "provenance",
                "answer_data": [
                  "authority",
                  "source and method",
                  "supporting and contradicting evidence",
                  "event and knowledge time",
                  "confidence and uncertainty"
                ]
              },
              {
                "id": "metric-definition-formula-unit-dimension-baseline-target-forecast-actual-and-aggregation-q03",
                "text": "How is metric definition, formula, unit, dimension, baseline, target, forecast, actual and aggregation validated, accessed, changed, contested, corrected and retained?",
                "kind": "validation",
                "answer_data": [
                  "validation and profile rules",
                  "access and disclosure",
                  "change and dispute",
                  "lineage",
                  "retention and disposition"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "metric-definition-formula-unit-dimension-baseline-target-forecast-actual-and-aggregation-data",
                "name": "Metric definition, formula, unit, dimension, baseline, target, forecast, actual and aggregation data",
                "description": "Structured programme or portfolio data for metric definition, formula, unit, dimension, baseline, target, forecast, actual and aggregation.",
                "value_kind": "collection",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-007",
                  "SRC-009",
                  "SRC-011"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "metric-definition-formula-unit-dimension-baseline-target-forecast-actual-and-aggregation-record",
                "name": "Metric definition, formula, unit, dimension, baseline, target, forecast, actual and aggregation record",
                "description": "Versioned evidence-bearing program or portfolio record for metric definition, formula, unit, dimension, baseline, target, forecast, actual and aggregation with authority, time, provenance and access marking.",
                "media_or_form": [
                  "logical program or portfolio assertion",
                  "plan, assignment, decision, event, observation or evidence reference"
                ],
                "serial": true,
                "identity_strategy": "Aggregate identifier plus program-or-portfolio profile plus metric-definition-formula-unit-dimension-baseline-target-forecast-actual-and-aggregation assertion, artifact or event identifier; name, date, timestamp and digest never identify the aggregate alone.",
                "source_refs": [
                  "SRC-007",
                  "SRC-009",
                  "SRC-011"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "lifecycle-decisions-performance-and-learning",
            "name": "Lifecycle, decisions, performance and learning",
            "description": "Preserves authorized state changes and source-qualified evidence of performance and value."
          },
          "layer": {
            "id": "measurement-evaluation-and-learning",
            "name": "Measurement, evaluation and learning",
            "description": "Separates metric definitions, observations, conclusions and learning."
          },
          "finding": {
            "id": "performance-observation-evaluation-health-variance-benefit-review-and-lesson",
            "name": "Performance observation, evaluation, health, variance, benefit review and lesson",
            "description": "Source dataset, period, observed value, quality, uncertainty, health rule, variance, evaluation method, benefit review, conclusion, decision, lesson and applicability.",
            "source_refs": [
              "SRC-007",
              "SRC-008",
              "SRC-009",
              "SRC-010",
              "SRC-011"
            ],
            "questions": [
              {
                "id": "performance-observation-evaluation-health-variance-benefit-review-and-lesson-q01",
                "text": "What identities, types, roles, scope, versions and explicit values define performance observation, evaluation, health, variance, benefit review and lesson?",
                "kind": "evidence",
                "answer_data": [
                  "identifiers and classifications",
                  "roles and scope",
                  "versions and validity",
                  "values and explicit unknowns"
                ]
              },
              {
                "id": "performance-observation-evaluation-health-variance-benefit-review-and-lesson-q02",
                "text": "Which authority, source, method, evidence, event time and knowledge time support performance observation, evaluation, health, variance, benefit review and lesson?",
                "kind": "provenance",
                "answer_data": [
                  "authority",
                  "source and method",
                  "supporting and contradicting evidence",
                  "event and knowledge time",
                  "confidence and uncertainty"
                ]
              },
              {
                "id": "performance-observation-evaluation-health-variance-benefit-review-and-lesson-q03",
                "text": "How is performance observation, evaluation, health, variance, benefit review and lesson validated, accessed, changed, contested, corrected and retained?",
                "kind": "validation",
                "answer_data": [
                  "validation and profile rules",
                  "access and disclosure",
                  "change and dispute",
                  "lineage",
                  "retention and disposition"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "performance-observation-evaluation-health-variance-benefit-review-and-lesson-data",
                "name": "Performance observation, evaluation, health, variance, benefit review and lesson data",
                "description": "Structured programme or portfolio data for performance observation, evaluation, health, variance, benefit review and lesson.",
                "value_kind": "collection",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-007",
                  "SRC-008",
                  "SRC-009",
                  "SRC-010",
                  "SRC-011"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "performance-observation-evaluation-health-variance-benefit-review-and-lesson-record",
                "name": "Performance observation, evaluation, health, variance, benefit review and lesson record",
                "description": "Versioned evidence-bearing program or portfolio record for performance observation, evaluation, health, variance, benefit review and lesson with authority, time, provenance and access marking.",
                "media_or_form": [
                  "logical program or portfolio assertion",
                  "plan, assignment, decision, event, observation or evidence reference"
                ],
                "serial": true,
                "identity_strategy": "Aggregate identifier plus program-or-portfolio profile plus performance-observation-evaluation-health-variance-benefit-review-and-lesson assertion, artifact or event identifier; name, date, timestamp and digest never identify the aggregate alone.",
                "source_refs": [
                  "SRC-007",
                  "SRC-008",
                  "SRC-009",
                  "SRC-010",
                  "SRC-011"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        }
      ],
      "functions": [
        {
          "id": "register-and-profile-aggregate",
          "name": "Register and profile aggregate",
          "description": "Establish identity, profile, boundary and source lineage.",
          "inputs": [
            "programme or portfolio proposal",
            "authoritative source",
            "profile"
          ],
          "outputs": [
            "versioned aggregate root"
          ],
          "preconditions": [
            "identity, duplicate, profile and boundary rules validate"
          ],
          "effects": [
            "a governed root exists without admitting components"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-003",
            "SRC-010"
          ]
        },
        {
          "id": "authorize-mandate-and-governance",
          "name": "Authorize mandate and governance",
          "description": "Bind accountable authority, governance roles, decision rights and assurance.",
          "inputs": [
            "aggregate root",
            "mandate",
            "governing actors",
            "policy"
          ],
          "outputs": [
            "authorized governance release"
          ],
          "preconditions": [
            "mandate, delegation, segregation, jurisdiction and gate controls validate"
          ],
          "effects": [
            "the aggregate may be governed within explicit limits"
          ],
          "source_refs": [
            "SRC-004",
            "SRC-006"
          ]
        },
        {
          "id": "admit-or-remove-component",
          "name": "Admit or remove component",
          "description": "Append a source-qualified component membership decision.",
          "inputs": [
            "aggregate",
            "external component",
            "criteria",
            "decision"
          ],
          "outputs": [
            "membership event"
          ],
          "preconditions": [
            "profile, eligibility, authority, effective interval and expected revision validate"
          ],
          "effects": [
            "membership changes without absorbing or rewriting the component master"
          ],
          "source_refs": [
            "SRC-002",
            "SRC-003",
            "SRC-004",
            "SRC-006"
          ]
        },
        {
          "id": "map-alignment-and-dependencies",
          "name": "Map alignment and dependencies",
          "description": "Connect strategy, objectives, components, interfaces and constraints.",
          "inputs": [
            "strategy and objective refs",
            "components",
            "evidence"
          ],
          "outputs": [
            "alignment and dependency graph release"
          ],
          "preconditions": [
            "source, relation type, direction, validity, assumptions and contradictions validate"
          ],
          "effects": [
            "coordination and selection reasoning becomes inspectable"
          ],
          "source_refs": [
            "SRC-002",
            "SRC-003",
            "SRC-006",
            "SRC-009"
          ]
        },
        {
          "id": "define-outcomes-and-benefit-realization",
          "name": "Define outcomes and benefit realization",
          "description": "Release a results chain and benefit or disbenefit realization plan.",
          "inputs": [
            "need",
            "components",
            "stakeholders",
            "evidence"
          ],
          "outputs": [
            "results framework and benefit plan"
          ],
          "preconditions": [
            "result levels, owners, baselines, targets, methods, assumptions and causal limits validate"
          ],
          "effects": [
            "intended change becomes measurable without asserting realization"
          ],
          "source_refs": [
            "SRC-007",
            "SRC-008",
            "SRC-009",
            "SRC-011"
          ]
        },
        {
          "id": "plan-roadmap-resources-and-transition",
          "name": "Plan roadmap, resources and transition",
          "description": "Coordinate tranches or horizons, capacity, milestones and operational adoption.",
          "inputs": [
            "aggregate release",
            "components",
            "capacity",
            "constraints"
          ],
          "outputs": [
            "roadmap and transition release"
          ],
          "preconditions": [
            "dependencies, schedule, resources, readiness, ownership and acceptance validate"
          ],
          "effects": [
            "staged work and adoption are planned without claiming completion"
          ],
          "source_refs": [
            "SRC-002",
            "SRC-003",
            "SRC-006",
            "SRC-012"
          ]
        },
        {
          "id": "prioritize-balance-sequence-and-reallocate",
          "name": "Prioritize, balance, sequence and reallocate",
          "description": "Apply the profile-appropriate decision method to components and resources.",
          "inputs": [
            "components",
            "criteria and weights",
            "constraints",
            "scenarios"
          ],
          "outputs": [
            "ranking, sequence or allocation decision"
          ],
          "preconditions": [
            "programme sequencing or portfolio selection guard, authority, alternatives, evidence and expected revision validate"
          ],
          "effects": [
            "approved priorities and allocation change with preserved rationale"
          ],
          "source_refs": [
            "SRC-002",
            "SRC-003",
            "SRC-004",
            "SRC-006"
          ]
        },
        {
          "id": "transition-program-or-portfolio-lifecycle",
          "name": "Transition program or portfolio lifecycle",
          "description": "Append an authorized proposal, start, pause, rebalance, termination, closure or supersession event.",
          "inputs": [
            "current revision",
            "transition",
            "authority",
            "evidence"
          ],
          "outputs": [
            "lifecycle event and current-state projection"
          ],
          "preconditions": [
            "profile transition table, gate, scope, reason, event time and downstream controls validate"
          ],
          "effects": [
            "operating state changes without rewriting prior history"
          ],
          "source_refs": [
            "SRC-002",
            "SRC-003",
            "SRC-004",
            "SRC-006",
            "SRC-010",
            "SRC-012"
          ]
        },
        {
          "id": "record-evaluate-and-review-performance",
          "name": "Record, evaluate and review performance",
          "description": "Attach source-qualified observations and method-bounded performance and benefit conclusions.",
          "inputs": [
            "metric definitions",
            "source datasets",
            "evaluation method"
          ],
          "outputs": [
            "observation, evaluation and review records"
          ],
          "preconditions": [
            "formula, unit, dimensions, baseline, target, denominator, aggregation, quality and attribution limits validate"
          ],
          "effects": [
            "decisions can use evidence without confusing outputs, outcomes, benefits or causation"
          ],
          "source_refs": [
            "SRC-007",
            "SRC-008",
            "SRC-009",
            "SRC-010",
            "SRC-011"
          ]
        },
        {
          "id": "project-validate-correct-retain-and-audit",
          "name": "Project, validate, correct, retain and audit",
          "description": "Produce a loss-aware view or execute governed correction, retention and audit operations.",
          "inputs": [
            "aggregate revision",
            "target profile or policy",
            "purpose"
          ],
          "outputs": [
            "projection, validation, correction, disposition or audit event"
          ],
          "preconditions": [
            "identity, version, mapping loss, access, legal hold, minimum tombstone and post-checks validate"
          ],
          "effects": [
            "programme or portfolio data remains interoperable and accountable under policy"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-003",
            "SRC-004",
            "SRC-006",
            "SRC-010",
            "SRC-011",
            "SRC-012"
          ]
        }
      ],
      "composition": [
        {
          "target": "Project, Program-as-component, Product, Operation and Campaign models",
          "relation": "REFERENCE",
          "purpose": "Resolve component masters while preserving their identity, lifecycle, authority and evidence.",
          "required": true,
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-003",
            "SRC-005",
            "SRC-006"
          ]
        },
        {
          "target": "Party, Role, Mandate, Strategy, Objective and Policy models",
          "relation": "REFERENCE",
          "purpose": "Resolve accountable actors, decision authority, governing context and strategic alignment.",
          "required": true,
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-003",
            "SRC-004",
            "SRC-006"
          ]
        },
        {
          "target": "Outcome, Benefit, Resource, Budget, Contract, Risk, Issue, Decision, Metric, Observation, Dataset and Audit models",
          "relation": "REFERENCE",
          "purpose": "Bind external masters to aggregate-scoped plans, allocations, controls, observations and evaluation without copying their lifecycle.",
          "required": false,
          "source_refs": [
            "SRC-004",
            "SRC-006",
            "SRC-007",
            "SRC-008",
            "SRC-009",
            "SRC-010",
            "SRC-011"
          ]
        },
        {
          "target": "ISO 21500, ISO 21503, ISO 21504 and ISO 21505",
          "relation": "ALIGN",
          "purpose": "Project the declared programme or portfolio profile, context and governance with explicit public-source and conformance limits.",
          "required": false,
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-003",
            "SRC-004"
          ]
        },
        {
          "target": "OECD results terminology, W3C PROV-O and RDF Data Cube",
          "relation": "ALIGN",
          "purpose": "Project results chains, provenance and multidimensional performance observations with declared semantic loss.",
          "required": false,
          "source_refs": [
            "SRC-008",
            "SRC-009",
            "SRC-010",
            "SRC-011"
          ]
        }
      ],
      "researchAdjudication": {
        "providerMode": "single-provider-waiver",
        "activeProviders": [
          "codex"
        ],
        "waivedProviders": [
          "claude",
          "grok"
        ],
        "providerPolicy": {
          "contract_version": "1.0.0",
          "mode": "single-provider-waiver",
          "effective_at": "2026-09-06T00:00:00Z",
          "scope": "Canonical single-stream subject-model research after the six-workstream consolidation",
          "active_providers": [
            "codex"
          ],
          "waived_providers": [
            {
              "provider": "claude",
              "authorized_by": "repository owner",
              "authorized_at": "2026-09-06T00:00:00Z",
              "reason": "Claude produced no result on prior 1800-second and 900-second attempts and again timed out on bounded 600-second Sonnet and 300-second Haiku passes. The owner prioritized completion over provider availability."
            },
            {
              "provider": "grok",
              "authorized_by": "repository owner",
              "authorized_at": "2026-09-06T00:00:00Z",
              "reason": "The repository owner authorized completion without Grok when Grok is unavailable, slow or schema-invalid. Grok may still be attempted as a bounded supplemental reviewer, but its failure never blocks a valid Claude plus no-tools result."
            }
          ],
          "review_rule": "Codex may complete source-grounded fallback research after bounded Claude and Grok attempts fail. It requires a separate no-tools adversarial audit and remains reviewable-draft with a visible absence-of-external-review hold.",
          "supplemental_provider_attempts": [
            {
              "provider": "claude",
              "required": false,
              "maximum_attempts": 1,
              "failure_policy": "record-and-continue",
              "admission_rule": "Use only a locally schema-valid result whose sources and boundaries survive adjudication."
            },
            {
              "provider": "grok",
              "required": false,
              "maximum_attempts": 1,
              "failure_policy": "record-and-continue",
              "admission_rule": "Use only a locally schema-valid result whose sources and boundaries survive adjudication."
            }
          ]
        },
        "boundaryDecision": {
          "entry_kind": "aggregate",
          "status": "accepted",
          "rationale": "Two axes must stay separate. On the record plane the frozen registry classifies this as a standalone model record (standalone-mm); that is a storage and publication classification of the Vercy record and is not a member of the subject-model enum, so it must never be emitted as entry_kind. On the subject plane the modelled thing is an invariant-enforcing root: it owns profile, mandate, governance, membership, allocation, sequencing, lifecycle and evaluation assertions, while every component, party, strategy, benefit, budget, risk, decision and observation master is referenced only by external identity and retains its own lifecycle, owner and evidence. That is an aggregate. It is not an entity, which would not carry the membership and allocation invariants; not a registry, which would hold the catalogue of investments but neither the mandate, reserved decision rights nor the root lifecycle; not a relationship, since membership is one owned assertion class inside the root rather than the root itself; and not a pattern, mixin, classifier or event. Accepted for a reviewable draft. The Programme-versus-Portfolio split remains a deferred contingency guarded by the required profile discriminator and profile-specific rules, not a present reclassification."
        },
        "decisions": [
          {
            "concept": "Aggregate root: one profiled programme-or-portfolio root",
            "disposition": "accepted",
            "rationale": "The root owns membership, allocation, sequencing and lifecycle assertions while every component and master is referenced by external identity, which is the defining invariant boundary of an aggregate rather than a plain entity."
          },
          {
            "concept": "Alternative entry kind: portfolio-as-registry",
            "disposition": "rejected",
            "rationale": "A registry would own only the catalogue of investments; this root also carries mandate, governance, reserved decision rights, benefit logic and its own lifecycle, so registry understates the invariants it enforces."
          },
          {
            "concept": "Record-plane value standalone-mm versus subject-model entry kind",
            "disposition": "reclassified to the schema kind aggregate",
            "rationale": "standalone-mm describes how the registry stores and publishes the record, not what the modelled subject is; the two axes must be published separately so the enum value remains a subject-model claim."
          },
          {
            "concept": "Split into separate Programme and Portfolio models",
            "disposition": "deferred",
            "rationale": "The required profile discriminator plus profile-specific selection-versus-sequencing rules suffices for a reviewable draft; a split needs implementation evidence of unsafe ambiguity that this pack does not yet contain."
          },
          {
            "concept": "ISO SRC-001 to SRC-005 marked primary_source true",
            "disposition": "rejected as stated; downgrade to abstract-level support",
            "rationale": "The pinned URLs are catalogue pages and the pack's own omissions admit full text was unavailable, so tier-1 authority is fair but primary-source retrieval is not established and must not underwrite clause-level claims."
          },
          {
            "concept": "Source refs on the retention and the access findings",
            "disposition": "rejected as source support; relabel as Vercy house policy",
            "rationale": "SRC-004, SRC-006, SRC-010 and SRC-012 cover governance, provenance and timestamps; none is a records-retention or privacy authority, so retention class, legal hold, tombstone and minimum-necessary disclosure rules are currently unsourced."
          },
          {
            "concept": "Templated q02 provenance and q03 validation questions, 48 of 72",
            "disposition": "accepted for the draft, rewrite deferred",
            "rationale": "Identical wording across every finding gives no discriminating research prompt, but the questions are not wrong and deleting them would strip provenance and validation coverage before finding-specific replacements exist."
          },
          {
            "concept": "Uniform six-bundle, two-layer, two-finding lattice",
            "disposition": "accepted with a deferred depth rebalance",
            "rationale": "Perfect symmetry indicates generated rather than domain-driven decomposition; component membership and dependency carries far more real variability than profile definition and identity does."
          },
          {
            "concept": "Programme-or-portfolio profile embedded in the artifact identity strategy",
            "disposition": "accepted, conditional on an explicit supersession rule",
            "rationale": "Putting the profile in the identity tuple means reclassification cannot be an update, yet canon_and_patch defines only profile-safe successors and leaves profile-unsafe change entirely undefined."
          },
          {
            "concept": "Model name Program / Portfolio and the serial_naming_rule token program-or-portfolio",
            "disposition": "rejected as stated; normalize the spelling",
            "rationale": "Identity strategies, policies and boundary notes use programme-or-portfolio while the name and naming rule use the US spelling, which breaks deterministic artifact naming and crosswalk round-tripping."
          },
          {
            "concept": "Access scopes bundle, layer, finding, artifact versus field-level minimum necessary",
            "disposition": "deferred reconciliation",
            "rationale": "The default access rule and the audit requirements both assume field-level disclosure control and affected-field logging that the declared scope list cannot express, so one of the two must give."
          },
          {
            "concept": "Benefit and change owner role responsibilities",
            "disposition": "accepted with an aggregate-scoped qualifier",
            "rationale": "Owning outcome definitions, baselines, targets and realization evidence reads as ownership of the external benefit master that out_of_scope explicitly excludes; the qualifier keeps the ownership boundary intact."
          },
          {
            "concept": "Campaign and product neighbor distinctions in the profile boundary finding",
            "disposition": "deferred to sibling-model reconciliation",
            "rationale": "The finding asserts distinctions from campaign and product masters, but its source refs cover only ISO project, programme and portfolio material, leaving those two boundary claims unsupported inside this pack."
          },
          {
            "concept": "Coverage checklist marking all sixteen dimensions covered",
            "disposition": "rejected as stated; qualify interoperability, composition and capabilities",
            "rationale": "The same package admits abstract-only ISO support, unapproved relation rows and no dedicated stakeholder-engagement finding, so a uniform covered status overstates what has actually been verified."
          },
          {
            "concept": "serial set true on all twenty-four artifacts",
            "disposition": "accepted for the draft, per-artifact adjudication deferred",
            "rationale": "The crosswalk and metric-definition records behave like versioned releases rather than serially numbered event artifacts, but a uniform default is safe while the naming token is being normalized."
          },
          {
            "concept": "Grok waiver text citing a valid Claude plus no-tools result",
            "disposition": "accepted as recorded, publish a corrected waiver chain",
            "rationale": "The clause presumes a Claude result that never existed, while active_providers and the review rule remain unambiguous, so the remedy is accurate publication of the real waiver chain rather than a blocking contradiction."
          }
        ],
        "publicationHolds": [
          "Re-verify every source URL, edition and version pin live before publication, in particular GovS 002 version 2.1 dated 17 September 2025, the 2017 IPA benefits management PDF on its assets media path, and the five ISO catalogue editions cited as SRC-001 to SRC-005.",
          "Publish the owner-authorized absence of independent second-provider review in every artifact: neither Claude nor Grok produced an admissible result, and neither the Codex fallback research nor this local no-tools Claude audit may be described as independent external review.",
          "No ISO conformance claim of any kind until licensed clause-level text has been reviewed; the package currently rests on official abstracts plus public-authority guidance.",
          "Hold the registry Project parent link and every proposed strategy, component, benefit, finance, risk, decision, observation, policy and audit relation; no approved relation rows were supplied and the frozen registry context arrived empty, so the relationship contract could not be checked.",
          "Relabel the retention, disposition, tombstone and access rules as Vercy house policy until a records-management authority and a privacy or access-control authority are cited alongside them.",
          "Normalize the programme-or-portfolio profile token across the model name, the serial naming rule and all identity strategies, and state that a profile change is a supersession rather than an update, before any artifact identifiers are minted.",
          "Keep the record at reviewable-draft status and block canonical promotion while second-provider review remains waived.",
          "Independent external review was explicitly waived by the repository owner; this codex-only result remains a reviewable draft."
        ],
        "deferredResearch": [
          "Obtain licensed clause-level text of ISO 21500, 21502, 21503, 21504 and 21505 and re-derive the programme-versus-portfolio discriminator, governance and component definitions against normative clauses rather than catalogue abstracts.",
          "Cross-validate the profile discriminator and the selection-versus-sequencing split against at least one non-ISO practice standard family so the boundary does not rest on a single standards body.",
          "Acquire a records-management authority and a privacy or access-control authority to ground the retention class, legal hold, tombstone, purpose-bound view and minimum-necessary disclosure rules that are currently unsourced.",
          "Close the stakeholder engagement, communication and reporting coverage gap, which appears only incidentally as affected groups and affected stakeholder inside the transition and results-chain findings.",
          "Replace the forty-eight boilerplate provenance and validation questions with finding-specific probes, since their identical wording gives no discriminating research signal across twenty-four findings.",
          "Assess RFC 9557 additional-information suffixes against the RFC 3339 timestamp rule and the separation of planned, decision, event, effective, observation, ingestion and knowledge times.",
          "Collect implementation evidence on whether one profiled root or two separate Programme and Portfolio models is safer, and record the trigger that would force the split.",
          "Reconcile the campaign, product and operation neighbor boundaries with the sibling subject models that own those masters, and attach source refs to each asserted distinction.",
          "Attempt one bounded supplemental Grok review pass under the record-and-continue policy so the reviewable-draft hold can eventually be lifted by a genuinely independent provider."
        ]
      }
    },
    "project": {
      "publication": {
        "status": "published",
        "adjudicationStatus": "reviewable-draft",
        "publishableCanonical": false,
        "generatedAt": "2026-08-25T09:59:53Z",
        "synthesisSha256": "c1104b3d02abd63ae671e3d463be18a591c2ade178464f0f5aa1e3e4f35e0585",
        "providerMode": "dual-provider",
        "providers": [
          "Claude",
          "Grok"
        ],
        "waivedProviders": []
      },
      "model": {
        "registry_id": "vr.wm-act-005",
        "model_id": "WM-ACT-005",
        "name": "Project",
        "entry_kind": "aggregate",
        "purpose": "Provide the format-neutral context an agent needs to understand, create, inspect and operate one bounded undertaking: its identity, mandate, scope, breakdown, commitments, baselines, lifecycle, performance, uncertainty, records and closure.",
        "scope_statement": "A Project is a temporary, uniquely-scoped endeavour authorized by a sponsor to deliver defined outputs, outcomes or benefits within agreed constraints (ISO 21500:2021 concepts; ISO 21502:2020 practices; APM 'unique, transient endeavour'). This model owns the project as an aggregate root: identification and registration, authorization and governance, objectives and scope boundary, work breakdown, resource/funding/procurement commitments, lifecycle states and gates, approved baselines and change control, progress measurement, risk/issue/assurance, stakeholders, record provenance and access, and closure with retention. It holds typed edges to contained tasks and milestones/deliverables rather than restating their internals. It is storage- and interface-neutral: JSON, YAML, Markdown, HTML, Git, MCP and MongoDB are projections of the same semantics.",
        "in_scope": [
          "Project identity, alternate identifiers and registration in an authoritative master system",
          "Authorization instrument, sponsor, governing body and delegated decision authority",
          "Objectives, success criteria and the declared scope boundary with exclusions",
          "Work breakdown structure, control accounts and typed links to contained components",
          "Resource, budget, cost-baseline and supplier commitments bound to the project",
          "Lifecycle states, phases, decision gates and permitted transitions",
          "Approved scope, schedule and cost baselines, their versioning and change control",
          "Progress and performance measurement including earned value where applicable",
          "Risk, issue, escalation and independent assurance records",
          "Stakeholder register, reporting obligations and disclosure duties",
          "Record provenance, evidence, access classification, closure and retention"
        ],
        "out_of_scope": [
          "Task-level execution detail, effort logging and assignment mechanics (WM-ACT-006)",
          "Internal structure and acceptance criteria of milestones and deliverables (WM-ACT-031)",
          "Programme and portfolio selection, balancing and benefit aggregation (WM-ACT-029; ISO 21503, ISO 21504)",
          "Schedule network logic, dependency calculus and critical-path computation (sibling plan/schedule model)",
          "Definitions of repeatable processes and workflows (sibling process model)",
          "Person and organization master data (sibling person/organization models)",
          "Financial ledger postings, payroll and statutory accounting",
          "Contract instrument text and procurement award procedure internals",
          "Product, system or asset definitions of whatever the project produces",
          "Generic access-control and audit machinery, which is a service-layer concern"
        ],
        "boundary_notes": [
          {
            "neighbor": "Programme and portfolio (WM-ACT-029)",
            "distinction": "Component selection, balancing against strategy and aggregated benefit realization sit above the project; ISO 21504:2022 explicitly does not give project management guidance and ISO 21503:2022 keeps benefit realization at programme level. The project records only benefits it is itself accountable for.",
            "source_refs": [
              "SRC-018",
              "SRC-019",
              "SRC-001"
            ]
          },
          {
            "neighbor": "Task (WM-ACT-006)",
            "distinction": "The project owns decomposition down to work-package or control-account level (ISO 21511:2018); assignable execution units, their states and effort belong to the task model and are referenced by typed edge, not copied.",
            "source_refs": [
              "SRC-004",
              "SRC-001"
            ]
          },
          {
            "neighbor": "Milestone and deliverable (WM-ACT-031)",
            "distinction": "The project references milestones and deliverables, gates on them and reports variance against them; their acceptance criteria, versions and internal composition are owned by the contained model.",
            "source_refs": [
              "SRC-001",
              "SRC-004"
            ]
          },
          {
            "neighbor": "Plan and schedule (sibling K7)",
            "distinction": "The project binds authoritative planned/actual dates and approved baselines; activity network logic, durations, float and critical path are schedule-model semantics (GAO-16-89G scheduling practices).",
            "source_refs": [
              "SRC-013",
              "SRC-001"
            ]
          },
          {
            "neighbor": "Process and workflow (sibling K3)",
            "distinction": "A project is unique and transient; a process is repeatable. Repeatable procedures used inside a project are referenced, and the same work executed as steady-state operations is not a project (APM).",
            "source_refs": [
              "SRC-016",
              "SRC-002"
            ]
          },
          {
            "neighbor": "PROV Activity and Plan (W3C PROV-O)",
            "distinction": "PROV supplies attribution, generation and plan semantics for alignment. A project is not the provenance graph of every act performed; individual acts resolve to the act model and are related by prov:wasAssociatedWith style edges.",
            "source_refs": [
              "SRC-006"
            ]
          },
          {
            "neighbor": "schema.org Project",
            "distinction": "schema.org types Project as a subtype of Organization (an agent). This conflicts with the ISO/APM definition of a project as a temporary endeavour. Alignment is publication-only and lossy; conformance is not claimed.",
            "source_refs": [
              "SRC-017",
              "SRC-002",
              "SRC-016"
            ]
          },
          {
            "neighbor": "IATI activity",
            "distinction": "An IATI activity may be a project, a sub-activity or a funding slice, distinguished by @hierarchy and related-activity edges. IATI is treated as an alignment and publication target, not as the identity authority for a project.",
            "source_refs": [
              "SRC-007",
              "SRC-021"
            ]
          }
        ]
      },
      "selected_findings": [
        {
          "bundle": {
            "id": "b-mandate-and-identity",
            "name": "Mandate and identity",
            "description": "Who and what this project is, who authorized it, who owns it and why the investment is justified."
          },
          "layer": {
            "id": "l-identity-and-registration",
            "name": "Identity and registration",
            "description": "Resolvable identification and governed classification of the project across the master system and external registries."
          },
          "finding": {
            "id": "f-project-identity",
            "name": "Project identity and identifier reconciliation",
            "description": "Which identifier authoritatively designates this project, which system issued it, which governed global identifiers also designate it, and how duplicate or superseding records are resolved.",
            "source_refs": [
              "SRC-010",
              "SRC-011",
              "SRC-007",
              "SRC-001"
            ],
            "questions": [
              {
                "id": "q-master-identifier",
                "text": "Which system of record issues the authoritative identifier for this project, and what is that identifier?",
                "kind": "identity",
                "answer_data": [
                  "Master system name and instance",
                  "Authoritative identifier value",
                  "Identifier scheme and syntax rule",
                  "Issuing date-time of assignment"
                ]
              },
              {
                "id": "q-global-identifiers",
                "text": "Which governed global identifiers, such as a RAiD, a funder award number or a published activity identifier, also designate this project?",
                "kind": "interoperability",
                "answer_data": [
                  "Identifier type",
                  "Identifier value",
                  "Issuing registry or registration agency",
                  "Resolution URL"
                ]
              },
              {
                "id": "q-identity-collision-rule",
                "text": "What rule decides identity when two records appear to describe the same undertaking under different identifiers?",
                "kind": "validation",
                "answer_data": [
                  "Match criteria set",
                  "Precedence order between schemes",
                  "Merge, supersede or reject decision",
                  "Deciding role and decision time"
                ]
              },
              {
                "id": "q-identifier-stability",
                "text": "Does the identifier survive renaming, re-scoping, transfer or merger, and what event forces a new identifier?",
                "kind": "lifecycle",
                "answer_data": [
                  "Stability policy statement",
                  "Re-issue trigger list",
                  "Superseded-by reference",
                  "Retained alias list"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-project-identifier",
                "name": "Project identifier",
                "description": "Authoritative identifier of the project issued by its master system of record.",
                "value_kind": "identifier",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-010",
                  "SRC-007"
                ]
              },
              {
                "id": "de-identifier-scheme",
                "name": "Identifier scheme",
                "description": "Scheme or namespace under which the authoritative identifier is issued, including scheme version where governed.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-010",
                  "SRC-011"
                ]
              },
              {
                "id": "de-alternate-identifier",
                "name": "Alternate identifier",
                "description": "Any further identifier designating the same project, each recorded with its issuing registry and resolution target.",
                "value_kind": "identifier",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-010",
                  "SRC-007"
                ]
              },
              {
                "id": "de-superseded-by-project",
                "name": "Superseded-by project reference",
                "description": "Reference to the project record that replaces this one after a merge, split or re-charter.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-010",
                  "SRC-021"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "a-identifier-registration-record",
                "name": "Identifier registration record",
                "description": "The record evidencing assignment of the authoritative identifier and any registered global identifiers, with issuing authority and assignment time.",
                "media_or_form": [
                  "registry entry",
                  "identifier landing page",
                  "structured assignment record"
                ],
                "serial": false,
                "identity_strategy": "Keyed by the authoritative master-system identifier; each governed global identifier is stored as an alternate identifier bound to its issuing registry and resolution URL. Names, acronyms and charter dates are search aids only and never keys.",
                "source_refs": [
                  "SRC-010",
                  "SRC-011"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "b-mandate-and-identity",
            "name": "Mandate and identity",
            "description": "Who and what this project is, who authorized it, who owns it and why the investment is justified."
          },
          "layer": {
            "id": "l-identity-and-registration",
            "name": "Identity and registration",
            "description": "Resolvable identification and governed classification of the project across the master system and external registries."
          },
          "finding": {
            "id": "f-project-classification",
            "name": "Classification, type and delivery approach",
            "description": "How the project is typed against governed vocabularies: project type, delivery approach, sector or thematic codes, and the criterion separating it from operations or a process instance.",
            "source_refs": [
              "SRC-001",
              "SRC-007",
              "SRC-016",
              "SRC-017"
            ],
            "questions": [
              {
                "id": "q-project-type-vocabulary",
                "text": "Which project type and domain classification apply, and under which controlled vocabulary and vocabulary version?",
                "kind": "classification",
                "answer_data": [
                  "Type code",
                  "Scheme URI",
                  "Scheme version",
                  "Assignment scope note"
                ]
              },
              {
                "id": "q-delivery-approach",
                "text": "Is delivery predictive, incremental, iterative, adaptive or hybrid, and may that approach change during the life cycle?",
                "kind": "state",
                "answer_data": [
                  "Delivery approach code",
                  "Effective period of the approach",
                  "Change trigger and approver",
                  "Tailoring note"
                ]
              },
              {
                "id": "q-classification-assertor",
                "text": "Which sector, thematic or funding-scheme codes are asserted for this project and who asserted each of them?",
                "kind": "provenance",
                "answer_data": [
                  "Code value and scheme",
                  "Asserting party",
                  "Assertion time",
                  "Assertion basis or evidence"
                ]
              },
              {
                "id": "q-project-versus-operations",
                "text": "What criterion establishes that this record is a transient endeavour rather than business-as-usual or a repeatable process instance?",
                "kind": "definition",
                "answer_data": [
                  "Finite timespan evidence",
                  "Uniqueness statement",
                  "Distinguishing test applied",
                  "Referenced process model, if any"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-project-type-code",
                "name": "Project type code",
                "description": "Governed type classification of the project within a named scheme.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-007",
                  "SRC-001"
                ]
              },
              {
                "id": "de-delivery-approach-code",
                "name": "Delivery approach code",
                "description": "Recorded delivery approach: predictive, incremental, iterative, adaptive or hybrid.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              },
              {
                "id": "de-classification-scheme-uri",
                "name": "Classification scheme URI",
                "description": "Resolvable identifier and version of each vocabulary used to classify the project.",
                "value_kind": "identifier",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-007",
                  "SRC-011"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "a-classification-binding",
                "name": "Classification binding table",
                "description": "Table binding the project to external code lists with scheme URI, scheme version, code, asserting party and assertion time.",
                "media_or_form": [
                  "code-list binding table",
                  "vocabulary mapping record"
                ],
                "serial": false,
                "identity_strategy": "Composite key of project identifier plus scheme URI plus code; a new binding row is created when the scheme version changes rather than mutating the existing row.",
                "source_refs": [
                  "SRC-007",
                  "SRC-011"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "b-mandate-and-identity",
            "name": "Mandate and identity",
            "description": "Who and what this project is, who authorized it, who owns it and why the investment is justified."
          },
          "layer": {
            "id": "l-authority-and-mandate",
            "name": "Authority and mandate",
            "description": "The instrument that authorized the project, the parties accountable for it, and the investment justification that keeps it authorized."
          },
          "finding": {
            "id": "f-charter-and-authorization",
            "name": "Authorization instrument and mandate limits",
            "description": "What authorized the project to exist and spend, who signed it, what tolerances bound the project manager, and how authorization behaves on re-baseline, pause or transfer.",
            "source_refs": [
              "SRC-003",
              "SRC-001",
              "SRC-015"
            ],
            "questions": [
              {
                "id": "q-authorization-instrument",
                "text": "Which instrument authorized this project to start, and which role signed it?",
                "kind": "authority",
                "answer_data": [
                  "Instrument type and reference",
                  "Signing role and party",
                  "Authorization scope statement",
                  "Signature or approval evidence"
                ]
              },
              {
                "id": "q-authorization-evidence",
                "text": "What decision record evidences the authorization, when did it take effect, and where is that record held?",
                "kind": "evidence",
                "answer_data": [
                  "Decision record reference",
                  "Decision effective time",
                  "Record location or repository",
                  "Retention custodian"
                ]
              },
              {
                "id": "q-delegated-tolerance",
                "text": "What tolerances or delegated limits on cost, time, scope and risk constrain the project manager before escalation is required?",
                "kind": "constraint",
                "answer_data": [
                  "Tolerance dimension",
                  "Threshold value and unit",
                  "Escalation target role",
                  "Tolerance review cadence"
                ]
              },
              {
                "id": "q-authorization-continuity",
                "text": "What happens to the authorization when the project is re-baselined, suspended or transferred to another owner?",
                "kind": "lifecycle",
                "answer_data": [
                  "Re-authorization trigger",
                  "Revision number of the instrument",
                  "Continuity or lapse rule",
                  "Effective and recorded times of the change"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-authorization-instrument-ref",
                "name": "Authorization instrument reference",
                "description": "Reference to the charter, agreement or directive that authorizes the project.",
                "value_kind": "reference",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-015"
                ]
              },
              {
                "id": "de-authorizing-body",
                "name": "Authorizing body reference",
                "description": "The party or governing body that granted authorization.",
                "value_kind": "reference",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-003"
                ]
              },
              {
                "id": "de-authorization-effective-time",
                "name": "Authorization effective time",
                "description": "Instant from which the authorization takes effect, distinct from the time the record was captured.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-012",
                  "SRC-003"
                ]
              },
              {
                "id": "de-delegated-tolerance",
                "name": "Delegated tolerance",
                "description": "A bounded delegation of authority expressed as a dimension, threshold and escalation target.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-003",
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "a-project-charter",
                "name": "Project charter or authorization decision record",
                "description": "The signed instrument establishing the project, its mandate, sponsor and delegated limits, retained across revisions.",
                "media_or_form": [
                  "signed document",
                  "governing-body decision minute",
                  "structured authorization record"
                ],
                "serial": true,
                "identity_strategy": "Named by the master project identifier plus artifact kind plus a zero-padded monotonic revision number; superseded revisions are retained and marked superseded-by, never overwritten.",
                "source_refs": [
                  "SRC-001",
                  "SRC-015",
                  "SRC-003"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "b-mandate-and-identity",
            "name": "Mandate and identity",
            "description": "Who and what this project is, who authorized it, who owns it and why the investment is justified."
          },
          "layer": {
            "id": "l-authority-and-mandate",
            "name": "Authority and mandate",
            "description": "The instrument that authorized the project, the parties accountable for it, and the investment justification that keeps it authorized."
          },
          "finding": {
            "id": "f-business-case-and-funding",
            "name": "Investment justification and funding commitment",
            "description": "The justification that keeps the project authorized, who committed what funding under which award and conditions, and which benefits the project itself is accountable for.",
            "source_refs": [
              "SRC-001",
              "SRC-019",
              "SRC-007",
              "SRC-014"
            ],
            "questions": [
              {
                "id": "q-business-case-revalidation",
                "text": "What justification supports continued investment, and when was it last re-validated against actual performance?",
                "kind": "decision",
                "answer_data": [
                  "Business case reference",
                  "Last re-validation time",
                  "Re-validation outcome",
                  "Deciding body"
                ]
              },
              {
                "id": "q-funding-conditions",
                "text": "Which funders committed what amounts under which award or agreement, and what conditions attach to each commitment?",
                "kind": "constraint",
                "answer_data": [
                  "Funder reference",
                  "Committed amount, currency and period",
                  "Award or agreement identifier",
                  "Condition text and compliance evidence"
                ]
              },
              {
                "id": "q-benefit-accountability-split",
                "text": "Which benefits is this project accountable for, and which are owned by a parent programme or by operations?",
                "kind": "relationship",
                "answer_data": [
                  "Benefit statement",
                  "Accountable party",
                  "Owning model reference",
                  "Realization horizon"
                ]
              },
              {
                "id": "q-tranche-release-evidence",
                "text": "What evidence must exist before the next funding tranche or stage authorization is released?",
                "kind": "evidence",
                "answer_data": [
                  "Required evidence item",
                  "Assessing role",
                  "Decision point reference",
                  "Consequence of non-satisfaction"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-business-case-ref",
                "name": "Business case reference",
                "description": "Reference to the investment justification document or structured record.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-014"
                ]
              },
              {
                "id": "de-funding-commitment",
                "name": "Funding commitment",
                "description": "A committed sum from a named funder, with currency, period, award reference and conditions.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-007",
                  "SRC-001"
                ]
              },
              {
                "id": "de-award-identifier",
                "name": "Award or grant identifier",
                "description": "Governed identifier of the award, grant or funding agreement under which the project is financed.",
                "value_kind": "identifier",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-011",
                  "SRC-010"
                ]
              },
              {
                "id": "de-benefit-claim-ref",
                "name": "Benefit claim reference",
                "description": "Reference to a benefit the project is accountable for, resolvable to the owning benefit or programme record.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-019",
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "a-business-case",
                "name": "Business case and funding decision record",
                "description": "The investment justification with its funding commitments, conditions and re-validation history.",
                "media_or_form": [
                  "document",
                  "structured investment record",
                  "funding decision minute"
                ],
                "serial": true,
                "identity_strategy": "Project identifier plus artifact kind plus monotonic version; each version pins the cost estimate and benefit assumptions current at its approval time.",
                "source_refs": [
                  "SRC-014",
                  "SRC-001"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "b-scope-and-structure",
            "name": "Scope and structure",
            "description": "What the project has committed to achieve and deliver, where its boundary lies, and how the total scope is decomposed and linked to contained records."
          },
          "layer": {
            "id": "l-objectives-and-scope-boundary",
            "name": "Objectives and scope boundary",
            "description": "The measurable ends the project is accountable for and the declared limit of what it will and will not do."
          },
          "finding": {
            "id": "f-objectives-and-success-criteria",
            "name": "Objectives and success criteria",
            "description": "The outputs, outcomes or benefits the project is accountable for, the measurable criteria that decide whether each is met, who judges satisfaction, and how conflicting objectives are prioritized.",
            "source_refs": [
              "SRC-016",
              "SRC-007",
              "SRC-001"
            ],
            "questions": [
              {
                "id": "q-objective-statement",
                "text": "What objectives is this project accountable for, expressed as outputs, outcomes or benefits?",
                "kind": "requirement",
                "answer_data": [
                  "Objective statement",
                  "Objective category",
                  "Accountable role",
                  "Linked scope element"
                ]
              },
              {
                "id": "q-success-criterion-target",
                "text": "What measurable criterion, indicator, baseline value and target decides whether each objective has been met?",
                "kind": "measurement",
                "answer_data": [
                  "Indicator name and definition",
                  "Measurement unit and method",
                  "Baseline value",
                  "Target value and target period"
                ]
              },
              {
                "id": "q-objective-satisfaction-judge",
                "text": "Who determines that a success criterion has been satisfied, and on what evidence?",
                "kind": "validation",
                "answer_data": [
                  "Deciding role",
                  "Evidence item reference",
                  "Decision time",
                  "Dispute or re-measurement route"
                ]
              },
              {
                "id": "q-objective-priority-conflict",
                "text": "How are objectives prioritized, and which one yields when two objectives cannot both be satisfied?",
                "kind": "constraint",
                "answer_data": [
                  "Priority rank or weighting",
                  "Trade-off rule",
                  "Authorizing role for trade-offs",
                  "Recorded trade-off decisions"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-objective-statement",
                "name": "Objective statement",
                "description": "A stated objective of the project expressed as an output, outcome or benefit.",
                "value_kind": "text",
                "cardinality": "1..n",
                "required": true,
                "source_refs": [
                  "SRC-016",
                  "SRC-001"
                ]
              },
              {
                "id": "de-success-criterion",
                "name": "Success criterion",
                "description": "Indicator, method, baseline and target that make an objective testable.",
                "value_kind": "object",
                "cardinality": "1..n",
                "required": true,
                "source_refs": [
                  "SRC-007",
                  "SRC-016"
                ]
              },
              {
                "id": "de-target-value",
                "name": "Target value",
                "description": "Quantified target for an indicator, with unit and target period.",
                "value_kind": "quantity",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-007"
                ]
              },
              {
                "id": "de-objective-priority",
                "name": "Objective priority",
                "description": "Relative priority or weighting used to resolve conflicts between objectives.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "a-objectives-and-results-register",
                "name": "Objectives, indicators and results register",
                "description": "Register of objectives with indicators, baselines, targets, actuals and the evidence supporting each measurement.",
                "media_or_form": [
                  "register",
                  "indicator and results table",
                  "structured results record"
                ],
                "serial": false,
                "identity_strategy": "Composite key of project identifier plus objective key plus indicator key; measured periods are attributes inside the row and never used as the row key.",
                "source_refs": [
                  "SRC-007",
                  "SRC-016"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "b-scope-and-structure",
            "name": "Scope and structure",
            "description": "What the project has committed to achieve and deliver, where its boundary lies, and how the total scope is decomposed and linked to contained records."
          },
          "layer": {
            "id": "l-objectives-and-scope-boundary",
            "name": "Objectives and scope boundary",
            "description": "The measurable ends the project is accountable for and the declared limit of what it will and will not do."
          },
          "finding": {
            "id": "f-scope-boundary-and-exclusions",
            "name": "Scope boundary, exclusions and scope confirmation",
            "description": "What is inside the authorized scope of work, what is explicitly excluded, which assumptions bound the statement, who may move the boundary, and how delivery of scope is confirmed.",
            "source_refs": [
              "SRC-001",
              "SRC-004",
              "SRC-022"
            ],
            "questions": [
              {
                "id": "q-scope-inclusion-exclusion",
                "text": "What work is inside the authorized scope and what is explicitly excluded from it?",
                "kind": "definition",
                "answer_data": [
                  "Scope statement",
                  "Explicit exclusion list",
                  "Boundary interface note",
                  "Scope baseline version"
                ]
              },
              {
                "id": "q-scope-change-authority",
                "text": "Which role must approve a movement of the scope boundary, and above what threshold does approval escalate?",
                "kind": "authority",
                "answer_data": [
                  "Approving role",
                  "Escalation threshold",
                  "Change request reference",
                  "Approval decision time"
                ]
              },
              {
                "id": "q-scope-delivery-confirmation",
                "text": "How is delivery of the scope confirmed, and who accepts it on behalf of the sponsor?",
                "kind": "validation",
                "answer_data": [
                  "Confirmation method",
                  "Accepting role",
                  "Confirmation record reference",
                  "Outstanding exception list"
                ]
              },
              {
                "id": "q-scope-assumptions",
                "text": "Which assumptions and constraints does the stated scope depend on, and what happens if one proves false?",
                "kind": "constraint",
                "answer_data": [
                  "Assumption statement",
                  "Dependency on external party",
                  "Invalidation consequence",
                  "Linked risk entry"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-scope-statement",
                "name": "Scope statement",
                "description": "Authoritative statement of the work the project is authorized to perform.",
                "value_kind": "text",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-004"
                ]
              },
              {
                "id": "de-scope-exclusion",
                "name": "Scope exclusion",
                "description": "Work explicitly declared outside the project boundary.",
                "value_kind": "text",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              },
              {
                "id": "de-scope-assumption",
                "name": "Scope assumption",
                "description": "An assumption the scope statement depends on, linkable to a risk entry.",
                "value_kind": "text",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-014"
                ]
              },
              {
                "id": "de-scope-confirmation-record",
                "name": "Scope confirmation record reference",
                "description": "Reference to the record confirming that delivered scope has been accepted.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-022"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "a-scope-baseline-statement",
                "name": "Scope baseline statement",
                "description": "The approved scope statement with exclusions and assumptions, held as the scope component of the baseline set.",
                "media_or_form": [
                  "document",
                  "structured scope record"
                ],
                "serial": true,
                "identity_strategy": "Project identifier plus artifact kind plus monotonic baseline version; content hash recorded so that later performance reporting can prove which scope it was measured against.",
                "source_refs": [
                  "SRC-001",
                  "SRC-013"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "b-scope-and-structure",
            "name": "Scope and structure",
            "description": "What the project has committed to achieve and deliver, where its boundary lies, and how the total scope is decomposed and linked to contained records."
          },
          "layer": {
            "id": "l-breakdown-and-linkage",
            "name": "Breakdown and linkage",
            "description": "Decomposition of the total scope and the typed edges binding the project to contained and external records."
          },
          "finding": {
            "id": "f-component-links-and-dependencies",
            "name": "Contained components and external dependencies",
            "description": "Which tasks, milestones and deliverables the project contains, by what link type, which external dependencies condition delivery, and what happens to those links when the project is cancelled, merged or split.",
            "source_refs": [
              "SRC-021",
              "SRC-004",
              "SRC-001",
              "SRC-006"
            ],
            "questions": [
              {
                "id": "q-contained-components",
                "text": "Which tasks, milestones and deliverables belong to this project, and under which typed edge is each held?",
                "kind": "composition",
                "answer_data": [
                  "Target record identifier",
                  "Link type code",
                  "Link direction",
                  "Link assertion time and asserting party"
                ]
              },
              {
                "id": "q-external-dependencies",
                "text": "Which dependencies on other projects, suppliers or external events condition this project's delivery?",
                "kind": "relationship",
                "answer_data": [
                  "Dependency target reference",
                  "Dependency nature",
                  "Needed-by date",
                  "Owner of the dependency"
                ]
              },
              {
                "id": "q-cross-model-link-resolution",
                "text": "How are cross-model links expressed so a consumer can resolve them without access to the project's storage system?",
                "kind": "interoperability",
                "answer_data": [
                  "Link serialization form",
                  "Target identifier scheme",
                  "Resolution endpoint",
                  "Fallback when the target is unresolvable"
                ]
              },
              {
                "id": "q-link-disposition-on-closure",
                "text": "What happens to contained components and their links when the project is cancelled, merged or split?",
                "kind": "lifecycle",
                "answer_data": [
                  "Disposition rule per link type",
                  "Reassignment target",
                  "Orphan handling policy",
                  "Event record of the disposition"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-contained-component-ref",
                "name": "Contained component reference",
                "description": "Typed reference from the project to a contained task, milestone or deliverable record.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-021",
                  "SRC-004"
                ]
              },
              {
                "id": "de-link-type-code",
                "name": "Link type code",
                "description": "Governed code naming the semantics of a typed edge, such as contains, depends-on or delivered-by.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-021"
                ]
              },
              {
                "id": "de-external-dependency",
                "name": "External dependency",
                "description": "A dependency on a record outside the project, with nature, needed-by date and responsible party.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-013",
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "a-component-link-set",
                "name": "Typed edge set",
                "description": "The set of typed edges binding the project to contained components, parent programme and external dependencies.",
                "media_or_form": [
                  "typed edge list",
                  "link table",
                  "graph fragment"
                ],
                "serial": false,
                "identity_strategy": "Each edge keyed by source identifier, link type and target identifier; hierarchical grouping is always expressed with explicit parent or child edge types rather than inferred from nesting or array order.",
                "source_refs": [
                  "SRC-021",
                  "SRC-006"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "b-resources-and-commitments",
            "name": "Resources and commitments",
            "description": "The people, money and supplier obligations bound to the project, and the authority behind each commitment."
          },
          "layer": {
            "id": "l-organization-and-people",
            "name": "Project organization and people",
            "description": "Roles in the project organization and the time-bounded commitment of people and physical resources to it."
          },
          "finding": {
            "id": "f-project-organization-and-roles",
            "name": "Project organization and role assignment",
            "description": "Which roles exist, who holds each and for what period, what decision rights attach to each role, and what competencies or clearances gate role holding.",
            "source_refs": [
              "SRC-001",
              "SRC-003",
              "SRC-015"
            ],
            "questions": [
              {
                "id": "q-role-holders",
                "text": "Which roles exist in the project organization and who currently holds each one?",
                "kind": "ownership",
                "answer_data": [
                  "Role name and definition",
                  "Role holder reference",
                  "Appointment record",
                  "Deputy or alternate"
                ]
              },
              {
                "id": "q-role-decision-rights",
                "text": "What responsibility, accountability and decision rights attach to each role?",
                "kind": "authority",
                "answer_data": [
                  "Responsibility statement",
                  "Accountable versus consulted distinction",
                  "Decision rights list",
                  "Escalation target"
                ]
              },
              {
                "id": "q-role-time-bounds",
                "text": "Over what period is each role assignment valid, and what record evidences a handover?",
                "kind": "temporal",
                "answer_data": [
                  "Assignment start and end",
                  "Handover record reference",
                  "Effective and recorded times",
                  "Overlap or gap note"
                ]
              },
              {
                "id": "q-role-prerequisites",
                "text": "Which competencies, certifications or clearances must be held before a person may occupy a role?",
                "kind": "requirement",
                "answer_data": [
                  "Prerequisite type",
                  "Verification evidence",
                  "Verifying party",
                  "Expiry of the prerequisite"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-project-role",
                "name": "Project role",
                "description": "A defined role in the project organization with its responsibilities and decision rights.",
                "value_kind": "object",
                "cardinality": "1..n",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-003"
                ]
              },
              {
                "id": "de-role-holder-ref",
                "name": "Role holder reference",
                "description": "Reference to the person or team occupying a role, resolved against the person or organization model.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-006"
                ]
              },
              {
                "id": "de-role-validity-period",
                "name": "Role validity period",
                "description": "Start and end of a role assignment, with effective and recorded times.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-012",
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "a-responsibility-assignment-record",
                "name": "Project organization and responsibility assignment record",
                "description": "Record of the project organization structure with role definitions, holders, validity periods and decision rights.",
                "media_or_form": [
                  "responsibility assignment matrix",
                  "organization structure record"
                ],
                "serial": true,
                "identity_strategy": "Project identifier plus artifact kind plus monotonic version; assignments keyed by role code and holder reference, with validity periods as attributes rather than keys.",
                "source_refs": [
                  "SRC-001",
                  "SRC-003"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "b-resources-and-commitments",
            "name": "Resources and commitments",
            "description": "The people, money and supplier obligations bound to the project, and the authority behind each commitment."
          },
          "layer": {
            "id": "l-organization-and-people",
            "name": "Project organization and people",
            "description": "Roles in the project organization and the time-bounded commitment of people and physical resources to it."
          },
          "finding": {
            "id": "f-resource-allocation-commitment",
            "name": "Resource allocation and commitment",
            "description": "Which resources are committed to the project in what quantity and period, who owns them, how contention is resolved, and what is recorded when an allocation changes mid-flight.",
            "source_refs": [
              "SRC-001",
              "SRC-018",
              "SRC-014"
            ],
            "questions": [
              {
                "id": "q-committed-resources",
                "text": "Which resources are committed to this project, in what quantity, and over which period?",
                "kind": "measurement",
                "answer_data": [
                  "Resource reference and type",
                  "Committed quantity and unit",
                  "Commitment period",
                  "Breakdown element consuming it"
                ]
              },
              {
                "id": "q-resource-commitment-authority",
                "text": "Who owns each committed resource and what instrument binds that commitment?",
                "kind": "ownership",
                "answer_data": [
                  "Resource owning party",
                  "Commitment instrument reference",
                  "Authorizing role",
                  "Commitment firmness level"
                ]
              },
              {
                "id": "q-resource-contention",
                "text": "How is over-allocation or contention with other projects detected, and who arbitrates it?",
                "kind": "exception",
                "answer_data": [
                  "Detection rule",
                  "Arbitrating body",
                  "Arbitration outcome record",
                  "Effect on the schedule baseline"
                ]
              },
              {
                "id": "q-allocation-change-event",
                "text": "What is recorded when resources are added, moved or withdrawn while work is in progress?",
                "kind": "event",
                "answer_data": [
                  "Change event type",
                  "Prior and new allocation values",
                  "Effective time and recorded time",
                  "Reason and authorizing role"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-resource-allocation",
                "name": "Resource allocation",
                "description": "A commitment of a named resource to project work, with quantity, period and consuming breakdown element.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-014"
                ]
              },
              {
                "id": "de-allocated-quantity",
                "name": "Allocated quantity",
                "description": "Quantity of a resource committed, expressed with an explicit unit of measure.",
                "value_kind": "quantity",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-005",
                  "SRC-014"
                ]
              },
              {
                "id": "de-allocation-owner-ref",
                "name": "Allocation owner reference",
                "description": "Reference to the party that owns and releases the committed resource.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-018"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "a-resource-commitment-record",
                "name": "Resource commitment record",
                "description": "Record binding resources to project work for a period, with owning party, authorizing role and change history.",
                "media_or_form": [
                  "allocation record",
                  "commitment agreement",
                  "structured resource ledger"
                ],
                "serial": true,
                "identity_strategy": "Project identifier plus artifact kind plus monotonic sequence; each entry references the resource owner's own identifier so that the owning party retains authority over its own allocation data.",
                "source_refs": [
                  "SRC-001",
                  "SRC-003"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "b-resources-and-commitments",
            "name": "Resources and commitments",
            "description": "The people, money and supplier obligations bound to the project, and the authority behind each commitment."
          },
          "layer": {
            "id": "l-funding-and-procurement",
            "name": "Budget and procurement",
            "description": "The approved cost baseline with its reserves and assumptions, and the externally sourced portion of scope."
          },
          "finding": {
            "id": "f-budget-and-cost-baseline",
            "name": "Budget, reserves and cost baseline",
            "description": "The approved time-phased budget with currency and price base, the distinction between baseline, commitment, forecast and actual cost, the reserves and who may release them, and the economic assumptions embedded in the numbers.",
            "source_refs": [
              "SRC-014",
              "SRC-005",
              "SRC-007",
              "SRC-001"
            ],
            "questions": [
              {
                "id": "q-approved-budget",
                "text": "What is the approved budget, in which currency and price base, and how is it phased across periods?",
                "kind": "measurement",
                "answer_data": [
                  "Budget amount per period",
                  "Currency code",
                  "Price base or reference year",
                  "Phasing method"
                ]
              },
              {
                "id": "q-cost-value-distinction",
                "text": "What distinguishes cost baseline from commitment, forecast and actual cost in this record?",
                "kind": "definition",
                "answer_data": [
                  "Definition per cost value type",
                  "Source system per type",
                  "Cut-off rule for actuals",
                  "Reconciliation rule"
                ]
              },
              {
                "id": "q-reserve-release-authority",
                "text": "Which contingency and management reserves exist, and which role may release each of them?",
                "kind": "authority",
                "answer_data": [
                  "Reserve type and amount",
                  "Holding level",
                  "Releasing role",
                  "Release decision record"
                ]
              },
              {
                "id": "q-cost-assumptions",
                "text": "Which exchange-rate, inflation and escalation assumptions underlie the cost figures?",
                "kind": "constraint",
                "answer_data": [
                  "Assumption type and value",
                  "Assumption source",
                  "Applicable period",
                  "Sensitivity or uncertainty range"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-approved-budget-amount",
                "name": "Approved budget amount",
                "description": "Budgeted amount for a period, with currency and price base, forming part of the cost baseline.",
                "value_kind": "quantity",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-014",
                  "SRC-007"
                ]
              },
              {
                "id": "de-currency-code",
                "name": "Currency code",
                "description": "Currency of a monetary value, recorded as an explicit code rather than implied by locale.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-007"
                ]
              },
              {
                "id": "de-reserve-amount",
                "name": "Reserve amount",
                "description": "Contingency or management reserve held against the project, with the role authorized to release it.",
                "value_kind": "quantity",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-014"
                ]
              },
              {
                "id": "de-actual-cost-to-date",
                "name": "Actual cost to date",
                "description": "Cost actually incurred as at the stated data date, distinct from commitment and forecast.",
                "value_kind": "quantity",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-005",
                  "SRC-014"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "a-cost-baseline",
                "name": "Time-phased cost baseline",
                "description": "The approved time-phased budget by control account with reserves, currency, price base and economic assumptions.",
                "media_or_form": [
                  "time-phased budget",
                  "financial baseline record"
                ],
                "serial": true,
                "identity_strategy": "Project identifier plus baseline type plus monotonic version, with a content hash; superseded cost baselines are retained so historic performance remains reproducible.",
                "source_refs": [
                  "SRC-014",
                  "SRC-005"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "b-time-lifecycle-and-baselines",
            "name": "Time, lifecycle and baselines",
            "description": "Where the project is in its life, what dates and gates govern it, and what approved baselines performance is measured against."
          },
          "layer": {
            "id": "l-baselines-and-change",
            "name": "Baselines and change control",
            "description": "The approved reference against which performance is judged, and the controlled route by which it may move."
          },
          "finding": {
            "id": "f-baseline-set-and-versioning",
            "name": "Approved baseline set and versioning",
            "description": "Which scope, schedule and cost baselines are currently approved, what authority established each, how superseded baselines are retained for reproducibility, and what forces a re-baseline rather than an in-baseline change.",
            "source_refs": [
              "SRC-013",
              "SRC-014",
              "SRC-005",
              "SRC-015"
            ],
            "questions": [
              {
                "id": "q-current-baseline-versions",
                "text": "Which scope, schedule and cost baselines are currently approved, and what version identifies each?",
                "kind": "identity",
                "answer_data": [
                  "Baseline type",
                  "Version identifier",
                  "Content hash",
                  "Coverage note"
                ]
              },
              {
                "id": "q-baseline-approval",
                "text": "Which approval established the current baseline and from what instant does it apply?",
                "kind": "authority",
                "answer_data": [
                  "Approving body",
                  "Approval decision reference",
                  "Effective time",
                  "Scope of the approval"
                ]
              },
              {
                "id": "q-superseded-baseline-retention",
                "text": "How are superseded baselines retained so that historic performance figures remain reproducible?",
                "kind": "provenance",
                "answer_data": [
                  "Superseded baseline reference",
                  "Retention location",
                  "Immutability mechanism",
                  "Link from performance data to baseline version"
                ]
              },
              {
                "id": "q-rebaseline-trigger",
                "text": "Which conditions require a full re-baseline rather than a change applied within the existing baseline?",
                "kind": "constraint",
                "answer_data": [
                  "Threshold or trigger condition",
                  "Deciding authority",
                  "Required analysis",
                  "Communication obligation"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-baseline-version",
                "name": "Baseline version",
                "description": "Version identifier of an approved baseline component.",
                "value_kind": "identifier",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-013",
                  "SRC-014"
                ]
              },
              {
                "id": "de-baseline-type",
                "name": "Baseline type",
                "description": "Which dimension the baseline covers: scope, schedule, cost or an integrated performance measurement baseline.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-005",
                  "SRC-014"
                ]
              },
              {
                "id": "de-baseline-approval-time",
                "name": "Baseline approval time",
                "description": "Instant at which a baseline was approved, with explicit offset.",
                "value_kind": "timestamp",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-012",
                  "SRC-015"
                ]
              },
              {
                "id": "de-superseded-baseline-ref",
                "name": "Superseded baseline reference",
                "description": "Reference from the current baseline to the version it replaced.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-013"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "a-baseline-package",
                "name": "Approved baseline package",
                "description": "Immutable snapshot bundling the approved scope, schedule and cost baselines with their approval evidence.",
                "media_or_form": [
                  "immutable snapshot",
                  "versioned package",
                  "structured baseline record"
                ],
                "serial": true,
                "identity_strategy": "Project identifier plus baseline type plus zero-padded monotonic version, with a named-algorithm content hash; the approval date is metadata inside the package and never forms the key.",
                "source_refs": [
                  "SRC-013",
                  "SRC-014",
                  "SRC-015"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "b-time-lifecycle-and-baselines",
            "name": "Time, lifecycle and baselines",
            "description": "Where the project is in its life, what dates and gates govern it, and what approved baselines performance is measured against."
          },
          "layer": {
            "id": "l-baselines-and-change",
            "name": "Baselines and change control",
            "description": "The approved reference against which performance is judged, and the controlled route by which it may move."
          },
          "finding": {
            "id": "f-change-control",
            "name": "Change control against baselines",
            "description": "How change requests are raised, impact-assessed and decided, which thresholds escalate them, how a decided change links to the baseline version it altered, and how rejected requests are retained.",
            "source_refs": [
              "SRC-001",
              "SRC-022",
              "SRC-014",
              "SRC-003"
            ],
            "questions": [
              {
                "id": "q-change-request-flow",
                "text": "How is a change request raised, assessed for scope, schedule, cost and risk impact, and decided?",
                "kind": "process",
                "answer_data": [
                  "Request record fields",
                  "Impact assessment method",
                  "Deciding role or body",
                  "Decision outcome codes"
                ]
              },
              {
                "id": "q-change-escalation-threshold",
                "text": "Which thresholds move a change decision beyond the project manager's delegated authority?",
                "kind": "authority",
                "answer_data": [
                  "Threshold dimension and value",
                  "Escalation target",
                  "Approval evidence",
                  "Emergency deviation route"
                ]
              },
              {
                "id": "q-change-baseline-link",
                "text": "What links an approved change to the specific baseline version it altered?",
                "kind": "relationship",
                "answer_data": [
                  "Change request identifier",
                  "Prior and resulting baseline versions",
                  "Affected breakdown elements",
                  "Application time"
                ]
              },
              {
                "id": "q-rejected-change-retention",
                "text": "How long are rejected and withdrawn change requests retained, and who may see them?",
                "kind": "retention",
                "answer_data": [
                  "Retention period",
                  "Disposition action",
                  "Access restriction",
                  "Retention authority reference"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-change-request",
                "name": "Change request",
                "description": "A proposed alteration to a baseline, with originator, description and requested effect.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-022"
                ]
              },
              {
                "id": "de-change-impact-assessment",
                "name": "Change impact assessment",
                "description": "Assessed effect of a change on scope, schedule, cost, risk and benefits.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-014",
                  "SRC-001"
                ]
              },
              {
                "id": "de-change-decision-code",
                "name": "Change decision code",
                "description": "Outcome of the change decision, such as approved, rejected, deferred or withdrawn.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-003"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "a-change-request-register",
                "name": "Change request register",
                "description": "Register of change requests with impact assessments, decisions, authorizing roles and the baseline versions affected.",
                "media_or_form": [
                  "register",
                  "decision log",
                  "structured change record"
                ],
                "serial": true,
                "identity_strategy": "Project identifier plus artifact kind plus monotonic request number; decisions are appended as new entries linked to the request number, and rejected requests are retained rather than deleted.",
                "source_refs": [
                  "SRC-001",
                  "SRC-014"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "b-performance-and-uncertainty",
            "name": "Performance and uncertainty",
            "description": "How the project is actually going, how that is measured and reported, and how threats, problems and quality are handled."
          },
          "layer": {
            "id": "l-measurement-and-reporting",
            "name": "Measurement and reporting",
            "description": "Quantified progress against the approved baseline and the obligation to report it."
          },
          "finding": {
            "id": "f-progress-and-earned-value",
            "name": "Progress measurement and earned value",
            "description": "How physical progress is measured per control account, which indices and variances are computed against which baseline, the data date of the performance figures, the checks that keep them internally consistent, and what is used when earned value does not apply.",
            "source_refs": [
              "SRC-005",
              "SRC-014",
              "SRC-013"
            ],
            "questions": [
              {
                "id": "q-progress-technique",
                "text": "How is physical progress measured for each control account, using which technique, unit and frequency?",
                "kind": "measurement",
                "answer_data": [
                  "Measurement technique code",
                  "Unit of measure",
                  "Measurement frequency",
                  "Responsible role"
                ]
              },
              {
                "id": "q-performance-data-date",
                "text": "What is the data date of the performance figures, and how often are they refreshed?",
                "kind": "temporal",
                "answer_data": [
                  "Data date",
                  "Refresh cadence",
                  "Last computation time",
                  "Lag between data date and publication"
                ]
              },
              {
                "id": "q-performance-consistency-check",
                "text": "Which checks confirm that reported earned value is consistent with actual cost, schedule status and the named baseline?",
                "kind": "validation",
                "answer_data": [
                  "Consistency rule set",
                  "Tolerance for discrepancy",
                  "Failed-check handling",
                  "Verifying role"
                ]
              },
              {
                "id": "q-earned-value-inapplicable",
                "text": "When is earned value not an appropriate measure for this project, and what alternative measure is used instead?",
                "kind": "constraint",
                "answer_data": [
                  "Inapplicability condition",
                  "Alternative measure and method",
                  "Approval of the alternative",
                  "Comparability limitation"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-control-account-progress",
                "name": "Control account progress",
                "description": "Measured progress for a control account at a stated data date, with technique and unit.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-005",
                  "SRC-014"
                ]
              },
              {
                "id": "de-earned-value-metric",
                "name": "Earned value metric",
                "description": "A computed performance value or index, recorded with the baseline version it was computed against.",
                "value_kind": "quantity",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-005"
                ]
              },
              {
                "id": "de-performance-data-date",
                "name": "Performance data date",
                "description": "The as-of instant for a set of performance figures, separate from the time they were computed or ingested.",
                "value_kind": "timestamp",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-012",
                  "SRC-005"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "a-performance-measurement-record",
                "name": "Performance measurement dataset",
                "description": "Periodic dataset of progress, earned value and variance by control account, bound to a data date and a baseline version.",
                "media_or_form": [
                  "periodic dataset",
                  "measurement table",
                  "structured performance record"
                ],
                "serial": true,
                "identity_strategy": "Project identifier plus artifact kind plus monotonic period sequence; the data date and baseline version are recorded inside the dataset so that reruns are reproducible and periods are never used as identifiers.",
                "source_refs": [
                  "SRC-005",
                  "SRC-014"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "b-performance-and-uncertainty",
            "name": "Performance and uncertainty",
            "description": "How the project is actually going, how that is measured and reported, and how threats, problems and quality are handled."
          },
          "layer": {
            "id": "l-measurement-and-reporting",
            "name": "Measurement and reporting",
            "description": "Quantified progress against the approved baseline and the obligation to report it."
          },
          "finding": {
            "id": "f-status-reporting-and-forecast",
            "name": "Status reporting, forecast and disclosure",
            "description": "Who must receive which report at what cadence and detail, what forecast is asserted and on what basis, how report assertions trace to underlying performance data, and which external disclosure obligations apply.",
            "source_refs": [
              "SRC-001",
              "SRC-007",
              "SRC-014",
              "SRC-003"
            ],
            "questions": [
              {
                "id": "q-report-obligations",
                "text": "Who must receive which report, at what cadence and at what level of detail?",
                "kind": "requirement",
                "answer_data": [
                  "Recipient role or body",
                  "Report type",
                  "Cadence and due offset",
                  "Detail or projection level"
                ]
              },
              {
                "id": "q-forecast-basis",
                "text": "What forecast of final cost and completion date is asserted, and on what basis is it derived?",
                "kind": "measurement",
                "answer_data": [
                  "Forecast value and type",
                  "Derivation method",
                  "Assumptions and confidence range",
                  "Forecast as-of date"
                ]
              },
              {
                "id": "q-report-traceability",
                "text": "How is each reported assertion traced back to the underlying performance data and its data date?",
                "kind": "provenance",
                "answer_data": [
                  "Source dataset reference",
                  "Data date of the source",
                  "Transformation or aggregation applied",
                  "Preparing and approving roles"
                ]
              },
              {
                "id": "q-external-disclosure",
                "text": "Which external transparency or funder-reporting obligations apply to this project's status, and what must be published?",
                "kind": "access",
                "answer_data": [
                  "Obligation source",
                  "Publication target and schema",
                  "Fields required to be public",
                  "Fields withheld and the ground for withholding"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-report-obligation",
                "name": "Report obligation",
                "description": "An obligation to deliver a specified report to a named recipient at a stated cadence.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-003"
                ]
              },
              {
                "id": "de-forecast-value",
                "name": "Forecast value",
                "description": "Forecast final cost, completion date or benefit level, with its derivation basis.",
                "value_kind": "quantity",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-014",
                  "SRC-005"
                ]
              },
              {
                "id": "de-report-last-updated-time",
                "name": "Report last-updated time",
                "description": "Instant at which the reported data was last updated, supporting consumer freshness checks.",
                "value_kind": "timestamp",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-007",
                  "SRC-012"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "a-status-report",
                "name": "Periodic status report",
                "description": "Report covering a defined period with progress against objectives, forecast, top risks and issues, and its traceability to the underlying data.",
                "media_or_form": [
                  "report",
                  "structured status record",
                  "published data record"
                ],
                "serial": true,
                "identity_strategy": "Project identifier plus artifact kind plus zero-padded monotonic sequence; the reporting period is stored inside the report as bounded RFC 3339 instants and is never the identifier.",
                "source_refs": [
                  "SRC-001",
                  "SRC-007",
                  "SRC-012"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "b-stakeholders-records-and-closure",
            "name": "Stakeholders, records and closure",
            "description": "Who has an interest in the project, how its record is evidenced and protected, and how it ends and is retained."
          },
          "layer": {
            "id": "l-closure-and-retention",
            "name": "Closure and retention",
            "description": "How the project ends, what is learned and handed over, and how the record is retained or disposed of afterwards."
          },
          "finding": {
            "id": "f-closure-and-lessons",
            "name": "Closure, handover and lessons",
            "description": "What conditions permit closure, how the closure outcome is classified, what is handed over to operations or a parent programme, and how lessons are captured so they can be found by later projects.",
            "source_refs": [
              "SRC-001",
              "SRC-008",
              "SRC-019",
              "SRC-022"
            ],
            "questions": [
              {
                "id": "q-closure-conditions",
                "text": "What conditions must be satisfied before the project may be formally closed, and who confirms them?",
                "kind": "requirement",
                "answer_data": [
                  "Closure condition list",
                  "Confirming role",
                  "Outstanding exception disposition",
                  "Closure decision reference"
                ]
              },
              {
                "id": "q-closure-outcome-classification",
                "text": "How is the closure outcome classified, distinguishing completion from cancellation, merger and abandonment?",
                "kind": "classification",
                "answer_data": [
                  "Outcome code and vocabulary",
                  "Reason narrative",
                  "Residual obligations",
                  "Final state effective time"
                ]
              },
              {
                "id": "q-handover-targets",
                "text": "What is handed over at closure, to whom, and who becomes accountable for continuing benefits and support?",
                "kind": "ownership",
                "answer_data": [
                  "Handover item list",
                  "Receiving party",
                  "Acceptance evidence",
                  "Post-closure benefit owner"
                ]
              },
              {
                "id": "q-lessons-capture",
                "text": "How are lessons captured, classified and made discoverable to later projects?",
                "kind": "quality",
                "answer_data": [
                  "Lesson statement and context",
                  "Classification tags",
                  "Publication target",
                  "Review or validation of the lesson"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-closure-outcome-code",
                "name": "Closure outcome code",
                "description": "Classified outcome of closure drawn from a declared vocabulary.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-008",
                  "SRC-001"
                ]
              },
              {
                "id": "de-handover-item",
                "name": "Handover item",
                "description": "An item transferred at closure, with receiving party and acceptance evidence.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-019"
                ]
              },
              {
                "id": "de-lesson-entry",
                "name": "Lesson entry",
                "description": "A captured lesson with context, classification and publication target.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-022"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "a-closure-report",
                "name": "Closure report and lessons record",
                "description": "Final account of outcome against objectives, handover items and acceptance, residual obligations and captured lessons.",
                "media_or_form": [
                  "closure report",
                  "lessons record",
                  "structured closure dataset"
                ],
                "serial": true,
                "identity_strategy": "Project identifier plus artifact kind plus monotonic version; the closure decision time is metadata inside the report, and any post-closure correction is a new version with a superseded-by link.",
                "source_refs": [
                  "SRC-001",
                  "SRC-019"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        }
      ],
      "functions": [
        {
          "id": "fn-register-project",
          "name": "Register project",
          "description": "Create a project record with a resolvable identity and a declared authorization posture.",
          "inputs": [
            "Master system reference",
            "Proposed or issued authoritative identifier",
            "Project name and type classification",
            "Sponsoring organization reference"
          ],
          "outputs": [
            "Project record with authoritative identifier",
            "Identifier registration record",
            "Provenance statement of creation"
          ],
          "preconditions": [
            "The master system of record is named and reachable, or an explicit mint request is authorized",
            "The sponsoring organization reference resolves",
            "No existing record already carries the same authoritative identifier"
          ],
          "effects": [
            "A project record exists in state proposed or authorized",
            "Identity and classification findings are populated",
            "Creation is attributed to an agent with an ingestion timestamp"
          ],
          "source_refs": [
            "SRC-010",
            "SRC-011",
            "SRC-006"
          ]
        },
        {
          "id": "fn-authorize-project",
          "name": "Authorize project",
          "description": "Record the instrument, body and effective time that authorize the project and set its delegated tolerances.",
          "inputs": [
            "Authorization instrument reference",
            "Authorizing body reference",
            "Delegated tolerance set",
            "Effective time"
          ],
          "outputs": [
            "Charter or authorization artifact revision",
            "Updated mandate finding",
            "State transition entry"
          ],
          "preconditions": [
            "A project record exists",
            "The authorizing body holds the reserved decision for authorization",
            "The instrument reference resolves to a retained artifact"
          ],
          "effects": [
            "The project moves to an authorized state",
            "Tolerances become enforceable for change escalation",
            "The prior charter revision is retained and marked superseded"
          ],
          "source_refs": [
            "SRC-003",
            "SRC-001",
            "SRC-015"
          ]
        },
        {
          "id": "fn-establish-baseline",
          "name": "Establish baseline",
          "description": "Approve and freeze a scope, schedule or cost baseline as the reference for performance measurement.",
          "inputs": [
            "Baseline type",
            "Candidate baseline content",
            "Approving body reference",
            "Approval time"
          ],
          "outputs": [
            "Immutable baseline package with version and content hash",
            "Superseded-by link on the prior baseline",
            "Approval decision record"
          ],
          "preconditions": [
            "The scope is decomposed into mutually exclusive elements",
            "The approving body is authorized for the baseline type",
            "Any dependent change requests are decided"
          ],
          "effects": [
            "A new current baseline version exists",
            "Prior baselines remain retrievable for reproducing historic variance",
            "Performance measurement is bound to the new version"
          ],
          "source_refs": [
            "SRC-013",
            "SRC-014",
            "SRC-005"
          ]
        },
        {
          "id": "fn-transition-lifecycle-state",
          "name": "Transition lifecycle state",
          "description": "Move the project to a new state in its declared vocabulary, recording effective and recorded times separately.",
          "inputs": [
            "Target state code and vocabulary version",
            "Effective time",
            "Triggering actor",
            "Reason code and evidence reference"
          ],
          "outputs": [
            "Appended state transition entry",
            "Updated current state",
            "Notification to obligated recipients"
          ],
          "preconditions": [
            "The transition is permitted from the current state",
            "The triggering actor holds the authority for that transition",
            "Required evidence for the transition is attached"
          ],
          "effects": [
            "Current state changes from the effective time",
            "History remains append-only and reconstructable",
            "Downstream reporting and access rules re-evaluate"
          ],
          "source_refs": [
            "SRC-008",
            "SRC-001",
            "SRC-012"
          ]
        },
        {
          "id": "fn-record-gate-decision",
          "name": "Record gate decision",
          "description": "Capture a governing-body decision at a phase gate, including conditional outcomes and required actions.",
          "inputs": [
            "Gate identifier",
            "Products reviewed",
            "Deciding body reference",
            "Outcome code and conditions"
          ],
          "outputs": [
            "Gate decision record",
            "Action items with owners and due dates",
            "Authorization to proceed or to hold"
          ],
          "preconditions": [
            "Gate entry criteria are evidenced",
            "The deciding body is quorate and independent where required",
            "The applicable gate set reflects any approved tailoring"
          ],
          "effects": [
            "Continuation of work is authorized, conditioned or stopped",
            "Conditions become tracked obligations",
            "Assurance evidence is retained for audit"
          ],
          "source_refs": [
            "SRC-015",
            "SRC-003",
            "SRC-001"
          ]
        },
        {
          "id": "fn-decide-change-request",
          "name": "Decide change request",
          "description": "Assess a proposed change against baselines and tolerances, decide it and link the decision to the affected baseline version.",
          "inputs": [
            "Change request record",
            "Impact assessment across scope, schedule, cost and risk",
            "Deciding role reference"
          ],
          "outputs": [
            "Change decision with outcome code",
            "Link from the change to prior and resulting baseline versions",
            "Updated tolerance consumption"
          ],
          "preconditions": [
            "A current approved baseline exists",
            "The deciding role is within the delegated threshold or the change has been escalated",
            "Impact assessment is complete"
          ],
          "effects": [
            "Approved changes trigger a controlled baseline update",
            "Rejected and withdrawn requests are retained with their reasoning",
            "Traceability from performance data to the correct baseline is preserved"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-014",
            "SRC-003"
          ]
        },
        {
          "id": "fn-record-performance-measurement",
          "name": "Record performance measurement",
          "description": "Ingest or compute progress and earned value at a stated data date against a named baseline version.",
          "inputs": [
            "Control account progress values",
            "Actual cost values",
            "Baseline version reference",
            "Data date"
          ],
          "outputs": [
            "Performance measurement dataset",
            "Computed variances and indices",
            "Consistency check results"
          ],
          "preconditions": [
            "A performance measurement baseline is approved",
            "Measurement techniques are declared per control account",
            "The data date is not in the future relative to the recording time"
          ],
          "effects": [
            "Performance figures become reportable and reproducible",
            "Inconsistent data is flagged rather than silently published",
            "Forecast derivation gains a dated basis"
          ],
          "source_refs": [
            "SRC-005",
            "SRC-014",
            "SRC-012"
          ]
        },
        {
          "id": "fn-link-component",
          "name": "Link component",
          "description": "Create or retire a typed edge between the project and a contained, parent or external record.",
          "inputs": [
            "Source project identifier",
            "Target record identifier and scheme",
            "Link type code",
            "Asserting agent"
          ],
          "outputs": [
            "Typed edge in the link set",
            "Provenance statement for the assertion",
            "Validation result on target resolvability"
          ],
          "preconditions": [
            "The target record exists and its identifier resolves",
            "The link type is in the governed link vocabulary",
            "Hierarchical grouping uses explicit parent or child edge types"
          ],
          "effects": [
            "Containment and dependency become traversable without storage-specific nesting",
            "Retired edges are marked rather than removed",
            "Closure disposition rules can be applied per link type"
          ],
          "source_refs": [
            "SRC-021",
            "SRC-004",
            "SRC-006"
          ]
        },
        {
          "id": "fn-publish-status-report",
          "name": "Publish status report",
          "description": "Produce and release a periodic report to obligated recipients at the required cadence and detail, honouring disclosure and withholding rules.",
          "inputs": [
            "Reporting period bounds",
            "Performance dataset reference",
            "Forecast values",
            "Recipient and obligation set"
          ],
          "outputs": [
            "Status report artifact",
            "Publication record for externally mandated fields",
            "Traceability links to source data"
          ],
          "preconditions": [
            "Performance data exists with a data date inside or before the period",
            "Access classification has been applied to each field",
            "Withholding decisions are approved where fields are suppressed"
          ],
          "effects": [
            "Reporting obligations are discharged and evidenced",
            "Consumers can check freshness through a last-updated time",
            "Withheld fields carry a recorded ground rather than silently vanishing"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-007",
            "SRC-003"
          ]
        },
        {
          "id": "fn-close-and-dispose-project",
          "name": "Close and apply disposition",
          "description": "Formally close the project, classify the outcome, hand over residual obligations and place the record under its retention schedule.",
          "inputs": [
            "Closure conditions evidence",
            "Closure outcome code",
            "Handover items and receiving parties",
            "Applicable retention schedule reference"
          ],
          "outputs": [
            "Closure report and lessons record",
            "Final state transition entry",
            "Retention and disposition record"
          ],
          "preconditions": [
            "Open issues and change requests are dispositioned or transferred",
            "Scope delivery is confirmed or the shortfall is recorded",
            "No legal hold blocks the intended disposition path"
          ],
          "effects": [
            "The project reaches a terminal state with a classified outcome",
            "Post-closure accountability for benefits and support is assigned",
            "Records enter a scheduled retention regime with holds honoured"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-020",
            "SRC-008"
          ]
        },
        {
          "id": "fn-validate-project-record",
          "name": "Validate project record",
          "description": "Run the model's validation rules over a project record and report violations without mutating the record.",
          "inputs": [
            "Project record",
            "Active vocabulary versions",
            "Validation rule set"
          ],
          "outputs": [
            "Violation list with severity and rule reference",
            "Pass or fail summary",
            "Suggested remediation per violation"
          ],
          "preconditions": [
            "The record's declared vocabularies resolve",
            "Baseline references resolve to retained packages"
          ],
          "effects": [
            "Date ordering, future-date, identifier resolution and breakdown-coverage defects are surfaced",
            "Records failing required checks can be blocked from publication",
            "Validation runs are themselves attributable and timestamped"
          ],
          "source_refs": [
            "SRC-009",
            "SRC-004",
            "SRC-012",
            "SRC-006"
          ]
        },
        {
          "id": "fn-commit-resources",
          "name": "Commit resources",
          "description": "Bind allocations of people, funds or assets from a resource owner to WBS elements for a stated period.",
          "inputs": [
            "Resource owner commitment",
            "Target WBS elements and period"
          ],
          "outputs": [
            "Allocation records bound to WBS elements for a stated period"
          ],
          "preconditions": [
            "A resource-owning party has committed the resource"
          ],
          "effects": [
            "People, funds or assets are committed to the project while ownership stays with the providing party"
          ],
          "source_refs": [
            "SRC-027",
            "SRC-028"
          ]
        },
        {
          "id": "fn-raise-risk-or-issue",
          "name": "Raise risk or issue",
          "description": "Log an uncertain threat or opportunity or a realized issue, assign ownership and response, and escalate exceptions beyond tolerance.",
          "inputs": [
            "Identified threat, opportunity or realized issue"
          ],
          "outputs": [
            "Register entry with owner and response"
          ],
          "preconditions": [
            "Tolerances for manage-by-exception are defined"
          ],
          "effects": [
            "Exceptions beyond tolerance are escalated without deleting the project-level record"
          ],
          "source_refs": [
            "SRC-026",
            "SRC-030",
            "SRC-027"
          ]
        },
        {
          "id": "fn-tailor-and-exchange",
          "name": "Tailor method and exchange record",
          "description": "Record the method profile and tailoring, and export or import a projection under a named interchange profile without claiming unearned conformance.",
          "inputs": [
            "Adopted method profile and tailoring decisions",
            "Named interchange profile"
          ],
          "outputs": [
            "Recorded method profile, tailoring and waivers",
            "Exported or imported projection under the named profile"
          ],
          "preconditions": [
            "Tailoring is approved by the requirement owner or authorized approver"
          ],
          "effects": [
            "Alignment is recorded without being upgraded to a conformance claim",
            "Mapping losses of the exchange are declared"
          ],
          "source_refs": [
            "SRC-027",
            "SRC-030",
            "SRC-006"
          ]
        }
      ],
      "composition": [
        {
          "target": "WM-ACT-006 Task",
          "relation": "CHILD",
          "purpose": "The project contains assignable work units; the project holds decomposition to work-package or control-account level and delegates execution detail, effort and task state to the task model through typed contains edges.",
          "required": true,
          "source_refs": [
            "SRC-004",
            "SRC-021"
          ]
        },
        {
          "target": "WM-ACT-031 Milestone and Deliverable",
          "relation": "CHILD",
          "purpose": "The project contains dated checkpoints and defined outputs; it gates and reports against them while their acceptance criteria and internal versions stay in the contained model.",
          "required": true,
          "source_refs": [
            "SRC-001",
            "SRC-004"
          ]
        },
        {
          "target": "WM-ACT-029 Programme and Portfolio",
          "relation": "REFERENCE",
          "purpose": "Reference upward to the parent programme or portfolio that selected and contains this project; benefit aggregation and component balancing remain there. The containment edge is asserted from the parent side and must not be duplicated as a child edge here.",
          "required": false,
          "source_refs": [
            "SRC-019",
            "SRC-018",
            "SRC-021"
          ]
        },
        {
          "target": "Organization model (sponsoring and participating parties)",
          "relation": "REFERENCE",
          "purpose": "Resolve the sponsoring organization, governing body, funders and suppliers by their own authoritative identifiers instead of copying organization master data into the project record.",
          "required": true,
          "source_refs": [
            "SRC-007",
            "SRC-003"
          ]
        },
        {
          "target": "Person model (role holders and contributors)",
          "relation": "REFERENCE",
          "purpose": "Resolve role holders, risk owners and contributors, keeping personal data minimized in the project record and governed by the person model.",
          "required": false,
          "source_refs": [
            "SRC-010",
            "SRC-001"
          ]
        },
        {
          "target": "Plan and schedule model",
          "relation": "REFERENCE",
          "purpose": "Bind the approved schedule baseline and authoritative dates while leaving activity network logic, durations, float and critical-path computation to the schedule model.",
          "required": false,
          "source_refs": [
            "SRC-013",
            "SRC-001"
          ]
        },
        {
          "target": "Act and action model",
          "relation": "REFERENCE",
          "purpose": "Resolve performed work to recorded acts for provenance and effort evidence without turning the project record into an activity log.",
          "required": false,
          "source_refs": [
            "SRC-006",
            "SRC-001"
          ]
        },
        {
          "target": "Process and workflow model",
          "relation": "REFERENCE",
          "purpose": "Reference repeatable procedures applied inside the unique undertaking, preserving the project-versus-process distinction.",
          "required": false,
          "source_refs": [
            "SRC-016",
            "SRC-002"
          ]
        },
        {
          "target": "Ownership and access service models",
          "relation": "MIX-IN",
          "purpose": "Inherit record ownership, access grant and audit machinery from the catalogue's ownership and access models rather than defining bespoke access control inside this model.",
          "required": true,
          "source_refs": [
            "SRC-003",
            "SRC-010"
          ]
        },
        {
          "target": "W3C PROV-O",
          "relation": "ALIGN",
          "purpose": "Align project provenance to Entity, Activity, Agent, Plan and Association, using wasAttributedTo, wasAssociatedWith, actedOnBehalfOf, startedAtTime and endedAtTime for attribution and delegation. Alignment only; conformance is not asserted.",
          "required": false,
          "source_refs": [
            "SRC-006"
          ]
        },
        {
          "target": "ISO 21502:2020 project management practices",
          "relation": "ALIGN",
          "purpose": "Align the management-practice findings to the standard's clause structure for benefits, scope, resources, schedule, cost, risk, issue, change control, quality, stakeholders, reports, information management, acquisitions and lessons learned.",
          "required": false,
          "source_refs": [
            "SRC-001",
            "SRC-022"
          ]
        },
        {
          "target": "ISO 21511:2018 work breakdown structures",
          "relation": "ALIGN",
          "purpose": "Align decomposition semantics and relationships to other breakdown structures; the standard gives guidance rather than a mandate, so a WBS is expected but not required by this model.",
          "required": false,
          "source_refs": [
            "SRC-004"
          ]
        },
        {
          "target": "ISO 21508:2018 earned value management",
          "relation": "ALIGN",
          "purpose": "Align progress and performance measurement to earned value concepts where an organization applies them, including the prerequisite of mutually exclusive scope elements.",
          "required": false,
          "source_refs": [
            "SRC-005"
          ]
        },
        {
          "target": "IATI Activity Standard 2.03",
          "relation": "ALIGN",
          "purpose": "Align publication of identity, status, type-coded dates, budgets, participating organizations, locations and results for projects under aid transparency obligations; IATI activities are not necessarily one-to-one with projects.",
          "required": false,
          "source_refs": [
            "SRC-007",
            "SRC-008",
            "SRC-009",
            "SRC-021"
          ]
        },
        {
          "target": "RAiD (ISO 23527:2022) and DataCite Metadata Schema 4.6",
          "relation": "ALIGN",
          "purpose": "Align to governed global project identifiers and citable project metadata so that a project can be referenced persistently outside its master system.",
          "required": false,
          "source_refs": [
            "SRC-010",
            "SRC-011"
          ]
        },
        {
          "target": "schema.org Project",
          "relation": "ALIGN",
          "purpose": "Provide a lossy publication mapping for web discovery only. schema.org types Project as a subtype of Organization, which conflicts with the temporary-endeavour definition, so the mapping must not be reversed into the canonical model.",
          "required": false,
          "source_refs": [
            "SRC-017",
            "SRC-016"
          ]
        },
        {
          "target": "Records disposition authority (for example a NARA General Records Schedule or an equivalent national schedule)",
          "relation": "EXTEND",
          "purpose": "Extend the retention finding with the jurisdiction's binding disposition authority, which supplies retention periods, hold rules and deviation procedures that this model deliberately does not invent.",
          "required": false,
          "source_refs": [
            "SRC-020"
          ]
        }
      ],
      "researchAdjudication": {
        "providerMode": "dual-provider",
        "activeProviders": [
          "claude",
          "grok"
        ],
        "waivedProviders": [],
        "providerPolicy": {},
        "boundaryDecision": {
          "entry_kind": "aggregate",
          "status": "accepted",
          "rationale": "Both providers independently reached entry_kind=aggregate for vr.wm-act-005 and drew the same containment lines: the project owns decomposition to work-package/control-account level and holds typed edges to WM-ACT-006 tasks and WM-ACT-031 milestones/deliverables rather than restating their internals, references WM-ACT-029 programme/portfolio upward, and delegates schedule-network logic, repeatable process definitions and person/organization master data to siblings. Claude's boundary_notes additionally settle the three hard cases with evidence — schema.org's Project-as-Organization modelling is declared a lossy publication-only alignment rather than reconciled, IATI activity is an alignment and publication target rather than an identity authority, and PROV Activity/Plan supplies attribution semantics without the project becoming the provenance graph of every act. That is a complete, non-overlapping boundary, so the model boundary and entry kind are fixed before any node is accepted."
        },
        "decisions": [
          {
            "concept": "Base provider selection",
            "disposition": "claude as base",
            "rationale": "Not chosen on size. Claude's scope_statement, in_scope/out_of_scope and eight sourced boundary_notes settle every adjacent model (programme/portfolio, task, milestone/deliverable, plan/schedule, process, PROV, schema.org, IATI) with an explicit ownership rule and typed-edge delegation, and its six bundles decompose without overlap. Grok reorganizes much of the same material but leaves boundary work partly as method caveats rather than model boundaries."
          },
          {
            "concept": "Entry kind",
            "disposition": "accepted as aggregate",
            "rationale": "Both providers independently assert aggregate and both implement it the same way — the project owns registration, mandate, breakdown and baselines while contained tasks and milestones/deliverables are referenced by typed edge, never copied. No adjudication needed beyond recording the agreement."
          },
          {
            "concept": "Method tailoring, waivers and compliance matrix",
            "disposition": "accepted into l-authority-and-mandate",
            "rationale": "Wholly net-new against the base and backed by three independent regimes (NASA compliance matrix with deviations and waivers, PRINCE2 tailoring, GovS 002 mandated application). It also gives the base a structural home for the alignment-is-not-conformance rule that Claude otherwise states only in prose."
          },
          {
            "concept": "Transition, disposal and residual obligations at close",
            "disposition": "accepted into l-closure-and-retention",
            "rationale": "Asset disposal, decommissioning, data archival and the warranty, classified-material and liability tail that outlives operational close appear nowhere in the base closure or retention findings and are not listed among its known omissions. Partial overlap on close disposition is accepted because the net-new half is material and the layer is the exact right home."
          },
          {
            "concept": "Charter and continued business justification (grok)",
            "disposition": "rejected as duplicative",
            "rationale": "The base already holds the authorization instrument, signer, delegated tolerances and authorization continuity on re-baseline, suspension or transfer in f-charter-and-authorization, and business-case re-validation against actual performance in f-business-case-and-funding. Withdrawal of justification is already reachable through the abnormal-termination question."
          },
          {
            "concept": "Goals, scope, benefits and boundaries (grok)",
            "disposition": "rejected as duplicative",
            "rationale": "Fully covered by f-objectives-and-success-criteria and f-scope-boundary-and-exclusions, including the benefit accountability split between project, parent programme and operations that grok raises. Adding it would create a second scope statement inside the same model."
          },
          {
            "concept": "Provenance, ownership and access (grok)",
            "disposition": "rejected as duplicative",
            "rationale": "The base splits the same content into f-record-provenance-and-evidence and f-access-classification-and-confidentiality, both PROV-aligned, both with bundle/layer/finding/artifact access scoping and audit obligations. Software ingest agents are already reachable through the asserting-agent-and-system question."
          },
          {
            "concept": "Retention, deletion and interoperability (grok)",
            "disposition": "rejected as a finding, exchange half deferred",
            "rationale": "Roughly half the finding duplicates f-retention-archiving-and-deletion (disposition authority, legal hold, tombstones). The genuinely new part — a named interchange profile and an explicit aligned-not-conformant declaration — deserves its own evidence rather than riding into the base attached to duplicate retention structure, so it is deferred instead."
          },
          {
            "concept": "Grok bundles identity-and-classification and intent-and-authorization",
            "disposition": "rejected as reorganization",
            "rationale": "Both are alternative groupings of content the base already holds in b-mandate-and-identity and b-scope-and-structure; their child findings match base findings at 0.6 to 0.94 similarity. Accepting them would fork the model's top-level shape without adding evidence."
          },
          {
            "concept": "Base-only bundle b-time-lifecycle-and-baselines",
            "disposition": "retained",
            "rationale": "Grok scatters lifecycle, gates, dates, baselines and change across three bundles. Keeping the base grouping preserves the single place where an approved baseline, the change that altered it and the effective-versus-recorded time of the transition are reconciled, which is the property that makes performance figures reproducible."
          },
          {
            "concept": "Continuing-operations projects with unspecified end",
            "disposition": "deferred, recorded as a conflict note",
            "rationale": "Grok's NASA evidence (Phase E with unspecified end, initial capability cost instead of full life-cycle cost) sits in tension with the base purpose statement's temporary endeavour framing. It is a declared variant, not a contradiction — the base already asks the project-versus-operations criterion — so it goes to deferred research rather than blocking a draft."
          },
          {
            "concept": "schema.org Project typed as a subtype of Organization",
            "disposition": "resolved as lossy publication-only alignment",
            "rationale": "Both providers reached the same resolution independently: follow the ISO/APM temporary-endeavour reading, record the modelling conflict rather than smoothing it, and claim no conformance. Resolved, therefore not a critical conflict."
          },
          {
            "concept": "Earned value as a required field of every project",
            "disposition": "resolved as conditional with declared alternatives",
            "rationale": "ISO 21508 presumes decomposed control accounts and NASA explicitly exempts non-developmental, steady-state and basic-research work below its threshold. Both providers converge on requiring a declared measurement method with named alternatives, which the base already asks directly."
          },
          {
            "concept": "Grok functions authorize, baseline, report, control-change, decide-gate, transition, close-and-evaluate",
            "disposition": "rejected as duplicative",
            "rationale": "Each maps one-to-one onto an existing base function (fn-authorize-project, fn-establish-baseline, fn-publish-status-report with fn-record-performance-measurement, fn-decide-change-request, fn-record-gate-decision, fn-transition-lifecycle-state, fn-close-and-dispose-project). Only the three operations with no base counterpart were taken."
          }
        ],
        "publicationHolds": [
          "Source verification: none of the roughly thirty distinct URLs across the two providers has been re-resolved by this adjudication. Every accepted source must be fetched live and version-pinned before publication, with particular attention to the two NASA NPR 7120.5F entry points (directive page versus Chapter 2 deep link), GovS 002 v2.1, the PeopleCert PRINCE2 v7 page, schema.org v30.0, IATI 2.03 codelists, DataCite 4.6 and the NARA GRS page.",
          "Paywalled ISO texts: ISO 21500, 21502, 21503, 21504, 21505, 21508 and 21511 were read only as catalogue abstracts, committee pages, ISO news and one tier-4 secondary clause summary. Clause-level fidelity is asserted at abstract level only and the draft must say so; no clause number may be cited as if the purchased text had been read.",
          "Vocabulary currency: ISO/TR 21506:2018 is withdrawn and replaced by ISO 21506:2024, which neither provider retrieved; ISO 21511 is under revision as ISO/DIS 21511 and ISO 21513:2026 on post-project evaluation was not fetched. No term definition may be published as standard-derived until the current editions are checked.",
          "Multi-profile domain validation: the model has not been exercised against more than one delivery regime. Before publication it must be validated against at least a public-sector regime (NASA or GovS 002), an aid-transparency regime (IATI 2.03), a research regime (RAiD/ISO 23527) and an adaptive or agile delivery profile that maintains no control accounts.",
          "Declared gaps must ship as gaps: no data-protection instrument was retrieved live (the EUR-Lex fetch returned no body) and no information-security control standard was retrieved by either provider. Privacy and security coverage must be published as gaps with the jurisdictional instrument left to the adopting Dimension, not asserted.",
          "Accepted grok content needs first-party re-verification: grok's PMI fetch was blocked and taken via search, and the GovS 002 full PDF and Teal Book were not retrieved. Both accepted findings (f-tailoring-and-compliance, f-transition-disposal-and-residual-obligations) lean on SRC-006 and SRC-007, so their supporting text must be confirmed from the primary documents.",
          "Retention is anchored on NARA General Records Schedules as a US federal working example; the applicable disposition authority is jurisdictional and the adopting Dimension must substitute it before the retention finding is treated as operative."
        ],
        "deferredResearch": [
          "Open-ended undertakings: reconcile NASA continuing-operations projects (unspecified Phase E end, initial capability cost in place of a full life-cycle end) with the temporary-endeavour framing, and decide whether f-lifecycle-state-and-transitions or f-project-dates-and-time-semantics needs an explicit open-ended-horizon question rather than assuming a planned end.",
          "Interchange profile and conformance posture: research a dedicated interoperability finding covering the named import/export profile, which concepts are declared aligned rather than conformant, and the projection-is-not-semantics rule, with its own evidence instead of arriving attached to duplicate retention structure.",
          "Post-project evaluation: ISO 21513:2026 was not retrieved by either provider. Fetch it and decide whether formal post-project evaluation is a distinct finding or an extension of closure and lessons.",
          "Sibling risk model: the base holds risk and issue registers inline because no dedicated risk model is confirmed in the registry. Confirm the registry state; if such a model exists, move f-risk-register and f-issue-and-escalation there and replace them with typed references.",
          "Schedule and contracting interoperability: no alignment was verified to scheduling exchange formats (P6, project XML) or to a contracting data standard such as OCDS, so schedule interoperability beyond typed dates and supplier-commitment exchange both remain unproven.",
          "Exception as a first-class event: verify whether the base delegated-tolerance and escalation-threshold questions fully capture PRINCE2 manage-by-exception semantics, or whether raising, recording and closing an exception needs its own state and evidence trail."
        ]
      }
    }
  }
}

```
