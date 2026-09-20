# WM-ACT-052 bounded provider focus

Research the governed aggregate that connects one tax filing case and any
resulting authority assessment for a defined taxpayer, tax type, jurisdiction
and period. Cover return preparation, validation, declaration, submission,
receipt, acceptance or rejection, assessment, adjustment, liability, payment
and refund links, penalties and interest, amendment, dispute and closure while
keeping each externally mastered record distinct.

Use current official primary sources. Inspect OECD Tax Administration 2025,
Tax Administration 3.0, SAF-T 2.0 and ICAP materials; IRS Modernized e-File
schemas, business rules and Publication 4164 for Processing Year 2026; the HMRC
VAT MTD API current version; the EU VAT Directive; XBRL 2.1; OASIS UBL 2.4;
W3C PROV-O; EU GDPR and RFC 3339. Record jurisdiction, tax type, filing season,
schema and business-rule versions rather than claiming universal conformance.

Stress-test these semantics:

- taxpayer, registration, account and tax-obligation masters remain external;
  the process owns a filing-and-assessment case and typed references;
- return, schedule, attachment, declaration, submission, acknowledgement,
  assessment notice, liability, payment, refund, penalty and dispute are
  separate records with independent identities, states and times;
- structural validation, business-rule validation, transmission acceptance,
  filing acceptance, processing and legal acceptance are different outcomes;
- self-assessed values and authority-determined values remain source-qualified
  and differences retain reason, provision, calculation and appeal rights;
- payment or refund processing remains external; the case stores allocation,
  amount, currency, value date and status references without treating payment
  as satisfaction of every obligation;
- amended, corrected, superseding and replacement filings preserve the original
  return, submission receipt, effective rules and successor lineage;
- assessment, examination, audit, collection, enforcement and adjudication are
  external processes; this aggregate records notices, links and deadlines;
- submission or receipt does not prove validity, acceptance, assessment finality,
  payment, absence of penalties or dispute resolution.

No relation-ledger edges are registered. Treat the parent signal to WM-POL-011
and likely links to taxpayer, obligation, document, evidence, payment, audit,
assessment, dispute and records models as relationship-completeness holds, not
approved composition. Keep the result reviewable-draft until independent review
and jurisdiction-specific mappings clear the recorded holds.
