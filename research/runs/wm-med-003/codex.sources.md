# WM-MED-003 source verification

The Codex fallback uses 24 primary or official sources. Versions and current
status were checked on 7 September 2026 before synthesis. DataCite 4.7,
Crossref 5.5.0, MARC 21 Update 42, RDA Registry 5.4.13 and the January 2026
EPUB 3.3 Recommendation replace older versions that a static knowledge cutoff
could otherwise suggest.

Direct GET checks returned HTTP 200 for 19 source URLs. The official PRESSoo,
BIBFRAME, MARC, MODS and PREMIS pages are retrievable through browser search
and carry the stated current versions, but five relevant IFLA/Library of
Congress endpoints returned anti-bot HTTP 403 to the local curl client. The
status is recorded as transport restriction, not source absence. The ISBD
official bitstream and IFLA LRM repository record returned 200 directly.

Important interpretation constraints:

- IFLA LRM, RDA and BIBFRAME use different abstraction shapes; no direct class
  equality is assumed.
- ISBN, ISSN and DOI identify authority-defined targets. Equality or resolution
  cannot be promoted to universal edition identity.
- ONIX, JATS, Crossref and DataCite are community exchange profiles rather than
  one global publication ontology.
- EPUB 3.4 and EPUB Accessibility 1.2 are Candidate Recommendation Drafts as of
  the access date, so the stable publication pins remain EPUB 3.3 and EPUB
  Accessibility 1.1.
- Jurisdiction-specific legal publication, deposit, copyright, retraction and
  accessibility rules require adopting-Dimension profiles.
