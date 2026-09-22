Continuation of the same frozen R2 no-tools audit. ACK only; do not audit yet.
FRAGMENT 8/15
PAYLOAD BEGIN
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

if __name__=='__main__':unittest.main(verbosity=2)

END FILE test_sync.py

BEGIN FILE fault_worker.py sha256:a3c487b078297d9bc45fcb804d22aac6f8ac1f7d2bd8eac41b841eb2f1bd75d7
Complete text; display newlines may normalize CRLF to LF. SHA identifies original bytes.
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

END FILE fault_worker.py

BEGIN FILE fixtures.py sha256:79530908049f3516b268ca60bbda8ab058528504d84e9e2b9510fd3f438d406a
Complete text; display newlines may normalize CRLF to LF. SHA identifies original bytes.
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
def policy(revision=1,scopes=(SCOPE,),writer_rights=('intake','map','read')):
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

END FILE fixtures.py

BEGIN FILE run_tests.py sha256:d74e5e8ae1dbc3b52925b5525dd27ad106a365dc625bf3a4bc6fc1d858449452
Complete text; display newlines may normalize CRLF to LF. SHA identifies original bytes.
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

PAYLOAD END — FRAGMENT 8/15
