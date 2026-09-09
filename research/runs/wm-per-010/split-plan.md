# WM-PER-010 bounded Claude research plan

The monolithic Claude pass produced substantial content but failed semantic
validation because local identifiers were duplicated across its structure.
No invalid result may be published. The model is therefore researched through
three bounded, non-overlapping passes whose identifiers use disjoint prefixes.

1. `channels` owns the contact-point root, channel-specific addresses,
   verification and reachability state.
2. `preferences` owns routing preferences, purposes, availability, locale,
   accessibility and fallback order.
3. `governance` owns authority, consent references, sensitivity, lifecycle,
   provenance, access, retention, audit and all canonical service-layer rules.

Every pass must satisfy the complete provider schema and semantic validator.
The deterministic merger stable-unions sources and assigned structure, keeps
the complete model boundary from `channels`, keeps service layers from
`governance`, rejects duplicate IDs or questions and validates the merged
result again. A separate no-tools adjudication remains mandatory.
