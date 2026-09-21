"""Metadata-only reviewable reference. All callers/snapshots require a trusted host.

No network, payload access, grant evaluation, inference proof or deletion occurs.
Bounded reviewable reference; see review.md for the exact external audit scope.
"""
from pathlib import Path
import copy, datetime, hashlib, json, re
from jsonschema import Draft202012Validator

VERSION='0.1.0'
SCHEMA=json.loads(Path(__file__).with_name('disclosure.schema.json').read_text(encoding='utf-8'))
if not all(SCHEMA['$defs'][t]['properties']['version']['const']==VERSION for t in ('proposal','review','snapshot')):
    raise RuntimeError('schema/version mismatch')
VALIDATOR=Draft202012Validator(SCHEMA)
MAX_BYTES=262144
class Invalid(ValueError):pass
class Unauthorized(ValueError):pass

def canonical(value):
    """Restricted JSON: sorted keys, UTF-8, compact, no floats or normalization.

    List order is significant. Strings preserve code points. This is NOT JCS.
    Bounds are prototype limits, not a hardened hostile-input parser guarantee.
    """
    def visit(x,depth=0):
        if depth>20:raise Invalid('depth')
        if type(x) is str:
            if len(x)>4096 or any(0xD800<=ord(c)<=0xDFFF for c in x):raise Invalid('string')
        elif x is None or type(x) is bool:pass
        elif type(x) is int:
            if not -(2**53-1)<=x<=2**53-1:raise Invalid('integer')
        elif type(x) is list:
            if len(x)>128:raise Invalid('list')
            for a in x:visit(a,depth+1)
        elif type(x) is dict:
            if len(x)>128:raise Invalid('object')
            for k,v in x.items():
                if type(k) is not str:raise Invalid('key')
                visit(k,depth+1);visit(v,depth+1)
        else:raise Invalid('unsupported JSON value')
    visit(value)
    raw=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode('utf-8')
    if len(raw)>MAX_BYTES:raise Invalid('size')
    return raw

def load(raw):
    if not isinstance(raw,bytes) or len(raw)>MAX_BYTES:raise Invalid('input bytes')
    def pairs(items):
        d={}
        for k,v in items:
            if k in d:raise Invalid('duplicate JSON key')
            d[k]=v
        return d
    def forbidden(_):raise Invalid('non-integer number')
    def integer(s):
        if len(s)>17:raise Invalid('integer')
        return int(s)
    try:
        result=json.loads(raw.decode('utf-8'),object_pairs_hook=pairs,parse_float=forbidden,parse_constant=forbidden,parse_int=integer)
        canonical(result)
    except (UnicodeError,RecursionError,json.JSONDecodeError) as e:raise Invalid('JSON') from e
    return result

def native_fact_id(record):
    """Deterministic storage key for one immutable record revision."""
    validate(record)
    return 'urn:vercy:disclosure-revision:'+hashlib.sha256(canonical({'dimension':record['dimension'],'id':record['id'],'revision':record['revision']})).hexdigest()

def validate_native(fact,obj,*,dimension,capability,now,master,writer):
    """Companion semantic check AFTER separate V3 envelope validation.

    Host supplies authentic expected Dimension/master/writer and object registry.
    This is storage binding only, not active selection or disclosure permission.
    """
    authorize(capability,dimension)
    canonical(fact);canonical(obj)
    if not isinstance(fact,dict) or not isinstance(obj,dict):raise Invalid('native objects')
    for name in (master,writer):
        if type(name) is not str or not re.fullmatch(r'[A-Za-z][A-Za-z0-9+.-]*:[!-~]+',name):raise Invalid('native trusted identity')
    record=fact.get('value');validate(record)
    if record['dimension']!=dimension:raise Invalid('native Dimension')
    typ=record['type'];mid='vr.profile.enterprise-disclosure-review'
    if obj.get('recordType')!='object' or obj.get('schemaVersion')!='1.0.0' or obj.get('objectId')!=record['id'] or obj.get('objectType')!=mid+':'+typ or obj.get('state')!='active':raise Invalid('native object binding')
    if fact.get('recordType')!='fact' or fact.get('schemaVersion')!='1.0.0' or fact.get('subjectId')!=record['id'] or fact.get('path')!='disclosure.'+typ+'.revision':raise Invalid('native fact binding')
    if fact.get('factId')!=native_fact_id(record):raise Invalid('native revision identity')
    if fact.get('status')!='asserted' or 'unit' not in fact or fact['unit'] is not None or 'validTo' not in fact or fact['validTo'] is not None or fact.get('supersedes')!=[]:raise Invalid('native immutable storage semantics')
    if fact.get('accessClass')!='restricted' or obj.get('accessClass')!='restricted':raise Invalid('native access class')
    if fact.get('masterSystem')!=master or fact.get('authority')!={'source':writer,'rank':0} or type(fact['authority']['rank']) is not int:raise Invalid('native storage authority')
    if not isinstance(fact.get('provenance'),dict) or fact['provenance'].get('source')!=master or fact['provenance'].get('recordDigest')!=record['digest']:raise Invalid('native storage provenance')
    recorded=instant(fact.get('recordedAt'));object_at=instant(obj.get('recordedAt'));evaluation=instant(now)
    declared=instant(record['body']['capturedAt' if typ=='proposal' else 'reviewedAt'])
    if fact.get('validFrom')!=fact.get('recordedAt') or not object_at<=recorded<=evaluation or not declared<=recorded:raise Invalid('native storage time')
    return record

def hash_body(record):
    return 'sha256:'+hashlib.sha256(canonical({k:v for k,v in record.items() if k!='digest'})).hexdigest()

def instant(s):
    if not isinstance(s,str):raise Invalid('timestamp')
    try:
        m=re.fullmatch(r'([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})Z',s)
        if not m:raise ValueError()
        return datetime.datetime(*map(int,m.groups()),tzinfo=datetime.timezone.utc)
    except ValueError as e:raise Invalid('timestamp') from e

def pin(record):return {k:record[k] for k in ('id','revision','digest')}

def seal(record):
    if type(record) is not dict:raise Invalid('record object')
    canonical(record)
    result=copy.deepcopy(record);result['digest']=hash_body(result);validate(result);return result

def exact_identifiers(value,coherence=False):
    coherent={}
    def exact_strings(x):
        if isinstance(x,dict):
            if coherence and set(x)=={'id','revision','digest'}:
                previous=coherent.setdefault(x['id'],(x['revision'],x['digest']))
                if previous!=(x['revision'],x['digest']):raise Invalid('incoherent reference pin')
            for k,v in x.items():
                pattern=None
                if k in ('id','dimension','author','reviewer'):pattern=r'[A-Za-z][A-Za-z0-9+.-]*:[!-~]+'
                elif k in ('revision','key'):pattern=r'[A-Za-z0-9][A-Za-z0-9._-]*'
                elif k=='name':pattern=r'[A-Za-z_][A-Za-z0-9_]{0,63}'
                elif k=='digest':pattern=r'sha256:[0-9a-f]{64}'
                if pattern and (not isinstance(v,str) or not re.fullmatch(pattern,v)):raise Invalid('exact identifier syntax')
                exact_strings(v)
        elif isinstance(x,list):
            for v in x:exact_strings(v)
    exact_strings(value)

def validate(record):
    canonical(record)
    errors=list(VALIDATOR.iter_errors(record))
    if errors:raise Invalid('record shape')
    if record['digest']!=hash_body(record):raise Invalid('digest')
    exact_identifiers(record,coherence=True)
    b=record['body']
    if record['type']=='proposal':
        instant(b['capturedAt']);members=b['members']
        if len({m['key'] for m in members})!=len(members):raise Invalid('duplicate member key')
        for m in members:
            if len({f['name'] for f in m['fields']})!=len(m['fields']):raise Invalid('duplicate field')
    else:
        a,start,end=map(instant,[b['reviewedAt'],b['validFrom'],b['validTo']])
        if not a<=start<end:raise Invalid('review time interval')
        if b['supersedes'] and (b['supersedes']['id'],b['supersedes']['revision'])==(record['id'],record['revision']):raise Invalid('self supersession')
    return record

def authorize(capability,dimension):
    # These are trusted host assertions, never caller-submitted credentials.
    if not isinstance(dimension,str) or not re.fullmatch(r'[A-Za-z][A-Za-z0-9+.-]*:[!-~]+',dimension) or not isinstance(capability,dict) or capability.get('dimension')!=dimension or capability.get('inspect') is not True:
        raise Unauthorized('unavailable')

def validate_snapshot(snapshot,now):
    canonical(snapshot)
    v=Draft202012Validator({'$ref':'#/$defs/snapshot','$defs':SCHEMA['$defs']})
    if list(v.iter_errors(snapshot)):raise Invalid('snapshot shape')
    exact_identifiers(snapshot)
    for k in ('proposalAuthors','reviewers'):
        if any(not re.fullmatch(r'[A-Za-z][A-Za-z0-9+.-]*:[!-~]+',x) for x in snapshot[k]):raise Invalid('actor catalog syntax')
    if instant(snapshot['asOf'])!=instant(now):raise Invalid('snapshot time mismatch')
    active=snapshot['activeReviews'];withdrawn=snapshot['withdrawnReviews']
    if len({p['id'] for p in active})!=len(active):raise Invalid('multiple active revisions')
    a={(p['id'],p['revision']) for p in active};w={(p['id'],p['revision']) for p in withdrawn}
    if len(w)!=len(withdrawn):raise Invalid('conflicting withdrawn revision')
    if a & w:raise Invalid('active and withdrawn overlap')
    return {canonical(p) for p in active}

def inspect(proposal,reviews,snapshot,capability,now):
    """Return an INTERNAL applicability result for a complete trusted snapshot.

    The host attests current state, active-review completeness and authorities.
    It must resolve references independently; no remote artifacts are fetched.
    """
    dimension=snapshot.get('dimension') if isinstance(snapshot,dict) else None
    authorize(capability,dimension)
    active=validate_snapshot(snapshot,now)
    validate(proposal)
    if proposal['type']!='proposal' or proposal['dimension']!=dimension:raise Invalid('proposal scope')
    now=instant(now)
    if type(reviews) is not list or len(reviews)>64:raise Invalid('review set')
    counted=[];ignored=[];evaluated=False
    def result(status,reason=None):
        answer={'format':'vercy-disclosure-inspection','evaluatorVersion':VERSION,'status':status,'notServingAuthorization':True,'proposal':pin(proposal),'snapshotDigest':'sha256:'+hashlib.sha256(canonical(snapshot)).hexdigest(),'at':snapshot['asOf'],'reviewsEvaluated':evaluated,'counted':copy.deepcopy(counted),'ignored':copy.deepcopy(ignored),'withdrawn':copy.deepcopy(snapshot['withdrawnReviews'])}
        if reason:answer['reason']=reason
        return answer
    # Snapshot is a host catalog of current scalar metadata; exact equality avoids
    # undocumented classification order, schema adaptation, or shape widening.
    b=proposal['body'];context={k:b[k] for k in ('audience','purpose','environment','priorReleases','custodyContext')}
    if snapshot['proposal']!=pin(proposal):return result('stale','current-proposal-differs')
    if b['author'] not in snapshot['proposalAuthors']:return result('insufficient-context','proposal-author')
    if instant(b['capturedAt'])>now:return result('stale','future-capture')
    if context!=snapshot['context'] or b['members']!=snapshot['members']:return result('stale','current-inputs-differ')
    seen={};supplied=[]
    for r in reviews:
        validate(r)
        if r['type']!='review' or r['dimension']!=dimension:raise Invalid('review scope')
        if r['id']==proposal['id']:raise Invalid('identity changes type')
        if r['body']['proposal']!=pin(proposal):raise Invalid('review points to another proposal')
        if instant(r['body']['reviewedAt'])<instant(b['capturedAt']):raise Invalid('review predates proposal')
        key=(r['id'],r['revision'])
        if key in seen:raise Invalid('duplicate/conflicting review revision')
        if any(k[0]==r['id'] for k in seen):raise Invalid('multiple active revisions')
        seen[key]=r['digest'];supplied.append(pin(r))
    if {canonical(p) for p in supplied}!=active:return result('insufficient-context','review-set-incomplete')
    valid=[];evaluated=True
    for r in reviews:
        rb=r['body']
        if rb['supersedes'] and (rb['supersedes']['id'],rb['supersedes']['revision']) in seen:
            if rb['supersedes']['digest']!=seen[(rb['supersedes']['id'],rb['supersedes']['revision'])]:raise Invalid('incoherent supersession pin')
            raise Invalid('superseded review still active')
        reason=None
        if rb['reviewer'] not in snapshot['reviewers'] or rb['authority']!=snapshot['authority']:reason='authority'
        elif snapshot['separateReviewer'] and rb['reviewer']==b['author'] and rb['verdict']=='cleared':reason='self-clearance'
        elif instant(rb['reviewedAt'])>now:reason='future-assessment'
        elif now<instant(rb['validFrom']):reason='not-yet-valid'
        elif now>=instant(rb['validTo']):reason='expired'
        if reason:
            ignored.append({'pin':pin(r),'verdict':rb['verdict'],'reason':reason});continue
        counted.append(pin(r))
        valid.append(rb['verdict'])
    if not valid:return result('insufficient-context','no-applicable-review')
    if len(set(valid))>1:return result('conflict','active-review-disagreement')
    return result('applicable-review' if valid[0]=='cleared' else valid[0])

def import_records(existing,incoming,dimension,capability):
    """Pure transactional merge of immutable records, not persistent storage.

    Host must separately authorize writes, retain the full master set and apply
    compare-and-swap around persistence; this function has no database effects.
    """
    authorize(capability,dimension)
    if capability.get('record') is not True:raise Unauthorized('unavailable')
    if type(existing) is not list or type(incoming) is not list or len(existing)+len(incoming)>128:raise Invalid('record bounds')
    result=copy.deepcopy(existing);known={};types={}
    for n,r in enumerate(existing+incoming):
        validate(r)
        if r['dimension']!=dimension:raise Invalid('record scope')
        if r['id'] in types and types[r['id']]!=r['type']:raise Invalid('identity changes type')
        types[r['id']]=r['type']
        key=(r['type'],r['id'],r['revision'])
        if key in known:
            if known[key]!=r['digest']:raise Invalid('immutable revision conflict')
            if n<len(existing):raise Invalid('duplicate stored revision')
        else:
            known[key]=r['digest']
            if n>=len(existing):result.append(copy.deepcopy(r))
    # The supplied store is the complete local proposal/review master set. Domain
    # source and evidence references remain external; these two internal edges do not.
    records={(r['id'],r['revision']):r for r in result}
    edges={}
    def resolve(p,typ):
        target=records.get((p['id'],p['revision']))
        if target is None or target['type']!=typ or pin(target)!=p:raise Invalid('unresolved internal pin')
        return target
    for r in result:
        if r['type']!='review':continue
        rb=r['body'];proposal=resolve(rb['proposal'],'proposal')
        if instant(rb['reviewedAt'])<instant(proposal['body']['capturedAt']):raise Invalid('review predates proposal')
        if rb['supersedes']:
            prior=resolve(rb['supersedes'],'review')
            if prior['body']['proposal']['id']!=rb['proposal']['id']:raise Invalid('supersession crosses proposal identity')
            if instant(prior['body']['reviewedAt'])>instant(rb['reviewedAt']):raise Invalid('supersession time reversal')
            edges[(r['id'],r['revision'])]=(prior['id'],prior['revision'])
    for start in edges:
        visited=set();node=start
        while node in edges:
            if node in visited:raise Invalid('supersession cycle')
            visited.add(node);node=edges[node]
    return result
