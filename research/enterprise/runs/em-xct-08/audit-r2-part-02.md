Continuation of the same frozen R2 no-tools audit. ACK only; do not audit yet.
FRAGMENT 2/15
PAYLOAD BEGIN
The reference's complete flag is deliberately a strong key-accounting condition: a terminal page exists, no error or quarantine remains in the round, and all retained items are snapshot-read with known generations. It does not certify actual source completeness. Best-effort may be fully accounted yet cannot support absence comparison. A host must establish actual consistency and visibility before declaring them.

assess_rounds validates the complete restricted archive first. It requires two complete rounds, increasing local seal sequence, identical scope/purpose, source-snapshot consistency in both, visibilityCovered in both and the later round's explicit earlier-round/not-earlier witness. Opaque LSN/token values are not compared. Different epochs alone do not break comparison. Changed source-instance generation, filter, principal visibility or interpretation changes the scope and breaks it. Unknown order, missing pages or inadequate key coverage returns insufficient-context.

For a known lineage present in the earlier round and not the later, an explicit intervening deletion/removal/inaccessibility observation is reported separately. Otherwise the result is only not-observed-in-comparable-rounds with steward-review-only action and an empty effects list. Same principal does not prove unchanged per-object visibility. No absence result deletes data, retracts a mapping, chooses a fact or retires a subject. Cross-register/foreign-archive round comparison is not implemented.

## Export, versions and operational limits

Archives preserve bootstrap, complete journal, exact derived state, root and version. validate_archive recomputes history and rejects edited outcomes, missing evidence, changed state or unsupported versions. inspect_import returns a historical-only report or an explicit LossReport. It does not create a writable database. resume_archive always refuses. Original epoch states remain unchanged as historical evidence; the archive wrapper is non-resumable. Upgrade/downgrade transformations, origin-host handover and writable restoration are deferred, not silently approximated.

A normal process restart can reopen the same locally owned database. The host must establish that it is the current owned store. The reference cannot detect a coherent old backup or two cloned databases and has no live ownership token service. Another host starts a new local register/epoch and fresh acquisition baseline; it does not continue from an imported token. Fresh-source/baseline truth remains external because this reference has no network connector.

Budgets: 2,000 retained journal entries; 256 input records/descriptors per batch; 256 catalogue targets/pairs/grants; 32 round-error references; one complete archive at most 8 MiB of the reference's canonical JSON encoding. A new retained event is refused before persistence if its archive would exceed the budget; no-event exact retries and uniform unauthorized refusals remain available at the event limit. Generated journal entries are schema-checked before persistence. These are demonstration limits, not enterprise throughput targets. The journal is replayed on each operation; large-scale indexing/partitioning needs a separately reviewed implementation.

Canonical encoding uses Python sorted-key, compact, UTF-8 JSON with ordered arrays; floats, duplicate JSON keys, non-string keys and unpaired surrogates are refused. It is explicitly not RFC 8785/JCS. IDs are restricted URNs, lexical source keys remain exact bounded strings. Supplied SHA-256 values are declarations; no payload is fetched to confirm them. Schema version, object revision, journal sequence, epoch and source/record generation are independent values.

## Native binding and release posture

The native V3 binding is one SyncRegister object and a restricted sync.register.snapshot fact pointing to this exact companion/version and carrying its closed journal snapshot. The snapshot omits redundant derived state; installed replay reconstructs the exact complete archive. sync.schema.json closes this native value at the root, with command and journal definitions in $defs. One aggregate projection has an explicit owner, boundary and calculation rule. Generic business fact resolution must not treat this register snapshot as a Project field. Native outer validation and installed companion replay must both run; outer validity alone does not establish nested semantics, authenticity or current state.

This file currently describes an implementation candidate. Executed test reports and native acceptance state what was run. Separate frozen Claude/Grok audits are tracked in review.json and review.md; this candidate text alone makes no audit-acceptance claim. Published lifecycle, research assurance, implementation evidence and broader-contour completion remain separate. A source synchronization package is not a Company model or a production connector deployment.

END FILE model-spec.md

BEGIN FILE adoption-limits.md sha256:2ee87bbf00113fd1167b235fce4196f3ba10bde75543cc265296c675cac67438
Complete text; display newlines may normalize CRLF to LF. SHA identifies original bytes.
# Adoption limits

Version 0.1.0 is a bounded original companion and local executable reference. Research assurance remains reviewable-draft. Startups may use source, scope and descriptive mapping governance without enterprise infrastructure. The international and AI examples are synthetic scenarios, not claims about named companies.

Executable use requires authenticated actors, verified source/steward declarations, current policy/target catalogue, trusted host clock, protected evidence storage and a current owned SQLite database. These duties are not supplied by this package. Metadata-only commits neither acquire external bytes nor apply business facts. IAM, live connectors, distributed effects, partitions, complete erasure/retention, quarantine resolution, writable archive import, automatic EFA/EAP adapters and production-scale storage are deferred.

Archive and native functions expose the full restricted register. Protect identifiers, counts, references and digests. Copying a projection does not enforce current revocation. Authorized competing writers can infer that a key is unavailable; unauthorized calls get a uniform refusal before lookup. There is no zero-knowledge or timing guarantee.

The reference permits 2,000 retained events, 256 descriptors per batch and an 8 MiB canonical complete archive. It replays full history for each operation. Crash tests cover process exits, not power-loss or lying hardware. Hashes establish byte consistency, not source authenticity or latest-head continuity. Native snapshots remain read-only historical projections with explicit predecessor checking.

END FILE adoption-limits.md

BEGIN FILE bindings/native-v3.md sha256:3f4da9c31fcd8916ae23d0e7fe29d21c64a5698ecc120f4ac3e1595b3eb26972
Complete text; display newlines may normalize CRLF to LF. SHA identifies original bytes.
# Native V3 binding

One SyncRegister object and the object-valued sync.register.snapshot fact path form an aggregate projection. The closed native value contains bootstrap, complete journal, root, version and non-resumable marker; derived state is omitted and reconstructed exactly by archive_from_native. The schema root describes this native value; its $defs describe command and journal records. This is the companion namespace, never a field of Project or Person. The native ID is the exact registerId, restricted to 3..160 native-safe alphanumeric/colon/dot/underscore/hyphen characters; incompatible IDs are refused without rewriting. The generated object is appended once. Subsequent snapshots use content-root-derived fact IDs and strictly extend a trusted earlier snapshot. Re-exporting the same cut does not create a new revision.

acceptance.py uses pinned WM-XCT-040 0.1.1 to stage the companion and its separately semantic-only WM-XCT-012 reference into three NEW synthetic organizational/commercial-company Dimensions. Fixture publication metadata anticipates candidate installation; it is not evidence of production publication. The installed sync_register.py and sync.schema.json are read back byte-for-byte and executed. No existing production Dimension is migrated.

Write the object before facts with the native writer. Check native envelopes, then validate_native_snapshot on the installed companion with the trusted previous fact. This enforces full replay, exact prefix preservation, bootstrap consistency, root/provenance and snapshot identities. It does not prove that a first snapshot is latest/authentic or that the supplied predecessor was historically authorized. The host owns both trust decisions. Generic native schema validation deliberately accepts arbitrary object values and cannot substitute for this check.

authority.rank=0 identifies snapshot storage authority only, never business source precedence. The journal remains master. Neither fact supersession nor object retirement changes source/business state. No native import resumes synchronization. Authentication and current disclosure must wrap privileged functions separately.

END FILE bindings/native-v3.md

BEGIN FILE sync_register.py sha256:334962ff837ca04775fab83314eed05cf54ae24d7d989f6f332302948cfb4aa9
Complete text; display newlines may normalize CRLF to LF. SHA identifies original bytes.
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
SCHEMA=json.loads((Path(__file__).with_name('sync.schema.json')).read_text(encoding='utf-8'))
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
    walk(value)
    raw=json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')
    require(len(raw)<=MAX_BYTES,'byte budget')
    return raw
def digest(value):return 'sha256:'+hashlib.sha256(encode(value)).hexdigest()
def decode(raw):
    require(len(raw)<=MAX_BYTES,'byte budget')
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
    return datetime.strptime(value,'%Y-%m-%dT%H:%M:%SZ')
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

PAYLOAD END — FRAGMENT 2/15
