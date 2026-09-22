# Migration

Existing publication rows are observations, not authoritative ModelRelease records. Import only after reconstructing the exact package digest, immutable registry coordinate and WM-XCT-040 receipt. Never infer assurance from `published`, `installable` or `canonical_publishable`. Preserve the original row and record every unresolved field as a blocking hold.
