Focused NO-TOOLS follow-up audit of Enterprise Assertion Provenance 0.1.0. Earlier Claude verdict: BLOCK (correction freeze, timestamp-format dependency); earlier Grok verdict: ACCEPT WITH LIMITS with the same correction tension and cross-revision self-derivation edge. Both exact initial responses remain preserved. We chose to fix the implementation rather than narrow away correction capability. Give ACCEPT WITH LIMITS or BLOCK on this exact revised candidate, with concrete remaining defects and static-review/truncation limits. Do not browse, execute, fetch or grant publication authority.

Remediation: unchanged immediate historical references survive metadata corrections; new/changed immediate pins must be current active heads, and referenced Activity input history is not rewritten. A transitive dependency on any revision of one's own ID is rejected. Every timestamp is independently ASCII/fullmatch/calendar parsed; required URI/date-time checker presence is enforced. Revisions must be actual Python int (no bool or 1.0); snapshot-prefix and replay comparisons use canonical JSON bytes. Views disclose current Capture integrity/availability next to the old pin. New validate_snapshot helper checks aggregate identity, nested history, snapshot digests and predecessor/supersedes linkage; native V3 remains separately required. Scheme ID/revision derive from the embedded scheme. Read denial messages are uniform. Serialized JSON capped at 8 MiB; host enforces preparse limits. Native examples now have distinct Dimension IDs and package-immutable upstream source URLs.

Executed locally after fixes: 62 tests pass and all three native profiles pass, including snapshot digest tampering, nested malformed value, truncation, and exact round-trip. You did not execute those tests: trace the provided source. The host remains responsible for authentication/current complete root/config, receipt clock, no concurrent mutation, and generic write-only receipts/errors; do not mistake the trusted-host API for a public service. No source fetch, probability, legal/parent conformance or truth selection is claimed.

Input includes full revised code/schema/tests/acceptance, exact contract diff, AGENTS and the FULL normative structure tree (not just its count). Per-type facets are also supplied. Fields of spec.json other than its tree/contract remain outside your direct review. Hashes label source files but are not your own recomputations. Confirm final sentinel before reporting completeness.

FILE provenance.py SHA256 05f05d24ace3f67c65fb5ca56f3b6cadf56ef87b79298510ef6e1201fdac99bf
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
def refs(r):
    k=r['kind']
    if k=='Activity':return r['inputs']
    if k=='ProvenanceRecord':return [] if r['activity'] is None else [r['activity']]
    if k=='EvidenceLink':return [r['evidence']]
    if k=='ConfidenceAssessment':return [r['account'],r['activity'],*r['basis']]
    return []
ANCHORS={
'Capture':['sourceRef','sourceVersion','aboutRef','obtainedAt','mode','availability','representationDigest'],
'Activity':['actor','mode','startedAt','endedAt','inputs','observedTarget','method'],
'ProvenanceRecord':['claim','aboutRef','asserter','epistemicKind'],
'EvidenceLink':['claim','evidence','attributedTo','relation'],
'ConfidenceAssessment':['account','assessor','method','scheme','purpose'],
}
def semantic(r,prior,heads,old=None):
    retained={encode(p) for p in refs(old)} if old else set()
    def resolve(p,types=None,current=None):
        target=prior.get((p['id'],p['revision']))
        require(target is not None and pin(target)==p,'Unresolved exact internal pin')
        require(target['scope']==r['scope'],'Cross-scope internal link')
        if current is None:current=encode(p) not in retained
        require(target['state']=='active','Reliance target was already withdrawn')
        if current:require(pin(heads[p['id']])==p,'New link to inactive or superseded revision')
        require(types is None or target['kind'] in types,'Wrong internal target type')
        return target
    k=r['kind']
    for p in refs(r):resolve(p)
    # Revision pins form a DAG; additionally reject self-support through a
    # previous revision of this same semantic identity.
    todo=list(refs(r));visited=set()
    while todo:
        p=todo.pop();key=(p['id'],p['revision'])
        require(p['id']!=r['id'],'Self-derivation across revisions')
        if key not in visited:
            visited.add(key);todo.extend(refs(prior[key]))
    if k=='Capture':
        require(r['obtainedAt']<=r['recordedAt'],'Capture after receipt')
        require((r['availability']=='captured')==(r['representationDigest'] is not None),'Capture digest/availability mismatch')
        require(r['availability']=='captured' or r['integrity']=='not-tested','Unavailable capture cannot have checked integrity')
    elif k=='Activity':
        require(r['startedAt']<=r['endedAt']<=r['recordedAt'],'Activity time mismatch')
        inputs=[resolve(p,['Capture','ProvenanceRecord']) for p in r['inputs']]
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
            a=resolve(r['activity'],['Activity'])
            expected={'observed':['live-observation'],'source-asserted':['file-acquisition','live-observation'],'inferred':['synthesis'],'proposed':['proposal']}
            require(r['epistemicKind']=='unverified' or a['mode'] in expected[r['epistemicKind']],'Epistemic/activity mismatch')
            if r['epistemicKind']=='observed':require(r['aboutRef']==a['observedTarget'],'Observed account target mismatch')
            if r['epistemicKind']=='source-asserted':
                require(all(resolve(p,['Capture'],current=False)['aboutRef']==r['aboutRef'] for p in a['inputs']),'Source assertion target mismatch')
    elif k=='EvidenceLink':resolve(r['evidence'],['Capture','ProvenanceRecord'])
    elif k=='ConfidenceAssessment':
        resolve(r['account'],['ProvenanceRecord']);a=resolve(r['activity'],['Activity'])
        require(a['mode']=='review' and r['account'] in a['inputs'],'Assessment needs review of its exact account')
        require(a['actor']==r['assessor'] and a['method']==r['method'],'Assessment reviewer/method mismatch')
        require(r['scheme']==SCHEME,'Unknown confidence scheme pin')
        for p in r['basis']:resolve(p,['Capture','ProvenanceRecord','EvidenceLink'])
        if r['label']=='limited':require(bool(r['limitations']),'Limited assessment needs limitations')

def validate_ledger(ledger,config=None):
    validate(ledger)
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
    validate_ledger(previous,config)
    for old in previous['records']:
        if (old['id'],old['revision'])==(record['id'],record['revision']):
            require(encode({k:v for k,v in old.items() if k!='recordedAt'})==encode({k:v for k,v in record.items() if k!='recordedAt'}),'Conflicting replay')
            return copy.deepcopy(previous)
    candidate=copy.deepcopy(previous);candidate['records'].append(copy.deepcopy(record));validate_ledger(candidate,config)
    return candidate

def validate_extension(previous,candidate,config):
    validate_ledger(previous,config);validate_ledger(candidate,config)
    require(encode({k:v for k,v in previous.items() if k!='records'})==encode({k:v for k,v in candidate.items() if k!='records'}),'Register header changed')
    require(encode(candidate['records'][:len(previous['records'])])==encode(previous['records']),'Historical prefix rewritten or truncated')
    return True

def view(ledger,config,actor,purpose,claim,knownAt,now):
    gate(config,actor,purpose,now) # before any ledger/query diagnostic
    instant(knownAt);require(knownAt<=now,'Future knowledge cut');validate(claim,'pin');validate_ledger(ledger,config)
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

def import_snapshot(snapshot,config):
    validate_ledger(snapshot,config);return copy.deepcopy(snapshot)
def migrate(snapshot,config,targetVersion):
    require(targetVersion==VERSION,'Unsupported or lossy migration requires explicit mapping')
    return import_snapshot(snapshot,config)

def validate_snapshot(fact,config,previous=None):
    """Check companion snapshot pins; use V3 separately for the full envelope."""
    require(isinstance(fact,dict) and fact.get('recordType')=='fact' and fact.get('path')=='provenance.register.snapshot','Wrong snapshot envelope')
    require(isinstance(fact.get('factId'),str) and bool(fact['factId']),'Missing snapshot identity')
    ledger=fact.get('value');validate_ledger(ledger,config)
    require(fact.get('subjectId')==ledger['dimension']+':provenance-register','Wrong aggregate subject')
    provenance=fact.get('provenance',{})
    require(isinstance(provenance,dict) and provenance.get('snapshotDigest')==digest(ledger),'Wrong snapshot digest')
    if previous is None:
        require(provenance.get('previousSnapshotDigest') is None and fact.get('supersedes')==[],'Missing trusted previous snapshot')
    else:
        require(isinstance(previous,dict) and previous.get('subjectId')==fact['subjectId'] and previous.get('path')==fact['path'],'Snapshot lineage mismatch')
        previous_ledger=previous.get('value');validate_extension(previous_ledger,ledger,config)
        previous_provenance=previous.get('provenance')
        require(isinstance(previous.get('factId'),str) and isinstance(previous_provenance,dict) and previous_provenance.get('snapshotDigest')==digest(previous_ledger),'Wrong previous snapshot digest')
        require(provenance.get('previousSnapshotDigest')==digest(previous_ledger) and fact.get('supersedes')==[previous.get('factId')],'Wrong snapshot predecessor')
    return True

END FILE provenance.py

FILE provenance.schema.json SHA256 a7eae48f6e008ab124e08c6a89bae9cd49dbb4e48e2ef60d943b0cea64915516
{"$schema":"https://json-schema.org/draft/2020-12/schema","$id":"https://ver.cy/models/enterprise-assertion-provenance/versions/0.1.0/provenance.schema.json","type":"object","properties":{"format":{"const":"vercy-assertion-provenance"},"version":{"const":"0.1.0"},"dimension":{"type":"string","format":"uri","minLength":3,"maxLength":500},"records":{"type":"array","maxItems":10000,"items":{"oneOf":[{"$ref":"#/$defs/Capture"},{"$ref":"#/$defs/Activity"},{"$ref":"#/$defs/ProvenanceRecord"},{"$ref":"#/$defs/EvidenceLink"},{"$ref":"#/$defs/ConfidenceAssessment"}]}}},"required":["format","version","dimension","records"],"additionalProperties":false,"$defs":{"pin":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":500},"revision":{"type":"integer","minimum":1},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","revision","digest"],"additionalProperties":false},"Capture":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":500},"kind":{"const":"Capture"},"scope":{"type":"string","format":"uri","minLength":3,"maxLength":500},"revision":{"type":"integer","minimum":1},"previousDigest":{"anyOf":[{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"},{"type":"null"}]},"recordedAt":{"type":"string","format":"date-time","pattern":"^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"},"writer":{"type":"string","format":"uri","minLength":3,"maxLength":500},"state":{"enum":["active","withdrawn"]},"change":{"enum":["create","correct","withdraw"]},"reason":{"type":"string","minLength":1,"maxLength":4000},"notes":{"type":"array","items":{"type":"string","minLength":1,"maxLength":4000},"minItems":0,"maxItems":10000,"uniqueItems":true},"sourceRef":{"type":"string","format":"uri","minLength":3,"maxLength":500},"sourceVersion":{"anyOf":[{"type":"string","minLength":1,"maxLength":4000},{"type":"null"}]},"sourceAuthor":{"anyOf":[{"type":"string","format":"uri","minLength":3,"maxLength":500},{"type":"null"}]},"aboutRef":{"type":"string","format":"uri","minLength":3,"maxLength":500},"obtainedAt":{"type":"string","format":"date-time","pattern":"^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"},"mode":{"enum":["file","live-api","manual"]},"availability":{"enum":["captured","unavailable"]},"representationDigest":{"anyOf":[{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"},{"type":"null"}]},"originRef":{"anyOf":[{"type":"string","format":"uri","minLength":3,"maxLength":500},{"type":"null"}]},"integrity":{"enum":["not-tested","matched","mismatched"]}},"required":["id","kind","scope","revision","previousDigest","recordedAt","writer","state","change","reason","notes","sourceRef","sourceVersion","sourceAuthor","aboutRef","obtainedAt","mode","availability","representationDigest","originRef","integrity"],"additionalProperties":false},"Activity":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":500},"kind":{"const":"Activity"},"scope":{"type":"string","format":"uri","minLength":3,"maxLength":500},"revision":{"type":"integer","minimum":1},"previousDigest":{"anyOf":[{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"},{"type":"null"}]},"recordedAt":{"type":"string","format":"date-time","pattern":"^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"},"writer":{"type":"string","format":"uri","minLength":3,"maxLength":500},"state":{"enum":["active","withdrawn"]},"change":{"enum":["create","correct","withdraw"]},"reason":{"type":"string","minLength":1,"maxLength":4000},"notes":{"type":"array","items":{"type":"string","minLength":1,"maxLength":4000},"minItems":0,"maxItems":10000,"uniqueItems":true},"actor":{"type":"string","format":"uri","minLength":3,"maxLength":500},"mode":{"enum":["file-acquisition","live-observation","synthesis","proposal","review"]},"startedAt":{"type":"string","format":"date-time","pattern":"^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"},"endedAt":{"type":"string","format":"date-time","pattern":"^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"},"inputs":{"type":"array","items":{"$ref":"#/$defs/pin"},"minItems":0,"maxItems":10000,"uniqueItems":true},"observedTarget":{"anyOf":[{"type":"string","format":"uri","minLength":3,"maxLength":500},{"type":"null"}]},"method":{"$ref":"#/$defs/pin"}},"required":["id","kind","scope","revision","previousDigest","recordedAt","writer","state","change","reason","notes","actor","mode","startedAt","endedAt","inputs","observedTarget","method"],"additionalProperties":false},"ProvenanceRecord":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":500},"kind":{"const":"ProvenanceRecord"},"scope":{"type":"string","format":"uri","minLength":3,"maxLength":500},"revision":{"type":"integer","minimum":1},"previousDigest":{"anyOf":[{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"},{"type":"null"}]},"recordedAt":{"type":"string","format":"date-time","pattern":"^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"},"writer":{"type":"string","format":"uri","minLength":3,"maxLength":500},"state":{"enum":["active","withdrawn"]},"change":{"enum":["create","correct","withdraw"]},"reason":{"type":"string","minLength":1,"maxLength":4000},"notes":{"type":"array","items":{"type":"string","minLength":1,"maxLength":4000},"minItems":0,"maxItems":10000,"uniqueItems":true},"claim":{"$ref":"#/$defs/pin"},"aboutRef":{"type":"string","format":"uri","minLength":3,"maxLength":500},"asserter":{"type":"string","format":"uri","minLength":3,"maxLength":500},"epistemicKind":{"enum":["observed","source-asserted","inferred","proposed","unverified"]},"activity":{"anyOf":[{"$ref":"#/$defs/pin"},{"type":"null"}]},"limitations":{"type":"array","items":{"type":"string","minLength":1,"maxLength":4000},"minItems":0,"maxItems":10000,"uniqueItems":true}},"required":["id","kind","scope","revision","previousDigest","recordedAt","writer","state","change","reason","notes","claim","aboutRef","asserter","epistemicKind","activity","limitations"],"additionalProperties":false},"EvidenceLink":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":500},"kind":{"const":"EvidenceLink"},"scope":{"type":"string","format":"uri","minLength":3,"maxLength":500},"revision":{"type":"integer","minimum":1},"previousDigest":{"anyOf":[{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"},{"type":"null"}]},"recordedAt":{"type":"string","format":"date-time","pattern":"^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"},"writer":{"type":"string","format":"uri","minLength":3,"maxLength":500},"state":{"enum":["active","withdrawn"]},"change":{"enum":["create","correct","withdraw"]},"reason":{"type":"string","minLength":1,"maxLength":4000},"notes":{"type":"array","items":{"type":"string","minLength":1,"maxLength":4000},"minItems":0,"maxItems":10000,"uniqueItems":true},"claim":{"$ref":"#/$defs/pin"},"evidence":{"$ref":"#/$defs/pin"},"attributedTo":{"type":"string","format":"uri","minLength":3,"maxLength":500},"relation":{"enum":["supports","refutes","context","cites"]},"selector":{"type":"string","minLength":1,"maxLength":4000},"rationale":{"type":"string","minLength":1,"maxLength":4000}},"required":["id","kind","scope","revision","previousDigest","recordedAt","writer","state","change","reason","notes","claim","evidence","attributedTo","relation","selector","rationale"],"additionalProperties":false},"ConfidenceAssessment":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":500},"kind":{"const":"ConfidenceAssessment"},"scope":{"type":"string","format":"uri","minLength":3,"maxLength":500},"revision":{"type":"integer","minimum":1},"previousDigest":{"anyOf":[{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"},{"type":"null"}]},"recordedAt":{"type":"string","format":"date-time","pattern":"^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"},"writer":{"type":"string","format":"uri","minLength":3,"maxLength":500},"state":{"enum":["active","withdrawn"]},"change":{"enum":["create","correct","withdraw"]},"reason":{"type":"string","minLength":1,"maxLength":4000},"notes":{"type":"array","items":{"type":"string","minLength":1,"maxLength":4000},"minItems":0,"maxItems":10000,"uniqueItems":true},"account":{"$ref":"#/$defs/pin"},"assessor":{"type":"string","format":"uri","minLength":3,"maxLength":500},"activity":{"$ref":"#/$defs/pin"},"method":{"$ref":"#/$defs/pin"},"scheme":{"$ref":"#/$defs/pin"},"purpose":{"type":"string","minLength":1,"maxLength":4000},"label":{"enum":["insufficient","limited","supported"]},"basis":{"type":"array","items":{"$ref":"#/$defs/pin"},"minItems":1,"maxItems":10000,"uniqueItems":true},"limitations":{"type":"array","items":{"type":"string","minLength":1,"maxLength":4000},"minItems":0,"maxItems":10000,"uniqueItems":true}},"required":["id","kind","scope","revision","previousDigest","recordedAt","writer","state","change","reason","notes","account","assessor","activity","method","scheme","purpose","label","basis","limitations"],"additionalProperties":false},"configuration":{"type":"object","properties":{"id":{"type":"string","format":"uri","minLength":3,"maxLength":500},"dimension":{"type":"string","format":"uri","minLength":3,"maxLength":500},"validFrom":{"type":"string","format":"date-time","pattern":"^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"},"validUntil":{"type":"string","format":"date-time","pattern":"^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"},"writers":{"type":"array","items":{"type":"object","properties":{"kind":{"enum":["Capture","Activity","ProvenanceRecord","EvidenceLink","ConfidenceAssessment"]},"scope":{"type":"string","format":"uri","minLength":3,"maxLength":500},"actors":{"type":"array","items":{"type":"string","format":"uri","minLength":3,"maxLength":500},"minItems":1,"maxItems":10000,"uniqueItems":true}},"required":["kind","scope","actors"],"additionalProperties":false},"minItems":1,"maxItems":10000,"uniqueItems":true},"readers":{"type":"array","items":{"type":"string","format":"uri","minLength":3,"maxLength":500},"minItems":1,"maxItems":10000,"uniqueItems":true},"purposes":{"type":"array","items":{"type":"string","minLength":1,"maxLength":4000},"minItems":1,"maxItems":10000,"uniqueItems":true}},"required":["id","dimension","validFrom","validUntil","writers","readers","purposes"],"additionalProperties":false}},"x-confidenceScheme":{"id":"urn:vercy:scheme:qualitative-reliance","revision":1,"version":"0.1.0","purpose":"Assessor-declared fitness of the stated basis for a named reliance purpose; not probability or proposition truth.","labels":{"insufficient":"The assessor states the cited basis is insufficient for this purpose.","limited":"The assessor permits only qualified reliance within stated limitations.","supported":"The assessor states the cited basis supports this purpose within stated limitations."},"arithmetic":"No numeric conversion, averaging or automatic cross-method ordering."}}
END FILE provenance.schema.json

FILE test_provenance.py SHA256 7700745faf6f65a4c7cf2b8251fb1947e9092f552333a266cb541b65f151ab7d
"""Synthetic behavior tests and fixtures for the original reference contract."""
import copy,json,unittest
from unittest.mock import patch
from datetime import datetime,timedelta
from pathlib import Path
import provenance as p
HERE=Path(__file__).resolve().parent
U='urn:synthetic:'
CLAIM={'id':U+'claim:capacity','revision':1,'digest':'sha256:'+'a'*64}
METHOD={'id':U+'method:inspection','revision':1,'digest':'sha256:'+'b'*64}
NOW='2026-09-21T12:00:00Z'
def config():return {'id':U+'configuration','dimension':U+'dimension','validFrom':'2026-01-01T00:00:00Z','validUntil':'2030-01-01T00:00:00Z','writers':[{'kind':k,'scope':U+'scope','actors':[U+'writer']} for k in p.ANCHORS],'readers':[U+'reader'],'purposes':['research']}
def empty():return {'format':'vercy-assertion-provenance','version':'0.1.0','dimension':U+'dimension','records':[]}
def stamp(i):return (datetime(2026,9,21,10,0,0)+timedelta(seconds=i)).strftime('%Y-%m-%dT%H:%M:%SZ')
def row(kind,n,**kw):
    return {'id':U+n,'kind':kind,'scope':U+'scope','revision':1,'previousDigest':None,'recordedAt':stamp(1),'writer':U+'writer','state':'active','change':'create','reason':'Synthetic evidence-backed entry','notes':[],**kw}
def capture(n='capture',**kw):return row('Capture',n,**({'sourceRef':U+'source:document','sourceVersion':'v1','sourceAuthor':U+'document-author','aboutRef':U+'system','obtainedAt':'2026-09-21T09:00:00Z','mode':'file','availability':'captured','representationDigest':'sha256:'+'c'*64,'originRef':U+'declared-origin','integrity':'not-tested'}|kw))
def activity(c,n='acquisition',**kw):return row('Activity',n,**({'actor':U+'observer','mode':'file-acquisition','startedAt':'2026-09-21T08:00:00Z','endedAt':'2026-09-21T09:30:00Z','inputs':[p.pin(c)],'observedTarget':None,'method':METHOD}|kw))
def account(a,n='account',**kw):return row('ProvenanceRecord',n,**({'claim':CLAIM,'aboutRef':U+'system','asserter':U+'asserter','epistemicKind':'source-asserted','activity':p.pin(a) if a else None,'limitations':['Source statement; no live-system verification.']}|kw))
def link(c,n='evidence',**kw):return row('EvidenceLink',n,**({'claim':CLAIM,'evidence':p.pin(c),'attributedTo':U+'relation-author','relation':'cites','selector':'whole captured representation','rationale':'Reference context without automatic support'}|kw))
def add(ledger,r,cfg=None):
    r=copy.deepcopy(r);r['recordedAt']=stamp(len(ledger['records'])+1)
    return p.admit(ledger,r,cfg or config(),r['writer'],r['recordedAt']),r
def revision(r,**kw):return {**copy.deepcopy(r),'revision':r['revision']+1,'previousDigest':p.digest(r),'change':'correct',**kw}
def fixture(name='startup'):
    g=empty();g,c=add(g,capture());g,a=add(g,activity(c));g,pr=add(g,account(a));g,l=add(g,link(c))
    if name=='group':
        g,c2=add(g,capture('copy',sourceRef=U+'source:second-report'))
        g,a2=add(g,activity(c2,'second-acquisition'));g,pr2=add(g,account(a2,'second-account'))
        g,l2=add(g,link(c2,'counterevidence',relation='refutes',rationale='Second writer explicitly disputes the same pinned claim'))
    if name=='ai-team':
        g,s=add(g,activity(c,'synthesis',actor=U+'ai-agent',mode='synthesis',inputs=[p.pin(pr)]))
        g,inferred=add(g,account(s,'inference',epistemicKind='inferred',asserter=U+'ai-agent'))
        g,review=add(g,activity(c,'review',actor=U+'human-reviewer',mode='review',inputs=[p.pin(inferred)]))
        g,assessment=add(g,row('ConfidenceAssessment','assessment',account=p.pin(inferred),assessor=review['actor'],activity=p.pin(review),method=METHOD,scheme=p.SCHEME,purpose='Plan a separate live check',label='limited',basis=[p.pin(c)],limitations=['File analysis is not live observation.']))
    return g
def view(g,**kw):return p.view(g,config(),U+'reader','research',CLAIM,NOW,NOW,**kw)

class Tests(unittest.TestCase):
    def test_three_profiles(self):
        for name in ['startup','group','ai-team']:self.assertTrue(p.validate_ledger(fixture(name),config()))
    def test_no_truth_or_permission_inference(self):
        v=view(fixture());self.assertEqual((v['truth'],v['permissions']),('not-evaluated','not-inferred'))
    def test_shared_origin_not_independence(self):self.assertEqual(view(fixture('group'))['independence']['status'],'known-shared-origin')
    def test_distinct_roots_remain_unknown(self):
        g=fixture();g,c=add(g,capture('distinct',originRef=U+'other',representationDigest='sha256:'+'d'*64));g,a=add(g,activity(c,'distinct-event'));g,_=add(g,account(a,'distinct-account'))
        self.assertEqual(view(g)['independence']['status'],'unknown')
    def test_review_does_not_promote_inference(self):
        v=view(fixture('ai-team'));self.assertEqual(v['accounts'][-1]['epistemicKind'],'inferred');self.assertEqual(v['assessments'][0]['label'],'limited')
    def test_citation_has_no_support_default(self):self.assertEqual(view(fixture())['links'][0]['relation'],'cites')
    def test_unknown_empty_register(self):self.assertEqual(view(empty())['status'],'insufficient-context')
    def test_author_observer_asserter_recorder_separate(self):
        g=fixture();self.assertEqual(len({g['records'][0]['sourceAuthor'],g['records'][1]['actor'],g['records'][2]['asserter'],g['records'][0]['writer']}),4)
    def test_wrong_actor_denied(self):
        with self.assertRaises(p.Denied):p.admit(empty(),capture(),config(),U+'owner',stamp(1))
    def test_missing_write_grant(self):
        c=config();c['writers']=c['writers'][1:]
        with self.assertRaises(p.Denied):p.admit(empty(),capture(),c,U+'writer',stamp(1))
    def test_write_rotation_preserves_attribution(self):
        g=fixture();r=revision(g['records'][0],writer=U+'writer2',notes=['Correct attribution context']);c=config();c['writers'][0]['actors']=[U+'writer2'];g,r=add(g,r,c)
        self.assertEqual(r['sourceAuthor'],U+'document-author');self.assertEqual(g['records'][0]['writer'],U+'writer')
    def test_read_denied_before_malformed_input(self):
        with self.assertRaisesRegex(p.Denied,'^Read denied$'):p.view({'SECRET':'bad'},config(),U+'intruder','research',None,'bad',NOW)
    def test_purpose_gate(self):
        with self.assertRaises(p.Denied):p.view(fixture(),config(),U+'reader','other',CLAIM,NOW,NOW)
    def test_expired_config(self):
        with self.assertRaises(p.Denied):p.view(fixture(),config(),U+'reader','research',CLAIM,NOW,'2030-01-01T00:00:00Z')
    def test_replay_retains_receipt(self):
        g=fixture();r=copy.deepcopy(g['records'][0]);r['recordedAt']=NOW
        self.assertEqual(p.admit(g,r,config(),U+'writer',NOW),g)
    def test_replay_rechecks_rights(self):
        g=fixture();c=config();c['writers']=c['writers'][1:];r=copy.deepcopy(g['records'][0]);r['recordedAt']=NOW
        with self.assertRaises(p.Denied):p.admit(g,r,c,U+'writer',NOW)
    def test_conflicting_replay(self):
        g=fixture();r=copy.deepcopy(g['records'][0]);r['notes']=['conflicting'];r['recordedAt']=NOW
        with self.assertRaises(p.Invalid):p.admit(g,r,config(),U+'writer',NOW)
    def test_corrective_impact_and_past_knowledge(self):
        g=fixture();old=copy.deepcopy(g);g,_=add(g,revision(g['records'][0],integrity='mismatched'))
        self.assertTrue(view(g)['impacts'][0]['requiresReview']);self.assertEqual(g['records'][2]['epistemicKind'],'source-asserted')
        v=p.view(g,config(),U+'reader','research',CLAIM,stamp(4),NOW)
        self.assertEqual(v,p.view(old,config(),U+'reader','research',CLAIM,stamp(4),NOW))
    def test_withdrawal_preserves_external_claim(self):
        g=fixture();g,_=add(g,revision(g['records'][0],change='withdraw',state='withdrawn'))
        self.assertTrue(view(g)['impacts'][0]['requiresReview']);self.assertEqual(view(g)['truth'],'not-evaluated')
    def test_withdraw_dependent_after_input_withdrawn(self):
        g=fixture();g,_=add(g,revision(g['records'][0],change='withdraw',state='withdrawn'));g,_=add(g,revision(g['records'][2],change='withdraw',state='withdrawn'))
        self.assertEqual(view(g)['status'],'insufficient-context')
    def test_terminal_withdrawal(self):
        g=fixture();g,r=add(g,revision(g['records'][0],change='withdraw',state='withdrawn'))
        with self.assertRaises(p.Invalid):add(g,revision(r,state='active'))
    def test_reject_withdrawal_content_change(self):
        g=fixture()
        with self.assertRaises(p.Invalid):add(g,revision(g['records'][0],change='withdraw',state='withdrawn',originRef=U+'new'))
    def test_source_pin_is_immutable(self):
        g=fixture()
        with self.assertRaises(p.Invalid):add(g,revision(g['records'][0],representationDigest='sha256:'+'d'*64))
    def test_no_auto_carryover_to_new_claim(self):
        claim={**CLAIM,'revision':2,'digest':'sha256:'+'e'*64}
        v=p.view(fixture(),config(),U+'reader','research',claim,NOW,NOW);self.assertEqual(v['accounts'],[])
    def test_file_cannot_be_live(self):
        g=fixture()
        with self.assertRaises(p.Invalid):add(g,activity(g['records'][0],'fake-live',mode='live-observation',observedTarget=U+'system'))
    def test_inference_cannot_be_observation(self):
        g=fixture('ai-team')
        with self.assertRaises(p.Invalid):add(g,account(g['records'][4],'fake-observed',epistemicKind='observed'))
    def test_live_declaration_positive(self):
        g=empty();g,c=add(g,capture(mode='live-api'));g,a=add(g,activity(c,mode='live-observation',observedTarget=U+'system'));g,_=add(g,account(a,epistemicKind='observed'));self.assertTrue(p.validate_ledger(g))
    def test_observed_target_mismatch(self):
        g=empty();g,c=add(g,capture(mode='live-api'))
        with self.assertRaises(p.Invalid):add(g,activity(c,mode='live-observation',observedTarget=U+'other'))
    def test_unverified_requires_limitations(self):
        with self.assertRaises(p.Invalid):add(empty(),account({},activity=None,epistemicKind='unverified',limitations=[]))
    def test_unknown_and_unavailable_are_explicit(self):
        g=empty();g,c=add(g,capture(availability='unavailable',representationDigest=None));g,_=add(g,link(c));g,_=add(g,row('ProvenanceRecord','unknown',claim=CLAIM,aboutRef=U+'system',asserter=U+'asserter',epistemicKind='unverified',activity=None,limitations=['Awaiting source']))
        self.assertEqual(view(g)['status'],'insufficient-context');self.assertTrue(view(g)['impacts'][1]['sourceGaps'])
    def test_schema_closed(self):
        with self.assertRaises(p.Invalid):add(empty(),capture(password='secret'))
    def test_unknown_kind_and_nonrecord(self):
        for r in [{'kind':'Alien'},None]:
            with self.assertRaises(p.Invalid):p.admit(empty(),r,config(),U+'writer',stamp(1))
    def test_nested_pin_required(self):
        g=fixture();r=link(g['records'][0],'broken');r['evidence']['digest']='sha256:'+'0'*64
        with self.assertRaises(p.Invalid):add(g,r)
    def test_no_future_or_self_reference(self):
        g=fixture();r=activity(g['records'][0],'self',mode='synthesis');r['inputs']=[{'id':r['id'],'revision':1,'digest':'sha256:'+'f'*64}]
        with self.assertRaises(p.Invalid):add(g,r)
    def test_cross_scope_link(self):
        g=fixture();r=link(g['records'][0],'other-scope',scope=U+'other')
        with self.assertRaises(p.Invalid):p.validate_ledger({**g,'records':g['records']+[{**r,'recordedAt':stamp(5)}]})
    def test_new_reliance_on_superseded_revision_rejected(self):
        g=fixture();c=g['records'][0];g,_=add(g,revision(c,notes=['Correction']))
        with self.assertRaises(p.Invalid):add(g,link(c,'stale'))
    def test_bad_calendar(self):
        with self.assertRaises(p.Invalid):add(empty(),capture(obtainedAt='2026-02-30T09:00:00Z'))
    def test_activity_clock(self):
        g=fixture()
        with self.assertRaises(p.Invalid):add(g,activity(g['records'][0],'late',endedAt='2027-01-01T00:00:00Z'))
    def test_input_cannot_follow_synthesis_event(self):
        g=fixture()
        with self.assertRaises(p.Invalid):add(g,activity(g['records'][0],'premature',mode='synthesis',startedAt='2026-09-20T00:00:00Z',endedAt='2026-09-20T01:00:00Z'))
    def test_future_knowledge(self):
        with self.assertRaises(p.Invalid):p.view(fixture(),config(),U+'reader','research',CLAIM,'2027-01-01T00:00:00Z',NOW)
    def test_receipt_spoof(self):
        with self.assertRaises(p.Invalid):p.admit(empty(),capture(),config(),U+'writer',NOW)
    def test_non_monotone_receipt(self):
        g=fixture();r=capture('backdated')
        with self.assertRaises(p.Invalid):p.admit(g,r,config(),U+'writer',stamp(1))
    def test_prefix_rewrite_and_truncation(self):
        g=fixture()
        for records in [g['records'][:-1],[]]:
            with self.assertRaises(p.Invalid):p.validate_extension(g,{**g,'records':records},config())
    def test_dimension_header(self):
        with self.assertRaises(p.Invalid):p.validate_ledger({**fixture(),'dimension':U+'other'},config())
    def test_no_numeric_confidence(self):
        g=fixture('ai-team');r=revision(g['records'][-1],label=0.95)
        with self.assertRaises(p.Invalid):add(g,r)
    def test_assessment_scheme_and_review(self):
        for fields in [{'scheme':METHOD},{'assessor':U+'imposter'},{'method':CLAIM},{'limitations':[]}]:
            g=fixture('ai-team')
            with self.assertRaises(p.Invalid):add(g,revision(g['records'][-1],**fields))
    def test_import_roundtrip_and_lossy_refusal(self):
        g=fixture('ai-team');self.assertEqual(p.import_snapshot(json.loads(p.encode(g)),config()),g)
        with self.assertRaises(p.Invalid):p.migrate(g,config(),'legacy-owner-and-confidence')
    def test_rejection_does_not_mutate(self):
        g=fixture();original=p.encode(g)
        with self.assertRaises(p.Invalid):add(g,revision(g['records'][0],previousDigest='sha256:'+'0'*64))
        self.assertEqual(p.encode(g),original)
    def test_correct_unchanged_historical_dependencies(self):
        g=fixture();g,_=add(g,revision(g['records'][0],integrity='mismatched'))
        for i,kw in [(1,{'notes':['Event note']}),(2,{'limitations':['Capture mismatch now known']}),(3,{'rationale':'Updated caution without changing historical endpoint'})]:
            g,_=add(g,revision(g['records'][i],**kw))
        self.assertTrue(view(g)['impacts'][0]['requiresReview'])
    def test_correct_assessment_after_account_correction(self):
        g=fixture('ai-team');assessment=g['records'][-1];g,_=add(g,revision(g['records'][5],limitations=['New limitation']))
        g,_=add(g,revision(assessment,label='insufficient',limitations=['Account changed; retained historical target']))
        self.assertEqual(view(g)['assessments'][0]['label'],'insufficient');self.assertTrue(view(g)['impacts'][-1]['requiresReview'])
    def test_new_account_can_describe_existing_event_with_changed_input(self):
        g=fixture();g,_=add(g,revision(g['records'][0],integrity='mismatched'));g,_=add(g,account(g['records'][1],'new-account'))
        self.assertTrue(view(g)['impacts'][-2]['requiresReview'])
    def test_changed_dependency_pin_requires_current_head(self):
        g=fixture('ai-team');old=g['records'][4];g,new=add(g,revision(old,notes=['Correct event note']))
        g,account2=add(g,revision(g['records'][5],activity=p.pin(new)))
        with self.assertRaises(p.Invalid):add(g,revision(account2,activity=p.pin(old)))
    def test_ascii_calendar_and_newline_strict(self):
        for bad in ['2026-09-21T0١:00:00Z','2026-99-99T09:00:00Z','2026-09-21T09:00:00Z\n']:
            with self.assertRaises(p.Invalid):add(empty(),capture(obtainedAt=bad))
    def test_missing_format_support_fails_closed(self):
        checker=p.FormatChecker();checker.checkers=dict(checker.checkers);checker.checkers.pop('date-time')
        with patch.object(p,'FormatChecker',return_value=checker):
            with self.assertRaisesRegex(p.Invalid,'format checker unavailable'):p.validate_ledger(empty())
    def test_fractional_revision_encoding_rejected(self):
        g=fixture();candidate=copy.deepcopy(g);candidate['records'][-1]['revision']=1.0
        with self.assertRaisesRegex(p.Invalid,'fractional encoding'):p.validate_extension(g,candidate,config())
        r=link(g['records'][0],'float-pin');r['evidence']['revision']=1.0
        with self.assertRaises(p.Invalid):add(g,r)
    def test_actual_prefix_rewrite_rejected(self):
        g=fixture();c=copy.deepcopy(g);c['records'][-1]['rationale']='Rewritten history'
        self.assertTrue(p.validate_ledger(c,config()))
        with self.assertRaisesRegex(p.Invalid,'prefix rewritten'):p.validate_extension(g,c,config())
    def test_cross_revision_self_derivation(self):
        g=fixture('ai-team');original=g['records'][5];g,s=add(g,activity(g['records'][0],'self-cycle',mode='synthesis',inputs=[p.pin(original)]))
        with self.assertRaisesRegex(p.Invalid,'Self-derivation'):add(g,revision(original,activity=p.pin(s)))
    def test_current_capture_failure_visible(self):
        g=fixture();g,_=add(g,revision(g['records'][0],integrity='mismatched'))
        changed=view(g)['impacts'][0]['changedDependencies'];self.assertEqual(changed[0]['currentCaptureState']['integrity'],'mismatched')
    def test_assessment_genesis_semantic_guards(self):
        base=fixture('ai-team');prototype=base['records'][-1];g={**base,'records':base['records'][:-1]}
        for fields,message in [({'scheme':METHOD},'Unknown confidence scheme'),({'assessor':U+'imposter'},'reviewer/method mismatch'),({'method':CLAIM},'reviewer/method mismatch')]:
            r={**copy.deepcopy(prototype),**fields,'id':U+'bad-assessment'}
            with self.assertRaisesRegex(p.Invalid,message):add(g,r)
    def test_snapshot_digest_and_predecessor(self):
        g=fixture();new,_=add(g,revision(g['records'][0],notes=['New metadata']))
        def fact(ledger,n,previous=None):return {'recordType':'fact','path':'provenance.register.snapshot','factId':U+'snapshot'+str(n),'subjectId':ledger['dimension']+':provenance-register','value':ledger,'supersedes':[] if previous is None else [previous['factId']],'provenance':{'snapshotDigest':p.digest(ledger),'previousSnapshotDigest':None if previous is None else p.digest(previous['value'])}}
        f1=fact(g,1);f2=fact(new,2,f1);self.assertTrue(p.validate_snapshot(f1,config()));self.assertTrue(p.validate_snapshot(f2,config(),f1))
        for field in ['snapshotDigest','previousSnapshotDigest']:
            bad=copy.deepcopy(f2);bad['provenance'][field]='sha256:'+'0'*64
            with self.assertRaises(p.Invalid):p.validate_snapshot(bad,config(),f1)
        with self.assertRaises(p.Invalid):p.validate_snapshot(f2,config())
    def test_uniform_read_denial_when_config_expired(self):
        with self.assertRaisesRegex(p.Denied,'^Read denied$'):p.view(None,config(),U+'intruder','research',None,'bad','2030-01-01T00:00:00Z')
    def test_json_size_bound(self):
        with self.assertRaisesRegex(p.Invalid,'8 MiB'):p.encode('x'*(8*1024*1024))

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests);result=unittest.TextTestRunner(verbosity=2).run(suite)
    report={'testsRun':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'passed':result.wasSuccessful()}
    (HERE/'test-results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    if result.wasSuccessful():
        (HERE/'examples').mkdir(exist_ok=True)
        for name in ['startup','group','ai-team']:
            instance=fixture(name);cfg=config();instance['dimension']=cfg['dimension']=U+'dimension:'+name
            for suffix,value in [('.json',instance),('.config.json',cfg)]:
                (HERE/'examples'/(name+suffix)).write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
    raise SystemExit(0 if result.wasSuccessful() else 1)

END FILE test_provenance.py

FILE acceptance.py SHA256 cb4af12bee341836cca5d4dd67eb63598de6ce5d966f896b4229ab63c7131d42
"""Trusted synthetic new-Dimension composition, admission and snapshot checks."""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from datetime import datetime,timedelta,timezone
from pathlib import Path
import provenance as p
HERE=Path(__file__).resolve().parent
PROFILE_ID='vr.profile.enterprise-assertion-provenance'
SLUG='enterprise-assertion-provenance'
def run(composer,skill):
    p.require(__debug__,'Run without -O');composer=Path(composer).resolve();skill=Path(skill).resolve();pins=p.load(HERE/'tool-pins.json')
    for field,root in [('composerFiles',composer),('skillFiles',skill),('upstreamFiles',HERE/'upstream')]:
        for n,h in pins[field].items():p.require(hashlib.sha256((root/n).read_bytes()).hexdigest()==h,'Unexpected trusted asset: '+n)
    sys.path.insert(0,str(composer));import composition as c
    from bootstrap_dimension import bootstrap
    sys.path.insert(0,str(skill/'scripts'));from write_record import append
    from validate_dimension import validate as native_validate
    reports=[];at=c.now();expires=(datetime.now(timezone.utc)+timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    with tempfile.TemporaryDirectory(prefix='vercy-authority-acceptance-') as tmp:
        root=Path(tmp);assets=root/'assets';assets.mkdir()
        def descriptor(folder,name,source,url):
            raw=source.read_bytes();dest=assets/folder/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
            return {'path':folder+'/'+name,'digest':c.digest(raw),'size':len(raw),'mediaType':'application/json' if name.endswith('.json') else 'text/x-python' if name.endswith('.py') else 'text/markdown' if name.endswith('.md') else 'application/yaml','sourceUrl':url}
        def release(mid,version,folder,spec,agents,base,native):
            ds=descriptor(folder,spec.name,spec,base+spec.name);da=descriptor(folder,'AGENTS.md',agents,base+'AGENTS.md');binding=None
            if native:
                binding={'id':'urn:vercy:binding:enterprise-assertion-provenance','version':'0.1.0','forSpecificationDigest':ds['digest'],'runtime':descriptor(folder,'runtime-model.reference.json',HERE/'runtime-model.reference.json',base+'runtime-model.reference.json'),'instanceSchema':descriptor(folder,'provenance.schema.json',HERE/'provenance.schema.json',base+'provenance.schema.json'),'companionValidator':descriptor(folder,'provenance.py',HERE/'provenance.py',base+'provenance.py'),'scope':'Own companion namespace/specification; no parent subtype. Explicit nested validation and admission required.'}
            return {'modelId':mid,'version':version,'namespace':'urn:vercy:model:'+mid,'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','requires':[],'references':[],'specification':ds,'agents':da,'installationMode':'native-binding' if native else 'semantic-only','binding':binding,'semanticFingerprint':None,'compatibility':{'decision':'accepted','reviewer':'urn:synthetic:reviewer:authority','evidence':'urn:synthetic:acceptance:authority','observedAt':at,'scope':'Synthetic candidate-installation exercise, not global parent ratification; publication and research assurance are separate.'}}
        parent='wm-xct-012-provenance';up=HERE/'upstream'/parent
        semantic=release('vr.wm-xct-012','0.3.0-research.1',parent,up/'spec.yaml',up/'AGENTS.md','https://ver.cy/models/enterprise-assertion-provenance/versions/0.1.0/upstream/'+parent+'/',False)
        companion=release(PROFILE_ID,'0.1.0',SLUG,HERE/'spec.json',HERE/'AGENTS.md','https://ver.cy/models/enterprise-assertion-provenance/versions/0.1.0/',True)
        companion['references']=[{'modelId':semantic['modelId'],'version':semantic['version']}];releases=[semantic,companion]
        for name in ['startup','group','ai-team']:
            config=p.load(HERE/('examples/'+name+'.config.json'));fixture=p.load(HERE/('examples/'+name+'.json'));target=root/name;stage=root/(name+'-stage');pp=root/(name+'-policy.json');lp=root/(name+'-lock.json');planp=root/(name+'-plan.json');dimension=config['dimension']
            policy={'format':'vercy-composition-policy','version':1,'id':'urn:synthetic:composition-policy:authority','dimensionId':dimension,'owner':'urn:synthetic:owner:installation','allowInstall':True,'actors':['urn:synthetic:actor:composer'],'purposes':['Synthetic assertion provenance reference'],'allowedModelIds':[r['modelId'] for r in releases],'allowedOrigins':['https://ver.cy'],'reviewers':['urn:synthetic:reviewer:authority'],'allowReviewableDrafts':True,'validFrom':at,'validUntil':expires}
            pp.write_bytes(c.encode(policy));lp.write_bytes(c.encode({'models':[]}))
            plan={'format':'vercy-composition-plan','schemaVersion':'1.0.0','planId':'urn:synthetic:composition:authority:'+name,'revision':1,'supersedes':None,'algorithm':'exact-closure-v1','dimensionId':dimension,'createdAt':at,'validUntil':expires,'baseLockDigest':c.digest(lp.read_bytes()),'roots':[{'modelId':r['modelId'],'version':r['version']} for r in releases],'releases':releases,'authority':{'actor':policy['actors'][0],'allowReviewableDrafts':True,'allowedModelIds':policy['allowedModelIds'],'decision':'allow','owner':policy['owner'],'policyDigest':c.digest(pp.read_bytes()),'policyRef':policy['id'],'purpose':policy['purposes'][0]},'provenance':{'classification':'public-synthetic','evidenceKind':'proposal','masterSystem':'urn:synthetic:reference','recordedAt':at,'source':'urn:synthetic:fixture:'+name}}
            planp.write_bytes(c.encode(plan));c.stage(planp,assets,pp,lp,stage);bootstrap(stage,pp,lp,skill,target,'Synthetic provenance '+name,dimension)
            installed=target/'models/composed'/SLUG/'provenance.py';p.require(c.digest(installed.read_bytes())==companion['binding']['companionValidator']['digest'],'Code differs');p.require(c.digest((installed.parent/'provenance.schema.json').read_bytes())==companion['binding']['instanceSchema']['digest'],'Schema differs')
            ms=importlib.util.spec_from_file_location('installed_authority_'+name,installed);module=importlib.util.module_from_spec(ms);ms.loader.exec_module(module)
            ledger={'format':'vercy-assertion-provenance','version':'0.1.0','dimension':dimension,'records':[]}
            initial=copy.deepcopy(ledger)
            for row in fixture['records']:ledger=module.admit(ledger,row,config,row['writer'],row['recordedAt'])
            p.require(ledger==fixture,'Fixture admission differs');module.validate_extension(initial,ledger,config)
            correction=copy.deepcopy(ledger['records'][0]);correction.update(revision=2,previousDigest=module.digest(correction),change='correct',recordedAt='2026-09-21T10:01:00Z',integrity='mismatched',reason='Synthetic later integrity check')
            updated=module.admit(ledger,correction,config,correction['writer'],correction['recordedAt']);module.validate_extension(ledger,updated,config)
            oid=dimension+':provenance-register';operator='urn:synthetic:register-operator';register='urn:synthetic:governance-register'
            obj={'recordType':'object','schemaVersion':'1.0.0','recordId':oid+':object-r1','objectId':oid,'objectType':PROFILE_ID+':provenance-register','name':'Synthetic provenance register','description':'Own companion namespace, not a ControlRecord or Company','recordedAt':at,'previousRecordId':None,'state':'active','provenance':{'source':register,'synthetic':True},'accessClass':'synthetic-private'}
            path=root/(name+'-object.json');path.write_bytes(p.encode(obj));append(target,'object',path);facts=[]
            for i,snapshot in enumerate([ledger,updated],1):
                fact={'recordType':'fact','schemaVersion':'1.0.0','factId':oid+':snapshot-r'+str(i),'subjectId':oid,'path':'provenance.register.snapshot','value':snapshot,'unit':None,'validFrom':at,'validTo':None,'recordedAt':at,'supersedes':[] if i==1 else [oid+':snapshot-r1'],'status':'asserted','provenance':{'source':register,'synthetic':True,'snapshotDigest':p.digest(snapshot),'previousSnapshotDigest':None if i==1 else p.digest(ledger)},'authority':{'source':operator,'rank':0},'masterSystem':register,'accessClass':'synthetic-private'}
                path=root/(name+'-fact'+str(i)+'.json');path.write_bytes(p.encode(fact));result=append(target,'fact',path);facts.append(target/result['written'])
            stored=[p.load(x)['value'] for x in facts];p.require(stored==[ledger,updated],'Stored round-trip differs');module.validate_extension(stored[0],stored[1],config)
            first,second=[p.load(x) for x in facts];module.validate_snapshot(first,config);module.validate_snapshot(second,config,first)
            bad_pin=copy.deepcopy(second);bad_pin['provenance']['snapshotDigest']='sha256:'+'0'*64
            pin_rejected=False
            try:module.validate_snapshot(bad_pin,config,first)
            except module.Invalid:pin_rejected=True
            p.require(pin_rejected,'Native snapshot digest mismatch was accepted')
            def evaluate(snapshot):return module.view(snapshot,config,actor='urn:synthetic:reader',purpose='research',claim=fixture['records'][2]['claim'],knownAt='2026-09-21T12:00:00Z',now='2026-09-21T12:00:00Z')
            decisions=[evaluate(x) for x in stored]
            p.require(decisions[0]['truth']=='not-evaluated' and decisions[1]['impacts'][0]['requiresReview'],'Stored provenance outcomes differ')
            native=native_validate(target);p.require(native['valid'],'Native validation failed');victim=facts[-1];original=victim.read_bytes();bad=p.load(victim);bad['value']['records'][0]['representationDigest']='invalid';victim.write_bytes(p.encode(bad));negative=native_validate(target);rejected=False
            try:module.validate_ledger(p.load(victim)['value'],config)
            except module.Invalid:rejected=True
            finally:victim.write_bytes(original)
            p.require(negative['valid'] and rejected,'Native/companion distinction missing')
            truncated=p.load(victim);truncated['value']=copy.deepcopy(stored[0]);truncated['value']['records'].pop();victim.write_bytes(p.encode(truncated));truncation_rejected=False
            try:module.validate_extension(stored[0],p.load(victim)['value'],config)
            except module.Invalid:truncation_rejected=True
            finally:victim.write_bytes(original)
            p.require(truncation_rejected,'Snapshot truncation was accepted');native.pop('dimension',None);negative.pop('dimension',None)
            reports.append({'profile':name,'dimension':dimension,'objects':1,'facts':2,'native':native,'roundTripEqualsInput':True,'admissionReplayedThroughInstalledCompanion':True,'snapshotTruncationRejected':True,'snapshotDigestMismatchRejected':pin_rejected,'storedDecisions':decisions,'invalidNestedSnapshot':{'native':negative,'companionRejected':rejected},'envelopeOperator':operator,'envelopeAuthorityMeaning':'Snapshot storage only; never domain fact precedence','pins':[{'id':r['modelId'],'version':r['version'],'digest':r['specification']['digest'],'mode':r['installationMode']} for r in releases]})
    return {'format':'vercy-provenance-profile-acceptance','executedAt':c.now(),'passed':len(reports),'failed':0,'profiles':reports,'sourceDigests':{str(x.relative_to(HERE)):hashlib.sha256(x.read_bytes()).hexdigest() for x in [Path(__file__),HERE/'provenance.py',HERE/'provenance.schema.json',HERE/'spec.json',HERE/'tool-pins.json',*sorted((HERE/'examples').glob('*.json'))]},'limits':'Synthetic new Dimensions; semantic-only parent plus separately identified companion. Candidate-installation metadata anticipates publication. No IAM, source truth, durable concurrency or existing-Dimension migration proof.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True);args=ap.parse_args();report=run(args.composer,args.skill);Path(args.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':report['passed'],'failed':report['failed']}))

END FILE acceptance.py

FILE AGENTS.md SHA256 956411df8c86b3fe6c324f2efe7ee281f7842a5e1d807f597bb063480e3d82f9
# Agent use

Read model-spec.md, provenance.schema.json and provenance.py before using the register. Read spec.json for the normative Bundle/Layer/Finding/Question/Artifact/Action tree. Unknown context stays unknown. A source assertion or AI inference never becomes direct observation from repetition or human approval.

Use only a trusted host that authenticates callers, owns the complete current root/configuration and supplies the receipt clock. Static validation/import do not authenticate history. Invoke admit on every new row, validate_extension against the latest trusted root, and the companion on every nested native snapshot. Do not expose the full returned ledger or diagnostics to a write-only caller. Denial is all-register; partial views are unsupported.

Preserve withdrawn records, conflicting evidence, changed-dependency warnings and distinct role attribution. A digest is not truth, consent or verified authorship. Do not infer independence, average qualitative labels, contact people, fetch sources or change external claims automatically. The package grants no operational permission. Native storage operator is distinct from source authors/assessors.

No Python -O requirement is needed for enforcement: production require() checks do not use assert. Runtime dependency: Python 3.11+ and jsonschema with URI/date-time format support. Resolve methods and external claims under separately governed host policies.

The acceptance harness itself requires normal non-optimized execution. The companion explicitly fails closed if URI/date-time checkers are missing, parses every timestamp as canonical ASCII UTC, and rejects fractional revision encodings. Enforce request limits before parsing; the companion also caps serialized JSON at 8 MiB.

Retained historical pins remain valid for metadata corrections; only newly introduced/changed immediate references must name current active heads. Historical dependencies stay visible as requiring review. Call validate_snapshot on native facts to check aggregate identity, exact snapshot digest and predecessor linkage, then perform native V3 validation separately. A new snapshot still requires the host's trusted latest predecessor.

END FILE AGENTS.md

FILE whole-object-coverage.yaml SHA256 3e3d3d9cdf476cd4b0aed1226aa87b4d05382a2a20f735f649209b70629c3f91
{"Capture":{"identity-class":{"disposition":"required","reason":"Source, representation, acquisition time and mode anchors"},"direct-properties":{"disposition":"required","reason":"Availability, optional digest/author/origin and declared integrity"},"recognition-observation":{"disposition":"required","reason":"Capture mode/subject/time consistency; no live connector proof"},"capabilities-behaviour-actions":{"disposition":"required","reason":"Record metadata correction or terminal withdrawal; new acquisition gets new ID"},"context-evidence":{"disposition":"required","reason":"Source identity/version and origin declarations, recorder and limitations"}},"Activity":{"identity-class":{"disposition":"required","reason":"One occurrence with stable mode/actor/time/method/inputs"},"direct-properties":{"disposition":"required","reason":"Exact prior input pins and optional observed target"},"recognition-observation":{"disposition":"required","reason":"Typed input and interval checks, declared execution only"},"capabilities-behaviour-actions":{"disposition":"required","reason":"Create a new ID for a new run; correct notes or withdraw"},"context-evidence":{"disposition":"required","reason":"Method pin, executing actor and source inputs"}},"ProvenanceRecord":{"identity-class":{"disposition":"required","reason":"Asserter plus pinned claim, subject and epistemic kind"},"direct-properties":{"disposition":"required","reason":"Activity pin and explicit limitations"},"recognition-observation":{"disposition":"required","reason":"Kind-specific activity/subject consistency"},"capabilities-behaviour-actions":{"disposition":"required","reason":"Correct activity reference or limitations; withdraw; changed kind/claim gets new ID"},"context-evidence":{"disposition":"required","reason":"External claim content delegated to its pinned owner; local input closure retained"}},"EvidenceLink":{"identity-class":{"disposition":"required","reason":"Pinned source/target endpoints, relation kind and author"},"direct-properties":{"disposition":"required","reason":"Selector and explicit rationale"},"recognition-observation":{"disposition":"required","reason":"Exact local source pin and external target pin; selector not executed"},"capabilities-behaviour-actions":{"disposition":"required","reason":"Revise rationale/selector; withdraw; new endpoint or polarity gets new ID"},"context-evidence":{"disposition":"required","reason":"No inherited source authorship, veracity or support default"}},"ConfidenceAssessment":{"identity-class":{"disposition":"required","reason":"Exact account, assessor, purpose, method and scheme"},"direct-properties":{"disposition":"required","reason":"Qualitative label, basis, review activity and limitations"},"recognition-observation":{"disposition":"required","reason":"Reviewer/method/target consistency; quality of judgement external"},"capabilities-behaviour-actions":{"disposition":"required","reason":"Correct label/basis explicitly or withdraw; new independent judgement gets new ID"},"context-evidence":{"disposition":"required","reason":"No numeric probability, score aggregation or cross-method conversion"}},"ProvenanceRegister":{"identity-class":{"disposition":"required","reason":"One aggregate per Dimension: dimension URI plus provenance-register suffix"},"direct-properties":{"disposition":"required","reason":"Versioned header, complete ordered records and immutable snapshot digest"},"recognition-observation":{"disposition":"required","reason":"Full structural/history validation; completeness requires trusted previous root"},"capabilities-behaviour-actions":{"disposition":"required","reason":"Append authorized records, verify extension; no delete or partial projection"},"context-evidence":{"disposition":"required","reason":"Host config and operator; external claim mastership not transferred"}}}
END FILE whole-object-coverage.yaml

EXACT SEMANTIC CONTRACT DIFF
--- original/model-spec.md
+++ revised/model-spec.md
@@ -19,9 +19,9 @@
 
 ## Fields and value rules
 
-`provenance.schema.json` is the closed field/type/cardinality definition. All listed keys are required. Unknown keys, inline secrets, executable extensions and external schema fetching are unsupported. Arrays may be empty unless minItems says otherwise; each has a finite maximum. Null means explicitly unknown or inapplicable, never zero. SourceVersion/sourceAuthor/originRef may be null; an unavailable Capture requires a null representationDigest and not-tested integrity. Every reference pin requires URI id, positive integer revision and `sha256:` plus 64 lowercase hex digits. External pin truth, target existence and actual byte correspondence are not verified by this reference.
+`provenance.schema.json` is the closed field/type/cardinality definition. All listed keys are required. Unknown keys, inline secrets, executable extensions and external schema fetching are unsupported. Arrays may be empty unless minItems says otherwise; each has a finite maximum. Serialized JSON is capped at 8 MiB; the host must also enforce byte limits before parsing untrusted input. This is not a throughput guarantee. Null means explicitly unknown or inapplicable, never zero. SourceVersion/sourceAuthor/originRef may be null; an unavailable Capture requires a null representationDigest and not-tested integrity. Every reference pin requires URI id, positive integer revision and `sha256:` plus 64 lowercase hex digits. Fractional encodings such as 1.0 and booleans are rejected for revisions. External pin truth, target existence and actual byte correspondence are not verified by this reference.
 
-Every inner record has id, kind, scope, positive revision, nullable previousDigest, recordedAt, writer, state, change, reason and notes. Genesis has revision 1, previousDigest null, state active and change create. UTC timestamps use seconds and real calendar values. Receipt order is globally strictly increasing: this serial reference admits one new record per second. The host supplies receipt time. Capture obtainedAt and Activity endedAt cannot follow receipt; Activity startedAt ≤ endedAt. External business-valid time stays with the pinned claim; this reference does not invent an effective-time interval for its truth.
+Every inner record has id, kind, scope, positive revision, nullable previousDigest, recordedAt, writer, state, change, reason and notes. Genesis has revision 1, previousDigest null, state active and change create. Every timestamp is independently parsed as a strict ASCII UTC instant with second precision and a real calendar date; Unicode digits and trailing newlines reject. Canonical UTC lexical order equals chronological order. Missing URI/date-time format support fails closed. Receipt order is globally strictly increasing: this serial reference admits one new record per second. The host supplies receipt time. Capture obtainedAt and Activity endedAt cannot follow receipt; Activity startedAt ≤ endedAt. External business-valid time stays with the pinned claim; this reference does not invent an effective-time interval for its truth.
 
 Capture.mode is file/live-api/manual; availability is captured/unavailable; integrity is not-tested/matched/mismatched. Integrity and origin are **recorded declarations**, not results of an implemented fetch/signature verifier. A digest binds declared content, not authenticity or truth. Changing availability from unavailable to captured creates a new Capture, since it represents a new acquisition. Mode, sourceRef, sourceVersion, aboutRef, obtainedAt, availability and representationDigest are immutable anchors.
 
@@ -37,7 +37,7 @@
 
 ## Three separate graphs
 
-Internal reliance references pin already admitted, active, current record revisions in the same scope. Typed targets are checked. Each reference points backwards in receipt order, so the local derivation graph cannot cycle. An input's known capture/producing-activity time cannot follow the consuming activity's end. Unknown production time is not invented. Corrections also cannot introduce self-reference. New reliance on an already superseded/withdrawn revision is rejected; older historical reliance remains interpretable. Withdrawal creates no new reliance and preserves old references even when they have since changed. External claim/source/party references may form arbitrary external graphs; this module never traverses them.
+Every new or changed immediate internal reference must pin an already admitted active current revision in the same scope. An unchanged immediate pin retained in a correction instead resolves the exact historical revision: metadata maintenance must remain possible after its dependency changes. Indirect dependencies of an existing Activity likewise retain their original pins. These historical references are not upgraded or treated as fresh; the view continues to report changed/withdrawn dependency warnings. Typed targets and scope are always checked. Each pin points backwards in receipt order, so the revision graph cannot cycle. In addition, a record's transitive dependency closure must not contain any earlier revision of its own ID: an account cannot become generated by a later synthesis of itself. An input's known capture/producing-activity time cannot follow the consuming activity's end. Unknown production time is not invented. Withdrawal creates no new reliance and preserves old references even when they have since changed. External claim/source/party references may form arbitrary external graphs; this module never traverses them.
 
 Specification imports are empty. WM-XCT-012, WM-XCT-026 and WM-XCT-028 are exact **semantic references** with their published holds retained, not executable package dependencies or subtype assertions. Native installation optionally installs WM-XCT-012 semantic-only and the companion under its own ID `vr.profile.enterprise-assertion-provenance`. Package files and record relationships are not interchangeable with either graph.
 
@@ -45,7 +45,7 @@
 
 `admit(previous, record, config, actor, now)` is a pure host-internal operation. The trusted host authenticates actor, chooses the current complete root/configuration and clock, and prevents concurrent updates. Config contains dimension, validFrom/validUntil, explicit `(kind,scope,actors)` grants, full-register readers and purposes. Validity is half-open. A matching grant permits recording/correcting/withdrawing records of that type and scope; claimed authorship alone grants nothing. A changed authorized writer can record a correction while preserving earlier attribution. Record.writer must match the supplied caller. No network IAM, signature or durable transaction service is implemented.
 
-A correction follows the immediate previous revision and digest, retains all prior rows and immutable anchors, and remains active. Withdrawal is terminal and changes only revision, previousDigest, receipt, writer, state, change and reason. It cannot rewrite the withdrawn content. Resurrecting, deleting or truncating records is unsupported. Retracting a capture/account/link or correcting its basis does not automatically negate an external claim or alter downstream epistemic kinds; a view reports the affected dependency pins for reassessment.
+A correction follows the immediate previous revision and digest, retains all prior rows and immutable anchors, and remains active. Unchanged historical dependencies may be retained when correcting notes, limitations, selectors, rationale or an assessment label. Newly introduced/replaced immediate pins must be current and active. Correcting a judgement about an older account does not retarget it to the latest account; a fresh review needs a new review Activity and assessment. Withdrawal is terminal and changes only revision, previousDigest, receipt, writer, state, change and reason. It cannot rewrite the withdrawn content. Resurrecting, deleting or truncating records is unsupported. Retracting a capture/account/link or correcting its basis does not automatically negate an external claim or alter downstream epistemic kinds; a view reports the affected dependency pins for reassessment.
 
 Repeated `(id,revision)` admission is a no-op only for the identical payload, ignoring solely a newly restamped receipt and retaining the first receipt. Current authorization and receipt-now equality are rechecked. Conflicting replay rejects without mutation. `validate_extension` requires equal register headers, valid histories and the exact previous records as a prefix. It requires the host's trusted latest previous root; it cannot discover a missing newer root or prove that an arbitrary imported snapshot was authorized. Static validation checks consistency, not historical authorization. A host must call admit for each appended record and return only a receipt or generic rejection to write-only callers, never the entire returned ledger or raw diagnostics.
 
@@ -53,7 +53,7 @@
 
 `view` gates the current reader and purpose **before ledger or query diagnostics**. A reader must be cleared for the whole register. Denial exposes no hidden IDs, counts or contrary-evidence indicators. No partial filtering, anonymous projection, redaction or retention/erasure guarantee is supplied. Configuration diagnostics are trusted-host details, never public endpoint responses.
 
-At a nonfuture knowledge cut, the view selects the latest known revision per ID. It returns all accounts and links for the exact claim pin, including withdrawn current heads, and assessments whose pinned account addresses that claim. It reports transitive changed/withdrawn dependencies and unavailable/integrity-mismatched Capture bases. `context-available` means an active non-unverified account exists; it is **not** a ready-to-rely verdict. `insufficient-context` does not mean false. Every result explicitly says truth not-evaluated and permissions not-inferred. Input-slice and configuration digests pin reproducibility inputs, not signed publication.
+At a nonfuture knowledge cut, the view selects the latest known revision per ID. It returns all accounts and links for the exact claim pin, including withdrawn current heads, and assessments whose pinned account addresses that claim. It reports transitive changed/withdrawn dependencies and unavailable/integrity-mismatched Capture bases. A changed Capture also exposes its current availability/integrity, explicitly distinguished from the historical cited pin. `context-available` means an active non-unverified account exists; it is **not** a ready-to-rely verdict. `insufficient-context` does not mean false. Every result explicitly says truth not-evaluated and permissions not-inferred. Input-slice and configuration digests pin reproducibility inputs, not signed publication.
 
 Known shared representation digests or declared origin URIs across active accounts produce known-shared-origin, with the basis disclosed to the already authorized reader. All other independence results are unknown. Distinct files, sources, IDs, roots, authors and digests never prove independence. The origin URI is an attributed declaration and shared bytes are an overlap signal, not authenticated historical provenance. Evidence can change independently of its claim; prior knowledge views preserve the original dependency state.
 
@@ -64,3 +64,5 @@
 A startup needs only trusted host configuration, an external claim pin, one file Capture, acquisition Activity and source-asserted account; evidence links and assessments are optional. The group fixture keeps opposing evidence and recognizes a shared input. The AI fixture preserves inferred kind after a separately attributed human review. These fixtures make no claim about actual organizations. `test_provenance.py` and `acceptance.py` record executed coverage and native limitations separately.
 
 The normative `spec.json` also contains the full Bundle → Layer → Finding → Question → Artifact → Action tree. Unknown answers require the named missing context; listed actions confer no new authority. Sector/legal/clinical/forensic profiles, independent-source proof, PKI, external connectors, probabilistic calibration, fine-grained disclosure, erasure, concurrent durable storage, and existing-Dimension transactional migration remain deferred.
+
+`validate_snapshot(fact, config, previous)` additionally checks the aggregate subject, nested history, snapshotDigest, previousSnapshotDigest and supersedes relationship. A non-genesis snapshot requires the host's trusted previous snapshot. Use native V3 validation separately for the full envelope; neither check authenticates the supplied root. Hash prefixes use exact canonical JSON encoding, not Python value equality. Source files and native assets are separately pinned by their actual byte hashes.

END DIFF

FULL NORMATIVE STRUCTURE
{"bundles":[{"id":"AP-SOURCE","name":"Sources and execution","description":"Sources and execution for the bounded assertion-provenance contract.","layers":[{"id":"AP-CAPTURE","name":"Captured representations","description":"Collect explicit context and preserve unknowns. See the semantic contract for exact rules.","findings":[{"id":"AP-F01","name":"What was directly acquired, and by whom?","description":"What was directly acquired, and by whom? Separate capture from claim truth","questions":[{"id":"Q01","text":"What was directly acquired, and by whom? Separate capture from claim truth","kind":"governed-context","answer_data":["Capture and Activity and representation pin","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A01","name":"Capture and Activity and representation pin","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT01","description":"Show acquisition account; never infer source truth"}]},{"id":"AP-F05","name":"What survives rename or relocation?","description":"What survives rename or relocation? Distinguish source location and identity","questions":[{"id":"Q05","text":"What survives rename or relocation? Distinguish source location and identity","kind":"governed-context","answer_data":["Qualified external pin","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A05","name":"Qualified external pin","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT05","description":"Retain ID; record a new acquisition if content changes"}]},{"id":"AP-F18","name":"Which representation and which execution event are being described?","description":"Which representation and which execution event are being described? Keep their identities separate","questions":[{"id":"Q18","text":"Which representation and which execution event are being described? Keep their identities separate","kind":"governed-context","answer_data":["Capture and Activity pins, event and receipt times","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A18","name":"Capture and Activity pins, event and receipt times","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT18","description":"Record one representation and a separately identified event; reject incompatible declaration"}]}]},{"id":"AP-EVENT","name":"Execution activities","description":"Collect explicit context and preserve unknowns. See the semantic contract for exact rules.","findings":[{"id":"AP-F02","name":"Is this source-asserted, inferred or proposed?","description":"Is this source-asserted, inferred or proposed? Separate account and activity kind","questions":[{"id":"Q02","text":"Is this source-asserted, inferred or proposed? Separate account and activity kind","kind":"governed-context","answer_data":["ProvenanceRecord plus generation method","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A02","name":"ProvenanceRecord plus generation method","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT02","description":"Explain declared kind and its limits"}]},{"id":"AP-F06","name":"Correction or a new acquisition/assessment?","description":"Correction or a new acquisition/assessment? Preserve activity identity","questions":[{"id":"Q06","text":"Correction or a new acquisition/assessment? Preserve activity identity","kind":"governed-context","answer_data":["Change reason and predecessor pin","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A06","name":"Change reason and predecessor pin","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT06","description":"Correct metadata or mint a genuinely new event"}]}]}]},{"id":"AP-ACCOUNT","name":"Assertion accounts","description":"Assertion accounts for the bounded assertion-provenance contract.","layers":[{"id":"AP-GRAIN","name":"Claim and account boundary","description":"Collect explicit context and preserve unknowns. See the semantic contract for exact rules.","findings":[{"id":"AP-F04","name":"Is this the claim, its account or its evidence?","description":"Is this the claim, its account or its evidence? Preserve grain","questions":[{"id":"Q04","text":"Is this the claim, its account or its evidence? Preserve grain","kind":"governed-context","answer_data":["Typed IDs and external target reference","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A04","name":"Typed IDs and external target reference","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT04","description":"Resolve exact record kind"}]},{"id":"AP-F09","name":"Which system masters which data?","description":"Which system masters which data? Avoid a new master for the external claim","questions":[{"id":"Q09","text":"Which system masters which data? Avoid a new master for the external claim","kind":"governed-context","answer_data":["Mastership matrix","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A09","name":"Mastership matrix","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT09","description":"Link to the owning system"}]}]},{"id":"AP-HISTORY","name":"Historical reliance","description":"Collect explicit context and preserve unknowns. See the semantic contract for exact rules.","findings":[{"id":"AP-F03","name":"How is an unreliable account withdrawn?","description":"How is an unreliable account withdrawn? Preserve immutable history","questions":[{"id":"Q03","text":"How is an unreliable account withdrawn? Preserve immutable history","kind":"governed-context","answer_data":["Retraction revision and impact report","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A03","name":"Retraction revision and impact report","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT03","description":"Append an authorized withdrawal; propose re-review"}]},{"id":"AP-F10","name":"What was known at a particular time?","description":"What was known at a particular time? Keep occurrence/capture/receipt separate","questions":[{"id":"Q10","text":"What was known at a particular time? Keep occurrence/capture/receipt separate","kind":"governed-context","answer_data":["As-of history with exact pins","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A10","name":"As-of history with exact pins","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT10","description":"Read historical account without rewriting it"}]},{"id":"AP-F11","name":"Which state transitions are allowed?","description":"Which state transitions are allowed? Distinguish account lifecycle from kind","questions":[{"id":"Q11","text":"Which state transitions are allowed? Distinguish account lifecycle from kind","kind":"governed-context","answer_data":["Transition table and immutable revisions","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A11","name":"Transition table and immutable revisions","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT11","description":"Admit authorized creation/correction/withdrawal"}]}]}]},{"id":"AP-REVIEW","name":"Evidence and assessment","description":"Evidence and assessment for the bounded assertion-provenance contract.","layers":[{"id":"AP-EVIDENCE","name":"Evidence relationships","description":"Collect explicit context and preserve unknowns. See the semantic contract for exact rules.","findings":[{"id":"AP-F07","name":"What is missing or disputed?","description":"What is missing or disputed? No selected truth from absent evidence","questions":[{"id":"Q07","text":"What is missing or disputed? No selected truth from absent evidence","kind":"governed-context","answer_data":["Evidence links and explicit limitations","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A07","name":"Evidence links and explicit limitations","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT07","description":"Return insufficient-context and known gaps"}]},{"id":"AP-F12","name":"Which links and cardinalities are required?","description":"Which links and cardinalities are required? No dangling executable references","questions":[{"id":"Q12","text":"Which links and cardinalities are required? No dangling executable references","kind":"governed-context","answer_data":["Closed schema and local graph check","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A12","name":"Closed schema and local graph check","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT12","description":"Reject malformed or unresolved internal pins"}]},{"id":"AP-F16","name":"Are multiple citations independent?","description":"Are multiple citations independent? Repetition is not corroboration","questions":[{"id":"Q16","text":"Are multiple citations independent? Repetition is not corroboration","kind":"governed-context","answer_data":["Declared origin paths and overlap flags","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A16","name":"Declared origin paths and overlap flags","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT16","description":"Flag shared inputs; never count distinct roots as proof"}]}]},{"id":"AP-ASSESS","name":"Qualified confidence","description":"Collect explicit context and preserve unknowns. See the semantic contract for exact rules.","findings":[{"id":"AP-F17","name":"Can two confidence values be compared?","description":"Can two confidence values be compared? Method and scale matter","questions":[{"id":"Q17","text":"Can two confidence values be compared? Method and scale matter","kind":"governed-context","answer_data":["Exact assessment and scheme pins","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A17","name":"Exact assessment and scheme pins","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT17","description":"Refuse automatic cross-scheme arithmetic"}]}]}]},{"id":"AP-GOV","name":"Governance and adoption","description":"Governance and adoption for the bounded assertion-provenance contract.","layers":[{"id":"AP-RIGHTS","name":"Rights and disclosure","description":"Collect explicit context and preserve unknowns. See the semantic contract for exact rules.","findings":[{"id":"AP-F08","name":"Who may change this record?","description":"Who may change this record? Authorship is not authentication","questions":[{"id":"Q08","text":"Who may change this record? Authorship is not authentication","kind":"governed-context","answer_data":["Host-owned writer configuration","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A08","name":"Host-owned writer configuration","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT08","description":"Validate current scope; emit generic rejection"}]},{"id":"AP-F13","name":"What can this reader see for this purpose?","description":"What can this reader see for this purpose? Avoid evidence leakage","questions":[{"id":"Q13","text":"What can this reader see for this purpose? Avoid evidence leakage","kind":"governed-context","answer_data":["Full-register projection gate","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A13","name":"Full-register projection gate","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT13","description":"Return full permitted view or generic denial"}]},{"id":"AP-F15","name":"What can an agent conclude or propose?","description":"What can an agent conclude or propose? Keep evidence distinct from permission","questions":[{"id":"Q15","text":"What can an agent conclude or propose? Keep evidence distinct from permission","kind":"governed-context","answer_data":["Impact report and agent guide","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A15","name":"Impact report and agent guide","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT15","description":"Explain and propose a check; do not contact, publish or change rights"}]}]},{"id":"AP-ADOPT","name":"Minimal composition and migration","description":"Collect explicit context and preserve unknowns. See the semantic contract for exact rules.","findings":[{"id":"AP-F14","name":"What is the smallest useful setup?","description":"What is the smallest useful setup? Optional confidence, no mandatory ERP","questions":[{"id":"Q14","text":"What is the smallest useful setup? Optional confidence, no mandatory ERP","kind":"governed-context","answer_data":["Startup capture/account example","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A14","name":"Startup capture/account example","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT14","description":"Compose the bounded companion"}]},{"id":"AP-F19","name":"Does the native envelope validate the inner history?","description":"Does the native envelope validate the inner history? Check both layers","questions":[{"id":"Q19","text":"Does the native envelope validate the inner history? Check both layers","kind":"governed-context","answer_data":["Native report, installed schema and companion report","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A19","name":"Native report, installed schema and companion report","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT19","description":"Validate nested register and extension against trusted prior root"}]},{"id":"AP-F20","name":"Can this old payload be imported without losing semantics?","description":"Can this old payload be imported without losing semantics? Preserve unknowns","questions":[{"id":"Q20","text":"Can this old payload be imported without losing semantics? Preserve unknowns","kind":"governed-context","answer_data":["Migration decision and exact source pins","If unavailable: insufficient-context; name the missing pin, record, policy or evidence instead of inferring it."]}],"artifacts":[{"id":"AP-A20","name":"Migration decision and exact source pins","description":"Exact records or reproducible report; no inferred truth or permissions."}],"actions":[{"id":"AP-ACT20","description":"Accept same-version lossless snapshot only; stage other mappings for review"}]}]}]}]}
END STRUCTURE
FINAL SENTINEL: AP-REMEDIATED-62-THREE-DIMENSIONS
