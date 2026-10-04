# Proposed acceptance cases, not executed integration tests

- Same party with two buyers: preserve two scoped relationships.
- Consortium participants: retain typed references rather than invent a legal entity.
- Registered prospective supplier: never infer spend authorization.
- Category-specific qualification: never extend approval to unrelated categories.
- Expired certificate or absent evidence: explicit stale/unknown, not approved.
- Seller differs from payee: preserve both references; never redirect a payment.
- Assessment has a risk label but no method/date: retain as incomplete assertion,
  not an automatic exclusion decision.
- Missing sub-tier visibility: explicit gap, not a claim that dependencies are safe.
- Contradictory qualified source statuses: contested set until an authorized
  resolution; latest observation alone does not prove correctness.
- Relationship suspension: does not cancel contracts, accounts or outstanding debt.
- Export to a target with weaker role semantics: warning/refusal and loss report.
- Unapproved actor or wrong Dimension: no write, merge, disclosure or side effect.

Five facets: identity/class and seller/buyer scope; direct role/state/qualification
properties; recognition evidence; bounded record functions; commercial and risk
context. Physical material/geometry are not applicable to the relationship and
remain on referenced goods/site models. Nested schemas and adapter fixtures
must remain an explicit gap until implemented.
