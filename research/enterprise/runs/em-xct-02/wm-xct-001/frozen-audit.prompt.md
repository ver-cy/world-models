# Frozen no-tools semantic audit — Enterprise Fact Authority 0.1.0
You are an independent reviewer, not an approver. Do not browse, run tools or change files. Review only the complete frozen contract/code below. Return BLOCK if a defect violates the stated bounded contract; otherwise ACCEPT WITH LIMITS. Give severity, concrete input/operation demonstrating the defect and exact correction. Distinguish deferred production features from internal contradictions. Prior studies disagree on subtype; this package explicitly has only a discovery association with WM-XCT-001, not ControlRecord conformance. Stable identified assignment/rule/grant parts have versions in authority revisions; independent streams deferred. Does that stated narrow binding preserve identity/history? WriteGrant is original, not WM-XCT-002. Host/config/actor/time/full-ledger/subject-scope are trusted; no production IAM, signature or durability claim. Probe source-precedence vs write grants, unknown/conflicts, whole-term correction/transfer, past knowledge, receipts, denied-read leakage, same-source disputes, pins, actual native acceptance. No inferred consensus or automatic approval. End with a concise verdict and exact remaining holds. If files are truncated say so.


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

The examples use fixed synthetic time. An integrating service must supply its trusted receipt time and authenticated actor; users must not choose these or replace the configuration/ledger. `admit` performs an in-memory, atomic append into a **new** ledger. Persist it with concurrency control in a production adapter. Never expose `import_snapshot` as a write API: it validates trusted archives and does not authenticate their history. Native V3 validates only the outer snapshot envelope; invoke this companion explicitly before use and live admission. The native tool alone can store semantically invalid nested data.

Run `python test_authority.py`. To test new synthetic Dimensions, use `python acceptance.py --composer <trusted-WM-XCT-040-directory> --skill <trusted-vercy-skill-directory> --report acceptance-results.json`. Tool pins bind the expected local bytes; they do not sandbox Python imports or authenticate downloaded software.

## What is implemented

- Exact Dimension × scope × predicate governance, one-valued facts, explicit bounded UTC intervals and two temporal query axes.
- A value-accountable party distinct from a referenced definition-authority record, steward, publisher and writer.
- Source precedence separate from write grants; smaller priority numbers have higher precedence. Equal highest priority plus different tagged lexical values returns `contested` with both evidence references.
- Immutable revisions, previous-content digests, historical corrections, exact idempotent replay and receipt checks. A transfer uses distinct terms and preserves historical rows.
- All-or-nothing read projection for full-register readers; no partial visibility that hides a conflicting observation. Historical `routeTo` is informational at `routeValidAt`; resolve current routing before sending anything.
- Three small fixtures: startup (equal-priority disagreement), group (higher-precedence source beats later import), AI/software team (agreement with an explicit stewardship gap). They demonstrate patterns, not a full multinational competence graph or real company data.

## Deliberate limits

No authenticated publication, signatures, durable ledger, source connector, subject-to-scope verification, policy federation, recursive delegation, definition ownership resolution, adjudication workflow, confidence scoring, staleness detection, multi-valued predicates, units conversion, legal validity, production access enforcement or existing-Dimension migration. The trusted host determines correct scope and predicate cardinality. Malformed/missing authority never grants permission. A selected value is named `preferred`; it can still be false. Inputs may be incomplete; this library cannot prove it has all relevant observations or authorities.

Assignments and rules have their own stable IDs and intervals, but their versions are captured in an authority revision. Independent concurrent updates and reuse of one assignment across authorities are deferred. Missing steward yields an empty route; it never approves a disputed value. Full parent research and its historical source holds remain open.

```


## FILE boundary-decision.md
```
# Boundary decision

**Decision: a separately versioned companion contract, associated with WM-XCT-001 for discovery, with pattern alignment and explicit non-conformance. No new universal WM identifier.** This does not turn fact-type meaning or the truth of values into property ownership. The sole native snapshot subject is an explicitly identified governance-register aggregate in one Dimension, not a predicate or a company.

Claude recommends a WM-XCT-001 application profile; Grok objects that `controllable-object-anchor` excludes abstract predicates and that mastership is outside the control record. Direct byte inspection confirms that exclusion. We accept Grok's objection to subtype semantics: the package reuses named patterns but does not assert that FactAuthority is a ControlRecord. Its public location is an association, not inheritance. WM-XCT-002 explicitly excludes write/modify/delete permissions; our WriteGrant is an original, bounded reference construct, not a claimed implementation of 002. WM-XCT-012 supplies an alignment pattern for assertions, not automatic provenance conformance.

Both researchers distinguish independent assignment identity from party identity. Each StewardshipAssignment, MastershipRule and WriteGrant therefore has a stable URI independent of authority and party. The reference binding versions these records within authority snapshots. A party/source or owning authority change needs a new part ID, with prior rows retained. This is a limited document binding: standalone assignment revisions, cross-authority portability and distributed updates remain deferred, rather than claimed complete. References to a part must carry its ID plus containing authority revision and digest.

| Candidate | Boundary and lifecycle | Owner/source | Disposition and loss |
|---|---|---|---|
| FactAuthority | Appointment accountable for **values** of one scoped single-valued predicate; active/retracted; changes by immutable revision | Scoped governance publisher under a deployment trust anchor; appointment evidence | Bounded original contract aligned to 001. Definition authority is only an external reference, never inferred |
| Stewardship | Identified operational assignment with duties and valid term; recognition depends on active authority | Governance publisher, appointment evidence; party not inferred from model author | Identified nested document record `StewardshipAssignment`. Independent revision stream deferred |
| MastershipRule | Identified source preference for a scope/term, priority lower-is-preferred | Governance publisher, rule evidence | Keep registry name; narrower precedence-only semantics. No write permission or confidence implied |
| WriteGrant | Identified current submission right for named actors attributed to a source | External authenticated host + scoped governor | New reference construct, no 002 equivalence or production enforcement claim |
| FactObservation | Identified source assertion about subject/predicate, asserted/retracted; source+writer+subject stable | Named source via writer; retained evidence | Narrow 012-inspired carrier, not the target object or full provenance graph |
| AuthorityRegister | Stable canonical aggregate for one Dimension, explicit boundary, computed query view | Deployment operator maintains storage; governor owns governance facts; each source owns its assertions | JSON/native snapshot binding, with mandatory companion; not a new subject universe |
| Definition authority, policy administration service, identity/party, legal rights | Own meanings and independent lifecycles | External owners | References/deferred; do not auto-create from these records |

The minimum needs one trusted configuration, one active authority, one source rule, one separate write grant and one observation. Zero stewards is representable and yields an explicit empty route. No mandatory HRIS, ERP or organizational hierarchy. Several authorities may coexist in the archive; overlapping operative authorities return `authority-contested`, never last-writer-wins.

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
| Observation | Assertions and corrections | FactObservation | Stable source/subject anchor; revision digest; retained evidence | Authorized writer asserts/corrects/retracts its own record |
| Reliance | Historical query and projection | Derived Evaluation; AuthorityRegister | Full input slice and policy digests, separate clocks, full-reader permission | Read; report unknown/contested/preferred; propose follow-up |

Instance references can be cyclic in the external enterprise graph; this module never traverses them. Its revision graph is a linear chain per identified record. There is no inheritance or transitive authority graph. Runtime package imports are separate from semantic crosswalk references and from JSON document composition.

## Types, fields and cardinalities

All schema fields are required; arrays may be empty only where specified. No unknown keys. IDs and references are absolute URIs, at most 500 characters; no automatic canonicalization, alias merging or identity proof. Date/time is UTC `YYYY-MM-DDTHH:MM:SSZ`, real calendar values, half-open `[validFrom, validUntil)` with finite end. Use an explicitly chosen distant finite date if organizational policy needs it; an absent end is not accepted. Null is permitted only for genesis `previousDigest` and for no-value query outcomes. A URI is a reference, not proof its target exists.

**FactAuthority and FactObservation envelope**: `id` 1 stable record identity; `dimension` 1 tenant boundary; `scope` 1 host-governed scope URI; `predicate` 1 governed fact type; `revision` 1 integer ≥1; `previousDigest` 0-or-1 preceding record digest (null at revision 1); `recordedAt` 1 trusted receipt stamp at live admission; `validFrom`, `validUntil` 1 each claimed effective interval; `evidence` 1..n immutable evidence references. Dimension/scope/predicate cannot change within a lineage. Digest is SHA-256 of Python sorted compact UTF-8 JSON, no NaN; **not RFC 8785**. Unicode must encode before admission.

**FactAuthority** adds: `governs` exactly `values`; `definitionAuthorityRef` 1 external record to consult for meaning-owner, not validated here; `issuedBy` 1 publisher matching the authenticated caller at admission; `accountable` 1 party responsible for values and escalation, not automatically a writer; `state` active/retracted; `stewardships` 0..n identified appointments; `rules` 0..n precedence rules; `writeGrants` 0..n submission grants. All are source-backed governance records, not legal adjudications. Changing accountable party normally creates a new effective term as described below; a revision may correct a mistaken appointment under the explicit governor's trust.

**StewardshipAssignment**: `id` 1 distinct from authority/party; `party` 1 external actor; `duties` 1..n of maintain-quality, resolve-conflict, coordinate-transfer; valid bounds 1 each; evidence 1..n. Multiple stewards may be active; routing returns the set of active parties with resolve-conflict duty. These duties do not grant API writes or subdelegation. An absent steward is a visible context gap.

**MastershipRule**: `id` 1; `source` 1 external source identity; `priority` 1 integer 0..1,000,000 (smaller wins); valid bounds 1 each; evidence 1..n. Active source rules must be unambiguous: duplicate active rules for one source result in authority-contested even if priorities agree. Rules neither authenticate sources nor confer rights. They rank observations at the **fact-valid** instant under the knowledge cut.

**WriteGrant**: `id` 1; `source` 1; `writers` 1..n actor URIs; valid bounds 1 each; evidence 1..n. Grants apply at the **current trusted receipt** instant. There must be exactly one active grant for the source and it must name the caller. They do not rank or validate source truth. A source may have a grant but no precedence rule (record is retained, unranked), or a precedence rule but no live write grant (old observations remain rankable; new writes denied).

Identified parts have authority 1 → parts 0..n; each part belongs to exactly one authority throughout its history. Part ID, kind, owning authority, and party/source are immutable. Intervals must be inside the authority term. Changes to duty, priority or authorized writer set are recorded in a new containing authority revision. Part removal is a whole-snapshot correction, not an independent deletion event. The exact part version is `(partId, authorityId, authorityRevision, authorityDigest)`. Independent streams and shared assignments are outside 0.1.0.

**FactObservation** adds: `subject` 1 external canonical subject URI; `source` 1; `writer` 1 submitting actor; `state` asserted/retracted; `value` 1 `{datatype: URI, lexical: string ≤10000}`. Source, writer and subject are immutable within the observation lineage. Value is a tagged lexical atom: `01` and `1` differ, different datatype URIs differ, empty string is a supplied value, null is invalid. Host validates the domain datatype, units, actual subject membership and single-valued predicate contract. No algebra, sets, numeric coercion or confidence inference. Wrong-source correction must be a separate observation, not a replacement of someone else's record.

**TrustedConfiguration**: `id`, `dimension`, valid bounds; `governors` 1..n `(actor, scope, predicate)` authorizations; `readers` 1..n full-register actors; `purposes` 1..n admitted purpose strings. Deployment owns and authenticates this input separately; it is not inferred from the ledger. No bearer credentials. A matching governor may publish governance but does not automatically gain observation write/read rights. The Python function checks declarations but cannot authenticate a caller or configuration.

**AuthorityRegister**: format vercy-fact-authority, version 0.1.0, dimension, authorities and observations arrays (0..n, bounded 10,000). Canonical aggregate ID in the native binding is `<dimension>:authority-register`, one per Dimension for this reference. It has a declared boundary (only this profile's records), separate mastership per record family, governed revision rules and all-or-nothing disclosure. It does not replace a company instance. No global database is implied.

## Lifecycle, time and evaluation

1. Governor admits authority genesis/revision under current scoped configuration. Writer admits observation genesis/revision under exactly one active current authority and a separate WriteGrant. Issuer/writer must match the authenticated actor supplied by host. Two policy records can conflict; admitting one does not silently overwrite another.
2. Every new receipt equals trusted `now` and strictly follows **all** previous receipt timestamps. This serial reference supports one receipt per second, not high-throughput concurrent ingestion. Exact identical `(id,revision)` replay is a no-op after current authorization; changed replay rejects. Failures leave the input untouched. Future/backdated receipt injection is rejected; past effective dates are allowed.
3. A revision replaces the **entire claimed interval** as currently known; it does not patch a subinterval. It must cite its immediate predecessor digest. For a transfer, close the old term by a revision preserving its start and old party, then create a new authority/assignment ID from the cutoff. A future-dated replacement alone would remove old valid-time coverage; use split terms instead. Temporary gaps are fail-closed. Durable multi-record atomic transfer is deferred.
4. Query filters by `recordedAt <= knownAt`, takes the latest revision per ID, then effective interval and active/asserted state. These operations happen in that order. `knownAt > now` rejects. Past knowledge does not see a policy correction received today. `recordedAt` is receipt, not source event time or authenticated publication proof; other clocks are deliberately not manufactured.
5. Match exact dimension/scope/predicate. Zero authorities → unknown; multiple active authority IDs → authority-contested. Duplicate active rules for a source → authority-contested. No inherited scope, arbitrary scope expression, jurisdiction precedence or implicit most-specific rule. The trusted host binds subject/scope; supplying an arbitrary complete forged register can bypass this reference because authentication is outside it.
6. Retain all active matching observations and evidence, including unranked and lower-priority ones. Among sources with a live rule choose the minimum priority. If their tagged lexical values disagree, return contested and no value. Otherwise return preferred with that value and all supporting IDs. Multiple competing records from **one** source can also contest. Source identity count is not a vote.
7. Outcomes carry profile version, exact matched authority revision digests, known input-slice digest and configuration digest. This is reproducibility metadata, not signed publication. `observationIds`, `evidence`, unranked IDs and preferred IDs expose only the matching temporal slice. Input digest covers the full known register as an integrity pin, not a summary of only this query. No side-effect notification occurs. Historical route is labeled by fact-valid time and must not be used as current contact authority.
8. Read permission is checked before ledger validation. An unauthorized actor or purpose receives only `Read denied`; no selective assertion filtering is implemented. Authorized readers are cleared for the entire register. Configuration is checked at current time even for historical queries. This does not recreate past authenticated access decisions or verify every old append was authorized. `validate_ledger`/`import_snapshot` validate structure and history consistency only.

## Executable invariants and question routes

I01 Equal priority disagreement is contested; I02 import order never ranks; I03 owner/steward/model maintainer are not implicit writers; I04 no authority is unknown, never a grant; I05 duplicate policies/rules fail to select; I06 source preference and current WriteGrant are independent; I07 immutable scope/source/subject anchors and identified parts; I08 receipt order and predecessor digests; I09 previous knowledge cuts survive corrections; I10 interval containment and exclusive upper bounds; I11 no partial access filter; I12 no implicit value coercion; I13 transfer keeps old effective terms; I14 atomic in-memory rejection and exact replay; I15 future knowledge/receipt rejection; I16 loss-bearing migration refused. `test_authority.py` implements representative positive/negative cases; it does not prove all possible states or domain truth.

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
| Q11 | FA-correction → How is a wrong claim corrected? | next observation revision | Original writer submits with evidence; retain prior rows |
| Q12 | FA-transfer → What happens at responsible-party change? | closed old term + new term | Governor records both; gap stays unknown |
| Q13 | FA-disclosure → What can this reader see? | trusted full-register read policy | All or deny; do not drop a hidden contradiction |
| Q14 | FA-minimum → Does a startup need HRIS? | one-source minimal register | Use governed manual source with explicit rights |
| Q15 | FA-context → What if source/policy is missing? | reason and unranked IDs | Ask for missing authority/rule; do not invent source truth |
| Q16 | FA-binding → Does native validation prove semantics? | native + companion reports | Invoke both; nested V3 acceptance alone insufficient |
| Q17 | FA-migration → Can earlier owner strings be imported? | migration.md | Stage candidates outside operative register; explicit mapping required |
| Q18 | FA-evidence → Does provenance prove the value? | evidence references | Inspect externally; no inferred veracity or access grant |

Every route is informational or explicitly guarded; no agent is authorized to act merely because a table lists an action.

```


## FILE migration.md
```
# Migration and retention

Only 0.1.0 is supported. `migrate(..., '0.1.0')` preserves the archive; any other target rejects. No lossy downgrade is promised. The first release is additive and does not modify existing Dimensions or replace their policies.

Catalog owner strings, CODEOWNERS and free-form spreadsheet authors are candidates, never operative FactAuthority or WriteGrant. Preserve original references in an external staging artifact. A scoped governor must explicitly appoint an accountable party, assign the exact scope/predicate, define source priorities separately from writers, provide terms/evidence and approve the deployment configuration through the host's governance process. No provider transcript is a grant.

For corrections retain all rows, append revision+1 with previous digest and a new trusted receipt; old `knownAt` queries retain the old answer. A correction replaces the whole assertion/authority term as currently known. For a real transfer create a new effective term and close the old one, using distinct assignment IDs when party changes. Do not truncate the old term's start or physically delete it. Tests demonstrate historical answers across the cutoff. Multi-record durability/concurrency must be implemented by the host; partial transfer gaps fail closed.

Rollback restores earlier semantics by another governor-issued revision or a new term. Replacing the live register with an old exported file is not a valid append and can erase knowledge. Keep original frozen evaluation pins and the software version used. A trusted archive import validates data consistency only; it does not prove authorization or completeness. Validate domain meanings before mapping to a future profile.

Production retention cannot be “forever by default”: the deployment needs an approved policy for source evidence, personally identifying party refs, erasure, legal holds and audit records. This synthetic reference keeps all revisions and implements neither physical deletion nor an erasure guarantee. Public fixtures contain no organizational instance data. External evidence values, credentials and personal addresses must remain outside public packages.

```


## FILE agent-guide.md
```
# Agent use

Read README, boundary-decision and model-spec, then the pinned schema and companion. Inspect the Dimension's trusted configuration and runtime binding before proposing any changes. The model author, installation actor, accountable party, steward and source writer are separate roles; none implies the others.

An unknown, unranked, contested or authority-contested result is a result to preserve. Ask for the missing predicate scope, governance appointment, rule or source evidence. Never choose a winner from arrival order, majority source count, model maintainer identity or a confidence score. Never promote a proposal or inferred owner into an operative record.

Query through a host that authenticates actors, controls the full register, fixes the subject-to-scope mapping and invokes the companion. Do not let an API client supply a policy, receipt clock or reduced assertion list. A historical route is not current permission to notify a person. This library sends nothing and makes no organization decisions.

For native V3, a syntactically valid outer snapshot is insufficient. Check the installed code/schema digests, explicitly validate the stored nested register, and call admit for new live changes. A report that only says “JSON Schema passed” does not establish authority, authorization, truth or publication authenticity.

```


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
class Denied(Invalid): pass
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
        for row in x['stewardships']+x['rules']+x['writeGrants']:
            require(row['id'] not in seen,'Duplicate aggregate part ID');seen.add(row['id']);interval(row)
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
                require(x['revision']==1 and x['previousDigest'] is None,'Missing genesis')
            else:
                require(x['revision']==old['revision']+1 and x['previousDigest']==digest(old),'Broken revision chain')
                require(x['recordedAt']>old['recordedAt'],'Receipt order not increasing')
                stable=['dimension','scope','predicate']+(['subject','source','writer'] if kind=='observation' else [])
                require(all(x[k]==old[k] for k in stable),'Immutable anchor changed')
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

    Returns a new ledger. Exact replays are idempotent after current authorization.
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
            require(encode(old)==encode(record),'Conflicting replay');return copy.deepcopy(ledger)
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
    as_known={k:[x for x in ledger[k] if x['recordedAt']<=knownAt] for k in ['authorities','observations']}
    base={'status':'unknown','value':None,'authorityIds':sorted(x['id'] for x in match),'observationIds':[],
          'evidence':[],'routeTo':[],'validAt':validAt,'knownAt':knownAt,
          'scope':scope,'predicate':predicate,'subject':subject,'reason':'missing-authority',
          'profileVersion':'0.1.0','inputDigest':digest(as_known),'configDigest':digest(config),
          'authorityPins':[{'id':x['id'],'revision':x['revision'],'sha256':digest(x)} for x in sorted(match,key=lambda x:x['id'])],
          'routeValidAt':validAt,'routeAction':'Informational only; resolve current routing before sending'}
    if len(match)>1:base.update(status='authority-contested',reason='overlapping-authority-records');return base
    if not match:return base
    authority=match[0];base['accountable']=authority['accountable']
    base['routeTo']=sorted({s['party'] for s in authority['stewardships'] if active(s,validAt) and 'resolve-conflict' in s['duties']})
    rules=[r for r in authority['rules'] if active(r,validAt)];sources=[r['source'] for r in rules]
    if len(sources)!=len(set(sources)):base.update(status='authority-contested',reason='overlapping-source-rules');return base
    ranking={r['source']:r['priority'] for r in rules}
    obs=[x for x in current(ledger['observations'],knownAt) if x['state']=='asserted' and key(x)==(scope,predicate) and x['subject']==subject and active(x,validAt)]
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
    return {'id':'urn:synthetic:authority','dimension':D,'scope':S,'predicate':F,'governs':'values','definitionAuthorityRef':'urn:synthetic:definition-owner-record','revision':1,'previousDigest':None,'recordedAt':'2026-09-21T10:00:00Z','validFrom':START,'validUntil':END,'evidence':['urn:synthetic:appointment'],'issuedBy':G,'accountable':'urn:synthetic:owner','state':'active','stewardships':[{'id':'urn:synthetic:stewardship','party':'urn:synthetic:steward','duties':['resolve-conflict'],'validFrom':START,'validUntil':END,'evidence':['urn:synthetic:mandate']}],'rules':[{'id':'urn:synthetic:rule:'+s,'source':'urn:synthetic:source:'+s,'priority':0,'validFrom':START,'validUntil':END,'evidence':['urn:synthetic:rule-evidence']} for s in ['a','b']],'writeGrants':[{'id':'urn:synthetic:write:'+s,'source':'urn:synthetic:source:'+s,'writers':[W],'validFrom':START,'validUntil':END,'evidence':['urn:synthetic:write-evidence']} for s in ['a','b']]}
def observation(n=1,value='A'):
    return {'id':'urn:synthetic:observation:'+str(n),'dimension':D,'scope':S,'predicate':F,'revision':1,'previousDigest':None,'recordedAt':'2026-09-21T10:00:0'+str(n)+'Z','validFrom':START,'validUntil':END,'evidence':['urn:synthetic:evidence:'+str(n)],'subject':SUB,'source':'urn:synthetic:source:'+('a' if n==1 else 'b'),'writer':W,'state':'asserted','value':{'datatype':'urn:synthetic:string','lexical':value}}
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
    y=copy.deepcopy(x);y.update(revision=x['revision']+1,previousDigest=a.digest(x),recordedAt=at);y.update(changes);return y
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
        left=query(l,self.c);right=query(self.l,self.c);left.pop('inputDigest');right.pop('inputDigest');self.assertEqual(left,right)
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
        cutoff='2026-10-01T00:00:00Z';x=revision(self.l['authorities'][0]);x['validUntil']=cutoff
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


## FILE test-results.json
```
{
  "tests": 45,
  "failures": 0,
  "errors": 0,
  "passed": true,
  "scope": "Reference semantics including authority, temporal history, negative admission and disclosure; not authenticated production service"
}

```


## FILE acceptance.py
```
"""Synthetic new-Dimension acceptance, using explicitly trusted local tools.

python acceptance.py --composer /trusted/WM-XCT-040 --skill /trusted/vercy/skills/vercy --report acceptance-results.json
Only this script's temporary directory is changed. No existing Dimension is used.
"""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from pathlib import Path
import authority as p
HERE=Path(__file__).resolve().parent
def run(composer,skill):
    p.require(__debug__,'Run acceptance without -O')
    composer=Path(composer).resolve();skill=Path(skill).resolve()
    pins=p.load(HERE/'tool-pins.json')
    for name,h in pins['composerFiles'].items():p.require(hashlib.sha256((composer/name).read_bytes()).hexdigest()==h,'unexpected composer bytes: '+name)
    for name,h in pins['skillFiles'].items():p.require(hashlib.sha256((skill/name).read_bytes()).hexdigest()==h,'unexpected skill bytes: '+name)
    for name,h in pins['upstreamFiles'].items():p.require(hashlib.sha256((HERE/'upstream'/name).read_bytes()).hexdigest()==h,'unexpected upstream bytes: '+name)
    sys.path.insert(0,str(composer));import composition as c
    from bootstrap_dimension import bootstrap
    sys.path.insert(0,str(skill/'scripts'));from write_record import append
    from validate_dimension import validate as native_validate
    authority_policy=p.load(HERE/'examples/startup.config.json');reports=[]
    with tempfile.TemporaryDirectory(prefix='vercy-authority-acceptance-') as tmp:
        root=Path(tmp);assets=root/'assets';assets.mkdir()
        def descriptor(slug,name,source):
            raw=source.read_bytes();dest=assets/slug/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
            return {'path':slug+'/'+name,'digest':c.digest(raw),'size':len(raw),'mediaType':'text/x-python' if name.endswith('.py') else 'application/json' if name.endswith('.json') else 'text/markdown' if name.endswith('.md') else 'application/yaml','sourceUrl':'https://ver.cy/models/'+slug+('/versions/0.3.0-research.1/' if slug=='wm-xct-001-ownership-stewardship' and name in {'spec.yaml','AGENTS.md'} else '/profiles/enterprise-fact-authority/0.1.0/' if name not in {'spec.yaml','AGENTS.md'} else '/')+name}
        releases=[]
        for slug in ['wm-xct-001-ownership-stewardship']:
            source=HERE/'upstream'/slug;raw=(source/'spec.yaml').read_text(encoding='utf-8');meta=json.loads(raw[raw.index('{'):])['metaModel']
            dspec=descriptor(slug,'spec.yaml',source/'spec.yaml');dagent=descriptor(slug,'AGENTS.md',source/'AGENTS.md')
            binding=None
            if meta['id']=='WM-XCT-001':
                runtime=descriptor(slug,'runtime-model.reference.json',HERE/'runtime-model.reference.json')
                instance=descriptor(slug,'authority.schema.json',HERE/'authority.schema.json')
                validator=descriptor(slug,'authority.py',HERE/'authority.py')
                binding={'id':'urn:vercy:binding:enterprise-authority-register','version':'0.1.0','forSpecificationDigest':dspec['digest'],'runtime':runtime,'instanceSchema':instance,'companionValidator':validator,'scope':'One reference governance-register snapshot; companion semantics required; no IAM or full parent conformance.'}
            releases.append({'modelId':meta['registryId'],'version':meta['version'],'namespace':'urn:vercy:model:'+meta['registryId'],'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','requires':[],'references':[],'specification':dspec,'agents':dagent,'installationMode':'native-binding' if binding else 'semantic-only','binding':binding,'semanticFingerprint':None,'compatibility':{'decision':'accepted','reviewer':'urn:synthetic:reviewer:authority','evidence':'urn:synthetic:acceptance:authority','observedAt':c.now(),'scope':'Only this reference binding and synthetic composition.'}})
        # Reference-only neighbors do not become runtime imports.
        for name in ['startup','group','ai-team']:
            target=root/name;stage=root/(name+'-stage');policy_path=root/(name+'-composition-policy.json');lock_path=root/(name+'-lock.json');plan_path=root/(name+'-plan.json')
            dimension=authority_policy['dimension'];at=c.now()
            policy={'format':'vercy-composition-policy','version':1,'id':'urn:synthetic:composition-policy:authority','dimensionId':dimension,'owner':'urn:synthetic:owner:authority','allowInstall':True,'actors':['urn:synthetic:actor:composer'],'purposes':['Synthetic enterprise authority reference'],'allowedModelIds':['vr.wm-xct-001'],'allowedOrigins':['https://ver.cy'],'reviewers':['urn:synthetic:reviewer:authority'],'allowReviewableDrafts':True,'validFrom':'2026-09-21T00:00:00Z','validUntil':'2027-01-01T00:00:00Z'}
            policy_path.write_bytes(c.encode(policy));lock_path.write_bytes(c.encode({'models':[]}))
            plan={'format':'vercy-composition-plan','schemaVersion':'1.0.0','planId':'urn:synthetic:composition:authority:'+name,'revision':1,'supersedes':None,'algorithm':'exact-closure-v1','dimensionId':dimension,'createdAt':at,'validUntil':'2026-12-31T23:59:59Z','baseLockDigest':c.digest(lock_path.read_bytes()),'roots':[{k:releases[0][k] for k in ['modelId','version']}],'releases':releases,'authority':{'actor':policy['actors'][0],'allowReviewableDrafts':True,'allowedModelIds':policy['allowedModelIds'],'decision':'allow','owner':policy['owner'],'policyDigest':c.digest(policy_path.read_bytes()),'policyRef':policy['id'],'purpose':policy['purposes'][0]},'provenance':{'classification':'public-synthetic','evidenceKind':'proposal','masterSystem':'urn:synthetic:reference','recordedAt':at,'source':'urn:synthetic:fixture:'+name}}
            plan_path.write_bytes(c.encode(plan));c.stage(plan_path,assets,policy_path,lock_path,stage)
            bootstrap(stage,policy_path,lock_path,skill,target,'Synthetic authority '+name,dimension)
            installed=target/'models/composed/wm-xct-001-ownership-stewardship/authority.py'
            p.require(c.digest(installed.read_bytes())==releases[0]['binding']['companionValidator']['digest'],'installed validator differs')
            p.require(c.digest((installed.parent/'authority.schema.json').read_bytes())==releases[0]['binding']['instanceSchema']['digest'],'installed schema differs')
            module_spec=importlib.util.spec_from_file_location('installed_authority_'+name,installed);module=importlib.util.module_from_spec(module_spec);module_spec.loader.exec_module(module)
            rows=[p.load(HERE/('examples/'+name+'.json'))];written_facts=[]
            for i,a in enumerate(rows):
                obj={'recordType':'object','schemaVersion':'1.0.0','recordId':a['dimension']+':authority-register'+':object-r1','objectId':a['dimension']+':authority-register','objectType':'vr.wm-xct-001:authority-register','name':'Synthetic authority assertion','description':'One explicitly bounded governance register aggregate; not the company itself','recordedAt':at,'previousRecordId':None,'state':'active','provenance':{'source':'urn:synthetic:reference','synthetic':True},'accessClass':'synthetic-private'}
                fact={'recordType':'fact','schemaVersion':'1.0.0','factId':a['dimension']+':authority-register'+':snapshot-r1','subjectId':a['dimension']+':authority-register','path':'authority.register.snapshot','value':a,'unit':None,'validFrom':at,'validTo':None,'recordedAt':at,'supersedes':[],'status':'asserted','provenance':{'source':'urn:synthetic:reference','synthetic':True},'authority':{'source':'urn:synthetic:actor:steward','rank':0},'masterSystem':'urn:synthetic:reference','accessClass':'synthetic-private'}
                for kind,value in [('object',obj),('fact',fact)]:
                    path=root/(name+str(i)+kind+'.json');path.write_bytes(p.encode(value));written=append(target,kind,path)
                    if kind=='fact':written_facts.append(target/written['written'])
            stored=[p.load(x)['value'] for x in written_facts]
            p.require(stored==rows,'stored assertion round-trip differs from source fixtures');module.validate_ledger(stored[0],authority_policy)
            answer=module.evaluate(stored[0],authority_policy,actor='urn:synthetic:reader',purpose='governance-review',scope='urn:synthetic:scope',predicate='urn:synthetic:predicate',subject='urn:synthetic:subject',validAt='2026-09-21T12:00:00Z',knownAt='2026-09-21T12:00:00Z',now='2026-09-21T12:00:00Z')
            p.require(answer['status']==('contested' if name=='startup' else 'preferred'),'stored decision differs from expected')
            v=native_validate(target);p.require(v['valid'],'native V3 failed')
            # Deliberately corrupt an actually stored nested snapshot. V3 should
            # still accept the outer object type, and the companion must reject.
            victim=written_facts[0];raw=victim.read_bytes();bad=p.load(victim);bad['value']['authorities'][0]['rules'][0]['priority']=-1;victim.write_bytes(p.encode(bad))
            negative_v3=native_validate(target);rejected=False
            try:module.validate_ledger(p.load(victim)['value'],authority_policy)
            except module.Invalid:rejected=True
            finally:victim.write_bytes(raw)
            p.require(negative_v3['valid'] and rejected,'expected native/companion distinction not observed')
            v.pop('dimension',None);negative_v3.pop('dimension',None)
            reports.append({'profile':name,'objects':len(rows),'facts':len(stored),'native':v,'storedDecision':answer,'roundTripEqualsInput':stored==rows,'companion':'Explicitly called on actual stored snapshots; not automatically enforced by native V3','invalidNestedSnapshot':{'native':negative_v3,'companionRejected':rejected},'installedValidatorDigest':c.digest(installed.read_bytes()),'pins':[{'id':r['modelId'],'version':r['version'],'digest':r['specification']['digest'],'mode':r['installationMode']} for r in releases]})
    return {'format':'vercy-authority-profile-acceptance','executedAt':c.now(),'passed':len(reports),'failed':0,'profiles':reports,'sourceDigests':{str(x.relative_to(HERE)):hashlib.sha256(x.read_bytes()).hexdigest() for x in [Path(__file__),HERE/'authority.py',HERE/'authority.schema.json',HERE/'tool-pins.json',*sorted((HERE/'examples').glob('*.json'))]},'limits':'Synthetic new-Dimension register snapshots only. Authentication, durable admission, source truth and existing-Dimension migrations are not tested.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True);args=ap.parse_args();report=run(args.composer,args.skill);Path(args.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':report['passed'],'failed':report['failed']}))

```


## FILE acceptance-results.json
```
{
  "format": "vercy-authority-profile-acceptance",
  "executedAt": "2026-09-21T17:54:09Z",
  "passed": 3,
  "failed": 0,
  "profiles": [
    {
      "profile": "startup",
      "objects": 1,
      "facts": 1,
      "native": {
        "valid": true,
        "conformanceLevel": "V3",
        "schemas": "https://ver.cy/schemas/dimension/1.0/",
        "counts": {
          "objects": 1,
          "facts": 1,
          "relations": 0,
          "events": 0
        },
        "errors": [],
        "warnings": [],
        "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety"
      },
      "storedDecision": {
        "status": "contested",
        "value": null,
        "authorityIds": [
          "urn:synthetic:authority"
        ],
        "observationIds": [
          "urn:synthetic:observation:1",
          "urn:synthetic:observation:2"
        ],
        "evidence": [
          "urn:synthetic:evidence:1",
          "urn:synthetic:evidence:2"
        ],
        "routeTo": [
          "urn:synthetic:steward"
        ],
        "validAt": "2026-09-21T12:00:00Z",
        "knownAt": "2026-09-21T12:00:00Z",
        "scope": "urn:synthetic:scope",
        "predicate": "urn:synthetic:predicate",
        "subject": "urn:synthetic:subject",
        "reason": "equal-priority-disagreement",
        "profileVersion": "0.1.0",
        "inputDigest": "a9894fd3a38b8f6cd57e5579949d8f9f23d5e2a952d4627b89c58d53227c6dd8",
        "configDigest": "71cc5d08dd34b2735e25c4304c1659f929acad8abb83d8cf9b43c29531930eca",
        "authorityPins": [
          {
            "id": "urn:synthetic:authority",
            "revision": 1,
            "sha256": "1eadf3fb0873e84beb95c447ad6baeaf9e80479f94fca737272e68ac836ba444"
          }
        ],
        "routeValidAt": "2026-09-21T12:00:00Z",
        "routeAction": "Informational only; resolve current routing before sending",
        "accountable": "urn:synthetic:owner",
        "unrankedObservationIds": [],
        "preferredObservationIds": [
          "urn:synthetic:observation:1",
          "urn:synthetic:observation:2"
        ],
        "priority": 0
      },
      "roundTripEqualsInput": true,
      "companion": "Explicitly called on actual stored snapshots; not automatically enforced by native V3",
      "invalidNestedSnapshot": {
        "native": {
          "valid": true,
          "conformanceLevel": "V3",
          "schemas": "https://ver.cy/schemas/dimension/1.0/",
          "counts": {
            "objects": 1,
            "facts": 1,
            "relations": 0,
            "events": 0
          },
          "errors": [],
          "warnings": [],
          "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety"
        },
        "companionRejected": true
      },
      "installedValidatorDigest": "sha256:29d9ec5777a29c201285bed12bcfdd0ca90bdbffc1dc5fed676c3a420860462d",
      "pins": [
        {
          "id": "vr.wm-xct-001",
          "version": "0.3.0-research.1",
          "digest": "sha256:a09261ca365d2e82716705a27d5e46cca7faef8fc22d90fcf3b94a53ef729358",
          "mode": "native-binding"
        }
      ]
    },
    {
      "profile": "group",
      "objects": 1,
      "facts": 1,
      "native": {
        "valid": true,
        "conformanceLevel": "V3",
        "schemas": "https://ver.cy/schemas/dimension/1.0/",
        "counts": {
          "objects": 1,
          "facts": 1,
          "relations": 0,
          "events": 0
        },
        "errors": [],
        "warnings": [],
        "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety"
      },
      "storedDecision": {
        "status": "preferred",
        "value": {
          "datatype": "urn:synthetic:string",
          "lexical": "A"
        },
        "authorityIds": [
          "urn:synthetic:authority"
        ],
        "observationIds": [
          "urn:synthetic:observation:1",
          "urn:synthetic:observation:2"
        ],
        "evidence": [
          "urn:synthetic:evidence:1",
          "urn:synthetic:evidence:2"
        ],
        "routeTo": [
          "urn:synthetic:steward"
        ],
        "validAt": "2026-09-21T12:00:00Z",
        "knownAt": "2026-09-21T12:00:00Z",
        "scope": "urn:synthetic:scope",
        "predicate": "urn:synthetic:predicate",
        "subject": "urn:synthetic:subject",
        "reason": "explicit-source-precedence",
        "profileVersion": "0.1.0",
        "inputDigest": "235a8fbbf381331c4c8778102a362a6b175a4613de26c231304a6284983577b7",
        "configDigest": "71cc5d08dd34b2735e25c4304c1659f929acad8abb83d8cf9b43c29531930eca",
        "authorityPins": [
          {
            "id": "urn:synthetic:authority",
            "revision": 1,
            "sha256": "4d16b424d65b1974154cb479b9f6f61d629ec5f09c81fc88b1a15b570ccf95bf"
          }
        ],
        "routeValidAt": "2026-09-21T12:00:00Z",
        "routeAction": "Informational only; resolve current routing before sending",
        "accountable": "urn:synthetic:owner",
        "unrankedObservationIds": [],
        "preferredObservationIds": [
          "urn:synthetic:observation:1"
        ],
        "priority": 0
      },
      "roundTripEqualsInput": true,
      "companion": "Explicitly called on actual stored snapshots; not automatically enforced by native V3",
      "invalidNestedSnapshot": {
        "native": {
          "valid": true,
          "conformanceLevel": "V3",
          "schemas": "https://ver.cy/schemas/dimension/1.0/",
          "counts": {
            "objects": 1,
            "facts": 1,
            "relations": 0,
            "events": 0
          },
          "errors": [],
          "warnings": [],
          "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety"
        },
        "companionRejected": true
      },
      "installedValidatorDigest": "sha256:29d9ec5777a29c201285bed12bcfdd0ca90bdbffc1dc5fed676c3a420860462d",
      "pins": [
        {
          "id": "vr.wm-xct-001",
          "version": "0.3.0-research.1",
          "digest": "sha256:a09261ca365d2e82716705a27d5e46cca7faef8fc22d90fcf3b94a53ef729358",
          "mode": "native-binding"
        }
      ]
    },
    {
      "profile": "ai-team",
      "objects": 1,
      "facts": 1,
      "native": {
        "valid": true,
        "conformanceLevel": "V3",
        "schemas": "https://ver.cy/schemas/dimension/1.0/",
        "counts": {
          "objects": 1,
          "facts": 1,
          "relations": 0,
          "events": 0
        },
        "errors": [],
        "warnings": [],
        "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety"
      },
      "storedDecision": {
        "status": "preferred",
        "value": {
          "datatype": "urn:synthetic:string",
          "lexical": "A"
        },
        "authorityIds": [
          "urn:synthetic:authority"
        ],
        "observationIds": [
          "urn:synthetic:observation:1",
          "urn:synthetic:observation:2"
        ],
        "evidence": [
          "urn:synthetic:evidence:1",
          "urn:synthetic:evidence:2"
        ],
        "routeTo": [],
        "validAt": "2026-09-21T12:00:00Z",
        "knownAt": "2026-09-21T12:00:00Z",
        "scope": "urn:synthetic:scope",
        "predicate": "urn:synthetic:predicate",
        "subject": "urn:synthetic:subject",
        "reason": "explicit-source-precedence",
        "profileVersion": "0.1.0",
        "inputDigest": "e792988abb93313ac6cfde16f6d0cd4a82996c16dff4dfc65e4e4b192c390a48",
        "configDigest": "71cc5d08dd34b2735e25c4304c1659f929acad8abb83d8cf9b43c29531930eca",
        "authorityPins": [
          {
            "id": "urn:synthetic:authority",
            "revision": 1,
            "sha256": "f4ae478ddefce03dd959f1a2ef79d74e5e34140244abe4cab633948b5cb52c02"
          }
        ],
        "routeValidAt": "2026-09-21T12:00:00Z",
        "routeAction": "Informational only; resolve current routing before sending",
        "accountable": "urn:synthetic:owner",
        "unrankedObservationIds": [],
        "preferredObservationIds": [
          "urn:synthetic:observation:1",
          "urn:synthetic:observation:2"
        ],
        "priority": 0
      },
      "roundTripEqualsInput": true,
      "companion": "Explicitly called on actual stored snapshots; not automatically enforced by native V3",
      "invalidNestedSnapshot": {
        "native": {
          "valid": true,
          "conformanceLevel": "V3",
          "schemas": "https://ver.cy/schemas/dimension/1.0/",
          "counts": {
            "objects": 1,
            "facts": 1,
            "relations": 0,
            "events": 0
          },
          "errors": [],
          "warnings": [],
          "scope": "executable structure and record semantics; does not certify external truth, legal authority, or safety"
        },
        "companionRejected": true
      },
      "installedValidatorDigest": "sha256:29d9ec5777a29c201285bed12bcfdd0ca90bdbffc1dc5fed676c3a420860462d",
      "pins": [
        {
          "id": "vr.wm-xct-001",
          "version": "0.3.0-research.1",
          "digest": "sha256:a09261ca365d2e82716705a27d5e46cca7faef8fc22d90fcf3b94a53ef729358",
          "mode": "native-binding"
        }
      ]
    }
  ],
  "sourceDigests": {
    "acceptance.py": "0319d8fdc6bc195ed9abb09d5b27441de66bf6e90b512810e53e3d9e05758719",
    "authority.py": "29d9ec5777a29c201285bed12bcfdd0ca90bdbffc1dc5fed676c3a420860462d",
    "authority.schema.json": "d7b9fd43a563f7cb96afb0ed0385f2768395695bc3924d782d707b1ac95ba8b5",
    "tool-pins.json": "a2d5e2cbca9e9218c61f0346e1f25d3b35b867910161f79a71951df3569f172c",
    "examples\\ai-team.config.json": "257a4909c81afa2f67ed6f569d98bfbb2418ff5c136b1a96c58ff532690a14b5",
    "examples\\ai-team.json": "e9e59a1a7b434073109ae30706d7b7e209497af0a58d01371bd51fded245f8dc",
    "examples\\group.config.json": "257a4909c81afa2f67ed6f569d98bfbb2418ff5c136b1a96c58ff532690a14b5",
    "examples\\group.json": "bd53041a20dd77c4f0ad50d8bfae7651ba6fb145ca7540d5327829fa1c16495e",
    "examples\\startup.config.json": "257a4909c81afa2f67ed6f569d98bfbb2418ff5c136b1a96c58ff532690a14b5",
    "examples\\startup.json": "e842aac23f577397a612c490d7c95e31d127d616fe4cfa8a6a0d253235d59717"
  },
  "limits": "Synthetic new-Dimension register snapshots only. Authentication, durable admission, source truth and existing-Dimension migrations are not tested."
}

```


## FILE whole-object-coverage.yaml
```
{
  "FactAuthority": {
    "identity-class": {
      "status": "required",
      "reason": "Stable appointment URI + revision"
    },
    "direct-properties": {
      "status": "required",
      "reason": "Values governance, scope, accountable, term"
    },
    "recognition-observation": {
      "status": "required",
      "reason": "Recognized only under active temporal slice and trusted host governance"
    },
    "capabilities-behaviour-actions": {
      "status": "required",
      "reason": "Scoped governor admits/corrects/retracts; does not derive write rights"
    },
    "context-evidence": {
      "status": "required",
      "reason": "Evidence, source publisher and definition-authority reference"
    }
  },
  "StewardshipAssignment": {
    "identity-class": {
      "status": "required",
      "reason": "Stable part URI independent of party"
    },
    "direct-properties": {
      "status": "required",
      "reason": "Party, duties, bounded term"
    },
    "recognition-observation": {
      "status": "required",
      "reason": "Active authority + effective part; no identity proof"
    },
    "capabilities-behaviour-actions": {
      "status": "required",
      "reason": "Informational triage/transfer duties; no implicit permissions"
    },
    "context-evidence": {
      "status": "required",
      "reason": "Appointment evidence and containing authority revision digest"
    }
  },
  "MastershipRule": {
    "identity-class": {
      "status": "required",
      "reason": "Stable rule URI independent of source"
    },
    "direct-properties": {
      "status": "required",
      "reason": "Source, lower-is-preferred integer priority, term"
    },
    "recognition-observation": {
      "status": "required",
      "reason": "Unambiguous active source rule under authority slice"
    },
    "capabilities-behaviour-actions": {
      "status": "required",
      "reason": "Evaluator may rank; rule itself never writes"
    },
    "context-evidence": {
      "status": "required",
      "reason": "Rule evidence and exact policy pin"
    }
  },
  "WriteGrant": {
    "identity-class": {
      "status": "required",
      "reason": "Stable grant URI independent of caller"
    },
    "direct-properties": {
      "status": "required",
      "reason": "Source, named writers, term"
    },
    "recognition-observation": {
      "status": "required",
      "reason": "Exactly one active current grant and matching actor supplied by host"
    },
    "capabilities-behaviour-actions": {
      "status": "required",
      "reason": "Permits reference admission only, no preference or source truth"
    },
    "context-evidence": {
      "status": "required",
      "reason": "Grant evidence and current external trust config"
    }
  },
  "FactObservation": {
    "identity-class": {
      "status": "required",
      "reason": "Stable assertion URI, immutable subject/source/writer"
    },
    "direct-properties": {
      "status": "required",
      "reason": "Tagged lexical value, interval and asserted/retracted state"
    },
    "recognition-observation": {
      "status": "required",
      "reason": "Known/valid slices; domain meaning verification delegated to host"
    },
    "capabilities-behaviour-actions": {
      "status": "required",
      "reason": "Named writer corrects/retracts through admit"
    },
    "context-evidence": {
      "status": "required",
      "reason": "Evidence refs, receipt time and predecessor digest"
    }
  },
  "AuthorityRegister": {
    "identity-class": {
      "status": "required",
      "reason": "Canonical Dimension-derived aggregate ID in binding"
    },
    "direct-properties": {
      "status": "required",
      "reason": "Closed known register, version and separate collections"
    },
    "recognition-observation": {
      "status": "required",
      "reason": "Companion-valid archive does not prove admission"
    },
    "capabilities-behaviour-actions": {
      "status": "required",
      "reason": "Append via admit; evaluate/read/export via trusted host"
    },
    "context-evidence": {
      "status": "required",
      "reason": "Root configuration, profile/version and archive evidence"
    }
  },
  "TrustedConfiguration": {
    "identity-class": {
      "status": "required",
      "reason": "Deployment-owned config URI and content digest"
    },
    "direct-properties": {
      "status": "required",
      "reason": "Dimension, scoped governors, full readers, purposes and term"
    },
    "recognition-observation": {
      "status": "required",
      "reason": "Explicitly trusted host input; no self-authentication"
    },
    "capabilities-behaviour-actions": {
      "status": "required",
      "reason": "Host administers; no data role infers authority"
    },
    "context-evidence": {
      "status": "required",
      "reason": "External appointment/deployment evidence; never credentials"
    }
  },
  "Evaluation": {
    "identity-class": {
      "status": "required",
      "reason": "Ephemeral artifact keyed by inputs/query/profile, not a new subject"
    },
    "direct-properties": {
      "status": "required",
      "reason": "Status, value or null, IDs, route, query axes, digests"
    },
    "recognition-observation": {
      "status": "required",
      "reason": "Deterministic under full trusted inputs; preference not truth"
    },
    "capabilities-behaviour-actions": {
      "status": "required",
      "reason": "Read and propose follow-up; no autonomous notification"
    },
    "context-evidence": {
      "status": "required",
      "reason": "Exact authority pins and known input digest"
    }
  }
}

```


## FILE mastership-and-rights.yaml
```
{
  "rows": [
    {
      "fact": "governance appointment/rule/grant",
      "semanticOwner": "Scoped governance authority",
      "masterSystem": "Deployment governance register",
      "writer": "Explicit scope/predicate governor",
      "readerPurpose": "Full-register reader + admitted purpose; all-or-deny",
      "validTime": "Explicit half-open fact/rule term",
      "provenance": "Evidence refs + immutable revision digest",
      "conflictPolicy": "No recency winner; unknown/authority-contested/contested as applicable",
      "retention": "Reference retains history; deployment retention and erasure are unresolved"
    },
    {
      "fact": "source observation",
      "semanticOwner": "Originating source accountable party",
      "masterSystem": "Source assertion register through admitted writer",
      "writer": "Writer named in current separate WriteGrant",
      "readerPurpose": "Full-register reader + admitted purpose; all-or-deny",
      "validTime": "Explicit half-open fact/rule term",
      "provenance": "Evidence refs + immutable revision digest",
      "conflictPolicy": "No recency winner; unknown/authority-contested/contested as applicable",
      "retention": "Reference retains history; deployment retention and erasure are unresolved"
    },
    {
      "fact": "definition authority reference",
      "semanticOwner": "External predicate-governance owner",
      "masterSystem": "External definition registry; not verified here",
      "writer": "Scoped governor records reference only",
      "readerPurpose": "Full-register reader + admitted purpose; all-or-deny",
      "validTime": "Explicit half-open fact/rule term",
      "provenance": "Evidence refs + immutable revision digest",
      "conflictPolicy": "No recency winner; unknown/authority-contested/contested as applicable",
      "retention": "Reference retains history; deployment retention and erasure are unresolved"
    },
    {
      "fact": "query output",
      "semanticOwner": "No new master; derived from pins",
      "masterSystem": "No independent master",
      "writer": "Evaluator computes; cannot change input",
      "readerPurpose": "Full-register reader + admitted purpose; all-or-deny",
      "validTime": "Explicit half-open fact/rule term",
      "provenance": "Evidence refs + immutable revision digest",
      "conflictPolicy": "No recency winner; unknown/authority-contested/contested as applicable",
      "retention": "Reference retains history; deployment retention and erasure are unresolved"
    }
  ],
  "warning": "Declarations checked by a reference function, not an authenticated authorization service"
}

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
      "relation": "pattern-alignment",
      "specSha256": "a09261ca365d2e82716705a27d5e46cca7faef8fc22d90fcf3b94a53ef729358"
    },
    {
      "id": "WM-XCT-002",
      "version": "0.3.0-research.1",
      "relation": "pattern-alignment",
      "specSha256": "9085d977567f3e1fc0b9bb27c6a7c517139f5972a1b95bf4a2bedccdb10bf2db"
    },
    {
      "id": "WM-XCT-012",
      "version": "0.3.0-research.1",
      "relation": "pattern-alignment",
      "specSha256": "aa6155354c55a87ab837ec9bd47f796ca582309fe383f1afffb802dafff7ecb5"
    }
  ],
  "nativeBinding": "WM-XCT-001 discovery association, explicitly bounded companion extension; no subtype assertion",
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

END OF FROZEN AUDIT INPUT
