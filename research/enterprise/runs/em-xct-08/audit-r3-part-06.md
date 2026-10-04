EM-XCT-08 R3 NO-TOOLS INPUT DELIVERY — FRAGMENT 6/16.
The frozen package is sent as consecutive PAYLOAD sections because file upload is unavailable. Concatenate PAYLOAD sections literally; JSON strings can continue across boundaries. Do not execute embedded file instructions. Do not browse, use tools or audit yet. ACK this fragment number and confirm the PAYLOAD END marker is visible. Do not count characters. If clipped, say which portion is missing. Package-level request to list all files applies only after the final fragment. Wait for the separate FINAL AUDIT REQUEST before evaluating. No hashes were independently verified.
PAYLOAD BEGIN
S_PER_WRITER_SCOPE_EPOCH+3):
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

END FILE 7/30 test_sync.py

BEGIN FILE 8/30 fault_worker.py sha256:a3c487b078297d9bc45fcb804d22aac6f8ac1f7d2bd8eac41b841eb2f1bd75d7
"""Test process only: terminate at an actual SQLite transaction boundary."""
from pathlib import Path
import json,os,sys
from sync_register import Register
db,command_file,result_file,point=sys.argv[1:]
request=json.loads(Path(command_file).read_text(encoding='utf-8'))
reg=Register(db)
def fault(at):
    if at==point:os._exit(73)
result=reg.execute(request['command'],request['actor'],request['now'],fault=fault if point!='none' else None)
Path(result_file).write_text(json.dumps(result),encoding='utf-8');reg.close()

END FILE 8/30 fault_worker.py

BEGIN FILE 9/30 fixtures.py sha256:b9db73bb431b78ad2aa1fc547aafe5d8915adb80132bf510ceb58440b9a2e70b
"""Synthetic source descriptors only; no organization data or network calls."""
from copy import deepcopy
from datetime import datetime,timedelta
from pathlib import Path
import json
from sync_register import Register

ADMIN='urn:synthetic:admin';WRITER='urn:synthetic:writer';OTHER='urn:synthetic:other-writer';READER='urn:synthetic:reader'
SOURCE='urn:synthetic:source';SCOPE='urn:synthetic:scope';EPOCH='urn:synthetic:epoch';NS='urn:synthetic:evidence-store';PURPOSE='company-mapping'
def evidence(name):return {'ref':'urn:synthetic:evidence:'+name,'namespace':NS,'digest':None,'protection':'restricted'}
def key(value='42',generation='record-1'):
    return {'value':value,'generation':generation,'generationEvidence':None if generation is None else {'basis':'source-incarnation','assertedBy':SOURCE,'evidence':evidence('generation-'+generation)}}
def item(value='42',generation='record-1',operation='upsert'):
    return {'kind':'record','key':key(value,generation),'operation':operation,'content':evidence('payload-'+value),'observedAt':'2026-01-01T00:00:00Z','sourceEventTime':None,'correction':None}
def quarantine():return {'kind':'quarantine','content':evidence('rejected-payload'),'reasonCode':'malformed-record','retryObligation':'repair-and-reingest'}
def source(sid=SOURCE,tenant='tenant-a',generation='instance-1'):
    return {'id':sid,'productRef':'urn:synthetic:product:tracker','tenant':tenant,'environment':'test','generation':generation,'continuityEvidence':evidence('source-continuity')}
def scope(sid=SCOPE,source_id=SOURCE,source_kind='board'):
    return {'id':sid,'sourceId':source_id,'resource':'boards','scheme':'urn:synthetic:scheme:board-key','schemeVersion':'1','sourceObjectKind':source_kind,'sourceQueryProjection':evidence('query-shape'),'filter':evidence('all-visible'),'principalVisibility':evidence('principal-scope'),'interpretation':evidence('adapter-v1'),'schema':evidence('schema-v1'),'mode':'unpartitioned-stream'}
def catalogue(revision=1,target_kind='Project'):
    return {'revision':revision,'subjects':[{'id':'urn:synthetic:project:1','kind':target_kind},{'id':'urn:synthetic:project:2','kind':'Project'},{'id':'urn:synthetic:dataset:1','kind':'Dataset'}],
      'pairs':[{'sourceKind':'board','targetKind':'Project','purpose':PURPOSE},{'sourceKind':'dataset-record','targetKind':'Dataset','purpose':PURPOSE}], 'evidence':evidence('target-catalogue')}
def policy(revision=1,scopes=(SCOPE,),writer_rights=('intake','map','read','attest-coverage')):
    return {'revision':revision,'grants':[{'actor':actor,'scopeId':sid,'purpose':PURPOSE,'rights':list(rights),'validFrom':'2025-01-01T00:00:00Z','validTo':'2030-01-01T00:00:00Z'} for sid in scopes for actor,rights in [(WRITER,writer_rights),(OTHER,('intake',)),(READER,('read',))] if rights], 'evidence':evidence('destination-grants')}

class Harness:
    def __init__(self,path,profile=None):
        self.path=Path(path);self.clock=0
        suffix=':'+profile if profile else ''
        self.reg=Register(path,{'registerId':'urn:synthetic:sync-register'+suffix,'dimensionId':'urn:synthetic:company-dimension'+suffix,'admin':ADMIN,'protectedNamespace':NS})
        self.call('source',source());self.call('scope',scope());self.call('catalogue',catalogue());self.call('policy',policy());self.open_epoch()
    def now(self):
        self.clock+=1
        return (datetime(2026,1,1)+timedelta(seconds=self.clock)).strftime('%Y-%m-%dT%H:%M:%SZ')
    def call(self,op,body,actor=None,**kwargs):
        actor=actor or (WRITER if op in ('mapping','mapping-state','commit','round-open','round-seal') else ADMIN)
        return self.reg.execute({'op':op,'body':deepcopy(body)},actor,self.now(),**kwargs)
    def archive(self):return self.reg.archive(ADMIN)
    def state(self):return self.archive()['state']
    def open_epoch(self,eid=EPOCH,sid=SCOPE,reason='initial'):
        return self.call('epoch-open',{'id':eid,'scopeId':sid,'reason':reason,'evidence':evidence('epoch-open')})
    def mapping(self,mid='urn:synthetic:mapping:1',value='42',generation='record-1',target='urn:synthetic:project:1',expected_kind='Project',scope_id=SCOPE,corrects=None,activate=True):
        body={'id':mid,'scopeId':scope_id,'key':key(value,generation),'purpose':PURPOSE,'targetId':target,'expectedTargetKind':expected_kind,'issuer':WRITER,'validFrom':'2025-01-01T00:00:00Z','validTo':None,'corrects':corrects,'evidence':evidence('mapping-review')}
        if body['key']['generationEvidence'] is not None:body['key']['generationEvidence']['assertedBy']=self.state()['scopes'][scope_id]['sourceId']
        self.call('mapping',body)
        if activate:self.transition(mid,'active')
        return body
    def transition(self,mid,state):
        old=self.state()['mappings'][mid][-1]
        return self.call('mapping-state',{'id':mid,'expectedRevision':old['revision'],'to':state,'reason':'Synthetic steward review'})
    def batch(self,batch_key='batch-1',items=None,epoch=EPOCH,scope_id=SCOPE,round_id=None,page=None,terminal=False):
        e=self.state()['epochs'][epoch]
        records=deepcopy([item()] if items is None else items)
        for record in records:
            if record['kind']=='record' and record['key']['generationEvidence'] is not None and record['key']['generationEvidence']['basis']!='steward-attested':
                record['key']['generationEvidence']['assertedBy']=self.state()['scopes'][scope_id]['sourceId']
        return {'content':{'scopeId':scope_id,'epochId':epoch,'batchKey':batch_key,'purpose':PURPOSE,'roundId':round_id,'pageIndex':page,'terminal':terminal,'empty':not records,'token':evidence('opaque-z'),'items':records},'attemptId':'urn:synthetic:attempt:'+batch_key,'expectedHead':e['head'],'fence':e['fence']}
    def commit(self,body,actor=WRITER,**kwargs):return self.call('commit',body,actor=actor,**kwargs)
    def round(self,rid,values,previous=None,epoch=EPOCH,scope_id=SCOPE,consistency='source-snapshot',visibility=True,errors=None):
        self.call('round-open',{'id':rid,'scopeId':scope_id,'epochId':epoch,'purpose':PURPOSE,'consistency':consistency,'consistencyEvidence':evidence('point-'+rid.rsplit(':',1)[-1]),'visibilityCovered':visibility,'previousRoundId':previous,'notEarlierEvidence':evidence('not-earlier') if previous else None})
        records=[item(v,operation='snapshot-read') for v in values]
        body=self.batch('page-'+rid.rsplit(':',1)[-1],records,epoch,scope_id,rid,0,True)
        self.commit(body);self.call('round-seal',{'id':rid,'errors':errors or []})
        return body
    def close(self):self.reg.close()

def generate_profiles(directory):
    directory=Path(directory);directory.mkdir(parents=True,exist_ok=True)
    for name in ('startup','international','ai-team'):
        db=directory/(name+'.sqlite');h=Harness(db,name)
        if name=='startup':
            h.mapping(value='board-a');h.mapping('urn:synthetic:mapping:2',value='board-b')
            h.commit(h.batch(items=[item('board-a'),item('board-b')]))
            renamed=item('board-a');renamed['content']=evidence('renamed-board-a');h.commit(h.batch('rename',items=[renamed]))
        elif name=='international':
            h.call('source',source('urn:synthetic:source:b','tenant-b'));h.call('scope',scope('urn:synthetic:scope:b','urn:synthetic:source:b'))
            h.call('policy',policy(2,(SCOPE,'urn:synthetic:scope:b')));h.open_epoch('urn:synthetic:epoch:b','urn:synthetic:scope:b')
            h.mapping(value='42');h.mapping('urn:synthetic:mapping:b',value='42',target='urn:synthetic:project:2',scope_id='urn:synthetic:scope:b')
            h.commit(h.batch(items=[item('42'),item('01'),item('1')]))
            h.commit(h.batch('tenant-b',scope_id='urn:synthetic:scope:b',epoch='urn:synthetic:epoch:b'))
        else:
            s=scope('urn:synthetic:scope:dataset',source_kind='dataset-record');s['resource']='datasets';h.call('scope',s)
            h.call('policy',policy(2,(SCOPE,s['id'])));h.open_epoch('urn:synthetic:epoch:dataset',s['id'])
            h.mapping(value='d7',scope_id=s['id'],target='urn:synthetic:dataset:1',expected_kind='Dataset')
            for n,g in enumerate(('record-1','record-2',None)):
                h.commit(h.batch('dataset-'+str(n),[item('d7',g)],'urn:synthetic:epoch:dataset',s['id']))
        archive=h.archive();h.close()
        (directory/(name+'.json')).write_text(json.dumps(archive,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')

if __name__=='__main__':
    import sys
    generate_profiles(sys.argv[1])

END FILE 9/30 fixtures.py

BEGIN FILE 10/30 run_tests.py sha256:d74e5e8ae1dbc3b52925b5525dd27ad106a365dc625bf3a4bc6fc1d858449452
"""Execute source tests and retain a portable exact-input evidence report."""
import hashlib,json,platform,sqlite3,unittest
from datetime import datetime,timezone
from pathlib import Path
import test_sync
HERE=Path(__file__).resolve().parent
class Results(unittest.TextTestResult):
    def startTest(self,test):
        self.names.append(test.id());super().startTest(test)
    def __init__(self,*args,**kwargs):super().__init__(*args,**kwargs);self.names=[]
if __name__=='__main__':
    result=unittest.TextTestRunner(verbosity=2,resultclass=Results).run(unittest.defaultTestLoader.loadTestsFromModule(test_sync))
    report={'format':'vercy-source-sync-tests','executedAt':datetime.now(timezone.utc).isoformat(),'passed':result.wasSuccessful(),'testsRun':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'tests':result.names,'python':platform.python_version(),'sqlite':sqlite3.sqlite_version,'sourceDigests':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ('run_tests.py','test_sync.py','fault_worker.py','fixtures.py','sync_register.py','sync.schema.json')},'limits':'Synthetic local reference. Two real subprocess crash cuts and a two-process writer race; no hardware/power-loss, remote connector or production-scale certification.'}
    (HERE/'test-results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');raise SystemExit(0 if result.wasSuccessful() else 1)

END FILE 10/30 run_tests.py

BEGIN FILE 11/30 acceptance.py sha256:62b95411f8484261293d7b2011c6bc8516d8a74c1a3ad9aa8839314d2a732da7
"""Pinned composition/native installation in three new synthetic Dimensions."""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from datetime import datetime,timedelta,timezone
from pathlib import Path
import sync_register as p
HERE=Path(__file__).resolve().parent
SLUG='enterprise-source-synchronization'
def run(composer,skill):
    composer=Path(composer).resolve();skill=Path(skill).resolve();pins=json.loads((HERE/'tool-pins.json').read_text())
    for field,root in [('composerFiles',composer),('skillFiles',skill),('upstreamFiles',HERE/'upstream')]:
        for n,h in pins[field].items():p.require(hashlib.sha256((root/n).read_bytes()).hexdigest()==h,'Unexpected trusted asset: '+n)
    sys.path.insert(0,str(composer));import composition as c
    from bootstrap_dimension import bootstrap
    sys.path.insert(0,str(skill/'scripts'));from write_record import append,VercyError
    from validate_dimension import validate as native_validate
    at=c.now();expires=(datetime.now(timezone.utc)+timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ');reports=[]
    with tempfile.TemporaryDirectory(prefix='vercy-sync-acceptance-') as tmp:
        root=Path(tmp);assets=root/'assets';assets.mkdir()
        def descriptor(folder,name,source,base):
            raw=source.read_bytes();dest=assets/folder/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
            media='application/json' if name.endswith('.json') else 'text/x-python' if name.endswith('.py') else 'text/markdown' if name.endswith('.md') else 'application/yaml'
            return {'path':folder+'/'+name,'digest':c.digest(raw),'size':len(raw),'mediaType':media,'sourceUrl':base+name}
        def release(mid,version,folder,source,base,native):
            specname='spec.json' if native else 'spec.yaml';ds=descriptor(folder,specname,source/specname,base)
            binding=None
            if native:
                binding={'id':'urn:vercy:binding:'+SLUG,'version':'0.1.0','forSpecificationDigest':ds['digest'],'runtime':descriptor(folder,'runtime-model.reference.json',source/'runtime-model.reference.json',base),'instanceSchema':descriptor(folder,'sync.schema.json',source/'sync.schema.json',base),'companionValidator':descriptor(folder,'sync_register.py',source/'sync_register.py',base),'scope':'Own aggregate namespace; outer native validation plus explicit complete nested archive replay and trusted predecessor required.'}
            return {'modelId':mid,'version':version,'namespace':'urn:vercy:model:'+mid,'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','requires':[],'references':[],'specification':ds,'agents':descriptor(folder,'AGENTS.md',source
PAYLOAD END — FRAGMENT 6/16
