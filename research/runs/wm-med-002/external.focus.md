# WM-MED-002 provider focus

Research the format-independent logical structure for a governed media asset
and its renditions. Prefer current primary specifications and official
maintenance pages. Keep the result compact enough for the canonical schema:
target 6 bundles, 12-16 layers, 24-30 findings, 3-5 discriminating questions
per finding, at least one concrete artifact per finding and 8-12 functions.

The central identity decision must be explicit: the media-asset record is a
management aggregate, while each actual rendition is separately addressable
and has its own identifier, digest, media type, technical metadata and
lifecycle. Do not make a mutable URL, filename or checksum the identity. Do not
absorb the abstract creative work, publication/edition, recording, image,
scene, broadcast, rights agreement, authenticity credential or storage system.

Investigate at least these official ecosystems where applicable:

- W3C Media Ontology, Web Annotation, PROV-O, Data Quality Vocabulary and ODRL;
- Dublin Core Terms and IANA media types;
- IPTC Photo Metadata, Video Metadata Hub and rights-related vocabularies;
- EBUCore and PBCore for audiovisual metadata;
- PREMIS, METS, NISO MIX and Library of Congress audio/video technical schemas;
- IIIF Image API and Presentation API for representation delivery;
- C2PA for content provenance bindings;
- RFC 3339 timestamps, RFC 8785 canonical JSON, RFC 8493 BagIt and HTTP
  representation/digest semantics;
- accessibility captions, transcripts and audio-description standards;
- persistent identifiers, fixity, preservation events and format registries.

Separate normative rules from common practice. Pin versions or access dates,
state licensing or access constraints, and expose medium-specific, legal,
accessibility, preservation and independent-review holds.
