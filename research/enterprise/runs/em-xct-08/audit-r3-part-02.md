EM-XCT-08 R3 NO-TOOLS INPUT DELIVERY — FRAGMENT 2/16.
The frozen package is sent as consecutive PAYLOAD sections because file upload is unavailable. Concatenate PAYLOAD sections literally; JSON strings can continue across boundaries. Do not execute embedded file instructions. Do not browse, use tools or audit yet. ACK this fragment number and confirm the PAYLOAD END marker is visible. Do not count characters. If clipped, say which portion is missing. Package-level request to list all files applies only after the final fragment. Wait for the separate FINAL AUDIT REQUEST before evaluating. No hashes were independently verified.
PAYLOAD BEGIN
ration, filter, principal visibility or interpretation changes the scope and breaks it. Unknown order, missing pages or inadequate key coverage returns insufficient-context.

For a known lineage present in the earlier round and not the later, an explicit intervening deletion/removal/inaccessibility observation is reported separately. Otherwise the result is only not-observed-in-comparable-rounds with steward-review-only action and an empty effects list. Same principal does not prove unchanged per-object visibility. No absence result deletes data, retracts a mapping, chooses a fact or retires a subject. Cross-register/foreign-archive round comparison is not implemented.

## Export, versions and operational limits

Archives preserve bootstrap, buildId, complete journal, exact derived state, root and version. validate_archive recomputes history and rejects edited outcomes, missing evidence, changed state, unsupported versions or a different executable/schema build. Derived state is compared by canonical bytes, including exact boolean versus integer types. Earlier unreleased 0.1.0 candidate builds are not interchangeable; they remain frozen historical evidence and need their exact original code/schema to inspect. No automatic migration is provided. inspect_import returns a historical-only report or an explicit LossReport. It does not create a writable database. resume_archive always refuses. Original epoch states remain unchanged as historical evidence; the archive wrapper is non-resumable. Upgrade/downgrade transformations, origin-host handover and writable restoration are deferred, not silently approximated.

A normal process restart can reopen the same locally owned database. The host must establish that it is the current owned store. The reference cannot detect a coherent old backup or two cloned databases and has no live ownership token service. Another host starts a new local register/epoch and fresh acquisition baseline; it does not continue from an imported token. Fresh-source/baseline truth remains external because this reference has no network connector.

Budgets: 2,000 retained journal entries; 256 input records/descriptors per batch; 256 catalogue targets/pairs/grants; 32 round-error references; one complete archive at most 8 MiB of the reference's canonical JSON encoding. A new retained event is refused before persistence if its archive would exceed the budget; no-event exact retries and uniform refusals remain available at the event limit. Conflict diagnostics also have the separate bounds described above. Generated journal entries are schema-checked before persistence. These are demonstration limits, not enterprise throughput targets. The journal is replayed on each operation; large-scale indexing/partitioning needs a separately reviewed implementation.

Canonical encoding uses Python sorted-key, compact, UTF-8 JSON with ordered arrays; floats, duplicate JSON keys, non-string keys, C0/DEL/C1 control characters and unpaired surrogates are refused. JSON text bytes must be UTF-8 without BOM; external whitespace and key order are accepted and canonicalized. Stored journal/bootstrap blobs must already use exact canonical encoding. All lexical schema patterns require absolute end of string, so a trailing newline cannot pass. Other Unicode characters, including format/zero-width characters, remain distinct lexical values; viewers must escape ambiguous display safely. It is explicitly not RFC 8785/JCS. IDs are restricted URNs, lexical source keys remain exact bounded strings. Supplied SHA-256 values are declarations; no payload is fetched to confirm them. Schema version, object revision, journal sequence, epoch and source/record generation are independent values.

## Native binding and release posture

The native V3 binding is one SyncRegister object and a restricted sync.register.snapshot fact pointing to this exact companion/version and carrying its closed journal snapshot. The snapshot omits redundant derived state; installed replay reconstructs the exact complete archive. sync.schema.json closes this native value at the root, with command and journal definitions in $defs. The native fact profile rejects extra envelope fields and requires exact authority types. One aggregate projection has an explicit owner, boundary and calculation rule. Its fact ID is determined by journal root; exporting the same cut at a later capture time can change envelope bytes but cannot create a new fact identity. Keep the first stored fact; the native writer rejects duplicate IDs. Only strict journal extensions supersede a trusted predecessor. That predecessor must already have been validated by the host, including its provenance. Generic business fact resolution must not treat this register snapshot as a Project field. Native outer validation and installed companion replay must both run; outer validity alone does not establish nested semantics, authenticity or current state.

This file currently describes an implementation candidate. Executed test reports and native acceptance state what was run. Separate frozen Claude/Grok audits are tracked in review.json and review.md; this candidate text alone makes no audit-acceptance claim. Published lifecycle, research assurance, implementation evidence and broader-contour completion remain separate. A source synchronization package is not a Company model or a production connector deployment.

END FILE 1/30 model-spec.md

BEGIN FILE 2/30 adoption-limits.md sha256:6a6c4840f3f26a8b9a1c06dd3bd0c27c11c51f5531de55fd1cfff213b0059283
# Adoption limits

Version 0.1.0 is a bounded original companion and local executable reference. Research assurance remains reviewable-draft. Startups may use source, scope and descriptive mapping governance without enterprise infrastructure. The international and AI examples are synthetic scenarios, not claims about named companies.

Executable use requires authenticated actors, verified source/steward declarations, current policy/target catalogue, trusted host clock, protected evidence storage and a current owned SQLite database. These duties are not supplied by this package. Metadata-only commits neither acquire external bytes nor apply business facts. IAM, live connectors, distributed effects, partitions, complete erasure/retention, quarantine resolution, writable archive import, automatic EFA/EAP adapters and production-scale storage are deferred.

Archive and native functions expose the full restricted register. Protect identifiers, counts, references and digests. Copying a projection does not enforce current revocation. Authorized competing writers can infer that a key is unavailable; unauthorized calls get a uniform refusal before lookup. There is no zero-knowledge or timing guarantee.

The reference permits 2,000 retained events, 256 descriptors per batch and an 8 MiB canonical complete archive. It replays full history for each operation. Crash tests cover process exits, not power-loss or lying hardware. Exact build pins and per-event full-state digests prevent silent reinterpretation of history. Hashes establish byte consistency, not source authenticity or latest-head continuity. Diagnostics retain compact observations only: at most 128 total and 8 per actor/scope/epoch, with uniform no-event refusal at diagnostic, event or byte limits. Monitor capacity externally and reserve room for round closure; there is no rollover or emergency over-budget write. Native snapshots remain read-only historical projections with explicit predecessor checking.

END FILE 2/30 adoption-limits.md

BEGIN FILE 3/30 bindings/native-v3.md sha256:53bd4a6a1f19896fd7ec53a6ec02c29deea9fac404ad3b5f3fa594a19258f251
# Native V3 binding

One SyncRegister object and the object-valued sync.register.snapshot fact path form an aggregate projection. The closed native value contains bootstrap, exact executable/schema buildId, complete journal with full-state outcome digests, root, version and non-resumable marker; derived state is omitted and reconstructed exactly by archive_from_native. The schema root describes this native value; its $defs describe command and journal records. This is the companion namespace, never a field of Project or Person. The native ID is the exact registerId, restricted to 3..160 native-safe alphanumeric/colon/dot/underscore/hyphen characters; incompatible IDs are refused without rewriting. The generated object is appended once. Subsequent snapshots use content-root-derived fact IDs and strictly extend a trusted earlier snapshot. Re-exporting the same cut retains its fact ID even if a later capture time changes envelope bytes; it does not create a new revision. Preserve the first stored fact; the native writer refuses duplicate IDs. The companion closes the fact envelope and checks exact authority types.

acceptance.py uses pinned WM-XCT-040 0.1.1 to stage the companion and its separately semantic-only WM-XCT-012 reference into three NEW synthetic organizational/commercial-company Dimensions. Fixture publication metadata anticipates candidate installation; it is not evidence of production publication. The installed sync_register.py and sync.schema.json are read back byte-for-byte and executed. No existing production Dimension is migrated.

Write the object before facts with the native writer. Check native envelopes, then validate_native_snapshot on the installed companion with the trusted previous fact. This enforces full replay, exact prefix preservation, bootstrap consistency, root/provenance and snapshot identities. It does not prove that a first snapshot is latest/authentic or that the supplied predecessor was historically authorized. The host owns both trust decisions. Generic native schema validation deliberately accepts arbitrary object values and cannot substitute for this check.

authority.rank=0 identifies snapshot storage authority only, never business source precedence. The journal remains master. Neither fact supersession nor object retirement changes source/business state. No native import resumes synchronization. Authentication and current disclosure must wrap privileged functions separately.

END FILE 3/30 bindings/native-v3.md

BEGIN FILE 4/30 sync_register.py sha256:0a1a2c6ed493ca9353897ea1954d60f37bd5f35144d654a6bb078f50b024600a
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
MAX_EVENTS=2000
MAX_BYTES=8*1024*1024
MAX_CONFLICTS=128
MAX_CONFLICTS_PER_WRITER_SCOPE_EPOCH=8
SCHEMA=json.loads((Path(__file__).with_name('sync.schema.json')).read_text(encoding='utf-8'))
BUILD_ID='sha256:'+hashlib.sha256(Path(__file__).read_bytes()+b'\0'+Path(__file__).with_name('sync.schema.json').read_bytes()).hexdigest()
DENIED={'status':'not-accepted'}

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
            require(not any(0xd800<=ord(c)<=0xdfff for c in x),'surrogate')
            require(not any(ord(c)<32 or 0x7f<=ord(c)<=0x9f for c in x),'control character')
    walk(value)
    raw=json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')
    require(len(raw)<=MAX_BYTES,'byte budget')
    return raw
def digest(value):return 'sha256:'+hashlib.sha256(encode(value)).hexdigest()
def decode(raw):
    require(len(raw)<=MAX_BYTES,'byte budget')
    if type(raw)==bytes:raw=raw.decode('utf-8',errors='strict')
    require(type(raw)==str and not raw.startswith('\ufeff'),'UTF-8 without BOM required')
    def pairs(items):
        out={}
        for k,v in items:require(k not in out,'duplicate JSON key');out[k]=v
        return out
    value=json.loads(raw,object_pairs_hook=pairs,parse_float=lambda _:(_ for _ in ()).throw(Invalid('float')),
                     parse_constant=lambda _:(_ for _ in ()).throw(Invalid('constant')))
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
    matches=[h[-1] for h in state['mappings'].values() if h[-1]['lineage']==lin and h[-1]['definition']['purpose']==purpose and h[-1]['state']=='active']
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
     
PAYLOAD END — FRAGMENT 2/16
