# Customer relationship acceptance design

Designed cases only, not an executed CRM adapter test suite:

- Same email, different seller scopes: return distinct candidates.
- Default allow-email, no authority evidence: do not contact.
- Contact linked to account, no mandate: do not grant purchasing power.
- Closed CRM record, outstanding agreement: preserve agreement reference.
- Account grouping: reject inferred legal control or inherited data access.
- Proposed duplicate merge: retain source IDs, scope checks and recovery plan;
  no external CRM transaction is executed.
- Date-only effective state: preserve precision, do not fabricate midnight UTC.
- Unknown nested answer: explicit unknown, not guessed required values.
- Changed preference meaning in target schema: loss warning or refusal.
- Unauthorized disclosure: no projection or transmission.

Structural validation of the research contract does not execute these cases.
