# Enterprise Action Requests

Version 0.1.0 candidate. **Not released; R1 audits are complete; corrections require a new frozen R2 audit.** English semantic package with a synthetic Python/SQLite reference. Two modeled objects — ActionDefinition and ActionRequest — and seven native Event profiles. The synthetic label resource, policy snapshots and storage tables are fixture infrastructure, not additional enterprise metamodels.

Use ActionDefinition to describe a governed, versioned operation with an exact parameter contract, target, precondition, effect boundary and steward. Description never grants permission. A descriptive-only definition can represent an external company operation without giving this package an execution adapter. In the reference implementation only the explicitly named synthetic ordered-label replacement can execute. It accepts no command, script, endpoint, SQL expression or remote side effect.

An ActionRequest is a durable statement of intent, independent of an occurrence or result. The host mints its ID once, outside the client intent digest. Events distinguish a submission, a delivery, a current-policy execution try, a committed effect receipt, a terminal disposition, an observer's knowledge and retirement of a retained retry key. Proposed actions remain proposals in their originating context; there is no proposal-to-execution inference.

The minimum useful adoption is one descriptive definition, one accountable steward and its parameter-document reference. Executable adoption additionally requires a trusted host, an isolated local store, explicit identities, scopes, resource version, deadline, disclosure rules and retained evidence. No ERP, HRIS or agent platform is required.

## Reference use

Python 3.12 and jsonschema 4.26.0 were selected for the fixture. Install the declared dependency in an isolated environment. `python test_action.py` checks the source modules. `python build_bundle.py` regenerates the standalone companion. `python action_bundle.py PATH_TO_EXPORT` checks a complete export. The bundle and sibling `action.schema.json` must be pinned as a unit by the host; neither proves its own trusted origin.

`Executor.create` creates a fresh test store exclusively. Reopen with its separately retained epoch. `add_definition`, `set_policy`, `add_resource`, `retire_definition`, `retire_key` and `snapshot` are **trusted fixture administration**, never endpoints for untrusted callers. A host must verify issuer standing and the referenced basis before admitting policy, authenticate the actor and supply trustworthy monotonic time. Fixture Pins have deterministic invented preimages; they are not external credentials or verified mandates.

`dispatch(wire_json, retry_key, authenticated_actor, host_time)` admits and tries an intent. Initial admission requires submit permission; each attempt requires current execute permission. `lookup`, `cancel` and `observe` apply current disclosure/action scopes. Do not accept authenticated_actor, host_time or `_fault` directly from an untrusted request. The reference has no login, signing, identity-proof, network server or production authorization integration.

Build an example with `fixtures.fixture(path, 'startup')`, `'matrix'` or `'ai-service'`; all are invented organizations. The latter two use direct representation by a distinct actor. They do not assert AI subjecthood. The host is responsible for legitimate principal identity and authority outside this fixture.

## Limits that affect adoption

This release is a bounded reference, not an exactly-once distributed executor. Its only effect is replacing a list in the same SQLite transaction that retains the request, revision and receipt. SQLite/OS/storage guarantees, privileged file integrity and host isolation are assumptions. Process rollback and independent connections are tested; hardware power failure is not.

A coherent old database has the same epoch and valid hashes. The restore-limit test deliberately demonstrates that it can be replayed. **After recovery or uncertain continuity, stop dispatch and reconcile against a trusted external latest-history anchor; never automatically resend merely because the local database says absent.** No external continuity service ships here. Likewise, a new key is a new intent, so automatic key replacement after a lost response can duplicate a business effect.

All export contents are privileged evidence. Native records and manifests do not enforce read rights. Serve them only through host-controlled projections. `validate_snapshot` and `verify_export` establish internal consistency and file closure relative to the supplied cut, not authenticity, authority, completeness against the world, or the latest cut. Native outer schemas alone do not validate nested action meaning.

The package does not implement delegation chains, impersonation, use counters, remote effects, durable distributed sagas, receipts from third parties, arbitrary descriptive-action invocation, operational credentials, legal mandate validation, force cancellation of an already committed effect, erasure, per-field disclosure, or production history restoration. Retired keys retain the complete immutable intent and receipt in this fixture; this is not a compliant deletion mechanism.


R2 adds atomic 10,000-row capacity bounds, a reserved final global policy revocation, complete operation replay, and portable record filenames. At capacity, never replace a retry key or silently start a new store. Same-pin compensation is unavailable after definition retirement. An interrupted export with a torn file needs a fresh directory; between-files interruption can resume the exact cut. Test installations retain the mandatory snapshot and manifest inside the Dimension and label the model lock candidate/simulationOnly.

## Package and review state

See `model-spec.md`, `model-fields.md`, `whole-object-coverage.yaml`, `mastership-and-rights.yaml`, `composition.yaml`, `crosswalk.json`, `invariants.md`, `migration.md` and the executable sources. Frozen reviewer input and exact acceptance reports must accompany the eventual release. D1 and the earlier 24-test transaction / 14-negative shape experiments remain separate historical research evidence; they are not acceptance of this implementation.
