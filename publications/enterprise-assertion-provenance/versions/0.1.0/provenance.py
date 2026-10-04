"""Original bounded trusted-host reference; no IAM, fetching or truth inference."""
from pathlib import Path
from datetime import datetime
import copy,hashlib,json,re
from jsonschema import Draft202012Validator,FormatChecker,ValidationError
HERE=Path(__file__).resolve().parent
VERSION='0.1.0'
class Invalid(ValueError):pass
class Denied(PermissionError):pass
def require(ok,message):
    if not ok:raise Invalid(message)
def load(path):return json.loads(Path(path).read_text(encoding='utf-8'))
def encode(value):
    try:raw=json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode('utf-8')
    except (TypeError,ValueError,UnicodeError,RecursionError) as e:raise Invalid('Not bounded JSON') from e
    require(len(raw)<=8*1024*1024,'Serialized JSON exceeds 8 MiB')
    return raw
def digest(value):return 'sha256:'+hashlib.sha256(encode(value)).hexdigest()
def pin(row):return {'id':row['id'],'revision':row['revision'],'digest':digest(row)}
SCHEMA=load(HERE/'provenance.schema.json')
SCHEME={k:SCHEMA['x-confidenceScheme'][k] for k in ['id','revision']}|{'digest':digest(SCHEMA['x-confidenceScheme'])}
def validate(value,kind=None):
    encode(value)
    require(kind is None or kind in SCHEMA['$defs'],'Unknown record type')
    checker=FormatChecker()
    require(all(k in checker.checkers for k in ['uri','date-time']),'Required URI/date-time format checker unavailable')
    todo=[value]
    while todo:
        item=todo.pop()
        if isinstance(item,dict):
            for k,v in item.items():
                if k=='revision':require(type(v) is int,'Revision must be a JSON integer without a fractional encoding')
                if k in ['recordedAt','obtainedAt','startedAt','endedAt','validFrom','validUntil']:instant(v)
                todo.append(v)
        elif isinstance(item,list):todo.extend(item)
    schema=SCHEMA if kind is None else {'$schema':SCHEMA['$schema'],'$defs':SCHEMA['$defs'],'$ref':'#/$defs/'+kind}
    try:Draft202012Validator(schema,format_checker=checker).validate(value)
    except (ValidationError,RecursionError) as e:raise Invalid('Schema mismatch') from e
def instant(s):
    require(isinstance(s,str) and re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z',s) is not None,'ASCII UTC instant required')
    try:return datetime.strptime(s,'%Y-%m-%dT%H:%M:%SZ')
    except ValueError as e:raise Invalid('Invalid UTC time') from e
def config_check(config,now):
    validate(config,'configuration');instant(now)
    require(config['validFrom']<config['validUntil'],'Empty configuration interval')
    if not config['validFrom']<=now<config['validUntil']:raise Denied('Access denied')
def gate(config,actor,purpose,now):
    try:config_check(config,now)
    except Denied:raise Denied('Read denied') from None
    if actor not in config['readers'] or purpose not in config['purposes']:raise Denied('Read denied')
def ref_slots(r):
    k=r['kind']
    if k=='Activity':return {'inputs':r['inputs']}
    if k=='ProvenanceRecord':return {'activity':[] if r['activity'] is None else [r['activity']]}
    if k=='EvidenceLink':return {'evidence':[r['evidence']]}
    if k=='ConfidenceAssessment':return {'account':[r['account']],'activity':[r['activity']],'basis':r['basis']}
    return {}
def refs(r):return [p for pins in ref_slots(r).values() for p in pins]
ANCHORS={
'Capture':['sourceRef','sourceVersion','aboutRef','obtainedAt','mode','availability','representationDigest'],
'Activity':['actor','mode','startedAt','endedAt','inputs','observedTarget','method'],
'ProvenanceRecord':['claim','aboutRef','asserter','epistemicKind'],
'EvidenceLink':['claim','evidence','attributedTo','relation'],
'ConfidenceAssessment':['account','assessor','method','scheme','purpose'],
}
def semantic(r,prior,heads,old=None):
    retained={(field,encode(p)) for field,pins in ref_slots(old).items() for p in pins} if old else set()
    new_judgement=r['kind']=='ConfidenceAssessment' and r['label']!='insufficient' and (old is None or any(r[f]!=old[f] for f in ['label','basis','activity']))
    if new_judgement:
        retained=set()
        if old is not None:require(r['activity']['id']!=old['activity']['id'],'Changed reliance judgement needs a fresh review activity ID')
    def resolve(p,types=None,current=None,field=None):
        target=prior.get((p['id'],p['revision']))
        require(target is not None and pin(target)==p,'Unresolved exact internal pin')
        require(target['scope']==r['scope'],'Cross-scope internal link')
        if current is None:current=(field,encode(p)) not in retained
        require(target['state']=='active','Reliance target was already withdrawn')
        if current:require(pin(heads[p['id']])==p,'New link to inactive or superseded revision')
        require(types is None or target['kind'] in types,'Wrong internal target type')
        return target
    k=r['kind']
    for field,pins in ref_slots(r).items():
        for p in pins:resolve(p,field=field)
    # Revision pins form a DAG; additionally reject self-support through a
    # previous revision of this same semantic identity.
    todo=list(refs(r));visited=set()
    while todo:
        p=todo.pop();key=(p['id'],p['revision'])
        require(p['id']!=r['id'],'Self-derivation across revisions')
        if new_judgement:
            target=prior[key];head=heads[p['id']]
            require(pin(head)==p and head['state']=='active','Changed reliance judgement has stale or withdrawn dependencies')
            require(target['kind']!='Capture' or (target['availability']=='captured' and target['integrity']!='mismatched'),'Changed reliance judgement has unavailable or mismatched capture')
        if key not in visited:
            visited.add(key);todo.extend(refs(prior[key]))
    if k=='Capture':
        require(r['obtainedAt']<=r['recordedAt'],'Capture after receipt')
        require((r['availability']=='captured')==(r['representationDigest'] is not None),'Capture digest/availability mismatch')
        require(r['availability']=='captured' or r['integrity']=='not-tested','Unavailable capture cannot have checked integrity')
    elif k=='Activity':
        require(r['startedAt']<=r['endedAt']<=r['recordedAt'],'Activity time mismatch')
        inputs=[resolve(p,['Capture','ProvenanceRecord'],field='inputs') for p in r['inputs']]
        for source in inputs:
            available_at=source['obtainedAt'] if source['kind']=='Capture' else None
            if source['kind']=='ProvenanceRecord' and source['activity'] is not None:
                producer=prior[(source['activity']['id'],source['activity']['revision'])]
                available_at=producer['endedAt']
            require(available_at is None or available_at<=r['endedAt'],'Input event follows consuming activity')
        if r['mode'] in ['file-acquisition','live-observation']:
            require(bool(inputs) and all(x['kind']=='Capture' for x in inputs),'Acquisition requires captures')
            mode='live-api' if r['mode']=='live-observation' else 'file'
            require(all(x['mode']==mode and x['availability']=='captured' for x in inputs),'Acquisition mode mismatch')
            require(all(r['startedAt']<=x['obtainedAt']<=r['endedAt'] for x in inputs),'Capture outside activity')
        if r['mode']=='live-observation':
            require(r['observedTarget'] is not None and all(x['aboutRef']==r['observedTarget'] for x in inputs),'Observed target mismatch')
        else:require(r['observedTarget'] is None,'Only live observation declares observed target')
        if r['mode'] in ['synthesis','review']:require(bool(inputs),'Analysis needs inputs')
        if r['mode']=='review':require(all(x['kind']=='ProvenanceRecord' for x in inputs),'Review targets accounts')
    elif k=='ProvenanceRecord':
        if r['epistemicKind']=='unverified':require(bool(r['limitations']),'Unverified account needs explicit limitations')
        else:require(r['activity'] is not None,'Account needs generating activity')
        if r['activity'] is not None:
            a=resolve(r['activity'],['Activity'],field='activity')
            expected={'observed':['live-observation'],'source-asserted':['file-acquisition','live-observation'],'inferred':['synthesis'],'proposed':['proposal']}
            require(r['epistemicKind']=='unverified' or a['mode'] in expected[r['epistemicKind']],'Epistemic/activity mismatch')
            if r['epistemicKind']=='observed':require(r['aboutRef']==a['observedTarget'],'Observed account target mismatch')
            if r['epistemicKind']=='source-asserted':
                require(all(resolve(p,['Capture'],current=False)['aboutRef']==r['aboutRef'] for p in a['inputs']),'Source assertion target mismatch')
    elif k=='EvidenceLink':resolve(r['evidence'],['Capture','ProvenanceRecord'],field='evidence')
    elif k=='ConfidenceAssessment':
        resolve(r['account'],['ProvenanceRecord'],field='account');a=resolve(r['activity'],['Activity'],field='activity')
        require(a['mode']=='review' and r['account'] in a['inputs'],'Assessment needs review of its exact account')
        require(a['actor']==r['assessor'] and a['method']==r['method'],'Assessment reviewer/method mismatch')
        require(r['scheme']==SCHEME,'Unknown confidence scheme pin')
        for p in r['basis']:resolve(p,['Capture','ProvenanceRecord','EvidenceLink'],field='basis')
        if new_judgement:
            review_at=prior[(a['id'],1)]['recordedAt']
            require(old is None or old['recordedAt']<review_at,'Fresh review must be first registered after the previous assessment')
            require(all(prior[(p['id'],p['revision'])]['recordedAt']<=review_at for p in r['basis']),'Review first registered before its evidence basis')
        if r['label']=='limited':require(bool(r['limitations']),'Limited assessment needs limitations')

def validate_ledger(ledger,config=None,now=None):
    validate(ledger)
    if now is not None:
        instant(now)
        require(all(r['recordedAt']<=now for r in ledger['records']),'Receipt follows trusted now')
    if config is not None:
        validate(config,'configuration');require(ledger['dimension']==config['dimension'],'Dimension mismatch')
    prior={};heads={};last=None
    for r in ledger['records']:
        require(last is None or last<r['recordedAt'],'Receipts must strictly increase')
        old=heads.get(r['id'])
        if old is None:
            require(r['revision']==1 and r['previousDigest'] is None and r['change']=='create' and r['state']=='active','Invalid genesis')
        else:
            require(r['kind']==old['kind'] and r['scope']==old['scope'],'Identity kind/scope changed')
            require(r['revision']==old['revision']+1 and r['previousDigest']==digest(old),'Broken revision chain')
            require(old['state']=='active','Withdrawal is terminal')
            require(all(r[f]==old[f] for f in ANCHORS[r['kind']]),'Identity anchor changed')
            require((r['change'],r['state']) in [('correct','active'),('withdraw','withdrawn')],'Invalid revision transition')
            if r['change']=='withdraw':
                allowed={'revision','previousDigest','recordedAt','writer','state','change','reason'}
                require(all(r[f]==old[f] for f in r if f not in allowed),'Withdrawal changes content')
        # A withdrawal preserves references even if those have subsequently
        # been superseded. It makes no new reliance assertion.
        if r['change']!='withdraw':semantic(r,prior,heads,old)
        prior[(r['id'],r['revision'])]=r;heads[r['id']]=r;last=r['recordedAt']
    return True

def admit(previous,record,config,actor,now):
    """Host-internal API. Return no ledger/diagnostics to a write-only client."""
    config_check(config,now)
    require(isinstance(record,dict) and record.get('kind') in ANCHORS,'Unknown record type')
    validate(record,record['kind'])
    if record['writer']!=actor or not any(g['kind']==record['kind'] and g['scope']==record['scope'] and actor in g['actors'] for g in config['writers']):
        raise Denied('Write denied')
    require(record['recordedAt']==now,'Receipt must equal trusted now')
    validate_ledger(previous,config,now)
    for old in previous['records']:
        if (old['id'],old['revision'])==(record['id'],record['revision']):
            require(encode({k:v for k,v in old.items() if k!='recordedAt'})==encode({k:v for k,v in record.items() if k!='recordedAt'}),'Conflicting replay')
            return copy.deepcopy(previous)
    candidate=copy.deepcopy(previous);candidate['records'].append(copy.deepcopy(record));validate_ledger(candidate,config,now)
    return candidate

def validate_extension(previous,candidate,config,now=None):
    validate_ledger(previous,config,now);validate_ledger(candidate,config,now)
    require(encode({k:v for k,v in previous.items() if k!='records'})==encode({k:v for k,v in candidate.items() if k!='records'}),'Register header changed')
    require(encode(candidate['records'][:len(previous['records'])])==encode(previous['records']),'Historical prefix rewritten or truncated')
    return True

def view(ledger,config,actor,purpose,claim,knownAt,now):
    gate(config,actor,purpose,now) # before any ledger/query diagnostic
    instant(knownAt);require(knownAt<=now,'Future knowledge cut');validate(claim,'pin');validate_ledger(ledger,config,now)
    known=[r for r in ledger['records'] if r['recordedAt']<=knownAt];heads={r['id']:r for r in known};by={(r['id'],r['revision']):r for r in known}
    def closure(r):
        result={};todo=list(refs(r))
        while todo:
            p=todo.pop();key=(p['id'],p['revision'])
            if key in result:continue
            node=by[key];result[key]=node;todo.extend(refs(node))
        return list(result.values())
    accounts=[r for r in heads.values() if r['kind']=='ProvenanceRecord' and r['claim']==claim]
    links=[r for r in heads.values() if r['kind']=='EvidenceLink' and r['claim']==claim]
    assessments=[r for r in heads.values() if r['kind']=='ConfidenceAssessment' and by[(r['account']['id'],r['account']['revision'])]['claim']==claim]
    impacts=[]
    for r in accounts+links+assessments:
        dependencies=closure(r)
        changed=[{'cited':pin(x),'current':pin(heads[x['id']]),'state':heads[x['id']]['state'],**({'currentCaptureState':{'availability':heads[x['id']]['availability'],'integrity':heads[x['id']]['integrity']}} if x['kind']=='Capture' else {})} for x in dependencies if pin(x)!=pin(heads[x['id']]) or heads[x['id']]['state']=='withdrawn']
        gaps=[{'pin':pin(x),'availability':x['availability'],'integrity':x['integrity']} for x in dependencies if x['kind']=='Capture' and (x['availability']=='unavailable' or x['integrity']=='mismatched')]
        impacts.append({'record':pin(r),'state':r['state'],'requiresReview':bool(changed or gaps),'changedDependencies':changed,'sourceGaps':gaps})
    origins={}
    for a in accounts:
        if a['state']!='active':continue
        for x in closure(a):
            if x['kind']=='Capture':
                for label,value in [('bytes',x['representationDigest']),('declared-origin',x['originRef'])]:
                    if value is not None:origins.setdefault((label,value),set()).add(a['id'])
    shared=[{'basis':k[0],'value':k[1],'accounts':sorted(v)} for k,v in sorted(origins.items()) if len(v)>1]
    return {'profileVersion':VERSION,'claim':copy.deepcopy(claim),'knownAt':knownAt,'inputSliceDigest':digest({**ledger,'records':known}),'configurationDigest':digest(config),
        'status':'context-available' if any(r['state']=='active' and r['epistemicKind']!='unverified' for r in accounts) else 'insufficient-context',
        'accounts':copy.deepcopy(accounts),'links':copy.deepcopy(links),'assessments':copy.deepcopy(assessments),'impacts':impacts,
        'independence':{'status':'known-shared-origin' if shared else 'unknown','shared':shared},
        'truth':'not-evaluated','permissions':'not-inferred'}

def import_snapshot(snapshot,config,*,now):
    config_check(config,now);validate_ledger(snapshot,config,now);return copy.deepcopy(snapshot)
def migrate(snapshot,config,targetVersion,*,now):
    require(targetVersion==VERSION,'Unsupported or lossy migration requires explicit mapping')
    return import_snapshot(snapshot,config,now=now)

def validate_snapshot(fact,config,previous=None,*,now):
    """Check companion snapshot pins; use V3 separately for the full envelope."""
    require(isinstance(fact,dict) and fact.get('recordType')=='fact' and fact.get('path')=='provenance.register.snapshot','Wrong snapshot envelope')
    require(isinstance(fact.get('factId'),str) and bool(fact['factId']),'Missing snapshot identity')
    config_check(config,now);ledger=fact.get('value');validate_ledger(ledger,config,now)
    require(fact.get('subjectId')==ledger['dimension']+':provenance-register','Wrong aggregate subject')
    provenance=fact.get('provenance',{})
    require(isinstance(provenance,dict) and provenance.get('snapshotDigest')==digest(ledger),'Wrong snapshot digest')
    if previous is None:
        require(provenance.get('previousSnapshotDigest') is None and fact.get('supersedes')==[],'Missing trusted previous snapshot')
    else:
        require(isinstance(previous,dict) and previous.get('recordType')=='fact' and previous.get('subjectId')==fact['subjectId'] and previous.get('path')==fact['path'],'Snapshot lineage mismatch')
        require(previous.get('factId')!=fact['factId'],'Snapshot identity reused')
        previous_ledger=previous.get('value');validate_extension(previous_ledger,ledger,config,now)
        previous_provenance=previous.get('provenance')
        require(isinstance(previous.get('factId'),str) and isinstance(previous_provenance,dict) and previous_provenance.get('snapshotDigest')==digest(previous_ledger),'Wrong previous snapshot digest')
        require(provenance.get('previousSnapshotDigest')==digest(previous_ledger) and fact.get('supersedes')==[previous.get('factId')],'Wrong snapshot predecessor')
    return True
