# WM-ECO-023 Codex fallback source note

Codex independently grounded the fallback in official UN/EDIFACT reservation and transport-booking messages, Schema.org V30.0 reservation terms, IATA ONE Order, TM Forum appointment and resource-reservation API entries, EU package-travel and consumer-rights law, RFC 5545 and RFC 3339, PROV-O, ODRL, DQV, ISO 4217 maintenance data and OpenAPI 3.1.1.

The UN/EDIFACT and TM Forum publishers blocked direct automated HEAD requests with 403 while their live official pages remained available through indexed retrieval. This transport limitation is recorded in `source-verification.csv`; it is not represented as direct-fetch success. RFC info endpoint HEAD responses were transient 500, so the official stable RFC HTML documents are cited.

No provider result was available. Claude and Grok each timed out after one bounded 120-second attempt. Confidence remains medium and external-review, relation, jurisdiction, sector and release-pinned mapping holds remain visible.
