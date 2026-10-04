# Agent guide

1. Read README.md, model-spec.md and crosswalk.json before using this profile. Check the profile/version manifest, all required raw file hashes and the runtime binding pins. Do not infer full parent conformance from publication status.
2. Obtain the owning Dimension, declared purpose, trusted policy, source scheme definitions and source referent evidence. If any is absent, request that artifact from its semantic owner; never guess a Person from an account or an email.
3. Evaluate only the locally authorized complete-for-caller input. The policy is externally trusted and digest-pinned; this reference does not authenticate people or authorize disclosure.
4. Use validate_set for trusted snapshot inspection. For a live change use import_assertion with a trusted receipt clock, preserve the existing input and commit under a lock/expected-head check. Each new event must have that receipt time after the global input head. A plain validation pass cannot prove history preservation.
5. Resolve with explicit valid_at, known_at, evaluation_at, reader and purpose. Present the status and its supporting, opposing, candidate/disputed and excluded IDs. Do not hide contested/negative evidence or promote accepted-in-input to global identity.
6. In a Vercy Dimension, the identity.assertion.snapshot fact belongs to the assertion object. It describes a recorded snapshot. Native outer status/rank is not inner identity truth. Explicitly run the companion validator and live-import checks; native V3 alone is insufficient.
7. Do not perform endpoint merges, account ownership changes, access grants, source writes or deletion through this profile. Such actions need their actual subject/relationship model and authority.

The 18 question routes in model-spec.md map to artifact requests and bounded actions. Number them Q01-Q18 in table order when recording findings. A missing definition or source is an explicit insufficient-context result, never an invitation to infer a fact.
