# WM-PLC-004 Administrative Area independent pre-provider boundary

An Administrative Area is a versioned unit used by a competent authority or
official statistical system to organize territory. It owns register-qualified
identity, unit class and level, parent and containment relations, official and
historic names, authority and instrument references, boundary assertions,
effective time and successor lineage.

It does not own the government organization, legal jurisdiction, settlement,
address, postal or electoral zone, parcel, physical terrain, population,
statistics or source survey. Those are linked external records.

Required checks:

- Codes are qualified by code list, edition, issuing authority and validity and
  are never assumed globally unique or permanent.
- Administrative hierarchy, geometric containment and governmental authority
  can differ and remain separate relations.
- Official, statistical, claimed, disputed and de facto boundary assertions
  keep source, recognition scope, time, CRS and accuracy.
- Splits, mergers, transfers, annexations, renaming and abolition preserve
  predecessor-successor lineage and do not overwrite prior legal history.
- A map geometry, name, postal code or population count alone never proves the
  current legal identity or authority of an administrative unit.
