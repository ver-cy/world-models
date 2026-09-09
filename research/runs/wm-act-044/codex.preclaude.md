# Codex pre-Claude research: WM-ACT-044 Content Publication

## Frozen boundary

This model owns the governed publication operation from intake through release,
distribution and post-publication change. It stores versioned assertions and
events about what was approved, instructed, delivered, observed and corrected.
It references, but does not absorb, content, edition, actor, channel, rights,
rendition, communication, analytics and record masters.

## Critical distinctions

- Draft, approved revision, immutable release instruction and observed public
  availability are separate states.
- Editorial approval, rights clearance, privacy review, accessibility review and
  final publication authority are separate assertions.
- Origin publication, syndication, subscription notification, indexing and
  downstream availability are separate events.
- Resource identity, edition identity, representation, rendition, canonical URI
  and delivery URL are not interchangeable.
- Update, correction, retraction, withdrawal, takedown, unpublish, tombstone and
  deletion have different authority and preservation effects.
- Scheduled, effective, event, observation, ingestion and knowledge times remain
  distinct and use RFC 3339 timestamps with seconds and an explicit offset.

## Candidate structure

Six bundles cover: identity and authority; release definition and editorial
workflow; packaging, channels and distribution; discovery, syndication and
subscriptions; observation and governed change; lifecycle, provenance,
retention, interoperability and agents. Each bundle has two layers and each
layer two source-grounded findings.

## Evidence plan

Use official W3C, IETF/RFC Editor and DCMI specifications. Pin versions and keep
protocol semantics narrower than editorial or legal policy. No external provider
claim is admitted unless its result validates locally and survives adjudication.
