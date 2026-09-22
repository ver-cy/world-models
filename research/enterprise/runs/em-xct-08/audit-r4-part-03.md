R4 DELTA INPUT PART 3/8. Continue retaining the exact R3 baseline plus these patches. No tools or audit yet. A file/diff may span parts. ACK only this part number and its end marker.

da2c8c1c19d92dce0b2cd4d3d4be96af049266d83a8be86f169326",
-      "previousDigest": "sha256:f3c67ad90c7a3a70d4ac9d841189b27c610cf57641600f78795a7631aa0b58d1",
+      "previousDigest": "sha256:0e6b4572b4abb74e1badf99dc8a2165ae7e3720f8bf3e04ca4d61bf080949eb1",
       "recordedAt": "2026-01-01T00:00:14Z",
       "result": {
         "receiptId": "urn:synthetic:sync-register:international:14:receipt",
         "status": "committed"
@@ -720,11 +720,11 @@
           "fence": 1
         },
         "op": "commit"
       },
-      "digest": "sha256:00d02dcc93f97922b9e063992f304f33eafda951805e80c544dd865a28f5618b",
+      "digest": "sha256:c6ae44250a09eb111a11fcaee34c1412251a9fb8ccb21986afd9148b85a3e504",
       "outcomeDigest": "sha256:ff77ec3a3328cc54389f0fb79090d485699a07ee99b95105b19bf404b643f78a",
-      "previousDigest": "sha256:f903971086a285b686df55c4b1ac2de14c328efe700d6de0f08e8633d3756c45",
+      "previousDigest": "sha256:ae43e2dffa98574dc4928c09964ef7f8dac407faa1f31d8e71788178c12ec137",
       "recordedAt": "2026-01-01T00:00:15Z",
       "result": {
         "receiptId": "urn:synthetic:sync-register:international:15:receipt",
         "status": "committed"
@@ -1573,7 +1573,7 @@
       }
     },
     "conflicts": []
   },
-  "root": "sha256:00d02dcc93f97922b9e063992f304f33eafda951805e80c544dd865a28f5618b",
+  "root": "sha256:c6ae44250a09eb111a11fcaee34c1412251a9fb8ccb21986afd9148b85a3e504",
   "resumable": false
 }
--- a/examples/startup.json
+++ b/examples/startup.json
@@ -1,8 +1,8 @@
 {
   "format": "vercy-source-sync-archive",
   "version": "0.1.0",
-  "buildId": "sha256:90421fd37ea30b8b7fb546c5fffdf3cbf28ef16a6daf487cbc919f5644515287",
+  "buildId": "sha256:b782bbca6c4b5bcc9344dde998d88486c1635ce45a00fbcf6bb7bb179af25cd6",
   "config": {
     "admin": "urn:synthetic:admin",
     "dimensionId": "urn:synthetic:company-dimension:startup",
     "protectedNamespace": "urn:synthetic:evidence-store",
@@ -26,11 +26,11 @@
           "tenant": "tenant-a"
         },
         "op": "source"
       },
-      "digest": "sha256:db324d4dddb756590ae99752d843db8327027d61740c227e1fdba3d8f007c30d",
+      "digest": "sha256:9d5b946fe84249622ea6453c7369b5e79f58b2e8c073f2763e7438d6d33ef16b",
       "outcomeDigest": "sha256:470b1868e6b50ecb494e246d69f416d9cbb628a8f610b1460c7b612f3631079a",
-      "previousDigest": "sha256:0d1fc5f13e6ab0a56afd7bc1a16305b7040c0bfd655a89fd6539a4dfec63eaa8",
+      "previousDigest": "sha256:2bd3200d4f3f73d02c7b67acee9d433d29e783cb5dcb40f1a685bc34bc2fa1ef",
       "recordedAt": "2026-01-01T00:00:01Z",
       "result": {
         "status": "recorded"
       },
@@ -79,11 +79,11 @@
           }
         },
         "op": "scope"
       },
-      "digest": "sha256:31613037b9f749a5cd18694866913d1bf1680bbdbdee1b3b16b248e16b69a325",
+      "digest": "sha256:6d0c0352234d74aae7f9edbeeded562ce6b241db1815dd87e5d4c0eec7fb4291",
       "outcomeDigest": "sha256:8612a3395c791d4b7f2c6b9859350c27abb41c5e8cc388f5ede2f5f804d9417e",
-      "previousDigest": "sha256:db324d4dddb756590ae99752d843db8327027d61740c227e1fdba3d8f007c30d",
+      "previousDigest": "sha256:9d5b946fe84249622ea6453c7369b5e79f58b2e8c073f2763e7438d6d33ef16b",
       "recordedAt": "2026-01-01T00:00:02Z",
       "result": {
         "status": "recorded"
       },
@@ -128,11 +128,11 @@
           ]
         },
         "op": "catalogue"
       },
-      "digest": "sha256:9da798a20d49c6b772d2280471373c35069784d0a7525fd991ab54ccafe9ae0f",
+      "digest": "sha256:4de3bcd73b198fcce6234a583f54cb6e9b7db9a319292eeff715467532285bbc",
       "outcomeDigest": "sha256:8b699c3d78da339504de219f6ca9884212b7933560c4a9ae509aa37721106263",
-      "previousDigest": "sha256:31613037b9f749a5cd18694866913d1bf1680bbdbdee1b3b16b248e16b69a325",
+      "previousDigest": "sha256:6d0c0352234d74aae7f9edbeeded562ce6b241db1815dd87e5d4c0eec7fb4291",
       "recordedAt": "2026-01-01T00:00:03Z",
       "result": {
         "status": "recorded"
       },
@@ -186,11 +186,11 @@
           "revision": 1
         },
         "op": "policy"
       },
-      "digest": "sha256:43d3b2fae2ac70b1143ee7b61abe52cd4d24bdcfa49d5d5bd44d1ee003646aa8",
+      "digest": "sha256:4576103456e2e93382a32d5c9548307f374ed9e90419e03d1f9d1063a5e54baf",
       "outcomeDigest": "sha256:892a97170d778b4d1ce534b4c980602ac0213097de1edfdb274c5a5627e4e383",
-      "previousDigest": "sha256:9da798a20d49c6b772d2280471373c35069784d0a7525fd991ab54ccafe9ae0f",
+      "previousDigest": "sha256:4de3bcd73b198fcce6234a583f54cb6e9b7db9a319292eeff715467532285bbc",
       "recordedAt": "2026-01-01T00:00:04Z",
       "result": {
         "status": "recorded"
       },
@@ -211,11 +211,11 @@
           "scopeId": "urn:synthetic:scope"
         },
         "op": "epoch-open"
       },
-      "digest": "sha256:790b07e4315f39ea5fb6e591e7eeccd0ed6957bd1e53e6889e54a6a3d579eb25",
+      "digest": "sha256:fa8bff87061972823adfdb7329f7a7a0996c294acf9973473f895b55b34e9c96",
       "outcomeDigest": "sha256:1b55d2926c9cbfc018971784d8044c1011989738aa50a996a5ac75b1acdaf840",
-      "previousDigest": "sha256:43d3b2fae2ac70b1143ee7b61abe52cd4d24bdcfa49d5d5bd44d1ee003646aa8",
+      "previousDigest": "sha256:4576103456e2e93382a32d5c9548307f374ed9e90419e03d1f9d1063a5e54baf",
       "recordedAt": "2026-01-01T00:00:05Z",
       "result": {
         "status": "recorded"
       },
@@ -256,11 +256,11 @@
           "validTo": null
         },
         "op": "mapping"
       },
-      "digest": "sha256:f3fb4722e83bf8235d4047d06629d569541cc454e184dd3de0b841208fab7d76",
+      "digest": "sha256:ed6c9d26d56a5ad1ad8a6f9ecec5cbb12350ad3653cfe43f6342c073d67aa942",
       "outcomeDigest": "sha256:01a5dbe5377ee91fbdfa36cf6d7b440e2b6a0bd40ee1f15a1642097626ae6f5d",
-      "previousDigest": "sha256:790b07e4315f39ea5fb6e591e7eeccd0ed6957bd1e53e6889e54a6a3d579eb25",
+      "previousDigest": "sha256:fa8bff87061972823adfdb7329f7a7a0996c294acf9973473f895b55b34e9c96",
       "recordedAt": "2026-01-01T00:00:06Z",
       "result": {
         "status": "recorded"
       },
@@ -276,11 +276,11 @@
           "to": "active"
         },
         "op": "mapping-state"
       },
-      "digest": "sha256:45c78437acfbd8b0626d7e1ed05040c3667fdbcb915f7285d1ebbafe79b68060",
+      "digest": "sha256:de6780007b37fda6af4c8d7c490697724d16ba144e330db00d2e441ece2121cf",
       "outcomeDigest": "sha256:cdbc0995f31de79cb9fbe22d2283f57dcf9596d5e911d7fd31ca9d05bb0d23e6",
-      "previousDigest": "sha256:f3fb4722e83bf8235d4047d06629d569541cc454e184dd3de0b841208fab7d76",
+      "previousDigest": "sha256:ed6c9d26d56a5ad1ad8a6f9ecec5cbb12350ad3653cfe43f6342c073d67aa942",
       "recordedAt": "2026-01-01T00:00:07Z",
       "result": {
         "status": "recorded"
       },
@@ -321,11 +321,11 @@
           "validTo": null
         },
         "op": "mapping"
       },
-      "digest": "sha256:506c9340c7175553c9207d38f798640d25d681a6e9c514dedc959a4735fcf54f",
+      "digest": "sha256:5f4af93647ea8ba85b3ec45fd281ee2cfb52ab960d2bf7f8e3be2f9ed4198f7c",
       "outcomeDigest": "sha256:01d954094c8062ef92c7e6decdcf61d2ed03c0a0c057e2f2a3612bbf228c8884",
-      "previousDigest": "sha256:45c78437acfbd8b0626d7e1ed05040c3667fdbcb915f7285d1ebbafe79b68060",
+      "previousDigest": "sha256:de6780007b37fda6af4c8d7c490697724d16ba144e330db00d2e441ece2121cf",
       "recordedAt": "2026-01-01T00:00:08Z",
       "result": {
         "status": "recorded"
       },
@@ -341,11 +341,11 @@
           "to": "active"
         },
         "op": "mapping-state"
       },
-      "digest": "sha256:afdb2ad1c7ecfeb5699d75a52e725ea22e4a36538861f9ec54232d27e9c9e9c0",
+      "digest": "sha256:28cbb8573a730bf62766f0effe9b3852930eda94840291aa8294b493fd842997",
       "outcomeDigest": "sha256:dd491df46aed08ebe64b1e19cf650e868758840d89f1eeb88118d2db0fd5c3c5",
-      "previousDigest": "sha256:506c9340c7175553c9207d38f798640d25d681a6e9c514dedc959a4735fcf54f",
+      "previousDigest": "sha256:5f4af93647ea8ba85b3ec45fd281ee2cfb52ab960d2bf7f8e3be2f9ed4198f7c",
       "recordedAt": "2026-01-01T00:00:09Z",
       "result": {
         "status": "recorded"
       },
@@ -432,11 +432,11 @@
           "fence": 1
         },
         "op": "commit"
       },
-      "digest": "sha256:e7eafb6e9fd82648abf34598a36413e421cc082ffa72a85a652e2d84b87dec3d",
+      "digest": "sha256:fc37443aed184b7394a320f3b5a1ee68a15fd1f5f67c61ceb2368efb551f226b",
       "outcomeDigest": "sha256:96bff5010e47fde4011daa2250a652d1cad2e80e792a377912317395284fc0a7",
-      "previousDigest": "sha256:afdb2ad1c7ecfeb5699d75a52e725ea22e4a36538861f9ec54232d27e9c9e9c0",
+      "previousDigest": "sha256:28cbb8573a730bf62766f0effe9b3852930eda94840291aa8294b493fd842997",
       "recordedAt": "2026-01-01T00:00:10Z",
       "result": {
         "receiptId": "urn:synthetic:sync-register:startup:10:receipt",
         "status": "committed"
@@ -497,11 +497,11 @@
           "fence": 1
         },
         "op": "commit"
       },
-      "digest": "sha256:d23ddb55cef4095d2feb3b2c21191e7ede78991a8831c5c3198d551d56044582",
+      "digest": "sha256:09d2537d1322cba3fa08eeee1e78a5e580e6442f22583e509c42710a464713a4",
       "outcomeDigest": "sha256:a03731681f1a6a771e084f98d33827458a3fe63afef45b05c61e72f3b80e6e9d",
-      "previousDigest": "sha256:e7eafb6e9fd82648abf34598a36413e421cc082ffa72a85a652e2d84b87dec3d",
+      "previousDigest": "sha256:fc37443aed184b7394a320f3b5a1ee68a15fd1f5f67c61ceb2368efb551f226b",
       "recordedAt": "2026-01-01T00:00:11Z",
       "result": {
         "receiptId": "urn:synthetic:sync-register:startup:11:receipt",
         "status": "committed"
@@ -1179,7 +1179,7 @@
       }
     },
     "conflicts": []
   },
-  "root": "sha256:d23ddb55cef4095d2feb3b2c21191e7ede78991a8831c5c3198d551d56044582",
+  "root": "sha256:09d2537d1322cba3fa08eeee1e78a5e580e6442f22583e509c42710a464713a4",
   "resumable": false
 }
--- a/fixtures.py
+++ b/fixtures.py
@@ -78,9 +78,9 @@
             h.mapping(value='42');h.mapping('urn:synthetic:mapping:b',value='42',target='urn:synthetic:project:2',scope_id='urn:synthetic:scope:b')
             h.commit(h.batch(items=[item('42'),item('01'),item('1')]))
             h.commit(h.batch('tenant-b',scope_id='urn:synthetic:scope:b',epoch='urn:synthetic:epoch:b'))
         else:
-            s=scope('urn:synthetic:scope:dataset',source_kind='dataset-record');s['resource']='datasets';h.call('scope',s)
+            s=scope('urn:synthetic:scope:dataset',source_kind='dataset-record');s['resource']='datasets';s['scheme']='urn:synthetic:scheme:dataset-key';h.call('scope',s)
             h.call('policy',policy(2,(SCOPE,s['id'])));h.open_epoch('urn:synthetic:epoch:dataset',s['id'])
             h.mapping(value='d7',scope_id=s['id'],target='urn:synthetic:dataset:1',expected_kind='Dataset')
             for n,g in enumerate(('record-1','record-2',None)):
                 h.commit(h.batch('dataset-'+str(n),[item('d7',g)],'urn:synthetic:epoch:dataset',s['id']))
--- a/invariants.md
+++ b/invariants.md
@@ -3,9 +3,9 @@
 1. A source record is not a business subject; aboutness never creates or merges one.
 2. Qualified lineage preserves exact source/resource/scheme/key/generation; unknown generation is non-joinable.
 3. Source-instance generation, record generation and SyncEpoch are independent.
 4. Every mapping activation enforces one active claim per complete lineage/purpose.
-5. Changed anchors need a new mapping ID; corrects stays in the same scope/purpose/known lineage. Historical pins are bound by per-event state digests and exact code/schema build.
+5. Changed anchors need a new mapping ID; corrects stays in the same scope/purpose/known lineage. Historical pins are bound by per-event state digests and exact code/schema build. New pins never reuse another acquisition scope. Global lineage reservations require explicit dual-scope stewardship for moves.
 6. Current authentication/authorization precedes receipt lookup; full archives stay privileged. Occurrence corrections require intake/map/read and cannot probe another scope or purpose. Coverage attestation needs its separate grant.
 7. Batch identity is scope/epoch-wide, not actor-scoped; exact own retry requires current intake rights.
 8. Content identity excludes attempt/head/fence/computed pins; ordered input descriptors remain exact.
 9. One local transaction retains receipt, occurrences, quarantine and head; conservation always holds.
--- a/lifecycle/transitions.md
+++ b/lifecycle/transitions.md
@@ -1,9 +1,9 @@
 # Guarded lifecycle
 
 Mapping: proposed -> active/disputed/retracted; active -> disputed/retracted; disputed -> active/retracted; retracted terminal. Activation checks catalogue/pair, uniqueness and corrected-predecessor retirement. Changed immutable anchors need a new ID. Correction predecessors share scope/purpose/known lineage. Any current map grantee can transition; the issuer remains immutable. Validity-window misses also suspend new pins.
 
-Epoch: new -> open -> closed; one open per scope. Open starts fence 1/head null/progress 0. Admin advances fence; admitted first batches advance progress/head atomically. All rounds must be sealed before close. Admin must explicitly grant intake to an operator to seal an orphaned round with error evidence; reserve budget for closure. Closed epoch permits no commit even for an old key; current authorized read is separate.
+Epoch: new -> open -> closed; one open per scope. Open starts fence 1/head null/progress 0. Admin advances fence; admitted first batches advance progress/head atomically. All rounds must be sealed before close. Admin must explicitly grant intake to an operator to seal an orphaned round with nonempty error evidence; that close cannot prove completeness. Successful attested closure requires current attest-coverage. Reserve budget for closure. Closed epoch permits no commit even for an old key; current authorized read is separate.
 
-Round: opened -> pages in contiguous order -> sealed once. Terminal stops later pages. Incomplete/errored rounds can be sealed without completeness. Snapshot assessment never changes mappings or subjects.
+Round: opened -> pages in contiguous order -> sealed once. Attested rounds require current attest-coverage on open, new terminal-page admission and error-free seal; revocation is rechecked. Nonterminal intake and explicit errored incomplete seal need intake only. Terminal stops later pages. Incomplete/errored rounds can be sealed without completeness. Snapshot assessment never changes mappings or subjects.
 
-Batch: new admitted key -> immutable committed receipt; exact own retry returns prior acknowledgement without an event. Changed content, principal collision and stale new-admission preconditions may retain a compact restricted conflict observation, not the rejected full command. Limits are 128 total and 8 per actor/scope/epoch; exhausted diagnostic/event/byte capacity yields the same refusal without an event. Internal conflict observations cannot be submitted as client commands. Unauthorized/invalid calls and exact-retry telemetry are external. Quarantine stays open; resolution is deferred.
+Batch: new admitted key -> immutable committed receipt; exact own retry returns prior acknowledgement without an event. Changed content, principal collision and stale new-admission preconditions may retain a compact restricted conflict observation, not the rejected full command. Limits are 32 total and 4 per actor/scope/epoch; exhausted diagnostic/event/byte capacity yields the same refusal without an event. Internal conflict observations cannot be submitted as client commands. Unauthorized/invalid calls and exact-retry telemetry are external. Quarantine stays open; resolution is deferred.
--- a/migration.md
+++ b/migration.md
@@ -1,7 +1,7 @@
 # Migration and recovery
 
 This release introduces an original companion, not a subtype or replacement of a World Model. Existing source keys need explicit qualification and continuity evidence; unmatched kinds/unknown generations cannot be silently coerced. Export source descriptions and review mappings before acquisition.
 
-There is no writable archive migration. inspect_import accepts an exact supported archive only as historical evidence and emits a structured LossReport on unsupported/inconsistent input. No lossy conversion, token resume or origin-host takeover is attempted. A new host needs a new local register/epoch and verified fresh baseline. A normal process restart can reopen the current locally owned database after host continuity verification. Old/cloned databases cannot be detected internally. Bootstrap, archive and native snapshots pin exact source/schema build bytes; other candidate builds, even with the same unreleased version label, are refused. Keep old code/schema for historical inspection. Runtime and dependency pins are separate. No automatic candidate-build migration occurs.
+There is no writable archive migration. inspect_import accepts an exact supported archive only as historical evidence and emits a structured LossReport on unsupported/inconsistent input. No lossy conversion, token resume or origin-host takeover is attempted. A new host needs a new local register/epoch and verified fresh baseline. A normal process restart can reopen the current locally owned database after host continuity verification. Old/cloned databases cannot be detected internally. Bootstrap, archive and native snapshots pin exact source/schema build bytes; other candidate builds, even with the same unreleased version label, are refused. Keep old code/schema for historical inspection. Tested runtime/dependency versions are recorded; only jsonschema is pinned in requirements.txt, not the entire execution environment. No automatic candidate-build migration occurs.
 
 Future schema/algorithm changes require new pinned versions and separately reviewed migrations preserving lexical keys, generations, purpose, mapping revisions/pins, accepted and quarantine ordinals, grants/catalogue chronology and receipt/head history. Removing a native projection does not undo a commit. Database rollback is not a semantic correction; retain evidence and reconcile externally.
--- a/model-spec.md
+++ b/model-spec.md
@@ -19,23 +19,23 @@
 RecordSubjectMapping has immutable ID, complete known lineage, target subject/kind, purpose, issuer, validity interval, evidence and optional correction predecessor. The creating actor must be the issuer. Mapping admission requires a trusted target catalogue match and an allowed (sourceKind, targetKind, purpose) pair; arbitrary kinds are governed values rather than Identity's four-kind enum. Source kind comes from the trusted scope interpretation. A proposed mapping can activate, dispute or retract; active can dispute/retract; disputed can activate/retract; retraction is terminal. Every activation checks uniqueness across all mapping IDs and revisions for complete lineage plus purpose.
 
 Changing a target, key, generation, purpose, kind or issuer requires a new mapping ID. A replacement that declares corrects must name an earlier claim in the same scope, purpose and known lineage, and cannot activate until that predecessor is retracted. A different-key claim needs independent retirement and new admission without a misleading correction edge. Any current map grantee for the claim scope/purpose may transition it; issuer attribution remains immutable. A zero-active interval is allowed. The first release exposes separate guarded transitions, not an atomic replace convenience API. At no point can two claims for one lineage/purpose be active. Renames of source content do not edit the mapping.
 
-At first batch admission, each record gets a derived mapping outcome. A pin names mapping ID/state revision, target catalogue revision and current policy revision. The mapping validity window is checked against connector-declared observedAt. The state revision is selected at receipt time, not reconstructed from sourceEventTime. A later retraction or correction does not repin historical occurrences. A catalogue reclassification, changed source-kind interpretation or observedAt outside the mapping validity window suspends new pins with active-pin-suspended, while the old active claim still reserves uniqueness until steward action. Unknowns yield continuity-unknown; known lineages without an active claim yield unmapped. Disputed claims confer no operative pin.
+At first batch admission, each record gets a derived mapping outcome. A pin can use only a mapping declared in that same acquisition scope and purpose. Another scope with the same qualified lineage does not inherit its mapping, even if only the filter changed; its outcome is unmapped. Global lineage/purpose uniqueness still reserves an active claim across scopes. To move governance, a steward with current map grants for both scopes explicitly retracts the old claim and activates a separately proposed new one. Cross-scope corrects is refused; host evidence records the migration instead. Historical pins are unchanged. A pin names mapping ID/state revision, target catalogue revision and current policy revision. The mapping validity window is checked against connector-declared observedAt. The state revision is selected at receipt time, not reconstructed from sourceEventTime. A later retraction or correction does not repin historical occurrences. A catalogue reclassification, changed source-kind interpretation or observedAt outside the mapping validity window suspends new pins with active-pin-suspended, while the old active claim still reserves uniqueness until steward action. Unknowns yield continuity-unknown; known lineages without an active claim yield unmapped. Disputed claims confer no operative pin.
 
 This is a narrow combination of fixed mapping validity and append-only receipt knowledge. It is not a universal bitemporal mapping engine: future-effective state transitions, assignment closure revisions, retroactive repinning and historical reprocessing are deferred. historical_cut reports the journal known by a host receipt timestamp; within one second sequence remains the ordering key.
 
 ## Permission and host trust
 
-Bootstrap administration can declare sources/scopes, replace versioned host catalogue/policy, open/close epochs and advance fences. It does not automatically receive intake, mapping or ordinary receipt-read permission. A current exact Grant binds actor, scope, purpose, a subset of intake/map/read/attest-coverage, and a half-open validity interval. No wildcard, group inheritance, delegation chain or real IAM integration ships. Authentication, source/steward verification, policy-issuer competence and current time are trusted host inputs. A grant and a source's semantic priority remain distinct.
+Bootstrap administration can declare sources/scopes, replace versioned host catalogue/policy, open/close epochs and advance fences. It does not automatically receive intake, mapping or ordinary receipt-read permission. Mapping/round identifiers are register-global, not secret per-scope namespaces. A foreign scope/purpose ID collision and a foreign active-lineage reservation produce uniform DENIED without diagnostic detail. They can still reveal that an identifier or lineage is unavailable compared with a fresh successful proposal. Hosts allocate collision-resistant IDs and coordinate namespace stewardship. Receipt IDs expose register-wide sequence/activity; no concealment guarantee is made. There is no ordinary API for head/fence discovery: a trusted coordinator supplies current preconditions across purposes in a shared epoch. A current exact Grant binds actor, scope, purpose, a subset of intake/map/read/attest-coverage, and a half-open validity interval. No wildcard, group inheritance, delegation chain or real IAM integration ships. Authentication, source/steward verification, policy-issuer competence and current time are trusted host inputs. A grant and a source's semantic priority remain distinct.
 
 Unauthorized/revoked calls return the same not-accepted shap
END R4 INPUT PART 3/8 â€” SYNC-R4-PART-03
