# WM-ECO-036 bounded external research focus

Produce one complete schema-valid result for `WM-ECO-036 Insurance Claim`.

Treat the root as the governed identity and substantive assertion aggregate by
which a claimant requests an insurance benefit or remedy under one or more
policy, statutory or scheme bases. Cover claim identity and version lineage;
claim class and line of business; claimant, insured, policyholder, beneficiary,
injured party, representative, insurer and third-party roles; policy, coverage,
loss occurrence and insured-interest bindings; notification and presentation;
claimed causes, perils, damage, injury, expense, service and benefit assertions;
claim lines, quantities, amounts, currencies, deductibles, limits and allocation;
supporting evidence references; competing party positions; related, duplicate,
parent, child, catastrophe and multi-policy claims; withdrawal, amendment,
correction, reopening and closure; settlement, payment, recovery, subrogation,
complaint, dispute, fraud and regulatory references; privacy, provenance,
retention, quality, interoperability and safe agent operations.

Keep Insurance Policy (`WM-ECO-003`), the loss or incident, persons,
organizations, roles, insured assets or interests, injuries, healthcare facts,
evidence, documents, the handling case (`WM-ACT-045`), assessments, coverage
decisions, reserves, offers, settlements, payments, complaints, disputes, fraud
cases, recoveries, audit and record masters separate. Do not conflate a notice
with a valid claim, policy existence with coverage, a claimant allegation with
verified fact, claimed amount with assessed or allowed amount, reserve with
liability, coverage position with legal truth, settlement with payment, closure
with extinguished rights, or fraud indicator with fraud determination.

The candidate relation ledger says `WM-ECO-003 CONTAINS WM-ECO-036` and
`WM-ECO-036 COMPOSE WM-ACT-045`. Treat both as candidate metadata, not approved
edges. Resolve claim-to-handling-case cardinality explicitly and preserve the
claim master when multiple handlers, insurers, jurisdictions or reopened cases
exist.

Target 6 bundles, 12 layers, 24 findings, 72 questions, 24 artifacts and 10
functions. Prefer IAIS ICP 19 and 21, NAIC claims models, FCA ICOBS 8, EIOPA and
EU motor-insurance sources, HL7 FHIR R5 Claim, ClaimResponse and
ExplanationOfBenefit, ACORD public claim material, ISO 4217, RFC 3339, PROV-O,
DQV, ODRL and GDPR. Keep jurisdiction, insurance-line, maturity, access,
licensing and conformance limits explicit.
