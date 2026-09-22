# D1 request shape and native envelope experiment

This is a **provisional research fixture**, not a model release, an executor, an authorization test or an installed Vercy Dimension. The draft status `D1` is deliberately different from a released semantic version. The `urn:vercy:research:*` type names are research identifiers; they are not registered runtime models.

Three invented profiles (startup, matrix unit and AI service) each have a closed request payload, a native object envelope and a native submission Event envelope. The object is the actual independently referenced intent; there is no artificial aggregate host or extra request-state fact. Native `state=active` means the record is active, not that the operation ran. All six envelopes pass the existing native schemas. References between each object and its submission are checked explicitly. This is six envelope validations, **zero installed Dimensions**.

The selected semantic checks also reject fourteen cases: unknown fields, boolean and float integer encodings, reordered labels or changed purpose under an old digest, wrong definition digest, invented parameters, incompatible native request ID, changed submitter, admission at the exclusive deadline, invalid calendar date, unpaired surrogate, unsupported version and missing explicit nullable field. They do not validate full event history, duplicate keys at a JSON parser boundary, real authority, archive completeness or any effect.

`request.schema.json` constrains the full provisional request shape. `definition.json` uses the exact canonical UTF-8 bytes whose SHA-256 appears in the request; this definition supports only the ordered-label example. Both native envelopes remain open in their nested data, which is why the separate request validator is necessary. A schema-valid authority reference or fixture admission record proves neither issuer identity nor permission. The matrix and AI examples intentionally do not pretend to implement current delegated scope checks; those remain a D1 implementation requirement.

`validation-results.json` records the actual checks and native schema hashes. The original 24-test transaction spike is separate and unchanged; these fourteen negative shape cases are not additional transaction acceptance tests.

To reproduce in a disposable working directory with Python 3.12 and `jsonschema` installed, use the Vercy native schemas from the official skills package:

```text
python reproduce.py --native-schema-dir <vercy-skills>/schemas --output <new-output-directory>
```

The output directory is populated with the three fixture sets, definition, request schema and validation report. The reproducer does no network requests, has no credentials and produces no business effect. The final metamodel still needs authenticated host admission, full semantic/history validators, scoped execution decisions, lifecycle operations, native installation, migration, substantive Claude research and separate frozen Claude/Grok audits.
