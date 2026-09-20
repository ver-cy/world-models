# WM-PLC-002 Land Parcel independent pre-provider boundary

A Land Parcel is an authoritative or proposed land-administration spatial unit
identified within a jurisdiction and registry context. It owns parcel identity,
classification, status, geometry and boundary evidence, measured or official
area, lifecycle and provenance. It references but does not own parties, title,
rights, restrictions, responsibilities, addresses, buildings, land cover,
planning rules, valuation, taxation or source surveys.

Required checks:

- A parcel identifier is qualified by jurisdiction, register and version and
  is not inferred from address, owner, geometry or map label.
- Legal boundary, surveyed boundary, mapped geometry and occupied fence line
  may disagree and remain separately attributable.
- Coordinate reference system, dimensionality, precision, accuracy, topology,
  area method and valid time are never dropped.
- Split, merge and reparcellation create successor identities and preserve
  lineage; geometry edits do not silently mutate released legal history.
- Rights and ownership are separate legal relationships and cannot be inferred
  from parcel inclusion, possession, address or tax records alone.
