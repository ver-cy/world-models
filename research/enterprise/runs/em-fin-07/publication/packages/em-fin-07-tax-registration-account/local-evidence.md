# EM-FIN-07 local synthesis

The reconciled boundary reuses WM-POL-011 for obligations, assessments, notices, due components and balance positions; WM-ECO-032 for return revisions, filing attempts and authority responses; WM-ECO-009 for payments; and WM-ACT-052 only for case correlation. Calculations are assertions owned by exactly one ReturnRevision or Obligation.

TaxRegistrationAccount is an optional, independently identified, identifier-unassigned candidate. It can be instantiated only from an authority handle or an explicit authority-named opening/application event. Jurisdictional basis assertions have their own identity and remain resolvable when no account exists. All mutable facts use effective and knowledge time; state and lineage are append-only.

The normative 22-rule set is in `invariants.json`. The single frozen audit found 17 mechanical defects, all remediated without rerun. This is reviewable research only: no ID, runtime, installability or publication-readiness claim.
