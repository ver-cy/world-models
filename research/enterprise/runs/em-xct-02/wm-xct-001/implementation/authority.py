"""Enterprise Fact Authority 0.1.0. Trusted-input, in-memory reference only.

No authentication, durable transactions, signature verification or ACL service.
Call admit for live changes; validate_ledger alone does not prove admission.
"""
from pathlib import Path
import copy,hashlib,json,re
from datetime import datetime
from jsonschema import Draft202012Validator,FormatChecker

HERE=Path(__file__).resolve().parent
class Invalid(ValueError): pass
class Denied(ValueError): pass
def require(ok,message):
    if not ok: raise Invalid(message)
def encode(x):
    try:return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode('utf-8')
    except (ValueError,UnicodeError,TypeError) as e:raise Invalid('Not portable JSON') from e
def digest(x):return hashlib.sha256(encode(x)).hexdigest()
def load(path):return json.loads(Path(path).read_text(encoding='utf-8'))
def stamp(x):
    require(isinstance(x,str) and re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z',x),'UTC seconds required')
    try:datetime.strptime(x,'%Y-%m-%dT%H:%M:%SZ')
    except ValueError as e:raise Invalid('Invalid calendar date') from e
    return x
def schema(x,kind):
    encode(x)
    checker=FormatChecker();require('uri' in checker.checkers and 'date-time' in checker.checkers,'Install jsonschema[format-nongpl]')
    doc=load(HERE/'authority.schema.json');doc={'$ref':'#/$defs/'+kind,'$defs':doc['$defs'],'$schema':doc['$schema']}
    errors=sorted(Draft202012Validator(doc,format_checker=checker).iter_errors(x),key=lambda e:str(e.path))
    require(not errors,'Schema error: '+('; '.join(str(e.message) for e in errors[:3])))
def interval(x):
    stamp(x['validFrom']);stamp(x['validUntil']);require(x['validFrom']<x['validUntil'],'Empty/reversed interval')
def active(x,t):return x['validFrom']<=t<x['validUntil']
def key(x):return (x['scope'],x['predicate'])
def current(rows,known):
    result={}
    for x in rows:
        if x['recordedAt']<=known:result[x['id']]=x
    return list(result.values())
def policies(ledger,scope,predicate,valid,known):
    return [x for x in current(ledger['authorities'],known) if key(x)==(scope,predicate) and x['state']=='active' and active(x,valid)]
def root_check(config,now):
    schema(config,'config');interval(config);stamp(now)
    require(active(config,now),'Trusted configuration is not current')
def validate_record(x,kind):
    schema(x,kind);interval(x);stamp(x['recordedAt'])
    if kind=='authority':
        seen=set()
        actors={x['issuedBy'],x['accountable'],*(s['party'] for s in x['stewardships']),*(r['source'] for r in x['rules']),*(r['source'] for r in x['writeGrants'])}
        actors.update(w for g in x['writeGrants'] for w in g['writers'])
        for row in x['stewardships']+x['rules']+x['writeGrants']:
            require(row['id'] not in seen,'Duplicate aggregate part ID');seen.add(row['id']);interval(row)
            require(row['id'] not in actors,'Part ID must differ from party/source/actor identity')
            require(x['validFrom']<=row['validFrom'] and row['validUntil']<=x['validUntil'],'Part outside authority interval')
    # A tagged string preserves domain lexical semantics; no implicit coercion.
def validate_ledger(ledger,config):
    schema(config,'config');interval(config);schema(ledger,'ledger')
    require(ledger['dimension']==config['dimension'],'Dimension mismatch')
    ids=set();record_times=[];parts={}
    for collection,kind in [('authorities','authority'),('observations','observation')]:
        heads={}
        for x in ledger[collection]:
            validate_record(x,kind);record_times.append(x['recordedAt'])
            require(x['dimension']==ledger['dimension'],'Cross-Dimension record')
            old=heads.get(x['id'])
            if old is None:
                require(x['id'] not in ids,'ID reused between record kinds');ids.add(x['id'])
                require(x['revision']==1 and x['previousDigest'] is None and x['change']=='genesis' and x['state']!='retracted','Missing genesis')
            else:
                require(x['revision']==old['revision']+1 and x['previousDigest']==digest(old),'Broken revision chain')
                require(x['recordedAt']>old['recordedAt'],'Receipt order not increasing')
                require(x['change']!='genesis','Repeated genesis')
                stable=['dimension','scope','predicate']+(['subject','source'] if kind=='observation' else [])
                require(all(x[k]==old[k] for k in stable),'Immutable anchor changed')
                if x['change']=='closure':
                    require(x['validUntil']<old['validUntil'],'Closure must reduce the end')
                    expected=copy.deepcopy(old);expected['validUntil']=x['validUntil']
                    if kind=='authority':
                        for item in expected['rules']+expected['stewardships']+expected['writeGrants']:item['validUntil']=min(item['validUntil'],x['validUntil'])
                    exempt={'revision','previousDigest','recordedAt','change','evidence','issuedBy' if kind=='authority' else 'writer'}
                    require(all(x[k]==v for k,v in expected.items() if k not in exempt),'Closure changed more than the term end')
            require((x['state']=='retracted')==(x['change']=='retraction'),'Retraction change/state mismatch')
            require(not heads or x['recordedAt']>max(h['recordedAt'] for h in heads.values()),'Collection is not receipt-ordered')
            heads[x['id']]=x
            if kind=='authority':
                for part_kind,items in [('stewardship',x['stewardships']),('rule',x['rules']),('writeGrant',x['writeGrants'])]:
                    for item in items:
                        identity=(x['id'],part_kind,item['party'] if part_kind=='stewardship' else item['source'])
                        require(item['id'] not in parts or parts[item['id']]==identity,'Aggregate part identity changed')
                        parts[item['id']]=identity
    require(len(record_times)==len(set(record_times)),'Receipt seconds must be unique across register')
    require(not ids.intersection(parts),'Part ID collides with record ID')
    return True
def validate_extension(previous,candidate,config):
    """Trusted adapter check against a trusted previous complete snapshot."""
    validate_ledger(previous,config);validate_ledger(candidate,config)
    require(all(previous[k]==candidate[k] for k in ['format','version','dimension']),'Snapshot header changed')
    old_times=[x['recordedAt'] for c in ['authorities','observations'] for x in previous[c]]
    for c in ['authorities','observations']:
        require(len(candidate[c])>=len(previous[c]) and encode(candidate[c][:len(previous[c])])==encode(previous[c]),'Snapshot history truncated or rewritten')
        require(not old_times or all(x['recordedAt']>max(old_times) for x in candidate[c][len(previous[c]):]),'Extension backdates receipt')
    return True
def empty(dimension):return {'format':'vercy-fact-authority','version':'0.1.0','dimension':dimension,'authorities':[],'observations':[]}
def authority_for_write(ledger,scope,predicate,source,actor,now):
    matches=policies(ledger,scope,predicate,now,now)
    require(len(matches)==1,'Unknown or contested write authority')
    rules=[r for r in matches[0]['writeGrants'] if r['source']==source and actor in r['writers'] and active(r,now)]
    require(len(rules)==1,'Writer/source is not uniquely authorized')
    # No priority is read here. Multiple grants are deliberately ambiguous.
    require(sum(r['source']==source and active(r,now) for r in matches[0]['writeGrants'])==1,'Overlapping write grants')
def admit(ledger,record,kind,config,actor,now):
    """Pure atomic append; caller supplies authenticated actor and trusted receipt.

    Returns a new ledger to the TRUSTED HOST ONLY, never directly to an API client.
    Same payload replay ignores a restamped recordedAt, retaining the old receipt.
    The host must return a receipt/generic errors, not this full ledger or diagnostics.
    No caller-controlled clock, configuration or stale/incomplete ledger in a service.
    """
    require(kind in ['authority','observation'],'Unsupported record kind')
    root_check(config,now);validate_ledger(ledger,config);validate_record(record,kind)
    require(record['dimension']==config['dimension'],'Dimension mismatch')
    if kind=='authority':
        require(record['issuedBy']==actor,'Issuer mismatch')
        require(any(g['actor']==actor and key(g)==key(record) for g in config['governors']),'No scoped governance permission')
    else:
        require(record['writer']==actor,'Writer mismatch')
        authority_for_write(ledger,record['scope'],record['predicate'],record['source'],actor,now)
    collection='authorities' if kind=='authority' else 'observations'
    for old in ledger[collection]:
        if (old['id'],old['revision'])==(record['id'],record['revision']):
            require(encode({k:v for k,v in old.items() if k!='recordedAt'})==encode({k:v for k,v in record.items() if k!='recordedAt'}),'Conflicting replay');return copy.deepcopy(ledger)
    require(record['recordedAt']==now,'Receipt must equal trusted current time')
    times=[x['recordedAt'] for c in ['authorities','observations'] for x in ledger[c]]
    require(not times or now>max(times),'New receipt must follow register head')
    result=copy.deepcopy(ledger);result[collection].append(copy.deepcopy(record));validate_ledger(result,config)
    return result
def evaluate(ledger,config,*,actor,purpose,scope,predicate,subject,validAt,knownAt,now):
    """All-or-nothing full-register reader projection, no partial access filtering.
    Result is preference among supplied observations, never verified real-world truth.
    """
    root_check(config,now)
    if actor not in config['readers'] or purpose not in config['purposes']:raise Denied('Read denied')
    validate_ledger(ledger,config);stamp(validAt);stamp(knownAt)
    require(knownAt<=now,'Future knowledge query')
    match=policies(ledger,scope,predicate,validAt,knownAt)
    as_known={**{k:ledger[k] for k in ['format','version','dimension']},**{k:[x for x in ledger[k] if x['recordedAt']<=knownAt] for k in ['authorities','observations']}}
    obs=[x for x in current(ledger['observations'],knownAt) if x['state']=='asserted' and key(x)==(scope,predicate) and x['subject']==subject and active(x,validAt)]
    def pin(x):return {'id':x['id'],'revision':x['revision'],'sha256':digest(x)}
    base={'status':'unknown','value':None,'authorityIds':sorted(x['id'] for x in match),'observationIds':[],
          'evidence':[],'routeTo':[],'validAt':validAt,'knownAt':knownAt,
          'scope':scope,'predicate':predicate,'subject':subject,'reason':'missing-authority',
          'profileVersion':'0.1.0','inputDigest':digest(as_known),'configDigest':digest(config),
          'authorityPins':[{'id':x['id'],'revision':x['revision'],'sha256':digest(x)} for x in sorted(match,key=lambda x:x['id'])],
          'routeValidAt':validAt,'routeAction':'Informational only; resolve current routing before sending'}
    base.update(observationIds=sorted(x['id'] for x in obs),evidence=sorted({e for x in obs for e in x['evidence']}),observationPins=[pin(x) for x in sorted(obs,key=lambda x:x['id'])],unrankedObservationIds=sorted(x['id'] for x in obs),rulePins=[],routePins=[])
    if len(match)>1:base.update(status='authority-contested',reason='overlapping-authority-records');return base
    if not match:return base
    authority=match[0];base['accountable']=authority['accountable']
    def part_pin(x):return {'id':x['id'],'authorityId':authority['id'],'authorityRevision':authority['revision'],'authoritySha256':digest(authority)}
    base['routeTo']=sorted({s['party'] for s in authority['stewardships'] if active(s,validAt) and 'resolve-conflict' in s['duties']})
    base['routePins']=[part_pin(s) for s in sorted(authority['stewardships'],key=lambda x:x['id']) if active(s,validAt) and 'resolve-conflict' in s['duties']]
    rules=[r for r in authority['rules'] if active(r,validAt)];sources=[r['source'] for r in rules]
    base['rulePins']=[part_pin(r) for r in sorted(rules,key=lambda x:x['id'])]
    if len(sources)!=len(set(sources)):base.update(status='authority-contested',reason='overlapping-source-rules');return base
    ranking={r['source']:r['priority'] for r in rules}
    base['observationIds']=sorted(x['id'] for x in obs)
    base['evidence']=sorted({e for x in obs for e in x['evidence']})
    base['unrankedObservationIds']=sorted(x['id'] for x in obs if x['source'] not in ranking)
    ranked=[x for x in obs if x['source'] in ranking]
    if not ranked:base['reason']='no-ranked-observation';return base
    best=min(ranking[x['source']] for x in ranked);top=[x for x in ranked if ranking[x['source']]==best]
    values={encode(x['value']) for x in top}
    base['preferredObservationIds']=sorted(x['id'] for x in top);base['priority']=best
    if len(values)>1:base.update(status='contested',reason='equal-priority-disagreement');return base
    base.update(status='preferred',value=copy.deepcopy(top[0]['value']),reason='explicit-source-precedence')
    return base
def export_ledger(ledger,config):validate_ledger(ledger,config);return encode(ledger)
def import_snapshot(raw,config):
    """Trusted historical archive check, not an admission or security boundary."""
    try:
        def pairs(items):
            d={}
            for k,v in items:
                require(k not in d,'Duplicate JSON key');d[k]=v
            return d
        result=json.loads(raw,object_pairs_hook=pairs)
    except (ValueError,UnicodeError) as e:raise Invalid('Invalid archive') from e
    validate_ledger(result,config);return result
def migrate(ledger,target):
    require(target=='0.1.0','No lossless migration defined; retain original archive')
    return copy.deepcopy(ledger)
