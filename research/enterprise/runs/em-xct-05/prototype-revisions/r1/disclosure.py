"""Metadata-only research prototype. All callers/snapshots require a trusted host.

No network, payload access, grant evaluation, inference proof or deletion occurs.
This is not yet a published/installable Vercy model or an audited implementation.
"""
from pathlib import Path
import copy, datetime, hashlib, json
from jsonschema import Draft202012Validator

VERSION='0.0.0-prototype.1'
SCHEMA=json.loads(Path(__file__).with_name('disclosure.schema.json').read_text(encoding='utf-8'))
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
        if isinstance(x,str):
            if len(x)>4096 or any(0xD800<=ord(c)<=0xDFFF for c in x):raise Invalid('string')
        elif x is None or type(x) is bool:pass
        elif type(x) is int:
            if not -(2**53-1)<=x<=2**53-1:raise Invalid('integer')
        elif isinstance(x,list):
            if len(x)>128:raise Invalid('list')
            for a in x:visit(a,depth+1)
        elif isinstance(x,dict):
            if len(x)>128:raise Invalid('object')
            for k,v in x.items():
                if not isinstance(k,str):raise Invalid('key')
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
    try:
        result=json.loads(raw.decode('utf-8'),object_pairs_hook=pairs,parse_float=forbidden,parse_constant=forbidden)
        canonical(result)
    except (UnicodeError,RecursionError,json.JSONDecodeError) as e:raise Invalid('JSON') from e
    return result

def hash_body(record):
    return 'sha256:'+hashlib.sha256(canonical({k:v for k,v in record.items() if k!='digest'})).hexdigest()

def instant(s):
    if not isinstance(s,str):raise Invalid('timestamp')
    try:
        t=datetime.datetime.strptime(s,'%Y-%m-%dT%H:%M:%SZ')
        if t.strftime('%Y-%m-%dT%H:%M:%SZ')!=s:raise ValueError()
        return t.replace(tzinfo=datetime.timezone.utc)
    except ValueError as e:raise Invalid('timestamp') from e

def pin(record):return {k:record[k] for k in ('id','revision','digest')}

def seal(record):
    result=copy.deepcopy(record);result['digest']=hash_body(result);validate(result);return result

def validate(record):
    canonical(record)
    errors=list(VALIDATOR.iter_errors(record))
    if errors:raise Invalid('record shape')
    if record['digest']!=hash_body(record):raise Invalid('digest')
    b=record['body']
    if record['type']=='proposal':
        instant(b['capturedAt']);members=b['members']
        if len({m['key'] for m in members})!=len(members):raise Invalid('duplicate member key')
        for m in members:
            if len({f['name'] for f in m['fields']})!=len(m['fields']):raise Invalid('duplicate field')
            for f in m['fields']:
                keys=[(p['id'],p['revision']) for p in f['classificationBindings']]
                if len(set(keys))!=len(keys):raise Invalid('conflicting binding pin')
    else:
        a,start,end=map(instant,[b['reviewedAt'],b['validFrom'],b['validTo']])
        if not a<=start<end:raise Invalid('review time interval')
        if b['supersedes'] and b['supersedes']==pin(record):raise Invalid('self supersession')
    return record

def authorize(capability,dimension):
    # These are trusted host assertions, never caller-submitted credentials.
    if not isinstance(capability,dict) or capability.get('dimension')!=dimension or capability.get('inspect') is not True:
        raise Unauthorized('unavailable')

def inspect(proposal,reviews,snapshot,capability,now):
    """Return an INTERNAL applicability result for a complete trusted snapshot.

    The host attests current state, active-review completeness and authorities.
    It must resolve references independently; no remote artifacts are fetched.
    """
    dimension=snapshot.get('dimension') if isinstance(snapshot,dict) else None
    authorize(capability,dimension)
    validate(proposal)
    if proposal['type']!='proposal' or proposal['dimension']!=dimension:raise Invalid('proposal scope')
    now=instant(now)
    if not isinstance(reviews,list) or len(reviews)>64:raise Invalid('review set')
    if not isinstance(snapshot,dict):raise Invalid('snapshot')
    required={'dimension','context','members','proposalAuthors','reviewers','authority','activeReviews','withdrawnReviews','separateReviewer'}
    if set(snapshot)!=required or type(snapshot['separateReviewer']) is not bool:raise Invalid('snapshot shape')
    canonical(snapshot)
    for k in ('proposalAuthors','reviewers'):
        values=snapshot[k]
        if not isinstance(values,list) or len(values)>64 or any(not isinstance(v,str) or ':' not in v for v in values):raise Invalid('actor catalog')
        if len(values)!=len(set(values)):raise Invalid('duplicate actor')
    # Snapshot is a host catalog of current scalar metadata; exact equality avoids
    # undocumented classification order, schema adaptation, or shape widening.
    b=proposal['body'];context={k:b[k] for k in ('audience','purpose','environment','priorReleases','custodyContext')}
    if b['author'] not in snapshot['proposalAuthors']:return {'status':'insufficient-context','reason':'proposal-author'}
    if instant(b['capturedAt'])>now:return {'status':'stale','reason':'future-capture'}
    if context!=snapshot['context'] or b['members']!=snapshot['members']:return {'status':'stale','reason':'current-inputs-differ'}
    seen={};supplied=[]
    for r in reviews:
        validate(r)
        if r['type']!='review' or r['dimension']!=dimension:raise Invalid('review scope')
        key=(r['id'],r['revision'])
        if key in seen:raise Invalid('duplicate/conflicting review revision')
        seen[key]=r['digest'];supplied.append(pin(r))
    def pins(items):
        if not isinstance(items,list) or len(items)>64:raise Invalid('pin set')
        # Validate every pin without allowing extra keys, then compare exact sets.
        pv=Draft202012Validator({'$ref':'#/$defs/pin','$defs':SCHEMA['$defs']})
        if any(list(pv.iter_errors(x)) for x in items):raise Invalid('pin shape')
        keys=[canonical(x) for x in items]
        if len(keys)!=len(set(keys)):raise Invalid('duplicate pin')
        return set(keys)
    if pins(supplied)!=pins(snapshot['activeReviews']):return {'status':'insufficient-context','reason':'review-set-incomplete'}
    withdrawn=pins(snapshot['withdrawnReviews']);valid=[];ignored=[]
    for r in reviews:
        rb=r['body']
        if rb['proposal']!=pin(proposal):raise Invalid('review points to another proposal')
        if canonical(pin(r)) in withdrawn:ignored.append('withdrawn');continue
        if rb['reviewer'] not in snapshot['reviewers'] or rb['authority']!=snapshot['authority']:ignored.append('authority');continue
        if snapshot['separateReviewer'] and rb['reviewer']==b['author']:ignored.append('self-review');continue
        if instant(rb['reviewedAt'])<instant(b['capturedAt']):raise Invalid('review predates proposal')
        if not instant(rb['validFrom'])<=now<instant(rb['validTo']):ignored.append('outside-window');continue
        valid.append(rb['verdict'])
    if not valid:return {'status':'insufficient-context','reason':'no-applicable-review','ignored':ignored}
    if len(set(valid))>1:return {'status':'conflict','reason':'active-review-disagreement'}
    if valid[0]=='cleared':return {'status':'applicable-review','notServingAuthorization':True}
    return {'status':valid[0],'notServingAuthorization':True}

def import_records(existing,incoming,dimension,capability):
    """Pure transactional merge of immutable records, not persistent storage.

    Host must separately authorize writes, retain the full master set and apply
    compare-and-swap around persistence; this function has no database effects.
    """
    authorize(capability,dimension)
    if capability.get('record') is not True:raise Unauthorized('unavailable')
    if not isinstance(existing,list) or not isinstance(incoming,list) or len(existing)+len(incoming)>128:raise Invalid('record bounds')
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
    return result
