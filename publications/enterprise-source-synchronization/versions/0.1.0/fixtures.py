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
            s=scope('urn:synthetic:scope:dataset',source_kind='dataset-record');s['resource']='datasets';s['scheme']='urn:synthetic:scheme:dataset-key';h.call('scope',s)
            h.call('policy',policy(2,(SCOPE,s['id'])));h.open_epoch('urn:synthetic:epoch:dataset',s['id'])
            h.mapping(value='d7',scope_id=s['id'],target='urn:synthetic:dataset:1',expected_kind='Dataset')
            for n,g in enumerate(('record-1','record-2',None)):
                h.commit(h.batch('dataset-'+str(n),[item('d7',g)],'urn:synthetic:epoch:dataset',s['id']))
        archive=h.archive();h.close()
        (directory/(name+'.json')).write_text(json.dumps(archive,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')

if __name__=='__main__':
    import sys
    generate_profiles(sys.argv[1])
