# WM-ACT-045 bounded external research focus

Produce one complete schema-valid result for `WM-ACT-045 Insurance Claim Handling`.

Treat it as one governed claim-handling case and process aggregate, not the
Insurance Claim master. Cover notification and acknowledgement, claimant
guidance, policy and coverage binding, triage, assignment, evidence requests,
investigation, expert input, coverage and liability assessment, benefit and
damage quantification, fraud indicators and referral, reserves as external
financial assertions, reasoned decisions, offers and settlements, payment
handoffs, status communication, deadlines, complaints and disputes, recovery,
subrogation and salvage handoffs, closure, reopening, provenance, retention,
interoperability, quality and safe agent operations.

Keep the Insurance Claim (`WM-ECO-036`), Insurance Policy (`WM-ECO-003`), loss
event, person, organization, role, asset, damage, injury, evidence, expert,
fraud case, complaint, legal case, payment, accounting reserve, communication,
audit and record masters separate. Do not conflate notification with a valid
claim, policy existence with coverage, investigation with proof, an estimate or
reserve with an offer, an offer with acceptance, a decision with payment,
suspicion with fraud, closure with extinguished rights, complaint with claim,
or internal review with external adjudication.

The candidate relation ledger says `WM-ECO-036 COMPOSE WM-ACT-045` for
case/process separation. Treat it as candidate metadata, not an approved edge.

Target 6 bundles, 12 layers, 24 findings, 72 questions, 24 artifacts and 10
functions. Prefer IAIS Insurance Core Principles and ComFrame adopted December
2024, NAIC Models 900, 902 and 910, FCA ICOBS 8, EIOPA complaints guidance, EU
motor-insurance and distribution directives, HL7 FHIR R5 Claim, ClaimResponse
and ExplanationOfBenefit, ACORD P&C XML 2.13 public documentation, GDPR,
PROV-O and RFC 3339. Keep regional and paywalled-source limits explicit.
