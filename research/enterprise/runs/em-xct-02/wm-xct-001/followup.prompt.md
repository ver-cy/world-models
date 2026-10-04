# Focused remediation audit — Enterprise Fact Authority 0.1.0
No tools, no web, no code execution. You are a reviewer, not an approver. Independently check the changed code and machine binding below against the dispositions. Prior frozen audit and its blockers are preserved. Return BLOCK only for a concrete defect in this bounded trusted-host reference, or ACCEPT WITH LIMITS with exact remaining holds. Check B1/B2, M1–M5 and observation retention/part pins. Do not infer production IAM, durable transactional support or parent conformance. Publication and research assurance are distinct. This is a materially revised frozen implementation, not a retry of the earlier input. Verify that own model ID, own spec digest, semantic-only parent and register operator resolve machine contradictions. Explain if remaining holes are disclosed deferrals versus internal contradictions.
# Frozen audit remediation

Original audits are retained. Claude returned BLOCK for native identity and envelope authority; Grok returned ACCEPT WITH LIMITS with a medium observation-retention concern. These are research reviews, not authorization. No previous publication occurred for this version.

| Finding | Change / disposition |
|---|---|
| Claude B1 | Own runtime ID `vr.profile.enterprise-fact-authority`, namespace, spec.json and binding digest. WM-XCT-001 is semantic-only, binding=null; optional exact reference. Both are explicit synthetic composition roots. Publication lifecycle and reviewable-draft research assurance remain separate; the composer itself requires published releases. Prepublication tests use candidate metadata and do not claim production already exists |
| Claude B2 | Envelope source is independent register-operator, masterSystem governance-register. Acceptance asserts it differs from accountable/steward roles. Domain precedence remains nested rule logic |
| Claude M1 | validate_extension checks identical header, exact prior collection prefixes and strictly later appended receipts. Native acceptance rebuilds archive using admit, admits a correction, stores r1/r2 with supersedes and previous digest, and rejects actual stored truncation |
| Claude M2 | Retry compares the payload excluding only restamped recordedAt, keeps original receipt. Current authorization still required. Changed payload is rejected |
| Claude M3 | Writer becomes per-revision attribution; source and subject remain immutable. A currently granted successor writer can retract an earlier same-source assertion; original attribution survives in history |
| Claude M4 | Explicit trusted-host-only function, never a public endpoint. Host must return receipt/generic rejection to non-readers, never ledger or raw diagnostics. This release does not implement a service projection; limitation stays visible |
| Claude M5 | Required change kind genesis/correction/closure/retraction. Closure guards unchanged start/party/value and clipped term end, while allowing revision/receipt/issuer-or-writer/evidence metadata. Full-term correction remains intentionally possible and labeled |
| Claude L1 | Explicit observation revision pins and rule/route part pins (ID plus containing authority revision/digest) |
| Claude L2 | Part IDs cannot equal parties/sources/writers/accountable/publisher in that authority |
| Claude L3 / Grok medium | Matching observations/evidence/pins are collected before unknown or contested-authority returns; no selected value is invented |
| Claude L4 | Governance can explicitly issue write grants including itself. No implicit grant; no separate dual-control policy claimed |
| Claude L5 | Semantic edge labels distinguish discovery/selected patterns, read-contract patterns only, and assertion patterns; WriteGrant is original |
| Claude L6 | Composition plan/policy validity windows are derived from current UTC for each acceptance run. Synthetic domain evaluation clocks remain fixed and documented |
| Claude L7 | Input digest includes register header. Record digests are bare hex; native asset descriptors use required sha256: prefix, explicitly documented |
| Claude L8 | Configuration is trusted host data. Host-facing generic-error obligation includes config diagnostics. No direct untrusted endpoint supported |
| Grok low overlap | Archives retain contested write grants; live admission denies ambiguity. This is intentional and now explicit |
| Grok low observation interval | Assertion interval can exceed policy term; selection without authority returns unknown and retains observations. No invented authority or discarded history |
| Grok low Denied inheritance | Denied is a distinct ValueError type; guide instructs separate handling |
| Grok URI optics | Own machine namespace/specification; associated hosting URI remains. No subtype or parent-native claim |

Unchanged limits include independent assignment revision streams, signed publication, recursive delegation, real source connectors, subject/scope proof, durable concurrent storage, fine-grained disclosure and legal/domain conformance. Candidate custom profile ID is local to this published companion package; it is not a new canonical WM catalog row or a promise that the public model resolver accepts that ID independently.

## FILE authority.py
```
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

```

## FILE authority.schema.json
```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://ver.cy/models/wm-xct-001-ownership-stewardship/profiles/enterprise-fact-authority/0.1.0/authority.schema.json",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "format",
    "version",
    "dimension",
    "authorities",
    "observations"
  ],
  "properties": {
    "format": {
      "const": "vercy-fact-authority"
    },
    "version": {
      "const": "0.1.0"
    },
    "dimension": {
      "type": "string",
      "format": "uri",
      "maxLength": 500
    },
    "authorities": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/authority"
      },
      "minItems": 0,
      "maxItems": 10000,
      "uniqueItems": true
    },
    "observations": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/observation"
      },
      "minItems": 0,
      "maxItems": 10000,
      "uniqueItems": true
    }
  },
  "$defs": {
    "stewardship": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "party",
        "duties",
        "validFrom",
        "validUntil",
        "evidence"
      ],
      "properties": {
        "id": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "party": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "duties": {
          "type": "array",
          "items": {
            "enum": [
              "maintain-quality",
              "resolve-conflict",
              "coordinate-transfer"
            ]
          },
          "minItems": 1,
          "maxItems": 10000,
          "uniqueItems": true
        },
        "validFrom": {
          "type": "string",
          "format": "date-time",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
        },
        "validUntil": {
          "type": "string",
          "format": "date-time",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
        },
        "evidence": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "uri",
            "maxLength": 500
          },
          "minItems": 1,
          "maxItems": 10000,
          "uniqueItems": true
        }
      }
    },
    "rule": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "source",
        "priority",
        "validFrom",
        "validUntil",
        "evidence"
      ],
      "properties": {
        "id": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "source": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "priority": {
          "type": "integer",
          "minimum": 0,
          "maximum": 1000000
        },
        "validFrom": {
          "type": "string",
          "format": "date-time",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
        },
        "validUntil": {
          "type": "string",
          "format": "date-time",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
        },
        "evidence": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "uri",
            "maxLength": 500
          },
          "minItems": 1,
          "maxItems": 10000,
          "uniqueItems": true
        }
      }
    },
    "writeGrant": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "source",
        "writers",
        "validFrom",
        "validUntil",
        "evidence"
      ],
      "properties": {
        "id": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "source": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "writers": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "uri",
            "maxLength": 500
          },
          "minItems": 1,
          "maxItems": 10000,
          "uniqueItems": true
        },
        "validFrom": {
          "type": "string",
          "format": "date-time",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
        },
        "validUntil": {
          "type": "string",
          "format": "date-time",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
        },
        "evidence": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "uri",
            "maxLength": 500
          },
          "minItems": 1,
          "maxItems": 10000,
          "uniqueItems": true
        }
      }
    },
    "authority": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "dimension",
        "scope",
        "predicate",
        "change",
        "revision",
        "previousDigest",
        "recordedAt",
        "validFrom",
        "validUntil",
        "evidence",
        "governs",
        "definitionAuthorityRef",
        "issuedBy",
        "accountable",
        "state",
        "stewardships",
        "rules",
        "writeGrants"
      ],
      "properties": {
        "id": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "dimension": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "scope": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "predicate": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "change": {
          "enum": [
            "genesis",
            "correction",
            "closure",
            "retraction"
          ]
        },
        "revision": {
          "type": "integer",
          "minimum": 1
        },
        "previousDigest": {
          "anyOf": [
            {
              "type": "null"
            },
            {
              "type": "string",
              "pattern": "^[a-f0-9]{64}$"
            }
          ]
        },
        "recordedAt": {
          "type": "string",
          "format": "date-time",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
        },
        "validFrom": {
          "type": "string",
          "format": "date-time",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
        },
        "validUntil": {
          "type": "string",
          "format": "date-time",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
        },
        "evidence": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "uri",
            "maxLength": 500
          },
          "minItems": 1,
          "maxItems": 10000,
          "uniqueItems": true
        },
        "governs": {
          "const": "values"
        },
        "definitionAuthorityRef": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "issuedBy": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "accountable": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "state": {
          "enum": [
            "active",
            "retracted"
          ]
        },
        "stewardships": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/stewardship"
          },
          "minItems": 0,
          "maxItems": 10000,
          "uniqueItems": true
        },
        "rules": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/rule"
          },
          "minItems": 0,
          "maxItems": 10000,
          "uniqueItems": true
        },
        "writeGrants": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/writeGrant"
          },
          "minItems": 0,
          "maxItems": 10000,
          "uniqueItems": true
        }
      }
    },
    "value": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "datatype",
        "lexical"
      ],
      "properties": {
        "datatype": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "lexical": {
          "type": "string",
          "maxLength": 10000
        }
      }
    },
    "observation": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "dimension",
        "scope",
        "predicate",
        "change",
        "revision",
        "previousDigest",
        "recordedAt",
        "validFrom",
        "validUntil",
        "evidence",
        "subject",
        "source",
        "writer",
        "state",
        "value"
      ],
      "properties": {
        "id": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "dimension": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "scope": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "predicate": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "change": {
          "enum": [
            "genesis",
            "correction",
            "closure",
            "retraction"
          ]
        },
        "revision": {
          "type": "integer",
          "minimum": 1
        },
        "previousDigest": {
          "anyOf": [
            {
              "type": "null"
            },
            {
              "type": "string",
              "pattern": "^[a-f0-9]{64}$"
            }
          ]
        },
        "recordedAt": {
          "type": "string",
          "format": "date-time",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
        },
        "validFrom": {
          "type": "string",
          "format": "date-time",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
        },
        "validUntil": {
          "type": "string",
          "format": "date-time",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
        },
        "evidence": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "uri",
            "maxLength": 500
          },
          "minItems": 1,
          "maxItems": 10000,
          "uniqueItems": true
        },
        "subject": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "source": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "writer": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "state": {
          "enum": [
            "asserted",
            "retracted"
          ]
        },
        "value": {
          "$ref": "#/$defs/value"
        }
      }
    },
    "config": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "dimension",
        "validFrom",
        "validUntil",
        "governors",
        "readers",
        "purposes"
      ],
      "properties": {
        "id": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "dimension": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "validFrom": {
          "type": "string",
          "format": "date-time",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
        },
        "validUntil": {
          "type": "string",
          "format": "date-time",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
        },
        "governors": {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": false,
            "required": [
              "actor",
              "scope",
              "predicate"
            ],
            "properties": {
              "actor": {
                "type": "string",
                "format": "uri",
                "maxLength": 500
              },
              "scope": {
                "type": "string",
                "format": "uri",
                "maxLength": 500
              },
              "predicate": {
                "type": "string",
                "format": "uri",
                "maxLength": 500
              }
            }
          },
          "minItems": 1,
          "maxItems": 10000,
          "uniqueItems": true
        },
        "readers": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "uri",
            "maxLength": 500
          },
          "minItems": 1,
          "maxItems": 10000,
          "uniqueItems": true
        },
        "purposes": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1
          },
          "minItems": 1,
          "maxItems": 10000,
          "uniqueItems": true
        }
      }
    },
    "ledger": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "format",
        "version",
        "dimension",
        "authorities",
        "observations"
      ],
      "properties": {
        "format": {
          "const": "vercy-fact-authority"
        },
        "version": {
          "const": "0.1.0"
        },
        "dimension": {
          "type": "string",
          "format": "uri",
          "maxLength": 500
        },
        "authorities": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/authority"
          },
          "minItems": 0,
          "maxItems": 10000,
          "uniqueItems": true
        },
        "observations": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/observation"
          },
          "minItems": 0,
          "maxItems": 10000,
          "uniqueItems": true
        }
      }
    }
  }
}

```

## FILE acceptance.py
```
"""Trusted synthetic new-Dimension composition, admission and snapshot checks."""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from datetime import datetime,timedelta,timezone
from pathlib import Path
import authority as p
HERE=Path(__file__).resolve().parent
PROFILE_ID='vr.profile.enterprise-fact-authority'
SLUG='enterprise-fact-authority'
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
                binding={'id':'urn:vercy:binding:enterprise-fact-authority','version':'0.1.0','forSpecificationDigest':ds['digest'],'runtime':descriptor(folder,'runtime-model.reference.json',HERE/'runtime-model.reference.json',base+'runtime-model.reference.json'),'instanceSchema':descriptor(folder,'authority.schema.json',HERE/'authority.schema.json',base+'authority.schema.json'),'companionValidator':descriptor(folder,'authority.py',HERE/'authority.py',base+'authority.py'),'scope':'Own companion namespace/specification; no parent subtype. Explicit nested validation and admission required.'}
            return {'modelId':mid,'version':version,'namespace':'urn:vercy:model:'+mid,'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','requires':[],'references':[],'specification':ds,'agents':da,'installationMode':'native-binding' if native else 'semantic-only','binding':binding,'semanticFingerprint':None,'compatibility':{'decision':'accepted','reviewer':'urn:synthetic:reviewer:authority','evidence':'urn:synthetic:acceptance:authority','observedAt':at,'scope':'Synthetic candidate-installation exercise, not global parent ratification; publication and research assurance are separate.'}}
        parent='wm-xct-001-ownership-stewardship';up=HERE/'upstream'/parent
        semantic=release('vr.wm-xct-001','0.3.0-research.1',parent,up/'spec.yaml',up/'AGENTS.md','https://ver.cy/models/'+parent+'/versions/0.3.0-research.1/',False)
        companion=release(PROFILE_ID,'0.1.0',SLUG,HERE/'spec.json',HERE/'AGENTS.md','https://ver.cy/models/'+parent+'/profiles/enterprise-fact-authority/0.1.0/',True)
        companion['references']=[{'modelId':semantic['modelId'],'version':semantic['version']}];releases=[semantic,companion]
        for name in ['startup','group','ai-team']:
            config=p.load(HERE/('examples/'+name+'.config.json'));fixture=p.load(HERE/('examples/'+name+'.json'));target=root/name;stage=root/(name+'-stage');pp=root/(name+'-policy.json');lp=root/(name+'-lock.json');planp=root/(name+'-plan.json');dimension=config['dimension']
            policy={'format':'vercy-composition-policy','version':1,'id':'urn:synthetic:composition-policy:authority','dimensionId':dimension,'owner':'urn:synthetic:owner:installation','allowInstall':True,'actors':['urn:synthetic:actor:composer'],'purposes':['Synthetic fact authority reference'],'allowedModelIds':[r['modelId'] for r in releases],'allowedOrigins':['https://ver.cy'],'reviewers':['urn:synthetic:reviewer:authority'],'allowReviewableDrafts':True,'validFrom':at,'validUntil':expires}
            pp.write_bytes(c.encode(policy));lp.write_bytes(c.encode({'models':[]}))
            plan={'format':'vercy-composition-plan','schemaVersion':'1.0.0','planId':'urn:synthetic:composition:authority:'+name,'revision':1,'supersedes':None,'algorithm':'exact-closure-v1','dimensionId':dimension,'createdAt':at,'validUntil':expires,'baseLockDigest':c.digest(lp.read_bytes()),'roots':[{'modelId':r['modelId'],'version':r['version']} for r in releases],'releases':releases,'authority':{'actor':policy['actors'][0],'allowReviewableDrafts':True,'allowedModelIds':policy['allowedModelIds'],'decision':'allow','owner':policy['owner'],'policyDigest':c.digest(pp.read_bytes()),'policyRef':policy['id'],'purpose':policy['purposes'][0]},'provenance':{'classification':'public-synthetic','evidenceKind':'proposal','masterSystem':'urn:synthetic:reference','recordedAt':at,'source':'urn:synthetic:fixture:'+name}}
            planp.write_bytes(c.encode(plan));c.stage(planp,assets,pp,lp,stage);bootstrap(stage,pp,lp,skill,target,'Synthetic authority '+name,dimension)
            installed=target/'models/composed'/SLUG/'authority.py';p.require(c.digest(installed.read_bytes())==companion['binding']['companionValidator']['digest'],'Code differs');p.require(c.digest((installed.parent/'authority.schema.json').read_bytes())==companion['binding']['instanceSchema']['digest'],'Schema differs')
            ms=importlib.util.spec_from_file_location('installed_authority_'+name,installed);module=importlib.util.module_from_spec(ms);ms.loader.exec_module(module)
            ledger=module.empty(dimension)
            entries=sorted([(x,'authority') for x in fixture['authorities']]+[(x,'observation') for x in fixture['observations']],key=lambda item:item[0]['recordedAt'])
            for row,kind in entries:ledger=module.admit(ledger,row,kind,config,row['issuedBy'] if kind=='authority' else row['writer'],row['recordedAt'])
            p.require(ledger==fixture,'Fixture admission differs');module.validate_extension(module.empty(dimension),ledger,config)
            correction=copy.deepcopy(ledger['observations'][-1]);correction.update(revision=2,previousDigest=module.digest(correction),change='correction',recordedAt='2026-09-21T10:01:00Z',value=copy.deepcopy(ledger['observations'][0]['value']))
            updated=module.admit(ledger,correction,'observation',config,correction['writer'],correction['recordedAt']);module.validate_extension(ledger,updated,config)
            oid=dimension+':authority-register';operator='urn:synthetic:register-operator';register='urn:synthetic:governance-register'
            p.require(all(operator!=a['accountable'] and all(operator!=s['party'] for s in a['stewardships']) for a in updated['authorities']),'Envelope operator is not a steward/accountable role')
            obj={'recordType':'object','schemaVersion':'1.0.0','recordId':oid+':object-r1','objectId':oid,'objectType':PROFILE_ID+':authority-register','name':'Synthetic authority register','description':'Own companion namespace, not a ControlRecord or Company','recordedAt':at,'previousRecordId':None,'state':'active','provenance':{'source':register,'synthetic':True},'accessClass':'synthetic-private'}
            path=root/(name+'-object.json');path.write_bytes(p.encode(obj));append(target,'object',path);facts=[]
            for i,snapshot in enumerate([ledger,updated],1):
                fact={'recordType':'fact','schemaVersion':'1.0.0','factId':oid+':snapshot-r'+str(i),'subjectId':oid,'path':'authority.register.snapshot','value':snapshot,'unit':None,'validFrom':at,'validTo':None,'recordedAt':at,'supersedes':[] if i==1 else [oid+':snapshot-r1'],'status':'asserted','provenance':{'source':register,'synthetic':True,'snapshotDigest':p.digest(snapshot),'previousSnapshotDigest':None if i==1 else p.digest(ledger)},'authority':{'source':operator,'rank':0},'masterSystem':register,'accessClass':'synthetic-private'}
                path=root/(name+'-fact'+str(i)+'.json');path.write_bytes(p.encode(fact));result=append(target,'fact',path);facts.append(target/result['written'])
            stored=[p.load(x)['value'] for x in facts];p.require(stored==[ledger,updated],'Stored round-trip differs');module.validate_extension(stored[0],stored[1],config)
            def evaluate(snapshot):return module.evaluate(snapshot,config,actor='urn:synthetic:reader',purpose='governance-review',scope='urn:synthetic:scope',predicate='urn:synthetic:predicate',subject='urn:synthetic:subject',validAt='2026-09-21T12:00:00Z',knownAt='2026-09-21T12:00:00Z',now='2026-09-21T12:00:00Z')
            decisions=[evaluate(x) for x in stored];p.require(decisions[0]['status']==('contested' if name=='startup' else 'preferred') and decisions[1]['status']=='preferred','Stored outcomes differ')
            native=native_validate(target);p.require(native['valid'],'Native validation failed');victim=facts[-1];original=victim.read_bytes();bad=p.load(victim);bad['value']['authorities'][0]['rules'][0]['priority']=-1;victim.write_bytes(p.encode(bad));negative=native_validate(target);rejected=False
            try:module.validate_ledger(p.load(victim)['value'],config)
            except module.Invalid:rejected=True
            finally:victim.write_bytes(original)
            p.require(negative['valid'] and rejected,'Native/companion distinction missing')
            truncated=p.load(victim);truncated['value']=copy.deepcopy(stored[0]);truncated['value']['observations'].pop();victim.write_bytes(p.encode(truncated));truncation_rejected=False
            try:module.validate_extension(stored[0],p.load(victim)['value'],config)
            except module.Invalid:truncation_rejected=True
            finally:victim.write_bytes(original)
            p.require(truncation_rejected,'Snapshot truncation was accepted');native.pop('dimension',None);negative.pop('dimension',None)
            reports.append({'profile':name,'objects':1,'facts':2,'native':native,'roundTripEqualsInput':True,'admissionReplayedThroughInstalledCompanion':True,'snapshotTruncationRejected':True,'storedDecisions':decisions,'invalidNestedSnapshot':{'native':negative,'companionRejected':rejected},'envelopeOperator':operator,'envelopeAuthorityMeaning':'Snapshot storage only; never domain fact precedence','pins':[{'id':r['modelId'],'version':r['version'],'digest':r['specification']['digest'],'mode':r['installationMode']} for r in releases]})
    return {'format':'vercy-authority-profile-acceptance','executedAt':c.now(),'passed':len(reports),'failed':0,'profiles':reports,'sourceDigests':{str(x.relative_to(HERE)):hashlib.sha256(x.read_bytes()).hexdigest() for x in [Path(__file__),HERE/'authority.py',HERE/'authority.schema.json',HERE/'spec.json',HERE/'tool-pins.json',*sorted((HERE/'examples').glob('*.json'))]},'limits':'Synthetic new Dimensions; semantic-only parent plus separately identified companion. Candidate-installation metadata anticipates publication. No IAM, source truth, durable concurrency or existing-Dimension migration proof.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True);args=ap.parse_args();report=run(args.composer,args.skill);Path(args.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':report['passed'],'failed':report['failed']}))

```

## FILE test_authority.py
```
import copy,json,unittest
from pathlib import Path
import authority as a
P=Path(__file__).resolve().parent
NOW='2026-09-21T12:00:00Z';START='2026-01-01T00:00:00Z';END='2027-01-01T00:00:00Z'
G='urn:synthetic:governor';W='urn:synthetic:writer';READ='urn:synthetic:reader'
D='urn:synthetic:dimension';S='urn:synthetic:scope';F='urn:synthetic:predicate';SUB='urn:synthetic:subject'
def config():return {'id':'urn:synthetic:config','dimension':D,'validFrom':START,'validUntil':END,'governors':[{'actor':G,'scope':S,'predicate':F}],'readers':[READ],'purposes':['governance-review']}
def policy():
    return {'id':'urn:synthetic:authority','dimension':D,'scope':S,'predicate':F,'governs':'values','definitionAuthorityRef':'urn:synthetic:definition-owner-record','change':'genesis','revision':1,'previousDigest':None,'recordedAt':'2026-09-21T10:00:00Z','validFrom':START,'validUntil':END,'evidence':['urn:synthetic:appointment'],'issuedBy':G,'accountable':'urn:synthetic:owner','state':'active','stewardships':[{'id':'urn:synthetic:stewardship','party':'urn:synthetic:steward','duties':['resolve-conflict'],'validFrom':START,'validUntil':END,'evidence':['urn:synthetic:mandate']}],'rules':[{'id':'urn:synthetic:rule:'+s,'source':'urn:synthetic:source:'+s,'priority':0,'validFrom':START,'validUntil':END,'evidence':['urn:synthetic:rule-evidence']} for s in ['a','b']],'writeGrants':[{'id':'urn:synthetic:write:'+s,'source':'urn:synthetic:source:'+s,'writers':[W],'validFrom':START,'validUntil':END,'evidence':['urn:synthetic:write-evidence']} for s in ['a','b']]}
def observation(n=1,value='A'):
    return {'id':'urn:synthetic:observation:'+str(n),'dimension':D,'scope':S,'predicate':F,'change':'genesis','revision':1,'previousDigest':None,'recordedAt':'2026-09-21T10:00:0'+str(n)+'Z','validFrom':START,'validUntil':END,'evidence':['urn:synthetic:evidence:'+str(n)],'subject':SUB,'source':'urn:synthetic:source:'+('a' if n==1 else 'b'),'writer':W,'state':'asserted','value':{'datatype':'urn:synthetic:string','lexical':value}}
def fixture(profile='startup'):
    c=config();p=policy()
    if profile=='group':p['rules'][1]['priority']=10
    if profile=='ai-team':p['stewardships']=[]
    ledger=a.admit(a.empty(D),p,'authority',c,G,p['recordedAt'])
    for x in [observation(),observation(2,'B' if profile!='ai-team' else 'A')]:ledger=a.admit(ledger,x,'observation',c,W,x['recordedAt'])
    return c,ledger
def query(l,c,**kw):
    args=dict(actor=READ,purpose='governance-review',scope=S,predicate=F,subject=SUB,validAt=NOW,knownAt=NOW,now=NOW);args.update(kw)
    return a.evaluate(l,c,**args)
def revision(x,at='2026-09-21T10:01:00Z',**changes):
    y=copy.deepcopy(x);y.update(revision=x['revision']+1,previousDigest=a.digest(x),recordedAt=at,change='retraction' if changes.get('state')=='retracted' else 'correction');y.update(changes);return y
class Tests(unittest.TestCase):
    def setUp(self):self.c,self.l=fixture()
    def test_equal_conflict(self):
        r=query(self.l,self.c);self.assertEqual(r['status'],'contested');self.assertEqual(len(r['evidence']),2);self.assertEqual(r['routeTo'],['urn:synthetic:steward']);self.assertIsNone(r['value'])
    def test_lower_priority_late_csv(self):
        c,l=fixture('group');r=query(l,c);self.assertEqual(r['value']['lexical'],'A');self.assertEqual(len(r['observationIds']),2)
    def test_same_value_corroboration(self):
        c,l=fixture('ai-team');self.assertEqual(query(l,c)['status'],'preferred');self.assertEqual(query(l,c)['routeTo'],[])
    def test_reverse_import_receipts(self):
        l=a.empty(D);p=policy();l=a.admit(l,p,'authority',self.c,G,p['recordedAt'])
        for x in [dict(observation(2,'B'),recordedAt='2026-09-21T10:00:01Z'),dict(observation(),recordedAt='2026-09-21T10:00:02Z')]:l=a.admit(l,x,'observation',self.c,W,x['recordedAt'])
        left=query(l,self.c);right=query(self.l,self.c)
        for k in ['inputDigest','observationPins']:left.pop(k);right.pop(k)
        self.assertEqual(left,right)
    def test_owner_not_writer(self):
        x=observation(3);x['writer']='urn:synthetic:owner'
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'observation',self.c,x['writer'],x['recordedAt'])
    def test_steward_not_governor(self):
        x=policy();x['issuedBy']='urn:synthetic:steward'
        with self.assertRaises(a.Invalid):a.admit(a.empty(D),x,'authority',self.c,x['issuedBy'],x['recordedAt'])
    def test_confused_deputy(self):
        x=policy();x['issuedBy']=W
        with self.assertRaises(a.Invalid):a.admit(a.empty(D),x,'authority',self.c,W,x['recordedAt'])
    def test_no_authority(self):self.assertEqual(query(a.empty(D),self.c)['status'],'unknown')
    def test_no_observations(self):
        self.l['observations']=[];self.assertEqual(query(self.l,self.c)['reason'],'no-ranked-observation')
    def test_overlapping_authorities(self):
        p=policy();p['id']+=':other';p['recordedAt']='2026-09-21T10:02:00Z'
        for x in p['rules']+p['stewardships']+p['writeGrants']:x['id']+=':other'
        l=a.admit(self.l,p,'authority',self.c,G,p['recordedAt']);self.assertEqual(query(l,self.c)['status'],'authority-contested')
        x=observation(3)
        with self.assertRaises(a.Invalid):a.admit(l,x,'observation',self.c,W,'2026-09-21T11:00:00Z')
    def test_ambiguous_rules(self):
        p=revision(self.l['authorities'][0]);r=copy.deepcopy(p['rules'][0]);r['id']+=':duplicate';p['rules'].append(r)
        l=a.admit(self.l,p,'authority',self.c,G,p['recordedAt']);self.assertEqual(query(l,self.c)['reason'],'overlapping-source-rules')
    def test_ambiguous_write_grants(self):
        p=revision(self.l['authorities'][0]);r=copy.deepcopy(p['writeGrants'][0]);r['id']+=':duplicate';r['writers']=['urn:synthetic:other'];p['writeGrants'].append(r)
        l=a.admit(self.l,p,'authority',self.c,G,p['recordedAt']);x=observation(3);x['source']='urn:synthetic:source:a';x['recordedAt']='2026-09-21T11:00:00Z'
        with self.assertRaises(a.Invalid):a.admit(l,x,'observation',self.c,W,x['recordedAt'])
    def test_priority_does_not_grant_write(self):
        p=revision(self.l['authorities'][0]);p['writeGrants']=[];l=a.admit(self.l,p,'authority',self.c,G,p['recordedAt'])
        self.assertEqual(query(l,self.c)['status'],'contested')
        x=observation(3);x['recordedAt']='2026-09-21T11:00:00Z'
        with self.assertRaises(a.Invalid):a.admit(l,x,'observation',self.c,W,x['recordedAt'])
    def test_write_grant_does_not_grant_precedence(self):
        p=revision(self.l['authorities'][0]);p['rules']=[];l=a.admit(self.l,p,'authority',self.c,G,p['recordedAt'])
        x=observation(3);x['recordedAt']='2026-09-21T11:00:00Z';l=a.admit(l,x,'observation',self.c,W,x['recordedAt']);self.assertEqual(query(l,self.c)['status'],'unknown')
    def test_replay_idempotent(self):
        self.assertEqual(a.admit(self.l,self.l['observations'][0],'observation',self.c,W,NOW),self.l)
    def test_conflicting_replay(self):
        x=observation();x['value']['lexical']='C'
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'observation',self.c,W,NOW)
    def test_backdate_receipt(self):
        x=observation(3)
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'observation',self.c,W,NOW)
    def test_future_receipt(self):
        x=observation(3);x['recordedAt']='2026-09-22T00:00:00Z'
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'observation',self.c,W,NOW)
    def test_head_order(self):
        x=observation(3);x['recordedAt']=self.l['observations'][0]['recordedAt']
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'observation',self.c,W,x['recordedAt'])
    def test_correction_history(self):
        old=query(self.l,self.c);x=revision(self.l['observations'][1]);x['value']['lexical']='A'
        l=a.admit(self.l,x,'observation',self.c,W,x['recordedAt']);self.assertEqual(query(l,self.c)['status'],'preferred')
        self.assertEqual(query(l,self.c,knownAt='2026-09-21T10:00:02Z')['status'],old['status']);self.assertEqual(len(l['observations']),3)
    def test_retraction_history(self):
        x=revision(self.l['observations'][1],state='retracted');l=a.admit(self.l,x,'observation',self.c,W,x['recordedAt']);self.assertEqual(query(l,self.c)['status'],'preferred')
        self.assertEqual(query(l,self.c,knownAt='2026-09-21T10:00:02Z')['status'],'contested')
    def test_retroactive_rule(self):
        x=revision(self.l['authorities'][0]);x['rules'][1]['priority']=1
        l=a.admit(self.l,x,'authority',self.c,G,x['recordedAt']);self.assertEqual(query(l,self.c)['status'],'preferred');self.assertEqual(query(l,self.c,knownAt='2026-09-21T10:00:02Z')['status'],'contested')
    def test_transfer_preserves_valid_history(self):
        cutoff='2026-10-01T00:00:00Z';x=revision(self.l['authorities'][0],change='closure');x['validUntil']=cutoff
        for part in x['rules']+x['stewardships']+x['writeGrants']:part['validUntil']=cutoff
        l=a.admit(self.l,x,'authority',self.c,G,x['recordedAt']);new=policy();new['id']+=':successor';new['recordedAt']='2026-09-21T10:02:00Z';new['validFrom']=cutoff;new['accountable']='urn:synthetic:successor'
        for part in new['rules']+new['stewardships']+new['writeGrants']:part['id']+=':successor';part['validFrom']=cutoff
        l=a.admit(l,new,'authority',self.c,G,new['recordedAt']);self.assertEqual(query(l,self.c)['accountable'],'urn:synthetic:owner');self.assertEqual(query(l,self.c,validAt=cutoff)['accountable'],'urn:synthetic:successor')
    def test_unknown_source_retained(self):
        x=revision(self.l['authorities'][0]);x['rules']=x['rules'][:1];l=a.admit(self.l,x,'authority',self.c,G,x['recordedAt']);r=query(l,self.c);self.assertEqual(len(r['unrankedObservationIds']),1);self.assertEqual(len(r['evidence']),2)
    def test_denied_no_data(self):
        with self.assertRaisesRegex(a.Denied,'^Read denied$'):query({'secret':'bad'},self.c,actor='urn:synthetic:intruder')
    def test_purpose_denied(self):
        with self.assertRaises(a.Denied):query(self.l,self.c,purpose='advertising')
    def test_expired_root(self):
        with self.assertRaises(a.Invalid):query(self.l,self.c,now=END)
    def test_future_knowledge(self):
        with self.assertRaises(a.Invalid):query(self.l,self.c,knownAt=END)
    def test_cross_dimension(self):
        self.l['dimension']='urn:wrong'
        with self.assertRaises(a.Invalid):query(self.l,self.c)
    def test_scope_shopping(self):
        x=observation(3);x['scope']='urn:ungranted'
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'observation',self.c,W,x['recordedAt'])
    def test_policy_scope(self):
        x=policy();x['predicate']='urn:ungranted'
        with self.assertRaises(a.Invalid):a.admit(a.empty(D),x,'authority',self.c,G,x['recordedAt'])
    def test_value_not_coerced(self):
        self.l['observations'][0]['value']['lexical']='01';self.l['observations'][1]['value']['lexical']='1';self.assertEqual(query(self.l,self.c)['status'],'contested')
    def test_same_source_conflict(self):
        self.l['observations'][1]['source']=self.l['observations'][0]['source'];self.assertEqual(query(self.l,self.c)['status'],'contested')
    def test_future_steward(self):
        self.l['authorities'][0]['stewardships'][0]['validFrom']='2026-10-01T00:00:00Z';r=query(self.l,self.c);self.assertEqual(r['status'],'contested');self.assertEqual(r['routeTo'],[])
    def test_exclusive_interval_end(self):
        self.assertEqual(query(self.l,self.c,validAt=END)['status'],'unknown')
    def test_expired_write_grant(self):
        for r in self.l['authorities'][0]['writeGrants']:r['validUntil']='2026-09-21T11:00:00Z'
        x=observation(3);x['recordedAt']=NOW
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'observation',self.c,W,NOW)
        self.assertEqual(query(self.l,self.c)['status'],'contested')
    def test_query_wrong_subject(self):
        r=query(self.l,self.c,subject='urn:synthetic:different');self.assertEqual(r['status'],'unknown');self.assertEqual(r['observationIds'],[])
    def test_appended_copy_isolated(self):
        x=observation(3);l=a.admit(self.l,x,'observation',self.c,W,x['recordedAt']);x['value']['lexical']='mutated';self.assertEqual(l['observations'][-1]['value']['lexical'],'A');self.assertEqual(len(self.l['observations']),2)
    def test_restamped_retry(self):
        x=copy.deepcopy(self.l['observations'][0]);x['recordedAt']=NOW;l=a.admit(self.l,x,'observation',self.c,W,NOW);self.assertEqual(l,self.l)
    def test_snapshot_truncation(self):
        candidate=copy.deepcopy(self.l);candidate['observations'].pop();a.validate_ledger(candidate,self.c)
        with self.assertRaises(a.Invalid):a.validate_extension(self.l,candidate,self.c)
    def test_snapshot_rewrite(self):
        candidate=copy.deepcopy(self.l);candidate['observations'][0]['value']['lexical']='changed'
        with self.assertRaises(a.Invalid):a.validate_extension(self.l,candidate,self.c)
    def test_snapshot_extension(self):
        x=observation(3);l=a.admit(self.l,x,'observation',self.c,W,x['recordedAt']);self.assertTrue(a.validate_extension(self.l,l,self.c))
    def test_rotated_source_writer_can_retract(self):
        x=revision(self.l['authorities'][0]);x['writeGrants'][0]['writers']=['urn:synthetic:new-writer'];l=a.admit(self.l,x,'authority',self.c,G,x['recordedAt'])
        obs=revision(l['observations'][0],at='2026-09-21T10:02:00Z',state='retracted',writer='urn:synthetic:new-writer');l=a.admit(l,obs,'observation',self.c,obs['writer'],obs['recordedAt']);self.assertEqual(query(l,self.c)['status'],'preferred');self.assertEqual(l['observations'][0]['writer'],W)
    def test_closure_cannot_change_accountable(self):
        x=revision(self.l['authorities'][0],change='closure',validUntil='2026-12-01T00:00:00Z',accountable='urn:synthetic:other')
        for part in x['rules']+x['stewardships']+x['writeGrants']:part['validUntil']=x['validUntil']
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'authority',self.c,G,x['recordedAt'])
    def test_no_authority_retains_evidence(self):
        self.l['authorities']=[];r=query(self.l,self.c);self.assertEqual(r['status'],'unknown');self.assertEqual(len(r['observationIds']),2);self.assertEqual(len(r['evidence']),2)
    def test_part_is_not_party(self):
        self.l['authorities'][0]['stewardships'][0]['id']=self.l['authorities'][0]['stewardships'][0]['party']
        with self.assertRaises(a.Invalid):a.validate_ledger(self.l,self.c)
    def test_null_not_unknown(self):
        self.l['observations'][0]['value']=None
        with self.assertRaises(a.Invalid):query(self.l,self.c)
    def test_round_trip(self):self.assertEqual(a.import_snapshot(a.export_ledger(self.l,self.c),self.c),self.l)
    def test_duplicate_json_key(self):
        with self.assertRaises(a.Invalid):a.import_snapshot('{"format":"a","format":"b"}',self.c)
    def test_migration(self):
        self.assertEqual(a.migrate(self.l,'0.1.0'),self.l)
        with self.assertRaises(a.Invalid):a.migrate(self.l,'0.0.1')
    def test_atomic_rejection(self):
        old=copy.deepcopy(self.l);x=observation(3);x['value']['lexical']='\ud800'
        with self.assertRaises(a.Invalid):a.admit(self.l,x,'observation',self.c,W,x['recordedAt'])
        self.assertEqual(self.l,old)
    def test_schema_negatives(self):
        for field,value in [('revision',True),('scope','not uri'),('state','proposed'),('recordedAt','2026-09-31T00:00:00Z'),('validFrom','2026-01-01T00:00:00+02:00')]:
            with self.subTest(field=field):
                x=policy();x[field]=value
                with self.assertRaises(a.Invalid):a.validate_record(x,'authority')
    def test_graph_negatives(self):
        for change in ['digest','anchor','part-party','part-source','part-time','part-id']:
            with self.subTest(change=change):
                x=revision(self.l['authorities'][0]);l=copy.deepcopy(self.l)
                if change=='digest':x['previousDigest']='0'*64
                if change=='anchor':x['predicate']='urn:other'
                if change=='part-party':x['stewardships'][0]['party']='urn:other'
                if change=='part-source':x['rules'][0]['source']='urn:other'
                if change=='part-time':x['rules'][0]['validUntil']='2028-01-01T00:00:00Z'
                if change=='part-id':x['rules'][0]['id']=x['id']
                l['authorities'].append(x)
                with self.assertRaises(a.Invalid):a.validate_ledger(l,self.c)
if __name__=='__main__':
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Tests))
    report={'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'passed':result.wasSuccessful(),'scope':'Reference semantics including authority, temporal history, negative admission and disclosure; not authenticated production service'}
    (P/'test-results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');raise SystemExit(not result.wasSuccessful())

```

## FILE model-spec.md
```
# Enterprise Fact Authority 0.1.0 — semantic contract

This document describes the reference implementation, not every capability proposed by the researchers. Terms are original design proposals unless `research.md` explicitly links an observed source. The closed JSON Schema and companion are normative for this bounded reference. Research assurance is reviewable-draft.

## Structure, responsibility and graph boundary

| Bundle | Layer | Objects / findings | Artifacts and quality | Allowed actions |
|---|---|---|---|---|
| Governance | Scope and accountable term | FactAuthority; definition/value separation | Authority revision and exact scope; no default owner | Scoped governor records/corrects/retracts appointment |
| Governance | Operational appointments | StewardshipAssignment | Stable part identity, evidence, bounded duties and term | Governor changes appointment; steward may receive a route, not acquire powers |
| Source policy | Selection | MastershipRule | Source × priority × valid term; explicit overlap conflict | Governor revises preference; evaluator reads |
| Source policy | Submission | WriteGrant | Source × writers × current term; no priority field | Host authorizes authenticated writer; governor changes grant |
| Observation | Assertions and corrections | FactObservation | Stable source/subject anchor; per-revision writer and digest; retained evidence | Authorized writer asserts/corrects/retracts its source’s record under the current explicit grant |
| Reliance | Historical query and projection | Derived Evaluation; AuthorityRegister | Full input slice and policy digests, separate clocks, full-reader permission | Read; report unknown/contested/preferred; propose follow-up |

Instance references can be cyclic in the external enterprise graph; this module never traverses them. Its revision graph is a linear chain per identified record. There is no inheritance or transitive authority graph. Runtime package imports are separate from semantic crosswalk references and from JSON document composition.

## Types, fields and cardinalities

All schema fields are required; arrays may be empty only where specified. No unknown keys. IDs and references are absolute URIs, at most 500 characters; no automatic canonicalization, alias merging or identity proof. Date/time is UTC `YYYY-MM-DDTHH:MM:SSZ`, real calendar values, half-open `[validFrom, validUntil)` with finite end. Use an explicitly chosen distant finite date if organizational policy needs it; an absent end is not accepted. Null is permitted only for genesis `previousDigest` and for no-value query outcomes. A URI is a reference, not proof its target exists.

**FactAuthority and FactObservation envelope**: `id` 1 stable record identity; `dimension` 1 tenant boundary; `scope` 1 host-governed scope URI; `predicate` 1 governed fact type; `change` 1 of genesis/correction/closure/retraction; `revision` 1 integer ≥1; `previousDigest` 0-or-1 preceding record digest (null at revision 1); `recordedAt` 1 trusted receipt stamp at live admission; `validFrom`, `validUntil` 1 each claimed effective interval; `evidence` 1..n immutable evidence references. Dimension/scope/predicate cannot change within a lineage. Digest is SHA-256 of Python sorted compact UTF-8 JSON, no NaN; **not RFC 8785**. Unicode must encode before admission.

**FactAuthority** adds: `governs` exactly `values`; `definitionAuthorityRef` 1 external record to consult for meaning-owner, not validated here; `issuedBy` 1 publisher matching the authenticated caller at admission; `accountable` 1 party responsible for values and escalation, not automatically a writer; `state` active/retracted; `stewardships` 0..n identified appointments; `rules` 0..n precedence rules; `writeGrants` 0..n submission grants. All are source-backed governance records, not legal adjudications. Changing accountable party normally creates a new effective term as described below; a revision may correct a mistaken appointment under the explicit governor's trust.

**StewardshipAssignment**: `id` 1 distinct from authority/party; `party` 1 external actor; `duties` 1..n of maintain-quality, resolve-conflict, coordinate-transfer; valid bounds 1 each; evidence 1..n. Multiple stewards may be active; routing returns the set of active parties with resolve-conflict duty. These duties do not grant API writes or subdelegation. An absent steward is a visible context gap.

**MastershipRule**: `id` 1; `source` 1 external source identity; `priority` 1 integer 0..1,000,000 (smaller wins); valid bounds 1 each; evidence 1..n. Active source rules must be unambiguous: duplicate active rules for one source result in authority-contested even if priorities agree. Rules neither authenticate sources nor confer rights. They rank observations at the **fact-valid** instant under the knowledge cut.

**WriteGrant**: `id` 1; `source` 1; `writers` 1..n actor URIs; valid bounds 1 each; evidence 1..n. Grants apply at the **current trusted receipt** instant. There must be exactly one active grant for the source and it must name the caller. They do not rank or validate source truth. A source may have a grant but no precedence rule (record is retained, unranked), or a precedence rule but no live write grant (old observations remain rankable; new writes denied).

Identified parts have authority 1 → parts 0..n; each part belongs to exactly one authority throughout its history. Part ID, kind, owning authority, and party/source are immutable. Intervals must be inside the authority term. Changes to duty, priority or authorized writer set are recorded in a new containing authority revision. Part removal is a whole-snapshot correction, not an independent deletion event. The exact part version is `(partId, authorityId, authorityRevision, authorityDigest)`. Independent streams and shared assignments are outside 0.1.0.

**FactObservation** adds: `subject` 1 external canonical subject URI; `source` 1; `writer` 1 submitting actor; `state` asserted/retracted; `value` 1 `{datatype: URI, lexical: string ≤10000}`. Source and subject are immutable within the observation lineage. Writer is recorded per revision; a newly granted writer may correct or retract prior records of that same source, preserving earlier attribution. Value is a tagged lexical atom: `01` and `1` differ, different datatype URIs differ, empty string is a supplied value, null is invalid. Host validates the domain datatype, units, actual subject membership and single-valued predicate contract. No algebra, sets, numeric coercion or confidence inference. A different source must submit a separate competing observation, not revise another source's lineage.

**TrustedConfiguration**: `id`, `dimension`, valid bounds; `governors` 1..n `(actor, scope, predicate)` authorizations; `readers` 1..n full-register actors; `purposes` 1..n admitted purpose strings. Deployment owns and authenticates this input separately; it is not inferred from the ledger. No bearer credentials. A matching governor may publish governance but does not automatically gain observation write/read rights. The Python function checks declarations but cannot authenticate a caller or configuration.

**AuthorityRegister**: format vercy-fact-authority, version 0.1.0, dimension, authorities and observations arrays (0..n, bounded 10,000). Canonical aggregate ID in the native binding is `<dimension>:authority-register`, one per Dimension for this reference. It has a declared boundary (only this profile's records), separate mastership per record family, governed revision rules and all-or-nothing disclosure. It does not replace a company instance. No global database is implied.

## Lifecycle, time and evaluation

1. Governor admits authority genesis/revision under current scoped configuration. Writer admits observation genesis/revision under exactly one active current authority and a separate WriteGrant. Issuer/writer must match the authenticated actor supplied by host. Two policy records can conflict; admitting one does not silently overwrite another.
2. Every new receipt equals trusted `now` and strictly follows **all** previous receipt timestamps. This serial reference supports one receipt per second, not high-throughput concurrent ingestion. Identical payload `(id,revision)` replay is a no-op after current authorization, ignoring only a host-restamped recordedAt and retaining the original receipt. Changed payload rejects. Failures leave the input untouched. Future/backdated receipt injection is rejected; past effective dates are allowed.
3. A revision replaces the **entire claimed interval** as currently known; it does not patch a subinterval. It must cite its immediate predecessor digest. Genesis requires change=genesis and a live state; retraction requires both change=retraction and state=retracted. Closure requires change=closure, a strictly reduced end, the original start/party/value, and clipped part ends; only revision/receipt/issuer-or-writer/evidence metadata may additionally change. A correction may intentionally amend an erroneous entire term and is distinct from closure. For a transfer, close the old term by a guarded closure revision preserving its start and old party, then create a new authority/assignment ID from the cutoff. A future-dated replacement alone would remove old valid-time coverage; use split terms instead. Temporary gaps are fail-closed. Durable multi-record atomic transfer is deferred.
4. Query filters by `recordedAt <= knownAt`, takes the latest revision per ID, then effective interval and active/asserted state. These operations happen in that order. `knownAt > now` rejects. Past knowledge does not see a policy correction received today. `recordedAt` is receipt, not source event time or authenticated publication proof; other clocks are deliberately not manufactured.
5. Match exact dimension/scope/predicate. Zero authorities → unknown; multiple active authority IDs → authority-contested. Duplicate active rules for a source → authority-contested. No inherited scope, arbitrary scope expression, jurisdiction precedence or implicit most-specific rule. The trusted host binds subject/scope; supplying an arbitrary complete forged register can bypass this reference because authentication is outside it.
6. Retain all active matching observations and evidence, including unranked and lower-priority ones. Among sources with a live rule choose the minimum priority. If their tagged lexical values disagree, return contested and no value. Otherwise return preferred with that value and all supporting IDs. Multiple competing records from **one** source can also contest. Source identity count is not a vote.
7. Outcomes carry profile version, authority/rule/route pins and observation revision digests, exact matched authority revision digests, known input-slice digest including register header and configuration digest. This is reproducibility metadata, not signed publication. `observationIds`, `evidence`, unranked IDs and preferred IDs expose only the matching temporal slice. Input digest covers the full known register as an integrity pin, not a summary of only this query. No side-effect notification occurs. Historical route is labeled by fact-valid time and must not be used as current contact authority.
8. Read permission is checked before ledger validation. An unauthorized actor or purpose receives only `Read denied`; no selective assertion filtering is implemented. Authorized readers are cleared for the entire register. Configuration is checked at current time even for historical queries. This does not recreate past authenticated access decisions or verify every old append was authorized. `validate_ledger`/`import_snapshot` validate structure and history consistency only.

## Executable invariants and question routes

I01 Equal priority disagreement is contested; I02 import order never ranks; I03 owner/steward/model maintainer are not implicit writers; I04 no authority is unknown, never a grant; I05 duplicate policies/rules fail to select; I06 source preference and current WriteGrant are independent; I07 immutable scope/source/subject anchors and identified parts; I08 receipt order and predecessor digests; I09 previous knowledge cuts survive corrections; I10 interval containment and exclusive upper bounds; I11 no partial access filter; I12 no implicit value coercion; I13 transfer keeps old effective terms; I14 atomic in-memory rejection and payload-idempotent replay; I15 future knowledge/receipt rejection; I16 loss-bearing migration refused. `test_authority.py` implements representative positive/negative cases; it does not prove all possible states or domain truth.

| Route | Finding → question | Artifact | Permitted action / unknown behavior |
|---|---|---|---|
| Q01 | FA-boundary → Is this a meaning, value assertion or ownership record? | boundary-decision + governs | Explain; do not infer title or definition ownership |
| Q02 | FA-identity → What survives rename/transfer? | record IDs, anchors, revision chain | Follow exact lineage; transfer by new term, never merge parties |
| Q03 | FA-meaning → Who defines this predicate? | definitionAuthorityRef | Resolve externally; insufficient context if absent/unverified |
| Q04 | FA-accountable → Who answers for values at T? | authority slice | Read accountable; zero/multiple returns unknown/contested |
| Q05 | FA-steward → Who handles the disagreement? | active assignment IDs and duties | Propose routing; missing route needs appointment, no approval |
| Q06 | FA-write → May this actor submit for source S now? | separate WriteGrant + trust config | Call admit through host; absent/ambiguous rejects |
| Q07 | FA-rank → Which source is preferred at fact time? | MastershipRule + policy pin | Evaluate; priority is not truth or permission |
| Q08 | FA-conflict → What if equal sources disagree? | both observation IDs/evidence | Preserve contested; request human review, never overwrite |
| Q09 | FA-overlap → Which of two authorities applies? | authority-contested outcome | Governor investigates; no recency fallback |
| Q10 | FA-history → What was known at T about valid time V? | known input slice + authority pins | Re-evaluate; future knowledge rejected |
| Q11 | FA-correction → How is a wrong claim corrected? | next observation revision | Currently granted same-source writer submits with evidence; retain prior rows |
| Q12 | FA-transfer → What happens at responsible-party change? | closed old term + new term | Governor records both; gap stays unknown |
| Q13 | FA-disclosure → What can this reader see? | trusted full-register read policy | All or deny; do not drop a hidden contradiction |
| Q14 | FA-minimum → Does a startup need HRIS? | one-source minimal register | Use governed manual source with explicit rights |
| Q15 | FA-context → What if source/policy is missing? | reason and unranked IDs | Ask for missing authority/rule; do not invent source truth |
| Q16 | FA-binding → Does native validation prove semantics? | native + companion reports | Invoke both; nested V3 acceptance alone insufficient |
| Q17 | FA-migration → Can earlier owner strings be imported? | migration.md | Stage candidates outside operative register; explicit mapping required |
| Q18 | FA-evidence → Does provenance prove the value? | evidence references | Inspect externally; no inferred veracity or access grant |

Every route is informational or explicitly guarded; no agent is authorized to act merely because a table lists an action.

## Host integration requirements after audit

`admit` and its diagnostics are internal trusted-host APIs. A caller with write rights but no read rights must never receive the returned complete ledger, replay/conflict details, or configuration diagnostics. The host returns only a receipt for that submission or a generic Admission rejected; catch Denied separately from Invalid. Deploying raw functions as public endpoints would violate this contract. Root governance may explicitly grant its actors source-write rights; there is no separation-of-duties rule beyond no implicit grants.

`validate_extension(previous, candidate, config)` requires identical headers, exact historical prefixes in both collections and all appended receipts after the prior global head. Use it with a trusted previous full snapshot, and admit every new row. It does not prove the previous snapshot itself is complete. Native acceptance demonstrates both and records supersedes/previousSnapshotDigest on snapshot-r2. Overlapping write grants remain representable conflicts in archives, but actual submission fails closed; snapshot validation does not deny their existence. Observation intervals may extend beyond a governance term; selection outside known authority is unknown with retained observation pins.

Native identity is `vr.profile.enterprise-fact-authority@0.1.0` and its own JSON-compatible `spec.json` digest. WM-XCT-001 is installed only as semantic-only with binding=null; it is an optional exact semantic reference. Snapshot authority names the deployment register operator, not a steward or accountable party. Native storage authority is not domain precedence. Bare SHA-256 record pins and native sha256:-prefixed asset descriptors are explicitly distinct encodings.

```

## FILE README.md
```
# Enterprise Fact Authority · 0.1.0

An English reference contract for accountable parties, identified stewardship appointments, source precedence, separate write grants, and retained competing observations. It is a **reviewable draft** and a bounded increment of EM-XCT-02.

This package is discoverable alongside WM-XCT-001. That location is **not an `is-a` claim**: a predicate is not a controllable object, and these records are not conforming WM-XCT-001 control records. The unchanged parent specification remains the semantic reference for selected appointment, time and contestation patterns. See `boundary-decision.md` and `crosswalk.json`.

## Use the reference

Python 3.10+ and `pip install -r requirements.txt` are required. In a trusted environment:

```python
import authority as a
c = a.load('examples/startup.config.json')  # deployment-owned, trusted configuration
l = a.load('examples/startup.json')         # trusted synthetic historical archive
a.validate_ledger(l, c)
answer = a.evaluate(l, c, actor='urn:synthetic:reader', purpose='governance-review',
    scope='urn:synthetic:scope', predicate='urn:synthetic:predicate',
    subject='urn:synthetic:subject', validAt='2026-09-21T12:00:00Z',
    knownAt='2026-09-21T12:00:00Z', now='2026-09-21T12:00:00Z')
assert answer['status'] == 'contested'
assert answer['value'] is None
```

The examples use fixed synthetic time. An integrating service must supply its trusted receipt time and authenticated actor; users must not choose these or replace the configuration/ledger. `admit` performs an in-memory, atomic append into a **new** ledger. Persist it with concurrency control in a production adapter. Never expose `import_snapshot` as a write API: it validates trusted archives and does not authenticate their history. Native V3 validates only the outer snapshot envelope; invoke this companion explicitly before use and live admission. Validate each new full snapshot with validate_extension against the trusted prior snapshot. The native tool alone can store semantically invalid nested data.

Run `python test_authority.py`. To test new synthetic Dimensions, use `python acceptance.py --composer <trusted-WM-XCT-040-directory> --skill <trusted-vercy-skill-directory> --report acceptance-results.json`. Tool pins bind the expected local bytes; they do not sandbox Python imports or authenticate downloaded software.

## What is implemented

- Exact Dimension × scope × predicate governance, one-valued facts, explicit bounded UTC intervals and two temporal query axes.
- A value-accountable party distinct from a referenced definition-authority record, steward, publisher and writer.
- Source precedence separate from write grants; smaller priority numbers have higher precedence. Equal highest priority plus different tagged lexical values returns `contested` with both evidence references.
- Immutable revisions, previous-content digests, historical corrections, payload-idempotent replay preserving original receipt and receipt checks. A transfer uses distinct terms and preserves historical rows.
- All-or-nothing read projection for full-register readers; no partial visibility that hides a conflicting observation. Historical `routeTo` is informational at `routeValidAt`; resolve current routing before sending anything.
- Three small fixtures: startup (equal-priority disagreement), group (higher-precedence source beats later import), AI/software team (agreement with an explicit stewardship gap). They demonstrate patterns, not a full multinational competence graph or real company data.

## Deliberate limits

No authenticated publication, signatures, durable ledger, source connector, subject-to-scope verification, policy federation, recursive delegation, definition ownership resolution, adjudication workflow, confidence scoring, staleness detection, multi-valued predicates, units conversion, legal validity, production access enforcement or existing-Dimension migration. The trusted host determines correct scope and predicate cardinality. Malformed/missing authority never grants permission. A selected value is named `preferred`; it can still be false. Inputs may be incomplete; this library cannot prove it has all relevant observations or authorities.

Assignments and rules have their own stable IDs and intervals, but their versions are captured in an authority revision. Independent concurrent updates and reuse of one assignment across authorities are deferred. Missing steward yields an empty route; it never approves a disputed value. Full parent research and its historical source holds remain open.

## Native identity and host boundary

The companion has its own runtime ID `vr.profile.enterprise-fact-authority`, specification (`spec.json`) and object namespace. WM-XCT-001 is a separately pinned **semantic-only** reference. Snapshot storage belongs to the register operator, never an implicit steward grant. A part citation needs its containing authority revision/digest.

The host must keep the complete ledger and raw admit/validation diagnostics internal. A non-reader receives only a submission receipt or a generic rejection, not the full return value. Functions here are not a public API. Receipt retries preserve the originally stored recordedAt; a restamp alone is ignored. Source writer rotation can correct/retract earlier same-source observations under the current explicit grant. Structural snapshot truncation is checked against a trusted prior snapshot; forged or incomplete roots remain outside the trust boundary.

```

## FILE composition.yaml
```
{
  "profile": "enterprise-fact-authority",
  "version": "0.1.0",
  "runtimeImports": [],
  "semanticReferences": [
    {
      "id": "WM-XCT-001",
      "version": "0.3.0-research.1",
      "relation": "discovery-association-and-selected-patterns",
      "specSha256": "a09261ca365d2e82716705a27d5e46cca7faef8fc22d90fcf3b94a53ef729358"
    },
    {
      "id": "WM-XCT-002",
      "version": "0.3.0-research.1",
      "relation": "read-contract-patterns-only-not-write-grant",
      "specSha256": "9085d977567f3e1fc0b9bb27c6a7c517139f5972a1b95bf4a2bedccdb10bf2db"
    },
    {
      "id": "WM-XCT-012",
      "version": "0.3.0-research.1",
      "relation": "assertion-pattern-alignment",
      "specSha256": "aa6155354c55a87ab837ec9bd47f796ca582309fe383f1afffb802dafff7ecb5"
    }
  ],
  "nativeBinding": "Own vr.profile.enterprise-fact-authority@0.1.0 spec/namespace; WM-XCT-001 semantic-only optional reference",
  "instanceReferences": [
    "party",
    "source",
    "predicate",
    "scope",
    "definitionAuthorityRef",
    "evidence"
  ],
  "packageComposition": "Schema, code, docs, fixtures, tests; identified part versions embedded in authority revisions"
}

```

## FILE runtime-model.reference.json
```
{
  "format": "vercy-runtime-model-schema",
  "schemaVersion": "1.0.0",
  "modelId": "vr.profile.enterprise-fact-authority",
  "paths": {
    "authority.register.snapshot": {
      "valueTypes": [
        "object"
      ],
      "units": [
        null
      ]
    }
  }
}

```

## FILE AGENTS.md
```
# Agent use

Read README, boundary-decision and model-spec, then the pinned schema and companion. Inspect the Dimension's trusted configuration and runtime binding before proposing any changes. The model author, installation actor, accountable party, steward and source writer are separate roles; none implies the others.

An unknown, unranked, contested or authority-contested result is a result to preserve. Ask for the missing predicate scope, governance appointment, rule or source evidence. Never choose a winner from arrival order, majority source count, model maintainer identity or a confidence score. Never promote a proposal or inferred owner into an operative record.

Query through a host that authenticates actors, controls the full register, fixes the subject-to-scope mapping and invokes the companion. Do not let an API client supply a policy, receipt clock or reduced assertion list. A historical route is not current permission to notify a person. This library sends nothing and makes no organization decisions.

For native V3, a syntactically valid outer snapshot is insufficient. Check the installed code/schema digests, explicitly validate the stored nested register, and call admit for new live changes. A report that only says “JSON Schema passed” does not establish authority, authorization, truth or publication authenticity.

Treat admit as a host-internal operation. Never return its complete ledger or raw diagnostics to a write-only caller; return a receipt or generic rejection. Catch Denied distinctly from Invalid. Verify new full snapshots extend the trusted prior one. Native facts use the companion runtime identity, with a separate register operator on the envelope and semantic-only WM-XCT-001 reference.

```

## FILE research.md
```
# EM-XCT-02 research and reconciliation

Two independent studies received the same frozen English boundary on 2026-09-21: Claude through its actual CLI with web research enabled, Grok through the owner's browser in Heavy mode. Original answers and hash manifests are separate files. Claude reports `claude-opus-5`; Grok's backend version is not exposed and is not inferred. Codex's normalized contract is separate from both answers. All examples are synthetic.

The direct comparison parsed full published specifications of WM-XCT-001, WM-XCT-002 and WM-XCT-012, recursively inventoried their findings/data elements, compared spec/AGENTS/publication bytes to production and retained holds. This is not a fresh verification of every historical source or every proposed field. The archived semantic basis is 0.3.0-research.1 for each. No independent native instance validators/examples for this exact enterprise contract existed in those legacy semantic packages; new companion examples and tests are therefore explicit additions.

## Evidence and alternatives

`source-verification.json` records nine primary/public author sources, section/version, inspection limits, claim, chosen consequence, URL and download digest where available. A successful fetch is not conformance. All schema and code here are original; external standards/products are paraphrased and linked, with no copied schemas or source documents.

Three approaches informed the result:

1. **Standards:** PROV separates provenance agency from the target; ODRL makes policy conflict strategy explicit; NIST's ABAC abstract distinguishes authorization inputs. We use these as patterns, not a standard mapping. Detailed NIST clauses and unread ISO texts remain unverified here. [PROV-O](https://www.w3.org/TR/2013/REC-prov-o-20130430/), [ODRL §2.10](https://www.w3.org/TR/2018/REC-odrl-model-20180215/#conflict), [NIST](https://csrc.nist.gov/pubs/sp/800/162/upd2/final).
2. **Operational practice:** Kubernetes field management detects conflicts but also supports force/update behavior; that is not enterprise truth. DataHub separates custom ownership types from the privilege to edit owners. Catalog ownership in OpenMetadata is a product convention, not universal fact authority. We separate assignment, precedence and write grant. [Kubernetes](https://kubernetes.io/docs/reference/using-api/server-side-apply/), [DataHub](https://docs.datahub.com/docs/ownership/ownership-types), [OpenMetadata](https://docs.open-metadata.org/v2.0.x/how-to-guides/guide-for-data-users/data-ownership).
3. **Alternative school:** domain ownership in data mesh motivates scoped governance; XTDB distinguishes valid/system time; Wikidata distinguishes statement ranks from references. Our exact-scope, retained-assertion algorithm is an original proposal, not an implementation of these systems or a CRDT. [Data mesh](https://martinfowler.com/articles/data-mesh-principles.html), [XTDB](https://docs.xtdb.com/concepts/key-concepts.html), [Wikidata](https://www.wikidata.org/wiki/Help:Ranking).

## Disagreements and decisions

| Issue | Claude | Grok | Codex disposition |
|---|---|---|---|
| Attach point | Profile of WM-XCT-001 | Reject subtype: predicate is abstraction, not controllable object | Discovery association only; independent companion contract. Original parent's semantics unchanged. Direct inspection confirms Grok's quoted boundary |
| Number of parent bundles | Fetch summarizer returned four; flagged discrepancy | Six in boundary | Full parsed source has six; discrepancy is summarization, not a source change |
| Definition versus values | Must separate governs=definition/values | Broad FactAuthority wording also includes meaning | 0.1.0 explicitly governs values; definition authority is unresolved external reference |
| Source rank and write rights | Separate precedence/admission/change right; 002 excludes writes | Distinct rank vs write permission | Separate MastershipRule and original WriteGrant; no 002 conformance claimed |
| Assignment identity | Independent identified records | Reject unidentifiable aggregate fields | Stable identified parts and immutable party/source anchor, versioned by containing authority revision. Independent streams and cross-authority portability deferred |
| Overlap | Suggested specificity algorithm | Refuse invented lattice | Exact scope only; overlapping operative records fail to select |
| Temporal proof | Bitemporal history is not authenticated publication | Separate authenticated policy clock/pin | Trusted receipt admission + pins; no signature/publication authenticity claim. Other clocks not invented |
| Disclosure | Predicate-level redacted contest projection proposed | Preserve conflict but restrict payload | Minimum all-or-deny full-register read; no partial projection, no count leakage to denied reader |
| Future knowledge | Suggested clamp | Explicit policy clock | Reject future knownAt; no silent alteration of question |
| Broad first increment | Many additional types | Narrow startup contract | Bounded original reference plus three small pattern fixtures; comprehensive group/AI governance deferred |

The executable contract selects a **preferred observation under policy**, never an objectively true fact. It is useful for building a Company Dimension's governance register today, but remains partial with respect to the broader registry contour. Source/subject authentication, real connectors, definition governance, independent assignment streams, federated competencies, durable transactions, full history/erasure policy and human adjudication are next research targets. Parent legal/source holds are inherited as limitations, not silently closed by this study.

```

## FILE crosswalk.json
```
{
  "contour": "EM-XCT-02",
  "v1Candidate": "XCT-02",
  "candidateMap": {
    "accountable_ref": "FactAuthority.accountable; values only",
    "steward_ref": "StewardshipAssignment.party; qualified by assignment ID/term",
    "master_system_ref": "MastershipRule.source; priority distinct from WriteGrant",
    "authority_scope": "exact dimension/scope/predicate URIs; no free-text evaluation"
  },
  "models": [
    {
      "modelId": "WM-XCT-001",
      "version": "0.3.0-research.1",
      "registryId": "vr.wm-xct-001",
      "files": [
        {
          "name": "spec.yaml",
          "sha256": "a09261ca365d2e82716705a27d5e46cca7faef8fc22d90fcf3b94a53ef729358",
          "bytes": 301760,
          "publicMatchesLocal": true
        },
        {
          "name": "AGENTS.md",
          "sha256": "0f9aba04a9b4f58f152cdca0ea3f1da73143cd6867c4e393770a0c7b69c0249b",
          "bytes": 952,
          "publicMatchesLocal": true
        },
        {
          "name": "publication.json",
          "sha256": "605d2d20a9db70c34c5e215de07912166c3dcccb51bd8b11211cc84382c7cf2c",
          "bytes": 2929,
          "publicMatchesLocal": true
        }
      ],
      "researchAssurance": "reviewable-draft",
      "holds": [
        "Source and live-version verification is not complete and must be retained as a hold: Grok's CRPD citation resolves to a generic OHCHR instruments page rather than Article 12, its LADM support is a FIG co-editor paper rather than the ISO text, Claude's UCC Article 12 citation is a Uniform Law Commission community page rather than the act text, and Claude's DID v1.1 is a Candidate Recommendation snapshot whose alignment is provisional.",
        "Multi-profile domain validation has not been performed by either provider. Before publication the mixin must be exercised against at least a land-parcel profile, an electronic-transferable-record profile, a corporate-vehicle/beneficial-ownership profile and a personal-data profile, since its defaults are calibrated to EU law and would misfire in open-register jurisdictions.",
        "Normative clause text of ISO 19152-1:2024, ISO/IEC 27002:2022 and ISO 19115-1 was never read directly by either provider. Every attribute-level alignment claim to LADM, control 5.9 and CI_RoleCode must be labelled unverified in the draft, and no conformance claim may be made.",
        "The imported HCCH trust material (Articles 2, 3, 8, 11, 13, 15) and FATF Recommendation 24/25 material were read at page and guidance level. Clause-level confirmation against the primary instruments is required before these claims are cited in the merged draft.",
        "The two additions that touch legal effect \u2014 governing-law-and-situs and involuntary-deprivation-and-lapse-events \u2014 must be re-read against the base out_of_scope line stating that this model records a claimed basis and its evidence rather than its legal validity, to confirm the merged text does not slide into asserting recognition or adjudicating deprivation.",
        "Merged source de-duplication is unverified: VGGT and CRPD Article 12 appear in both packs under different IDs and URLs, and MLETR appears as a landing page in one and a PDF in the other. The synthesizer's source merge must be reviewed before the draft is published."
      ],
      "relationship": "overlap/pattern alignment; not exactMatch or subtype",
      "action": "reference semantic basis; isolated companion contract",
      "losses": "Full legacy control/read-contract/provenance semantics not implemented; no automatic legacy instance migration",
      "observedRuntime": {
        "version": "0.3.0-research.1",
        "status": "published",
        "installable": true,
        "digest": "sha256:a09261ca365d2e82716705a27d5e46cca7faef8fc22d90fcf3b94a53ef729358",
        "requires": []
      }
    },
    {
      "modelId": "WM-XCT-002",
      "version": "0.3.0-research.1",
      "registryId": "vr.wm-xct-002",
      "files": [
        {
          "name": "spec.yaml",
          "sha256": "9085d977567f3e1fc0b9bb27c6a7c517139f5972a1b95bf4a2bedccdb10bf2db",
          "bytes": 260231,
          "publicMatchesLocal": true
        },
        {
          "name": "AGENTS.md",
          "sha256": "2bc544b6e87d6512ffd7e4b0fd9a239d8d1ac52d99ab96ca53d16673d566326f",
          "bytes": 960,
          "publicMatchesLocal": true
        },
        {
          "name": "publication.json",
          "sha256": "101e759a6ffe71d0123ecb276ead428c6ec19b21c337b351ddcc2c058ed3f938",
          "bytes": 2579,
          "publicMatchesLocal": true
        }
      ],
      "researchAssurance": "reviewable-draft",
      "holds": [
        "Source liveness and version pinning is unverified for all nineteen accepted sources. Two specific reconciliations are mandatory before publication: pin FHIR Consent to the version-qualified R5 URL rather than the unversioned current URL that will drift, and reconcile the two DPVCG 27560-guide citations that disagree on both host and date (w3c-cg.github.io retrieved 2026-08-23 versus w3id.org Final Community Group Report 15 February 2026).",
        "Domain-profile validation is incomplete. The model has been exercised only against EU/GDPR, the US health sector under 45 CFR 164.508, and a healthcare FHIR profile. At least one non-health, non-EU jurisdiction profile must be run end to end before publication to test whether the instrument-form and flavour parameters actually generalise.",
        "Normative text for ISO/IEC TS 27560:2023 and ISO/IEC 29184:2020 is paywalled; field inventories rest on catalogue pages plus the DPVCG mapping rather than annex text. TS 27560 is a Technical Specification, not an International Standard, and a revision (CD 27560.2) may change mandatory fields. Any field-level claim must be labelled as mapping-derived.",
        "The security dimension is self-declared a gap by the base (key management, token binding, replay resistance, cryptographic proof suites). Now that entitlement cutoff is imported, publication must name the sibling security model that owns these and state plainly that this model does not close them.",
        "Collective, community and Indigenous group permission is unsupported by any source in either pack and must be published as an explicitly unmodelled gap, never approximated through the delegate capacity."
      ],
      "relationship": "overlap/pattern alignment; not exactMatch or subtype",
      "action": "reference semantic basis; isolated companion contract",
      "losses": "Full legacy control/read-contract/provenance semantics not implemented; no automatic legacy instance migration",
      "observedRuntime": {
        "version": "0.3.0-research.1",
        "status": "published",
        "installable": true,
        "digest": "sha256:9085d977567f3e1fc0b9bb27c6a7c517139f5972a1b95bf4a2bedccdb10bf2db",
        "requires": []
      }
    },
    {
      "modelId": "WM-XCT-012",
      "version": "0.3.0-research.1",
      "registryId": "vr.wm-xct-012",
      "files": [
        {
          "name": "spec.yaml",
          "sha256": "aa6155354c55a87ab837ec9bd47f796ca582309fe383f1afffb802dafff7ecb5",
          "bytes": 271531,
          "publicMatchesLocal": true
        },
        {
          "name": "AGENTS.md",
          "sha256": "a036444b2ea477073a32e1c8aa10ec14b4b35f953c98af029e29ea40e65fa9bb",
          "bytes": 904,
          "publicMatchesLocal": true
        },
        {
          "name": "publication.json",
          "sha256": "a050d44bcdf079f5f02ae682c60722d2c3065bdf49581afbf988f3612451ca87",
          "bytes": 1181,
          "publicMatchesLocal": true
        }
      ],
      "researchAssurance": "reviewable-draft",
      "holds": [
        "Verify live availability, version pins and exact claim support for every source accepted into the synthesis.",
        "Create and test sector profiles for archival records, geospatial data, clinical records, software supply chains and media authenticity before promoting a universal completeness claim."
      ],
      "relationship": "overlap/pattern alignment; not exactMatch or subtype",
      "action": "reference semantic basis; isolated companion contract",
      "losses": "Full legacy control/read-contract/provenance semantics not implemented; no automatic legacy instance migration",
      "observedRuntime": {
        "version": "0.3.0-research.1",
        "status": "published",
        "installable": true,
        "digest": "sha256:aa6155354c55a87ab837ec9bd47f796ca582309fe383f1afffb802dafff7ecb5",
        "requires": []
      }
    }
  ],
  "sanitizedPredecessorReview": [
    {
      "input": "Owner-supplied AI analysis A",
      "candidate": "S1 Ownership",
      "relation": "Legacy ownership pointer; not exact fact-authority semantics",
      "current": "WM-XCT-001 0.3.0-research.1 patterns only",
      "decision": "Do not import its combined owner-steward label or suggested source systems as verified grants; entity shareholding remains a different domain"
    },
    {
      "input": "Owner-supplied AI analysis B",
      "candidate": "MastershipRule; DataOwner; DataSteward; DataCustodian",
      "relation": "Requirements vocabulary, not executable specification",
      "current": "This bounded companion plus external role/party definitions",
      "decision": "Split source preference, assignment identity, write grant and definition governance. Candidate source systems remain unverified; no private organization bindings published."
    }
  ]
}

```

## FILE examples/startup.json
```
{
  "format": "vercy-fact-authority",
  "version": "0.1.0",
  "dimension": "urn:synthetic:dimension",
  "authorities": [
    {
      "id": "urn:synthetic:authority",
      "dimension": "urn:synthetic:dimension",
      "scope": "urn:synthetic:scope",
      "predicate": "urn:synthetic:predicate",
      "governs": "values",
      "definitionAuthorityRef": "urn:synthetic:definition-owner-record",
      "change": "genesis",
      "revision": 1,
      "previousDigest": null,
      "recordedAt": "2026-09-21T10:00:00Z",
      "validFrom": "2026-01-01T00:00:00Z",
      "validUntil": "2027-01-01T00:00:00Z",
      "evidence": [
        "urn:synthetic:appointment"
      ],
      "issuedBy": "urn:synthetic:governor",
      "accountable": "urn:synthetic:owner",
      "state": "active",
      "stewardships": [
        {
          "id": "urn:synthetic:stewardship",
          "party": "urn:synthetic:steward",
          "duties": [
            "resolve-conflict"
          ],
          "validFrom": "2026-01-01T00:00:00Z",
          "validUntil": "2027-01-01T00:00:00Z",
          "evidence": [
            "urn:synthetic:mandate"
          ]
        }
      ],
      "rules": [
        {
          "id": "urn:synthetic:rule:a",
          "source": "urn:synthetic:source:a",
          "priority": 0,
          "validFrom": "2026-01-01T00:00:00Z",
          "validUntil": "2027-01-01T00:00:00Z",
          "evidence": [
            "urn:synthetic:rule-evidence"
          ]
        },
        {
          "id": "urn:synthetic:rule:b",
          "source": "urn:synthetic:source:b",
          "priority": 0,
          "validFrom": "2026-01-01T00:00:00Z",
          "validUntil": "2027-01-01T00:00:00Z",
          "evidence": [
            "urn:synthetic:rule-evidence"
          ]
        }
      ],
      "writeGrants": [
        {
          "id": "urn:synthetic:write:a",
          "source": "urn:synthetic:source:a",
          "writers": [
            "urn:synthetic:writer"
          ],
          "validFrom": "2026-01-01T00:00:00Z",
          "validUntil": "2027-01-01T00:00:00Z",
          "evidence": [
            "urn:synthetic:write-evidence"
          ]
        },
        {
          "id": "urn:synthetic:write:b",
          "source": "urn:synthetic:source:b",
          "writers": [
            "urn:synthetic:writer"
          ],
          "validFrom": "2026-01-01T00:00:00Z",
          "validUntil": "2027-01-01T00:00:00Z",
          "evidence": [
            "urn:synthetic:write-evidence"
          ]
        }
      ]
    }
  ],
  "observations": [
    {
      "id": "urn:synthetic:observation:1",
      "dimension": "urn:synthetic:dimension",
      "scope": "urn:synthetic:scope",
      "predicate": "urn:synthetic:predicate",
      "change": "genesis",
      "revision": 1,
      "previousDigest": null,
      "recordedAt": "2026-09-21T10:00:01Z",
      "validFrom": "2026-01-01T00:00:00Z",
      "validUntil": "2027-01-01T00:00:00Z",
      "evidence": [
        "urn:synthetic:evidence:1"
      ],
      "subject": "urn:synthetic:subject",
      "source": "urn:synthetic:source:a",
      "writer": "urn:synthetic:writer",
      "state": "asserted",
      "value": {
        "datatype": "urn:synthetic:string",
        "lexical": "A"
      }
    },
    {
      "id": "urn:synthetic:observation:2",
      "dimension": "urn:synthetic:dimension",
      "scope": "urn:synthetic:scope",
      "predicate": "urn:synthetic:predicate",
      "change": "genesis",
      "revision": 1,
      "previousDigest": null,
      "recordedAt": "2026-09-21T10:00:02Z",
      "validFrom": "2026-01-01T00:00:00Z",
      "validUntil": "2027-01-01T00:00:00Z",
      "evidence": [
        "urn:synthetic:evidence:2"
      ],
      "subject": "urn:synthetic:subject",
      "source": "urn:synthetic:source:b",
      "writer": "urn:synthetic:writer",
      "state": "asserted",
      "value": {
        "datatype": "urn:synthetic:string",
        "lexical": "B"
      }
    }
  ]
}

```

## FILE examples/group.json
```
{
  "format": "vercy-fact-authority",
  "version": "0.1.0",
  "dimension": "urn:synthetic:dimension",
  "authorities": [
    {
      "id": "urn:synthetic:authority",
      "dimension": "urn:synthetic:dimension",
      "scope": "urn:synthetic:scope",
      "predicate": "urn:synthetic:predicate",
      "governs": "values",
      "definitionAuthorityRef": "urn:synthetic:definition-owner-record",
      "change": "genesis",
      "revision": 1,
      "previousDigest": null,
      "recordedAt": "2026-09-21T10:00:00Z",
      "validFrom": "2026-01-01T00:00:00Z",
      "validUntil": "2027-01-01T00:00:00Z",
      "evidence": [
        "urn:synthetic:appointment"
      ],
      "issuedBy": "urn:synthetic:governor",
      "accountable": "urn:synthetic:owner",
      "state": "active",
      "stewardships": [
        {
          "id": "urn:synthetic:stewardship",
          "party": "urn:synthetic:steward",
          "duties": [
            "resolve-conflict"
          ],
          "validFrom": "2026-01-01T00:00:00Z",
          "validUntil": "2027-01-01T00:00:00Z",
          "evidence": [
            "urn:synthetic:mandate"
          ]
        }
      ],
      "rules": [
        {
          "id": "urn:synthetic:rule:a",
          "source": "urn:synthetic:source:a",
          "priority": 0,
          "validFrom": "2026-01-01T00:00:00Z",
          "validUntil": "2027-01-01T00:00:00Z",
          "evidence": [
            "urn:synthetic:rule-evidence"
          ]
        },
        {
          "id": "urn:synthetic:rule:b",
          "source": "urn:synthetic:source:b",
          "priority": 10,
          "validFrom": "2026-01-01T00:00:00Z",
          "validUntil": "2027-01-01T00:00:00Z",
          "evidence": [
            "urn:synthetic:rule-evidence"
          ]
        }
      ],
      "writeGrants": [
        {
          "id": "urn:synthetic:write:a",
          "source": "urn:synthetic:source:a",
          "writers": [
            "urn:synthetic:writer"
          ],
          "validFrom": "2026-01-01T00:00:00Z",
          "validUntil": "2027-01-01T00:00:00Z",
          "evidence": [
            "urn:synthetic:write-evidence"
          ]
        },
        {
          "id": "urn:synthetic:write:b",
          "source": "urn:synthetic:source:b",
          "writers": [
            "urn:synthetic:writer"
          ],
          "validFrom": "2026-01-01T00:00:00Z",
          "validUntil": "2027-01-01T00:00:00Z",
          "evidence": [
            "urn:synthetic:write-evidence"
          ]
        }
      ]
    }
  ],
  "observations": [
    {
      "id": "urn:synthetic:observation:1",
      "dimension": "urn:synthetic:dimension",
      "scope": "urn:synthetic:scope",
      "predicate": "urn:synthetic:predicate",
      "change": "genesis",
      "revision": 1,
      "previousDigest": null,
      "recordedAt": "2026-09-21T10:00:01Z",
      "validFrom": "2026-01-01T00:00:00Z",
      "validUntil": "2027-01-01T00:00:00Z",
      "evidence": [
        "urn:synthetic:evidence:1"
      ],
      "subject": "urn:synthetic:subject",
      "source": "urn:synthetic:source:a",
      "writer": "urn:synthetic:writer",
      "state": "asserted",
      "value": {
        "datatype": "urn:synthetic:string",
        "lexical": "A"
      }
    },
    {
      "id": "urn:synthetic:observation:2",
      "dimension": "urn:synthetic:dimension",
      "scope": "urn:synthetic:scope",
      "predicate": "urn:synthetic:predicate",
      "change": "genesis",
      "revision": 1,
      "previousDigest": null,
      "recordedAt": "2026-09-21T10:00:02Z",
      "validFrom": "2026-01-01T00:00:00Z",
      "validUntil": "2027-01-01T00:00:00Z",
      "evidence": [
        "urn:synthetic:evidence:2"
      ],
      "subject": "urn:synthetic:subject",
      "source": "urn:synthetic:source:b",
      "writer": "urn:synthetic:writer",
      "state": "asserted",
      "value": {
        "datatype": "urn:synthetic:string",
        "lexical": "B"
      }
    }
  ]
}

```

## FILE examples/ai-team.json
```
{
  "format": "vercy-fact-authority",
  "version": "0.1.0",
  "dimension": "urn:synthetic:dimension",
  "authorities": [
    {
      "id": "urn:synthetic:authority",
      "dimension": "urn:synthetic:dimension",
      "scope": "urn:synthetic:scope",
      "predicate": "urn:synthetic:predicate",
      "governs": "values",
      "definitionAuthorityRef": "urn:synthetic:definition-owner-record",
      "change": "genesis",
      "revision": 1,
      "previousDigest": null,
      "recordedAt": "2026-09-21T10:00:00Z",
      "validFrom": "2026-01-01T00:00:00Z",
      "validUntil": "2027-01-01T00:00:00Z",
      "evidence": [
        "urn:synthetic:appointment"
      ],
      "issuedBy": "urn:synthetic:governor",
      "accountable": "urn:synthetic:owner",
      "state": "active",
      "stewardships": [],
      "rules": [
        {
          "id": "urn:synthetic:rule:a",
          "source": "urn:synthetic:source:a",
          "priority": 0,
          "validFrom": "2026-01-01T00:00:00Z",
          "validUntil": "2027-01-01T00:00:00Z",
          "evidence": [
            "urn:synthetic:rule-evidence"
          ]
        },
        {
          "id": "urn:synthetic:rule:b",
          "source": "urn:synthetic:source:b",
          "priority": 0,
          "validFrom": "2026-01-01T00:00:00Z",
          "validUntil": "2027-01-01T00:00:00Z",
          "evidence": [
            "urn:synthetic:rule-evidence"
          ]
        }
      ],
      "writeGrants": [
        {
          "id": "urn:synthetic:write:a",
          "source": "urn:synthetic:source:a",
          "writers": [
            "urn:synthetic:writer"
          ],
          "validFrom": "2026-01-01T00:00:00Z",
          "validUntil": "2027-01-01T00:00:00Z",
          "evidence": [
            "urn:synthetic:write-evidence"
          ]
        },
        {
          "id": "urn:synthetic:write:b",
          "source": "urn:synthetic:source:b",
          "writers": [
            "urn:synthetic:writer"
          ],
          "validFrom": "2026-01-01T00:00:00Z",
          "validUntil": "2027-01-01T00:00:00Z",
          "evidence": [
            "urn:synthetic:write-evidence"
          ]
        }
      ]
    }
  ],
  "observations": [
    {
      "id": "urn:synthetic:observation:1",
      "dimension": "urn:synthetic:dimension",
      "scope": "urn:synthetic:scope",
      "predicate": "urn:synthetic:predicate",
      "change": "genesis",
      "revision": 1,
      "previousDigest": null,
      "recordedAt": "2026-09-21T10:00:01Z",
      "validFrom": "2026-01-01T00:00:00Z",
      "validUntil": "2027-01-01T00:00:00Z",
      "evidence": [
        "urn:synthetic:evidence:1"
      ],
      "subject": "urn:synthetic:subject",
      "source": "urn:synthetic:source:a",
      "writer": "urn:synthetic:writer",
      "state": "asserted",
      "value": {
        "datatype": "urn:synthetic:string",
        "lexical": "A"
      }
    },
    {
      "id": "urn:synthetic:observation:2",
      "dimension": "urn:synthetic:dimension",
      "scope": "urn:synthetic:scope",
      "predicate": "urn:synthetic:predicate",
      "change": "genesis",
      "revision": 1,
      "previousDigest": null,
      "recordedAt": "2026-09-21T10:00:02Z",
      "validFrom": "2026-01-01T00:00:00Z",
      "validUntil": "2027-01-01T00:00:00Z",
      "evidence": [
        "urn:synthetic:evidence:2"
      ],
      "subject": "urn:synthetic:subject",
      "source": "urn:synthetic:source:b",
      "writer": "urn:synthetic:writer",
      "state": "asserted",
      "value": {
        "datatype": "urn:synthetic:string",
        "lexical": "A"
      }
    }
  ]
}

```

## FILE examples/startup.config.json
```
{
  "id": "urn:synthetic:config",
  "dimension": "urn:synthetic:dimension",
  "validFrom": "2026-01-01T00:00:00Z",
  "validUntil": "2027-01-01T00:00:00Z",
  "governors": [
    {
      "actor": "urn:synthetic:governor",
      "scope": "urn:synthetic:scope",
      "predicate": "urn:synthetic:predicate"
    }
  ],
  "readers": [
    "urn:synthetic:reader"
  ],
  "purposes": [
    "governance-review"
  ]
}

```

## FILE test-results.json
```
{
  "tests": 53,
  "failures": 0,
  "errors": 0,
  "passed": true,
  "scope": "Reference semantics including authority, temporal history, negative admission and disclosure; not authenticated production service"
}

```

## spec.json machine fields (contract omitted only because identical model-spec.md appears above)
{
  "metaModel": {
    "id": "enterprise-fact-authority",
    "registryId": "vr.profile.enterprise-fact-authority",
    "version": "0.1.0",
    "name": "Enterprise Fact Authority",
    "kind": "companion-contract"
  },
  "canonicalUrl": "https://ver.cy/models/wm-xct-001-ownership-stewardship/profiles/enterprise-fact-authority/0.1.0/spec.json",
  "researchAssurance": "reviewable-draft",
  "semanticRelationship": "Original companion contract, not a WM-XCT-001 ControlRecord subtype",
  "composition": {
    "profile": "enterprise-fact-authority",
    "version": "0.1.0",
    "runtimeImports": [],
    "semanticReferences": [
      {
        "id": "WM-XCT-001",
        "version": "0.3.0-research.1",
        "relation": "discovery-association-and-selected-patterns",
        "specSha256": "a09261ca365d2e82716705a27d5e46cca7faef8fc22d90fcf3b94a53ef729358"
      },
      {
        "id": "WM-XCT-002",
        "version": "0.3.0-research.1",
        "relation": "read-contract-patterns-only-not-write-grant",
        "specSha256": "9085d977567f3e1fc0b9bb27c6a7c517139f5972a1b95bf4a2bedccdb10bf2db"
      },
      {
        "id": "WM-XCT-012",
        "version": "0.3.0-research.1",
        "relation": "assertion-pattern-alignment",
        "specSha256": "aa6155354c55a87ab837ec9bd47f796ca582309fe383f1afffb802dafff7ecb5"
      }
    ],
    "nativeBinding": "Own vr.profile.enterprise-fact-authority@0.1.0 spec/namespace; WM-XCT-001 semantic-only optional reference",
    "instanceReferences": [
      "party",
      "source",
      "predicate",
      "scope",
      "definitionAuthorityRef",
      "evidence"
    ],
    "packageComposition": "Schema, code, docs, fixtures, tests; identified part versions embedded in authority revisions"
  },
  "nativeBinding": {
    "modelId": "vr.profile.enterprise-fact-authority",
    "path": "authority.register.snapshot",
    "companionRequired": true
  }
}

## Executed acceptance report, compact projection excluding verbose storedDecisions only
{
  "format": "vercy-authority-profile-acceptance",
  "executedAt": "2026-09-21T18:05:29Z",
  "passed": 3,
  "failed": 0,
  "profiles": [
    {
      "profile": "startup",
      "objects": 1,
      "facts": 2,
      "native": {
        "valid": true,
        "conformanceLevel": "V3",
        "schemas": "https://ver.cy/schemas/dimension/1.0/",
        "counts": {
          "objects": 1,
          "facts": 2,
          "relations": 0,
          "events": 0
        },
        "errors": [],
        "warnings": [],
        "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety"
      },
      "roundTripEqualsInput": true,
      "admissionReplayedThroughInstalledCompanion": true,
      "snapshotTruncationRejected": true,
      "invalidNestedSnapshot": {
        "native": {
          "valid": true,
          "conformanceLevel": "V3",
          "schemas": "https://ver.cy/schemas/dimension/1.0/",
          "counts": {
            "objects": 1,
            "facts": 2,
            "relations": 0,
            "events": 0
          },
          "errors": [],
          "warnings": [],
          "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety"
        },
        "companionRejected": true
      },
      "envelopeOperator": "urn:synthetic:register-operator",
      "envelopeAuthorityMeaning": "Snapshot storage only; never domain fact precedence",
      "pins": [
        {
          "id": "vr.wm-xct-001",
          "version": "0.3.0-research.1",
          "digest": "sha256:a09261ca365d2e82716705a27d5e46cca7faef8fc22d90fcf3b94a53ef729358",
          "mode": "semantic-only"
        },
        {
          "id": "vr.profile.enterprise-fact-authority",
          "version": "0.1.0",
          "digest": "sha256:cf027b56d01f23e39c15ad49a728967e45e7fb8d2b34137b6bb532536f35f582",
          "mode": "native-binding"
        }
      ]
    },
    {
      "profile": "group",
      "objects": 1,
      "facts": 2,
      "native": {
        "valid": true,
        "conformanceLevel": "V3",
        "schemas": "https://ver.cy/schemas/dimension/1.0/",
        "counts": {
          "objects": 1,
          "facts": 2,
          "relations": 0,
          "events": 0
        },
        "errors": [],
        "warnings": [],
        "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety"
      },
      "roundTripEqualsInput": true,
      "admissionReplayedThroughInstalledCompanion": true,
      "snapshotTruncationRejected": true,
      "invalidNestedSnapshot": {
        "native": {
          "valid": true,
          "conformanceLevel": "V3",
          "schemas": "https://ver.cy/schemas/dimension/1.0/",
          "counts": {
            "objects": 1,
            "facts": 2,
            "relations": 0,
            "events": 0
          },
          "errors": [],
          "warnings": [],
          "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety"
        },
        "companionRejected": true
      },
      "envelopeOperator": "urn:synthetic:register-operator",
      "envelopeAuthorityMeaning": "Snapshot storage only; never domain fact precedence",
      "pins": [
        {
          "id": "vr.wm-xct-001",
          "version": "0.3.0-research.1",
          "digest": "sha256:a09261ca365d2e82716705a27d5e46cca7faef8fc22d90fcf3b94a53ef729358",
          "mode": "semantic-only"
        },
        {
          "id": "vr.profile.enterprise-fact-authority",
          "version": "0.1.0",
          "digest": "sha256:cf027b56d01f23e39c15ad49a728967e45e7fb8d2b34137b6bb532536f35f582",
          "mode": "native-binding"
        }
      ]
    },
    {
      "profile": "ai-team",
      "objects": 1,
      "facts": 2,
      "native": {
        "valid": true,
        "conformanceLevel": "V3",
        "schemas": "https://ver.cy/schemas/dimension/1.0/",
        "counts": {
          "objects": 1,
          "facts": 2,
          "relations": 0,
          "events": 0
        },
        "errors": [],
        "warnings": [],
        "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety"
      },
      "roundTripEqualsInput": true,
      "admissionReplayedThroughInstalledCompanion": true,
      "snapshotTruncationRejected": true,
      "invalidNestedSnapshot": {
        "native": {
          "valid": true,
          "conformanceLevel": "V3",
          "schemas": "https://ver.cy/schemas/dimension/1.0/",
          "counts": {
            "objects": 1,
            "facts": 2,
            "relations": 0,
            "events": 0
          },
          "errors": [],
          "warnings": [],
          "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety"
        },
        "companionRejected": true
      },
      "envelopeOperator": "urn:synthetic:register-operator",
      "envelopeAuthorityMeaning": "Snapshot storage only; never domain fact precedence",
      "pins": [
        {
          "id": "vr.wm-xct-001",
          "version": "0.3.0-research.1",
          "digest": "sha256:a09261ca365d2e82716705a27d5e46cca7faef8fc22d90fcf3b94a53ef729358",
          "mode": "semantic-only"
        },
        {
          "id": "vr.profile.enterprise-fact-authority",
          "version": "0.1.0",
          "digest": "sha256:cf027b56d01f23e39c15ad49a728967e45e7fb8d2b34137b6bb532536f35f582",
          "mode": "native-binding"
        }
      ]
    }
  ],
  "sourceDigests": {
    "acceptance.py": "9670cd4931faf0a0f6b98f28d3858e7609dba37790d2745c4cd2eaa257153518",
    "authority.py": "cf058afbbab8e152bfbfc327365e0cc1863a77e2cd0a3df3da9ff116998b4415",
    "authority.schema.json": "cd76dc2dbe9c29551a22fecdf9374c440d3327cb92d0de1d8e216e55c0038944",
    "spec.json": "cf027b56d01f23e39c15ad49a728967e45e7fb8d2b34137b6bb532536f35f582",
    "tool-pins.json": "a2d5e2cbca9e9218c61f0346e1f25d3b35b867910161f79a71951df3569f172c",
    "examples\\ai-team.config.json": "257a4909c81afa2f67ed6f569d98bfbb2418ff5c136b1a96c58ff532690a14b5",
    "examples\\ai-team.json": "d5926ab1816403d3bc74e8d8387ab81797c2f68cda00cd3ff7382aa4d0a05483",
    "examples\\group.config.json": "257a4909c81afa2f67ed6f569d98bfbb2418ff5c136b1a96c58ff532690a14b5",
    "examples\\group.json": "ccc7c95f9ff7dfc01a9e5bb06d1886224e4693f86f10e80dd1a2b6a26e8870b8",
    "examples\\startup.config.json": "257a4909c81afa2f67ed6f569d98bfbb2418ff5c136b1a96c58ff532690a14b5",
    "examples\\startup.json": "d31046e0f54a63f4bea38ff1d4e57fba3431838a7f692e9b84fffd86fecce877"
  },
  "limits": "Synthetic new Dimensions; semantic-only parent plus separately identified companion. Candidate-installation metadata anticipates publication. No IAM, source truth, durable concurrency or existing-Dimension migration proof."
}
END OF REMEDIATION AUDIT INPUT
