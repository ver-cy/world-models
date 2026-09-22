"""Build closed input contracts for the bounded source synchronization reference."""
from pathlib import Path
import json

def obj(**properties):
    return {'type':'object','additionalProperties':False,'required':list(properties),'properties':properties}
def arr(items,maximum=256): return {'type':'array','maxItems':maximum,'items':items}
def enum(*values):return {'enum':list(values)}
def nullable(value):return {'anyOf':[value,{'type':'null'}]}
def ref(name):return {'$ref':'#/$defs/'+name}
END=r'$(?![\s\S])'
S={'type':'string','minLength':1,'maxLength':256,'pattern':r'^[^\x00-\x1f\x7f-\x9f]+'+END}
U={**S,'pattern':r'^urn:[A-Za-z0-9][A-Za-z0-9:._/-]*'+END}
T={'type':'string','pattern':r'^20[0-9]{2}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z'+END}
I={'type':'integer','minimum':0,'maximum':1000000}
P={'type':'integer','minimum':1,'maximum':1000000}
B={'type':'boolean'}
H={'type':'string','pattern':r'^sha256:[0-9a-f]{64}'+END}
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
D['Grant']=obj(actor=U,scopeId=U,purpose=S,rights={'type':'array','items':enum('intake','map','read','attest-coverage'),'uniqueItems':True,'minItems':1,'maxItems':4},validFrom=T,validTo=T)
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
D['ConflictRecord']=obj(scopeId=U,epochId=U,batchKey=S,purpose=S,attemptId=U,expectedHead=nullable(U),fence=P,suppliedDigest=H,reason=enum('principal-collision','changed-content','stale-head','stale-fence'))
JCOMMAND={'oneOf':[ref('Command'),obj(op=enum('conflict-observation'),body=ref('ConflictRecord'))]}
D['JournalEvent']=obj(sequence=P,previousDigest=H,actor=U,recordedAt=T,command=JCOMMAND,result=ref('JournalResult'),outcomeDigest=H,digest=H)
NATIVE=obj(format=enum('vercy-source-sync-journal-snapshot'),version=enum('0.1.0'),buildId=H,config=ref('Bootstrap'),events=arr(ref('JournalEvent'),2000),root=H,resumable=enum(False))
SCHEMA={'$schema':'https://json-schema.org/draft/2020-12/schema','$id':'urn:vercy:enterprise-source-synchronization:0.1.0:inputs','$defs':D,**NATIVE}
if __name__=='__main__':
    (Path(__file__).parent/'sync.schema.json').write_text(json.dumps(SCHEMA,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'definitions':len(D),'commands':len(OPS)}))
