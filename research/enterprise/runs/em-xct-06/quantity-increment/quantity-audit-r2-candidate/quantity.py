"""Bounded embedded exact scalar values. No registry, I/O, rights or storage authority."""
from pathlib import Path
from fractions import Fraction
import hashlib,json,copy,re
from datetime import datetime
from jsonschema import Draft202012Validator

MID='vr.profile.enterprise-quantity-values'
SCHEMA_SHA='76f8f7e8947d42a381b3467c26d72f153b5643f14f92bb57d82757bd75e2913c'
MAX_BYTES=262144
class Rejected(ValueError):pass
def require(ok,reason):
    if not ok:raise Rejected(reason)
def bounds(v,depth=0):
    require(depth<=24,'depth')
    if type(v) is dict:
        require(len(v)<=32 and all(type(k) is str for k in v),'object-bounds')
        for k,x in v.items():bounds(k,depth+1);bounds(x,depth+1)
    elif type(v) is list:
        require(len(v)<=32,'array-bounds')
        for x in v:bounds(x,depth+1)
    elif type(v) is str:require(len(v)<=1024 and all(32<=ord(c)<=126 for c in v),'ascii-string')
    elif type(v) is int:require(abs(v)<=9999,'integer-bounds')
    else:require(v is None or type(v) is bool,'unsupported-number-or-type')
def canonical(v):
    bounds(v)
    raw=json.dumps(v,sort_keys=True,ensure_ascii=True,separators=(',',':'),allow_nan=False).encode('ascii')
    require(len(raw)<=MAX_BYTES,'bytes');return raw
def digest(v):return hashlib.sha256(canonical(v)).hexdigest()
def load(raw):
    require(type(raw) is bytes and len(raw)<=MAX_BYTES,'wire-bytes')
    def pairs(xs):
        d={}
        for k,v in xs:
            require(k not in d,'duplicate-key');d[k]=v
        return d
    def nofloat(s):raise Rejected('wire-float')
    def integer(s):
        require(len(s)<=5,'wire-integer');return int(s)
    try:v=json.loads(raw.decode('utf-8'),object_pairs_hook=pairs,parse_float=nofloat,parse_constant=nofloat,parse_int=integer)
    except (UnicodeError,RecursionError,json.JSONDecodeError) as e:raise Rejected('wire-json') from e
    canonical(v);return v
_raw=Path(__file__).with_name('quantity.schema.json').read_bytes()
require(hashlib.sha256(_raw).hexdigest()==SCHEMA_SHA,'schema-pin')
SCHEMA=json.loads(_raw);Draft202012Validator.check_schema(SCHEMA);V=Draft202012Validator(SCHEMA)
def rational(x):
    f=Fraction(int(x['n']),int(x['d']))
    require(str(f.numerator)==x['n'] and str(f.denominator)==x['d'],'noncanonical-rational');return f
def pack(f):return {'n':str(f.numerator),'d':str(f.denominator)}
def admission(sets):
    require(type(sets) is dict and set(sets)=={'definitions','sources','contexts'},'admission-shape')
    for s in sets.values():
        require(type(s) in (set,frozenset) and all(type(x) is str and re.fullmatch('[a-f0-9]{64}',x) for x in s),'admission-set')
def unit(u,sets):
    a,b=rational(u['a']),rational(u['b']);require(a>0,'positive-factor')
    require('scalar' not in u['roles'] or b==0,'scalar-offset')
    require(digest(u) in sets['definitions'],'definition-not-admitted')
    return a,b
def scalar(q,sets):
    a,b=unit(q['unit'],sets);require(q['role'] in q['unit']['roles'],'role-not-admitted')
    require(digest(q['context']) in sets['contexts'],'context-not-admitted')
    require(digest(q['source']) in sets['sources'],'source-not-admitted')
    m=q['magnitude']
    if m['state']!='known':return None
    lex=m['lexical'];fractional=len(lex.split('.')[1]) if '.' in lex else 0
    require(type(m['scale']) is int and m['scale']==fractional,'scale')
    require(sum(c.isdigit() for c in lex)<=36 and fractional<=18,'decimal-bounds')
    return Fraction(lex)
def compatible(source,target):
    require(source['kind']==target['kind'],'kind-mismatch')
    require(source['dimension']==target['dimension'],'dimension-mismatch')
    require(source['anchor']==target['anchor'],'anchor-mismatch')
def result(q,target,x):
    a,b=rational(q['unit']['a']),rational(q['unit']['b']);c,d=rational(target['a']),rational(target['b'])
    return pack((a*x+(b-d if q['role']=='point' else 0))/c)
def validate(document,*,admitted):
    canonical(document);admission(admitted)
    require(not list(V.iter_errors(document)),'schema')
    # JSON Schema allows 1.0 as integer; bounds rejects all floats before schema.
    q=document['quantity'];x=scalar(q,admitted)
    if document['format']=='vercy-embedded-conversion':
        require(x is not None,'non-numeric');t=document['target'];unit(t,admitted)
        compatible(q['unit'],t);require(q['role'] in t['roles'],'target-role')
        rational(document['result']);require(document['result']==result(q,t,x),'replay-mismatch')
    return copy.deepcopy(document)
def convert(quantity,target,*,admitted):
    original=validate({'format':'vercy-embedded-quantity','version':'0.1.0','quantity':quantity},admitted=admitted)['quantity']
    # Validate target shape before accessing arithmetic members.
    candidate={'format':'vercy-embedded-conversion','version':'0.1.0','quantity':original,'target':copy.deepcopy(target),'result':{'n':'0','d':'1'}}
    canonical(candidate);require(not list(V.iter_errors(candidate)),'schema')
    unit(target,admitted);compatible(original['unit'],target);require(original['role'] in target['roles'],'target-role')
    x=scalar(original,admitted);require(x is not None,'non-numeric');candidate['result']=result(original,target,x)
    return validate(candidate,admitted=admitted)
def compare(left,right,*,admitted):
    l=validate({'format':'vercy-embedded-quantity','version':'0.1.0','quantity':left},admitted=admitted)['quantity']
    r=validate({'format':'vercy-embedded-quantity','version':'0.1.0','quantity':right},admitted=admitted)['quantity']
    require(l['context']==r['context'],'context-mismatch');require(l['role']==r['role'],'role-mismatch')
    c=convert(l,r['unit'],admitted=admitted);a=rational(c['result']);b=scalar(r,admitted);require(b is not None,'non-numeric')
    return (a>b)-(a<b)
def stamp(s):
    require(type(s) is str and re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z',s),'native-time')
    try:return datetime.strptime(s,'%Y-%m-%dT%H:%M:%SZ')
    except ValueError as e:raise Rejected('native-time') from e
def validate_native(fact,host_object,*,subject,master,writer,access,admitted):
    """After V3 outer validation and host access check, verify one stored fact binding.
    No current-head selection, credential verification or Dimension inference.
    """
    canonical(fact)
    require(type(fact) is dict and type(host_object) is dict,'native-shape')
    # The host object's unrelated properties belong to its own outer V3 schema.
    canonical({k:host_object.get(k) for k in ('recordType','schemaVersion','objectId','accessClass')})
    require(type(master) is str and bool(master.strip()) and type(writer) is str and bool(writer.strip()),'native-context')
    require(type(fact.get('factId')) is str and bool(fact['factId']),'native-id')
    require(fact.get('recordType')=='fact' and host_object.get('recordType')=='object' and fact.get('schemaVersion')==host_object.get('schemaVersion')=='1.0.0','native-version')
    require(type(subject) is str and bool(subject) and fact.get('subjectId')==host_object.get('objectId')==subject,'native-subject')
    require(type(fact.get('authority')) is dict and type(fact['authority'].get('rank')) is int and fact.get('masterSystem')==master and fact.get('authority')=={'source':writer,'rank':0},'native-master')
    require(access in ('public','internal','restricted','confidential') and fact.get('accessClass')==host_object.get('accessClass')==access,'native-access')
    require(fact.get('status')=='asserted' and fact.get('unit') is None and fact.get('validTo') is None,'native-state')
    v=validate(fact.get('value'),admitted=admitted)
    require(fact.get('path')==('quantity.value' if v['format']=='vercy-embedded-quantity' else 'quantity.conversion'),'native-path')
    # Outer provenance is capture evidence; source pin inside quantity is semantic evidence.
    require(type(fact.get('provenance')) is dict and fact['provenance'].get('source')==master,'native-provenance')
    stamp(fact.get('recordedAt'));stamp(fact.get('validFrom'))
    return v
def validate_correction(previous,current,host_object,*,subject,master,writer,access,admitted):
    validate_native(previous,host_object,subject=subject,master=master,writer=writer,access=access,admitted=admitted)
    validate_native(current,host_object,subject=subject,master=master,writer=writer,access=access,admitted=admitted)
    require(type(previous.get('factId')) is str and bool(previous['factId']) and type(current.get('factId')) is str and bool(current['factId']) and current['factId']!=previous['factId'] and current.get('supersedes')==[previous['factId']],'correction-link')
    require(type(previous.get('supersedes')) is list and current['factId'] not in previous['supersedes'],'correction-cycle')
    require(current['path']==previous['path'],'correction-path')
    require(stamp(current['recordedAt'])>=stamp(previous['recordedAt']),'correction-time')
    require(type(current['provenance'].get('correctionReason')) is str and bool(current['provenance']['correctionReason'].strip()),'correction-reason')
    return current['value']
