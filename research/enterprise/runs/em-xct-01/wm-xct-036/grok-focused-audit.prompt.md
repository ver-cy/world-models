# Frozen semantic and implementation audit: enterprise identity profile

Respond in English. No tools, browsing, delegation, file writes or publication. Review only supplied frozen contents. Return BLOCK / ACCEPT WITH LIMITS, specific defects and executable counterexamples. Review is not approval authority. State exact scope and anything not seen.

This is a narrow profile of existing WM-XCT-036, with WM-XCT-011 carriage, not a new world-model. 48 tests and three native new-Dimension scenarios passed locally; audit these claims critically, do not pretend you ran them. Existing source holds and historical Claude-only 036 review remain. Your earlier study saw source excerpts partially; selected exact local/public-byte-verified definitions are included below to close the specific relation/assignment mapping questions, not all legacy holds.

Design reconciliation: retain parent relation codes equivalent-in-context/not-same-assertion/probable-entity-match with candidate never asserted; do not adopt Grok's new source-scoped-denotation code. A single assertion owns no resolution status; a pure query gives accepted-in-input, not globally accepted. All authority conflicts stay contested, no ranking. Policy is frozen, digest-pinned and caller-trusted; policy rotation fails closed. Authentication, evidence truth, read/write enforcement, global completeness and retention remain external. A user-account or service-account cannot become Person even by override. Startup fixtures explicitly use synthetic person-reference exports, not Git/tracker account IDs. This narrower scope means EM-XCT-01 remains partial.

Inspect especially bitemporal events, contested/negative/candidate cases, assignment reuse and collision, schema bypass, idempotency, input mutation, source evidence, policy/namespace gates, and nested V3 versus companion validation. Flag a bug versus an explicitly out-of-scope capability distinctly. Publication plan: additive versioned profile associated with the existing model; never claim your bounded review verifies all 108 historical sources or the whole parent.

This focused Grok pass includes the complete reference evaluator below, but not full schemas, tests or native harness. Schema summary: closed assertion and nested objects; URI-qualified IDs; UTC-second dates; fixed version; relation enum above; policy actors are an array of actor plus allowed state list; issuer/reader lists unique; required fixed claim fields and event history. Companion uses the provided JSON Schema through Draft202012Validator. Do not claim the unseen artifacts are reviewed.

"""Bounded, offline enterprise assertion profile. No endpoint writes or matching.

Policy, clock and input completeness are caller trust inputs. This reference
checks declared constraints; it does not authenticate users or evidence.
"""
import argparse,copy,datetime,hashlib,json,re
from pathlib import Path
from jsonschema import Draft202012Validator,FormatChecker

HERE=Path(__file__).resolve().parent
class Invalid(ValueError):pass
def require(condition,message):
    if not condition:raise Invalid(message)
def encode(value):return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode('utf-8')
def digest(value):return 'sha256:'+hashlib.sha256(encode(value)).hexdigest()
def load(path):
    def unique(pairs):
        value={}
        for key,item in pairs:
            require(key not in value,'duplicate JSON member: '+key);value[key]=item
        return value
    return json.loads(Path(path).read_text(encoding='utf-8'),object_pairs_hook=unique,parse_constant=lambda x:(_ for _ in ()).throw(Invalid('nonfinite JSON number')))
def stamp(value):
    require(isinstance(value,str) and re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z',value) is not None,'UTC second precision timestamp required')
    try:return datetime.datetime.strptime(value,'%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=datetime.timezone.utc)
    except (ValueError,TypeError) as e:raise Invalid('UTC second precision timestamp required') from e
def schema(value,name):
    document=load(HERE/'identity-profile.schema.json')
    contract=document if name=='assertion.schema.json' else document['$defs'][name.split('.')[0]]
    errors=sorted(Draft202012Validator(contract,format_checker=FormatChecker()).iter_errors(value),key=lambda e:str(e.path))
    require(not errors,'SCHEMA: '+('; '.join(e.message for e in errors[:3])))
def interval(start,end):require(end is None or stamp(start)<stamp(end),'empty or reversed interval')
def inside(time,start,end):return stamp(start)<=stamp(time) and (end is None or stamp(time)<stamp(end))
def key(binding):return tuple(binding[k] for k in ['scheme','schemeVersion','issuer','scope','value'])
def validate(assertion,policy):
    schema(policy,'policy.schema.json');schema(assertion,'assertion.schema.json')
    interval(policy['validFrom'],policy['validTo'])
    actors={item['actor']:item['states'] for item in policy['actors']}
    require(len(actors)==len(policy['actors']),'duplicate policy actor')
    require(assertion['policyDigest']==digest(policy),'policy bytes do not match pinned digest')
    require(assertion['dimension']==policy['dimension'] and assertion['purpose']==policy['purpose'],'wrong Dimension or purpose')
    b=assertion['binding'];target=assertion['target']
    require(b['issuer'] in policy['issuers'],'untrusted identifier issuer')
    require(b['kind']==target['kind'],'different referent kinds: account ownership is not identity')
    require(target['id'].startswith(policy['subjectPrefix']),'subject outside local namespace')
    require(assertion['relation'] in policy['relations'],'relation outside supplied policy')
    interval(b['validFrom'],b['validTo']);interval(assertion['validFrom'],assertion['validTo'])
    require(inside(assertion['validFrom'],b['validFrom'],b['validTo']),'assertion starts outside assignment')
    if b['validTo'] is not None:require(assertion['validTo'] is not None and stamp(assertion['validTo'])<=stamp(b['validTo']),'assertion exceeds assignment')
    require(stamp(b['recordedAt'])>=stamp(b['validFrom']),'binding observed before assignment began')
    previous=None;ids=set()
    transitions={None:{'proposed'},'proposed':{'asserted','disputed','retracted'},'asserted':{'disputed','retracted'},'disputed':{'asserted','retracted'},'retracted':set()}
    for event in assertion['history']:
        require(event['id'] not in ids,'duplicate event identity');ids.add(event['id'])
        require(event['previousDigest']==(digest(previous) if previous else None),'event predecessor mismatch')
        require(event['state'] in transitions[previous['state'] if previous else None],'invalid lifecycle transition')
        require(previous is None or stamp(event['recordedAt'])>stamp(previous['recordedAt']),'recorded time must strictly increase')
        require(stamp(event['recordedAt'])>=stamp(b['recordedAt']),'claim predates binding evidence')
        require(stamp(assertion['validFrom'])<=stamp(event['effectiveAt'])<=stamp(event['recordedAt']),'event time outside admissible past')
        require(inside(event['recordedAt'],policy['validFrom'],policy['validTo']),'authority inactive when event recorded')
        require(event['actor'] in actors and event['state'] in actors[event['actor']],'actor cannot issue this state')
        kinds={x['kind'] for x in event['evidence']}
        if event['state']=='asserted':
            require(assertion['relation']!='probable-entity-match','candidate relation cannot activate')
            require({'source-record','review-decision'}<=kinds,'activation requires source evidence and review evidence')
            require(any(x['kind']=='source-record' and x['ref']==b['sourceRecord'] for x in event['evidence']),'source evidence does not match binding source record')
        previous=event
    return assertion
def validate_set(assertions,policy):
    require(isinstance(assertions,list),'assertions must be a list')
    ids={};bindings={};event_ids=set()
    for a in assertions:
        validate(a,policy)
        require(a['id'] not in ids,'duplicate assertion ID in input; use import_assertion for replay')
        ids[a['id']]=a
        bid=a['binding']['assignmentId'];content=digest(a['binding'])
        require(bid not in bindings or bindings[bid]==content,'assignment ID reused for different binding content')
        bindings[bid]=content
        for event in a['history']:
            require(event['id'] not in event_ids,'event ID reused across assertions');event_ids.add(event['id'])
    return assertions
def import_assertion(existing,incoming,policy):
    """Pure import, with no filesystem writes. Caller commits under its own lock."""
    validate_set(existing,policy);validate(incoming,policy)
    for old in existing:
        if old['id']!=incoming['id']:continue
        if old==incoming:return copy.deepcopy(existing)
        old_base={k:v for k,v in old.items() if k!='history'};new_base={k:v for k,v in incoming.items() if k!='history'}
        require(old_base==new_base,'claim-bearing content changed; retract and use a new assertion ID')
        require(len(incoming['history'])>len(old['history']) and incoming['history'][:len(old['history'])]==old['history'],'history is not an append-only extension')
        result=[copy.deepcopy(incoming if x['id']==old['id'] else x) for x in existing]
        validate_set(result,policy);return result
    result=copy.deepcopy(existing+[incoming]);validate_set(result,policy);return result
def resolve(assertions,query_binding,policy,*,valid_at,known_at,evaluation_at,reader,purpose):
    """A view of the supplied complete-for-caller input only, never global truth."""
    validate_set(assertions,policy);schema(query_binding,'query.schema.json')
    require(reader in policy['readers'] and purpose==policy['purpose'],'read purpose/actor denied by supplied policy')
    require(inside(evaluation_at,policy['validFrom'],policy['validTo']),'current policy is inactive')
    require(stamp(known_at)<=stamp(evaluation_at),'knowledge time exceeds evaluation time')
    stamp(valid_at)
    positives={};negative={};candidates=[];disputed=[];excluded=[]
    for a in assertions:
        if key(a['binding'])!=key(query_binding):continue
        history=[e for e in a['history'] if stamp(e['recordedAt'])<=stamp(known_at) and stamp(e['effectiveAt'])<=stamp(valid_at)]
        if not history:continue
        e=history[-1]
        if not inside(valid_at,a['validFrom'],a['validTo']) or not inside(valid_at,a['binding']['validFrom'],a['binding']['validTo']):excluded.append({'id':a['id'],'reason':'outside-validity'});continue
        if e['state']=='retracted':excluded.append({'id':a['id'],'reason':'retracted'});continue
        if e['state']=='disputed':disputed.append(a['id']);continue
        if e['state']=='proposed':candidates.append(a['id']);continue
        target=a['target']['id']
        bucket=negative if a['relation']=='not-same-assertion' else positives
        bucket.setdefault(target,[]).append(a['id'])
    contested=bool(disputed or len(positives)>1 or set(positives)&set(negative))
    status='contested' if contested else 'accepted-in-input' if positives else 'candidate' if candidates else 'unknown'
    return {'status':status,'targets':sorted(positives),'supporting':sorted(x for v in positives.values() for x in v),'opposing':sorted(x for v in negative.values() for x in v),'disputed':sorted(disputed),'candidates':sorted(candidates),'excluded':sorted(excluded,key=lambda x:x['id']),'validAt':valid_at,'knownAt':known_at,'inputDigest':digest(sorted(assertions,key=lambda x:x['id'])),'policyDigest':digest(policy),'scope':'supplied-input-only','grantsAccess':False,'globalEquality':False}
def main():
    p=argparse.ArgumentParser();p.add_argument('assertions');p.add_argument('--policy',required=True);a=p.parse_args()
    values=load(a.assertions);validate_set(values,load(a.policy));print(json.dumps({'valid':True,'assertions':len(values),'scope':'declared constraints only; caller authenticates policy and evidence'}))
if __name__=='__main__':main()


Parent definitions verified: identifier-assignment-record owns assigner, evidence, valid and recorded time; als-tax-kind-register defines equivalent-in-context as equivalence void outside declared context, probable-entity-match as non-asserted hypothesis, not-same-assertion as explicit denial. No new source-scoped-denotation predicate is needed.
