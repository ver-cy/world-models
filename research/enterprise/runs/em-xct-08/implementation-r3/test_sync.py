from pathlib import Path
from copy import deepcopy
import json,subprocess,sys,tempfile,unittest
from jsonschema.exceptions import ValidationError
from fixtures import *
from sync_register import Invalid,DENIED,validate_archive,assess_rounds,historical_cut,resume_archive,lineage,digest,decode,inspect_import

HERE=Path(__file__).parent
class SyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='sync-test-');self.root=Path(self.tmp.name);self.h=Harness(self.root/'state.sqlite')
    def tearDown(self):self.h.close();self.tmp.cleanup()
    def test_global_conflict_budget_is_shared_across_writers(self):
        from unittest.mock import patch
        import sync_register as sr
        body=self.h.batch();self.h.commit(body);changed=deepcopy(body);changed['content']['token']=evidence('changed-token')
        with patch.object(sr,'MAX_CONFLICTS',3):
            for actor in (WRITER,OTHER,WRITER):self.assertEqual(self.h.commit(changed,actor),DENIED)
            before=self.h.archive();self.assertEqual(len(before['state']['conflicts']),3)
            self.assertEqual(self.h.commit(changed,OTHER),DENIED);self.assertEqual(self.h.archive(),before)
    def test_same_lineage_can_have_separate_purpose_mappings(self):
        self.h.mapping();other='asset-analysis';cat=catalogue(2)
        cat['pairs'].append({'sourceKind':'board','targetKind':'Project','purpose':other});self.h.call('catalogue',cat,ADMIN)
        pol=policy(2);grant=deepcopy(pol['grants'][0]);grant['purpose']=other;pol['grants'].append(grant);self.h.call('policy',pol,ADMIN)
        definition=deepcopy(self.h.state()['mappings']['urn:synthetic:mapping:1'][-1]['definition'])
        definition.update(id='urn:synthetic:mapping:other-purpose',purpose=other,targetId='urn:synthetic:project:2')
        self.h.call('mapping',definition);self.h.transition(definition['id'],'active')
        self.assertEqual(sum(h[-1]['state']=='active' for h in self.h.state()['mappings'].values()),2)
    def test_mapping_correction_cannot_probe_foreign_purpose(self):
        self.h.mapping();definition=deepcopy(self.h.state()['mappings']['urn:synthetic:mapping:1'][-1]['definition'])
        definition.update(id='urn:synthetic:mapping:correction',purpose='other-purpose')
        cat=catalogue(2);cat['pairs'].append({'sourceKind':'board','targetKind':'Project','purpose':'other-purpose'});self.h.call('catalogue',cat,ADMIN)
        pol=policy(2);grant=deepcopy(pol['grants'][0]);grant['purpose']='other-purpose';pol['grants'].append(grant);self.h.call('policy',pol,ADMIN)
        before=self.h.archive()
        for predecessor in ('urn:synthetic:mapping:1','urn:synthetic:mapping:missing'):
            definition['corrects']=predecessor;self.assertEqual(self.h.call('mapping',definition),DENIED);self.assertEqual(self.h.archive(),before)
    def test_admin_can_explicitly_grant_intake_to_close_orphan_round(self):
        rid='urn:synthetic:round:orphan'
        self.h.call('round-open',{'id':rid,'scopeId':SCOPE,'epochId':EPOCH,'purpose':PURPOSE,'consistency':'best-effort','consistencyEvidence':evidence('best-effort'),'visibilityCovered':False,'previousRoundId':None,'notEarlierEvidence':None})
        pol=policy(2,writer_rights=());self.h.call('policy',pol,ADMIN)
        self.assertEqual(self.h.call('round-seal',{'id':rid,'errors':[evidence('writer-revoked')]},ADMIN),DENIED)
        pol['revision']=3;pol['grants'].append({'actor':ADMIN,'scopeId':SCOPE,'purpose':PURPOSE,'rights':['intake'],'validFrom':'2025-01-01T00:00:00Z','validTo':'2030-01-01T00:00:00Z'});self.h.call('policy',pol,ADMIN)
        self.h.call('round-seal',{'id':rid,'errors':[evidence('writer-revoked')]},ADMIN)
        self.h.call('epoch-close',{'id':EPOCH,'reason':'operator-close','evidence':evidence('orphan-closed')},ADMIN);self.assertEqual(self.h.state()['epochs'][EPOCH]['status'],'closed')
    def test_two_boards_one_project_rename(self):
        self.h.mapping(value='a');self.h.mapping('urn:synthetic:mapping:2',value='b')
        self.h.commit(self.h.batch(items=[item('a'),item('b')]));renamed=item('a');renamed['content']=evidence('rename')
        self.h.commit(self.h.batch('rename',[renamed]));s=self.h.state()
        self.assertEqual(len(s['catalogue']['subjects']),3);self.assertEqual(len(s['mappings']),2)
        self.assertEqual([b['occurrences'][0]['mapping']['pin']['mappingId'] for b in s['batches'].values()],['urn:synthetic:mapping:1']*2)
    def test_exact_qualified_keys(self):
        s=self.h.state();self.assertNotEqual(lineage(s,SCOPE,key('01')),lineage(s,SCOPE,key('1')))
        self.h.call('source',source('urn:synthetic:source:b','tenant-b'));self.h.call('scope',scope('urn:synthetic:scope:b','urn:synthetic:source:b'));s=self.h.state()
        self.assertNotEqual(lineage(s,SCOPE,key()),lineage(s,'urn:synthetic:scope:b',key()))
    def test_recycled_and_unknown_keys_not_mapped(self):
        self.h.mapping();self.h.commit(self.h.batch(items=[item(),item(generation='record-2'),item(generation=None)]))
        outcomes=list(self.h.state()['batches'].values())[0]['occurrences']
        self.assertEqual([o['mapping']['status'] for o in outcomes],['mapped','unmapped','continuity-unknown'])
        with self.assertRaises(Invalid):self.h.mapping('urn:synthetic:mapping:unknown',generation=None)
    def test_retry_after_mapping_change_and_progress_retains_pin(self):
        self.h.mapping();body=self.h.batch();first=self.h.commit(body);events=len(self.h.archive()['events'])
        self.h.transition('urn:synthetic:mapping:1','retracted')
        self.h.mapping('urn:synthetic:mapping:2',target='urn:synthetic:project:2',corrects='urn:synthetic:mapping:1')
        self.h.commit(self.h.batch('later'));before=self.h.archive()
        body['attemptId']='urn:synthetic:attempt:retry';body['fence']=999
        self.assertEqual(self.h.commit(body),first);after=self.h.archive();self.assertEqual(before,after)
        receipt=next(b for b in after['state']['batches'].values() if b['id']==first['receiptId'])
        self.assertEqual(receipt['occurrences'][0]['mapping']['pin']['mappingId'],'urn:synthetic:mapping:1');self.assertGreater(len(after['events']),events)
    def test_changed_body_conflicts_without_overwrite(self):
        body=self.h.batch();self.h.commit(body);before=deepcopy(self.h.state()['batches'])
        body['content']['items'][0]['content']=evidence('different');self.assertEqual(self.h.commit(body),{'status':'not-accepted'})
        state=self.h.state();self.assertEqual(state['batches'],before);self.assertEqual(state['conflicts'][-1]['reason'],'changed-content')
    def test_reference_rewrapping_is_changed_body(self):
        body=self.h.batch();self.h.commit(body);body['content']['token']=evidence('new-wrapper')
        self.assertEqual(self.h.commit(body),{'status':'not-accepted'});self.assertEqual(self.h.state()['conflicts'][-1]['reason'],'changed-content')
    def test_duplicate_record_occurrences_keep_ordinals(self):
        self.h.commit(self.h.batch(items=[item(),item()]));o=list(self.h.state()['batches'].values())[0]['occurrences']
        self.assertNotEqual(o[0]['id'],o[1]['id']);self.assertEqual([x['ordinal'] for x in o],[0,1])
    def test_source_delete_has_no_subject_effect(self):
        self.h.mapping();before=self.h.state();self.h.commit(self.h.batch(items=[item(operation='source-deleted')]))
        after=self.h.state();self.assertEqual(before['catalogue'],after['catalogue']);self.assertEqual(before['mappings'],after['mappings'])
    def test_closed_epoch_commit_refused_read_allowed(self):
        body=self.h.batch();self.h.commit(body);self.h.call('epoch-close',{'id':EPOCH,'reason':'token-reset','evidence':evidence('reset')})
        before=self.h.archive();self.assertEqual(self.h.commit(body),{'status':'not-accepted'});self.assertEqual(before,self.h.archive())
        self.assertIn('occurrences',self.h.reg.read_receipt(SCOPE,PURPOSE,EPOCH,'batch-1',READER,self.h.now()))
        self.assertEqual(self.h.reg.read_receipt(SCOPE,PURPOSE,EPOCH,'batch-1',OTHER,self.h.now()),{'status':'not-accepted'})
    def test_stale_fence_and_head(self):
        body=self.h.batch();self.h.call('fence',{'id':EPOCH,'expectedFence':1,'evidence':evidence('fence')})
        self.assertEqual(self.h.commit(body),{'status':'not-accepted'});self.assertEqual(self.h.state()['conflicts'][-1]['reason'],'stale-fence')
        fresh=self.h.batch('ok');self.h.commit(fresh);fresh['content']['batchKey']='stale'
        self.assertEqual(self.h.commit(fresh),{'status':'not-accepted'});self.assertEqual(self.h.state()['conflicts'][-1]['reason'],'stale-head')
    def test_opaque_tokens_are_not_sorted(self):
        body=self.h.batch();self.h.commit(body);body=self.h.batch('next');body['content']['token']=evidence('opaque-a');self.h.commit(body)
        self.assertEqual(self.h.state()['epochs'][EPOCH]['progress'],2)
    def test_quarantine_conserved_and_retained(self):
        self.h.commit(self.h.batch(items=[item(),quarantine()]));self.h.commit(self.h.batch('next'))
        b=list(self.h.state()['batches'].values())[0];self.assertEqual((b['received'],b['accepted'],b['quarantined']),(2,1,1));self.assertEqual(b['quarantine'][0]['state'],'open')
        bad=self.h.archive();bad['state']['batches'][next(iter(bad['state']['batches']))]['quarantine']=[]
        with self.assertRaises(Invalid):validate_archive(bad)
    def test_no_fact_winner_in_intake(self):
        a=item();b=item();b['content']=evidence('disagreement');self.h.commit(self.h.batch(items=[a,b]))
        rows=list(self.h.state()['batches'].values())[0]['occurrences'];self.assertEqual(len(rows),2);self.assertNotEqual(rows[0]['content'],rows[1]['content']);self.assertFalse(any('winner' in x for x in rows))
    def test_wrong_target_kind_rejected(self):
        with self.assertRaises(Invalid):self.h.mapping(expected_kind='Person')
    def test_in_place_retarget_rejected(self):
        definition=self.h.mapping();definition['targetId']='urn:synthetic:project:2'
        with self.assertRaises(Invalid):self.h.call('mapping',definition)
    def test_reactivation_enforces_unique_active(self):
        self.h.mapping();self.h.transition('urn:synthetic:mapping:1','disputed');self.h.mapping('urn:synthetic:mapping:2',target='urn:synthetic:project:2')
        with self.assertRaises(Invalid):self.h.transition('urn:synthetic:mapping:1','active')
    def test_revoked_writer_cannot_probe_receipts(self):
        body=self.h.batch();self.h.commit(body);self.h.call('policy',policy(2,writer_rights=()))
        before=self.h.archive();existing=self.h.commit(body);body['content']['batchKey']='nonexistent';missing=self.h.commit(body)
        self.assertEqual(existing,missing);self.assertEqual(before,self.h.archive())
    def test_different_writer_no_duplicate_no_receipt(self):
        body=self.h.batch();self.h.commit(body);result=self.h.commit(body,OTHER)
        self.assertEqual(result,{'status':'not-accepted'});s=self.h.state();self.assertEqual(len(s['batches']),1);self.assertEqual(s['conflicts'][-1]['reason'],'principal-collision')
    def test_target_reclassification_suspends_new_pins(self):
        self.h.mapping();self.h.commit(self.h.batch());self.h.call('catalogue',catalogue(2,'Person'));self.h.commit(self.h.batch('after-reclassification'))
        rows=[b['occurrences'][0] for b in self.h.state()['batches'].values()]
        self.assertEqual([x['mapping']['status'] for x in rows],['mapped','active-pin-suspended'])
    def test_source_kind_change_cannot_reuse_mapping(self):
        self.h.mapping();new=scope('urn:synthetic:scope:changed',source_kind='dataset-record');self.h.call('scope',new);self.h.call('policy',policy(2,(SCOPE,new['id'])));self.h.open_epoch('urn:synthetic:epoch:new',new['id'])
        self.h.commit(self.h.batch('changed-kind',epoch='urn:synthetic:epoch:new',scope_id=new['id']))
        self.assertEqual(list(self.h.state()['batches'].values())[0]['occurrences'][0]['mapping']['status'],'active-pin-suspended')
    def test_correction_retains_known_history_no_invented_time(self):
        self.h.commit(self.h.batch());old=list(self.h.state()['batches'].values())[0]['occurrences'][0];cut=self.h.archive()['events'][-1]['recordedAt']
        corrected=item();corrected['content']=evidence('corrected');corrected['correction']={'occurrenceId':old['id'],'assertedBy':WRITER,'basis':'steward-asserted','evidence':evidence('correction')}
        self.h.commit(self.h.batch('correction',[corrected]));archive=self.h.archive();self.assertEqual(len(historical_cut(archive,cut)['state']['batches']),1)
        self.assertTrue(all(x['sourceEventTime'] is None for b in archive['state']['batches'].values() for x in b['occurrences']))
    def test_correction_wrong_lineage_refused(self):
        self.h.commit(self.h.batch());old=list(self.h.state()['batches'].values())[0]['occurrences'][0]
        corrected=item('different');corrected['correction']={'occurrenceId':old['id'],'assertedBy':WRITER,'basis':'steward-asserted','evidence':evidence('correction')}
        with self.assertRaises(Invalid):self.h.commit(self.h.batch('bad-correction',[corrected]))
    def test_two_complete_rounds_propose_only(self):
        self.h.round('urn:synthetic:round:1',['a','b']);self.h.round('urn:synthetic:round:2',['a'],'urn:synthetic:round:1')
        report=assess_rounds(self.h.archive(),'urn:synthetic:round:1','urn:synthetic:round:2');self.assertEqual(len(report['candidates']),1);self.assertEqual(report['effects'],[])
    def test_best_effort_or_visibility_unknown_refuses_absence(self):
        self.h.round('urn:synthetic:round:1',['a']);self.h.round('urn:synthetic:round:2',[],'urn:synthetic:round:1',consistency='best-effort')
        self.assertEqual(assess_rounds(self.h.archive(),'urn:synthetic:round:1','urn:synthetic:round:2')['status'],'insufficient-context')
    def test_failed_round_does_not_prove_absence(self):
        self.h.round('urn:synthetic:round:1',['a']);self.h.round('urn:synthetic:round:2',[],'urn:synthetic:round:1',errors=[evidence('failed-page')])
        self.assertFalse(self.h.state()['rounds']['urn:synthetic:round:2']['complete']);self.assertEqual(assess_rounds(self.h.archive(),'urn:synthetic:round:1','urn:synthetic:round:2')['status'],'insufficient-context')
    def test_epoch_reset_alone_does_not_break_round_comparison(self):
        self.h.round('urn:synthetic:round:1',['a']);self.h.call('epoch-close',{'id':EPOCH,'reason':'token-reset','evidence':evidence('reset')});self.h.open_epoch('urn:synthetic:epoch:2',reason='token-reset')
        self.h.round('urn:synthetic:round:2',[],'urn:synthetic:round:1',epoch='urn:synthetic:epoch:2')
        self.assertEqual(len(assess_rounds(self.h.archive(),'urn:synthetic:round:1','urn:synthetic:round:2')['candidates']),1)
    def test_explicit_deletion_reported_separately(self):
        self.h.round('urn:synthetic:round:1',['a']);self.h.commit(self.h.batch('delete',[item('a',operation='source-deleted')]))
        self.h.round('urn:synthetic:round:2',[],'urn:synthetic:round:1');result=assess_rounds(self.h.archive(),'urn:synthetic:round:1','urn:synthetic:round:2')
        self.assertEqual(result['candidates'],[]);self.assertEqual(result['explicitAvailabilityEvidence'][0]['operation'],'source-deleted')
    def test_round_unknown_order_refuses_absence(self):
        self.h.round('urn:synthetic:round:1',['a']);self.h.round('urn:synthetic:round:2',[])
        self.assertEqual(assess_rounds(self.h.archive(),'urn:synthetic:round:1','urn:synthetic:round:2')['status'],'insufficient-context')
    def test_archive_roundtrip_is_nonresumable(self):
        self.h.commit(self.h.batch());archive=self.h.archive();copy=decode(json.dumps(archive).encode())
        self.assertTrue(validate_archive(copy)['valid']);self.assertEqual(copy,archive)
        with self.assertRaises(Invalid):resume_archive(copy)
        copy['version']='0.0.1'
        with self.assertRaises(Invalid):validate_archive(copy)
    def test_archive_tamper_rejected(self):
        archive=self.h.archive();archive['events'][0]['command']['body']['tenant']='changed'
        with self.assertRaises(Invalid):validate_archive(archive)
    def test_unsupported_partitioned_scope_refused(self):
        body=scope('urn:synthetic:scope:p');body['mode']='global'
        with self.assertRaises(ValidationError):self.h.call('scope',body)
    def test_empty_batch_needs_explicit_flag(self):
        body=self.h.batch(items=[]);body['content']['empty']=False
        with self.assertRaises(Invalid):self.h.commit(body)
        body['content']['empty']=True;self.assertEqual(self.h.commit(body)['status'],'committed')
    def test_raw_secret_fields_refused(self):
        body=self.h.batch();body['content']['token']['rawToken']='synthetic-forbidden'
        with self.assertRaises(ValidationError):self.h.commit(body)
    def test_foreign_evidence_namespace_refused(self):
        body=self.h.batch();body['content']['token']['namespace']='urn:synthetic:other-store'
        with self.assertRaises(Invalid):self.h.commit(body)
    def test_duplicate_json_keys_refused(self):
        with self.assertRaises(Invalid):decode(b'{"x":1,"x":2}')
    def test_lossy_import_reports_refusal(self):
        archive=self.h.archive();archive['version']='0.0.1';report=inspect_import(json.dumps(archive).encode())
        self.assertEqual(report['status'],'refused');self.assertFalse(report['resumable']);self.assertIn('unsupported archive version',report['lossReport']['detail'])
    def test_source_generation_change_requires_new_mapping(self):
        self.h.mapping();sid='urn:synthetic:scope:restored';sourceid='urn:synthetic:source:restored';epoch='urn:synthetic:epoch:restored'
        self.h.call('source',source(sourceid,generation='instance-2'));self.h.call('scope',scope(sid,sourceid));self.h.call('policy',policy(2,(SCOPE,sid)));self.h.open_epoch(epoch,sid,reason='continuity-lost')
        self.h.commit(self.h.batch('restored',scope_id=sid,epoch=epoch))
        self.assertEqual(list(self.h.state()['batches'].values())[0]['occurrences'][0]['mapping']['status'],'unmapped')
        self.h.mapping('urn:synthetic:mapping:restored',scope_id=sid);self.h.commit(self.h.batch('reviewed',scope_id=sid,epoch=epoch))
        self.assertEqual(list(self.h.state()['batches'].values())[-1]['occurrences'][0]['mapping']['status'],'mapped')
    def test_scope_change_breaks_round_comparison(self):
        self.h.round('urn:synthetic:round:1',['a']);sid='urn:synthetic:scope:filtered';new=scope(sid);new['filter']=evidence('filter-changed')
        self.h.call('scope',new);self.h.call('policy',policy(2,(SCOPE,sid)));self.h.open_epoch('urn:synthetic:epoch:filtered',sid)
        self.h.round('urn:synthetic:round:2',[],scope_id=sid,epoch='urn:synthetic:epoch:filtered')
        self.assertEqual(assess_rounds(self.h.archive(),'urn:synthetic:round:1','urn:synthetic:round:2')['status'],'insufficient-context')
    def test_partial_page_progress_is_not_round_completeness(self):
        rid='urn:synthetic:round:partial';self.h.call('round-open',{'id':rid,'scopeId':SCOPE,'epochId':EPOCH,'purpose':PURPOSE,'consistency':'source-snapshot','consistencyEvidence':evidence('snapshot'),'visibilityCovered':True,'previousRoundId':None,'notEarlierEvidence':None})
        self.h.commit(self.h.batch('p0',[item(operation='snapshot-read')],round_id=rid,page=0));s=self.h.state()
        self.assertEqual(s['epochs'][EPOCH]['progress'],1);self.assertFalse(s['rounds'][rid]['complete'])
        with self.assertRaises(Invalid):self.h.commit(self.h.batch('p2',[],round_id=rid,page=2,terminal=True))
        self.h.call('round-seal',{'id':rid,'errors':[evidence('page-failed')]});self.assertFalse(self.h.state()['rounds'][rid]['complete'])
    def test_quarantine_blocks_round_absence(self):
        self.h.round('urn:synthetic:round:1',['a']);rid='urn:synthetic:round:quarantine'
        self.h.call('round-open',{'id':rid,'scopeId':SCOPE,'epochId':EPOCH,'purpose':PURPOSE,'consistency':'source-snapshot','consistencyEvidence':evidence('snapshot'),'visibilityCovered':True,'previousRoundId':'urn:synthetic:round:1','notEarlierEvidence':evidence('not-earlier')})
        self.h.commit(self.h.batch('q0',[quarantine()],round_id=rid,page=0,terminal=True));self.h.call('round-seal',{'id':rid,'errors':[]})
        self.assertEqual(assess_rounds(self.h.archive(),'urn:synthetic:round:1',rid)['status'],'insufficient-context')
    def test_visibility_uncertainty_blocks_absence(self):
        self.h.round('urn:synthetic:round:1',['a']);self.h.round('urn:synthetic:round:2',[],'urn:synthetic:round:1',visibility=False)
        self.assertEqual(assess_rounds(self.h.archive(),'urn:synthetic:round:1','urn:synthetic:round:2')['status'],'insufficient-context')
    def test_generation_attribution_wrong_source_rejected(self):
        body=self.h.batch();body['content']['items'][0]['key']['generationEvidence']['assertedBy']='urn:synthetic:unrelated-source'
        with self.assertRaises(Invalid):self.h.commit(body)
    def test_steward_generation_requires_mapping_right(self):
        body=self.h.batch();body['content']['items'][0]['key']['generationEvidence']={'basis':'steward-attested','assertedBy':OTHER,'evidence':evidence('attested')}
        with self.assertRaises(Invalid):self.h.commit(body,OTHER)
    def worker(self,body,name,point):
        inp=self.root/(name+'.input.json');out=self.root/(name+'.result.json')
        inp.write_text(json.dumps({'command':{'op':'commit','body':body},'actor':WRITER,'now':'2026-01-01T00:05:00Z'}),encoding='utf-8')
        return subprocess.Popen([sys.executable,str(HERE/'fault_worker.py'),str(self.h.path),str(inp),str(out),point],stdout=subprocess.PIPE,stderr=subprocess.PIPE),out
    def test_process_crash_before_commit(self):
        body=self.h.batch();proc,out=self.worker(body,'before','before-commit');stdout,stderr=proc.communicate(timeout=30)
        self.assertEqual(proc.returncode,73,stderr);self.assertEqual(self.h.state()['epochs'][EPOCH]['head'],None)
        self.assertEqual(self.h.commit(body)['status'],'committed')
    def test_process_crash_after_commit_lost_response(self):
        body=self.h.batch();proc,out=self.worker(body,'after','after-commit');stdout,stderr=proc.communicate(timeout=30)
        self.assertEqual(proc.returncode,73,stderr);self.h.clock=301
        before=self.h.archive();result=self.h.commit(body);self.assertEqual(result['status'],'committed');self.assertEqual(before,self.h.archive())
    def test_two_processes_one_progress_edge(self):
        a=self.h.batch('a');b=self.h.batch('b');p1,o1=self.worker(a,'one','none');p2,o2=self.worker(b,'two','none')
        for p in (p1,p2):out,err=p.communicate(timeout=30);self.assertEqual(p.returncode,0,err)
        results=[json.loads(p.read_text())['status'] for p in (o1,o2)];self.assertEqual(sorted(results),['committed','not-accepted']);self.assertEqual(self.h.state()['epochs'][EPOCH]['progress'],1)

    def test_exact_retry_at_event_budget(self):
        from unittest.mock import patch
        import sync_register
        body=self.h.batch();expected=self.h.commit(body);before=self.h.archive()
        with patch.object(sync_register,'MAX_EVENTS',len(before['events'])):
            self.assertEqual(self.h.commit(body),expected)
            self.assertEqual(self.h.archive(),before)
            with self.assertRaises(Invalid):self.h.commit(self.h.batch('new'))
    def test_denied_at_event_budget_is_uniform(self):
        from unittest.mock import patch
        import sync_register
        with patch.object(sync_register,'MAX_EVENTS',len(self.h.archive()['events'])):
            self.assertEqual(self.h.commit(self.h.batch(),actor='urn:synthetic:outsider'),DENIED)
    def test_oversized_register_id_rejected_before_store_creation(self):
        config=dict(self.h.archive()['config'],registerId='urn:'+'a'*157);path=self.root/'too-long.sqlite'
        with self.assertRaises(ValidationError):Register(path,config)
        self.assertFalse(path.exists())
    def test_maximum_register_id_remains_replayable(self):
        config=dict(self.h.archive()['config'],registerId='urn:'+'a'*156);reg=Register(self.root/'max-id.sqlite',config)
        events=self.h.archive()['events']
        for e in events:reg.execute(e['command'],e['actor'],e['recordedAt'])
        body=self.h.batch();result=reg.execute({'op':'commit','body':body},WRITER,'2026-01-01T00:01:00Z')
        self.assertEqual(result['status'],'committed');self.assertTrue(validate_archive(reg.archive(ADMIN))['valid']);reg.close()

    def test_prohibited_controls_in_key_actor_digest_and_bootstrap(self):
        for suffix in ('\n','\x00','\x7f','\x85'):
            body=self.h.batch();body['content']['items'][0]['key']['value']+=''+suffix
            with self.assertRaises(Invalid):self.h.commit(body)
            p=policy(2);p['grants'][0]['actor']+=suffix
            with self.assertRaises(Invalid):self.h.call('policy',p)
            body=self.h.batch();body['content']['token']['digest']='sha256:'+'0'*64+suffix
            with self.assertRaises(Invalid):self.h.commit(body)
            config=dict(self.h.archive()['config'],registerId='urn:synthetic:control'+suffix)
            with self.assertRaises(Invalid):Register(self.root/('control-'+str(ord(suffix))+'.sqlite'),config)
    def test_schema_itself_rejects_trailing_linefeed(self):
        import sync_register as s
        from jsonschema import Draft202012Validator
        schema={'$defs':s.SCHEMA['$defs'],'$ref':'#/$defs/RecordKey'}
        k=key();k['value']+='\n';self.assertFalse(Draft202012Validator(schema).is_valid(k))
    def test_non_ascii_lexical_keys_remain_exact(self):
        self.h.mapping(value='工程');records=[item('工程'),item('工\u200d程')]
        for n,r in enumerate(records):r['content']=evidence('unicode-payload-'+str(n))
        self.h.commit(self.h.batch(items=records))
        occ=next(iter(self.h.state()['batches'].values()))['occurrences'];self.assertEqual([o['mapping']['status'] for o in occ],['mapped','unmapped'])
    def test_derived_state_bool_int_substitution_rejected(self):
        self.h.commit(self.h.batch());a=self.h.archive();a['state']['epochs'][EPOCH]['progress']=True
        with self.assertRaises(Invalid):validate_archive(a)
    def test_changed_reducer_outcome_rejected(self):
        from unittest.mock import patch
        import sync_register as s
        self.h.mapping();self.h.commit(self.h.batch())
        with patch.object(s,'mapping_outcome',return_value={'status':'unmapped','pin':None}):
            with self.assertRaises(Invalid):self.h.archive()
    def test_changed_build_refuses_store_archive_and_native(self):
        import sync_register as s
        from unittest.mock import patch
        a=self.h.archive();value=s.native_value(a)
        with patch.object(s,'BUILD_ID','sha256:'+'0'*64):
            with self.assertRaises(Invalid):Register(self.h.path)
            with self.assertRaises(Invalid):validate_archive(a)
            with self.assertRaises(Invalid):s.archive_from_native(value)
    def test_outcome_digest_cannot_be_rewritten_with_outer_hash(self):
        a=self.h.archive();e=a['events'][-1];e['outcomeDigest']='sha256:'+'0'*64;e['digest']=digest({k:v for k,v in e.items() if k!='digest'});a['root']=e['digest']
        with self.assertRaises(Invalid):validate_archive(a)
    def test_conflicts_are_compact_bounded_and_do_not_advance_head(self):
        import sync_register as s
        self.h.commit(self.h.batch());before=self.h.state()['epochs'][EPOCH].copy()
        for n in range(s.MAX_CONFLICTS_PER_WRITER_SCOPE_EPOCH+3):
            b=self.h.batch();b['content']['items'][0]['content']=evidence('rejected-body-'+str(n));self.assertEqual(self.h.commit(b),DENIED)
        a=self.h.archive();self.assertEqual(len(a['state']['conflicts']),s.MAX_CONFLICTS_PER_WRITER_SCOPE_EPOCH);self.assertEqual(a['state']['epochs'][EPOCH],before)
        events=[e for e in a['events'] if e['command']['op']=='conflict-observation'];self.assertEqual(len(events),s.MAX_CONFLICTS_PER_WRITER_SCOPE_EPOCH)
        self.assertTrue(all('items' not in e['command']['body'] and 'content' not in e['command']['body'] for e in events));self.assertNotIn('rejected-body-',json.dumps(events))
    def test_conflict_at_event_limit_is_uniform_no_event(self):
        import sync_register as s
        from unittest.mock import patch
        b=self.h.batch();self.h.commit(b);a=self.h.archive();b['content']['items'][0]['content']=evidence('changed')
        with patch.object(s,'MAX_EVENTS',len(a['events'])):self.assertEqual(self.h.commit(b),DENIED);self.assertEqual(self.h.archive(),a)
    def test_internal_conflict_command_cannot_be_injected(self):
        self.h.commit(self.h.batch());changed=self.h.batch();changed['content']['items'][0]['content']=evidence('different');self.h.commit(changed)
        a=self.h.archive();cmd=a['events'][-1]['command'];self.assertEqual(self.h.reg.execute(cmd,WRITER,self.h.now()),DENIED);self.assertEqual(self.h.archive(),a)
    def test_correction_cannot_probe_foreign_scope_or_missing_target(self):
        sid='urn:synthetic:scope:private';s=scope(sid);s['filter']=evidence('private-filter');self.h.call('scope',s);self.h.call('policy',policy(2,(SCOPE,sid)));self.h.open_epoch('urn:synthetic:epoch:private',sid)
        self.h.commit(self.h.batch('private',scope_id=sid,epoch='urn:synthetic:epoch:private'));a=self.h.archive();oid=next(iter(a['state']['batches'].values()))['occurrences'][0]['id']
        self.h.call('policy',policy(3));before=self.h.archive()
        for target in (oid,'urn:synthetic:unknown'):
            row=item();row['correction']={'occurrenceId':target,'basis':'source-asserted','assertedBy':SOURCE,'evidence':evidence('correction')}
            self.assertEqual(self.h.commit(self.h.batch('correction',items=[row])),DENIED)
        self.assertEqual(self.h.archive(),before)
    def test_correction_requires_current_read_and_map(self):
        self.h.commit(self.h.batch());oid=next(iter(self.h.state()['batches'].values()))['occurrences'][0]['id'];row=item();row['correction']={'occurrenceId':oid,'basis':'source-asserted','assertedBy':SOURCE,'evidence':evidence('correction')}
        for revision,rights in [(2,('intake','map')),(3,('intake','read'))]:
            self.h.call('policy',policy(revision,writer_rights=rights));self.assertEqual(self.h.commit(self.h.batch('correction',items=[row])),DENIED)
    def test_source_asserted_correction_with_scoped_authority(self):
        self.h.commit(self.h.batch());oid=next(iter(self.h.state()['batches'].values()))['occurrences'][0]['id'];row=item();row['correction']={'occurrenceId':oid,'basis':'source-asserted','assertedBy':SOURCE,'evidence':evidence('correction')}
        self.assertEqual(self.h.commit(self.h.batch('correction',items=[row]))['status'],'committed')
    def test_coverage_attestation_needs_separate_grant(self):
        self.h.call('policy',policy(2,writer_rights=('intake','map','read')))
        body={'id':'urn:synthetic:round:no-attest','scopeId':SCOPE,'epochId':EPOCH,'purpose':PURPOSE,'consistency':'source-snapshot','consistencyEvidence':evidence('snapshot'),'visibilityCovered':True,'previousRoundId':None,'notEarlierEvidence':None}
        self.assertEqual(self.h.call('round-open',body),DENIED);body.update(consistency='best-effort',visibilityCovered=False);self.assertEqual(self.h.call('round-open',body),{'status':'recorded'})
    def test_mapping_correction_lineage_and_predecessor_guards(self):
        self.h.mapping();self.h.mapping('urn:synthetic:mapping:correction',corrects='urn:synthetic:mapping:1',activate=False)
        with self.assertRaises(Invalid):self.h.transition('urn:synthetic:mapping:correction','active')
        with self.assertRaises(Invalid):self.h.mapping('urn:synthetic:mapping:wrong-lineage',value='different',corrects='urn:synthetic:mapping:1')
        self.h.transition('urn:synthetic:mapping:1','retracted')
        with self.assertRaises(Invalid):self.h.transition('urn:synthetic:mapping:1','active')
        self.h.transition('urn:synthetic:mapping:correction','active')
    def test_mapping_window_and_disputed_state_produce_no_pin(self):
        body={'id':'urn:synthetic:mapping:window','scopeId':SCOPE,'key':key(),'purpose':PURPOSE,'targetId':'urn:synthetic:project:1','expectedTargetKind':'Project','issuer':WRITER,'validFrom':'2025-01-01T00:00:00Z','validTo':'2026-01-01T00:00:00Z','corrects':None,'evidence':evidence('mapping')}
        self.h.call('mapping',body);self.h.transition(body['id'],'active');self.h.commit(self.h.batch());self.assertEqual(next(iter(self.h.state()['batches'].values()))['occurrences'][0]['mapping']['status'],'active-pin-suspended')
        self.h.transition(body['id'],'disputed');self.h.commit(self.h.batch('disputed'));self.assertEqual(list(self.h.state()['batches'].values())[-1]['occurrences'][0]['mapping']['status'],'unmapped')
    def test_admin_has_no_implicit_intake_mapping_or_read(self):
        self.assertEqual(self.h.commit(self.h.batch(),ADMIN),DENIED)
        self.assertEqual(self.h.reg.read_receipt(SCOPE,PURPOSE,EPOCH,'batch-1',ADMIN,self.h.now()),DENIED)
        self.h.mapping(activate=False);self.assertEqual(self.h.call('mapping-state',{'id':'urn:synthetic:mapping:1','expectedRevision':1,'to':'active','reason':'admin attempt'},actor=ADMIN),DENIED)
    def test_expired_grant_and_wrong_purpose_do_not_replay(self):
        b=self.h.batch();self.h.commit(b)
        self.assertEqual(self.h.reg.execute({'op':'commit','body':b},WRITER,'2030-01-01T00:00:00Z'),DENIED)
        self.assertEqual(self.h.reg.read_receipt(SCOPE,'wrong-purpose',EPOCH,'batch-1',READER,self.h.now()),DENIED)
    def test_steward_generation_positive(self):
        b=self.h.batch();b['content']['items'][0]['key']['generationEvidence']={'basis':'steward-attested','assertedBy':WRITER,'evidence':evidence('attested')};self.assertEqual(self.h.commit(b)['status'],'committed')
    def test_invalid_calendar_timestamp_is_invalid_and_atomic(self):
        b=self.h.batch();b['content']['items'][0]['observedAt']='2026-02-30T00:00:00Z';a=self.h.archive()
        with self.assertRaises(Invalid):self.h.commit(b)
        self.assertEqual(self.h.archive(),a)
    def test_complete_archive_byte_budget_is_atomic(self):
        import sync_register as s
        from unittest.mock import patch
        a=self.h.archive();limit=len(s.encode(a))+100
        with patch.object(s,'MAX_BYTES',limit):
            with self.assertRaises(Invalid):self.h.commit(self.h.batch())
        self.assertEqual(self.h.archive(),a)
    def test_transport_utf8_and_internal_canonical_rows(self):
        import sync_register as s
        a=self.h.archive();raw=json.dumps(a,indent=2)
        self.assertTrue(inspect_import(raw.encode('utf-8'))['valid'])
        for encoding in ('utf-16','utf-32','utf-8-sig'):self.assertFalse(inspect_import(raw.encode(encoding))['valid'])
        row=self.h.reg.db.execute('SELECT seq,body FROM journal ORDER BY seq LIMIT 1').fetchone();self.h.reg.db.execute('UPDATE journal SET body=? WHERE seq=?',(b' '+row[1],row[0]))
        with self.assertRaises(Invalid):self.h.archive()
    def test_native_snapshot_profile_rejects_extra_fields_and_boolean_rank(self):
        import sync_register as s
        _,fact=s.native_records(self.h.archive(),'2026-01-01T01:00:00Z')
        bad=deepcopy(fact);bad['extra']='not-in-profile'
        with self.assertRaises(Invalid):s.validate_native_snapshot(bad)
        bad=deepcopy(fact);bad['authority']['rank']=False
        with self.assertRaises(Invalid):s.validate_native_snapshot(bad)
    def test_round_terminal_seal_and_epoch_close_guards(self):
        rid='urn:synthetic:round:guard';body={'id':rid,'scopeId':SCOPE,'epochId':EPOCH,'purpose':PURPOSE,'consistency':'source-snapshot','consistencyEvidence':evidence('snapshot'),'visibilityCovered':True,'previousRoundId':None,'notEarlierEvidence':None};self.h.call('round-open',body)
        with self.assertRaises(Invalid):self.h.call('epoch-close',{'id':EPOCH,'reason':'operator-close','evidence':evidence('close')})
        self.h.commit(self.h.batch('terminal',[item(operation='snapshot-read')],round_id=rid,page=0,terminal=True))
        with self.assertRaises(Invalid):self.h.commit(self.h.batch('after-terminal',round_id=rid,page=1,terminal=True))
        self.h.call('round-seal',{'id':rid,'errors':[]})
        with self.assertRaises(Invalid):self.h.commit(self.h.batch('sealed',round_id=rid,page=1,terminal=True))
        self.h.call('epoch-close',{'id':EPOCH,'reason':'operator-close','evidence':evidence('close')})
    def test_duplicate_declarations_and_configuration_revisions(self):
        with self.assertRaises(Invalid):self.h.call('source',source('urn:synthetic:duplicate-source'))
        with self.assertRaises(Invalid):self.h.call('scope',scope('urn:synthetic:duplicate-scope'))
        with self.assertRaises(Invalid):self.h.call('policy',policy(3))
        with self.assertRaises(Invalid):self.h.call('catalogue',catalogue(3))
        c=catalogue(2);c['subjects'].append(deepcopy(c['subjects'][0]))
        with self.assertRaises(Invalid):self.h.call('catalogue',c)
    def test_malformed_authorization_inputs_are_uniform(self):
        for command in ({'op':'commit','body':[]},{'op':'mapping-state','body':None},{'op':'round-seal','body':{}},[]):self.assertEqual(self.h.reg.execute(command,WRITER,self.h.now()),DENIED)
    def test_equal_host_times_are_ordered_by_journal_sequence(self):
        b=self.h.batch();now=self.h.now();self.h.reg.execute({'op':'commit','body':b},WRITER,now)
        b=self.h.batch('second');self.h.reg.execute({'op':'commit','body':b},WRITER,now)
        a=self.h.archive();cut=historical_cut(a,now);self.assertEqual(cut['events'],len(a['events']));self.assertEqual(cut['state']['epochs'][EPOCH]['progress'],2)

if __name__=='__main__':unittest.main(verbosity=2)
