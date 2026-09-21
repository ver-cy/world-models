"""Bounded monetary calculation receipts. No network, ledger or authorization engine."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime
import copy,hashlib,json,re
from jsonschema import Draft202012Validator

VERSION='0.1.0'
MID='vr.profile.enterprise-monetary-calculation'
PATH='monetary.calculation.receipt'
MAX_BYTES=2_097_152
SCHEMA=json.loads(Path(__file__).with_name('monetary.schema.json').read_text(encoding='utf-8'))
Draft202012Validator.check_schema(SCHEMA)
VALIDATOR=Draft202012Validator(SCHEMA)

class Rejected(ValueError):pass
def require(ok,code):
    if not ok:raise Rejected(code)
def canonical(x):
    try:return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode('utf-8')
    except (ValueError,TypeError,UnicodeError,RecursionError) as e:raise Rejected('invalid-json') from e
def digest(x):return 'sha256:'+hashlib.sha256(canonical(x)).hexdigest()
def load(raw):
    require(type(raw) in (bytes,str),'wire-type')
    require(len(raw if type(raw) is bytes else raw.encode('utf-8'))<=MAX_BYTES,'wire-size')
    def pairs(items):
        out={}
        for k,v in items:
            require(k not in out,'duplicate-json-key');out[k]=v
        return out
    def nonfinite(_):raise Rejected('nonfinite-json')
    try:return json.loads(raw,object_pairs_hook=pairs,parse_constant=nonfinite)
    except (ValueError,UnicodeError,RecursionError) as e:raise Rejected('invalid-wire-json') from e
def bounded(x,depth=0):
    require(depth<=16,'depth-bound')
    if type(x) is dict:
        require(len(x)<=32 and all(type(k) is str for k in x),'object-bound')
        for v in x.values():bounded(v,depth+1)
    elif type(x) is list:
        require(len(x)<=256,'list-bound')
        for v in x:bounded(v,depth+1)
    elif type(x) is str:require(len(x)<=512,'string-bound')
    elif x is None or type(x) is bool:pass
    elif type(x) is int:require(abs(x)<=9999,'integer-bound')
    else:raise Rejected('unsupported-json-type')
def shape(x,definition):
    bounded(x);require(len(canonical(x))<=MAX_BYTES,'record-size')
    schema={'$ref':'#/$defs/'+definition,'$defs':SCHEMA['$defs']}
    errors=list(Draft202012Validator(schema).iter_errors(x))
    require(not errors,'schema:'+definition)
def stamp(s):
    try:return datetime.strptime(s,'%Y-%m-%dT%H:%M:%SZ')
    except (ValueError,TypeError) as e:raise Rejected('invalid-instant') from e
def amount(s):
    require(type(s) is str and re.fullmatch(r'-?(?:0|[1-9][0-9]{0,35})(?:\.[0-9]{1,18})?',s) is not None,'decimal-grammar')
    require(len(s.replace('-','').replace('.',''))<=36,'decimal-digits')
    value=Fraction(s);require(not(s.startswith('-') and value==0),'negative-zero')
    return value
def scale(s):return len(s.split('.')[1]) if '.' in s else 0
def rational(v):return {'numerator':str(v.numerator),'denominator':str(v.denominator)}
def fixed(v,places):
    c=v*10**places;require(c.denominator==1,'nonfinite-result')
    n=c.numerator;digits=str(abs(n)).zfill(places+1)
    return ('-' if n<0 else '')+(digits[:-places]+'.'+digits[-places:] if places else digits)
def round_units(v,mode):
    sign=-1 if v<0 else 1;n=abs(v.numerator);d=v.denominator;q,r=divmod(n,d)
    if mode=='floor':return v.numerator//d
    if mode=='ceiling':return -((-v.numerator)//d)
    if mode=='toward-zero':return sign*q
    if mode=='half-away-from-zero':return sign*(q+(2*r>=d))
    if mode=='half-even':return sign*(q+(2*r>d or (2*r==d and q%2==1)))
    raise Rejected('rounding-mode')
def compute(request):
    shape(request,'Request')
    require(SCHEMA['$defs']['Request']['properties']['schemaVersion']['const']==VERSION,'code-schema-version')
    stamp(request['computedAt']);currency=request['inputs'][0]['currency'];context=request['inputs'][0]['context'];stamp(context['valuationAt'])
    require((request['supersedes'] is None and request['correctionReason'] is None) or (request['supersedes'] is not None and type(request['correctionReason']) is str and bool(request['correctionReason'].strip())),'correction-reason')
    require(request['policy']['currency']==currency,'policy-currency')
    require(len({x['key'] for x in request['inputs']})==len(request['inputs']),'duplicate-input-key')
    seen={};values=[]
    for x in request['inputs']:
        require(x['currency']==currency,'mixed-currency-or-edition')
        require(x['context']==context,'incompatible-valuation-context')
        require(x['source']['id'] not in seen,'duplicate-source-slot')
        seen[x['source']['id']]=x['source'];values.append(amount(x['amount']))
        require(scale(x['amount'])==x['declaredScale'],'declared-scale-mismatch')
    quantum=amount(request['policy']['increment']);require(quantum>0,'nonpositive-increment')
    places=scale(request['policy']['increment']);mode=request['policy']['mode'];stage=request['policy']['stage']
    exact=sum(values,Fraction(0));steps=[]
    if stage=='per-item':
        results=[]
        for x,v in zip(request['inputs'],values):
            r=round_units(v/quantum,mode)*quantum;results.append(r)
            steps.append({'inputKey':x['key'],'exact':rational(v),'rounded':fixed(r,places),'residual':rational(v-r)})
        result=sum(results,Fraction(0))
    else:
        result=round_units(exact/quantum,mode)*quantum
        steps.append({'inputKey':'@total','exact':rational(exact),'rounded':fixed(result,places),'residual':rational(exact-result)})
    output=fixed(result,places)
    require(len(output.replace('-','').replace('.',''))<=42,'output-capacity')
    return {'currency':copy.deepcopy(currency),'context':copy.deepcopy(context),'exactTotal':rational(exact),'roundedTotal':output,'declaredScale':places,'residual':rational(exact-result),'inexact':any(s['residual']['numerator']!='0' for s in steps),'steps':steps,'authority':'calculation-only'}
def issue(request):
    out={'format':'vercy-monetary-calculation-receipt','schemaVersion':VERSION,'request':copy.deepcopy(request),'result':compute(request)}
    out['digest']=digest(out);validate(out);return out
def validate(receipt):
    shape(receipt,'Receipt');copy_r=copy.deepcopy(receipt);claimed=copy_r.pop('digest')
    require(digest(copy_r)==claimed,'receipt-digest')
    require(receipt['result']==compute(receipt['request']),'replay-mismatch')
    require(receipt['request']['id']!=(receipt['request']['supersedes'] or {}).get('id'),'self-supersession')
    return copy.deepcopy(receipt)
def pin(receipt):
    return {'id':receipt['request']['id'],'digest':receipt['digest']}
def import_receipts(existing,incoming,*,dimension,allowed_issuers):
    require(type(existing) is list and type(incoming) is list,'register-type')
    require(type(allowed_issuers) is set and all(type(x) is str for x in allowed_issuers),'host-issuer-set')
    require(len(existing)+len(incoming)<=256,'register-bound')
    merged={}
    for raw in existing+incoming:
        r=validate(raw);q=r['request'];require(q['dimension']==dimension,'wrong-dimension')
        require(q['issuer'] in allowed_issuers,'issuer-not-admitted')
        if q['id'] in merged:require(merged[q['id']]==r,'immutable-identity-conflict')
        else:merged[q['id']]=r
    for r in merged.values():
        q=r['request'];p=q['supersedes']
        if p:
            require(p['id'] in merged and merged[p['id']]['digest']==p['digest'],'supersedes-unresolved')
            old=merged[p['id']]['request']
            require(q['subject']==old['subject'] and q['issuer']==old['issuer'],'supersedes-scope')
            require(stamp(q['computedAt'])>=stamp(old['computedAt']),'supersedes-time')
        visited=set();cursor=r
        while cursor['request']['supersedes']:
            cid=cursor['request']['id'];require(cid not in visited,'supersession-cycle');visited.add(cid)
            cursor=merged[cursor['request']['supersedes']['id']]
    return list(merged.values())
def native_fact_id(r):return 'urn:vercy:monetary-fact:'+hashlib.sha256(canonical({'dimension':r['request']['dimension'],'id':r['request']['id'],'digest':r['digest']})).hexdigest()
def validate_native(fact,obj,*,dimension,master,writer,allowed_issuers):
    # Outer envelopes must also pass the pinned V3 validator. This adds semantic checks.
    require(type(fact) is dict and type(obj) is dict,'native-type')
    for envelope in (fact,obj):
        bounded(envelope);require(len(canonical(envelope))<=MAX_BYTES,'native-envelope-size')
    require(fact.get('recordType')=='fact' and obj.get('recordType')=='object','native-record-type')
    r=validate(fact.get('value'));q=r['request']
    require(q['dimension']==dimension and q['issuer'] in allowed_issuers,'native-host-scope')
    require(obj.get('objectId')==q['id'] and obj.get('objectType')==MID+':MonetaryCalculationReceipt','native-object')
    require(obj.get('state')=='active' and obj.get('accessClass')=='restricted','native-object-state')
    require(fact.get('subjectId')==q['id'] and fact.get('path')==PATH and fact.get('factId')==native_fact_id(r),'native-binding')
    require(fact.get('status')=='asserted' and fact.get('unit') is None and fact.get('validTo') is None and fact.get('supersedes')==[],'native-shape')
    require(fact.get('masterSystem')==master and fact.get('authority')=={'source':writer,'rank':0},'native-master')
    require(fact.get('accessClass')=='restricted' and fact.get('provenance',{}).get('recordDigest')==r['digest'],'native-disclosure-digest')
    require(fact.get('validFrom')==fact.get('recordedAt'),'native-storage-time')
    require(stamp(fact.get('recordedAt'))>=stamp(q['computedAt']),'native-recorded-before-computed')
    return r
