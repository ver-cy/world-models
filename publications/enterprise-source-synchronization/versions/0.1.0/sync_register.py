"""Local metadata intake reference; host-authenticated actors, no connector/IAM.

The immutable SQLite journal is the master. Reducer-derived state is a view.
Archives are historical evidence only and cannot be imported as writable stores.
"""
from pathlib import Path
from datetime import datetime
from copy import deepcopy
import hashlib,json,sqlite3,re
from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError

VERSION='0.1.0'
MAX_EVENTS=128
MAX_BYTES=512*1024
MAX_TRANSPORT_BYTES=8*1024*1024
MAX_CONFLICTS=32
MAX_CONFLICTS_PER_WRITER_SCOPE_EPOCH=4
SCHEMA=json.loads((Path(__file__).with_name('sync.schema.json')).read_text(encoding='utf-8'))
BUILD_ID='sha256:'+hashlib.sha256(Path(__file__).read_bytes()+b'\0'+Path(__file__).with_name('sync.schema.json').read_bytes()).hexdigest()
DENIED={'status':'not-accepted'}
SURROGATE=re.compile('[\ud800-\udfff]')
CONTROL=re.compile('[\x00-\x1f\x7f-\x9f]')

class Invalid(ValueError): pass
def require(ok,message):
    if not ok:raise Invalid(message)
def encode(value):
    def walk(x):
        require(type(x) in (dict,list,str,int,bool,type(None)),'unsupported JSON value')
        if type(x)==dict:
            require(all(type(k)==str for k in x),'non-string JSON key')
            for k,v in x.items():walk(k);walk(v)
        elif type(x)==list:
            for v in x:walk(v)
        elif type(x)==int:require(abs(x)<=1000000,'integer bound')
        elif type(x)==str:
            require(SURROGATE.search(x) is None,'surrogate')
            require(CONTROL.search(x) is None,'control character')
    try:walk(value)
    except RecursionError as error:raise Invalid('nesting too deep') from error
    raw=json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')
    require(len(raw)<=MAX_BYTES,'byte budget')
    return raw
def digest(value):return 'sha256:'+hashlib.sha256(encode(value)).hexdigest()
def decode(raw):
    require(type(raw) in (bytes,str),'JSON bytes or text required')
    require(len(raw if type(raw)==bytes else raw.encode('utf-8'))<=MAX_TRANSPORT_BYTES,'transport byte budget')
    if type(raw)==bytes:raw=raw.decode('utf-8',errors='strict')
    require(type(raw)==str and not raw.startswith('\ufeff'),'UTF-8 without BOM required')
    def pairs(items):
        out={}
        for k,v in items:require(k not in out,'duplicate JSON key');out[k]=v
        return out
    try:value=json.loads(raw,object_pairs_hook=pairs,parse_float=lambda _:(_ for _ in ()).throw(Invalid('float')),
                         parse_constant=lambda _:(_ for _ in ()).throw(Invalid('constant')))
    except RecursionError as error:raise Invalid('nesting too deep') from error
    encode(value)
    return value
def validate(name,value):
    encode(value)
    Draft202012Validator({'$schema':SCHEMA['$schema'],'$defs':SCHEMA['$defs'],'$ref':'#/$defs/'+name}).validate(value)
def time(value):
    require(type(value)==str and len(value)==20 and value.endswith('Z'),'UTC seconds required')
    try:return datetime.strptime(value,'%Y-%m-%dT%H:%M:%SZ')
    except ValueError as e:raise Invalid('invalid calendar timestamp') from e
def within(now,start,end):return time(start)<=time(now) and (end is None or time(now)<time(end))
def initial(config):
    validate('Bootstrap',config)
    return {'config':deepcopy(config),'catalogue':None,'policy':None,'sources':{},'scopes':{},'mappings':{},'epochs':{},'rounds':{},'batches':{},'conflicts':[]}
def permitted(state,actor,scope,purpose,right,now):
    return bool(state['policy']) and any(g['actor']==actor and g['scopeId']==scope and g['purpose']==purpose and right in g['rights'] and within(now,g['validFrom'],g['validTo']) for g in state['policy']['grants'])
def evidence_check(value,namespace):
    if type(value)==dict:
        if set(value)=={'ref','namespace','digest','protection'}:require(value['namespace']==namespace,'foreign protected namespace')
        for v in value.values():evidence_check(v,namespace)
    elif type(value)==list:
        for v in value:evidence_check(v,namespace)
def key_check(key):
    require((key['generation'] is None)==(key['generationEvidence'] is None),'generation evidence mismatch')
def incoming_key(state,scope_id,key,actor,purpose,now):
    key_check(key)
    e=key['generationEvidence']
    if e is None:return
    if e['basis']=='steward-attested':
        require(e['assertedBy']==actor and permitted(state,actor,scope_id,purpose,'map',now),'steward generation authority')
    else:require(e['assertedBy']==state['scopes'][scope_id]['sourceId'],'source generation attribution')
def lineage(state,scope_id,key):
    key_check(key)
    if key['generation'] is None:return None
    scope=state['scopes'][scope_id];source=state['sources'][scope['sourceId']]
    return [source['id'],source['generation'],scope['resource'],scope['scheme'],scope['schemeVersion'],key['value'],key['generation']]
def eligible_mapping(state,mapping):
    c=state['catalogue'];scope=state['scopes'][mapping['scopeId']]
    return c is not None and any(x['id']==mapping['targetId'] and x['kind']==mapping['expectedTargetKind'] for x in c['subjects']) and {'sourceKind':scope['sourceObjectKind'],'targetKind':mapping['expectedTargetKind'],'purpose':mapping['purpose']} in c['pairs']
def mapping_outcome(state,scope_id,item,purpose):
    lin=lineage(state,scope_id,item['key'])
    if lin is None:return {'status':'continuity-unknown','pin':None}
    matches=[h[-1] for h in state['mappings'].values() if h[-1]['lineage']==lin and h[-1]['definition']['scopeId']==scope_id and h[-1]['definition']['purpose']==purpose and h[-1]['state']=='active']
    require(len(matches)<=1,'ambiguous active mappings')
    if not matches:return {'status':'unmapped','pin':None}
    m=matches[0];definition=m['definition']
    if state['scopes'][scope_id]['sourceObjectKind']!=state['scopes'][definition['scopeId']]['sourceObjectKind'] or not eligible_mapping(state,definition) or not within(item['observedAt'],definition['validFrom'],definition['validTo']):
        return {'status':'active-pin-suspended','pin':None}
    return {'status':'mapped','pin':{'mappingId':definition['id'],'revision':m['revision'],'catalogueRevision':state['catalogue']['revision'],'policyRevision':state['policy']['revision']}}
def occurrence_by_id(state,oid,scope,purpose):
    return next((x for b in state['batches'].values() if b['content']['scopeId']==scope and b['content']['purpose']==purpose for x in b['occurrences'] if x['id']==oid),None)
def event_id(state,seq,suffix):return state['config']['registerId']+':'+str(seq)+':'+suffix

def record_conflict(state,body,actor,now,seq):
    """Internal compact observation; never accepted as a public command."""
    validate('ConflictRecord',body)
    require(permitted(state,actor,body['scopeId'],body['purpose'],'intake',now),'conflict admission right')
    e=state['epochs'].get(body['epochId']);require(e is not None and e['status']=='open' and e['scopeId']==body['scopeId'],'conflict epoch')
    old=state['batches'].get(digest([body['scopeId'],body['epochId'],body['batchKey']]))
    reason=('principal-collision' if old['actor']!=actor else 'changed-content' if old['contentDigest']!=body['suppliedDigest'] else None) if old else ('stale-head' if e['head']!=body['expectedHead'] else 'stale-fence' if e['fence']!=body['fence'] else None)
    require(reason is not None and reason==body['reason'],'unsubstantiated conflict observation')
    count=sum(x['actor']==actor and x['scopeId']==body['scopeId'] and x['epochId']==body['epochId'] for x in state['conflicts'])
    if seq>MAX_EVENTS or len(state['conflicts'])>=MAX_CONFLICTS or count>=MAX_CONFLICTS_PER_WRITER_SCOPE_EPOCH:return deepcopy(DENIED),False
    state['conflicts'].append({'id':event_id(state,seq,'conflict'),'scopeId':body['scopeId'],'epochId':body['epochId'],'attemptId':body['attemptId'],'actor':actor,'recordedAt':now,'sequence':seq,'reason':reason,'suppliedDigest':body['suppliedDigest'],'retainedDigest':old['contentDigest'] if old else None})
    return deepcopy(DENIED),True

def compact_conflict(body,reason):
    c=body['content']
    return {**{k:c[k] for k in ('scopeId','epochId','batchKey','purpose')},**{k:body[k] for k in ('attemptId','expectedHead','fence')},'suppliedDigest':digest(c),'reason':reason}

def apply(state,command,actor,now,seq):
    """Trusted host reducer. Return result + whether a journal entry is retained."""
    time(now)
    op=command.get('op') if type(command)==dict else None
    body=command.get('body') if type(command)==dict else None
    admin=actor==state['config']['admin']
    # Authorization precedes schema diagnostics and any receipt lookup.
    if op in ('source','scope','catalogue','policy','epoch-open','epoch-close','fence'):
        if not admin:return deepcopy(DENIED),False
    elif op in ('commit','round-open','round-seal','mapping','mapping-state'):
        try:
            if op=='commit':scope,purpose=body['content']['scopeId'],body['content']['purpose']
            elif op=='mapping-state':m=state['mappings'][body['id']][-1]['definition'];scope,purpose=m['scopeId'],m['purpose']
            elif op=='round-seal':r=state['rounds'][body['id']]['definition'];scope,purpose=r['scopeId'],r['purpose']
            else:scope,purpose=body['scopeId'],body['purpose']
            if not permitted(state,actor,scope,purpose,'map' if op.startswith('mapping') else 'intake',now):return deepcopy(DENIED),False
        except (KeyError,TypeError):return deepcopy(DENIED),False
    else:return deepcopy(DENIED),False
    validate('Command',command);evidence_check(body,state['config']['protectedNamespace'])
    if op=='source':
        require(body['id'] not in state['sources'],'source identity exists')
        require(not any((s['tenant'],s['environment'],s['productRef'],s['generation'])==(body['tenant'],body['environment'],body['productRef'],body['generation']) for s in state['sources'].values()),'duplicate declared source identity')
        state['sources'][body['id']]=deepcopy(body)
    elif op=='scope':
        require(body['id'] not in state['scopes'] and body['sourceId'] in state['sources'],'scope/source identity')
        fingerprint=digest({k:v for k,v in body.items() if k!='id'})
        require(all(s['fingerprint']!=fingerprint for s in state['scopes'].values()),'duplicate scope')
        state['scopes'][body['id']]={**deepcopy(body),'fingerprint':fingerprint}
    elif op in ('policy','catalogue'):
        previous=state[op];require(body['revision']==(previous['revision']+1 if previous else 1),'configuration revision')
        if op=='policy':
            for g in body['grants']:require(time(g['validFrom'])<time(g['validTo']),'grant window')
        else:require(len({s['id'] for s in body['subjects']})==len(body['subjects']),'duplicate target')
        state[op]=deepcopy(body)
    elif op=='mapping':
        existing=state['mappings'].get(body['id'])
        if existing and (existing[-1]['definition']['scopeId'],existing[-1]['definition']['purpose'])!=(body['scopeId'],body['purpose']):return deepcopy(DENIED),False
        require(body['id'] not in state['mappings'] and body['scopeId'] in state['scopes'],'mapping identity')
        incoming_key(state,body['scopeId'],body['key'],actor,body['purpose'],now)
        require(body['issuer']==actor,'mapping issuer must be authenticated steward')
        require(body['key']['generation'] is not None,'unknown generation cannot map')
        time(body['validFrom']);require(body['validTo'] is None or time(body['validFrom'])<time(body['validTo']),'mapping window')
        if body['corrects'] is not None:
            old=state['mappings'].get(body['corrects'])
            if old is None or old[-1]['definition']['scopeId']!=body['scopeId'] or old[-1]['definition']['purpose']!=body['purpose']:return deepcopy(DENIED),False
            require(old[-1]['lineage']==lineage(state,body['scopeId'],body['key']),'mapping correction lineage')
        require(eligible_mapping(state,body),'target kind or aboutness policy')
        state['mappings'][body['id']]=[{'definition':deepcopy(body),'lineage':lineage(state,body['scopeId'],body['key']),'revision':1,'state':'proposed','recordedAt':now,'sequence':seq,'actor':actor,'reason':'proposal','catalogueRevision':state['catalogue']['revision']}]
    elif op=='mapping-state':
        h=state['mappings'][body['id']];old=h[-1];require(old['revision']==body['expectedRevision'],'mapping revision')
        transitions={'proposed':{'active','disputed','retracted'},'active':{'disputed','retracted'},'disputed':{'active','retracted'},'retracted':set()}
        require(body['to'] in transitions[old['state']],'mapping transition')
        if body['to']=='active':
            require(eligible_mapping(state,old['definition']),'target kind or aboutness policy')
            if any(x[-1]['state']=='active' and x[-1]['lineage']==old['lineage'] and x[-1]['definition']['purpose']==old['definition']['purpose'] and x[-1]['definition']['scopeId']!=old['definition']['scopeId'] for x in state['mappings'].values()):return deepcopy(DENIED),False
            require(not any(x[-1]['state']=='active' and x[-1]['lineage']==old['lineage'] and x[-1]['definition']['purpose']==old['definition']['purpose'] for mid,x in state['mappings'].items() if mid!=body['id']),'active mapping already exists')
            previous=old['definition']['corrects']
            require(previous is None or state['mappings'][previous][-1]['state']=='retracted','corrected claim not retracted')
        h.append({**deepcopy(old),'revision':old['revision']+1,'state':body['to'],'recordedAt':now,'sequence':seq,'actor':actor,'reason':body['reason'],'catalogueRevision':state['catalogue']['revision']})
    elif op=='epoch-open':
        require(body['id'] not in state['epochs'] and body['scopeId'] in state['scopes'],'epoch identity')
        require(not any(e['scopeId']==body['scopeId'] and e['status']=='open' for e in state['epochs'].values()),'scope already has open epoch')
        state['epochs'][body['id']]={**deepcopy(body),'status':'open','head':None,'fence':1,'progress':0,'openedAt':now,'openedSequence':seq,'closedAt':None,'closedSequence':None}
    elif op in ('epoch-close','fence'):
        e=state['epochs'].get(body['id']);require(e is not None and e['status']=='open','epoch not open')
        if op=='fence':require(body['expectedFence']==e['fence'],'stale fence');e['fence']+=1
        else:
            require(not any(r['definition']['epochId']==body['id'] and not r['sealed'] for r in state['rounds'].values()),'seal open rounds, including partial evidence, before epoch close')
            e.update(status='closed',closedAt=now,closedSequence=seq,closeReason=body['reason'])
    elif op=='round-open':
        if (body['consistency']=='source-snapshot' or body['visibilityCovered']) and not permitted(state,actor,body['scopeId'],body['purpose'],'attest-coverage',now):return deepcopy(DENIED),False
        existing=state['rounds'].get(body['id'])
        if existing and (existing['definition']['scopeId'],existing['definition']['purpose'])!=(body['scopeId'],body['purpose']):return deepcopy(DENIED),False
        require(body['id'] not in state['rounds'],'round exists')
        e=state['epochs'].get(body['epochId']);require(e is not None and e['status']=='open' and e['scopeId']==body['scopeId'],'round epoch')
        require((body['previousRoundId'] is None)==(body['notEarlierEvidence'] is None),'round order evidence')
        if body['previousRoundId'] is not None:
            old=state['rounds'].get(body['previousRoundId']);require(old is not None and old['sealed'] and old['definition']['scopeId']==body['scopeId'],'round predecessor')
        state['rounds'][body['id']]={'definition':deepcopy(body),'pages':[],'sealed':False,'errors':[],'openedSequence':seq,'sealedSequence':None,'complete':False}
    elif op=='round-seal':
        r=state['rounds'][body['id']];require(not r['sealed'],'round already sealed')
        d=r['definition']
        if not body['errors'] and (d['consistency']=='source-snapshot' or d['visibilityCovered']) and not permitted(state,actor,d['scopeId'],d['purpose'],'attest-coverage',now):return deepcopy(DENIED),False
        pages=[state['batches'][p] for p in r['pages']]
        r.update(sealed=True,errors=deepcopy(body['errors']),sealedSequence=seq)
        r['complete']=bool(pages and pages[-1]['content']['terminal'] and not body['errors'] and all(not b['quarantine'] and all(o['key']['generation'] is not None and o['operation']=='snapshot-read' for o in b['occurrences']) for b in pages))
    elif op=='commit':
        c=body['content'];e=state['epochs'].get(c['epochId'])
        if e is None or e['status']!='open' or e['scopeId']!=c['scopeId']:return deepcopy(DENIED),False
        slot=digest([c['scopeId'],c['epochId'],c['batchKey']]);cd=digest(c);old=state['batches'].get(slot)
        def conflict(reason):
            return record_conflict(state,compact_conflict(body,reason),actor,now,seq)
        if old is not None:
            if old['actor']!=actor:return conflict('principal-collision')
            if old['contentDigest']!=cd:return conflict('changed-content')
            if encode(old['content'])!=encode(c):return deepcopy(DENIED),False
            return {'status':'committed','receiptId':old['id']},False
        if e['head']!=body['expectedHead']:return conflict('stale-head')
        if e['fence']!=body['fence']:return conflict('stale-fence')
        require(c['empty']==(len(c['items'])==0),'empty declaration')
        if c['roundId'] is None:require(c['pageIndex'] is None and not c['terminal'],'round/page mismatch')
        else:
            r=state['rounds'].get(c['roundId']);require(r is not None and not r['sealed'],'round not open')
            d=r['definition'];require((d['scopeId'],d['epochId'],d['purpose'])==(c['scopeId'],c['epochId'],c['purpose']),'round context')
            if c['terminal'] and (d['consistency']=='source-snapshot' or d['visibilityCovered']) and not permitted(state,actor,c['scopeId'],c['purpose'],'attest-coverage',now):return deepcopy(DENIED),False
            require(c['pageIndex']==len(r['pages']),'page chain gap')
            require(not r['pages'] or not state['batches'][r['pages'][-1]]['content']['terminal'],'page after terminal')
        rid=event_id(state,seq,'receipt');occ=[];quarantine=[]
        for ordinal,item in enumerate(c['items']):
            if item['kind']=='quarantine':quarantine.append({**deepcopy(item),'id':rid+':quarantine:'+str(ordinal),'ordinal':ordinal,'state':'open'});continue
            incoming_key(state,c['scopeId'],item['key'],actor,c['purpose'],now);time(item['observedAt'])
            if item['sourceEventTime'] is not None:time(item['sourceEventTime'])
            correction=item['correction']
            if correction is not None:
                if not permitted(state,actor,c['scopeId'],c['purpose'],'map',now) or not permitted(state,actor,c['scopeId'],c['purpose'],'read',now):return deepcopy(DENIED),False
                prev=occurrence_by_id(state,correction['occurrenceId'],c['scopeId'],c['purpose'])
                if prev is None:return deepcopy(DENIED),False
                require(prev['lineage'] is not None and prev['lineage']==lineage(state,c['scopeId'],item['key']),'correction lineage')
                asserted=state['scopes'][c['scopeId']]['sourceId'] if correction['basis']=='source-asserted' else actor
                require(correction['assertedBy']==asserted,'correction attribution mismatch')
            outcome=mapping_outcome(state,c['scopeId'],item,c['purpose'])
            occ.append({**deepcopy(item),'id':rid+':occurrence:'+str(ordinal),'ordinal':ordinal,'lineage':lineage(state,c['scopeId'],item['key']),'mapping':outcome,'recordedAt':now,'sequence':seq})
        receipt={'id':rid,'content':deepcopy(c),'contentDigest':cd,'actor':actor,'attemptId':body['attemptId'],'committedAt':now,'sequence':seq,'previousHead':e['head'],'fence':e['fence'],'progress':e['progress']+1,'policyRevision':state['policy']['revision'],'occurrences':occ,'quarantine':quarantine,'received':len(c['items']),'accepted':len(occ),'quarantined':len(quarantine)}
        require(receipt['received']==receipt['accepted']+receipt['quarantined'],'conservation')
        state['batches'][slot]=receipt;e.update(head=rid,progress=e['progress']+1)
        if c['roundId'] is not None:state['rounds'][c['roundId']]['pages'].append(slot)
        return {'status':'committed','receiptId':rid},True
    return {'status':'recorded'},True

def replay(config,events,build_id=None):
    require((BUILD_ID if build_id is None else build_id)==BUILD_ID,'unsupported reducer/schema build; migration required')
    require(type(events)==list and len(events)<=MAX_EVENTS,'event budget')
    state=initial(config);previous=digest({'config':config,'buildId':BUILD_ID});last=None
    for seq,event in enumerate(events,1):
        validate('JournalEvent',event)
        require(set(event)=={'sequence','previousDigest','actor','recordedAt','command','result','outcomeDigest','digest'},'event fields')
        require(event['sequence']==seq and event['previousDigest']==previous,'event chain')
        require(last is None or time(event['recordedAt'])>=time(last),'host recorded time moved backwards')
        expected=digest({k:v for k,v in event.items() if k!='digest'});require(event['digest']==expected,'event digest')
        cmd=event['command']
        result,retained=record_conflict(state,cmd['body'],event['actor'],event['recordedAt'],seq) if cmd['op']=='conflict-observation' else apply(state,cmd,event['actor'],event['recordedAt'],seq)
        require(retained and encode(result)==encode(event['result']) and digest(state)==event['outcomeDigest'],'event outcome/state digest')
        previous=expected;last=event['recordedAt']
    return state,previous

class Register:
    def __init__(self,path,config=None):
        self.path=Path(path)
        if config is not None:
            initial(config)
            with self.path.open('xb'):pass
        require(config is not None or self.path.is_file(),'explicit bootstrap required')
        require(config is not None or self.path.stat().st_size>0,'uninitialized store; preserve and inspect, or bootstrap a different path')
        self.db=sqlite3.connect(str(self.path),timeout=10,isolation_level=None)
        self.db.execute('PRAGMA journal_mode=DELETE');self.db.execute('PRAGMA synchronous=FULL')
        if config is not None:
            try:
                self.db.execute('BEGIN IMMEDIATE')
                require(not self.db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall(),'new empty store required')
                self.db.execute('CREATE TABLE bootstrap (id INTEGER PRIMARY KEY CHECK(id=1), body BLOB NOT NULL)')
                self.db.execute('CREATE TABLE journal (seq INTEGER PRIMARY KEY, body BLOB NOT NULL)')
                self.db.execute('INSERT INTO bootstrap VALUES (1,?)',(encode({'config':config,'buildId':BUILD_ID}),));self.db.commit()
            except BaseException:self.db.rollback();raise
        raw=self.db.execute('SELECT body FROM bootstrap WHERE id=1').fetchone()[0];bootstrap=decode(raw)
        try:
            require(set(bootstrap)=={'config','buildId'} and bootstrap['buildId']==BUILD_ID,'unsupported store build; migration required')
            require(encode(bootstrap)==raw,'noncanonical stored bootstrap')
            self.config=bootstrap['config'];self.build_id=bootstrap['buildId'];initial(self.config)
        except BaseException:self.db.close();raise
    def close(self):self.db.close()
    def _events(self):
        out=[]
        for row in self.db.execute('SELECT body FROM journal ORDER BY seq'):
            value=decode(row[0]);require(encode(value)==row[0],'noncanonical stored event');out.append(value)
        return out
    def execute(self,command,actor,now,*,fault=None):
        """actor/now are verified host inputs. Fault hook is test-only."""
        try:
            self.db.execute('BEGIN IMMEDIATE');events=self._events();state,root=replay(self.config,events,self.build_id)
            require(not events or time(now)>=time(events[-1]['recordedAt']),'host clock rollback')
            result,retained=apply(state,command,actor,now,len(events)+1)
            if retained:
                require(len(events)<MAX_EVENTS,'event budget')
                is_conflict=result==DENIED
                stored_command={'op':'conflict-observation','body':compact_conflict(command['body'],state['conflicts'][-1]['reason'])} if is_conflict else deepcopy(command)
                event={'sequence':len(events)+1,'previousDigest':root,'actor':actor,'recordedAt':now,'command':stored_command,'result':result,'outcomeDigest':digest(state)}
                event['digest']=digest(event)
                validate('JournalEvent',event)
                # Keep every committed cut exportable under the same byte budget.
                try:encode({'format':'vercy-source-sync-archive','version':VERSION,'buildId':self.build_id,'config':self.config,'events':events+[event],'state':state,'root':event['digest'],'resumable':False})
                except Invalid as error:
                    if is_conflict and str(error)=='byte budget':self.db.rollback();return deepcopy(DENIED)
                    raise
                self.db.execute('INSERT INTO journal VALUES (?,?)',(event['sequence'],encode(event)))
            if fault:fault('before-commit')
            self.db.commit()
            if fault:fault('after-commit')
            return deepcopy(result)
        except BaseException:self.db.rollback();raise
    def archive(self,actor):
        """Privileged full-store export, not a public/partial disclosure API."""
        require(actor==self.config['admin'],'full export requires host administrator')
        self.db.execute('BEGIN')
        try:
            events=self._events();state,root=replay(self.config,events,self.build_id)
            out={'format':'vercy-source-sync-archive','version':VERSION,'buildId':self.build_id,'config':self.config,'events':events,'state':state,'root':root,'resumable':False}
            encode(out);self.db.commit();return deepcopy(out)
        except BaseException:self.db.rollback();raise
    def read_receipt(self,scope,purpose,epoch,batch_key,actor,now):
        self.db.execute('BEGIN')
        try:
            state,_=replay(self.config,self._events(),self.build_id)
            if not permitted(state,actor,scope,purpose,'read',now):result=deepcopy(DENIED)
            else:
                receipt=state['batches'].get(digest([scope,epoch,batch_key]))
                result=deepcopy(receipt) if receipt and receipt['content']['purpose']==purpose else {'status':'not-found'}
            self.db.commit();return result
        except BaseException:self.db.rollback();raise

def validate_archive(archive):
    encode(archive)
    require(set(archive)=={'format','version','buildId','config','events','state','root','resumable'},'archive fields')
    require(archive['format']=='vercy-source-sync-archive' and archive['version']==VERSION,'unsupported archive version')
    require(archive['resumable'] is False,'archive is never resumable')
    state,root=replay(archive['config'],archive['events'],archive['buildId'])
    require(encode(state)==encode(archive['state']) and root==archive['root'],'archive derived state/root mismatch')
    return {'valid':True,'scope':'historical-consistency-only','resumable':False,'events':len(archive['events'])}

def assess_rounds(archive,earlier,later):
    """Privileged offline analysis of a complete restricted archive; no effects."""
    validate_archive(archive);s=archive['state'];a=s['rounds'].get(earlier);b=s['rounds'].get(later)
    if a is None or b is None:return {'status':'insufficient-context','candidates':[]}
    x,y=a['definition'],b['definition']
    ok=a['complete'] and b['complete'] and a['sealedSequence']<b['sealedSequence'] and x['scopeId']==y['scopeId'] and x['purpose']==y['purpose'] and x['consistency']==y['consistency']=='source-snapshot' and x['visibilityCovered'] and y['visibilityCovered'] and y['previousRoundId']==earlier and y['notEarlierEvidence'] is not None
    if not ok:return {'status':'insufficient-context','candidates':[]}
    def observed(r):return {digest(o['lineage']):o for slot in r['pages'] for o in s['batches'][slot]['occurrences']}
    old,new=observed(a),observed(b);candidates=[];explicit=[]
    for key,o in old.items():
        if key in new:continue
        unavailable=[p for receipt in s['batches'].values() if receipt['content']['scopeId']==x['scopeId'] and receipt['content']['purpose']==x['purpose'] and a['sealedSequence']<receipt['sequence']<=b['sealedSequence'] for p in receipt['occurrences'] if p['lineage']==o['lineage'] and p['operation'] in ('source-deleted','removed-from-scope','inaccessible')]
        if unavailable:
            latest=max(unavailable,key=lambda p:(p['sequence'],p['ordinal']))
            explicit.append({'lineage':o['lineage'],'operation':latest['operation'],'evidenceOccurrence':latest['id']})
        else:candidates.append({'conclusion':'not-observed-in-comparable-rounds','lineage':o['lineage'],'earlierRound':earlier,'laterRound':later,'permittedAction':'steward-review-only'})
    return {'status':'assessed','candidates':candidates,'explicitAvailabilityEvidence':explicit,'effects':[]}

def resume_archive(_):raise Invalid('Archive resume refused; new local acquisition baseline required')

def inspect_import(raw):
    """Read-only import report; never creates a database or grants live authority."""
    try:
        archive=decode(raw);report=validate_archive(archive)
        return {**report,'status':'historical-only','lossReport':None}
    except (ValueError,TypeError,KeyError,ValidationError) as error:
        return {'valid':False,'status':'refused','resumable':False,'lossReport':{'code':'unsupported-or-inconsistent-archive','detail':str(error),'action':'retain original; supply an exact supported archive; no lossy conversion attempted'}}

def historical_cut(archive,known_at):
    """Privileged historical view. Current disclosure must be enforced by its host."""
    validate_archive(archive);time(known_at)
    events=[e for e in archive['events'] if time(e['recordedAt'])<=time(known_at)]
    state,root=replay(archive['config'],events,archive['buildId'])
    return {'knownAt':known_at,'events':len(events),'root':root,'buildId':archive['buildId'],'state':state,'resumable':False}

PROFILE_ID='vr.profile.enterprise-source-synchronization'

def native_value(archive):
    validate_archive(archive)
    return {**{k:deepcopy(v) for k,v in archive.items() if k!='state'},'format':'vercy-source-sync-journal-snapshot'}

def archive_from_native(value):
    encode(value);Draft202012Validator(SCHEMA).validate(value)
    state,root=replay(value['config'],value['events'],value['buildId']);require(root==value['root'],'native journal root mismatch')
    return {**deepcopy(value),'format':'vercy-source-sync-archive','state':state}

def native_records(archive,captured_at,previous_fact=None):
    """Privileged restricted projection. Never imports or resumes a register."""
    validate_archive(archive);time(captured_at)
    config=archive['config'];oid=config['registerId'];root=archive['root'].split(':')[1]
    require(re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._:-]{2,159}',oid) is not None,'native register ID requires 3..160 safe characters; no automatic rewriting')
    require(not archive['events'] or time(captured_at)>=time(archive['events'][-1]['recordedAt']),'capture precedes journal')
    obj={'recordType':'object','schemaVersion':'1.0.0','recordId':oid+':object-r1','objectId':oid,'objectType':PROFILE_ID+':sync-register','name':'Source synchronization register','recordedAt':captured_at,'previousRecordId':None,'state':'active','provenance':{'source':oid,'dimensionId':config['dimensionId']},'accessClass':'restricted'}
    value=native_value(archive)
    fact={'recordType':'fact','schemaVersion':'1.0.0','factId':oid+':snapshot:'+root,'subjectId':oid,'path':'sync.register.snapshot','value':value,'unit':None,'validFrom':captured_at,'validTo':None,'recordedAt':captured_at,'supersedes':[] if previous_fact is None else [previous_fact['factId']],'status':'asserted','provenance':{'source':oid,'dimensionId':config['dimensionId'],'snapshotDigest':digest(value),'previousSnapshotDigest':None if previous_fact is None else digest(previous_fact['value'])},'authority':{'source':config['admin'],'rank':0},'masterSystem':oid,'accessClass':'restricted'}
    validate_native_snapshot(fact,previous_fact)
    return obj,fact

def validate_native_snapshot(fact,previous=None):
    """Run after native outer validation; caller provides trusted predecessor."""
    require(set(fact)=={'recordType','schemaVersion','factId','subjectId','path','value','unit','validFrom','validTo','recordedAt','supersedes','status','provenance','authority','masterSystem','accessClass'},'closed native snapshot profile')
    a=archive_from_native(fact['value']);config=a['config'];oid=config['registerId']
    require(fact['recordType']=='fact' and fact['schemaVersion']=='1.0.0' and fact['path']=='sync.register.snapshot','snapshot envelope')
    require(fact['subjectId']==oid and fact['factId']==oid+':snapshot:'+a['root'].split(':')[1] and fact['masterSystem']==oid,'snapshot identity')
    require(encode(fact['authority'])==encode({'source':config['admin'],'rank':0}) and fact['accessClass']=='restricted','snapshot storage authority/class')
    require(fact['status']=='asserted' and fact['unit'] is None and fact['validTo'] is None and fact['validFrom']==fact['recordedAt'],'snapshot times/status')
    time(fact['recordedAt']);require(not a['events'] or time(fact['recordedAt'])>=time(a['events'][-1]['recordedAt']),'capture precedes journal')
    expected={'source':oid,'dimensionId':config['dimensionId'],'snapshotDigest':digest(fact['value']),'previousSnapshotDigest':None if previous is None else digest(previous['value'])}
    require(fact['provenance']==expected,'snapshot provenance/digest')
    require(fact['supersedes']==([] if previous is None else [previous['factId']]),'snapshot predecessor')
    if previous is not None:
        old=archive_from_native(previous['value'])
        require(previous['subjectId']==oid and previous['path']=='sync.register.snapshot' and previous['factId']==oid+':snapshot:'+old['root'].split(':')[1],'predecessor identity')
        require(previous['provenance']['snapshotDigest']==digest(previous['value']),'predecessor digest')
        require(config==old['config'] and len(a['events'])>len(old['events']) and a['events'][:len(old['events'])]==old['events'],'snapshot must strictly extend exact predecessor')
        require(time(fact['recordedAt'])>=time(previous['recordedAt']),'capture time rollback')
    return {'valid':True,'scope':'historical-restricted-projection','resumable':False}
