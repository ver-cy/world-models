# Adoption limits

Use this as a small offline review component for category sets, profile restrictions and correspondence evidence. It does not implement the complete Classification Scheme or Classification Binding models. Read model-spec.md for exact algorithms and capacities.

Required host inputs: authenticated actor and clock; a current independently issued grant for the entire packet; verified source custody and completeness; selected source revision; competent mapping-approval evidence; access-controlled storage, retention and interpretation of the returned questions. A string or copied policy is not proof of authority. The Python caller and host are trusted; this library is not an IAM boundary.

The initial dialect supports finite required independent category sets, exact release pins, bounded profile ancestry and direct1:1 migration proposals. It preserves n:m and empty-sided correspondence evidence for review. It does not implement general SKOS entailment, SHACL, PROF, FHIR translations, value-set expansion, classification algorithms, clinical/legal decisions or live taxonomy editing. No assertion of MUC/MMAS/MUFP certification is made.

All-or-nothing packet access is restricted. No redacted or federated projection is supplied. Native outer validation does not replay the nested evaluator. Recorded approval basis allows historical consistency checking, not future authorization. A result may be internally consistent while its source assertions are wrong, incomplete or stale.

The host retains grant provenance independently; no host-grant identity or authentication evidence is embedded in the assessment. Native materialization performs no authorization, and the companion validates the nested fact rather than the separate native object record. The combined packet/result must fit1MiB canonical encoding. A packet that fits alone may be refused when its complete result would exceed that cap; no alternatives are dropped.

Only new synthetic Dimensions are tested. Production deployment inside a company, existing-Dimension migration, scale/load guarantees, multi-host custody, erasure propagation and generic upgrades/downgrades need separate implementation and review. Runtime package publication and research assurance are separate statuses.
