# WM-MED-002 source synthesis

The 24 admitted sources are first-party specifications or official maintenance
pages. Their current content was checked on 7 September 2026 through the live
web index and targeted opens. Direct command-line retrieval returned HTTP 200
for several sources and HTTP 403 for the four Library of Congress pages; the
official indexed pages still exposed their current titles, versions and scope.
Short concurrent command-line checks also timed out on some otherwise readable
pages, so those transport results are not treated as evidence of absence.

The W3C Media Ontology and DCMI terms provide the cross-format description
baseline, but W3C explicitly does not distinguish every abstraction level and
warns that crosswalks can lose semantics. WM-MED-002 therefore imposes a
stricter boundary between the creative work, publication, asset aggregate,
rendition, file, bitstream, fragment, service and locator. IANA media types,
HTTP representation semantics and digest fields separate format naming,
selected representations and message content from durable asset identity.

PREMIS and BagIt cover fixity, preservation objects, events, agents, rights and
portable packages. METS describes compound structure; MIX, AudioMD and VideoMD
add technical image, audio and video metadata. PBCore and EBUCore demonstrate
the asset-versus-instantiation pattern in broadcast repositories. IPTC Photo
Metadata and Video Metadata Hub cover descriptive, administrative, rights,
accessibility, technical and AI-generation context, while noting profile and
implementation boundaries.

IIIF distinguishes image services, presentation manifests, canvases, content
resources, annotations and choices. Web Annotation supplies target and selector
semantics. WebVTT and WCAG 2.2 ground timed-text and accessibility requirements.
PROV-O covers derivation, activities and agents; ODRL covers policy statements.
C2PA 2.4 supplies signed manifests, hard and soft bindings and trust signals,
but neither signature validation nor content binding proves factual truth or
legal permission. RFC 3339 supplies second-precision clocks with offsets and
RFC 8785 supplies deterministic JSON canonicalization.
