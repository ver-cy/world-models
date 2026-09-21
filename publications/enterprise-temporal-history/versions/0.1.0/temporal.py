"""Bounded trusted-host bitemporal snapshots; no database, IAM or domain engine."""
from pathlib import Path
import copy,datetime,hashlib,json,re
from jsonschema import Draft202012Validator,FormatChecker
HERE=Path(__file__).resolve().parent
class Invalid(ValueError):pass
def require(ok,message):
    if not ok:raise Invalid(message)
def encode(x):
    try:return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode('utf-8')
    except (ValueError,TypeError,UnicodeError,RecursionError) as e:raise Invalid('Invalid JSON value') from e
def digest(x):return 'sha256:'+hashlib.sha256(encode(x)).hexdigest()
def load(p):return json.loads(Path(p).read_text(encoding='utf-8'))
SCHEMA=load(HERE/'temporal.schema.json')
def instant(t):
    require(type(t) is str and re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z',t) is not None,'Unsupported timestamp')
    try:datetime.datetime.strptime(t,'%Y-%m-%dT%H:%M:%SZ')
    except ValueError as e:raise Invalid('Invalid calendar instant') from e
    return t
def shape(x,kind):
    require(len(encode(x))<=8*1024*1024,'8 MiB limit exceeded')
    checker=FormatChecker()
    require('uri' in checker.checkers and 'date-time' in checker.checkers,'Required format checker unavailable')
    s={'$schema':SCHEMA['$schema'],'$defs':SCHEMA['$defs'],'$ref':'#/$defs/'+kind}
    errors=list(Draft202012Validator(s,format_checker=checker).iter_errors(x))
    require(not errors,'Closed schema violation: '+(errors[0].message if errors else ''))
    def walk(v):
        if isinstance(v,dict):
            for k,w in v.items():
                if k in {'validFrom','validUntil','validTo','recordedAt','sourceRecordedAt'} and w is not None:instant(w)
                if k=='sequence':require(type(w) is int,'Sequence must have integer JSON encoding')
                if k in {'digest','expectedHead','scopeDigest'} and w is not None:require(re.fullmatch(r'sha256:[0-9a-f]{64}',w) is not None,'Invalid digest encoding')
                if k=='version':require(re.fullmatch(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)',w) is not None,'Unsupported version grammar')
                walk(w)
        elif isinstance(v,list):
            for w in v:walk(w)
    walk(x)
def configuration(config,now):
    shape(config,'config');instant(now)
    require(config['validFrom']<config['validUntil'],'Empty configuration interval')
    require(config['validFrom']<=now<config['validUntil'],'Current configuration unavailable')
    for name in ['readers','purposes','acceptedSchemas','acceptedStates']:
        require(len({encode(x) for x in config[name]})==len(config[name]),'Duplicate configuration entry')
    # One definition per ID/version; exact bytes cannot silently change under the same schema/profile pin.
    pins=config['acceptedSchemas']+[x['profile'] for x in config['acceptedStates']]
    seen={}
    for p in pins:
        key=(p['id'],p['version']);require(key not in seen or seen[key]==p['digest'],'Repointed binding');seen[key]=p['digest']
    axes=set()
    for p in config['acceptedStates']:
        key=(encode(p['profile']),p['axis']);require(key not in axes,'Duplicate state axis definition');axes.add(key)
        require(len(set(p['codes']))==len(p['codes']),'Duplicate state code')
def matching(ledger,config):
    require(isinstance(ledger,dict) and all(k in ledger for k in ['dimension','timeline','scope']),'Missing governed scope')
    for k in ['dimension','timeline','scope']:require(ledger[k]==config[k],'Wrong governed scope')
def head(ledger):return digest(ledger['commits'][-1]) if ledger['commits'] else None
def scope_digest(ledger):return digest({k:v for k,v in ledger.items() if k!='commits'})
def empty(config):return dict(format='vercy-enterprise-temporal',version='0.1.0',dimension=config['dimension'],timeline=config['timeline'],scope=copy.deepcopy(config['scope']),commits=[])
def segments(rows,config=None,retained=()):
    previous=None
    for s in rows:
        if s['validTo'] is not None:require(s['validFrom']<s['validTo'],'Empty/reversed interval')
        if previous is not None:require(previous['validTo'] is not None and previous['validTo']<=s['validFrom'],'Unsorted/overlapping intervals')
        previous=s
        if config is not None and encode(s) not in {encode(x) for x in retained}:
            require(s['schema'] in config['acceptedSchemas'],'Unaccepted schema binding')
            if s['state'] is not None:
                state=s['state'];require(any(state['profile']==r['profile'] and state['axis']==r['axis'] and state['code'] in r['codes'] for r in config['acceptedStates']),'Unaccepted state vocabulary binding')
def validate_ledger(ledger,*,now):
    """Structural history only; this cannot establish historical writer authorization."""
    shape(ledger,'ledger');instant(now);keys=set();revisions=set();last=None;pin_definitions={};value_definitions={}
    for i,c in enumerate(ledger['commits'],1):
        q=c['request'];require(c['sequence']==i,'Non-contiguous receipt sequence')
        require(c['scopeDigest']==scope_digest(ledger),'History transplanted to another scope/header')
        require(c['recordedAt']<=now,'Future receipt')
        require(last is None or c['recordedAt']>=last['recordedAt'],'Receipt clock moved backwards')
        require(q['expectedHead']==(digest(last) if last else None),'Broken head chain')
        require(q['key'] not in keys and q['revision'] not in revisions,'Reused commit identity');keys.add(q['key']);revisions.add(q['revision'])
        require(q['sourceRecordedAt'] is None or q['sourceRecordedAt']<=c['recordedAt'],'Source record time after receipt')
        require(q['operation']==('record' if last is None else q['operation']) and (last is None or q['operation']!='record'),'Wrong genesis operation')
        if last is not None:require(last['request']['operation']!='archive','Archive is terminal')
        if q['operation']=='archive':require(last is not None and encode(q['segments'])==encode(last['request']['segments']),'Archive rewrites timeline')
        segments(q['segments'])
        for s in q['segments']:
            v=s['value'];vk=(v['id'],v['revision']);require(vk not in value_definitions or value_definitions[vk]==v['digest'],'Payload revision repointed');value_definitions[vk]=v['digest']
            for b in [s['schema']]+([] if s['state'] is None else [s['state']['profile']]):
                k=(b['id'],b['version']);require(k not in pin_definitions or pin_definitions[k]==b['digest'],'Binding repointed across history');pin_definitions[k]=b['digest']
        last=c
    return True
def validate_extension(old,new,*,now):
    validate_ledger(old,now=now);validate_ledger(new,now=now)
    require(encode({k:v for k,v in old.items() if k!='commits'})==encode({k:v for k,v in new.items() if k!='commits'}),'Scope/header changed')
    require(len(new['commits'])>=len(old['commits']) and encode(new['commits'][:len(old['commits'])])==encode(old['commits']),'History rewritten/truncated')
    return True
def admit(ledger,request,config,*,actor,now):
    """Pure function. Host selects trusted current config/root, actor and clock; serializes persistence."""
    configuration(config,now);require(actor==config['writer'],'Write denied')
    matching(ledger,config);validate_ledger(ledger,now=now);shape(request,'request')
    # Repeat is checked before expected-head and archive guards; first receipt is retained.
    for c in ledger['commits']:
        if c['request']['key']==request['key']:
            require(c['writer']==actor and encode(c['request'])==encode(request),'Conflicting replay')
            return copy.deepcopy(ledger)
    require(request['expectedHead']==head(ledger),'Head conflict')
    require(not ledger['commits'] or ledger['commits'][-1]['request']['operation']!='archive','Archive is terminal')
    retained=ledger['commits'][-1]['request']['segments'] if ledger['commits'] else []
    segments(request['segments'],config,retained)
    result=copy.deepcopy(ledger);result['commits'].append(dict(sequence=len(ledger['commits'])+1,recordedAt=now,writer=actor,scopeDigest=scope_digest(ledger),request=copy.deepcopy(request)))
    validate_extension(ledger,result,now=now)
    return result
def resolve(ledger,config,*,actor,purpose,validAt,knownAt,now,knownSequence=None):
    configuration(config,now)
    require(actor in config['readers'] and purpose in config['purposes'],'Read denied')
    matching(ledger,config);validate_ledger(ledger,now=now);instant(validAt);instant(knownAt)
    require(knownAt<=now,'Future knowledge cutoff')
    require(knownSequence is None or type(knownSequence) is int and 0<=knownSequence<=len(ledger['commits']),'Invalid knowledge sequence')
    known=[c for c in ledger['commits'] if c['recordedAt']<=knownAt and (knownSequence is None or c['sequence']<=knownSequence)]
    c=known[-1] if known else None
    result={'status':'insufficient-context','missing':['No registered timeline at this knowledge cutoff'] if c is None else ['No segment covers this valid instant'],'validAt':validAt,'knownAt':knownAt,'knownSequence':knownSequence,'commit':None if c is None else {'revision':c['request']['revision'],'sequence':c['sequence'],'recordedAt':c['recordedAt'],'digest':digest(c)},'segment':None,'archivedAsKnown':False if c is None else c['request']['operation']=='archive','archiveNow':bool(ledger['commits'] and ledger['commits'][-1]['request']['operation']=='archive'),'inputDigest':digest(ledger),'policyDigest':digest(config),'truth':'not-evaluated','domainValidation':'not-executed','transitionLegality':'not-evaluated'}
    if c:
        for s in c['request']['segments']:
            if s['validFrom']<=validAt and (s['validTo'] is None or validAt<s['validTo']):result.update(status='recorded-assertion',missing=[],segment=copy.deepcopy(s));break
    return result
def migrate(ledger,target,*,now):
    validate_ledger(ledger,now=now);require(target=='0.1.0','Unsupported migration/downgrade; retain full history');return json.loads(encode(ledger))
def snapshot_envelope(fact,*,dimension,now):
    """Check one native storage envelope, independently of its predecessor's availability."""
    require(isinstance(fact,dict) and all(k in fact for k in ['factId','path','value','subjectId','provenance','supersedes','status','unit','recordedAt','validFrom','validTo']),'Incomplete snapshot envelope')
    require(isinstance(fact['provenance'],dict) and all(k in fact['provenance'] for k in ['snapshotDigest','previousSnapshotDigest']),'Incomplete snapshot provenance')
    require(fact['path']=='temporal.timeline.snapshot','Wrong native path');ledger=fact['value'];validate_ledger(ledger,now=now)
    require(ledger['dimension']==dimension,'Wrong native Dimension')
    require(fact['status']=='asserted' and fact['unit'] is None and fact['validTo'] is None,'Unsupported snapshot envelope state')
    instant(fact['recordedAt']);instant(fact['validFrom'])
    require(fact['validFrom']==fact['recordedAt'] and fact['recordedAt']<=now,'Invalid snapshot receipt envelope')
    require(not ledger['commits'] or ledger['commits'][-1]['recordedAt']<=fact['recordedAt'],'Snapshot precedes inner receipt')
    require(fact['subjectId']==ledger['timeline'],'Wrong timeline subject')
    require(fact['provenance']['snapshotDigest']==digest(ledger),'Snapshot digest mismatch')
    return ledger

def validate_snapshot(fact,*,dimension,now,previous=None):
    """Additional semantic check AFTER native envelope validation; requires trusted previous snapshot."""
    ledger=snapshot_envelope(fact,dimension=dimension,now=now)
    if previous is None:
        require(fact['supersedes']==[] and fact['provenance']['previousSnapshotDigest'] is None,'Unexpected predecessor')
    else:
        snapshot_envelope(previous,dimension=dimension,now=now)
        require(fact['recordedAt']>=previous['recordedAt'],'Snapshot receipt precedes predecessor')
        require(fact['factId']!=previous['factId'] and fact['supersedes']==[previous['factId']],'Wrong snapshot predecessor identity')
        require(fact['provenance']['previousSnapshotDigest']==digest(previous['value']),'Wrong previous snapshot digest')
        validate_extension(previous['value'],ledger,now=now)
    return True
