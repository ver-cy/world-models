# Frozen semantic and implementation audit: enterprise identity profile

Respond in English. No tools, browsing, delegation, file writes or publication. Review only supplied frozen contents. Return BLOCK / ACCEPT WITH LIMITS, specific defects and executable counterexamples. Review is not approval authority. State exact scope and anything not seen.

This is a narrow profile of existing WM-XCT-036, with WM-XCT-011 carriage, not a new world-model. 48 tests and three native new-Dimension scenarios passed locally; audit these claims critically, do not pretend you ran them. Existing source holds and historical Claude-only 036 review remain. Your earlier study saw source excerpts partially; selected exact local/public-byte-verified definitions are included below to close the specific relation/assignment mapping questions, not all legacy holds.

Design reconciliation: retain parent relation codes equivalent-in-context/not-same-assertion/probable-entity-match with candidate never asserted; do not adopt Grok's new source-scoped-denotation code. A single assertion owns no resolution status; a pure query gives accepted-in-input, not globally accepted. All authority conflicts stay contested, no ranking. Policy is frozen, digest-pinned and caller-trusted; policy rotation fails closed. Authentication, evidence truth, read/write enforcement, global completeness and retention remain external. A user-account or service-account cannot become Person even by override. Startup fixtures explicitly use synthetic person-reference exports, not Git/tracker account IDs. This narrower scope means EM-XCT-01 remains partial.

Inspect especially bitemporal events, contested/negative/candidate cases, assignment reuse and collision, schema bypass, idempotency, input mutation, source evidence, policy/namespace gates, and nested V3 versus companion validation. Flag a bug versus an explicitly out-of-scope capability distinctly. Publication plan: additive versioned profile associated with the existing model; never claim your bounded review verifies all 108 historical sources or the whole parent.

## FILE README.md
```
# Enterprise identity assertions

Profile version 0.1.0 for WM-XCT-036 Alias / Same-as Mapping, with qualified identifier assignments reused from WM-XCT-011. This is a bounded reference profile, with research assurance `reviewable-draft`.

An assertion links one source-qualified identifier assignment to one existing local subject. Several independently reviewed person-reference IDs may refer to one Person. An account is a different referent: a Git or tracker account does not become a Person because somebody owns it. Account ownership requires a separate relationship model. The synthetic startup fixture explicitly represents person-reference exports from source directories; it does not describe the actual semantics of a Git account API.

The reference keeps links and their revision history separate from the subjects. It computes a view of the supplied assertion set at a valid time and a knowledge time. It never edits source systems, merges people, runs matching or exports global equality.

## Run locally

Use Python 3.12+ and install `jsonschema[format-nongpl]>=4,<5` in your chosen environment. Extract the complete profile package and run:

```text
python -m pip install "jsonschema[format-nongpl]>=4,<5"
python test_identity.py
python identity_profile.py examples/startup.json --policy examples/policy.json
```

The bundled policy is synthetic. It grants no authority over a real organization. Supply policy and evidence from independently trusted local sources for any real use. The implementation checks declared constraints; it does not authenticate a caller, signature, source record or reviewer. It is not enterprise IAM or an identity-proofing service.

## Read the result correctly

`resolve()` returns `accepted-in-input`, `contested`, `candidate` or `unknown`, with supporting and opposing assertion IDs, temporal coordinates and input/policy digests. `accepted-in-input` means exactly one admissible target in the supplied snapshot. It does not prove global uniqueness, complete source coverage, a person's identity or any access right. Negative claims remain visible even when there is no positive target. A dispute blocks acceptance. Different authorized targets remain contested; this profile has no silent precedence winner.

`import_assertion()` is a pure function. Identical replay is a no-op. A longer history must preserve the exact previous prefix. Changing endpoints, relation, assignment window or purpose requires retracting the old assertion and using a new assertion ID. The function does not write files or implement a concurrent transaction; a real importer must own storage, locking, expected-head checks and audit.

## Boundaries

- Exact string comparison only. Unknown assignment starts, custom normalizers, fuzzy matches and general schemes need another explicit profile. Unknown is never replaced by epoch or a fabricated open-ended date.
- The same qualified lexical ID may have separate assignment occurrences. Resolution considers overlapping active occurrences together; reassignment does not extend an old person's identity into a new period.
- One frozen, independently supplied policy governs each input set. Changing it makes prior digest pins fail closed. Dynamic warrant revocation, policy history, ranking, cross-policy federation and erasure are deferred; do not infer those capabilities from a passing test.
- Historical reads do not grant present authority. The supplied current read policy must still be valid. The caller supplies the authenticated actor, trusted clock and input set.
- Local subject references must use the declared namespace. No cross-Dimension disclosure is implemented. Correlation links can themselves be sensitive: access must be enforced before this reference receives its inputs and after it returns a result.
- No in-place migration of existing Dimensions, endpoint merge/split or inverse conversion to a lossy legacy table is implemented. Preserve the complete JSON envelope on round-trip.
- The original Identifier Scheme and Alias / Same-as Mapping publication holds remain. The new Claude and Grok reviews cover this enterprise increment only.

See `model-spec.md`, the four closed JSON schemas, `crosswalk.json`, `whole-object-coverage.json`, `mastership-and-rights.json`, and the separately recorded test and native acceptance reports. Native V3 validation checks the outer record; the companion validator must check the nested assertion separately.

```

## FILE model-spec.md
```
# Enterprise identity-assertion profile 0.1.0

## Boundary and canonical ownership

This is a narrower usage and representation profile of WM-XCT-036, not a new subject model. Identifier assignment meaning is reused from WM-XCT-011. A source binding is a frozen carrier value in an assertion, whose source authority remains external. An assertion is its own identified claim. The resolution result is a derived, disposable query artifact; it has no subject mastership. The externally supplied policy is a reference-test binding of local governance, not a new policy model owned by identity.

Included WM-XCT-036 concerns: assertion envelope, endpoint reference boundary, relation classification, contextual validity, evidence, immutable transition history, and a scoped read contract. Matching engines, graph closure, redirects, global equality, cluster mastership, disclosure engines and endpoint mutations remain excluded. The exact included source finding/layer IDs are recorded in `crosswalk.json`.

The profile admits `equivalent-in-context`, `not-same-assertion` and `probable-entity-match`, using the existing relation register. All have `inferencePermitted=false`; the third can never enter asserted state. The existing definition of equivalent-in-context limits its claim to a named context; here that context is the adopting Dimension, declared purpose, referent kind and interval. It does not mean account ownership, loose resemblance or global OWL equality. We deliberately retain existing codes instead of adopting Grok's proposed new names. Scores, names and email matches cannot activate a claim on their own.

## Types, identities and relationships

| Type | Identity and role | Cardinality and ownership |
|---|---|---|
| QualifiedIdentifierAssignment | Source-issued `assignmentId`, exact `scheme`, `schemeVersion`, `issuer`, `scope`, `value`; occurrence validity and source record | One frozen assignment carrier per assertion. Issuer owns the assignment; importer cannot reinterpret it. Same assignment ID with different content is refused. |
| IdentityAssertion | Local issuer-qualified `id`, Dimension, purpose, predicate, fixed source and target, fixed validity | One source and one target. A subject can have many independent assertions. Zero or many assertions may concern one qualified ID. Conflicting claims are data to preserve. |
| AssertionRevisionEvent | Distinct `id`, previous event digest, effective time, recorded time, actor, state, reason and evidence | Ordered one-to-many owned history. Event IDs are unique across the provided set. Source evidence is referenced, not copied as private content. |
| EvidenceReference | Source-qualified URI plus kind and description | One or more per event. Activation requires source-record and review-decision categories; authenticity is a caller responsibility. |
| ReferenceAuthorityPolicy | Independently supplied URI/version and digest, Dimension, purpose, namespace, issuer list, actor permissions, readers and interval | One frozen policy for the bounded input set. The Dimension policy owner supplies it. It is not self-issued by an assertion. |
| ResolutionView | Canonical input digest, policy digest and two temporal coordinates | Computed on demand over one supplied set. Returns supporting/opposing/candidate/disputed IDs. No editable canonical subject or aggregate is created. |

Field-level types, requiredness and cardinalities are defined by `assertion.schema.json`, `binding.schema.json`, `policy.schema.json` and `query.schema.json`. `field-catalog.json` maps their carrier fields to ownership, sensitivity and the governing contract. All object schemas are closed. Optional open end is `null`; missing required context is rejected, not guessed. No numeric confidence is encoded, so absence cannot be confused with zero.

## Lifecycle, temporal queries and correction

An assertion begins proposed. Proposed can become asserted, disputed or retracted. Asserted can become disputed or retracted. Disputed can become asserted or retracted. Retracted is terminal. These are recorded issuer declarations; a derived view separately evaluates eligibility and conflict.

Each event must be authorized by the supplied frozen policy at its recording time. Recording times increase strictly. Effective times may be retroactive but cannot precede the assertion's start or exceed their recording time. At `(validAt, knownAt)`, select the latest recorded event known then whose effective time has arrived. Both assertion and assignment intervals are half-open. A later correction changes a current view without rewriting an earlier knowledge-time answer. The report's digest may change when the supplied set grows even though the historical substantive answer stays the same.

A changed endpoint, purpose, predicate or validity window is a new assertion ID, after explicit retraction of the old claim when appropriate. Append-only history is enforced relative to the caller's existing input by `import_assertion`; the reference cannot prove that an arbitrary standalone input has not been falsified or truncated. Concurrent persistence, event authentication and historical-policy recovery are separate integration duties.

## Invariants

1. Compare exact qualified keys only; issuer and tenant scope are never inferred.
2. Preserve scheme version, raw value and assignment occurrence. This profile has no normalization transform.
3. The assignment's declared referent kind must equal the target kind. Account-to-person ownership is refused even with a claimed override.
4. The target must be in the policy's local subject namespace; no positive identifier-to-identifier chains are traversed.
5. Fixed assertion content cannot change under the same assertion ID; previous event digests and historical prefixes remain intact.
6. Candidate relations never activate. Activation requires both source evidence and reviewer evidence as declared categories.
7. Policy digest, Dimension, purpose, permitted issuer, actor/state grant and recording-time validity must agree.
8. Read purpose and actor must be allowed by the currently supplied policy. Historical knowledge cannot exceed evaluation time.
9. Validity cannot exceed the assignment interval. Unknown starts and invalid/reversed windows are refused.
10. Multiple active target IDs, active opposition against a positive target, or a disputed claim produce contested status. Authority ranking is deliberately absent.
11. No positive evidence means unknown or candidate; explicit negative claims remain in `opposing` and are not dropped.
12. Replaying an identical assertion is a no-op; divergent content or history truncation is refused. Full JSON round-trip is lossless.
13. The resolver does not grant access, export equality, mutate endpoints or assert global completeness.
14. A V3-valid outer fact can contain a semantically invalid snapshot; companion validation is mandatory.

## Questions and artifact routes

| Question | Inspect / produce | Permitted next action |
|---|---|---|
| What does this source ID actually denote? | Binding kind and source record | Request source evidence; do not infer Person from Account |
| Who owns its namespace? | Scheme, issuer, scope | Compare only within the qualified key |
| Which scheme version governs comparison? | Version and exact-string declaration | Refuse unsupported normalization |
| Is this a new assignment occurrence? | Assignment ID and validity | Preserve prior occurrence and inspect source history |
| What local subject does the claim concern? | Target ID and kind | Verify namespace and reference externally |
| Who may assert this link? | Policy digest and event actor grant | Validate declared grant, then authenticate externally |
| What evidence supports activation? | Source-record and review-decision references | Keep name/email-only material proposed |
| Is the claim only a candidate? | Relation and history | Never auto-activate a score |
| What was effective at a date? | Valid time and event effective time | Produce a scoped temporal view |
| What was known at that date? | Recorded times and knownAt | Preserve earlier substantive answers |
| Is another claim incompatible? | Complete caller-selected input set | Return contested; do not choose a winner |
| Is there explicit opposition? | Negative assertions and opposing IDs | Retain negative knowledge distinctly |
| How is a mistake corrected? | Retraction plus successor assertion | Use append-only import; leave endpoints intact |
| Can this link disclose another Dimension? | Namespace and external access policy | Deny implicit disclosure |
| Is a replay identical? | Assertion identity, digest and history prefix | No-op or explicit conflict |
| What is missing for a real merge? | Separate migration/transaction plan | Defer endpoint merge and split |
| What survives a round-trip? | Complete closed envelope | Refuse field-dropping conversions |
| Is this globally unique or authenticated? | Scope and caller trust assumptions | Answer insufficient-context; do not claim proof |

Every answer is conditional on available authoritative context. If evidence or permission is missing, request the relevant artifact or return a refusal/unknown; do not synthesize facts.

## Adoption and migration

Start with the synthetic fixtures. A real deployment needs source-specific mapping, source-issued assignment identities, authenticated policy/evidence, retention and access controls, storage concurrency and an independently selected complete input set. The reference does not allocate those responsibilities to Git, HRIS or an ERP merely by naming them.

Legacy matcher scores or denormalized identity columns enter review as proposals. Do not import an existing merge as accepted truth. A changed profile version requires explicit semantic comparison; unknown versions are refused. No automated downgrade or in-place Dimension migration is supplied. WM-XCT-040's exact new-Dimension composition route is used only with explicit pins and separate semantic/native readiness.

```

## FILE identity_profile.py
```
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

```

## FILE identity-profile.schema.json
```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://ver.cy/enterprise/profiles/identity-assertion/0.1.0/identity-profile.schema.json",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "format": {
      "const": "vercy-enterprise-identity-assertion"
    },
    "version": {
      "const": "0.1.0"
    },
    "id": {
      "type": "string",
      "minLength": 1,
      "maxLength": 1024,
      "format": "uri",
      "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
    },
    "dimension": {
      "type": "string",
      "minLength": 1,
      "maxLength": 1024,
      "format": "uri",
      "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
    },
    "purpose": {
      "type": "string",
      "minLength": 1,
      "maxLength": 1024
    },
    "policyDigest": {
      "type": "string",
      "pattern": "^sha256:[0-9a-f]{64}$"
    },
    "binding": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "assignmentId": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024,
          "format": "uri",
          "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
        },
        "scheme": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024,
          "format": "uri",
          "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
        },
        "schemeVersion": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024
        },
        "issuer": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024,
          "format": "uri",
          "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
        },
        "scope": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024,
          "format": "uri",
          "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
        },
        "value": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024
        },
        "comparison": {
          "const": "exact-string"
        },
        "kind": {
          "enum": [
            "person",
            "organization",
            "user-account",
            "service-account"
          ]
        },
        "validFrom": {
          "type": "string",
          "format": "date-time",
          "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"
        },
        "validTo": {
          "anyOf": [
            {
              "type": "string",
              "format": "date-time",
              "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"
            },
            {
              "type": "null"
            }
          ]
        },
        "recordedAt": {
          "type": "string",
          "format": "date-time",
          "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"
        },
        "sourceRecord": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024,
          "format": "uri",
          "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
        },
        "personalDataClass": {
          "enum": [
            "synthetic",
            "restricted"
          ]
        },
        "credentialProhibition": {
          "const": true
        }
      },
      "required": [
        "assignmentId",
        "scheme",
        "schemeVersion",
        "issuer",
        "scope",
        "value",
        "comparison",
        "kind",
        "validFrom",
        "validTo",
        "recordedAt",
        "sourceRecord",
        "personalDataClass",
        "credentialProhibition"
      ]
    },
    "target": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "id": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024,
          "format": "uri",
          "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
        },
        "kind": {
          "enum": [
            "person",
            "organization",
            "user-account",
            "service-account"
          ]
        }
      },
      "required": [
        "id",
        "kind"
      ]
    },
    "relation": {
      "enum": [
        "equivalent-in-context",
        "not-same-assertion",
        "probable-entity-match"
      ]
    },
    "validFrom": {
      "type": "string",
      "format": "date-time",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"
    },
    "validTo": {
      "anyOf": [
        {
          "type": "string",
          "format": "date-time",
          "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"
        },
        {
          "type": "null"
        }
      ]
    },
    "inferencePermitted": {
      "const": false
    },
    "history": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1024,
            "format": "uri",
            "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
          },
          "previousDigest": {
            "anyOf": [
              {
                "type": "string",
                "pattern": "^sha256:[0-9a-f]{64}$"
              },
              {
                "type": "null"
              }
            ]
          },
          "recordedAt": {
            "type": "string",
            "format": "date-time",
            "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"
          },
          "effectiveAt": {
            "type": "string",
            "format": "date-time",
            "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"
          },
          "actor": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1024,
            "format": "uri",
            "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
          },
          "state": {
            "enum": [
              "proposed",
              "asserted",
              "disputed",
              "retracted"
            ]
          },
          "reason": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1024
          },
          "evidence": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "ref": {
                  "type": "string",
                  "minLength": 1,
                  "maxLength": 1024,
                  "format": "uri",
                  "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
                },
                "kind": {
                  "enum": [
                    "source-record",
                    "review-decision",
                    "name-match",
                    "email-match",
                    "git-author",
                    "legacy-import"
                  ]
                },
                "description": {
                  "type": "string",
                  "minLength": 1,
                  "maxLength": 1024
                }
              },
              "required": [
                "ref",
                "kind",
                "description"
              ]
            },
            "minItems": 1
          }
        },
        "required": [
          "id",
          "previousDigest",
          "recordedAt",
          "effectiveAt",
          "actor",
          "state",
          "reason",
          "evidence"
        ]
      },
      "minItems": 1
    }
  },
  "required": [
    "format",
    "version",
    "id",
    "dimension",
    "purpose",
    "policyDigest",
    "binding",
    "target",
    "relation",
    "validFrom",
    "validTo",
    "inferencePermitted",
    "history"
  ],
  "$defs": {
    "policy": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "format": {
          "const": "vercy-identity-reference-policy"
        },
        "version": {
          "const": "0.1.0"
        },
        "id": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024,
          "format": "uri",
          "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
        },
        "dimension": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024,
          "format": "uri",
          "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
        },
        "purpose": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024
        },
        "subjectPrefix": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024,
          "format": "uri",
          "pattern": "^[a-z][a-z0-9+.-]*:.+[:/]$"
        },
        "validFrom": {
          "type": "string",
          "format": "date-time",
          "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"
        },
        "validTo": {
          "anyOf": [
            {
              "type": "string",
              "format": "date-time",
              "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"
            },
            {
              "type": "null"
            }
          ]
        },
        "issuers": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1024,
            "format": "uri",
            "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
          },
          "minItems": 1,
          "uniqueItems": true
        },
        "relations": {
          "type": "array",
          "items": {
            "enum": [
              "equivalent-in-context",
              "not-same-assertion",
              "probable-entity-match"
            ]
          },
          "minItems": 1,
          "uniqueItems": true
        },
        "actors": {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "actor": {
                "type": "string",
                "minLength": 1,
                "maxLength": 1024,
                "format": "uri",
                "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
              },
              "states": {
                "type": "array",
                "items": {
                  "enum": [
                    "proposed",
                    "asserted",
                    "disputed",
                    "retracted"
                  ]
                },
                "minItems": 1,
                "uniqueItems": true
              }
            },
            "required": [
              "actor",
              "states"
            ]
          },
          "minItems": 1
        },
        "readers": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1024,
            "format": "uri",
            "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
          },
          "minItems": 1,
          "uniqueItems": true
        }
      },
      "required": [
        "format",
        "version",
        "id",
        "dimension",
        "purpose",
        "subjectPrefix",
        "validFrom",
        "validTo",
        "issuers",
        "relations",
        "actors",
        "readers"
      ]
    },
    "query": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "scheme": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024,
          "format": "uri",
          "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
        },
        "schemeVersion": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024
        },
        "issuer": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024,
          "format": "uri",
          "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
        },
        "scope": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024,
          "format": "uri",
          "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
        },
        "value": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024
        }
      },
      "required": [
        "scheme",
        "schemeVersion",
        "issuer",
        "scope",
        "value"
      ]
    },
    "binding": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "assignmentId": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024,
          "format": "uri",
          "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
        },
        "scheme": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024,
          "format": "uri",
          "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
        },
        "schemeVersion": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024
        },
        "issuer": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024,
          "format": "uri",
          "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
        },
        "scope": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024,
          "format": "uri",
          "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
        },
        "value": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024
        },
        "comparison": {
          "const": "exact-string"
        },
        "kind": {
          "enum": [
            "person",
            "organization",
            "user-account",
            "service-account"
          ]
        },
        "validFrom": {
          "type": "string",
          "format": "date-time",
          "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"
        },
        "validTo": {
          "anyOf": [
            {
              "type": "string",
              "format": "date-time",
              "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"
            },
            {
              "type": "null"
            }
          ]
        },
        "recordedAt": {
          "type": "string",
          "format": "date-time",
          "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"
        },
        "sourceRecord": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024,
          "format": "uri",
          "pattern": "^[a-zA-Z][a-zA-Z0-9+.-]*:"
        },
        "personalDataClass": {
          "enum": [
            "synthetic",
            "restricted"
          ]
        },
        "credentialProhibition": {
          "const": true
        }
      },
      "required": [
        "assignmentId",
        "scheme",
        "schemeVersion",
        "issuer",
        "scope",
        "value",
        "comparison",
        "kind",
        "validFrom",
        "validTo",
        "recordedAt",
        "sourceRecord",
        "personalDataClass",
        "credentialProhibition"
      ]
    }
  }
}

```

## FILE test_identity.py
```
import copy,datetime,json,unittest
from pathlib import Path
import identity_profile as p
HERE=Path(__file__).resolve().parent
class IdentityTests(unittest.TestCase):
 def setUp(self):
  self.policy=p.load(HERE/'examples/policy.json');self.rows=p.load(HERE/'examples/startup.json');self.a=copy.deepcopy(self.rows[0])
 def query(self,rows=None,**kw):
  defaults={'valid_at':'2026-01-01T00:00:00Z','known_at':'2026-01-01T00:00:00Z','evaluation_at':'2026-09-21T00:00:00Z','reader':'urn:synthetic:actor:steward','purpose':self.policy['purpose']};defaults.update(kw)
  return p.resolve(rows if rows is not None else self.rows,{k:self.a['binding'][k] for k in ['scheme','schemeVersion','issuer','scope','value']},self.policy,**defaults)
 def append(self,a,state='retracted',recorded='2025-08-01T00:00:00Z',effective='2025-02-01T00:00:00Z'):
  e=copy.deepcopy(a['history'][-1]);e.update(id=e['id']+':next',previousDigest=p.digest(a['history'][-1]),state=state,recordedAt=recorded,effectiveAt=effective);a['history'].append(e);return a
 def invalid(self,a):
  with self.assertRaises(p.Invalid):p.validate(a,self.policy)
 def other(self):
  b=copy.deepcopy(self.a);b['id']+=':other'
  for e in b['history']:e['id']+=':other'
  b['history'][1]['previousDigest']=p.digest(b['history'][0]);return b
 def test_three_profiles(self):
  for n in ['startup','group','ai-team']:p.validate_set(p.load(HERE/('examples/'+n+'.json')),self.policy)
 def test_three_person_references_one_subject(self):
  for a in self.rows:
   self.a=a;r=self.query();self.assertEqual(r['status'],'accepted-in-input');self.assertEqual(r['targets'],['urn:synthetic:subject:p1']);self.assertFalse(r['grantsAccess'])
 def test_equal_authority_conflict(self):
  b=self.other();b['target']['id']='urn:synthetic:subject:p2';self.assertEqual(self.query([self.a,b])['status'],'contested')
 def test_negative_conflict(self):
  b=self.other();b['relation']='not-same-assertion';self.assertEqual(self.query([self.a,b])['status'],'contested')
 def test_negative_only_not_silently_absent(self):
  self.a['relation']='not-same-assertion';r=self.query([self.a]);self.assertEqual(r['status'],'unknown');self.assertEqual(r['opposing'],[self.a['id']])
 def test_candidate_inert(self):
  self.a['relation']='probable-entity-match';self.a['history']=self.a['history'][:1];self.assertEqual(self.query([self.a])['status'],'candidate')
 def test_candidate_cannot_activate(self):self.a['relation']='probable-entity-match';self.invalid(self.a)
 def test_email_evidence_not_sufficient(self):
  self.a['history'][1]['evidence']=[{'ref':'urn:synthetic:email','kind':'email-match','description':'Same mailbox'}];self.invalid(self.a)
 def test_unknown_no_claim(self):self.assertEqual(self.query([])['status'],'unknown')
 def test_account_person_refused(self):self.a['binding']['kind']='user-account';self.invalid(self.a)
 def test_service_account_person_refused(self):self.a['binding']['kind']='service-account';self.invalid(self.a)
 def test_retract_history(self):
  later=self.append(copy.deepcopy(self.a));self.assertEqual(self.query([later])['status'],'unknown');self.assertEqual(self.query([later],known_at='2025-06-01T00:00:00Z')['status'],'accepted-in-input')
 def test_bitemporal_effective_date(self):
  later=self.append(copy.deepcopy(self.a));self.assertEqual(self.query([later],valid_at='2025-01-15T00:00:00Z')['status'],'accepted-in-input')
 def test_history_preserved_after_append(self):
  old=self.query([self.a],known_at='2025-06-01T00:00:00Z');new=self.query([self.append(copy.deepcopy(self.a))],known_at='2025-06-01T00:00:00Z')
  for k in ['status','targets','supporting','opposing','excluded']:self.assertEqual(old[k],new[k])
 def test_retracted_terminal(self):self.append(self.a);self.append(self.a,'asserted','2025-09-01T00:00:00Z');self.invalid(self.a)
 def test_disputed_blocks_resolution(self):self.append(self.a,'disputed');self.assertEqual(self.query([self.a])['status'],'contested')
 def test_predecessor_tamper(self):self.a['history'][1]['previousDigest']='sha256:'+'0'*64;self.invalid(self.a)
 def test_event_order(self):self.a['history'][1]['recordedAt']=self.a['history'][0]['recordedAt'];self.invalid(self.a)
 def test_actor_cannot_assert(self):self.a['history'][1]['actor']='urn:synthetic:actor:importer';self.invalid(self.a)
 def test_expired_authority(self):self.a['history'][1]['recordedAt']='2028-01-01T00:00:00Z';self.invalid(self.a)
 def test_policy_tamper(self):self.policy['purpose']='different';self.invalid(self.a)
 def test_wrong_dimension(self):self.a['dimension']='urn:other:dimension';self.invalid(self.a)
 def test_cross_dimension_target(self):self.a['target']['id']='urn:other:subject:p1';self.invalid(self.a)
 def test_issuer_scope_isolation(self):
  b=self.other();b['binding']['assignmentId']+=':other';b['binding']['scope']='urn:synthetic:tenant:other';b['target']['id']='urn:synthetic:subject:p2';self.assertEqual(self.query([self.a,b])['targets'],[self.a['target']['id']])
 def test_reassignment_temporal(self):
  rows=p.load(HERE/'examples/group.json');self.a=rows[0];self.assertEqual(self.query(rows,valid_at='2025-03-01T00:00:00Z')['targets'],['urn:synthetic:subject:pa']);self.assertEqual(self.query(rows,valid_at='2025-10-01T00:00:00Z')['targets'],['urn:synthetic:subject:pc'])
 def test_overlapping_reassignments_contested(self):
  b=self.other();b['binding']['assignmentId']+=':new';b['target']['id']='urn:synthetic:subject:p2';self.assertEqual(self.query([self.a,b])['status'],'contested')
 def test_qualified_assignment_not_overwritten(self):
  b=self.other();b['binding']['value']='different'
  with self.assertRaises(p.Invalid):p.validate_set([self.a,b],self.policy)
 def test_missing_qualification(self):del self.a['binding']['issuer'];self.invalid(self.a)
 def test_normalization_refused(self):self.a['binding']['comparison']='lowercase';self.invalid(self.a)
 def test_value_case_preserved(self):
  b=self.other();b['binding']['assignmentId']+=':new';b['binding']['value']='e7';b['target']['id']='urn:synthetic:subject:p2';self.assertEqual(self.query([self.a,b])['targets'],[self.a['target']['id']])
 def test_same_as_refused(self):self.a['relation']='owl:sameAs';self.invalid(self.a)
 def test_closure_refused(self):self.a['inferencePermitted']=True;self.invalid(self.a)
 def test_unknown_time_not_epoch(self):self.a['binding']['validFrom']=None;self.invalid(self.a)
 def test_interval_bounds(self):self.a['validTo']=self.a['validFrom'];self.invalid(self.a)
 def test_assignment_bounds(self):self.a['binding']['validTo']='2025-02-01T00:00:00Z';self.invalid(self.a)
 def test_read_denied(self):
  with self.assertRaises(p.Invalid):self.query(reader='urn:synthetic:actor:intruder')
 def test_current_authority_expiry(self):
  with self.assertRaises(p.Invalid):self.query(evaluation_at='2028-01-01T00:00:00Z')
 def test_future_knowledge_refused(self):
  with self.assertRaises(p.Invalid):self.query(known_at='2027-01-01T00:00:00Z')
 def test_replay_noop(self):self.assertEqual(p.import_assertion(self.rows,self.a,self.policy),self.rows)
 def test_history_extension(self):
  new=self.append(copy.deepcopy(self.a));out=p.import_assertion(self.rows,new,self.policy);self.assertEqual(out[0],new);self.assertEqual(len(self.rows[0]['history']),2)
 def test_history_truncation_refused(self):
  a=copy.deepcopy(self.a);a['history']=a['history'][:1]
  with self.assertRaises(p.Invalid):p.import_assertion(self.rows,a,self.policy)
 def test_endpoint_change_refused(self):
  b=self.append(copy.deepcopy(self.a));b['target']['id']='urn:synthetic:subject:p2'
  with self.assertRaises(p.Invalid):p.import_assertion(self.rows,b,self.policy)
 def test_round_trip(self):self.assertEqual(json.loads(p.encode(self.rows)),self.rows)
 def test_lossy_round_trip_refused(self):del self.a['binding']['sourceRecord'];self.invalid(self.a)
 def test_unknown_version_refused(self):self.a['version']='9';self.invalid(self.a)
 def test_undeclared_field_refused(self):self.a['resolutionStatus']='accepted';self.invalid(self.a)
 def test_policy_no_self_grant(self):self.a['policy']={'allow':True};self.invalid(self.a)
 def test_duplicate_event_id_refused(self):
  b=self.other();b['history'][0]['id']=self.a['history'][0]['id'];b['history'][1]['previousDigest']=p.digest(b['history'][0])
  with self.assertRaises(p.Invalid):p.validate_set([self.a,b],self.policy)

if __name__=='__main__':
 result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(IdentityTests))
 (HERE/'test-results.json').write_text(json.dumps({'executedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tests':result.testsRun,'passed':result.wasSuccessful(),'failures':len(result.failures),'errors':len(result.errors)},indent=2)+'\n')
 raise SystemExit(0 if result.wasSuccessful() else 1)

```

## FILE acceptance.py
```
"""Synthetic new-Dimension acceptance, using explicitly trusted local tools.

python acceptance.py --composer /trusted/WM-XCT-040 --skill /trusted/vercy/skills/vercy --report acceptance-results.json
Only this script's temporary directory is changed. No existing Dimension is used.
"""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from pathlib import Path
import identity_profile as p
HERE=Path(__file__).resolve().parent
def run(composer,skill):
    p.require(__debug__,'Run acceptance without -O')
    composer=Path(composer).resolve();skill=Path(skill).resolve()
    pins=p.load(HERE/'tool-pins.json')
    for name,h in pins['composerFiles'].items():p.require(hashlib.sha256((composer/name).read_bytes()).hexdigest()==h,'unexpected composer bytes: '+name)
    sys.path.insert(0,str(composer));import composition as c
    from bootstrap_dimension import bootstrap
    sys.path.insert(0,str(skill/'scripts'));from write_record import append
    from validate_dimension import validate as native_validate
    identity_policy=p.load(HERE/'examples/policy.json');reports=[]
    with tempfile.TemporaryDirectory(prefix='vercy-identity-acceptance-') as tmp:
        root=Path(tmp);assets=root/'assets';assets.mkdir()
        def descriptor(slug,name,source):
            raw=source.read_bytes();dest=assets/slug/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
            return {'path':slug+'/'+name,'digest':c.digest(raw),'size':len(raw),'mediaType':'text/x-python' if name.endswith('.py') else 'application/json' if name.endswith('.json') else 'text/markdown' if name.endswith('.md') else 'application/yaml','sourceUrl':'https://ver.cy/models/'+slug+'/'+name}
        releases=[]
        for slug in ['wm-xct-011-identifier-scheme','wm-xct-036-alias-same-as-mapping']:
            source=HERE/'upstream'/slug;raw=(source/'spec.yaml').read_text(encoding='utf-8');meta=json.loads(raw[raw.index('{'):])['metaModel']
            dspec=descriptor(slug,'spec.yaml',source/'spec.yaml');dagent=descriptor(slug,'AGENTS.md',source/'AGENTS.md')
            binding=None
            if meta['id']=='WM-XCT-036':
                runtime=descriptor(slug,'runtime-model.reference.json',HERE/'runtime-model.reference.json')
                instance=descriptor(slug,'identity-profile.schema.json',HERE/'identity-profile.schema.json')
                validator=descriptor(slug,'identity_profile.py',HERE/'identity_profile.py')
                binding={'id':'urn:vercy:binding:enterprise-identity-assertion','version':'0.1.0','forSpecificationDigest':dspec['digest'],'runtime':runtime,'instanceSchema':instance,'companionValidator':validator,'scope':'One bounded enterprise assertion snapshot; companion semantics required; no account ownership, endpoint merge, IAM or whole-model conformance.'}
            releases.append({'modelId':meta['registryId'],'version':meta['version'],'namespace':'urn:vercy:model:'+meta['registryId'],'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','requires':[],'references':[],'specification':dspec,'agents':dagent,'installationMode':'native-binding' if binding else 'semantic-only','binding':binding,'semanticFingerprint':None,'compatibility':{'decision':'accepted','reviewer':'urn:synthetic:reviewer:identity','evidence':'urn:synthetic:acceptance:identity','observedAt':c.now(),'scope':'Only this reference binding and synthetic composition.'}})
        releases[1]['requires']=[{k:releases[0][k] for k in ['modelId','version']}]
        for name in ['startup','group','ai-team']:
            target=root/name;stage=root/(name+'-stage');policy_path=root/(name+'-composition-policy.json');lock_path=root/(name+'-lock.json');plan_path=root/(name+'-plan.json')
            dimension=identity_policy['dimension'];at=c.now()
            policy={'format':'vercy-composition-policy','version':1,'id':'urn:synthetic:composition-policy:identity','dimensionId':dimension,'owner':'urn:synthetic:owner:identity','allowInstall':True,'actors':['urn:synthetic:actor:composer'],'purposes':['Synthetic enterprise identity reference'],'allowedModelIds':['vr.wm-xct-011','vr.wm-xct-036'],'allowedOrigins':['https://ver.cy'],'reviewers':['urn:synthetic:reviewer:identity'],'allowReviewableDrafts':True,'validFrom':'2026-09-21T00:00:00Z','validUntil':'2027-01-01T00:00:00Z'}
            policy_path.write_bytes(c.encode(policy));lock_path.write_bytes(c.encode({'models':[]}))
            plan={'format':'vercy-composition-plan','schemaVersion':'1.0.0','planId':'urn:synthetic:composition:identity:'+name,'revision':1,'supersedes':None,'algorithm':'exact-closure-v1','dimensionId':dimension,'createdAt':at,'validUntil':'2026-12-31T23:59:59Z','baseLockDigest':c.digest(lock_path.read_bytes()),'roots':[{k:releases[1][k] for k in ['modelId','version']}],'releases':releases,'authority':{'actor':policy['actors'][0],'allowReviewableDrafts':True,'allowedModelIds':policy['allowedModelIds'],'decision':'allow','owner':policy['owner'],'policyDigest':c.digest(policy_path.read_bytes()),'policyRef':policy['id'],'purpose':policy['purposes'][0]},'provenance':{'classification':'public-synthetic','evidenceKind':'proposal','masterSystem':'urn:synthetic:reference','recordedAt':at,'source':'urn:synthetic:fixture:'+name}}
            plan_path.write_bytes(c.encode(plan));c.stage(plan_path,assets,policy_path,lock_path,stage)
            bootstrap(stage,policy_path,lock_path,skill,target,'Synthetic identity '+name,dimension)
            installed=target/'models/composed/wm-xct-036-alias-same-as-mapping/identity_profile.py'
            p.require(c.digest(installed.read_bytes())==releases[1]['binding']['companionValidator']['digest'],'installed validator differs')
            module_spec=importlib.util.spec_from_file_location('installed_identity_'+name,installed);module=importlib.util.module_from_spec(module_spec);module_spec.loader.exec_module(module)
            rows=p.load(HERE/('examples/'+name+'.json'));written_facts=[]
            for i,a in enumerate(rows):
                obj={'recordType':'object','schemaVersion':'1.0.0','recordId':a['id']+':object-r1','objectId':a['id'],'objectType':'vr.wm-xct-036:identity-assertion','name':'Synthetic identity assertion','description':'One assertion; never a Person or a resolution aggregate','recordedAt':at,'previousRecordId':None,'state':'active','provenance':{'source':'urn:synthetic:reference','synthetic':True},'accessClass':'synthetic-private'}
                fact={'recordType':'fact','schemaVersion':'1.0.0','factId':a['id']+':snapshot-r1','subjectId':a['id'],'path':'identity.assertion.snapshot','value':a,'unit':None,'validFrom':a['validFrom'],'validTo':a['validTo'],'recordedAt':at,'supersedes':[],'status':'asserted','provenance':{'source':'urn:synthetic:reference','synthetic':True},'authority':{'source':'urn:synthetic:actor:steward','rank':1},'masterSystem':'urn:synthetic:reference','accessClass':'synthetic-private'}
                for kind,value in [('object',obj),('fact',fact)]:
                    path=root/(name+str(i)+kind+'.json');path.write_bytes(p.encode(value));written=append(target,kind,path)
                    if kind=='fact':written_facts.append(target/written['written'])
            stored=[p.load(x)['value'] for x in written_facts]
            p.require(len(stored)==len(rows),'stored fact count mismatch');module.validate_set(stored,identity_policy)
            v=native_validate(target);p.require(v['valid'],'native V3 failed')
            # Deliberately corrupt an actually stored nested snapshot. V3 should
            # still accept the outer object type, and the companion must reject.
            victim=written_facts[0];raw=victim.read_bytes();bad=p.load(victim);bad['value']['inferencePermitted']=True;victim.write_bytes(p.encode(bad))
            negative_v3=native_validate(target);rejected=False
            try:module.validate(p.load(victim)['value'],identity_policy)
            except module.Invalid:rejected=True
            finally:victim.write_bytes(raw)
            p.require(negative_v3['valid'] and rejected,'expected native/companion distinction not observed')
            v.pop('dimension',None);negative_v3.pop('dimension',None)
            reports.append({'profile':name,'objects':len(rows),'facts':len(stored),'native':v,'companion':'passed on actual stored snapshots','invalidNestedSnapshot':{'native':negative_v3,'companionRejected':rejected},'installedValidatorDigest':c.digest(installed.read_bytes()),'pins':[{'id':r['modelId'],'version':r['version'],'digest':r['specification']['digest'],'mode':r['installationMode']} for r in releases]})
    return {'format':'vercy-identity-profile-acceptance','executedAt':c.now(),'passed':len(reports),'failed':0,'profiles':reports,'limits':'Synthetic new-Dimension assertion snapshots only. Upstream subjects, account ownership, IAM, source truth and existing-Dimension migrations are not tested.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True);args=ap.parse_args();report=run(args.composer,args.skill);Path(args.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':report['passed'],'failed':report['failed']}))

```

## FILE examples/policy.json
```
{
  "format": "vercy-identity-reference-policy",
  "version": "0.1.0",
  "id": "urn:synthetic:policy:identity-v1",
  "dimension": "urn:synthetic:dimension:identity",
  "purpose": "synthetic-identity-review",
  "subjectPrefix": "urn:synthetic:subject:",
  "validFrom": "2025-01-01T00:00:00Z",
  "validTo": "2027-01-01T00:00:00Z",
  "issuers": [
    "urn:synthetic:source:hr",
    "urn:synthetic:source:git-person-map",
    "urn:synthetic:source:tracker-person-map"
  ],
  "relations": [
    "equivalent-in-context",
    "not-same-assertion",
    "probable-entity-match"
  ],
  "actors": [
    {
      "actor": "urn:synthetic:actor:steward",
      "states": [
        "proposed",
        "asserted",
        "disputed",
        "retracted"
      ]
    },
    {
      "actor": "urn:synthetic:actor:importer",
      "states": [
        "proposed"
      ]
    }
  ],
  "readers": [
    "urn:synthetic:actor:steward"
  ]
}

```

## FILE examples/startup.json
```
[
  {
    "format": "vercy-enterprise-identity-assertion",
    "version": "0.1.0",
    "id": "urn:synthetic:assertion:startup-0",
    "dimension": "urn:synthetic:dimension:identity",
    "purpose": "synthetic-identity-review",
    "policyDigest": "sha256:3d67258621a2412be4fea5dc7cdb0cc4d6cbade2ca22d04184f5fc49a1819dce",
    "binding": {
      "assignmentId": "urn:synthetic:assignment:startup-0",
      "scheme": "urn:synthetic:scheme:person-directory",
      "schemeVersion": "1",
      "issuer": "urn:synthetic:source:hr",
      "scope": "urn:synthetic:tenant:startup",
      "value": "E7",
      "comparison": "exact-string",
      "kind": "person",
      "validFrom": "2025-01-01T00:00:00Z",
      "validTo": null,
      "recordedAt": "2025-01-01T00:00:00Z",
      "sourceRecord": "urn:synthetic:evidence:source-startup-0",
      "personalDataClass": "synthetic",
      "credentialProhibition": true
    },
    "target": {
      "id": "urn:synthetic:subject:p1",
      "kind": "person"
    },
    "relation": "equivalent-in-context",
    "validFrom": "2025-01-01T00:00:00Z",
    "validTo": null,
    "inferencePermitted": false,
    "history": [
      {
        "id": "urn:synthetic:event:startup-0:proposed",
        "previousDigest": null,
        "recordedAt": "2025-01-01T00:00:00Z",
        "effectiveAt": "2025-01-01T00:00:00Z",
        "actor": "urn:synthetic:actor:steward",
        "state": "proposed",
        "reason": "Synthetic reviewed linkage; not a real source-system identity claim",
        "evidence": [
          {
            "ref": "urn:synthetic:evidence:source-startup-0",
            "kind": "source-record",
            "description": "Synthetic source export identifies a referent of the declared kind"
          },
          {
            "ref": "urn:synthetic:evidence:review-startup-0",
            "kind": "review-decision",
            "description": "Synthetic steward decision, no authentication claim"
          }
        ]
      },
      {
        "id": "urn:synthetic:event:startup-0:asserted",
        "previousDigest": "sha256:0df295998f3bb1ca99175e4a6f019ac88c75bb25a910c2b2bedde9cdcfc365be",
        "recordedAt": "2025-01-01T00:00:01Z",
        "effectiveAt": "2025-01-01T00:00:00Z",
        "actor": "urn:synthetic:actor:steward",
        "state": "asserted",
        "reason": "Synthetic reviewed linkage; not a real source-system identity claim",
        "evidence": [
          {
            "ref": "urn:synthetic:evidence:source-startup-0",
            "kind": "source-record",
            "description": "Synthetic source export identifies a referent of the declared kind"
          },
          {
            "ref": "urn:synthetic:evidence:review-startup-0",
            "kind": "review-decision",
            "description": "Synthetic steward decision, no authentication claim"
          }
        ]
      }
    ]
  },
  {
    "format": "vercy-enterprise-identity-assertion",
    "version": "0.1.0",
    "id": "urn:synthetic:assertion:startup-1",
    "dimension": "urn:synthetic:dimension:identity",
    "purpose": "synthetic-identity-review",
    "policyDigest": "sha256:3d67258621a2412be4fea5dc7cdb0cc4d6cbade2ca22d04184f5fc49a1819dce",
    "binding": {
      "assignmentId": "urn:synthetic:assignment:startup-1",
      "scheme": "urn:synthetic:scheme:person-directory",
      "schemeVersion": "1",
      "issuer": "urn:synthetic:source:git-person-map",
      "scope": "urn:synthetic:tenant:startup",
      "value": "person-7",
      "comparison": "exact-string",
      "kind": "person",
      "validFrom": "2025-01-01T00:00:00Z",
      "validTo": null,
      "recordedAt": "2025-01-01T00:00:00Z",
      "sourceRecord": "urn:synthetic:evidence:source-startup-1",
      "personalDataClass": "synthetic",
      "credentialProhibition": true
    },
    "target": {
      "id": "urn:synthetic:subject:p1",
      "kind": "person"
    },
    "relation": "equivalent-in-context",
    "validFrom": "2025-01-01T00:00:00Z",
    "validTo": null,
    "inferencePermitted": false,
    "history": [
      {
        "id": "urn:synthetic:event:startup-1:proposed",
        "previousDigest": null,
        "recordedAt": "2025-01-01T00:00:00Z",
        "effectiveAt": "2025-01-01T00:00:00Z",
        "actor": "urn:synthetic:actor:steward",
        "state": "proposed",
        "reason": "Synthetic reviewed linkage; not a real source-system identity claim",
        "evidence": [
          {
            "ref": "urn:synthetic:evidence:source-startup-1",
            "kind": "source-record",
            "description": "Synthetic source export identifies a referent of the declared kind"
          },
          {
            "ref": "urn:synthetic:evidence:review-startup-1",
            "kind": "review-decision",
            "description": "Synthetic steward decision, no authentication claim"
          }
        ]
      },
      {
        "id": "urn:synthetic:event:startup-1:asserted",
        "previousDigest": "sha256:4ce07eb7029ac2bb7a599818439c47c6e7c722f7a04cdc0d2d73b6ed38eba43d",
        "recordedAt": "2025-01-01T00:00:01Z",
        "effectiveAt": "2025-01-01T00:00:00Z",
        "actor": "urn:synthetic:actor:steward",
        "state": "asserted",
        "reason": "Synthetic reviewed linkage; not a real source-system identity claim",
        "evidence": [
          {
            "ref": "urn:synthetic:evidence:source-startup-1",
            "kind": "source-record",
            "description": "Synthetic source export identifies a referent of the declared kind"
          },
          {
            "ref": "urn:synthetic:evidence:review-startup-1",
            "kind": "review-decision",
            "description": "Synthetic steward decision, no authentication claim"
          }
        ]
      }
    ]
  },
  {
    "format": "vercy-enterprise-identity-assertion",
    "version": "0.1.0",
    "id": "urn:synthetic:assertion:startup-2",
    "dimension": "urn:synthetic:dimension:identity",
    "purpose": "synthetic-identity-review",
    "policyDigest": "sha256:3d67258621a2412be4fea5dc7cdb0cc4d6cbade2ca22d04184f5fc49a1819dce",
    "binding": {
      "assignmentId": "urn:synthetic:assignment:startup-2",
      "scheme": "urn:synthetic:scheme:person-directory",
      "schemeVersion": "1",
      "issuer": "urn:synthetic:source:tracker-person-map",
      "scope": "urn:synthetic:tenant:startup",
      "value": "person-reference-7",
      "comparison": "exact-string",
      "kind": "person",
      "validFrom": "2025-01-01T00:00:00Z",
      "validTo": null,
      "recordedAt": "2025-01-01T00:00:00Z",
      "sourceRecord": "urn:synthetic:evidence:source-startup-2",
      "personalDataClass": "synthetic",
      "credentialProhibition": true
    },
    "target": {
      "id": "urn:synthetic:subject:p1",
      "kind": "person"
    },
    "relation": "equivalent-in-context",
    "validFrom": "2025-01-01T00:00:00Z",
    "validTo": null,
    "inferencePermitted": false,
    "history": [
      {
        "id": "urn:synthetic:event:startup-2:proposed",
        "previousDigest": null,
        "recordedAt": "2025-01-01T00:00:00Z",
        "effectiveAt": "2025-01-01T00:00:00Z",
        "actor": "urn:synthetic:actor:steward",
        "state": "proposed",
        "reason": "Synthetic reviewed linkage; not a real source-system identity claim",
        "evidence": [
          {
            "ref": "urn:synthetic:evidence:source-startup-2",
            "kind": "source-record",
            "description": "Synthetic source export identifies a referent of the declared kind"
          },
          {
            "ref": "urn:synthetic:evidence:review-startup-2",
            "kind": "review-decision",
            "description": "Synthetic steward decision, no authentication claim"
          }
        ]
      },
      {
        "id": "urn:synthetic:event:startup-2:asserted",
        "previousDigest": "sha256:22119655ff728dffc128a3603aa00c947395541dd998e1c3114bbb8e70f421af",
        "recordedAt": "2025-01-01T00:00:01Z",
        "effectiveAt": "2025-01-01T00:00:00Z",
        "actor": "urn:synthetic:actor:steward",
        "state": "asserted",
        "reason": "Synthetic reviewed linkage; not a real source-system identity claim",
        "evidence": [
          {
            "ref": "urn:synthetic:evidence:source-startup-2",
            "kind": "source-record",
            "description": "Synthetic source export identifies a referent of the declared kind"
          },
          {
            "ref": "urn:synthetic:evidence:review-startup-2",
            "kind": "review-decision",
            "description": "Synthetic steward decision, no authentication claim"
          }
        ]
      }
    ]
  }
]

```

## FILE examples/group.json
```
[
  {
    "format": "vercy-enterprise-identity-assertion",
    "version": "0.1.0",
    "id": "urn:synthetic:assertion:suba-old",
    "dimension": "urn:synthetic:dimension:identity",
    "purpose": "synthetic-identity-review",
    "policyDigest": "sha256:3d67258621a2412be4fea5dc7cdb0cc4d6cbade2ca22d04184f5fc49a1819dce",
    "binding": {
      "assignmentId": "urn:synthetic:assignment:suba-old",
      "scheme": "urn:synthetic:scheme:person-directory",
      "schemeVersion": "1",
      "issuer": "urn:synthetic:source:hr",
      "scope": "urn:synthetic:tenant:suba",
      "value": "E7",
      "comparison": "exact-string",
      "kind": "person",
      "validFrom": "2025-01-01T00:00:00Z",
      "validTo": "2025-06-01T00:00:00Z",
      "recordedAt": "2025-01-01T00:00:00Z",
      "sourceRecord": "urn:synthetic:evidence:source-suba-old",
      "personalDataClass": "synthetic",
      "credentialProhibition": true
    },
    "target": {
      "id": "urn:synthetic:subject:pa",
      "kind": "person"
    },
    "relation": "equivalent-in-context",
    "validFrom": "2025-01-01T00:00:00Z",
    "validTo": "2025-06-01T00:00:00Z",
    "inferencePermitted": false,
    "history": [
      {
        "id": "urn:synthetic:event:suba-old:proposed",
        "previousDigest": null,
        "recordedAt": "2025-01-01T00:00:00Z",
        "effectiveAt": "2025-01-01T00:00:00Z",
        "actor": "urn:synthetic:actor:steward",
        "state": "proposed",
        "reason": "Synthetic reviewed linkage; not a real source-system identity claim",
        "evidence": [
          {
            "ref": "urn:synthetic:evidence:source-suba-old",
            "kind": "source-record",
            "description": "Synthetic source export identifies a referent of the declared kind"
          },
          {
            "ref": "urn:synthetic:evidence:review-suba-old",
            "kind": "review-decision",
            "description": "Synthetic steward decision, no authentication claim"
          }
        ]
      },
      {
        "id": "urn:synthetic:event:suba-old:asserted",
        "previousDigest": "sha256:1678d4ba7e85d6bfaf3d6665d0ef6ff9b93cc140a4889acefb3da324b695e5f5",
        "recordedAt": "2025-01-01T00:00:01Z",
        "effectiveAt": "2025-01-01T00:00:00Z",
        "actor": "urn:synthetic:actor:steward",
        "state": "asserted",
        "reason": "Synthetic reviewed linkage; not a real source-system identity claim",
        "evidence": [
          {
            "ref": "urn:synthetic:evidence:source-suba-old",
            "kind": "source-record",
            "description": "Synthetic source export identifies a referent of the declared kind"
          },
          {
            "ref": "urn:synthetic:evidence:review-suba-old",
            "kind": "review-decision",
            "description": "Synthetic steward decision, no authentication claim"
          }
        ]
      }
    ]
  },
  {
    "format": "vercy-enterprise-identity-assertion",
    "version": "0.1.0",
    "id": "urn:synthetic:assertion:subb",
    "dimension": "urn:synthetic:dimension:identity",
    "purpose": "synthetic-identity-review",
    "policyDigest": "sha256:3d67258621a2412be4fea5dc7cdb0cc4d6cbade2ca22d04184f5fc49a1819dce",
    "binding": {
      "assignmentId": "urn:synthetic:assignment:subb",
      "scheme": "urn:synthetic:scheme:person-directory",
      "schemeVersion": "1",
      "issuer": "urn:synthetic:source:hr",
      "scope": "urn:synthetic:tenant:subb",
      "value": "E7",
      "comparison": "exact-string",
      "kind": "person",
      "validFrom": "2025-01-01T00:00:00Z",
      "validTo": null,
      "recordedAt": "2025-01-01T00:00:00Z",
      "sourceRecord": "urn:synthetic:evidence:source-subb",
      "personalDataClass": "synthetic",
      "credentialProhibition": true
    },
    "target": {
      "id": "urn:synthetic:subject:pb",
      "kind": "person"
    },
    "relation": "equivalent-in-context",
    "validFrom": "2025-01-01T00:00:00Z",
    "validTo": null,
    "inferencePermitted": false,
    "history": [
      {
        "id": "urn:synthetic:event:subb:proposed",
        "previousDigest": null,
        "recordedAt": "2025-01-01T00:00:00Z",
        "effectiveAt": "2025-01-01T00:00:00Z",
        "actor": "urn:synthetic:actor:steward",
        "state": "proposed",
        "reason": "Synthetic reviewed linkage; not a real source-system identity claim",
        "evidence": [
          {
            "ref": "urn:synthetic:evidence:source-subb",
            "kind": "source-record",
            "description": "Synthetic source export identifies a referent of the declared kind"
          },
          {
            "ref": "urn:synthetic:evidence:review-subb",
            "kind": "review-decision",
            "description": "Synthetic steward decision, no authentication claim"
          }
        ]
      },
      {
        "id": "urn:synthetic:event:subb:asserted",
        "previousDigest": "sha256:a478840a16173b41dbf23c410d6275bc35ed670280d5953375806b26b31968b8",
        "recordedAt": "2025-01-01T00:00:01Z",
        "effectiveAt": "2025-01-01T00:00:00Z",
        "actor": "urn:synthetic:actor:steward",
        "state": "asserted",
        "reason": "Synthetic reviewed linkage; not a real source-system identity claim",
        "evidence": [
          {
            "ref": "urn:synthetic:evidence:source-subb",
            "kind": "source-record",
            "description": "Synthetic source export identifies a referent of the declared kind"
          },
          {
            "ref": "urn:synthetic:evidence:review-subb",
            "kind": "review-decision",
            "description": "Synthetic steward decision, no authentication claim"
          }
        ]
      }
    ]
  },
  {
    "format": "vercy-enterprise-identity-assertion",
    "version": "0.1.0",
    "id": "urn:synthetic:assertion:suba-new",
    "dimension": "urn:synthetic:dimension:identity",
    "purpose": "synthetic-identity-review",
    "policyDigest": "sha256:3d67258621a2412be4fea5dc7cdb0cc4d6cbade2ca22d04184f5fc49a1819dce",
    "binding": {
      "assignmentId": "urn:synthetic:assignment:suba-new",
      "scheme": "urn:synthetic:scheme:person-directory",
      "schemeVersion": "1",
      "issuer": "urn:synthetic:source:hr",
      "scope": "urn:synthetic:tenant:suba",
      "value": "E7",
      "comparison": "exact-string",
      "kind": "person",
      "validFrom": "2025-07-01T00:00:00Z",
      "validTo": null,
      "recordedAt": "2025-07-01T00:00:00Z",
      "sourceRecord": "urn:synthetic:evidence:source-suba-new",
      "personalDataClass": "synthetic",
      "credentialProhibition": true
    },
    "target": {
      "id": "urn:synthetic:subject:pc",
      "kind": "person"
    },
    "relation": "equivalent-in-context",
    "validFrom": "2025-07-01T00:00:00Z",
    "validTo": null,
    "inferencePermitted": false,
    "history": [
      {
        "id": "urn:synthetic:event:suba-new:proposed",
        "previousDigest": null,
        "recordedAt": "2025-07-01T00:00:00Z",
        "effectiveAt": "2025-07-01T00:00:00Z",
        "actor": "urn:synthetic:actor:steward",
        "state": "proposed",
        "reason": "Synthetic reviewed linkage; not a real source-system identity claim",
        "evidence": [
          {
            "ref": "urn:synthetic:evidence:source-suba-new",
            "kind": "source-record",
            "description": "Synthetic source export identifies a referent of the declared kind"
          },
          {
            "ref": "urn:synthetic:evidence:review-suba-new",
            "kind": "review-decision",
            "description": "Synthetic steward decision, no authentication claim"
          }
        ]
      },
      {
        "id": "urn:synthetic:event:suba-new:asserted",
        "previousDigest": "sha256:469b4c0af97b88b2af5e2273bd56296b262ee011723e70d001327fac19f4df72",
        "recordedAt": "2025-07-01T00:00:01Z",
        "effectiveAt": "2025-07-01T00:00:00Z",
        "actor": "urn:synthetic:actor:steward",
        "state": "asserted",
        "reason": "Synthetic reviewed linkage; not a real source-system identity claim",
        "evidence": [
          {
            "ref": "urn:synthetic:evidence:source-suba-new",
            "kind": "source-record",
            "description": "Synthetic source export identifies a referent of the declared kind"
          },
          {
            "ref": "urn:synthetic:evidence:review-suba-new",
            "kind": "review-decision",
            "description": "Synthetic steward decision, no authentication claim"
          }
        ]
      }
    ]
  }
]

```

## FILE examples/ai-team.json
```
[
  {
    "format": "vercy-enterprise-identity-assertion",
    "version": "0.1.0",
    "id": "urn:synthetic:assertion:human",
    "dimension": "urn:synthetic:dimension:identity",
    "purpose": "synthetic-identity-review",
    "policyDigest": "sha256:3d67258621a2412be4fea5dc7cdb0cc4d6cbade2ca22d04184f5fc49a1819dce",
    "binding": {
      "assignmentId": "urn:synthetic:assignment:human",
      "scheme": "urn:synthetic:scheme:person-directory",
      "schemeVersion": "1",
      "issuer": "urn:synthetic:source:hr",
      "scope": "urn:synthetic:tenant:startup",
      "value": "human-ref",
      "comparison": "exact-string",
      "kind": "person",
      "validFrom": "2025-01-01T00:00:00Z",
      "validTo": null,
      "recordedAt": "2025-01-01T00:00:00Z",
      "sourceRecord": "urn:synthetic:evidence:source-human",
      "personalDataClass": "synthetic",
      "credentialProhibition": true
    },
    "target": {
      "id": "urn:synthetic:subject:human",
      "kind": "person"
    },
    "relation": "equivalent-in-context",
    "validFrom": "2025-01-01T00:00:00Z",
    "validTo": null,
    "inferencePermitted": false,
    "history": [
      {
        "id": "urn:synthetic:event:human:proposed",
        "previousDigest": null,
        "recordedAt": "2025-01-01T00:00:00Z",
        "effectiveAt": "2025-01-01T00:00:00Z",
        "actor": "urn:synthetic:actor:steward",
        "state": "proposed",
        "reason": "Synthetic reviewed linkage; not a real source-system identity claim",
        "evidence": [
          {
            "ref": "urn:synthetic:evidence:source-human",
            "kind": "source-record",
            "description": "Synthetic source export identifies a referent of the declared kind"
          },
          {
            "ref": "urn:synthetic:evidence:review-human",
            "kind": "review-decision",
            "description": "Synthetic steward decision, no authentication claim"
          }
        ]
      },
      {
        "id": "urn:synthetic:event:human:asserted",
        "previousDigest": "sha256:453101dc86c87a17022b8fa6c1828638136e8800195dffd70ec54cd92692291b",
        "recordedAt": "2025-01-01T00:00:01Z",
        "effectiveAt": "2025-01-01T00:00:00Z",
        "actor": "urn:synthetic:actor:steward",
        "state": "asserted",
        "reason": "Synthetic reviewed linkage; not a real source-system identity claim",
        "evidence": [
          {
            "ref": "urn:synthetic:evidence:source-human",
            "kind": "source-record",
            "description": "Synthetic source export identifies a referent of the declared kind"
          },
          {
            "ref": "urn:synthetic:evidence:review-human",
            "kind": "review-decision",
            "description": "Synthetic steward decision, no authentication claim"
          }
        ]
      }
    ]
  },
  {
    "format": "vercy-enterprise-identity-assertion",
    "version": "0.1.0",
    "id": "urn:synthetic:assertion:bot",
    "dimension": "urn:synthetic:dimension:identity",
    "purpose": "synthetic-identity-review",
    "policyDigest": "sha256:3d67258621a2412be4fea5dc7cdb0cc4d6cbade2ca22d04184f5fc49a1819dce",
    "binding": {
      "assignmentId": "urn:synthetic:assignment:bot",
      "scheme": "urn:synthetic:scheme:person-directory",
      "schemeVersion": "1",
      "issuer": "urn:synthetic:source:hr",
      "scope": "urn:synthetic:tenant:startup",
      "value": "bot-ref",
      "comparison": "exact-string",
      "kind": "service-account",
      "validFrom": "2025-01-01T00:00:00Z",
      "validTo": null,
      "recordedAt": "2025-01-01T00:00:00Z",
      "sourceRecord": "urn:synthetic:evidence:source-bot",
      "personalDataClass": "synthetic",
      "credentialProhibition": true
    },
    "target": {
      "id": "urn:synthetic:subject:bot",
      "kind": "service-account"
    },
    "relation": "equivalent-in-context",
    "validFrom": "2025-01-01T00:00:00Z",
    "validTo": null,
    "inferencePermitted": false,
    "history": [
      {
        "id": "urn:synthetic:event:bot:proposed",
        "previousDigest": null,
        "recordedAt": "2025-01-01T00:00:00Z",
        "effectiveAt": "2025-01-01T00:00:00Z",
        "actor": "urn:synthetic:actor:steward",
        "state": "proposed",
        "reason": "Synthetic reviewed linkage; not a real source-system identity claim",
        "evidence": [
          {
            "ref": "urn:synthetic:evidence:source-bot",
            "kind": "source-record",
            "description": "Synthetic source export identifies a referent of the declared kind"
          },
          {
            "ref": "urn:synthetic:evidence:review-bot",
            "kind": "review-decision",
            "description": "Synthetic steward decision, no authentication claim"
          }
        ]
      },
      {
        "id": "urn:synthetic:event:bot:asserted",
        "previousDigest": "sha256:07108b0b30581b58acf6b2555e16567e5d3b49e30b3d868ba65ea621e1b1797a",
        "recordedAt": "2025-01-01T00:00:01Z",
        "effectiveAt": "2025-01-01T00:00:00Z",
        "actor": "urn:synthetic:actor:steward",
        "state": "asserted",
        "reason": "Synthetic reviewed linkage; not a real source-system identity claim",
        "evidence": [
          {
            "ref": "urn:synthetic:evidence:source-bot",
            "kind": "source-record",
            "description": "Synthetic source export identifies a referent of the declared kind"
          },
          {
            "ref": "urn:synthetic:evidence:review-bot",
            "kind": "review-decision",
            "description": "Synthetic steward decision, no authentication claim"
          }
        ]
      }
    ]
  }
]

```

## FILE test-results.json
```
{
  "executedAt": "2026-09-21T16:49:58.307974+00:00",
  "tests": 48,
  "passed": true,
  "failures": 0,
  "errors": 0
}

```

## FILE acceptance-results.json
```
{
  "format": "vercy-identity-profile-acceptance",
  "executedAt": "2026-09-21T16:52:28Z",
  "passed": 3,
  "failed": 0,
  "profiles": [
    {
      "profile": "startup",
      "objects": 3,
      "facts": 3,
      "native": {
        "valid": true,
        "conformanceLevel": "V3",
        "schemas": "https://ver.cy/schemas/dimension/1.0/",
        "counts": {
          "objects": 3,
          "facts": 3,
          "relations": 0,
          "events": 0
        },
        "errors": [],
        "warnings": [],
        "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety"
      },
      "companion": "passed on actual stored snapshots",
      "invalidNestedSnapshot": {
        "native": {
          "valid": true,
          "conformanceLevel": "V3",
          "schemas": "https://ver.cy/schemas/dimension/1.0/",
          "counts": {
            "objects": 3,
            "facts": 3,
            "relations": 0,
            "events": 0
          },
          "errors": [],
          "warnings": [],
          "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety"
        },
        "companionRejected": true
      },
      "installedValidatorDigest": "sha256:2ef84efa8a68c97450c9294fa1fddc1bf13882323e9fb9312bfeb28bb1e8a822",
      "pins": [
        {
          "id": "vr.wm-xct-011",
          "version": "0.3.0-research.1",
          "digest": "sha256:aad32a06d60f58191cba4c6675a8d93a49985c91ec5480ca5c05c132725d0834",
          "mode": "semantic-only"
        },
        {
          "id": "vr.wm-xct-036",
          "version": "0.3.0-research.1",
          "digest": "sha256:21fe1b8e3663c00c92ca433f5045581589f7e5b433775b3060d30ecc08c48b17",
          "mode": "native-binding"
        }
      ]
    },
    {
      "profile": "group",
      "objects": 3,
      "facts": 3,
      "native": {
        "valid": true,
        "conformanceLevel": "V3",
        "schemas": "https://ver.cy/schemas/dimension/1.0/",
        "counts": {
          "objects": 3,
          "facts": 3,
          "relations": 0,
          "events": 0
        },
        "errors": [],
        "warnings": [],
        "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety"
      },
      "companion": "passed on actual stored snapshots",
      "invalidNestedSnapshot": {
        "native": {
          "valid": true,
          "conformanceLevel": "V3",
          "schemas": "https://ver.cy/schemas/dimension/1.0/",
          "counts": {
            "objects": 3,
            "facts": 3,
            "relations": 0,
            "events": 0
          },
          "errors": [],
          "warnings": [],
          "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety"
        },
        "companionRejected": true
      },
      "installedValidatorDigest": "sha256:2ef84efa8a68c97450c9294fa1fddc1bf13882323e9fb9312bfeb28bb1e8a822",
      "pins": [
        {
          "id": "vr.wm-xct-011",
          "version": "0.3.0-research.1",
          "digest": "sha256:aad32a06d60f58191cba4c6675a8d93a49985c91ec5480ca5c05c132725d0834",
          "mode": "semantic-only"
        },
        {
          "id": "vr.wm-xct-036",
          "version": "0.3.0-research.1",
          "digest": "sha256:21fe1b8e3663c00c92ca433f5045581589f7e5b433775b3060d30ecc08c48b17",
          "mode": "native-binding"
        }
      ]
    },
    {
      "profile": "ai-team",
      "objects": 2,
      "facts": 2,
      "native": {
        "valid": true,
        "conformanceLevel": "V3",
        "schemas": "https://ver.cy/schemas/dimension/1.0/",
        "counts": {
          "objects": 2,
          "facts": 2,
          "relations": 0,
          "events": 0
        },
        "errors": [],
        "warnings": [],
        "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety"
      },
      "companion": "passed on actual stored snapshots",
      "invalidNestedSnapshot": {
        "native": {
          "valid": true,
          "conformanceLevel": "V3",
          "schemas": "https://ver.cy/schemas/dimension/1.0/",
          "counts": {
            "objects": 2,
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
      "installedValidatorDigest": "sha256:2ef84efa8a68c97450c9294fa1fddc1bf13882323e9fb9312bfeb28bb1e8a822",
      "pins": [
        {
          "id": "vr.wm-xct-011",
          "version": "0.3.0-research.1",
          "digest": "sha256:aad32a06d60f58191cba4c6675a8d93a49985c91ec5480ca5c05c132725d0834",
          "mode": "semantic-only"
        },
        {
          "id": "vr.wm-xct-036",
          "version": "0.3.0-research.1",
          "digest": "sha256:21fe1b8e3663c00c92ca433f5045581589f7e5b433775b3060d30ecc08c48b17",
          "mode": "native-binding"
        }
      ]
    }
  ],
  "limits": "Synthetic new-Dimension assertion snapshots only. Upstream subjects, account ownership, IAM, source truth and existing-Dimension migrations are not tested."
}

```

## EXACT SELECTED PARENT DEFINITIONS
{
  "wm-xct-011-identifier-scheme": [
    {
      "bundle": "assignment-and-lifecycle",
      "layer": "assignment-act-and-binding",
      "finding": {
        "id": "identifier-assignment-record",
        "name": "Assignment record: referent binding, assigner, evidence and period",
        "description": "The assignment is the atomic fact this model exists to support. The FHIR Identifier datatype gives the minimal shape a consumer needs: a system establishing the namespace, a value unique within it, an optional coded type, a use marker that modifies interpretation, a validity period and an assigner. DataCite shows that a registration agency may impose mandatory descriptive metadata as a condition of assignment. RFC 8141 requires the assignment mechanism and its uniqueness method to be specified. Event time and record time must be kept apart: when the binding took effect is not when the register learned of it.",
        "source_refs": [
          "SRC-013",
          "SRC-015",
          "SRC-001",
          "SRC-021",
          "SRC-014"
        ],
        "questions": [
          {
            "id": "q-assignment-referent",
            "text": "Which referent is bound by this assignment, and how is that referent itself identified?",
            "kind": "identity",
            "answer_data": [
              "Referent reference with its own identifier and scheme",
              "Referent class",
              "Statement of whether the binding is exclusive to one referent"
            ]
          },
          {
            "id": "q-assignment-assigner",
            "text": "Who performed the assignment, under which delegated authority?",
            "kind": "authority",
            "answer_data": [
              "Assigner reference",
              "Delegated namespace portion used",
              "Authorisation basis"
            ]
          },
          {
            "id": "q-assignment-time",
            "text": "When did the assignment take effect, and when was it recorded?",
            "kind": "temporal",
            "answer_data": [
              "Assignment effective time in RFC 3339",
              "Record or ingestion time in RFC 3339",
              "Reason for any gap between the two"
            ]
          },
          {
            "id": "q-assignment-evidence",
            "text": "What evidence supports that the referent is what the registrant claims it to be?",
            "kind": "evidence",
            "answer_data": [
              "Evidence artefacts referenced",
              "Verification level applied",
              "Party that performed verification"
            ]
          },
          {
            "id": "q-assignment-obligations",
            "text": "What metadata or conduct obligations does the registrant accept as a condition of assignment?",
            "kind": "requirement",
            "answer_data": [
              "Mandatory metadata properties",
              "Update and renewal duties",
              "Consequence of non-compliance"
            ]
          },
          {
            "id": "q-assignment-use",
            "text": "What is the intended use of this identifier relative to any others held by the same referent?",
            "kind": "classification",
            "answer_data": [
              "Use marker such as official, usual, secondary, temporary or old",
              "Coded identifier type",
              "Validity period"
            ]
          }
        ],
        "data_elements": [
          {
            "id": "de-identifier-value",
            "name": "Identifier value",
            "description": "The identifier string bound to the referent, unique within its namespace.",
            "value_kind": "identifier",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-013",
              "SRC-001"
            ]
          },
          {
            "id": "de-identifier-system",
            "name": "Identifier system",
            "description": "Absolute namespace URI or equivalent token establishing where the value is unique.",
            "value_kind": "identifier",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-013"
            ]
          },
          {
            "id": "de-referent-ref",
            "name": "Referent reference",
            "description": "Reference to the thing the identifier denotes.",
            "value_kind": "reference",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-013",
              "SRC-015"
            ]
          },
          {
            "id": "de-assigner-ref",
            "name": "Assigner reference",
            "description": "Organization or unit that issued or manages the identifier.",
            "value_kind": "reference",
            "cardinality": "0..1",
            "required": false,
            "source_refs": [
              "SRC-013",
              "SRC-014"
            ]
          },
          {
            "id": "de-identifier-use",
            "name": "Identifier use marker",
            "description": "Coded purpose of this identifier for its referent; interpretation-modifying.",
            "value_kind": "code",
            "cardinality": "0..1",
            "required": false,
            "source_refs": [
              "SRC-013"
            ]
          },
          {
            "id": "de-assignment-effective-time",
            "name": "Assignment effective time",
            "description": "Time from which the binding is in force.",
            "value_kind": "timestamp",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-013",
              "SRC-015"
            ]
          },
          {
            "id": "de-assignment-recorded-time",
            "name": "Assignment record time",
            "description": "Time at which the register observed or ingested the assignment.",
            "value_kind": "timestamp",
            "cardinality": "0..1",
            "required": false,
            "source_refs": [
              "SRC-003"
            ]
          },
          {
            "id": "de-assignment-evidence-ref",
            "name": "Assignment evidence reference",
            "description": "Reference to evidence supporting the referent's claim.",
            "value_kind": "reference",
            "cardinality": "0..n",
            "required": false,
            "source_refs": [
              "SRC-014",
              "SRC-001"
            ]
          },
          {
            "id": "de-assignment-validity-period",
            "name": "Identifier validity period",
            "description": "Period during which the identifier is or was valid for use.",
            "value_kind": "object",
            "cardinality": "0..1",
            "required": false,
            "source_refs": [
              "SRC-013"
            ]
          }
        ],
        "artifacts": [
          {
            "id": "assignment-register",
            "name": "Assignment register",
            "description": "The authoritative register of bindings between identifiers and referents, with assigner, effective and record times, evidence and obligatory metadata.",
            "media_or_form": [
              "authoritative register",
              "tabular dataset",
              "structured record set"
            ],
            "serial": false,
            "identity_strategy": "Namespace expression plus canonical identifier value as the natural key of each entry; the register itself is keyed by scheme registry key.",
            "source_refs": [
              "SRC-013",
              "SRC-014",
              "SRC-015"
            ]
          },
          {
            "id": "registration-metadata-record",
            "name": "Registration metadata record",
            "description": "The descriptive metadata a registration agency requires as a condition of assignment, including any alternate identifiers held by the same referent.",
            "media_or_form": [
              "structured metadata record"
            ],
            "serial": false,
            "identity_strategy": "The assigned identifier itself is the record key; version by RFC 3339 revision timestamp.",
            "source_refs": [
              "SRC-015"
            ]
          }
        ],
        "inline_only_rationale": null
      }
    },
    {
      "bundle": "assignment-and-lifecycle",
      "layer": "assignment-act-and-binding",
      "finding": {
        "id": "granularity-qualifiers-and-notations",
        "name": "Granularity, qualifiers and notations",
        "description": "ISO 26324 and ISO 24619 require explicit granularity. ARK qualifiers identify parts and variants. SKOS notations are lexical codes unique within a concept scheme and are not a substitute for URIs. Fragments and f-components identify constituents without changing the assigned name.",
        "source_refs": [
          "SRC-026",
          "SRC-029",
          "SRC-032",
          "SRC-011",
          "SRC-001"
        ],
        "questions": [
          {
            "id": "granularity-qualifiers-and-notations-q01",
            "text": "At what granularity is the identifier defined, and may finer parts be addressed by qualifiers or fragments rather than new assignments?",
            "kind": "composition",
            "answer_data": [
              "granularityLevel",
              "qualifierSyntax",
              "fragmentSemantics"
            ]
          },
          {
            "id": "granularity-qualifiers-and-notations-q02",
            "text": "If a notation or code is used, is it unique only within a concept scheme, and what URI or URN is the preferred computational identifier?",
            "kind": "interoperability",
            "answer_data": [
              "notationValue",
              "conceptSchemeRef",
              "preferredUri"
            ]
          },
          {
            "id": "granularity-qualifiers-and-notations-q03",
            "text": "Do content-negotiated, language, format or version variants share the assigned name or require distinct identifiers?",
            "kind": "classification",
            "answer_data": [
              "variantPolicy",
              "contentNegotiationFlag",
              "versionedIdPolicy"
            ]
          }
        ],
        "data_elements": [
          {
            "id": "granularity-qualifiers-and-notations-data01",
            "name": "Granularity level",
            "description": "Stated grain of the identified object.",
            "value_kind": "text",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-026",
              "SRC-029"
            ]
          },
          {
            "id": "granularity-qualifiers-and-notations-data02",
            "name": "Qualifier syntax",
            "description": "Rules for parts, variants or fragments.",
            "value_kind": "text",
            "cardinality": "0..1",
            "required": false,
            "source_refs": [
              "SRC-032",
              "SRC-001"
            ]
          },
          {
            "id": "granularity-qualifiers-and-notations-data03",
            "name": "Notation",
            "description": "Lexical code unique within a scheme, if any.",
            "value_kind": "text",
            "cardinality": "0..n",
            "required": false,
            "source_refs": [
              "SRC-011"
            ]
          }
        ],
        "artifacts": [],
        "inline_only_rationale": "Granularity and qualifier rules are constraints of the scheme definition and assignment record; they are expressed inline unless the scheme publishes a separate qualifier profile."
      }
    }
  ],
  "wm-xct-036-alias-same-as-mapping": [
    {
      "bundle": "als-tax-relation-semantics",
      "layer": "als-tax-kind-catalogue",
      "finding": {
        "id": "als-tax-kind-register",
        "name": "Governed register of mutually exclusive relation kinds",
        "description": "WM-XCT-036 recognises nine relation kinds, each with a normative definition and a discriminating test that separates it from its nearest neighbour: identifier-alias, where two identifiers designate the same subject within a declared identifier system; historical-identifier, a former identifier superseded by a current one for the same subject; referent-replacement, where the source resource or record is supplanted by a replacement that may be a different subject after a merge; exact-semantic-match, where terms are interchangeable across a wide range of retrieval applications; close-match, where terms are interchangeable in some applications only; equivalent-in-context, where equivalence is asserted only inside a declared context and is void outside it; probable-entity-match, an evidence-weighted, non-asserted hypothesis that two records denote one entity; not-same-assertion, an explicit negative claim; and strict-identity, a formal claim that both endpoints denote one and the same individual. Exactly one kind is assigned per assertion. Register status, effective interval and successor are held per kind so that retirement of a kind is itself governed.",
        "source_refs": [
          "SRC-018",
          "SRC-020",
          "SRC-022",
          "SRC-026",
          "SRC-027",
          "SRC-029"
        ],
        "questions": [
          {
            "id": "als-tax-q-kind-definition",
            "text": "Which relation kind in the register exactly matches the claim being made, and what is that kind's normative definition?",
            "kind": "definition",
            "answer_data": [
              "relation_kind_code",
              "normative definition text",
              "register release in force"
            ]
          },
          {
            "id": "als-tax-q-kind-discriminator",
            "text": "What discriminating test separates the selected relation kind from the adjacent kind that would otherwise be chosen?",
            "kind": "classification",
            "answer_data": [
              "adjacent kind code",
              "discriminating test statement",
              "outcome of the test for this assertion"
            ]
          },
          {
            "id": "als-tax-q-kind-authority",
            "text": "Which role is authorised to add, amend or retire a relation kind in the register, and under which decision record?",
            "kind": "authority",
            "answer_data": [
              "authorising role identifier",
              "decision record reference",
              "effective register release"
            ]
          },
          {
            "id": "als-tax-q-kind-exclusivity",
            "text": "Is exactly one relation kind carried on this assertion, and how is a multi-kind or blended claim rejected?",
            "kind": "constraint",
            "answer_data": [
              "assigned kind count",
              "exclusivity rule reference",
              "rejection outcome code"
            ]
          },
          {
            "id": "als-tax-q-kind-status",
            "text": "What is the register status of the relation kind, and if it is deprecated which successor kind replaces it?",
            "kind": "lifecycle",
            "answer_data": [
              "register status value",
              "deprecation effective timestamp",
              "successor kind code"
            ]
          }
        ],
        "data_elements": [
          {
            "id": "als-tax-de-relation-kind-code",
            "name": "relation_kind_code",
            "description": "Controlled code identifying exactly one relation kind from the governed register.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-020",
              "SRC-028"
            ]
          },
          {
            "id": "als-tax-de-kind-definition",
            "name": "kind_normative_definition",
            "description": "The normative definition text of the relation kind as published in the register release in force.",
            "value_kind": "text",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-018",
              "SRC-020"
            ]
          },
          {
            "id": "als-tax-de-kind-discriminator",
            "name": "kind_discriminating_test",
            "description": "Stated test that distinguishes this kind from its nearest neighbouring kinds, expressed so that a wrong assignment is detectable.",
            "value_kind": "text",
            "cardinality": "1..n",
            "required": true,
            "source_refs": [
              "SRC-020",
              "SRC-022"
            ]
          },
          {
            "id": "als-tax-de-kind-status",
            "name": "kind_register_status",
            "description": "Governed status of the relation kind: proposed, active, deprecated or withdrawn.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-026",
              "SRC-016"
            ]
          },
          {
            "id": "als-tax-de-kind-successor",
            "name": "kind_successor_code",
            "description": "Relation kind that replaces a deprecated kind; absent while the kind is active.",
            "value_kind": "reference",
            "cardinality": "0..1",
            "required": false,
            "source_refs": [
              "SRC-026"
            ]
          }
        ],
        "artifacts": [
          {
            "id": "als-tax-kind-register-doc",
            "name": "Relation Kind Register",
            "description": "The published, versioned register of relation kinds carrying for each kind its code, normative definition, discriminating tests, register status, effective interval and successor. It is a declarative catalogue; nothing in it evaluates or enforces an assertion.",
            "media_or_form": [
              "controlled register",
              "versioned tabular release",
              "structured record set"
            ],
            "serial": true,
            "identity_strategy": "Register entries are keyed by the authoritative master-system relation-kind code issued by the register owner; a governed IRI is minted per kind within the adopting Dimension namespace; a ULID is assigned to a register release only where the master system issues no release identifier.",
            "source_refs": [
              "SRC-020",
              "SRC-016",
              "SRC-026"
            ]
          }
        ],
        "inline_only_rationale": null
      }
    },
    {
      "bundle": "als-tax-relation-semantics",
      "layer": "als-tax-kind-catalogue",
      "finding": {
        "id": "als-tax-projection-crosswalk",
        "name": "Versioned alignment bindings to external vocabularies",
        "description": "Each relation kind carries zero or more bindings to external terms, declared as alignments with an explicit comparability verdict (narrower, broader, equivalent-as-used or incomparable) and the dated edition the binding was read from. Representative bindings: strict-identity to owl:sameAs and SameIndividual; not-same-assertion to owl:differentFrom, DifferentIndividuals and the SSSOM predicate modifier that negates a predicate; exact-semantic-match to skos:exactMatch; close-match to skos:closeMatch; referent-replacement to dcterms:isReplacedBy, to HTTP 301 and 308 responses and to FHIR Patient.link replaced-by; identifier-alias to database secondary keys and to the registered alternate relation; representation preference to rel=canonical and the registered duplicate relation; probable-entity-match to Wikidata P460 with SSSOM confidence and justification. Bindings never assert conformance and never import the target's operational behaviour.",
        "source_refs": [
          "SRC-018",
          "SRC-020",
          "SRC-023",
          "SRC-024",
          "SRC-016",
          "SRC-025",
          "SRC-026",
          "SRC-027",
          "SRC-028",
          "SRC-029"
        ],
        "questions": [
          {
            "id": "als-tax-q-binding-target",
            "text": "Which external vocabulary term is this relation kind bound to, and is the binding recorded as an alignment rather than a conformance claim?",
            "kind": "interoperability",
            "answer_data": [
              "external term IRI or registered token",
              "binding declaration type",
              "alignment statement text"
            ]
          },
          {
            "id": "als-tax-q-binding-comparability",
            "text": "Is the external term narrower than, broader than, equivalent-as-used to, or incomparable with the local relation kind?",
            "kind": "relationship",
            "answer_data": [
              "comparability verdict code",
              "justification note",
              "known divergence list"
            ]
          },
          {
            "id": "als-tax-q-binding-edition",
            "text": "Which dated edition or release of the external vocabulary was the binding taken from, and when was it last reconfirmed?",
            "kind": "provenance",
            "answer_data": [
              "external specification version or date",
              "binding author reference",
              "reconfirmation timestamp"
            ]
          },
          {
            "id": "als-tax-q-binding-evidence",
            "text": "What documented statement in the external specification supports the asserted binding strength?",
            "kind": "evidence",
            "answer_data": [
              "cited clause or axiom reference",
              "specification section identifier",
              "evidence sufficiency verdict"
            ]
          }
        ],
        "data_elements": [
          {
            "id": "als-tax-de-binding-term",
            "name": "external_term_reference",
            "description": "IRI or registered token of the external vocabulary term bound to the local relation kind.",
            "value_kind": "identifier",
            "cardinality": "0..n",
            "required": false,
            "source_refs": [
              "SRC-018",
              "SRC-020",
              "SRC-016"
            ]
          },
          {
            "id": "als-tax-de-binding-comparability",
            "name": "binding_comparability",
            "description": "Verdict on how the external term compares with the local kind: narrower, broader, equivalent-as-used or incomparable.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-020",
              "SRC-025"
            ]
          },
          {
            "id": "als-tax-de-binding-edition",
            "name": "external_specification_edition",
            "description": "Dated edition, version or registry snapshot of the external vocabulary from which the binding was read.",
            "value_kind": "text",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-016",
              "SRC-028"
            ]
          },
          {
            "id": "als-tax-de-binding-clause",
            "name": "binding_evidence_clause",
            "description": "Reference to the specific clause, axiom or registry row in the external specification that supports the binding.",
            "value_kind": "reference",
            "cardinality": "1..n",
            "required": true,
            "source_refs": [
              "SRC-019",
              "SRC-020",
              "SRC-024"
            ]
          }
        ],
        "artifacts": [
          {
            "id": "als-tax-crosswalk-table",
            "name": "Relation Kind Projection Crosswalk",
            "description": "Published crosswalk from each local relation kind to external vocabulary terms, carrying the comparability verdict, the dated external edition, the supporting clause reference and recorded divergences. It documents alignment only and confers no conformance.",
            "media_or_form": [
              "crosswalk table",
              "versioned mapping release",
              "structured record set"
            ],
            "serial": true,
            "identity_strategy": "Each crosswalk row is keyed by the authoritative master-system pair of relation-kind code and external term identifier; a governed IRI is minted per crosswalk release; a ULID is used only when no master-system release identifier is available.",
            "source_refs": [
              "SRC-020",
              "SRC-016",
              "SRC-028"
            ]
          }
        ],
        "inline_only_rationale": null
      }
    },
    {
      "bundle": "als-tax-relation-semantics",
      "layer": "als-tax-formal-properties",
      "finding": {
        "id": "als-tax-property-profile",
        "name": "Per-kind directionality, symmetry, reflexivity, transitivity and invertibility",
        "description": "Every relation kind carries a property profile with four-valued property states (asserted, denied, not-asserted-by-source, not-applicable) so that silence in a source vocabulary is never recorded as a negative. Grounded profile examples: strict-identity is non-directional, symmetric, reflexive and transitive because the axiom is satisfied only when the named individuals map to the identical domain element; exact-semantic-match is symmetric and transitive under SKOS S44 and S45, with reflexivity not asserted by the source; close-match is symmetric under S44 but transitivity is deliberately withheld to prevent compound error, so it is recorded as denied rather than unstated; not-same-assertion is symmetric and irreflexive and is not transitive; referent-replacement and historical-identifier are directional and invertible through a declared inverse and are asserted as single hops, never as a chain closure; probable-entity-match is symmetric, consistent with the deployed symmetric said-to-be-the-same-as property, and its transitivity is denied.",
        "source_refs": [
          "SRC-019",
          "SRC-020",
          "SRC-023",
          "SRC-006",
          "SRC-026",
          "SRC-029"
        ],
        "questions": [
          {
            "id": "als-tax-q-prop-symmetry",
            "text": "Is symmetry or reflexivity asserted for this relation kind by its source vocabulary, denied, or simply left unstated?",
            "kind": "constraint",
            "answer_data": [
              "symmetry state four-valued code",
              "reflexivity state four-valued code",
              "source clause reference"
            ]
          },
          {
            "id": "als-tax-q-prop-transitivity",
            "text": "Is transitivity asserted, explicitly withheld, or unstated, and does the kind have a named inverse relation?",
            "kind": "relationship",
            "answer_data": [
              "transitivity state four-valued code",
              "inverse relation kind code",
              "withholding rationale text"
            ]
          },
          {
            "id": "als-tax-q-prop-direction",
            "text": "For a directional kind, which endpoint is the subject and which is the object, and what does reversing them change?",
            "kind": "identity",
            "answer_data": [
              "directionality code",
              "subject endpoint role",
              "object endpoint role",
              "reversal semantics note"
            ]
          },
          {
            "id": "als-tax-q-prop-inference",
            "text": "Is inference permitted from this relation kind, and which externally owned entailment regime would perform it?",
            "kind": "decision",
            "answer_data": [
              "inference permitted flag",
              "named entailment regime reference",
              "owning system reference"
            ]
          }
        ],
        "data_elements": [
          {
            "id": "als-tax-de-directionality",
            "name": "directionality",
            "description": "Whether the relation kind is directional with distinct subject and object roles, or non-directional.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-006",
              "SRC-026"
            ]
          },
          {
            "id": "als-tax-de-symmetry-state",
            "name": "symmetry_state",
            "description": "Four-valued symmetry declaration: asserted, denied, not-asserted-by-source or not-applicable.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-020",
              "SRC-029"
            ]
          },
          {
            "id": "als-tax-de-reflexivity-state",
            "name": "reflexivity_state",
            "description": "Four-valued reflexivity declaration; strict-identity is asserted reflexive, not-same-assertion is irreflexive, SKOS matches are not asserted by source.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-019",
              "SRC-020"
            ]
          },
          {
            "id": "als-tax-de-transitivity-state",
            "name": "transitivity_state",
            "description": "Four-valued transitivity declaration; close-match is denied, exact-semantic-match and strict-identity are asserted.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-019",
              "SRC-020"
            ]
          },
          {
            "id": "als-tax-de-inverse-kind",
            "name": "inverse_relation_kind",
            "description": "Relation kind that expresses the inverse reading of a directional kind, where one exists.",
            "value_kind": "reference",
            "cardinality": "0..1",
            "required": false,
            "source_refs": [
              "SRC-020",
              "SRC-026"
            ]
          }
        ],
        "artifacts": [
          {
            "id": "als-tax-property-matrix",
            "name": "Relation Property Matrix",
            "description": "Matrix of relation kinds against directionality, symmetry, reflexivity, transitivity, invertibility, inference permission and the supporting source clause. It is a declaration surface only; it does not compute or materialise any closure.",
            "media_or_form": [
              "matrix table",
              "structured record set"
            ],
            "serial": false,
            "identity_strategy": "Keyed by the authoritative master-system relation-kind code plus the identifier of the register release it was generated against; no separate serial number is issued, and a UUID is assigned only if that register release lacks a master-system identifier.",
            "source_refs": [
              "SRC-019",
              "SRC-020",
              "SRC-006"
            ]
          }
        ],
        "inline_only_rationale": null
      }
    },
    {
      "bundle": "als-tax-relation-semantics",
      "layer": "als-tax-formal-properties",
      "finding": {
        "id": "als-tax-strength-inference",
        "name": "Ordinal semantic strength and inference permission",
        "description": "Each relation kind carries an ordinal strength rank on a single declared scale, from a non-asserted hypothesis (probable-entity-match), through scoped or retrieval-level interchangeability (close-match, equivalent-in-context, exact-semantic-match), through system-scoped designation (identifier-alias, historical-identifier, referent-replacement), to a maximal formal identity claim (strict-identity), with explicit negation (not-same-assertion) held on its own high-strength negative rank. Strength is a declared attribute of the kind, not a computed similarity score; a confidence value in the interval 0 to 1 may accompany an assertion but never upgrades its rank. The inference-permission flag states whether substitution or entailment is allowed at all, and any permitted inference is executed by an externally owned regime. Published analysis that identity behaves as a scale rather than a binary supports the ordinal treatment, while OWL semantics fix the maximal rank.",
        "source_refs": [
          "SRC-019",
          "SRC-020",
          "SRC-028",
          "SRC-029",
          "SRC-030"
        ],
        "questions": [
          {
            "id": "als-tax-q-strength-rank",
            "text": "What ordinal semantic-strength rank does this relation kind carry on the declared scale, and what is the scale's top rank?",
            "kind": "measurement",
            "answer_data": [
              "strength rank ordinal value",
              "scale definition reference",
              "top rank kind code"
            ]
          },
          {
            "id": "als-tax-q-strength-prohibited",
            "text": "Which downstream operations are prohibited at this strength rank without a higher-ranked assertion?",
            "kind": "constraint",
            "answer_data": [
              "prohibited operation list",
              "minimum rank required per operation",
              "rule reference"
            ]
          },
          {
            "id": "als-tax-q-strength-exception",
            "text": "Under what recorded exception may a lower-strength assertion be consumed as if it were stronger, and who authorises that exception?",
            "kind": "exception",
            "answer_data": [
              "exception record identifier",
              "authorising role",
              "exception validity interval",
              "scope limitation"
            ]
          },
          {
            "id": "als-tax-q-strength-confidence",
            "text": "Does a confidence value accompany this assertion, and is it prevented from altering the declared strength rank?",
            "kind": "decision",
            "answer_data": [
              "confidence value between 0 and 1",
              "confidence method reference",
              "rank immutability rule reference"
            ]
          }
        ],
        "data_elements": [
          {
            "id": "als-tax-de-strength-rank",
            "name": "strength_rank",
            "description": "Ordinal rank of the relation kind on the declared semantic-strength scale.",
            "value_kind": "number",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-020",
              "SRC-030"
            ]
          },
          {
            "id": "als-tax-de-inference-permitted",
            "name": "inference_permitted",
            "description": "Declared flag stating whether any inference or substitution may be drawn from the relation kind; execution belongs to an external regime.",
            "value_kind": "boolean",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-019",
              "SRC-030"
            ]
          },
          {
            "id": "als-tax-de-confidence",
            "name": "confidence_value",
            "description": "Optional confidence in the interval 0 to 1 supplied by the asserting party, where 1 indicates full confidence.",
            "value_kind": "number",
            "cardinality": "0..1",
            "required": false,
            "source_refs": [
              "SRC-028",
              "SRC-029"
            ]
          },
          {
            "id": "als-tax-de-justification-category",
            "name": "justification_category",
            "description": "Controlled category describing how the assertion was justified, for example lexical, logical, human-curated or similarity-based.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-028",
              "SRC-029"
            ]
          }
        ],
        "artifacts": [],
        "inline_only_rationale": "Strength rank, inference permission, confidence and justification category are scalar attributes carried on the relation-kind register entry and on the individual assertion record. Publishing them as a separate artifact would duplicate the register and create a second place where the ordinal scale could drift. The scale definition itself is a short inline declaration held with the register release, and the reasoning regime that would act on the inference flag is owned outside this model, so there is nothing further to materialise here."
      }
    },
    {
      "bundle": "als-tax-relation-semantics",
      "layer": "als-tax-subject-planes",
      "finding": {
        "id": "als-tax-endpoint-scope",
        "name": "Admissible endpoint types and contextual scope of an assertion",
        "description": "Each relation kind declares which endpoint types it admits and the scope inside which the assertion holds. SKOS mapping properties are conventionally used between concepts in different concept schemes, so a semantic match asserted inside a single scheme is flagged. Identifier alias holds only within its declared identifier system or systems. Equivalent-in-context requires a named context such as jurisdiction, purpose, dataset or time window and is void outside it. Representation-level relations hold between a context IRI and a target IRI in the sense of the web-linking model. Strict identity admits only endpoints that denote individuals in a shared domain of discourse. Each assertion also declares a validity interval and what is recorded when an endpoint cannot be resolved, without this model attempting resolution.",
        "source_refs": [
          "SRC-020",
          "SRC-021",
          "SRC-022",
          "SRC-006",
          "SRC-028"
        ],
        "questions": [
          {
            "id": "als-tax-q-endpoint-types",
            "text": "Which endpoint entity types are admissible for the selected relation kind, and does each endpoint satisfy them?",
            "kind": "constraint",
            "answer_data": [
              "admissible endpoint type list",
              "subject type code",
              "object type code",
              "admissibility verdict"
            ]
          },
          {
            "id": "als-tax-q-scope-interval",
            "text": "Over which validity interval and named context does this equivalence hold, and when does it lapse?",
            "kind": "temporal",
            "answer_data": [
              "context identifier",
              "valid from timestamp",
              "valid to timestamp",
              "lapse condition"
            ]
          },
          {
            "id": "als-tax-q-endpoint-authority",
            "text": "Which authority owns each endpoint, and is a cross-authority assertion permitted for this relation kind?",
            "kind": "ownership",
            "answer_data": [
              "subject owning authority",
              "object owning authority",
              "cross-authority permission verdict"
            ]
          },
          {
            "id": "als-tax-q-endpoint-unresolvable",
            "text": "What is recorded when an endpoint reference cannot be resolved at the time the assertion is made?",
            "kind": "state",
            "answer_data": [
              "endpoint resolution state code",
              "observation timestamp",
              "referral target for resolution"
            ]
          }
        ],
        "data_elements": [
          {
            "id": "als-tax-de-subject-type",
            "name": "subject_type",
            "description": "Declared type of the subject endpoint, for example ontology class, SKOS concept, named individual, record or identifier token.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-028",
              "SRC-020"
            ]
          },
          {
            "id": "als-tax-de-object-type",
            "name": "object_type",
            "description": "Declared type of the object endpoint, drawn from the same controlled list as subject_type.",
            "value_kind": "code",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-028",
              "SRC-020"
            ]
          },
          {
            "id": "als-tax-de-context-scope",
            "name": "context_scope_reference",
            "description": "Named context, such as a jurisdiction, purpose, dataset or scheme pair, inside which an equivalent-in-context or otherwise scoped assertion holds.",
            "value_kind": "reference",
            "cardinality": "0..1",
            "required": false,
            "source_refs": [
              "SRC-020",
              "SRC-030"
            ]
          },
          {
            "id": "als-tax-de-validity-interval",
            "name": "assertion_validity_interval",
            "description": "Interval during which the assertion is claimed to hold, expressed as RFC 3339 start and end instants with seconds and explicit offset.",
            "value_kind": "duration",
            "cardinality": "0..1",
            "required": false,
            "source_refs": [
              "SRC-023",
              "SRC-029"
            ]
          },
          {
            "id": "als-tax-de-endpoint-resolution-state",
            "name": "endpoint_resolution_state",
            "description": "Recorded state of each endpoint reference at assertion time: resolved, unresolvable or not-checked; this model records the state and does not perform resolution.",
            "value_kind": "code",
            "cardinality": "1..n",
            "required": true,
            "source_refs": [
              "SRC-021",
              "SRC-023"
            ]
          }
        ],
        "artifacts": [],
        "inline_only_rationale": "Endpoint typing and contextual scope are inline attributes of an individual assertion, and the admissible-type lists live as columns on the relation-kind register rather than as a separate deliverable. Producing an artifact here would require holding endpoint inventories or resolution results, which belong to the endpoint-owning and resolution models and are explicitly outside this model's boundary."
      }
    },
    {
      "bundle": "als-tax-assertion-integrity",
      "layer": "als-tax-consistency-layer",
      "finding": {
        "id": "als-tax-conflict-change",
        "name": "Invalid combinations, cycles, contradictions and strength change control",
        "description": "Declarative integrity rules over sets of assertions. Contradiction: the same endpoint pair on the same plane and context may not carry both strict-identity and explicit not-same. Disjointness carried from SKOS: an exact match is disjoint with broad match and related match, so those combinations are invalid. Plane contradiction: strict identity on the entity plane conflicts with a referent-replacement assertion that treats the endpoints as distinct successive referents. Cycles: replacement and historical-identifier chains must be acyclic and must terminate in a current endpoint; a closed cycle is recorded as a defect for referral, not silently broken. Cardinality: strict identity on the entity plane implies a one-to-one pairing, while probable-entity-match may stand at many-to-many pending adjudication elsewhere. Change control: any change of relation kind is a new classification carrying the prior kind, the reason, the authorising role and effective and observation timestamps; upgrade to the top strength rank additionally requires an authority declaration and an evidence reference, and downgrade must preserve the superseded classification rather than overwrite it. Detection, adjudication and enforcement of these rules are performed by services outside this model.",
        "source_refs": [
          "SRC-018",
          "SRC-020",
          "SRC-026",
          "SRC-027",
          "SRC-028",
          "SRC-029"
        ],
        "questions": [
          {
            "id": "als-tax-q-conflict-pairs",
            "text": "Which relation-kind combinations are declared mutually invalid for the same endpoint pair, plane and context?",
            "kind": "validation",
            "answer_data": [
              "invalid combination rule identifier",
              "conflicting kind codes",
              "source clause reference"
            ]
          },
          {
            "id": "als-tax-q-change-record",
            "text": "What must be recorded when an assertion's relation kind is downgraded or upgraded?",
            "kind": "lifecycle",
            "answer_data": [
              "prior kind code",
              "new kind code",
              "change reason code",
              "authorising role",
              "superseded classification reference"
            ]
          },
          {
            "id": "als-tax-q-change-timing",
            "text": "Which effective interval and observation timestamp distinguish a superseded classification from the current one?",
            "kind": "temporal",
            "answer_data": [
              "effective from timestamp",
              "effective to timestamp",
              "observation timestamp"
            ]
          },
          {
            "id": "als-tax-q-cycle-handling",
            "text": "How is a replacement or historical-identifier chain handled when it closes on itself?",
            "kind": "exception",
            "answer_data": [
              "cycle defect record identifier",
              "chain member list",
              "referral target for adjudication"
            ]
          },
          {
            "id": "als-tax-q-change-trigger",
            "text": "What event obliges a mandatory re-classification review of an existing assertion?",
            "kind": "event",
            "answer_data": [
              "trigger event code",
              "event timestamp",
              "review obligation deadline"
            ]
          }
        ],
        "data_elements": [
          {
            "id": "als-tax-de-invalid-combination",
            "name": "invalid_combination_rule",
            "description": "Declarative rule naming a pair or set of relation kinds that may not co-occur for the same endpoint pair, plane and context.",
            "value_kind": "object",
            "cardinality": "0..n",
            "required": false,
            "source_refs": [
              "SRC-020",
              "SRC-018"
            ]
          },
          {
            "id": "als-tax-de-prior-kind",
            "name": "prior_relation_kind",
            "description": "Relation kind carried before a downgrade or upgrade, retained so that the classification history is reconstructible.",
            "value_kind": "code",
            "cardinality": "0..1",
            "required": false,
            "source_refs": [
              "SRC-026",
              "SRC-027"
            ]
          },
          {
            "id": "als-tax-de-change-reason",
            "name": "classification_change_reason",
            "description": "Controlled reason for a change of relation kind, such as new evidence, overclaim correction, external vocabulary revision or authority decision.",
            "value_kind": "code",
            "cardinality": "0..1",
            "required": false,
            "source_refs": [
              "SRC-028",
              "SRC-029"
            ]
          },
          {
            "id": "als-tax-de-mapping-cardinality",
            "name": "mapping_cardinality",
            "description": "Declared cardinality of the pairing, such as one-to-one, one-to-many, many-to-one or many-to-many.",
            "value_kind": "code",
            "cardinality": "0..1",
            "required": false,
            "source_refs": [
              "SRC-028"
            ]
          },
          {
            "id": "als-tax-de-observation-time",
            "name": "observation_timestamp",
            "description": "RFC 3339 instant with seconds and explicit offset at which the classification was observed or ingested, recorded separately from the effective interval.",
            "value_kind": "timestamp",
            "cardinality": "1",
            "required": true,
            "source_refs": [
              "SRC-023",
              "SRC-028"
            ]
          }
        ],
        "artifacts": [
          {
            "id": "als-tax-conflict-rule-catalogue",
            "name": "Invalid Combination and Cycle Rule Catalogue",
            "description": "Declarative catalogue of contradiction rules, disjointness rules carried from aligned vocabularies, cycle constraints on directed chains, cardinality expectations per relation kind and the mandatory content of a classification-change record. It states the rules; evaluating assertions against them, raising defects and enforcing outcomes are functions of services outside this model.",
            "media_or_form": [
              "rule catalogue",
              "structured record set"
            ],
            "serial": false,
            "identity_strategy": "Each rule is keyed by the authoritative master-system rule identifier issued by the register owner and expressed as a governed IRI in the adopting Dimension namespace; a UUID is used only where the master system issues no identifier.",
            "source_refs": [
              "SRC-018",
              "SRC-020",
              "SRC-028"
            ]
          }
        ],
        "inline_only_rationale": null
      }
    }
  ]
}
