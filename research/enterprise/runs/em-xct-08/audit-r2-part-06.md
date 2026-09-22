Continuation of the same frozen R2 no-tools audit. ACK only; do not audit yet.
FRAGMENT 6/15
PAYLOAD BEGIN
p":{"enum":["catalogue"]},"body":{"$ref":"#/$defs/Catalogue"}}},{"type":"object","additionalProperties":false,"required":["op","body"],"properties":{"op":{"enum":["policy"]},"body":{"$ref":"#/$defs/Policy"}}},{"type":"object","additionalProperties":false,"required":["op","body"],"properties":{"op":{"enum":["mapping"]},"body":{"$ref":"#/$defs/RecordSubjectMapping"}}},{"type":"object","additionalProperties":false,"required":["op","body"],"properties":{"op":{"enum":["mapping-state"]},"body":{"$ref":"#/$defs/MappingTransition"}}},{"type":"object","additionalProperties":false,"required":["op","body"],"properties":{"op":{"enum":["epoch-open"]},"body":{"$ref":"#/$defs/EpochOpen"}}},{"type":"object","additionalProperties":false,"required":["op","body"],"properties":{"op":{"enum":["epoch-close"]},"body":{"$ref":"#/$defs/EpochClose"}}},{"type":"object","additionalProperties":false,"required":["op","body"],"properties":{"op":{"enum":["fence"]},"body":{"$ref":"#/$defs/FenceAdvance"}}},{"type":"object","additionalProperties":false,"required":["op","body"],"properties":{"op":{"enum":["round-open"]},"body":{"$ref":"#/$defs/SnapshotRound"}}},{"type":"object","additionalProperties":false,"required":["op","body"],"properties":{"op":{"enum":["round-seal"]},"body":{"$ref":"#/$defs/RoundSeal"}}},{"type":"object","additionalProperties":false,"required":["op","body"],"properties":{"op":{"enum":["commit"]},"body":{"$ref":"#/$defs/BatchAdmission"}}}]},"JournalResult":{"oneOf":[{"type":"object","additionalProperties":false,"required":["status"],"properties":{"status":{"enum":["recorded","not-accepted"]}}},{"type":"object","additionalProperties":false,"required":["status","receiptId"],"properties":{"status":{"enum":["committed"]},"receiptId":{"type":"string","minLength":1,"maxLength":256,"pattern":"^urn:[A-Za-z0-9][A-Za-z0-9:._/-]*$"}}}]},"JournalEvent":{"type":"object","additionalProperties":false,"required":["sequence","previousDigest","actor","recordedAt","command","result","digest"],"properties":{"sequence":{"type":"integer","minimum":1,"maximum":1000000},"previousDigest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"},"actor":{"type":"string","minLength":1,"maxLength":256,"pattern":"^urn:[A-Za-z0-9][A-Za-z0-9:._/-]*$"},"recordedAt":{"type":"string","pattern":"^20[0-9]{2}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"},"command":{"$ref":"#/$defs/Command"},"result":{"$ref":"#/$defs/JournalResult"},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}}}},"type":"object","additionalProperties":false,"required":["format","version","config","events","root","resumable"],"properties":{"format":{"enum":["vercy-source-sync-journal-snapshot"]},"version":{"enum":["0.1.0"]},"config":{"$ref":"#/$defs/Bootstrap"},"events":{"type":"array","maxItems":2000,"items":{"$ref":"#/$defs/JournalEvent"}},"root":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"},"resumable":{"enum":[false]}}}
END FILE sync.schema.json

BEGIN FILE build_schema.py sha256:ff3dac9dc120d1fe63f2c46df47c772e215961a3e05590f157a5db2c0bd4f569
Complete text; display newlines may normalize CRLF to LF. SHA identifies original bytes.
"""Build closed input contracts for the bounded source synchronization reference."""
from pathlib import Path
import json

def obj(**properties):
    return {'type':'object','additionalProperties':False,'required':list(properties),'properties':properties}
def arr(items,maximum=256): return {'type':'array','maxItems':maximum,'items':items}
def enum(*values):return {'enum':list(values)}
def nullable(value):return {'anyOf':[value,{'type':'null'}]}
def ref(name):return {'$ref':'#/$defs/'+name}
S={'type':'string','minLength':1,'maxLength':256,'pattern':r'^[^\x00-\x1f\x7f]+$'}
U={**S,'pattern':r'^urn:[A-Za-z0-9][A-Za-z0-9:._/-]*$'}
T={'type':'string','pattern':r'^20[0-9]{2}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$'}
I={'type':'integer','minimum':0,'maximum':1000000}
P={'type':'integer','minimum':1,'maximum':1000000}
B={'type':'boolean'}
H={'type':'string','pattern':'^sha256:[0-9a-f]{64}$'}
D={}
D['EvidenceRef']=obj(ref=U,namespace=U,digest=nullable(H),protection=enum('restricted'))
D['GenerationEvidence']=obj(basis=enum('source-incarnation','source-nonreuse-guarantee','steward-attested'),assertedBy=U,evidence=ref('EvidenceRef'))
D['RecordKey']=obj(value=S,generation=nullable(S),generationEvidence=nullable(ref('GenerationEvidence')))
D['Correction']=obj(occurrenceId=U,assertedBy=U,basis=enum('source-asserted','steward-asserted'),evidence=ref('EvidenceRef'))
D['OccurrenceInput']=obj(kind=enum('record'),key=ref('RecordKey'),operation=enum('snapshot-read','upsert','source-deleted','removed-from-scope','inaccessible'),content=ref('EvidenceRef'),observedAt=T,sourceEventTime=nullable(T),correction=nullable(ref('Correction')))
D['QuarantineInput']=obj(kind=enum('quarantine'),content=ref('EvidenceRef'),reasonCode=enum('malformed-record','unsupported-schema','missing-key','invalid-value','source-error'),retryObligation=enum('repair-and-reingest','steward-review'))
D['SourceInstance']=obj(id=U,productRef=U,tenant=S,environment=S,generation=S,continuityEvidence=ref('EvidenceRef'))
D['AcquisitionScope']=obj(id=U,sourceId=U,resource=S,scheme=U,schemeVersion=S,sourceObjectKind=S,sourceQueryProjection=ref('EvidenceRef'),filter=ref('EvidenceRef'),principalVisibility=ref('EvidenceRef'),interpretation=ref('EvidenceRef'),schema=ref('EvidenceRef'),mode=enum('unpartitioned-stream'))
D['Target']=obj(id=U,kind=S)
D['AboutnessPair']=obj(sourceKind=S,targetKind=S,purpose=S)
D['Catalogue']=obj(revision=P,subjects=arr(ref('Target')),pairs=arr(ref('AboutnessPair')),evidence=ref('EvidenceRef'))
D['Grant']=obj(actor=U,scopeId=U,purpose=S,rights={'type':'array','items':enum('intake','map','read'),'uniqueItems':True,'minItems':1,'maxItems':3},validFrom=T,validTo=T)
D['Policy']=obj(revision=P,grants=arr(ref('Grant')),evidence=ref('EvidenceRef'))
D['RecordSubjectMapping']=obj(id=U,scopeId=U,key=ref('RecordKey'),purpose=S,targetId=U,expectedTargetKind=S,issuer=U,validFrom=T,validTo=nullable(T),corrects=nullable(U),evidence=ref('EvidenceRef'))
D['MappingTransition']=obj(id=U,expectedRevision=P,to=enum('active','disputed','retracted'),reason=S)
D['EpochOpen']=obj(id=U,scopeId=U,reason=enum('initial','token-reset','continuity-lost','operator-reinit'),evidence=ref('EvidenceRef'))
D['EpochClose']=obj(id=U,reason=enum('token-reset','scope-retired','continuity-lost','operator-close'),evidence=ref('EvidenceRef'))
D['FenceAdvance']=obj(id=U,expectedFence=P,evidence=ref('EvidenceRef'))
D['SnapshotRound']=obj(id=U,scopeId=U,epochId=U,purpose=S,consistency=enum('source-snapshot','best-effort'),consistencyEvidence=ref('EvidenceRef'),visibilityCovered=B,previousRoundId=nullable(U),notEarlierEvidence=nullable(ref('EvidenceRef')))
D['RoundSeal']=obj(id=U,errors=arr(ref('EvidenceRef'),32))
D['BatchContent']=obj(scopeId=U,epochId=U,batchKey=S,purpose=S,roundId=nullable(U),pageIndex=nullable(I),terminal=B,empty=B,token=ref('EvidenceRef'),items=arr({'oneOf':[ref('OccurrenceInput'),ref('QuarantineInput')]},256))
D['BatchAdmission']=obj(content=ref('BatchContent'),attemptId=U,expectedHead=nullable(U),fence=P)
D['Bootstrap']=obj(registerId={**U,'maxLength':160},dimensionId=U,admin=U,protectedNamespace=U)
OPS={'source':'SourceInstance','scope':'AcquisitionScope','catalogue':'Catalogue','policy':'Policy','mapping':'RecordSubjectMapping','mapping-state':'MappingTransition','epoch-open':'EpochOpen','epoch-close':'EpochClose','fence':'FenceAdvance','round-open':'SnapshotRound','round-seal':'RoundSeal','commit':'BatchAdmission'}
D['Command']={'oneOf':[obj(op=enum(op),body=ref(typ)) for op,typ in OPS.items()]}
D['JournalResult']={'oneOf':[obj(status=enum('recorded','not-accepted')),obj(status=enum('committed'),receiptId=U)]}
D['JournalEvent']=obj(sequence=P,previousDigest=H,actor=U,recordedAt=T,command=ref('Command'),result=ref('JournalResult'),digest=H)
NATIVE=obj(format=enum('vercy-source-sync-journal-snapshot'),version=enum('0.1.0'),config=ref('Bootstrap'),events=arr(ref('JournalEvent'),2000),root=H,resumable=enum(False))
SCHEMA={'$schema':'https://json-schema.org/draft/2020-12/schema','$id':'urn:vercy:enterprise-source-synchronization:0.1.0:inputs','$defs':D,**NATIVE}
if __name__=='__main__':
    (Path(__file__).parent/'sync.schema.json').write_text(json.dumps(SCHEMA,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'definitions':len(D),'commands':len(OPS)}))

END FILE build_schema.py

BEGIN FILE test_sync.py sha256:6f9023fb8bd495f555f4e8587df0172a7e00e88531bb2f6de2b97638e8dba9bb
Complete text; display newlines may normalize CRLF to LF. SHA identifies original bytes.
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

PAYLOAD END — FRAGMENT 6/15
