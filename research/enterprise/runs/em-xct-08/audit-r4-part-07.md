R4 DELTA INPUT PART 7/8. Continue retaining the exact R3 baseline plus these patches. No tools or audit yet. A file/diff may span parts. ACK only this part number and its end marker.

 authorization refusals. Large-scale indexing/partitioning needs a separately reviewed implementation.\n\nCanonical encoding uses Python sorted-key, compact, UTF-8 JSON with ordered arrays; floats, duplicate JSON keys, non-string keys, C0/DEL/C1 control characters and unpaired surrogates are refused. JSON text bytes must be UTF-8 without BOM. Raw transport has a separate 8 MiB UTF-8 byte limit, including whitespace and escape spelling; the parsed canonical value remains limited to 512 KiB. Whitespace and key order within that transport budget are accepted and canonicalized. Excessive JSON nesting returns a structured import refusal; no unbounded parser support is promised. Stored journal/bootstrap blobs must already use exact canonical encoding. All lexical schema patterns require absolute end of string, so a trailing newline cannot pass. Other Unicode characters, including format/zero-width characters, remain distinct lexical values; viewers must escape ambiguous display safely. It is explicitly not RFC 8785/JCS. IDs are restricted URNs, lexical source keys remain exact bounded strings. Supplied SHA-256 values are declarations; no payload is fetched to confirm them. Schema version, object revision, journal sequence, epoch and source/record generation are independent values.\n\n## Native binding and release posture\n\nThe native V3 binding is one SyncRegister object and a restricted sync.register.snapshot fact pointing to this exact companion/version and carrying its closed journal snapshot. The snapshot omits redundant derived state; installed replay reconstructs the exact complete archive. sync.schema.json closes this native value at the root, with command and journal definitions in $defs. The native fact profile rejects extra envelope fields and requires exact authority types. One aggregate projection has an explicit owner, boundary and calculation rule. Its fact ID is determined by journal root; exporting the same cut at a later capture time can change envelope bytes but cannot create a new fact identity. Keep the first stored fact; the native writer rejects duplicate IDs. Only strict journal extensions supersede a trusted predecessor. That predecessor must already have been validated by the host, including its provenance. Generic business fact resolution must not treat this register snapshot as a Project field. Native outer validation and installed companion replay must both run; outer validity alone does not establish nested semantics, authenticity or current state.\n\nThis file currently describes an implementation candidate. Executed test reports and native acceptance state what was run. Separate frozen Claude/Grok audits are tracked in review.json and review.md; this candidate text alone makes no audit-acceptance claim. Published lifecycle, research assurance, implementation evidence and broader-contour completion remain separate. A source synchronization package is not a Company model or a production connector deployment.\n\n## Deterministic availability evidence\n\nAbsence assessment uses only availability occurrences from the compared scope and purpose. When multiple observations concern one lineage between the seals, the latest is selected by (receipt sequence, input ordinal), never dictionary or lexical key order. Canonical JSON export/import therefore preserves this result. Source-event clocks are not used to reorder host-admitted observations.\n"
   },
   "structure": {
     "bundles": [
       {
--- a/sync.schema.json
+++ b/sync.schema.json
@@ -1441,9 +1441,9 @@
       "$ref": "#/$defs/Bootstrap"
     },
     "events": {
       "type": "array",
-      "maxItems": 2000,
+      "maxItems": 128,
       "items": {
         "$ref": "#/$defs/JournalEvent"
       }
     },
--- a/sync_register.py
+++ b/sync_register.py
@@ -10,15 +10,18 @@
 from jsonschema import Draft202012Validator
 from jsonschema.exceptions import ValidationError
 
 VERSION='0.1.0'
-MAX_EVENTS=2000
-MAX_BYTES=8*1024*1024
-MAX_CONFLICTS=128
-MAX_CONFLICTS_PER_WRITER_SCOPE_EPOCH=8
+MAX_EVENTS=128
+MAX_BYTES=512*1024
+MAX_TRANSPORT_BYTES=8*1024*1024
+MAX_CONFLICTS=32
+MAX_CONFLICTS_PER_WRITER_SCOPE_EPOCH=4
 SCHEMA=json.loads((Path(__file__).with_name('sync.schema.json')).read_text(encoding='utf-8'))
 BUILD_ID='sha256:'+hashlib.sha256(Path(__file__).read_bytes()+b'\0'+Path(__file__).with_name('sync.schema.json').read_bytes()).hexdigest()
 DENIED={'status':'not-accepted'}
+SURROGATE=re.compile('[\ud800-\udfff]')
+CONTROL=re.compile('[\x00-\x1f\x7f-\x9f]')
 
 class Invalid(ValueError): pass
 def require(ok,message):
     if not ok:raise Invalid(message)
@@ -31,25 +34,28 @@
         elif type(x)==list:
             for v in x:walk(v)
         elif type(x)==int:require(abs(x)<=1000000,'integer bound')
         elif type(x)==str:
-            require(not any(0xd800<=ord(c)<=0xdfff for c in x),'surrogate')
-            require(not any(ord(c)<32 or 0x7f<=ord(c)<=0x9f for c in x),'control character')
-    walk(value)
+            require(SURROGATE.search(x) is None,'surrogate')
+            require(CONTROL.search(x) is None,'control character')
+    try:walk(value)
+    except RecursionError as error:raise Invalid('nesting too deep') from error
     raw=json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')
     require(len(raw)<=MAX_BYTES,'byte budget')
     return raw
 def digest(value):return 'sha256:'+hashlib.sha256(encode(value)).hexdigest()
 def decode(raw):
-    require(len(raw)<=MAX_BYTES,'byte budget')
+    require(type(raw) in (bytes,str),'JSON bytes or text required')
+    require(len(raw if type(raw)==bytes else raw.encode('utf-8'))<=MAX_TRANSPORT_BYTES,'transport byte budget')
     if type(raw)==bytes:raw=raw.decode('utf-8',errors='strict')
     require(type(raw)==str and not raw.startswith('\ufeff'),'UTF-8 without BOM required')
     def pairs(items):
         out={}
         for k,v in items:require(k not in out,'duplicate JSON key');out[k]=v
         return out
-    value=json.loads(raw,object_pairs_hook=pairs,parse_float=lambda _:(_ for _ in ()).throw(Invalid('float')),
-                     parse_constant=lambda _:(_ for _ in ()).throw(Invalid('constant')))
+    try:value=json.loads(raw,object_pairs_hook=pairs,parse_float=lambda _:(_ for _ in ()).throw(Invalid('float')),
+                         parse_constant=lambda _:(_ for _ in ()).throw(Invalid('constant')))
+    except RecursionError as error:raise Invalid('nesting too deep') from error
     encode(value)
     return value
 def validate(name,value):
     encode(value)
@@ -89,9 +95,9 @@
     return c is not None and any(x['id']==mapping['targetId'] and x['kind']==mapping['expectedTargetKind'] for x in c['subjects']) and {'sourceKind':scope['sourceObjectKind'],'targetKind':mapping['expectedTargetKind'],'purpose':mapping['purpose']} in c['pairs']
 def mapping_outcome(state,scope_id,item,purpose):
     lin=lineage(state,scope_id,item['key'])
     if lin is None:return {'status':'continuity-unknown','pin':None}
-    matches=[h[-1] for h in state['mappings'].values() if h[-1]['lineage']==lin and h[-1]['definition']['purpose']==purpose and h[-1]['state']=='active']
+    matches=[h[-1] for h in state['mappings'].values() if h[-1]['lineage']==lin and h[-1]['definition']['scopeId']==scope_id and h[-1]['definition']['purpose']==purpose and h[-1]['state']=='active']
     require(len(matches)<=1,'ambiguous active mappings')
     if not matches:return {'status':'unmapped','pin':None}
     m=matches[0];definition=m['definition']
     if state['scopes'][scope_id]['sourceObjectKind']!=state['scopes'][definition['scopeId']]['sourceObjectKind'] or not eligible_mapping(state,definition) or not within(item['observedAt'],definition['validFrom'],definition['validTo']):
@@ -152,8 +158,10 @@
             for g in body['grants']:require(time(g['validFrom'])<time(g['validTo']),'grant window')
         else:require(len({s['id'] for s in body['subjects']})==len(body['subjects']),'duplicate target')
         state[op]=deepcopy(body)
     elif op=='mapping':
+        existing=state['mappings'].get(body['id'])
+        if existing and (existing[-1]['definition']['scopeId'],existing[-1]['definition']['purpose'])!=(body['scopeId'],body['purpose']):return deepcopy(DENIED),False
         require(body['id'] not in state['mappings'] and body['scopeId'] in state['scopes'],'mapping identity')
         incoming_key(state,body['scopeId'],body['key'],actor,body['purpose'],now)
         require(body['issuer']==actor,'mapping issuer must be authenticated steward')
         require(body['key']['generation'] is not None,'unknown generation cannot map')
@@ -169,8 +177,9 @@
         transitions={'proposed':{'active','disputed','retracted'},'active':{'disputed','retracted'},'disputed':{'active','retracted'},'retracted':set()}
         require(body['to'] in transitions[old['state']],'mapping transition')
         if body['to']=='active':
             require(eligible_mapping(state,old['definition']),'target kind or aboutness policy')
+            if any(x[-1]['state']=='active' and x[-1]['lineage']==old['lineage'] and x[-1]['definition']['purpose']==old['definition']['purpose'] and x[-1]['definition']['scopeId']!=old['definition']['scopeId'] for x in state['mappings'].values()):return deepcopy(DENIED),False
             require(not any(x[-1]['state']=='active' and x[-1]['lineage']==old['lineage'] and x[-1]['definition']['purpose']==old['definition']['purpose'] for mid,x in state['mappings'].items() if mid!=body['id']),'active mapping already exists')
             previous=old['definition']['corrects']
             require(previous is None or state['mappings'][previous][-1]['state']=='retracted','corrected claim not retracted')
         h.append({**deepcopy(old),'revision':old['revision']+1,'state':body['to'],'recordedAt':now,'sequence':seq,'actor':actor,'reason':body['reason'],'catalogueRevision':state['catalogue']['revision']})
@@ -185,16 +194,20 @@
             require(not any(r['definition']['epochId']==body['id'] and not r['sealed'] for r in state['rounds'].values()),'seal open rounds, including partial evidence, before epoch close')
             e.update(status='closed',closedAt=now,closedSequence=seq,closeReason=body['reason'])
     elif op=='round-open':
         if (body['consistency']=='source-snapshot' or body['visibilityCovered']) and not permitted(state,actor,body['scopeId'],body['purpose'],'attest-coverage',now):return deepcopy(DENIED),False
+        existing=state['rounds'].get(body['id'])
+        if existing and (existing['definition']['scopeId'],existing['definition']['purpose'])!=(body['scopeId'],body['purpose']):return deepcopy(DENIED),False
         require(body['id'] not in state['rounds'],'round exists')
         e=state['epochs'].get(body['epochId']);require(e is not None and e['status']=='open' and e['scopeId']==body['scopeId'],'round epoch')
         require((body['previousRoundId'] is None)==(body['notEarlierEvidence'] is None),'round order evidence')
         if body['previousRoundId'] is not None:
             old=state['rounds'].get(body['previousRoundId']);require(old is not None and old['sealed'] and old['definition']['scopeId']==body['scopeId'],'round predecessor')
         state['rounds'][body['id']]={'definition':deepcopy(body),'pages':[],'sealed':False,'errors':[],'openedSequence':seq,'sealedSequence':None,'complete':False}
     elif op=='round-seal':
         r=state['rounds'][body['id']];require(not r['sealed'],'round already sealed')
+        d=r['definition']
+        if not body['errors'] and (d['consistency']=='source-snapshot' or d['visibilityCovered']) and not permitted(state,actor,d['scopeId'],d['purpose'],'attest-coverage',now):return deepcopy(DENIED),False
         pages=[state['batches'][p] for p in r['pages']]
         r.update(sealed=True,errors=deepcopy(body['errors']),sealedSequence=seq)
         r['complete']=bool(pages and pages[-1]['content']['terminal'] and not body['errors'] and all(not b['quarantine'] and all(o['key']['generation'] is not None and o['operation']=='snapshot-read' for o in b['occurrences']) for b in pages))
     elif op=='commit':
@@ -214,8 +227,9 @@
         if c['roundId'] is None:require(c['pageIndex'] is None and not c['terminal'],'round/page mismatch')
         else:
             r=state['rounds'].get(c['roundId']);require(r is not None and not r['sealed'],'round not open')
             d=r['definition'];require((d['scopeId'],d['epochId'],d['purpose'])==(c['scopeId'],c['epochId'],c['purpose']),'round context')
+            if c['terminal'] and (d['consistency']=='source-snapshot' or d['visibilityCovered']) and not permitted(state,actor,c['scopeId'],c['purpose'],'attest-coverage',now):return deepcopy(DENIED),False
             require(c['pageIndex']==len(r['pages']),'page chain gap')
             require(not r['pages'] or not state['batches'][r['pages'][-1]]['content']['terminal'],'page after terminal')
         rid=event_id(state,seq,'receipt');occ=[];quarantine=[]
         for ordinal,item in enumerate(c['items']):
@@ -261,8 +275,9 @@
         if config is not None:
             initial(config)
             with self.path.open('xb'):pass
         require(config is not None or self.path.is_file(),'explicit bootstrap required')
+        require(config is not None or self.path.stat().st_size>0,'uninitialized store; preserve and inspect, or bootstrap a different path')
         self.db=sqlite3.connect(str(self.path),timeout=10,isolation_level=None)
         self.db.execute('PRAGMA journal_mode=DELETE');self.db.execute('PRAGMA synchronous=FULL')
         if config is not None:
             try:
@@ -347,10 +362,12 @@
     def observed(r):return {digest(o['lineage']):o for slot in r['pages'] for o in s['batches'][slot]['occurrences']}
     old,new=observed(a),observed(b);candidates=[];explicit=[]
     for key,o in old.items():
         if key in new:continue
-        unavailable=[p for receipt in s['batches'].values() if receipt['content']['scopeId']==x['scopeId'] and a['sealedSequence']<receipt['sequence']<=b['sealedSequence'] for p in receipt['occurrences'] if p['lineage']==o['lineage'] and p['operation'] in ('source-deleted','removed-from-scope','inaccessible')]
-        if unavailable:explicit.append({'lineage':o['lineage'],'operation':unavailable[-1]['operation'],'evidenceOccurrence':unavailable[-1]['id']})
+        unavailable=[p for receipt in s['batches'].values() if receipt['content']['scopeId']==x['scopeId'] and receipt['content']['purpose']==x['purpose'] and a['sealedSequence']<receipt['sequence']<=b['sealedSequence'] for p in receipt['occurrences'] if p['lineage']==o['lineage'] and p['operation'] in ('source-deleted','removed-from-scope','inaccessible')]
+        if unavailable:
+            latest=max(unavailable,key=lambda p:(p['sequence'],p['ordinal']))
+            explicit.append({'lineage':o['lineage'],'operation':latest['operation'],'evidenceOccurrence':latest['id']})
         else:candidates.append({'conclusion':'not-observed-in-comparable-rounds','lineage':o['lineage'],'earlierRound':earlier,'laterRound':later,'permittedAction':'steward-review-only'})
     return {'status':'assessed','candidates':candidates,'explicitAvailabilityEvidence':explicit,'effects':[]}
 
 def resume_archive(_):raise Invalid('Archive resume refused; new local acquisition baseline required')
--- a/test-results.json
+++ b/test-results.json
@@ -1,29 +1,36 @@
 {
   "format": "vercy-source-sync-tests",
-  "executedAt": "2026-09-22T10:26:59.569264+00:00",
+  "executedAt": "2026-09-22T11:06:29.840671+00:00",
   "passed": true,
-  "testsRun": 81,
+  "testsRun": 98,
   "failures": 0,
   "errors": 0,
   "tests": [
     "test_sync.SyncTests.test_admin_can_explicitly_grant_intake_to_close_orphan_round",
     "test_sync.SyncTests.test_admin_has_no_implicit_intake_mapping_or_read",
     "test_sync.SyncTests.test_archive_roundtrip_is_nonresumable",
     "test_sync.SyncTests.test_archive_tamper_rejected",
+    "test_sync.SyncTests.test_attested_multi_page_intake_then_authorized_completion",
+    "test_sync.SyncTests.test_availability_from_other_purpose_does_not_suppress_absence",
+    "test_sync.SyncTests.test_availability_selection_is_roundtrip_stable_and_ordinal_ordered",
     "test_sync.SyncTests.test_best_effort_or_visibility_unknown_refuses_absence",
     "test_sync.SyncTests.test_changed_body_conflicts_without_overwrite",
     "test_sync.SyncTests.test_changed_build_refuses_store_archive_and_native",
     "test_sync.SyncTests.test_changed_reducer_outcome_rejected",
     "test_sync.SyncTests.test_closed_epoch_commit_refused_read_allowed",
     "test_sync.SyncTests.test_complete_archive_byte_budget_is_atomic",
     "test_sync.SyncTests.test_conflict_at_event_limit_is_uniform_no_event",
+    "test_sync.SyncTests.test_conflict_reason_tamper_fails_even_with_outer_digest_rewritten",
     "test_sync.SyncTests.test_conflicts_are_compact_bounded_and_do_not_advance_head",
     "test_sync.SyncTests.test_correction_cannot_probe_foreign_scope_or_missing_target",
     "test_sync.SyncTests.test_correction_requires_current_read_and_map",
     "test_sync.SyncTests.test_correction_retains_known_history_no_invented_time",
     "test_sync.SyncTests.test_correction_wrong_lineage_refused",
     "test_sync.SyncTests.test_coverage_attestation_needs_separate_grant",
+    "test_sync.SyncTests.test_cross_purpose_batch_collision_keeps_read_isolation",
+    "test_sync.SyncTests.test_cross_scope_pin_requires_explicit_stewardship_move",
+    "test_sync.SyncTests.test_deep_import_is_structured_loss_report",
     "test_sync.SyncTests.test_denied_at_event_budget_is_uniform",
     "test_sync.SyncTests.test_derived_state_bool_int_substitution_rejected",
     "test_sync.SyncTests.test_different_writer_no_duplicate_no_receipt",
     "test_sync.SyncTests.test_duplicate_declarations_and_configuration_revisions",
@@ -37,12 +44,16 @@
     "test_sync.SyncTests.test_expired_grant_and_wrong_purpose_do_not_replay",
     "test_sync.SyncTests.test_explicit_deletion_reported_separately",
     "test_sync.SyncTests.test_failed_round_does_not_prove_absence",
     "test_sync.SyncTests.test_foreign_evidence_namespace_refused",
+    "test_sync.SyncTests.test_foreign_mapping_and_round_id_collision_is_uniform_refusal",
     "test_sync.SyncTests.test_generation_attribution_wrong_source_rejected",
     "test_sync.SyncTests.test_global_conflict_budget_is_shared_across_writers",
+    "test_sync.SyncTests.test_grant_exclusive_end_and_invalid_month",
     "test_sync.SyncTests.test_in_place_retarget_rejected",
+    "test_sync.SyncTests.test_intake_only_cannot_complete_attested_snapshot",
     "test_sync.SyncTests.test_internal_conflict_command_cannot_be_injected",
+    "test_sync.SyncTests.test_interrupted_empty_bootstrap_is_preserved_and_not_resumed",
     "test_sync.SyncTests.test_invalid_calendar_timestamp_is_invalid_and_atomic",
     "test_sync.SyncTests.test_lossy_import_reports_refusal",
     "test_sync.SyncTests.test_malformed_authorization_inputs_are_uniform",
     "test_sync.SyncTests.test_mapping_correction_cannot_probe_foreign_purpose",
@@ -55,8 +66,9 @@
     "test_sync.SyncTests.test_opaque_tokens_are_not_sorted",
     "test_sync.SyncTests.test_outcome_digest_cannot_be_rewritten_with_outer_hash",
     "test_sync.SyncTests.test_oversized_register_id_rejected_before_store_creation",
     "test_sync.SyncTests.test_partial_page_progress_is_not_round_completeness",
+    "test_sync.SyncTests.test_pretty_and_ascii_escaped_transport_at_canonical_budget",
     "test_sync.SyncTests.test_process_crash_after_commit_lost_response",
     "test_sync.SyncTests.test_process_crash_before_commit",
     "test_sync.SyncTests.test_prohibited_controls_in_key_actor_digest_and_bootstrap",
     "test_sync.SyncTests.test_quarantine_blocks_round_absence",
@@ -65,18 +77,22 @@
     "test_sync.SyncTests.test_reactivation_enforces_unique_active",
     "test_sync.SyncTests.test_recycled_and_unknown_keys_not_mapped",
     "test_sync.SyncTests.test_reference_rewrapping_is_changed_body",
     "test_sync.SyncTests.test_retry_after_mapping_change_and_progress_retains_pin",
+    "test_sync.SyncTests.test_revoked_attester_cannot_terminally_commit_or_successfully_seal",
     "test_sync.SyncTests.test_revoked_writer_cannot_probe_receipts",
     "test_sync.SyncTests.test_round_terminal_seal_and_epoch_close_guards",
     "test_sync.SyncTests.test_round_unknown_order_refuses_absence",
     "test_sync.SyncTests.test_same_lineage_can_have_separate_purpose_mappings",
+    "test_sync.SyncTests.test_schema_generator_preserves_exact_shipped_bytes",
     "test_sync.SyncTests.test_schema_itself_rejects_trailing_linefeed",
+    "test_sync.SyncTests.test_schema_legal_slash_register_cannot_export_native",
     "test_sync.SyncTests.test_scope_change_breaks_round_comparison",
     "test_sync.SyncTests.test_source_asserted_correction_with_scoped_authority",
     "test_sync.SyncTests.test_source_delete_has_no_subject_effect",
     "test_sync.SyncTests.test_source_generation_change_requires_new_mapping",
     "test_sync.SyncTests.test_source_kind_change_cannot_reuse_mapping",
+    "test_sync.SyncTests.test_source_nonreuse_and_steward_correction_spoof",
     "test_sync.SyncTests.test_stale_fence_and_head",
     "test_sync.SyncTests.test_steward_generation_positive",
     "test_sync.SyncTests.test_steward_generation_requires_mapping_right",
     "test_sync.SyncTests.test_target_reclassification_suspends_new_pins",
@@ -84,19 +100,20 @@
     "test_sync.SyncTests.test_two_boards_one_project_rename",
     "test_sync.SyncTests.test_two_complete_rounds_propose_only",
     "test_sync.SyncTests.test_two_processes_one_progress_edge",
     "test_sync.SyncTests.test_unsupported_partitioned_scope_refused",
+    "test_sync.SyncTests.test_visibility_attestation_gate_applies_to_best_effort_too",
     "test_sync.SyncTests.test_visibility_uncertainty_blocks_absence",
     "test_sync.SyncTests.test_wrong_target_kind_rejected"
   ],
   "python": "3.12.14",
   "sqlite": "3.53.1",
   "sourceDigests": {
     "run_tests.py": "d74e5e8ae1dbc3b52925b5525dd27ad106a365dc625bf3a4bc6fc1d858449452",
-    "test_sync.py": "de93ce176ecf7478c3b400d280a1bf845e99efd5abb2fd4c7a1ad72c44ab43ad",
+    "test_sync.py": "6c8ddb318182d4d96e94bd98c30f7bf9fd244e2e80300738372d74bd597f7e8c",
     "fault_worker.py": "a3c487b078297d9bc45fcb804d22aac6f8ac1f7d2bd8eac41b841eb2f1bd75d7",
-    "fixtures.py": "b9db73bb431b78ad2aa1fc547aafe5d8915adb80132bf510ceb58440b9a2e70b",
-    "sync_register.py": "0a1a2c6ed493ca9353897ea1954d60f37bd5f35144d654a6bb078f50b024600a",
-    "sync.schema.json": "f03e3ec18a65694d9a815b68d2f2be2ba9b72a5b3f8238252347c3a7f0343a88"
+    "fixtures.py": "d3d3ff6d43ab5bb42124c31ec72da1e45397ccc5243aaa8eb267545f4f11fe37",
+    "sync_register.py": "a76275570093cc09a9de84924c95ee5e8f6532c30eec8d08d6e8fc3ef59aceba",
+    "sync.schema.json": "9a5ba286ce93ca216f496d470e50047366c1b8026d46cb96838fdaa63efa3e63"
   },
   "limits": "Synthetic local reference. Two real subprocess crash cuts and a two-process writer race; no hardware/power-loss, remote connector or production-scale certification."
 }
--- a/test_sync.py
+++ b/test_sync.py
@@ -9,8 +9,111 @@
 class SyncTests(unittest.TestCase):
     def setUp(self):
         self.tmp=tempfile.TemporaryDirectory(prefix='sync-test-');self.root=Path(self.tmp.name);self.h=Harness(self.root/'state.sqlite')
     def tearDown(self):self.h.close();self.tmp.cleanup()
+    def _open_attested(self,rid,previous=None,consistency='source-snapshot'):
+        body={'id':rid,'scopeId':SCOPE,'epochId':EPOCH,'purpose':PURPOSE,'consistency':consistency,'consistencyEvidence':evidence('snapshot'),'visibilityCovered':True,'previousRoundId':previous,'notEarlierEvidence':evidence('order') if previous else None}
+        self.h.call('round-open',body);return body
+    def _add_purpose(self,purpose):
+        pol=policy(self.h.state()['policy']['revision']+1)
+        for g in deepcopy(pol['gra
END R4 INPUT PART 7/8 â€” SYNC-R4-PART-07
