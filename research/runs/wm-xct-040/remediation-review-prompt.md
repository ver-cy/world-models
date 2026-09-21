Final remediation verification only. Your earlier full-file audit blocked X1 schema closure, X2 linked nested evidence, X3 wording. Verify that these exact fixes now close those blockers. Return at most 600 words with ACCEPT WITH LIMITS or concrete remaining blocker. No tools; no claim of executing tests. Keep the already accepted bounded contract, trusted-input and cooperative-Windows scope. Do not treat missing universal features as defects.

Changes: object type lists and properties-defined objects now closed; patternProperties refused; untyped/boolean-true nodes explicitly remain companion responsibility. Actual stored positive fact is validated, a malformed copy is written to a throwaway Dimension through the native writer and passes V3 while the same stored value fails the companion. Plan-declared closure, Python 3.12+, format extras, exact publisher-asset provenance, Windows/cooperating scope, descriptor versus execution and example expiry are explicit. Nine upstream assets verified. Additional malformed input, cleanup, staged-plan integrity, package-text trust-note and bootstrap observation fixes are included. 68 unit tests and 3 native profiles plus 3 bootstrap failure checks pass in Codex execution.

Unified diffs below are against the full files you reviewed; final file SHA-256 recorded. No previously reviewed code is omitted from the base.

FILE model-spec.md final sha256:ae5ab793362b395655b5a817837c7f8c24a7b986e7bc6186d3641f696ead713b
```diff
--- reviewed/model-spec.md
+++ final/model-spec.md
@@ -1,184 +1,96 @@
 # Model Composition Resolution / Композиция моделей Измерения
-
-
 
 Catalogue identity: WM-XCT-040, registry `vr.wm-xct-040`, version 0.1.0. A reusable contract aggregate above the existing Vercy kernel. It does not own organizations, people, products or their facts. Its subject is one reviewable resolution episode: which exact model releases may be assembled for one Dimension, under which local authority, with which readiness evidence.
 
-
-
 ## Boundary decision
-
-
 
 Create one bounded contract pattern. Reuse the Dimension identity, owner, provenance, immutable record envelope and policies. A ResolutionPlan is the main document of this aggregate; release references, mandatory and optional edges, byte descriptors, compatibility decisions and binding references are owned values. RuntimeBinding retains an independent URI and version because one semantic release may have several representations. A staging receipt is an immutable execution artifact, not another authoritative model lock. KernelBoundaryDecision is a governance artifact, not an installable kernel. Existing asynchronous ResolutionRequest and its API UUID are reused; this contract starts after exact candidate selection.
 
-
-
 The first executable profile is `exact-closure-v1`. It accepts a fixed set of release references and independently supplied trusted policy plus current lock bytes. It checks them offline and stages the minimal mandatory closure. It is not a package version range solver, ELMM Minimal Version Selection, online catalogue discovery, authenticity service or business-data writer. Exact versions are intentionally a small common denominator. Same name, newer SemVer or matching bytes never establish semantic equivalence.
-
-
 
 The current Vercy 0.4 downloader/validator mismatch is preserved as evidence. This package supplies an additive route for NEW Dimensions: semantic-only packages go into `registries/semantic-models.yaml`; explicit native bindings go into `registries/meta-models.yaml` with all V1 fields. Both are pinned in `vercy.lock`, with different readiness. Existing Dimensions and published specifications are never rewritten by this adapter. The native validator is unchanged.
 
-
-
 ## Identity and cardinalities
 
-
-
 | Type | Identity | Ownership and multiplicity |
-
 |---|---|---|
-
 | CompositionResolution / ResolutionPlan | Issuer-qualified planId; revision has a different planId and explicit supersedes | One Dimension, one purpose and actor, one supplied policy, one starting lock digest; one or more roots and releases |
-
 | ModelReleaseReference | modelId + exact version, additionally pinned to specification bytes | One selected version per model ID in this profile; changing bytes at the same version is a conflict |
-
 | DependencyEdge | Ordered source release, target release and edge kind within the plan | Zero or more requires and references; required target must exist exactly; optional references do not pull packages |
-
 | ContentDescriptor | Asset path within the transport package plus SHA-256 and byte size | Exactly one agents and specification descriptor per release; paths are carriers, never model identities |
-
 | RuntimeBinding | Issuer-qualified binding URI and version, exact target specification digest | Zero or one selected binding per release; more alternatives require a new selection plan |
-
 | CompatibilityDecision | Evidence URI, reviewer and observation time scoped to a release | Exactly one accepted decision per selected release; unknown or rejected cannot be applied |
-
 | AuthoritySnapshot | Policy reference and digest, actor, owner, purpose, effective policy interval | The external trusted policy is authoritative; the plan snapshot cannot authorize itself |
-
 | InstallationReceipt | Installer-generated UUID plus exact plan digest | A committed staging artifact; repeated identical staging reuses it; runtime and nested validation results are separate |
-
 | KernelBoundaryDecision | Governance record URI and source comparisons | Records reuse/defer choices; no package installation authority |
-
-
 
 `schemaVersion=1.0.0` is the instance contract, model release `0.1.0` is the specification, `revision` is the plan revision, publication status is the release lifecycle, and research assurance describes review evidence. None substitutes for another. Model IDs are publisher-qualified registry identifiers. Object/plan/binding/policy/evidence identifiers are absolute URIs. Unknown fingerprints are null; missing authority or exact dependencies causes refusal. A digest verifies bytes and does not authenticate their publisher.
 
-
-
 ## Fields and semantics
-
-
 
 The complete field types, nullability, enum values, cardinalities and additional-property rules are in `composition-plan.schema.json` and `policy.schema.json`. `field-catalog.json` adds semantic ownership and sensitivity per field. Required null values, including an absent semantic fingerprint or binding, mean explicitly unknown/not-selected, never a default successful result. Paths use the declared portable relative-path profile, not URLs or executable commands.
 
-
-
 Roots and required references use exact `(modelId, version)`. `references` is an informational package relation; it is not an instance relationship. `namespace` is a selected export namespace, not a filesystem folder or a legal ownership claim. `semanticFingerprint` carries an algorithm identifier when supplied; this profile preserves it but does not calculate or certify semantic equivalence. Compatibility `scope` and evidence are mandatory; the verifier checks reviewer allowlisting, not the truth of the review assertion.
-
-
 
 Binding `scope` states exactly which paths are implemented. A binding's `forSpecificationDigest` prevents attaching a schema to the wrong release. A native binding contains a nonempty Vercy runtime path contract. Structured values require both a closed JSON Schema 2020-12 schema and a companion semantic validator descriptor. Arbitrary network schema references, custom vocabularies and dynamic references are outside this first profile. Downloaded validator code is never executed by the composer. Native V3 validates envelopes and top-level types/units; the selected trusted companion must check nested and graph semantics separately. A bootstrap pass with zero records is a control-package test, not evidence that company data exists.
 
-
-
 ## State machine and effects
 
-
-
 1. **Scoped**: owner or delegated curator defines purpose and roots. Missing model requests remain in the existing Vercy API workflow.
-
 2. **Resolved candidate**: exact releases and descriptors are selected; all required edges are known. No write authority is inferred.
-
 3. **Verified**: schema, graph, policy, time, lock precondition, compatibility assertions, paths and asset bytes pass. This is a computed result for one evaluation time.
-
 4. **Refused**: any guard fails. Return a stable error category, keep source and target unchanged. A false assertion is not repaired by invention.
-
 5. **Assets staged**: one new directory contains verified bytes, the frozen plan and receipt. A sibling creation lease excludes cooperating writers. An incomplete temporary directory is not a committed result. Crash leftovers require inspection; no blind lease stealing.
-
 6. **Dimension bootstrapped**: the NEW-Dimension adapter creates owner controls, separate semantic/native registries and lock; runs unchanged V1-V3 validation before activation. No facts are invented. A final directory rename is the activation point on the tested local filesystem, not a distributed transaction or power-loss durability guarantee.
-
 7. **Instance validated**: a separate evidence record names the exact data, runtime validator and companion validation scope. It does not retroactively change the staging receipt.
-
 8. **Superseded**: a new plan identifies its predecessor. Applying changed versions, downgrades, changed bytes or migration of an existing Dimension is refused by this implementation. Historical validation can use an explicit evaluation time; historical time cannot authorize staging through either the CLI or the Python library.
-
-
 
 The caller supplies owner policy from a trusted location. The adapter rechecks policy and lock bytes before activation. It does not install a trust policy from downloaded text, execute package hooks, call corporate systems, change user access controls or send instance data to the catalogue. Filename/case collisions and symbolic-link/junction traversal are rejected. Physical storage permissions and policy authentication are the adopting environment's responsibility.
 
-
-
 ## Invariants and evidence
-
-
 
 The executable rule categories are SCHEMA, POLICY, POLICY-DIGEST, TIME, STALE, OWNER, AUTHORITY, DENIED, ASSURANCE, REVISION, VERSION, NAMESPACE, ROOT, LIFECYCLE, COMPATIBILITY, KERNEL, EDGE, READINESS, ORIGIN, COLLISION, PATH, ASSET, DIGEST, AGENTS, SPEC, BINDING, FACT-PATH, NESTED, DIALECT, SCHEMA-REF, CLOSURE, CYCLE, MINIMAL, LOCK, MIGRATION, TARGET, BUSY, STAGE and NEW-ONLY. Syntax is checked by a real JSON Schema 2020-12 implementation; graph and state rules are Python checks. These categories are not claims of security certification.
 
-
-
-Key requirements: unique selected IDs and namespaces; one release version per ID; all mandatory targets present; no mandatory cycles; no extraneous packages; no domain imports from a kernel-role node; only published releases; explicit permission for research drafts; independent owner/actor/purpose checks; fresh policy and plan; unchanged starting lock; exact specification and AGENTS bytes; portable contained paths; binding-to-spec match; nonempty native paths; no duplicate path owners; mandatory nested checks for structured snapshots; no implicit upgrade/downgrade; repeat staging unchanged; failure cannot replace an existing target.
-
-
+Key requirements: unique selected IDs and namespaces; one release version per ID; all plan-declared mandatory targets present; no mandatory cycles; no packages extraneous to the plan-declared closure; no domain imports from a kernel-role node; only published releases; explicit permission for research drafts; independent owner/actor/purpose checks; fresh policy and plan; unchanged starting lock; exact specification and AGENTS bytes; portable contained paths; binding-to-spec match; nonempty native paths; no duplicate path owners; mandatory nested schema/companion descriptor presence for structured snapshots; execution remains a separate step-7 obligation recorded in composition/plan.json; no implicit upgrade/downgrade; repeat staging unchanged; failure cannot replace an existing target under cooperating writers on the tested Windows filesystem.
 
 ## Mastership, time, conflicts and projections
 
-
-
 The publisher masters specification and release metadata. The Dimension owner masters installation policy and selected pins. A domain or binding maintainer masters the meaning of runtime paths. The executing agent records observations and receipts but cannot grant itself access. `createdAt` and `provenance.recordedAt` are knowledge timestamps; plan and policy effective intervals gate execution. A historical correction uses a new plan revision, not a silent overwrite. Equal-authority conflicting proposals remain separate candidates; this profile refuses ambiguous selected versions instead of choosing the latest timestamp.
-
-
 
 Public specifications and fictional acceptance fixtures may be disclosed. Real model selections can reveal technology or organizational structure and are private by default. A projection of a plan describes that one plan; a dashboard spanning installations is a context pack of separately permitted projections. The portable implementation records classifications and checks installation policy; it is not an IAM/read-side enforcement engine. A successful install grants no new right to read personnel or contract facts. Retention of receipts and invalidation history follows local policy; automated deletion and retrospective erasure are outside this package.
 
-
-
 ## Whole-object coverage
-
-
 
 `whole-object-coverage.json` supplies a distinct row for every exported type. Identity, direct properties, observation, possible actions and provenance are assessed per type. No abstract plan, release or receipt acquires mass, geometry or legal personality. The runtime code is an implementation artifact of a contract, not evidence that the contract has acted. A receipt states observed outcome, while a plan describes a proposed operation.
 
-
-
 ## Three adoption profiles
-
-
 
 **Startup**: use this contract with one Organization semantic specification. A minimal optional Organization identity binding contains the reviewed name fact only. No Employee, Employment, HRIS, ERP or legal-registration record is required merely to collaborate. Unknown legal form remains unknown.
 
-
-
 **Group**: select Organization and Organizational Unit packages in separate export namespaces, using this contract. Package selection does not create a subsidiary, employment relationship or reporting line. Those remain explicitly authored instance records in their subject models. Test a valid multi-root closure and reject namespace and version collisions.
-
-
 
 **AI organization**: select the published Performance Objective / Review model with its explicit reference binding and companion validator as a representative structured snapshot. The use case tests data structure and composition, not real employment decisions or productivity evaluation. Malformed nested context must fail its companion even when the outer native record passes V3.
 
-
-
 ## ELMM and neighbouring models
-
-
 
 ELMM's repository proposal composes contexts using an MMDG profile, minimum-version selection and semantic fingerprints. Its kernel has no outgoing domain composition edges. Vercy's public installation index uses exact byte digests and presently does not offer ELMM as an installable model. Adopt the separation of domain ownership and composition; do not label this exact-closure profile as an implementation of ELMM, MVS, context budgeting or all ARCH/FED gates. Enterprise Landscape remains a separate domain-level composition. PLMM's legacy runtime status and AISMM's release/version differences require explicit future migration; the three acronyms are not interchangeable.
 
-
-
 WM-XCT-037 Dependency / Impact overlaps typed edge description, but its public package carries unresolved boundary, identity and composition holds. It is not a dependency of this contract, and no claim of exact equivalence is made. WM-XCT-011 Identifier Scheme describes schemes; this contract uses existing qualified registry IDs rather than importing the scheme catalogue into the kernel. Crosswalk entries record pins, overlap, loss and chosen action.
-
-
 
 ## Migration, recovery and limits
 
-
-
 New Dimensions can use the supplied bootstrap adapter. Existing installations must first retain a recoverable copy, inspect current pins and runtime bindings, and prepare a separate migration; the adapter intentionally refuses to update them. Semantic-only to native-bound is not a status toggle: bind the exact specification, provide runtime paths and additional validators, validate representative facts, then record a new receipt. Downgrades require a loss analysis and explicit data conversion; unsupported cases are refused.
-
-
 
 A failed staging/bootstrap attempt removes only its task-created temporary directory and lease during normal exception handling. A process crash may leave a staging directory or lease: inspect recorded ownership and committed receipt before recovery. The implementation does not claim power-loss durability, adversarial multi-user filesystem isolation or distributed locking. No model is certified universally compatible, and source provenance alone never proves a factual assertion true.
 
-
-
 Published artifacts include independent provider memos, the reconciliation and frozen review, full schemas, source comparisons, whole-object and field coverage, code, fixtures and actual results. Research assurance and publication lifecycle remain separate. Numeric test counts are taken from reports, not this document.
-
-
 
 ## Bounded file and schema profile
 
-
-
 Specification bytes must be JSON or JSON with one leading `#` header line (the current Vercy JSON-compatible YAML projection). General YAML is refused. The three published package specifications used in acceptance were fetched from ver.cy and matched byte-for-byte. Only the commercial-company preset is supported by the new-Dimension adapter. JSON Schema closure checks require a closed root object and closed explicitly typed nested object nodes; this static gate is not a proof that every possible composed schema is semantically complete. Publication status and compatibility remain supplied assertions checked against owner policy, not digitally authenticated publisher/reviewer statements.
-
-
 
 A release must have publicationStatus=published. allowReviewableDrafts only admits the separate researchAssurance=reviewable-draft state of an already published release; it never permits an unpublished draft. Runtime bindings and semantic fingerprints are preserved with explicit scopes. No automatic execution of a companion follows from including its descriptor.
 
+Closure and minimality are computed only over dependencies declared in the plan. Dependencies are plan assertions and are not extracted from specification bytes. Untyped nodes and boolean-true subschemas can remain open; the companion validator must enforce their domain semantics. The bounded static walk may conservatively reject valid schemas when annotation values resemble schema keywords. Python 3.12+ is required for the documented junction checks. Atomic activation claims apply to the tested Windows filesystem and cooperating writers; non-cooperating POSIX writers can race a directory rename. The examples are directly reproducible only until 2026-12-31; regenerate policy and plan afterwards.
+
+Provenance of example artifacts: Organization, Organizational Unit and Performance semantic specs and agent guides are copies of published releases. The one-name Organization runtime binding is authored for this contract and published with it. The Performance runtime/schema/companion is copied from the already published reference binding, with its original limitations. Upstream verification names every fetched asset. Native bootstrap observations are stored in composition/bootstrap-observation.json, not presented as native event instances.

```

FILE implementation/composition.py final sha256:78aa1c6c29f14c7adedefd7dd8b3683c845118c49bb48d04c5e92ae4989ce06e
```diff
--- reviewed/implementation/composition.py
+++ final/implementation/composition.py
@@ -11,17 +11,22 @@
 from jsonschema import Draft202012Validator, FormatChecker
 
 ROOT=Path(__file__).resolve().parent
 DIALECT='https://json-schema.org/draft/2020-12/schema'
 EMPTY_LOCK={'format':'vercy-composition-lock','version':1,'models':[]}
 def encode(value):return (json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode('utf-8')
 def digest(raw):return 'sha256:'+hashlib.sha256(raw).hexdigest()
 def load(path):return json.loads(Path(path).read_text(encoding='utf-8'))
-def stamp(value):return dt.datetime.fromisoformat(value.replace('Z','+00:00'))
+def stamp(value):
+    try:
+        parsed=dt.datetime.fromisoformat(value.replace('Z','+00:00'))
+        require(parsed.tzinfo is not None,'TIME','timezone required')
+        return parsed
+    except (ValueError,AttributeError,TypeError):raise Invalid('TIME: invalid timestamp')
 def now():return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
 def key(ref):return (ref['modelId'],ref['version'])
 class Invalid(ValueError):pass
 def require(condition,code,message):
     if not condition:raise Invalid(code+': '+message)
 def safe_path(root,raw,exists=True):
     p=PurePosixPath(raw)
     require(not p.is_absolute() and len(p.parts)>0 and '\\' not in raw and ':' not in raw and all(x not in {'.','..',''} for x in raw.split('/')),'PATH','unsafe relative path')
@@ -42,23 +47,26 @@
     return json.loads(text)
 def descriptors(release):
     yield 'agents',release['agents']
     yield 'specification',release['specification']
     if release['binding']:
         for name in ('runtime','instanceSchema','companionValidator'):
             if release['binding'][name] is not None:yield name,release['binding'][name]
 def check_schema_closed(schema):
+    require(isinstance(schema,dict),'NESTED','instance schema must be an object')
     require(schema.get('$schema')==DIALECT,'DIALECT','instance schema must explicitly declare JSON Schema 2020-12')
     require(schema.get('type')=='object' and schema.get('additionalProperties') is False and bool(schema.get('required')),'NESTED','structured snapshot must have a closed nonempty object schema')
     def walk(x,root=False):
         if isinstance(x,dict):
             require(not any(k in x for k in ('$dynamicRef','$recursiveRef','$vocabulary')),'DIALECT','dynamic/custom vocabularies are outside this bounded binding profile')
             require(root or ('$id' not in x and '$schema' not in x),'DIALECT','nested schema resources are outside this single-resource profile')
-            if x.get('type')=='object':require(x.get('additionalProperties') is False,'NESTED','every explicitly typed object must be closed')
+            require('patternProperties' not in x,'NESTED','patternProperties is outside this closed-object profile')
+            types=x.get('type',[]);types=types if isinstance(types,list) else [types]
+            if 'object' in types or ('properties' in x and not types):require(x.get('additionalProperties') is False,'NESTED','every explicitly typed or properties-defined object must be closed')
             if '$ref' in x:require(isinstance(x['$ref'],str) and x['$ref'].startswith('#/$defs/'),'SCHEMA-REF','only internal $defs references are admitted')
             for y in x.values():walk(y)
         elif isinstance(x,list):
             for y in x:walk(y)
     walk(schema,True);Draft202012Validator.check_schema(schema)
     def pointers(x):
         if isinstance(x,dict):
             if '$ref' in x:
@@ -115,21 +123,22 @@
             require(u.scheme=='https' and not u.username and not u.password and origin in policy['allowedOrigins'],'ORIGIN','source outside trusted origins')
             pathkey=d['path'].casefold();require(pathkey not in paths,'COLLISION','two assets share a case-insensitive path')
             paths[pathkey]=r['modelId'];path=safe_path(assets,d['path']);raw=path.read_bytes()
             require(len(raw)==d['size'] and digest(raw)==d['digest'],'DIGEST','asset size/digest mismatch')
             content[kind]=raw;verified.append(d)
         require(content['agents'].strip(),'AGENTS','empty agent guide')
         try:spec=spec_json(content['specification'])
         except (ValueError,UnicodeError,IndexError):raise Invalid('SPEC: specification must use the declared JSON-compatible Vercy profile')
-        require(spec.get('metaModel',{}).get('registryId')==r['modelId'] and spec.get('metaModel',{}).get('version')==r['version'],'SPEC','specification identity/version mismatch')
+        require(isinstance(spec,dict) and isinstance(spec.get('metaModel'),dict),'SPEC','specification and metaModel must be objects')
+        require(spec['metaModel'].get('registryId')==r['modelId'] and spec['metaModel'].get('version')==r['version'],'SPEC','specification identity/version mismatch')
         if native:
             b=r['binding'];require(b['forSpecificationDigest']==r['specification']['digest'],'BINDING','binding targets different semantic bytes')
             runtime=json.loads(content['runtime'])
-            require(set(runtime)=={'format','schemaVersion','modelId','paths'} and runtime['format']=='vercy-runtime-model-schema' and runtime['schemaVersion']=='1.0.0' and runtime['modelId']==r['modelId'] and isinstance(runtime['paths'],dict) and bool(runtime['paths']),'BINDING','invalid or empty runtime path contract')
+            require(isinstance(runtime,dict) and set(runtime)=={'format','schemaVersion','modelId','paths'} and runtime['format']=='vercy-runtime-model-schema' and runtime['schemaVersion']=='1.0.0' and runtime['modelId']==r['modelId'] and isinstance(runtime['paths'],dict) and bool(runtime['paths']),'BINDING','invalid or empty runtime path contract')
             nested=False
             for path,contract in runtime['paths'].items():
                 require(isinstance(path,str) and len(path)>2 and path not in runtime_paths,'FACT-PATH','empty or multiply-owned native fact path')
                 runtime_paths[path]=r['modelId']
                 require(isinstance(contract,dict) and set(contract)=={'valueTypes','units'} and isinstance(contract['valueTypes'],list) and bool(contract['valueTypes']) and all(t in ['string','integer','number','boolean','array','object','null'] for t in contract['valueTypes']) and len(set(contract['valueTypes']))==len(contract['valueTypes']) and isinstance(contract['units'],list) and bool(contract['units']) and all(x is None or isinstance(x,str) for x in contract['units']),'BINDING','invalid native path definition')
                 nested|=bool(set(contract['valueTypes'])&{'object','array'})
             require(not nested or (b['instanceSchema'] is not None and b['companionValidator'] is not None),'NESTED','structured values need both nested schema and companion semantic validator')
             if b['instanceSchema'] is not None:check_schema_closed(json.loads(content['instanceSchema']))
@@ -140,16 +149,17 @@
         if k in reached:return
         visiting.add(k)
         for edge in by[k]['requires']:visit(key(edge))
         visiting.remove(k);reached.add(k)
     for r in plan['roots']:visit(key(r))
     require(reached==set(by),'MINIMAL','extraneous package outside requested closure')
     previous=json.loads(current_lock_raw)
     require(isinstance(previous,dict) and isinstance(previous.get('models'),list),'LOCK','current lock has no model array')
+    require(all(isinstance(x,dict) and isinstance(x.get('id'),str) and isinstance(x.get('version'),str) and isinstance(x.get('digest'),str) for x in previous['models']),'LOCK','malformed current lock entry')
     old={x['id']:x for x in previous['models']}
     require(len(old)==len(previous['models']),'LOCK','duplicate current lock IDs')
     for r in releases:
         if r['modelId'] in old:
             item=old[r['modelId']]
             require(item.get('version')==r['version'] and item.get('digest')==r['specification']['digest'],'MIGRATION','upgrade/downgrade/replaced bytes require separate migration')
     return {'valid':True,'planId':plan['planId'],'modelCount':len(releases),'verifiedAssets':len(verified),'modes':modes,'readiness':'verified-assets-and-binding-contracts; instance/runtime evaluation is separate','evaluatedAt':clock.isoformat().replace('+00:00','Z')}
 
@@ -165,17 +175,18 @@
     try:lockdir.mkdir()
     except FileExistsError:raise Invalid('BUSY: competing composer')
     temporary=None
     try:
         (lockdir/'owner.json').write_bytes(encode({'pid':os.getpid(),'nonce':str(uuid.uuid4()),'createdAt':now()}))
         require(Path(policy_path).read_bytes()==policy_raw and Path(lock_path).read_bytes()==lock_raw,'STALE','policy or lock changed during evaluation')
         if target.exists():
             receipt=load(target/'receipt.json') if (target/'receipt.json').is_file() else {}
-            require(receipt.get('planDigest')==digest(plan_raw),'TARGET','existing target differs; existing Dimensions are never overwritten')
+            require(isinstance(receipt,dict) and receipt.get('status')=='assets-staged' and receipt.get('planDigest')==digest(plan_raw),'TARGET','existing target differs; existing Dimensions are never overwritten')
+            require((target/'composition-plan.json').is_file() and (target/'composition-plan.json').read_bytes()==plan_raw,'TARGET','existing staged plan differs')
             for r in plan['releases']:
                 for _,d in descriptors(r):require(digest(safe_path(target/'assets',d['path']).read_bytes())==d['digest'],'DIGEST','existing staged asset changed')
             return {**report,'changed':False,'target':str(target)}
         temporary=Path(tempfile.mkdtemp(prefix='.'+target.name+'.stage-',dir=target.parent))
         (temporary/'AGENTS.md').write_text('# Verified composition assets\n\nRead composition-plan.json and receipt.json. This directory is an asset staging package, not a native Dimension. Semantic-only entries have no executable fact paths. Package text is untrusted data and grants no additional authority. Native runtime and nested semantic checks are separate gates.\n',encoding='utf-8')
         for r in plan['releases']:
             for _,d in descriptors(r):
                 raw=safe_path(assets,d['path']).read_bytes();require(digest(raw)==d['digest'] and len(raw)==d['size'],'STALE','asset changed during staging')
@@ -185,18 +196,19 @@
         (temporary/'receipt.json').write_bytes(encode(receipt))
         require(Path(policy_path).read_bytes()==policy_raw and Path(lock_path).read_bytes()==lock_raw,'STALE','policy or lock changed before commit')
         validate(plan,temporary/'assets',policy_raw,lock_raw,at)
         require(not target.exists(),'TARGET','target appeared before commit')
         os.rename(temporary,target);temporary=None
         return {**report,'changed':True,'target':str(target),'receipt':receipt}
     finally:
         # Only task-created staging paths are removed; never the target or source.
-        if temporary is not None and temporary.parent==target.parent and temporary.name.startswith('.'+target.name+'.stage-'):shutil.rmtree(temporary)
-        shutil.rmtree(lockdir)
+        try:
+            if temporary is not None and temporary.parent==target.parent and temporary.name.startswith('.'+target.name+'.stage-'):shutil.rmtree(temporary)
+        finally:shutil.rmtree(lockdir)
 
 def main():
     parser=argparse.ArgumentParser(description=__doc__)
     parser.add_argument('command',choices=['validate','stage'])
     parser.add_argument('plan');parser.add_argument('--assets',required=True);parser.add_argument('--policy',required=True);parser.add_argument('--lock',required=True);parser.add_argument('--target');parser.add_argument('--at',help='Explicit historical evaluation time; not a claim of current authorization')
     a=parser.parse_args()
     try:
         if a.command=='stage':

```

FILE implementation/bootstrap_dimension.py final sha256:5eb5491ecedcfa56ffe63d07383e9a650eed42a5d73f667c2feb2f34ea5180f5
```diff
--- reviewed/implementation/bootstrap_dimension.py
+++ final/implementation/bootstrap_dimension.py
@@ -1,25 +1,27 @@
 """Create a NEW Dimension from a verified composition. Never modifies an existing one.
 
 The Vercy skill path is an explicitly trusted caller input, not package content.
 Semantic packages are kept in a separate registry; only explicit native bindings
-enter the current V1-V3 registry. Nested semantic validation remains mandatory.
+enter the current V1-V3 registry. Nested-validator descriptors are required;
+execution is a separate caller obligation recorded in composition/plan.json.
 """
 from pathlib import Path
 import argparse, json, os, shutil, subprocess, sys, tempfile, uuid
 import composition as c
 
 def bootstrap(stage,policy,lock,skill,target,name,namespace):
     stage=Path(stage).resolve();skill=Path(skill).resolve();target=Path(target).absolute()
     plan_raw=(stage/'composition-plan.json').read_bytes();plan=json.loads(plan_raw)
     receipt=c.load(stage/'receipt.json')
-    c.require(receipt.get('status')=='assets-staged' and receipt.get('planDigest')==c.digest(plan_raw),'STAGE','unrecognized or changed staged plan')
+    c.require(isinstance(receipt,dict) and receipt.get('status')=='assets-staged' and receipt.get('planDigest')==c.digest(plan_raw),'STAGE','unrecognized or changed staged plan')
     policy_raw=Path(policy).read_bytes();lock_raw=Path(lock).read_bytes()
-    c.require(c.load(lock).get('models')==[],'NEW-ONLY','new Dimension requires empty starting lock; existing data needs a separate migration')
+    starting_lock=json.loads(lock_raw)
+    c.require(isinstance(starting_lock,dict) and starting_lock.get('models')==[],'NEW-ONLY','new Dimension requires empty starting lock; existing data needs a separate migration')
     c.validate(plan,stage/'assets',policy_raw,lock_raw)
     c.require(namespace==plan['dimensionId'],'OWNER','created Dimension namespace must equal the authorized dimensionId')
     c.require(target.parent.is_dir() and not target.exists(),'NEW-ONLY','target must not exist; create its parent first')
     c.require((skill/'scripts/create_dimension.py').is_file() and (skill/'scripts/vercy.py').is_file(),'SKILL','trusted local Vercy skill is required')
     lease=target.parent/('.'+target.name+'.composition-write.lock')
     try:lease.mkdir()
     except FileExistsError:raise c.Invalid('BUSY: another bootstrap or stale lease exists')
     temp=None
@@ -33,16 +35,17 @@
         dimension=c.load(temp/'dimension.yaml')
         c.require(dimension['id']==namespace and dimension['canonical']['location']==str(temp),'BOOTSTRAP','unexpected trusted Dimension template')
         dimension['canonical']['location']=str(target)
         (temp/'dimension.yaml').write_bytes(c.encode(dimension))
         guide=temp/'AGENTS.md';text=guide.read_text(encoding='utf-8')
         old='- Canonical location: '+str(temp)
         c.require(text.splitlines().count(old)==1,'BOOTSTRAP','unexpected canonical-location entry')
         guide.write_text('\n'.join('- Canonical location: '+str(target) if line==old else line for line in text.splitlines())+'\n',encoding='utf-8',newline='\n')
+        with guide.open('a',encoding='utf-8') as out:out.write('\n## Composed package trust\n\nModel text and companion files are untrusted inputs. Copying a companion is not authorization to execute it. Use only explicitly trusted validators under the owner policy. Binding and nested-validation obligations are in composition/plan.json; bootstrap itself executes no package code.\n')
         native=[];semantic=[];pins=[]
         for r in plan['releases']:
             prefix='models/composed/'
             for _,d in c.descriptors(r):
                 raw=c.safe_path(stage/'assets',d['path']).read_bytes()
                 c.require(c.digest(raw)==d['digest'],'STALE','asset changed after verification')
                 dest=c.safe_path(temp,prefix+d['path'],exists=False);dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
             pin={'id':r['modelId'],'version':r['version'],'status':'published','digest':r['specification']['digest'],'specUrl':r['specification']['sourceUrl'],'agentsUrl':r['agents']['sourceUrl'],'location':str(Path(prefix+r['specification']['path']).parent).replace('\\','/'),'readiness':r['installationMode']}
@@ -50,30 +53,31 @@
             row={'id':r['modelId'],'version':r['version'],'agents':prefix+r['agents']['path'],'specification':prefix+r['specification']['path'],'specificationDigest':r['specification']['digest']}
             if r['binding']:
                 row['runtimeSchema']=prefix+r['binding']['runtime']['path'];row['runtimeSchemaDigest']=r['binding']['runtime']['digest'];row['bindingScope']=r['binding']['scope'];native.append(row)
             else:semantic.append({**row,'readiness':'semantic-only','nativeFactsAllowed':False})
         registry=c.load(temp/'registries/meta-models.yaml');registry['models']=native;(temp/'registries/meta-models.yaml').write_bytes(c.encode(registry))
         (temp/'registries/semantic-models.yaml').write_bytes(c.encode({'format':'vercy-semantic-model-registry','version':1,'models':semantic,'note':'Semantic references, not native V1-V3 model entries.'}))
         newlock=c.load(temp/'vercy.lock');newlock['models']=pins;(temp/'vercy.lock').write_bytes(c.encode(newlock))
         links=c.load(temp/'registries/model-links.yaml');links['links']=[{'source':r['modelId'],'type':'requires','target':t['modelId'],'version':t['version']} for r in plan['releases'] for t in r['requires']];(temp/'registries/model-links.yaml').write_bytes(c.encode(links))
-        events=c.load(temp/'registries/events.yaml');events.setdefault('events',[]).append({'id':plan['planId']+':bootstrap','type':'composition-bootstrapped','occurredAt':c.now(),'actor':plan['authority']['actor'],'subject':plan['dimensionId'],'planDigest':c.digest(plan_raw),'nativeBoundModels':len(native),'semanticOnlyModels':len(semantic)});(temp/'registries/events.yaml').write_bytes(c.encode(events))
         proof=temp/'composition';proof.mkdir();(proof/'plan.json').write_bytes(plan_raw);(proof/'staging-receipt.json').write_bytes(c.encode(receipt))
+        (proof/'bootstrap-observation.json').write_bytes(c.encode({'format':'vercy-bootstrap-observation','occurredAt':c.now(),'actor':plan['authority']['actor'],'subject':plan['dimensionId'],'planDigest':c.digest(plan_raw),'nativeBoundModels':len(native),'semanticOnlyModels':len(semantic),'scope':'Adapter observation; not a native event instance.'}))
         proc=subprocess.run([sys.executable,str(skill/'scripts/vercy.py'),'validate',str(temp)],capture_output=True,text=True,encoding='utf-8')
         report=json.loads(proc.stdout);c.require(proc.returncode==0 and report.get('valid'),'NATIVE','staged Dimension failed V1-V3 validation: '+proc.stdout)
         report.pop('dimension',None)
         (proof/'bootstrap-validation.json').write_bytes(c.encode(report))
         c.require(Path(policy).read_bytes()==policy_raw and Path(lock).read_bytes()==lock_raw,'STALE','policy or starting lock changed')
         c.validate(plan,stage/'assets',policy_raw,lock_raw)
         c.require(not target.exists(),'NEW-ONLY','target appeared before activation')
         os.rename(temp,target);temp=None
         return {'created':True,'target':str(target),'nativeBoundModels':len(native),'semanticOnlyModels':len(semantic),'nativeControlValidation':report,'limits':'No instance facts created. Native binding checks do not execute companion validators or certify nested semantics. Existing Dimensions are not changed.'}
     finally:
-        if temp is not None and temp.parent==target.parent and temp.name.startswith('.'+target.name+'.bootstrap-'):shutil.rmtree(temp)
-        shutil.rmtree(lease)
+        try:
+            if temp is not None and temp.parent==target.parent and temp.name.startswith('.'+target.name+'.bootstrap-'):shutil.rmtree(temp)
+        finally:shutil.rmtree(lease)
 
 def main():
     p=argparse.ArgumentParser(description=__doc__)
     for name in ['stage','policy','lock','skill','target','name','namespace']:p.add_argument('--'+name,required=True)
     a=p.parse_args()
     try:print(json.dumps(bootstrap(a.stage,a.policy,a.lock,a.skill,a.target,a.name,a.namespace),ensure_ascii=False,indent=2));return 0
     except (c.Invalid,ValueError,OSError,KeyError,TypeError) as e:print(json.dumps({'created':False,'error':str(e)},indent=2));return 1
 if __name__=='__main__':sys.exit(main())

```

FILE implementation/composition-plan.schema.json final sha256:cc33e9ee4522cd586a2e1fb07307e6aa5361bf7cf3ca99a419c0f434d0e8a079
```diff
--- reviewed/implementation/composition-plan.schema.json
+++ final/implementation/composition-plan.schema.json
@@ -1,950 +1,475 @@
 {
-
   "$schema": "https://json-schema.org/draft/2020-12/schema",
-
   "$id": "https://ver.cy/models/wm-xct-040-model-composition-resolution/versions/0.1.0/composition-plan.schema.json",
-
   "title": "Bounded exact model composition plan",
-
   "type": "object",
-
   "additionalProperties": false,
-
   "required": [
-
     "format",
-
     "schemaVersion",
-
     "planId",
-
     "revision",
-
     "supersedes",
-
     "dimensionId",
-
     "createdAt",
-
     "validUntil",
-
     "baseLockDigest",
-
     "algorithm",
-
     "authority",
-
     "roots",
-
     "releases",
-
     "provenance"
-
   ],
-
   "properties": {
-
     "format": {
-
       "const": "vercy-composition-plan"
-
-    },
-
+    },
     "schemaVersion": {
-
       "const": "1.0.0"
-
-    },
-
+    },
     "planId": {
-
       "type": "string",
-
       "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
-
       "maxLength": 256
-
-    },
-
+    },
     "revision": {
-
       "type": "integer",
-
       "minimum": 1
-
-    },
-
+    },
     "supersedes": {
-
       "anyOf": [
-
         {
-
-          "type": "string",
-
-          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
-
-          "maxLength": 256
-
-        },
-
+          "type": "string",
+          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
+          "maxLength": 256
+        },
         {
-
           "type": "null"
-
-        }
-
+        }
       ]
-
-    },
-
+    },
     "dimensionId": {
-
       "type": "string",
-
       "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
-
       "maxLength": 256
-
-    },
-
+    },
     "createdAt": {
-
       "type": "string",
-
       "format": "date-time",
-
       "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(?:\\.\\d+)?(?:Z|[+-]\\d{2}:\\d{2})$"
-
-    },
-
+    },
     "validUntil": {
-
       "type": "string",
-
       "format": "date-time",
-
       "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(?:\\.\\d+)?(?:Z|[+-]\\d{2}:\\d{2})$"
-
-    },
-
+    },
     "baseLockDigest": {
-
       "type": "string",
-
       "pattern": "^sha256:[a-f0-9]{64}$"
-
-    },
-
+    },
     "algorithm": {
-
       "const": "exact-closure-v1"
-
-    },
-
+    },
     "authority": {
-
       "$ref": "#/$defs/authority"
-
-    },
-
+    },
     "roots": {
-
       "type": "array",
-
       "minItems": 1,
-
       "items": {
-
         "$ref": "#/$defs/releaseRef"
-
-      }
-
-    },
-
+      }
+    },
     "releases": {
-
       "type": "array",
-
       "minItems": 1,
-
       "items": {
-
         "$ref": "#/$defs/release"
-
-      }
-
-    },
-
+      }
+    },
     "provenance": {
-
       "$ref": "#/$defs/provenance"
-
     }
-
   },
-
   "$defs": {
-
     "releaseRef": {
-
-      "type": "object",
-
-      "additionalProperties": false,
-
-      "required": [
-
+      "type": "object",
+      "additionalProperties": false,
+      "required": [
         "modelId",
-
         "version"
-
-      ],
-
-      "properties": {
-
+      ],
+      "properties": {
         "modelId": {
-
-          "type": "string",
-
+          "type": "string",
           "pattern": "^[a-z][a-z0-9.-]{2,127}$"
-
-        },
-
+        },
         "version": {
-
-          "type": "string",
-
+          "type": "string",
           "pattern": "^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)(-[0-9A-Za-z.-]+)?(\\+[0-9A-Za-z.-]+)?$",
-
           "maxLength": 128
-
-        }
-
-      }
-
-    },
-
+        }
+      }
+    },
     "descriptor": {
-
-      "type": "object",
-
-      "additionalProperties": false,
-
-      "required": [
-
+      "type": "object",
+      "additionalProperties": false,
+      "required": [
         "path",
-
         "digest",
-
         "size",
-
         "mediaType",
-
         "sourceUrl"
-
-      ],
-
-      "properties": {
-
+      ],
+      "properties": {
         "path": {
-
-          "type": "string",
-
+          "type": "string",
           "pattern": "^[A-Za-z0-9][A-Za-z0-9._/-]{0,300}$"
-
-        },
-
+        },
         "digest": {
-
-          "type": "string",
-
+          "type": "string",
           "pattern": "^sha256:[a-f0-9]{64}$"
-
-        },
-
+        },
         "size": {
-
           "type": "integer",
-
           "minimum": 1,
-
           "maximum": 20000000
-
-        },
-
+        },
         "mediaType": {
-
-          "enum": [
-
+          "enum": [
             "text/markdown",
-
             "application/json",
-
             "application/yaml",
-
             "text/x-python"
-
-          ]
-
-        },
-
+          ]
+        },
         "sourceUrl": {
-
-          "type": "string",
-
+          "type": "string",
           "format": "uri",
-
           "pattern": "^https://"
-
-        }
-
-      }
-
-    },
-
+        }
+      }
+    },
     "fingerprint": {
-
-      "type": "object",
-
-      "additionalProperties": false,
-
-      "required": [
-
+      "type": "object",
+      "additionalProperties": false,
+      "required": [
         "algorithm",
-
         "value"
-
-      ],
-
-      "properties": {
-
+      ],
+      "properties": {
         "algorithm": {
-
-          "type": "string",
-
+          "type": "string",
           "minLength": 1,
-
           "maxLength": 2048
-
-        },
-
+        },
         "value": {
-
-          "type": "string",
-
+          "type": "string",
           "minLength": 1,
-
           "maxLength": 2048
-
-        }
-
-      }
-
-    },
-
+        }
+      }
+    },
     "binding": {
-
-      "type": "object",
-
-      "additionalProperties": false,
-
-      "required": [
-
+      "type": "object",
+      "additionalProperties": false,
+      "required": [
         "id",
-
         "version",
-
         "forSpecificationDigest",
-
         "runtime",
-
         "instanceSchema",
-
         "companionValidator",
-
         "scope"
-
-      ],
-
-      "properties": {
-
+      ],
+      "properties": {
         "id": {
-
-          "type": "string",
-
-          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
-
-          "maxLength": 256
-
-        },
-
+          "type": "string",
+          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
+          "maxLength": 256
+        },
         "version": {
-
-          "type": "string",
-
+          "type": "string",
           "pattern": "^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)(-[0-9A-Za-z.-]+)?(\\+[0-9A-Za-z.-]+)?$",
-
           "maxLength": 128
-
-        },
-
+        },
         "forSpecificationDigest": {
-
-          "type": "string",
-
+          "type": "string",
           "pattern": "^sha256:[a-f0-9]{64}$"
-
-        },
-
+        },
         "runtime": {
-
           "$ref": "#/$defs/descriptor"
-
-        },
-
+        },
         "instanceSchema": {
-
           "anyOf": [
-
-            {
-
+            {
               "$ref": "#/$defs/descriptor"
-
             },
-
-            {
-
+            {
               "type": "null"
-
             }
-
-          ]
-
-        },
-
+          ]
+        },
         "companionValidator": {
-
           "anyOf": [
-
-            {
-
+            {
               "$ref": "#/$defs/descriptor"
-
             },
-
-            {
-
+            {
               "type": "null"
-
             }
-
-          ]
-
-        },
-
+          ]
+        },
         "scope": {
-
-          "type": "string",
-
+          "type": "string",
           "minLength": 1,
-
           "maxLength": 2048
-
-        }
-
-      }
-
-    },
-
+        }
+      }
+    },
     "compatibility": {
-
-      "type": "object",
-
-      "additionalProperties": false,
-
-      "required": [
-
+      "type": "object",
+      "additionalProperties": false,
+      "required": [
         "decision",
-
         "evidence",
-
         "reviewer",
-
         "observedAt",
-
         "scope"
-
-      ],
-
-      "properties": {
-
+      ],
+      "properties": {
         "decision": {
-
-          "enum": [
-
+          "enum": [
             "accepted",
-
             "unknown",
-
             "rejected"
-
-          ]
-
-        },
-
+          ]
+        },
         "evidence": {
-
-          "type": "string",
-
-          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
-
-          "maxLength": 256
-
-        },
-
+          "type": "string",
+          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
+          "maxLength": 256
+        },
         "reviewer": {
-
-          "type": "string",
-
-          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
-
-          "maxLength": 256
-
-        },
-
+          "type": "string",
+          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
+          "maxLength": 256
+        },
         "observedAt": {
-
-          "type": "string",
-
+          "type": "string",
           "format": "date-time",
-
           "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(?:\\.\\d+)?(?:Z|[+-]\\d{2}:\\d{2})$"
-
-        },
-
+        },
         "scope": {
-
-          "type": "string",
-
+          "type": "string",
           "minLength": 1,
-
           "maxLength": 2048
-
-        }
-
-      }
-
-    },
-
+        }
+      }
+    },
     "release": {
-
-      "type": "object",
-
-      "additionalProperties": false,
-
-      "required": [
-
+      "type": "object",
+      "additionalProperties": false,
+      "required": [
         "modelId",
-
         "version",
-
         "namespace",
-
         "role",
-
         "publicationStatus",
-
         "researchAssurance",
-
         "semanticFingerprint",
-
         "specification",
-
         "agents",
-
         "requires",
-
         "references",
-
         "installationMode",
-
         "binding",
-
         "compatibility"
-
-      ],
-
-      "properties": {
-
+      ],
+      "properties": {
         "modelId": {
-
-          "type": "string",
-
+          "type": "string",
           "pattern": "^[a-z][a-z0-9.-]{2,127}$"
-
-        },
-
+        },
         "version": {
-
-          "type": "string",
-
+          "type": "string",
           "pattern": "^(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)(-[0-9A-Za-z.-]+)?(\\+[0-9A-Za-z.-]+)?$",
-
           "maxLength": 128
-
-        },
-
+        },
         "namespace": {
-
-          "type": "string",
-
-          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
-
-          "maxLength": 256
-
-        },
-
+          "type": "string",
+          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
+          "maxLength": 256
+        },
         "role": {
-
-          "enum": [
-
+          "enum": [
             "core",
-
             "landscape",
-
             "kernel"
-
-          ]
-
-        },
-
+          ]
+        },
         "publicationStatus": {
-
-          "enum": [
-
+          "enum": [
             "published",
-
             "draft",
-
             "legacy",
-
             "retired"
-
-          ]
-
-        },
-
+          ]
+        },
         "researchAssurance": {
-
-          "enum": [
-
+          "enum": [
             "reviewable-draft",
-
             "independently-reviewed"
-
-          ]
-
-        },
-
+          ]
+        },
         "semanticFingerprint": {
-
           "anyOf": [
-
-            {
-
+            {
               "$ref": "#/$defs/fingerprint"
-
             },
-
-            {
-
+            {
               "type": "null"
-
             }
-
-          ]
-
-        },
-
+          ]
+        },
         "specification": {
-
           "$ref": "#/$defs/descriptor"
-
-        },
-
+        },
         "agents": {
-
           "$ref": "#/$defs/descriptor"
-
-        },
-
+        },
         "requires": {
-
           "type": "array",
-
           "minItems": 0,
-
           "items": {
-
             "$ref": "#/$defs/releaseRef"
-
           }
-
-        },
-
+        },
         "references": {
-
           "type": "array",
-
           "minItems": 0,
-
           "items": {
-
             "$ref": "#/$defs/releaseRef"
-
           }
-
-        },
-
+        },
         "installationMode": {
-
-          "enum": [
-
+          "enum": [
             "semantic-only",
-
             "native-binding"
-
-          ]
-
-        },
-
+          ]
+        },
         "binding": {
-
           "anyOf": [
-
-            {
-
+            {
               "$ref": "#/$defs/binding"
-
             },
-
-            {
-
+            {
               "type": "null"
-
             }
-
-          ]
-
-        },
-
+          ]
+        },
         "compatibility": {
-
           "$ref": "#/$defs/compatibility"
-
-        }
-
-      }
-
-    },
-
+        }
+      }
+    },
     "authority": {
-
-      "type": "object",
-
-      "additionalProperties": false,
-
-      "required": [
-
+      "type": "object",
+      "additionalProperties": false,
+      "required": [
         "owner",
-
         "actor",
-
         "purpose",
-
         "policyRef",
-
         "policyDigest",
-
         "decision",
-
         "allowedModelIds",
-
         "allowReviewableDrafts"
-
-      ],
-
-      "properties": {
-
+      ],
+      "properties": {
         "owner": {
-
-          "type": "string",
-
-          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
-
-          "maxLength": 256
-
-        },
-
+          "type": "string",
+          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
+          "maxLength": 256
+        },
         "actor": {
-
-          "type": "string",
-
-          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
-
-          "maxLength": 256
-
-        },
-
+          "type": "string",
+          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
+          "maxLength": 256
+        },
         "purpose": {
-
-          "type": "string",
-
+          "type": "string",
           "minLength": 1,
-
           "maxLength": 2048
-
-        },
-
+        },
         "policyRef": {
-
-          "type": "string",
-
-          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
-
-          "maxLength": 256
-
-        },
-
+          "type": "string",
+          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
+          "maxLength": 256
+        },
         "policyDigest": {
-
-          "type": "string",
-
+          "type": "string",
           "pattern": "^sha256:[a-f0-9]{64}$"
-
-        },
-
+        },
         "decision": {
-
-          "enum": [
-
+          "enum": [
             "allow",
-
             "deny"
-
-          ]
-
-        },
-
+          ]
+        },
         "allowedModelIds": {
-
           "type": "array",
-
           "minItems": 1,
-
           "items": {
-
             "type": "string",
-
             "pattern": "^[a-z][a-z0-9.-]{2,127}$"
-
           }
-
-        },
-
+        },
         "allowReviewableDrafts": {
-
           "type": "boolean"
-
-        }
-
-      }
-
-    },
-
+        }
+      }
+    },
     "provenance": {
-
-      "type": "object",
-
-      "additionalProperties": false,
-
-      "required": [
-
+      "type": "object",
+      "additionalProperties": false,
+      "required": [
         "source",
-
         "masterSystem",
-
         "recordedAt",
-
         "classification",
-
         "evidenceKind"
-
-      ],
-
-      "properties": {
-
+      ],
+      "properties": {
         "source": {
-
-          "type": "string",
-
-          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
-
-          "maxLength": 256
-
-        },
-
+          "type": "string",
+          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
+          "maxLength": 256
+        },
         "masterSystem": {
-
-          "type": "string",
-
-          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
-
-          "maxLength": 256
-
-        },
-
+          "type": "string",
+          "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
+          "maxLength": 256
+        },
         "recordedAt": {
-
-          "type": "string",
-
+          "type": "string",
           "format": "date-time",
-
           "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(?:\\.\\d+)?(?:Z|[+-]\\d{2}:\\d{2})$"
-
-        },
-
+        },
         "classification": {
-
-          "enum": [
-
+          "enum": [
             "public-synthetic",
-
             "private"
-
-          ]
-
-        },
-
+          ]
+        },
         "evidenceKind": {
-
-          "enum": [
-
+          "enum": [
             "observed",
-
             "source-asserted",
-
             "proposal"
-
-          ]
-
-        }
-
-      }
-
+          ]
+        }
+      }
     }
-
   }
-
 }
-

```

FILE implementation/policy.schema.json final sha256:92e0386696c974b1e8a312b60ca08d981c223e9925c8f70dabdfa135b9041543
```diff
--- reviewed/implementation/policy.schema.json
+++ final/implementation/policy.schema.json
@@ -1,210 +1,105 @@
 {
-
   "$schema": "https://json-schema.org/draft/2020-12/schema",
-
   "$id": "https://ver.cy/models/wm-xct-040-model-composition-resolution/versions/0.1.0/policy.schema.json",
-
   "title": "Caller-supplied local composition authority policy",
-
   "type": "object",
-
   "additionalProperties": false,
-
   "required": [
-
     "format",
-
     "version",
-
     "id",
-
     "dimensionId",
-
     "owner",
-
     "actors",
-
     "purposes",
-
     "allowInstall",
-
     "allowedModelIds",
-
     "allowReviewableDrafts",
-
     "reviewers",
-
     "allowedOrigins",
-
     "validFrom",
-
     "validUntil"
-
   ],
-
   "properties": {
-
     "format": {
-
       "const": "vercy-composition-policy"
-
     },
-
     "version": {
-
       "const": 1
-
     },
-
     "id": {
-
       "type": "string",
-
       "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
-
       "maxLength": 256
-
     },
-
     "dimensionId": {
-
       "type": "string",
-
       "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
-
       "maxLength": 256
-
     },
-
     "owner": {
-
       "type": "string",
-
       "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
-
       "maxLength": 256
-
     },
-
     "actors": {
-
       "type": "array",
-
       "minItems": 1,
-
       "items": {
-
         "type": "string",
-
         "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
-
         "maxLength": 256
-
       }
-
     },
-
     "purposes": {
-
       "type": "array",
-
       "minItems": 1,
-
       "items": {
-
         "type": "string",
-
         "minLength": 1,
-
         "maxLength": 2048
-
       }
-
     },
-
     "allowInstall": {
-
       "type": "boolean"
-
     },
-
     "allowedModelIds": {
-
       "type": "array",
-
       "minItems": 1,
-
       "items": {
-
         "type": "string",
-
         "pattern": "^[a-z][a-z0-9.-]{2,127}$"
-
       }
-
     },
-
     "allowReviewableDrafts": {
-
       "type": "boolean"
-
     },
-
     "reviewers": {
-
       "type": "array",
-
       "minItems": 1,
-
       "items": {
-
         "type": "string",
-
         "pattern": "^[a-z][a-z0-9+.-]*:[^\\s]+$",
-
         "maxLength": 256
-
       }
-
     },
-
     "allowedOrigins": {
-
       "type": "array",
-
       "minItems": 1,
-
       "items": {
-
         "type": "string",
-
         "pattern": "^https://[a-z0-9.-]+(?::[0-9]+)?$"
-
       }
-
     },
-
     "validFrom": {
-
       "type": "string",
-
       "format": "date-time",
-
       "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(?:\\.\\d+)?(?:Z|[+-]\\d{2}:\\d{2})$"
-
     },
-
     "validUntil": {
-
       "type": "string",
-
       "format": "date-time",
-
       "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(?:\\.\\d+)?(?:Z|[+-]\\d{2}:\\d{2})$"
-
     }
-
   }
-
 }
-

```

FILE implementation/test_composition.py final sha256:3d4118d631319eef1d0497c4c2833326cf3d9ad85f99ea1efdf0681bcbf85acc
```diff
--- reviewed/implementation/test_composition.py
+++ final/implementation/test_composition.py
@@ -120,15 +120,36 @@
     def test_kernel_leaf_allowed(self):self.plan['releases'][0]['role']='kernel';self.assertTrue(self.runplan()['valid'])
     def test_policy_change_before_staging_commit(self):
         p,pol,lock=self.files();original=c.tempfile.mkdtemp
         def mutate(*args,**kwargs):
             out=original(*args,**kwargs);pol.write_bytes(b'{}');return out
         with patch.object(c.tempfile,'mkdtemp',side_effect=mutate):
             with self.assertRaisesRegex(c.Invalid,'STALE:'):c.stage(p,self.assets,pol,lock,self.root/'staged')
         self.assertFalse((self.root/'staged').exists())
+    def test_pattern_properties_reopens_root_refused(self):
+        self.plan['releases']=[self.release('test.company',True,True)];r=self.plan['releases'][0];s=c.load(self.assets/r['binding']['instanceSchema']['path']);s['patternProperties']={'^':{}};self.replaceasset(r,'instanceSchema',s);self.rejects('NESTED')
+    def test_list_typed_open_object_refused(self):
+        self.plan['releases']=[self.release('test.company',True,True)];r=self.plan['releases'][0];s=c.load(self.assets/r['binding']['instanceSchema']['path']);s['properties']['snapshot']={'type':['object','null']};self.replaceasset(r,'instanceSchema',s);self.rejects('NESTED')
+    def test_expired_policy(self):
+        self.policy['validUntil']='2026-01-01T00:00:00Z';self.policy_raw=c.encode(self.policy);self.plan['authority']['policyDigest']=c.digest(self.policy_raw);self.rejects('POLICY')
+    def test_unapproved_reviewer(self):self.plan['releases'][0]['compatibility']['reviewer']='urn:reviewer:other';self.rejects('COMPATIBILITY')
+    def test_expanded_allowlist(self):self.plan['authority']['allowedModelIds'].append('test.forbidden');self.rejects('AUTHORITY')
+    def test_future_provenance(self):self.plan['provenance']['recordedAt']='2100-01-01T00:00:00Z';self.rejects('TIME')
+    def test_overlapping_dependency_kinds(self):
+        r=self.plan['releases'][0];r['requires']=r['references']=[{'modelId':'test.unit','version':'1.0.0'}];self.rejects('EDGE')
+    def test_duplicate_dependency(self):
+        self.plan['releases'][0]['requires']=[{'modelId':'test.unit','version':'1.0.0'}]*2;self.rejects('EDGE')
+    def test_malformed_lock(self):self.lock_raw=c.encode({'models':['wrong']});self.plan['baseLockDigest']=c.digest(self.lock_raw);self.rejects('LOCK')
+    def test_non_object_spec(self):self.plan['releases'][0]['specification']=self.asset('test.company/spec.yaml',[],'application/yaml');self.rejects('SPEC')
+    def test_invalid_date(self):self.plan['createdAt']='2026-13-01T00:00:00Z';self.assertRaises(c.Invalid,self.runplan)
+    def test_case_insensitive_asset_collision(self):
+        r=self.plan['releases'][0];d=copy.deepcopy(r['specification']);d['path']='Test.Company/SPEC.yaml';p=self.assets/d['path'];p.parent.mkdir(exist_ok=True);p.write_bytes((self.assets/r['specification']['path']).read_bytes());r['agents']=d;self.rejects('COLLISION')
+    def test_corrupt_staged_plan_refused(self):
+        p,pol,lock=self.files();target=self.root/'staged';c.stage(p,self.assets,pol,lock,target);(target/'composition-plan.json').write_bytes(b'{}')
+        with self.assertRaisesRegex(c.Invalid,'TARGET:'):c.stage(p,self.assets,pol,lock,target)
 
 if __name__=='__main__':
     suite=unittest.defaultTestLoader.loadTestsFromTestCase(CompositionTests)
     result=unittest.TextTestRunner(verbosity=2).run(suite)
     report={'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'passed':result.wasSuccessful(),'scope':'Offline exact closure, trusted policy, descriptor integrity, readiness, historical correction, idempotency and staged-commit failure. Synthetic assets; native runtime acceptance is a separate test.'}
     (Path(__file__).parent/'test-results.json').write_bytes(c.encode(report))
     raise SystemExit(0 if result.wasSuccessful() else 1)

```

FILE implementation/acceptance.py final sha256:fa36502daaece79dba3bd2373bd8c8b4aa1e18a340f9bbcad67ba23b15594975
```diff
--- reviewed/implementation/acceptance.py
+++ final/implementation/acceptance.py
@@ -1,96 +1,60 @@
 """Reproduce three synthetic new-Dimension trials against a trusted Vercy skill.
-
 Usage: python acceptance.py --skill /trusted/vercy/skills/vercy --report result.json
-
 Never uses real company data or changes an existing Dimension.
-
 """
-
 from pathlib import Path
-
-import argparse,copy,importlib.util,json,sys,tempfile,subprocess
+import argparse,copy,importlib.util,json,sys,tempfile,subprocess,shutil
 from unittest.mock import patch
 import bootstrap_dimension as bd
 import composition as c
-
 from bootstrap_dimension import bootstrap
 
-
-
 def run(skill):
-
     skill=Path(skill).resolve();examples=Path(__file__).resolve().parent/'examples'
-
     sys.path.insert(0,str(skill/'scripts'))
-
     from write_record import append
-
     from validate_dimension import validate as native_validate
-
     reports=[];failure_checks=[]
     with tempfile.TemporaryDirectory(prefix='vercy-composition-acceptance-') as tmp:
-
         root=Path(tmp)
-
         for name in ['startup','group','ai-team']:
-
             src=examples/name;plan=c.load(src/'plan.json');stage=root/(name+'-stage');target=root/name
-
             c.stage(src/'plan.json',examples/'assets',src/'policy.json',src/'current.lock',stage)
-
             result=bootstrap(stage,src/'policy.json',src/'current.lock',skill,target,'Synthetic '+name,plan['dimensionId'])
-
             assert c.load(target/'dimension.yaml')['id']==plan['dimensionId']
-
             obj={'recordType':'object','schemaVersion':'1.0.0','recordId':'urn:synthetic:org:'+name+':r1','objectId':'urn:synthetic:org:'+name,'objectType':'vr.wm-org-001:organization','name':'Synthetic '+name,'description':'Public fictional acceptance fixture','recordedAt':c.now(),'previousRecordId':None,'state':'active','provenance':{'source':'urn:synthetic:reference','synthetic':True},'accessClass':'synthetic-private'}
-
             # Start from the current runtime fact template, retaining its exact temporal/provenance shape.
-
             template=c.load(examples/'native-fact.reference.json')
-
             fact={**template,'factId':'urn:synthetic:org:'+name+':name:r1','subjectId':obj['objectId'],'path':'organization.reference.name','value':obj['name'],'unit':None}
-
             for kind,value in [('object',obj),('fact',fact)]:
-
                 f=root/(name+'-'+kind+'.json');f.write_bytes(c.encode(value));append(target,kind,f)
-
             nested=None
-
             if name=='ai-team':
-
                 vf=examples/'assets/wm-org-017-performance-objective-review/validate_examples.py'
-
                 module_spec=importlib.util.spec_from_file_location('trusted_performance_reference',vf);module=importlib.util.module_from_spec(module_spec);module_spec.loader.exec_module(module)
-
-                good=c.load(examples/'example-founder-draft.json');bad=copy.deepcopy(good);bad['policy']['automatic_employment_decisions']=True
-
+                actual_fact=c.load(examples/'native-fact.reference.json');good=actual_fact['value'];assert good==c.load(examples/'example-founder-draft.json')
+                bad=copy.deepcopy(good);bad['policy']['automatic_employment_decisions']=True
                 assert not module.errors(good) and module.errors(bad)
-
-                for kind in ['object','fact']:append(target,kind,examples/('native-'+kind+'.reference.json'))
-
-                nested={'positivePassed':True,'negativeRejected':True,'rule':'No automatic employment decisions','execution':'Explicit trusted acceptance harness only; composer never executes package code.'}
-
+                append(target,'object',examples/'native-object.reference.json')
+                bad_target=root/'ai-team-negative-copy';shutil.copytree(target,bad_target)
+                bad_fact=copy.deepcopy(actual_fact);bad_fact['value']=bad;bad_file=root/'bad-performance-fact.json';bad_file.write_bytes(c.encode(bad_fact))
+                bad_written=append(bad_target,'fact',bad_file);assert native_validate(bad_target)['valid']
+                actual_bad=c.load(bad_target/bad_written['written']);assert module.errors(actual_bad['value'])
+                good_written=append(target,'fact',examples/'native-fact.reference.json');assert not module.errors(c.load(target/good_written['written'])['value'])
+                nested={'positiveStoredFactPassed':True,'negativeStoredFactPassedV3':True,'negativeStoredFactRejectedByCompanion':True,'rule':'No automatic employment decisions','execution':'Explicit trusted acceptance harness only; composer never executes package code.'}
             validation=native_validate(target);assert validation['valid'],validation
-
             # A second bootstrap must refuse, preserving all bytes.
-
             before={str(p.relative_to(target)):c.digest(p.read_bytes()) for p in target.rglob('*') if p.is_file()}
-
             try:bootstrap(stage,src/'policy.json',src/'current.lock',skill,target,'Synthetic '+name,plan['dimensionId'])
-
             except c.Invalid:pass
-
             else:raise AssertionError('existing Dimension was not refused')
-
             assert before=={str(p.relative_to(target)):c.digest(p.read_bytes()) for p in target.rglob('*') if p.is_file()}
-
             validation.pop('dimension',None)
-
             reports.append({'profile':name,'passed':True,'nativeModels':result['nativeBoundModels'],'semanticOnlyModels':result['semanticOnlyModels'],'nativeValidation':validation,'nestedValidation':nested,'existingDimensionPreserved':True})
         src=examples/'startup';stage=root/'startup-stage';plan=c.load(src/'plan.json')
         def invoke(target,namespace=plan['dimensionId']):return bootstrap(stage,src/'policy.json',src/'current.lock',skill,target,'Synthetic startup',namespace)
         target=root/'wrong-dimension'
         try:invoke(target,'urn:dimension:other')
         except c.Invalid as e:assert str(e).startswith('OWNER:')
         else:raise AssertionError('namespace mismatch allowed')
         assert not target.exists();failure_checks.append('authorized Dimension identity enforced')
@@ -106,11 +70,9 @@
         target=root/'rename-invalid'
         with patch.object(c.os,'rename',side_effect=OSError('injected rename failure')):
             try:invoke(target)
             except OSError:pass
             else:raise AssertionError('rename failure ignored')
         assert not target.exists() and not list(root.glob('.rename-invalid.*'));failure_checks.append('failed activation cleans only own temporary state')
     return {'format':'vercy-composition-acceptance','executedAt':c.now(),'passed':len(reports),'failed':0,'scope':'Synthetic limited bindings, not startup/group/AI-enterprise domain completeness; no real company data.','profiles':reports,'bootstrapFailureChecks':failure_checks}
 if __name__=='__main__':
-
     p=argparse.ArgumentParser();p.add_argument('--skill',required=True);p.add_argument('--report',required=True);a=p.parse_args();report=run(a.skill);Path(a.report).write_bytes(c.encode(report));print(json.dumps(report,indent=2))
-

```

FILE implementation/test-results.json final sha256:992fec9c07998f8bd366c1f77780e4b16e7b122573102f4f5ee3fe9169010adf
```diff
--- reviewed/implementation/test-results.json
+++ final/implementation/test-results.json
@@ -1,7 +1,7 @@
 {
   "errors": 0,
   "failures": 0,
   "passed": true,
   "scope": "Offline exact closure, trusted policy, descriptor integrity, readiness, historical correction, idempotency and staged-commit failure. Synthetic assets; native runtime acceptance is a separate test.",
-  "tests": 55
+  "tests": 68
 }

```

FILE implementation/acceptance-results.json final sha256:c34a5f95b87e5cda3a86619134faa142ecbd0c616043ab1f8776523a6c906ecc
```diff
--- reviewed/implementation/acceptance-results.json
+++ final/implementation/acceptance-results.json
@@ -1,15 +1,15 @@
 {
   "bootstrapFailureChecks": [
     "authorized Dimension identity enforced",
     "failed native validation never activates",
     "failed activation cleans only own temporary state"
   ],
-  "executedAt": "2026-09-21T15:13:51Z",
+  "executedAt": "2026-09-21T15:20:40Z",
   "failed": 0,
   "format": "vercy-composition-acceptance",
   "passed": 3,
   "profiles": [
     {
       "existingDimensionPreserved": true,
       "nativeModels": 1,
       "nativeValidation": {
@@ -67,18 +67,19 @@
         "errors": [],
         "schemas": "https://ver.cy/schemas/dimension/1.0/",
         "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety",
         "valid": true,
         "warnings": []
       },
       "nestedValidation": {
         "execution": "Explicit trusted acceptance harness only; composer never executes package code.",
-        "negativeRejected": true,
-        "positivePassed": true,
+        "negativeStoredFactPassedV3": true,
+        "negativeStoredFactRejectedByCompanion": true,
+        "positiveStoredFactPassed": true,
         "rule": "No automatic employment decisions"
       },
       "passed": true,
       "profile": "ai-team",
       "semanticOnlyModels": 0
     }
   ],
   "scope": "Synthetic limited bindings, not startup/group/AI-enterprise domain completeness; no real company data."

```

FILE implementation/upstream-verification.json final sha256:31180eaf0e915eb01cba9c62af209e29d4c28c2e65c0763da0ea0a5c479a7dd6
```diff
--- reviewed/implementation/upstream-verification.json
+++ final/implementation/upstream-verification.json
@@ -1,50 +1,59 @@
 {
-
+  "scope": "Only explicitly listed original upstream assets; Organization name binding is authored by WM-XCT-040 and verified at publication.",
   "checks": [
-
     {
-
+      "url": "https://ver.cy/models/wm-org-001-organization/AGENTS.md",
+      "http": 200,
+      "sha256": "df35cb3f0a3df14259ecf9207e0365aac82f19db7d0839ca64dff9985d1b0c87",
+      "exactBytesMatch": true
+    },
+    {
       "url": "https://ver.cy/models/wm-org-001-organization/spec.yaml",
-
       "http": 200,
-
       "sha256": "ce27fcf5453fb390d7aea631ab91748404ca25968a8b3af67311bf4c65a76cf1",
-
-      "exactBytesMatch": true,
-
-      "profile": "Vercy JSON-compatible YAML"
-
+      "exactBytesMatch": true
     },
-
     {
-
+      "url": "https://ver.cy/models/wm-org-002-organizational-unit/AGENTS.md",
+      "http": 200,
+      "sha256": "a2cab64d839356e39f70ff8a7bbf8e3cad01c363a2712d018afd11c46353a775",
+      "exactBytesMatch": true
+    },
+    {
       "url": "https://ver.cy/models/wm-org-002-organizational-unit/spec.yaml",
-
       "http": 200,
-
       "sha256": "9e3e80da4db6db6589991102b91af4af1a00080cd348848250b63f70a97b2330",
-
-      "exactBytesMatch": true,
-
-      "profile": "Vercy JSON-compatible YAML"
-
+      "exactBytesMatch": true
     },
-
     {
-
+      "url": "https://ver.cy/models/wm-org-017-performance-objective-review/AGENTS.md",
+      "http": 200,
+      "sha256": "628bfbb58674792e65b277273b48b174f194e9d113c54a07cd68b9d5fb9b5c7c",
+      "exactBytesMatch": true
+    },
+    {
+      "url": "https://ver.cy/models/wm-org-017-performance-objective-review/instance.schema.json",
+      "http": 200,
+      "sha256": "a97719fa2a646dfa6fb2a94f34cb9914c1ce4fad62f07e6166891ab55b0ff4a8",
+      "exactBytesMatch": true
+    },
+    {
+      "url": "https://ver.cy/models/wm-org-017-performance-objective-review/runtime-model.reference.json",
+      "http": 200,
+      "sha256": "11add1d36caaad434ee9e15677050dde12c7e1faf2a35beeb13b1fc774d5de3b",
+      "exactBytesMatch": true
+    },
+    {
       "url": "https://ver.cy/models/wm-org-017-performance-objective-review/spec.yaml",
-
       "http": 200,
-
       "sha256": "dfd609fcb460b3b8878df6c0e6cde28f324512b053705b007ec71e2d8aea01f7",
-
-      "exactBytesMatch": true,
-
-      "profile": "Vercy JSON-compatible YAML"
-
+      "exactBytesMatch": true
+    },
+    {
+      "url": "https://ver.cy/models/wm-org-017-performance-objective-review/validate_examples.py",
+      "http": 200,
+      "sha256": "1cd92b559bc70caa454ca8d4911fe7850a76e33b21c53d56ade3f3126ca6737a",
+      "exactBytesMatch": true
     }
-
   ]
-
 }
-

```

FILE implementation/README.md final sha256:72e74102fd221bab10ab50d70a2b461441a790865bade8b3b9db73359d530372
```diff
--- reviewed/implementation/README.md
+++ final/implementation/README.md
@@ -1,55 +1,73 @@
 # Композиция моделей для нового Измерения компании
-
-
 
 WM-XCT-040 Model Composition Resolution, 0.1.0. Общий контракт и эталонная реализация.
 
-
-
 Модель отвечает на вопрос: какие точные версии моделей выбраны для этого Измерения, кто разрешил их использование, какие зависимости обязательны, какие байты проверены и какие данные уже можно записывать. Это один контракт композиции. Он не заменяет ядро Vercy, модели Компании, Юрлица, Подразделения или Сотрудника.
-
-
 
 Публикация доступна для использования и дальнейшего рецензирования. Уровень исследования: `reviewable-draft`. Полная корпоративная архитектура и универсальная совместимость не заявляются. Состояние независимых проверок и оставшиеся ограничения находятся в исследовательском досье.
 
-
-
 ## Состав
 
-
-
 - `model-spec.md`: граница, типы, связи, состояния, права, время, мастерство данных, миграции.
-
 - `field-catalog.json`: поля с типами, обязательностью, источниками и владельцами.
-
 - `whole-object-coverage.json`: пять аспектов для каждого из девяти типов контракта.
-
 - `composition-plan.schema.json`, `policy.schema.json`: исполняемые схемы JSON Schema 2020-12.
-
 - `composition.py`: проверка точного состава и создание пакета проверенных файлов.
-
 - `bootstrap_dimension.py`: создание только нового Измерения через доверенную локальную копию Vercy skill.
-
 - `crosswalk.json`, `kernel-boundary-decision.json`: сопоставления с существующими моделями и решение о границе.
-
 - `examples/`: вымышленные сценарии, политики, точные версии и копии опубликованных пакетов.
-
 - `test-results.json`, `acceptance-results.json`: фактические результаты испытаний.
-
-
 
 ## Быстрый воспроизводимый пример
 
-
-
-Распакуйте полный пакет. Нужны Python 3.11+ и `jsonschema >=4,<5`. Путь к Vercy skill задаётся явно: используйте доверенную локальную копию из официального Vercy. Composer сам не скачивает и не исполняет код из пакетов.
-
-
+Распакуйте полный пакет. Нужны Python 3.12+ и `jsonschema[format-nongpl] >=4,<5`. Путь к Vercy skill задаётся явно: используйте доверенную локальную копию из официального Vercy. Composer сам не скачивает и не исполняет код из пакетов.
 
 ```text
+python -m pip install "jsonschema[format-nongpl]>=4,<5"
+python test_composition.py
+python acceptance.py --skill /trusted/vercy/skills/vercy --report acceptance-local.json
+```
 
-python -m pip install "jsonschema>=4,<5"
+`acceptance.py` создаёт временные тестовые Измерения и удаляет только свои временные данные после проверки. В нём явно запускается проверенный пример валидатора вложенных данных. Обычный Composer такой код автоматически не запускает.
 
-python test_composition.py
+Чтобы оставить отдельное учебное Измерение:
 
-python acceptance.py --skill /trusted/vercy/skills/vercy --report acceptance-local.json
+```text
+python composition.py validate examples/startup/plan.json --assets examples/assets --policy examples/startup/policy.json --lock examples/startup/current.lock
+python composition.py stage examples/startup/plan.json --assets examples/assets --policy examples/startup/policy.json --lock examples/startup/current.lock --target /existing-parent/startup-stage
+python bootstrap_dimension.py --stage /existing-parent/startup-stage --policy examples/startup/policy.json --lock examples/startup/current.lock --skill /trusted/vercy/skills/vercy --target /existing-parent/startup-dimension --name "Synthetic startup" --namespace urn:dimension:synthetic:startup
+```
+
+Замените пути на свои. Родительский каталог должен существовать, конечные каталоги должны быть новыми. `--namespace` должен точно совпадать с `dimensionId` плана и независимой политики. Bootstrap создаёт структуру и реестры; данные организации вы добавляете отдельно. Проверка `acceptance.py` показывает такой пример.
+
+## Использование для своей компании
+
+Вымышленные политики из примеров не дают полномочий работать с вашей компанией. Владелец Измерения отдельно задаёт идентификатор, исполнителей, цель, разрешённые модели, источники и срок действия политики. План ссылается на SHA-256 этой политики и исходного lock-файла. Обновление этих документов требует пересчёта соответствующих контрольных сумм.
+
+Для каждой выбранной модели укажите точную версию, SHA-256 и размер спецификации и AGENTS.md. Разделите обязательные зависимости `requires` и необязательные ссылки `references`. Замкнутый состав включает все обязательные зависимости, объявленные в плане, и исключает лишние относительно этого графа пакеты. Зависимости не извлекаются автоматически из текста спецификаций. Циклы, неоднозначные версии и конфликты пространств имён отклоняются.
+
+Режим `semantic-only` позволяет хранить и использовать семантическую спецификацию. Он не объявляет схему фактов готовой. Для `native-binding` отдельно укажите runtime-схему, привязанную к точным байтам спецификации. Для вложенного снимка также нужны закрытая схема данных и отдельный предметный валидатор. Успешная проверка V3 не заменяет проверку содержимого вложенного объекта.
+
+Учебные планы имеют ограниченный срок: до конца 2026 года. После истечения можно проверить исторический состав через `validate --at` с датой действия плана. Для нового создания нужна новая действующая политика и новый план; историческая дата не разрешает запись.
+
+## Что подтверждают сценарии
+
+| Сценарий | Проверено | Граница |
+|---|---|---|
+| Startup | Новый Dimension, Organization, объект и факт имени, V3 | Только имя; не вся схема организации |
+| Group | Organization с данными и Organizational Unit как семантический пакет | Подразделение не получает выдуманную runtime-схему |
+| AI team | Organization и опубликованный пример Performance Case, V3 и отдельный вложенный валидатор | Синтетический пример, не система реальной оценки людей |
+
+Во всех сценариях повторное создание поверх существующего Измерения отклоняется с сохранением данных.
+
+## Миграция и восстановление
+
+Реализация создаёт только новые Измерения. Для существующего Измерения нужен отдельный план миграции с резервной копией, анализом потерь и преобразованием данных. Автоматическое обновление и понижение версий не поддерживаются.
+
+Обычная ошибка убирает только временный каталог операции и её блокировку. При аварийном завершении процесса сначала проверьте владельца оставшейся блокировки, отсутствие активного процесса и квитанцию. Не удаляйте блокировки вслепую. Переименование каталога служит точкой активации на проверенной локальной файловой системе; распределённая транзакция и устойчивость к потере питания не заявляются.
+
+Контракт не реализует корпоративную IAM, проверку цифровых подписей издателей, ELMM minimum-version selection, исполнение всех правил предметных моделей или изменение действующих Измерений. Эти ограничения не скрываются за отметкой `published`.
+
+Спецификации принимаются только в формате JSON либо JSON с одной начальной строкой `#`, то есть в используемой Vercy JSON-совместимой форме YAML. Произвольный YAML отклоняется. Три пакета из примеров проверены по байтам с опубликованными версиями ver.cy. Поддерживаемый preset этого адаптера: `commercial-company`.
+
+Примеры воспроизводимы с текущими планами до 31 декабря 2026 года; далее нужны новые политика и план. Копии семантических спецификаций и AGENTS.md сохраняют источник. Минимальная схема имени Organization создана для этого выпуска; пример Performance использует уже опубликованную эталонную привязку. Наличие вложенной схемы и валидатора обязательно, но их исполнение остаётся отдельным шагом и не выполняется автоматически при создании Измерения. Подтверждение активации относится к Windows и процессам, соблюдающим блокировку.

```
