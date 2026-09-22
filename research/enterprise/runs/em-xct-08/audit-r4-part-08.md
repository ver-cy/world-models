R4 DELTA INPUT PART 8/8. Continue retaining the exact R3 baseline plus these patches. No tools or audit yet. A file/diff may span parts. ACK only this part number and its end marker.

nts']):g['purpose']=purpose;pol['grants'].append(g)
+        self.h.call('policy',pol)
+    def test_intake_only_cannot_complete_attested_snapshot(self):
+        r1='urn:synthetic:round:base';r2='urn:synthetic:round:current';self.h.round(r1,['a','b']);self._open_attested(r2,r1)
+        a=self.h.archive();self.assertEqual(self.h.commit(self.h.batch('empty',[],round_id=r2,page=0,terminal=True),OTHER),DENIED)
+        self.assertEqual(self.h.call('round-seal',{'id':r2,'errors':[]},OTHER),DENIED);self.assertEqual(self.h.archive(),a)
+        self.assertEqual(assess_rounds(a,r1,r2)['status'],'insufficient-context')
+    def test_revoked_attester_cannot_terminally_commit_or_successfully_seal(self):
+        rid='urn:synthetic:round:revoke';self._open_attested(rid)
+        self.h.call('policy',policy(2,writer_rights=('intake','map','read')))
+        a=self.h.archive();b=self.h.batch('terminal',[],round_id=rid,page=0,terminal=True)
+        self.assertEqual(self.h.commit(b),DENIED);self.assertEqual(self.h.call('round-seal',{'id':rid,'errors':[]}),DENIED);self.assertEqual(self.h.archive(),a)
+        self.h.call('policy',policy(3));self.h.commit(b)
+        self.h.call('policy',policy(4,writer_rights=('intake','map','read')));a=self.h.archive()
+        self.assertEqual(self.h.call('round-seal',{'id':rid,'errors':[]}),DENIED);self.assertEqual(self.h.archive(),a)
+        self.h.call('round-seal',{'id':rid,'errors':[evidence('attestation-unavailable')]})
+        self.assertFalse(self.h.state()['rounds'][rid]['complete'])
+    def test_visibility_attestation_gate_applies_to_best_effort_too(self):
+        rid='urn:synthetic:round:visible';self._open_attested(rid,consistency='best-effort')
+        self.assertEqual(self.h.commit(self.h.batch('terminal',[],round_id=rid,page=0,terminal=True),OTHER),DENIED)
+        self.assertEqual(self.h.call('round-seal',{'id':rid,'errors':[]},OTHER),DENIED)
+    def test_attested_multi_page_intake_then_authorized_completion(self):
+        rid='urn:synthetic:round:multi';self._open_attested(rid)
+        self.h.commit(self.h.batch('p0',[item('a',operation='snapshot-read')],round_id=rid,page=0),OTHER)
+        self.h.commit(self.h.batch('p1',[item('b',operation='snapshot-read')],round_id=rid,page=1,terminal=True))
+        self.h.call('round-seal',{'id':rid,'errors':[]});self.assertTrue(self.h.state()['rounds'][rid]['complete'])
+    def test_availability_selection_is_roundtrip_stable_and_ordinal_ordered(self):
+        import sync_register as sr
+        r1='urn:synthetic:round:base';r2='urn:synthetic:round:current';self.h.round(r1,['a'])
+        keys=sorted(('candidate-'+str(i) for i in range(20)),key=lambda k:digest([SCOPE,EPOCH,k]),reverse=True)
+        self.h.commit(self.h.batch(keys[0],[item('a',operation='source-deleted')]))
+        self.h.commit(self.h.batch(keys[-1],[item('a',operation='removed-from-scope'),item('a',operation='inaccessible')]))
+        self.h.round(r2,[],r1);a=self.h.archive();before=assess_rounds(a,r1,r2);after=assess_rounds(decode(sr.encode(a)),r1,r2)
+        self.assertEqual(before,after);self.assertEqual(before['explicitAvailabilityEvidence'][0]['operation'],'inaccessible')
+    def test_availability_from_other_purpose_does_not_suppress_absence(self):
+        r1='urn:synthetic:round:base';r2='urn:synthetic:round:current';self.h.round(r1,['a']);self._add_purpose('other-purpose')
+        b=self.h.batch('foreign-purpose',[item('a',operation='source-deleted')]);b['content']['purpose']='other-purpose';self.h.commit(b)
+        self.h.round(r2,[],r1);result=assess_rounds(self.h.archive(),r1,r2)
+        self.assertEqual(len(result['candidates']),1);self.assertEqual(result['explicitAvailabilityEvidence'],[])
+    def test_foreign_mapping_and_round_id_collision_is_uniform_refusal(self):
+        other='urn:synthetic:scope:other';s=scope(other);s['filter']=evidence('another-filter');self.h.call('scope',s);self.h.call('policy',policy(2,(SCOPE,other)));self.h.open_epoch('urn:synthetic:epoch:other',other)
+        definition=self.h.mapping();rid='urn:synthetic:round:base';r=self._open_attested(rid)
+        definition['scopeId']=other;r.update(scopeId=other,epochId='urn:synthetic:epoch:other',consistency='best-effort',visibilityCovered=False)
+        a=self.h.archive();self.assertEqual(self.h.call('mapping',definition),DENIED);self.assertEqual(self.h.call('round-open',r),DENIED);self.assertEqual(self.h.archive(),a)
+    def test_cross_scope_pin_requires_explicit_stewardship_move(self):
+        self.h.mapping();other='urn:synthetic:scope:rotation';s=scope(other);s['filter']=evidence('rotated-filter');self.h.call('scope',s);self.h.call('policy',policy(2,(SCOPE,other)));self.h.open_epoch('urn:synthetic:epoch:rotation',other)
+        body=self.h.batch('before',[item()],epoch='urn:synthetic:epoch:rotation',scope_id=other);first=self.h.commit(body)
+        self.h.mapping('urn:synthetic:mapping:rotation',scope_id=other,activate=False)
+        self.assertEqual(self.h.transition('urn:synthetic:mapping:rotation','active'),DENIED)
+        self.h.transition('urn:synthetic:mapping:1','retracted');self.h.transition('urn:synthetic:mapping:rotation','active')
+        self.h.commit(self.h.batch('after',[item()],epoch='urn:synthetic:epoch:rotation',scope_id=other));batches=self.h.state()['batches'].values()
+        old=next(x for x in batches if x['id']==first['receiptId']);self.assertEqual(old['occurrences'][0]['mapping']['status'],'unmapped')
+        new=next(x for x in batches if x['content']['batchKey']=='after');self.assertEqual(new['occurrences'][0]['mapping']['pin']['mappingId'],'urn:synthetic:mapping:rotation')
+    def test_pretty_and_ascii_escaped_transport_at_canonical_budget(self):
+        from unittest.mock import patch
+        import sync_register as sr
+        rec=item();rec['key']['value']='工程'*50;self.h.commit(self.h.batch(items=[rec]));a=self.h.archive();canonical=sr.encode(a)
+        for raw in (json.dumps(a,indent=2,ensure_ascii=True).encode(),json.dumps(a,indent=2,ensure_ascii=False).encode()):
+            self.assertGreater(len(raw),len(canonical))
+            with patch.object(sr,'MAX_BYTES',len(canonical)):self.assertTrue(inspect_import(raw)['valid'])
+        with patch.object(sr,'MAX_TRANSPORT_BYTES',len(canonical)-1):self.assertFalse(inspect_import(canonical)['valid'])
+    def test_deep_import_is_structured_loss_report(self):
+        report=inspect_import(b'['*200000+b']'*200000)
+        self.assertEqual(report['status'],'refused');self.assertEqual(report['lossReport']['code'],'unsupported-or-inconsistent-archive')
+    def test_interrupted_empty_bootstrap_is_preserved_and_not_resumed(self):
+        import sync_register as sr
+        path=self.root/'interrupted.sqlite'
+        run=subprocess.run([sys.executable,'-c','from pathlib import Path; import os,sys; Path(sys.argv[1]).touch(exist_ok=False); os._exit(79)',str(path)])
+        self.assertEqual(run.returncode,79)
+        with self.assertRaises(Invalid):sr.Register(path)
+        with self.assertRaises(FileExistsError):sr.Register(path,self.h.archive()['config'])
+        self.assertEqual(path.read_bytes(),b'')
+    def test_cross_purpose_batch_collision_keeps_read_isolation(self):
+        self._add_purpose('other-purpose');b=self.h.batch();self.h.commit(b);b['content']['purpose']='other-purpose'
+        self.assertEqual(self.h.commit(b),DENIED)
+        self.assertEqual(self.h.reg.read_receipt(SCOPE,'other-purpose',EPOCH,'batch-1',WRITER,self.h.now()),{'status':'not-found'})
+    def test_conflict_reason_tamper_fails_even_with_outer_digest_rewritten(self):
+        b=self.h.batch();self.h.commit(b);b['content']['token']=evidence('different');self.h.commit(b);a=self.h.archive();e=a['events'][-1]
+        e['command']['body']['reason']='stale-head';e['digest']=digest({k:v for k,v in e.items() if k!='digest'});a['root']=e['digest']
+        with self.assertRaises(Invalid):validate_archive(a)
+    def test_schema_generator_preserves_exact_shipped_bytes(self):
+        import build_schema
+        raw=(json.dumps(build_schema.SCHEMA,ensure_ascii=False,indent=2)+'\n').encode()
+        self.assertEqual(raw,(HERE/'sync.schema.json').read_bytes())
+    def test_source_nonreuse_and_steward_correction_spoof(self):
+        rec=item();rec['key']['generationEvidence']['basis']='source-nonreuse-guarantee';self.h.commit(self.h.batch(items=[rec]))
+        oid=next(iter(self.h.state()['batches'].values()))['occurrences'][0]['id'];rec=item();rec['correction']={'occurrenceId':oid,'assertedBy':OTHER,'basis':'steward-asserted','evidence':evidence('spoof')}
+        with self.assertRaises(Invalid):self.h.commit(self.h.batch('spoof',[rec]))
+    def test_grant_exclusive_end_and_invalid_month(self):
+        b=self.h.batch();self.assertEqual(self.h.reg.execute({'op':'commit','body':b},WRITER,'2030-01-01T00:00:00Z'),DENIED)
+        b['content']['items'][0]['observedAt']='2026-13-01T00:00:00Z'
+        with self.assertRaises(Invalid):self.h.commit(b)
+    def test_schema_legal_slash_register_cannot_export_native(self):
+        import sync_register as sr
+        config=self.h.archive()['config'];config['registerId']='urn:synthetic:register/slash';r=sr.Register(self.root/'slash.sqlite',config)
+        try:
+            with self.assertRaises(Invalid):sr.native_records(r.archive(ADMIN),'2026-01-01T01:00:00Z')
+        finally:r.close()
     def test_global_conflict_budget_is_shared_across_writers(self):
         from unittest.mock import patch
         import sync_register as sr
         body=self.h.batch();self.h.commit(body);changed=deepcopy(body);changed['content']['token']=evidence('changed-token')
@@ -121,9 +224,9 @@
         self.assertEqual([x['mapping']['status'] for x in rows],['mapped','active-pin-suspended'])
     def test_source_kind_change_cannot_reuse_mapping(self):
         self.h.mapping();new=scope('urn:synthetic:scope:changed',source_kind='dataset-record');self.h.call('scope',new);self.h.call('policy',policy(2,(SCOPE,new['id'])));self.h.open_epoch('urn:synthetic:epoch:new',new['id'])
         self.h.commit(self.h.batch('changed-kind',epoch='urn:synthetic:epoch:new',scope_id=new['id']))
-        self.assertEqual(list(self.h.state()['batches'].values())[0]['occurrences'][0]['mapping']['status'],'active-pin-suspended')
+        self.assertEqual(list(self.h.state()['batches'].values())[0]['occurrences'][0]['mapping']['status'],'unmapped')
     def test_correction_retains_known_history_no_invented_time(self):
         self.h.commit(self.h.batch());old=list(self.h.state()['batches'].values())[0]['occurrences'][0];cut=self.h.archive()['events'][-1]['recordedAt']
         corrected=item();corrected['content']=evidence('corrected');corrected['correction']={'occurrenceId':old['id'],'assertedBy':WRITER,'basis':'steward-asserted','evidence':evidence('correction')}
         self.h.commit(self.h.batch('correction',[corrected]));archive=self.h.archive();self.assertEqual(len(historical_cut(archive,cut)['state']['batches']),1)
--- /dev/null
+++ b/benchmark-results.json
@@ -0,0 +1,30 @@
+{
+  "format": "vercy-source-sync-capacity-run",
+  "executedAt": "2026-09-22T11:08:46.140038+00:00",
+  "passed": true,
+  "buildId": "sha256:b782bbca6c4b5bcc9344dde998d88486c1635ce45a00fbcf6bb7bb179af25cd6",
+  "python": "3.12.14",
+  "sqlite": "3.53.1",
+  "eventLimit": 128,
+  "canonicalByteLimit": 524288,
+  "retainedEvents": 128,
+  "canonicalBytes": 517105,
+  "budgetFillFraction": 0.9863,
+  "bulkRecords": 124,
+  "setupSeconds": 101.974,
+  "lastSetupWriteSeconds": 1.386,
+  "maxSetupWriteSeconds": 1.621,
+  "archiveSeconds": 1.411,
+  "readReceiptSeconds": 1.374,
+  "twoProcessExactRetrySeconds": 3.914,
+  "writerTimeouts": 0,
+  "retryAtLimitSeconds": 1.435,
+  "sourceDigests": {
+    "benchmark.py": "29f5265ee55665bede2550a214e66fa61b78b0d070044ec90a34259d41fd4960",
+    "sync_register.py": "a76275570093cc09a9de84924c95ee5e8f6532c30eec8d08d6e8fc3ef59aceba",
+    "sync.schema.json": "9a5ba286ce93ca216f496d470e50047366c1b8026d46cb96838fdaa63efa3e63",
+    "fixtures.py": "d3d3ff6d43ab5bb42124c31ec72da1e45397ccc5243aaa8eb267545f4f11fe37",
+    "fault_worker.py": "a3c487b078297d9bc45fcb804d22aac6f8ac1f7d2bd8eac41b841eb2f1bd75d7"
+  },
+  "limits": "One synthetic local run with large state present from early history, not an SLA, statistical benchmark or power-loss test. Host load/storage/dependency changes can cause latency and SQLite busy errors; admission and capacity recovery remain external. Original R3 2000-event/8MiB caps are withdrawn, not certified by this smaller run."
+}
--- /dev/null
+++ b/benchmark.py
@@ -0,0 +1,57 @@
+"""One synthetic near-capacity run; recorded timings are not an SLA."""
+from pathlib import Path
+from copy import deepcopy
+from time import perf_counter
+from datetime import datetime,timezone
+import argparse,hashlib,json,platform,sqlite3,subprocess,sys,tempfile
+import sync_register as p
+from fixtures import Harness,ADMIN,WRITER,SCOPE,EPOCH,PURPOSE,item,evidence
+HERE=Path(__file__).parent
+def run():
+    with tempfile.TemporaryDirectory(prefix='sync-capacity-') as tmp:
+        root=Path(tmp);db=root/'store.sqlite';h=Harness(db);setup_start=perf_counter();archive=h.archive();seq=len(archive['events'])+1;now=h.now()
+        def prospective(count):
+            rec=item();rec['key']['value']='K'*256;rec['content']=evidence('P'*210)
+            body=h.batch('bulk',[deepcopy(rec) for _ in range(count)]);state=deepcopy(archive['state']);command={'op':'commit','body':body}
+            result,kept=p.apply(state,command,WRITER,now,seq);assert kept
+            event={'sequence':seq,'previousDigest':archive['root'],'actor':WRITER,'recordedAt':now,'command':command,'result':result,'outcomeDigest':p.digest(state)};event['digest']=p.digest(event)
+            full={**archive,'events':archive['events']+[event],'state':state,'root':event['digest']}
+            return len(p.encode(full)),body
+        sample={'sequence':p.MAX_EVENTS,'previousDigest':'sha256:'+'0'*64,'actor':ADMIN,'recordedAt':now,'command':{'op':'fence','body':{'id':EPOCH,'expectedFence':1000000,'evidence':evidence('capacity-fence')}},'result':{'status':'recorded'},'outcomeDigest':'sha256:'+'0'*64,'digest':'sha256:'+'0'*64}
+        reserve=(p.MAX_EVENTS-seq)*len(p.encode(sample))+6000
+        low,high=0,256
+        while low<high:
+            middle=(low+high+1)//2
+            try:size,_=prospective(middle);fits=size+reserve<=p.MAX_BYTES
+            except p.Invalid:fits=False
+            if fits:low=middle
+            else:high=middle-1
+        assert low>0
+        _,body=prospective(low);h.reg.execute({'op':'commit','body':body},WRITER,now)
+        # Keep the large retained state from the start: this stresses full replay.
+        fence=1;write_times=[]
+        for _ in range(seq,p.MAX_EVENTS-2):
+            start=perf_counter();h.call('fence',{'id':EPOCH,'expectedFence':fence,'evidence':evidence('capacity-fence')});write_times.append(perf_counter()-start);fence+=1
+        at_capacity=h.archive();setup_seconds=perf_counter()-setup_start
+        start=perf_counter();h.archive();archive_seconds=perf_counter()-start
+        start=perf_counter();h.reg.read_receipt(SCOPE,PURPOSE,EPOCH,'bulk',WRITER,h.now());read_seconds=perf_counter()-start
+        request={'command':{'op':'commit','body':h.batch('capacity-race',[])},'actor':WRITER,'now':h.now()}
+        inp=root/'request.json';inp.write_text(json.dumps(request),encoding='utf-8');outputs=[root/'one.json',root/'two.json'];h.close()
+        start=perf_counter();workers=[subprocess.Popen([sys.executable,str(HERE/'fault_worker.py'),str(db),str(inp),str(out),'none'],stdout=subprocess.PIPE,stderr=subprocess.PIPE) for out in outputs]
+        runs=[]
+        for worker in workers:
+            _,err=worker.communicate(timeout=120);runs.append({'exitCode':worker.returncode,'stderr':err.decode('utf-8')})
+        race_seconds=perf_counter()-start
+        assert all(x['exitCode']==0 for x in runs),runs
+        replies=[json.loads(out.read_text()) for out in outputs];assert replies[0]==replies[1] and replies[0]['status']=='committed'
+        reg=p.Register(db);after_race=reg.archive(ADMIN)
+        # Fill to the exact retained-event cap, then prove a no-event retry still works.
+        while len(after_race['events'])<p.MAX_EVENTS:
+            reg.execute({'op':'fence','body':{'id':EPOCH,'expectedFence':fence,'evidence':evidence('capacity-fence')}},ADMIN,request['now']);fence+=1;after_race=reg.archive(ADMIN)
+        start=perf_counter();assert reg.execute(request['command'],WRITER,request['now'])==replies[0];retry_seconds=perf_counter()-start
+        final=reg.archive(ADMIN);reg.close();assert final==after_race
+        size=len(p.encode(final));assert size>p.MAX_BYTES*0.85 and size<=p.MAX_BYTES
+    files=('benchmark.py','sync_register.py','sync.schema.json','fixtures.py','fault_worker.py')
+    return {'format':'vercy-source-sync-capacity-run','executedAt':datetime.now(timezone.utc).isoformat(),'passed':True,'buildId':p.BUILD_ID,'python':platform.python_version(),'sqlite':sqlite3.sqlite_version,'eventLimit':p.MAX_EVENTS,'canonicalByteLimit':p.MAX_BYTES,'retainedEvents':len(final['events']),'canonicalBytes':size,'budgetFillFraction':round(size/p.MAX_BYTES,4),'bulkRecords':low,'setupSeconds':round(setup_seconds,3),'lastSetupWriteSeconds':round(write_times[-1],3),'maxSetupWriteSeconds':round(max(write_times),3),'archiveSeconds':round(archive_seconds,3),'readReceiptSeconds':round(read_seconds,3),'twoProcessExactRetrySeconds':round(race_seconds,3),'writerTimeouts':0,'retryAtLimitSeconds':round(retry_seconds,3),'sourceDigests':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in files},'limits':'One synthetic local run with large state present from early history, not an SLA, statistical benchmark or power-loss test. Host load/storage/dependency changes can cause latency and SQLite busy errors; admission and capacity recovery remain external. Original R3 2000-event/8MiB caps are withdrawn, not certified by this smaller run.'}
+if __name__=='__main__':
+    ap=argparse.ArgumentParser();ap.add_argument('--report',required=True);a=ap.parse_args();r=run();Path(a.report).write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in r.items() if k not in ('sourceDigests','limits')}))
--- /dev/null
+++ b/environment-report.json
@@ -0,0 +1,17 @@
+{
+  "format": "vercy-tested-runtime-inventory",
+  "observedAt": "2026-09-22T11:07:32.737705+00:00",
+  "python": "3.12.14",
+  "implementation": "CPython",
+  "sqlite": "3.53.1",
+  "osFamily": "Windows",
+  "architectureBits": 64,
+  "packages": {
+    "jsonschema": "4.26.0",
+    "attrs": "26.1.0",
+    "jsonschema-specifications": "2025.9.1",
+    "referencing": "0.37.0",
+    "rpds-py": "2026.6.3"
+  },
+  "limits": "Recorded versions used by author checks, not a complete environment lock, wheel hash pin or claim about other runtimes. requirements.txt pins only jsonschema. Host and personal paths are intentionally omitted."
+}

END COMPLETE PATCH â€” FINAL MARKER SYNC-R4-DELTA-20260922

END R4 INPUT PART 8/8 â€” SYNC-R4-PART-08
