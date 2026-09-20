# WM-ACT-052 Codex pre-provider note

This is preparatory boundary evidence, not provider research and not a
publication artifact.

- Registry identity: `vr.wm-act-052`, model `WM-ACT-052`, name Tax Filing /
  Assessment Process.
- Registry record plane: `world-model`; catalogue entry kind:
  `standalone-mm`; candidate subject-schema kind: `aggregate`.
- Purpose: connect return, validation, assessment, settlement references and
  dispute context without flattening filing, determination and payment.
- Parent signal: `WM-POL-011`; no relation-ledger edge is registered, so it
  remains a boundary hold and grants no ownership or cascade behavior.
- Expected external masters: taxpayer and representative, registration and tax
  account, tax obligation and law, form and schema, source document and ledger,
  evidence, payment and refund, penalty and interest, audit or examination,
  dispute or appeal, collection or enforcement, provenance and records policy.
- Required direct properties: case and return identity, tax type, jurisdiction,
  period, form and rule version, declaration, submission and acknowledgement,
  validations, authority assessment, adjustments, amounts and currency,
  deadlines, amendment lineage, payment or refund links and dispute state.
- Required safety boundary: no autonomous tax advice, declaration signature,
  filing, payment, amendment, authority decision, appeal waiver, disclosure or
  disposition without explicit delegated authority.
- Required time format: RFC 3339 with seconds and explicit offset or `Z`, with
  tax period, source effective, due, signed, submitted, received, accepted,
  assessed, paid, appealed, recorded, ingested and knowledge times distinct.
