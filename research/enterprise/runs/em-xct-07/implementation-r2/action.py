"""Enterprise Action Requests 0.1.0 candidate: a bounded synthetic local adapter.

Host administration, authenticated actor IDs, time, policy verification and file
access are TRUSTED fixture inputs, not production authentication. No network,
shell, financial, personnel or other real-world effect is supported.
"""
from contextlib import contextmanager
from pathlib import Path
import hashlib
import json
import re
import sqlite3
import uuid
from jsonschema import Draft202012Validator

MAX_BYTES=131072
MAX_ROWS=10000
SCHEMA=json.loads(Path(__file__).with_name('action.schema.json').read_text(encoding='utf-8'))
WITHHELD={'status':'withheld'}
STATES={'pending','committed','cancelled','expired','rejected-precondition'}

class Refused(ValueError): pass
class ResponseLost(RuntimeError): pass

def require(condition, code):
    if not condition: raise Refused(code)

def _bounded(value, depth=0):
    require(depth<=24,'wire-depth')
    if value is None or type(value) is bool: return
    if type(value) is int:
        require(abs(value)<=9007199254740991,'wire-integer'); return
    if type(value) is str:
        require(len(value)<=4096 and not any(0xD800<=ord(c)<=0xDFFF for c in value),'wire-string'); return
    if type(value) is list:
        require(len(value)<=256,'wire-array')
        for item in value: _bounded(item,depth+1)
        return
    if type(value) is dict:
        require(len(value)<=128 and all(type(k) is str for k in value),'wire-object')
        for k,v in value.items(): _bounded(k,depth+1); _bounded(v,depth+1)
        return
    raise Refused('wire-type')

def encoded(value):
    """Python code-point sorted, ordered arrays, UTF-8; explicitly NOT JCS."""
    _bounded(value)
    result=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode('utf-8')
    require(len(result)<=MAX_BYTES,'wire-bytes')
    return result

def digest(value): return hashlib.sha256(encoded(value)).hexdigest()

def _pairs(items):
    result={}
    for k,v in items:
        require(k not in result,'duplicate-key'); result[k]=v
    return result

def parse(raw):
    require(type(raw) in (str,bytes),'wire-input')
    try:
        if isinstance(raw,bytes): raw=raw.decode('utf-8',errors='strict')
        require(len(raw.encode('utf-8'))<=MAX_BYTES,'wire-bytes')
        def bad(_): raise Refused('wire-number')
        value=json.loads(raw,object_pairs_hook=_pairs,parse_float=bad,parse_constant=bad)
        encoded(value)
        return value
    except (UnicodeError,json.JSONDecodeError,RecursionError): raise Refused('wire-json') from None

def validate(kind, value):
    encoded(value)
    validator=Draft202012Validator({'$ref':'#/$defs/'+kind,'$defs':SCHEMA['$defs']})
    require(not list(validator.iter_errors(value)),'schema-'+kind)
    if kind=='ActionDefinition':
        require(value['validFrom']<value['validUntil'],'definition-window')
        if value['mode']=='synthetic-executable':
            require(value['parameterContract']=='ordered-label-list/1' and value['targetType']=='urn:vercy:synthetic:OrderedLabelResource' and value['adapter']=='local-sqlite-ordered-labels/1' and value['compensation']=='new-request-restores-before-labels-at-exact-after-revision','executable-definition')
            require(value['precondition']=='resource-revision-and-retained-compensation-v1' and value['effectBoundary']=='local-atomic-ordered-label-replacement-v1','executable-boundary')
        else:
            require(type(value['parameterContract']) is dict and value['adapter']=='none' and value['compensation']=='external-unspecified','descriptive-definition')
    if kind=='Policy':
        for rule in value:
            require((rule['actorId']==rule['principalId'])==(rule['mode']=='self'),'representation-mode')
            for name in ('principalScope','delegateScope'):
                require(rule[name]['validFrom']<rule[name]['validUntil'],'scope-window')
    return value

def definition_ref(definition):
    validate('ActionDefinition',definition)
    return {'definitionId':definition['definitionId'],'version':definition['version'],'sha256':digest(definition)}

def matching_rules(policy,intent,action,now):
    matches=[]
    for rule in policy:
        if (rule['actorId'],rule['principalId'])!=(intent['actorId'],intent['principalId']): continue
        def contains(scope):
            return all(scope[k]==intent[k] for k in ('dimensionId','definition','resourceId','purpose','audience')) and action in scope['actions'] and scope['validFrom']<=now<scope['validUntil']
        if contains(rule['principalScope']) and contains(rule['delegateScope']): matches.append(digest(rule))
    return sorted(set(matches))

def _json(value): return encoded(value).decode('utf-8')
def _id(prefix): return prefix+'.'+uuid.uuid4().hex

SQL='''
CREATE TABLE meta (id INTEGER PRIMARY KEY CHECK(id=1), dimension TEXT NOT NULL, issuer TEXT NOT NULL, epoch TEXT NOT NULL, clock INTEGER NOT NULL, policy_revision INTEGER NOT NULL, control_sequence INTEGER NOT NULL);
CREATE TABLE definitions (id TEXT NOT NULL, version TEXT NOT NULL, body TEXT NOT NULL, digest TEXT NOT NULL, available INTEGER NOT NULL, recorded_at INTEGER NOT NULL, control_sequence INTEGER NOT NULL, retired_sequence INTEGER, ordinal INTEGER PRIMARY KEY AUTOINCREMENT, UNIQUE(id,version));
CREATE TABLE policies (revision INTEGER PRIMARY KEY, body TEXT NOT NULL, recorded_at INTEGER NOT NULL, control_sequence INTEGER NOT NULL);
CREATE TABLE resources (id TEXT NOT NULL, revision INTEGER NOT NULL, labels TEXT NOT NULL, recorded_at INTEGER NOT NULL, control_sequence INTEGER NOT NULL, PRIMARY KEY(id,revision));
CREATE TABLE requests (id TEXT PRIMARY KEY, slot TEXT UNIQUE NOT NULL, body TEXT NOT NULL);
CREATE TABLE events (sequence INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT UNIQUE NOT NULL, body TEXT NOT NULL);
'''

class Executor:
    """One database is the authoritative fixture. Public methods return redacted results.

    The host must construct authenticated actor/time inputs and isolate admin API,
    exports and database access. The epoch pin detects a wrong store, not a coherent
    rollback. Restored stores require external continuity reconciliation before use.
    """
    def __init__(self,path,expected_epoch):
        self.path=Path(path).resolve(); self.expected_epoch=expected_epoch

    @classmethod
    def create(cls,path,dimension,issuer,now):
        require(re.fullmatch(SCHEMA['$defs']['Intent']['properties']['dimensionId']['pattern'],dimension) is not None,'dimension-id')
        require(re.fullmatch(SCHEMA['$defs']['Intent']['properties']['dimensionId']['pattern'],issuer) is not None,'issuer-id')
        cls._time(now)
        path=Path(path).resolve(); path.parent.mkdir(parents=True,exist_ok=True)
        # Exclusive create, so accidental use never truncates a prior history.
        with path.open('xb'): pass
        epoch=_id('epoch')
        c=sqlite3.connect(path)
        try:
            c.executescript(SQL)
            c.execute('INSERT INTO meta VALUES(1,?,?,?,?,0,0)',(dimension,issuer,epoch,now))
            c.execute('INSERT INTO policies VALUES(0,?,?,0)',('[]',now)); c.commit()
        finally: c.close()
        return cls(path,epoch)

    @staticmethod
    def _time(now): require(type(now) is int and 946684800<=now<=4102444800,'host-time')

    @contextmanager
    def _tx(self,now):
        self._time(now)
        c=sqlite3.connect(self.path.as_uri()+'?mode=rw',uri=True,timeout=15,isolation_level=None)
        c.row_factory=sqlite3.Row
        try:
            c.execute('PRAGMA synchronous=FULL'); c.execute('BEGIN IMMEDIATE')
            meta=dict(c.execute('SELECT * FROM meta WHERE id=1').fetchone())
            require(meta['epoch']==self.expected_epoch,'store-epoch')
            require(now>=meta['clock'],'host-clock-regression')
            mseq=meta['control_sequence']+1
            require(mseq<=9007199254740991,'control-sequence-overflow')
            c.execute('UPDATE meta SET clock=?,control_sequence=? WHERE id=1',(now,mseq))
            meta['control_sequence']=mseq; meta['clock']=now
            yield c,meta
            # Check before COMMIT: an overflowing operation, including its effect,
            # request and clock increment, rolls back as one unit.
            for table in ('definitions','policies','resources','requests','events'):
                require(c.execute('SELECT COUNT(*) FROM '+table).fetchone()[0]<=MAX_ROWS,'store-capacity')
            c.execute('COMMIT')
        except BaseException:
            if c.in_transaction: c.execute('ROLLBACK')
            raise
        finally: c.close()

    def set_policy(self,policy,now):
        """TRUSTED fixture host administration: verify issuer standing/basis externally."""
        validate('Policy',policy)
        with self._tx(now) as (c,m):
            rev=m['policy_revision']+1
            # Reserve the final policy row for a host-wide revocation. Never
            # overwrite older policy evidence or silently create a new store.
            require(not policy or rev<MAX_ROWS-1,'policy-revocation-reserve')
            c.execute('INSERT INTO policies VALUES(?,?,?,?)',(rev,_json(policy),now,m['control_sequence']))
            c.execute('UPDATE meta SET policy_revision=? WHERE id=1',(rev,))
            return rev

    def add_definition(self,definition,now):
        validate('ActionDefinition',definition)
        with self._tx(now) as (c,m):
            require(not c.execute('SELECT 1 FROM resources WHERE id=?',(definition['definitionId'],)).fetchone(),'object-kind-collision')
            old=c.execute('SELECT body FROM definitions WHERE id=? AND version=?',(definition['definitionId'],definition['version'])).fetchone()
            if old:
                require(old['body']==_json(definition),'definition-version-conflict'); return
            c.execute('INSERT INTO definitions(id,version,body,digest,available,recorded_at,control_sequence) VALUES(?,?,?,?,1,?,?)',
                      (definition['definitionId'],definition['version'],_json(definition),digest(definition),now,m['control_sequence']))

    def retire_definition(self,reference,now):
        validate('DefinitionRef',reference)
        with self._tx(now) as (c,m):
            require(c.execute('UPDATE definitions SET available=0,retired_sequence=COALESCE(retired_sequence,?) WHERE id=? AND version=? AND digest=?',
                  (m['control_sequence'],reference['definitionId'],reference['version'],reference['sha256'])).rowcount==1,'unknown-definition')

    def add_resource(self,resource_id,labels,now):
        validate('Labels',labels)
        require(type(resource_id) is str and re.fullmatch(SCHEMA['$defs']['Intent']['properties']['resourceId']['pattern'],resource_id) is not None,'resource-id')
        with self._tx(now) as (c,m):
            require(not c.execute('SELECT 1 FROM definitions WHERE id=?',(resource_id,)).fetchone(),'object-kind-collision')
            require(not c.execute('SELECT 1 FROM resources WHERE id=?',(resource_id,)).fetchone(),'resource-exists')
            c.execute('INSERT INTO resources VALUES(?,0,?,?,?)',(resource_id,_json(labels),now,m['control_sequence']))

    @staticmethod
    def _policy(c,m): return json.loads(c.execute('SELECT body FROM policies WHERE revision=?',(m['policy_revision'],)).fetchone()[0])
    @staticmethod
    def _slot(actor,key):
        require(type(key) is str and re.fullmatch('[A-Za-z0-9._:-]{8,128}',key) is not None,'retry-key')
        return digest({'actorId':actor,'key':key})
    @staticmethod
    def _get(c,slot):
        row=c.execute('SELECT body FROM requests WHERE slot=?',(slot,)).fetchone()
        return json.loads(row[0]) if row else None
    @staticmethod
    def _save(c,request): c.execute('UPDATE requests SET body=? WHERE id=?',(_json(request),request['requestId']))
    @staticmethod
    def _event(c,m,request,kind,payload,now):
        eid=_id('evt')
        cur=c.execute('INSERT INTO events(id,body) VALUES(?,?)',(eid,'{}'))
        e={'eventId':eid,'sequence':cur.lastrowid,'controlSequence':m['control_sequence'],'kind':kind,'requestId':request['requestId'],'recordedAt':now,'issuerId':m['issuer'],'payload':payload}
        validate('Event',e)
        c.execute('UPDATE events SET body=? WHERE sequence=?',(_json(e),cur.lastrowid)); return e
    @staticmethod
    def _definition(c,intent,now):
        pin=intent['definition']
        row=c.execute('SELECT * FROM definitions WHERE id=? AND version=? AND digest=?',(pin['definitionId'],pin['version'],pin['sha256'])).fetchone()
        if not row: return None,False
        d=json.loads(row['body'])
        return d,bool(row['available'] and d['validFrom']<=now<d['validUntil'])
    @staticmethod
    def _out(c,request,readable,code=None):
        if not readable: return dict(WITHHELD)
        if code and (not request or code=='key-conflict'): return {'status':code}
        result={'status':'key-retired' if request['keyRetired'] else request['state'],'requestId':request['requestId'],'intentDigest':request['intentDigest']}
        if code: result.update(status=code,requestState=request['state'])
        if request['receiptId']:
            result['receipt']=json.loads(c.execute('SELECT body FROM events WHERE id=?',(request['receiptId'],)).fetchone()[0])
        return result

    def dispatch(self,raw,key,actor,now,*,_fault=None):
        """Admit/try a closed synthetic intent. Key is per authenticated actor/store.

        _fault is test instrumentation, never an untrusted transport parameter.
        Malformed, absent and unauthorized diagnostics share the withheld response.
        A response does not disclose whether execute-only actions produced effects.
        """
        try:
            intent=validate('Intent',parse(raw)); require(intent['actorId']==actor,'authenticated-actor')
            slot=self._slot(actor,key)
            with self._tx(now) as (c,m):
                require(intent['dimensionId']==m['dimension'],'dimension')
                policy=self._policy(c,m); request=self._get(c,slot)
                readable=bool(matching_rules(policy,intent,'read',now))
                if request:
                    readable=readable and bool(matching_rules(policy,request['intent'],'read',now))
                    if request['intentDigest']!=digest(intent) or encoded(request['intent'])!=encoded(intent):
                        return self._out(c,request,readable,'key-conflict')
                    if request['keyRetired']: return self._out(c,request,readable)
                definition,available=self._definition(c,intent,now)
                if request and not any(matching_rules(policy,intent,a,now) for a in ('submit','execute','read','cancel','observe')):
                    return dict(WITHHELD)
                if not request:
                    if not matching_rules(policy,intent,'submit',now): return dict(WITHHELD)
                    if not definition or definition['mode']!='synthetic-executable': return self._out(c,None,readable,'definition-not-executable')
                    if intent['purpose'] not in definition['purposes']: return self._out(c,None,readable,'definition-purpose')
                    request={'requestId':_id('req'),'keyHash':slot,'intentDigest':digest(intent),'intent':intent,'submittedAt':now,'submissionEventId':_id('placeholder'),'state':'pending','receiptId':None,'keyRetired':False}
                    e=self._event(c,m,request,'submission',{'intentDigest':request['intentDigest']},now)
                    request['submissionEventId']=e['eventId']
                    c.execute('INSERT INTO requests VALUES(?,?,?)',(request['requestId'],slot,_json(request)))
                self._event(c,m,request,'delivery',{'intentDigest':request['intentDigest']},now)
                matches=matching_rules(policy,intent,'execute',now)
                allowed=bool(matches and available)
                trial=self._event(c,m,request,'try',{'decision':{'action':'execute','policyRevision':m['policy_revision'],'allowed':allowed,'matchedRuleDigests':matches,'definitionAvailable':available}},now)
                if request['state']!='pending': return self._out(c,request,readable,None if allowed else 'current-execution-denied')
                if now>=intent['expiresAt']:
                    self._terminal(c,m,request,'expired','deadline',now,trial['eventId'])
                elif not allowed: return self._out(c,request,readable,'current-execution-denied')
                else:
                    row=c.execute('SELECT * FROM resources WHERE id=? ORDER BY revision DESC LIMIT 1',(intent['resourceId'],)).fetchone()
                    reason='resource-revision'
                    valid=bool(row and row['revision']==intent['expectedRevision'])
                    if intent['compensatesReceiptId']:
                        old=c.execute('SELECT body FROM events WHERE id=?',(intent['compensatesReceiptId'],)).fetchone()
                        original=json.loads(old[0]) if old else None
                        p=original['payload'] if original else {}
                        original_request=c.execute('SELECT body FROM requests WHERE id=?',(original['requestId'],)).fetchone() if original else None
                        oi=json.loads(original_request[0])['intent'] if original_request else {}
                        same_context=all(oi.get(k)==intent[k] for k in ('actorId','principalId','purpose','audience','dimensionId'))
                        valid=bool(valid and original and original['kind']=='receipt' and same_context and p['resourceId']==intent['resourceId'] and p['definition']==intent['definition'] and p['afterRevision']==intent['expectedRevision'] and p['beforeLabels']==intent['parameters']['labels'])
                        reason='compensation-precondition'
                    if not valid: self._terminal(c,m,request,'rejected-precondition',reason,now,trial['eventId'])
                    else:
                        if _fault=='before-effect': raise Refused('injected-rollback')
                        after=row['revision']+1
                        require(after<=9007199254740991,'revision-overflow')
                        c.execute('INSERT INTO resources VALUES(?,?,?,?,?)',(intent['resourceId'],after,_json(intent['parameters']['labels']),now,m['control_sequence']))
                        if _fault=='after-effect': raise Refused('injected-rollback')
                        receipt=self._event(c,m,request,'receipt',{'definition':intent['definition'],'resourceId':intent['resourceId'],'beforeRevision':row['revision'],'afterRevision':after,'beforeLabels':json.loads(row['labels']),'afterLabels':intent['parameters']['labels'],'compensatesReceiptId':intent['compensatesReceiptId'],'tryEventId':trial['eventId']},now)
                        request['receiptId']=receipt['eventId']; request['state']='committed'; self._save(c,request)
                result=self._out(c,request,readable)
            if _fault=='after-commit': raise ResponseLost('Committed transaction; caller did not receive the response. Reconcile using the SAME key.')
            return result
        except (ValueError,sqlite3.Error,KeyError,TypeError,IndexError,AttributeError,OverflowError,RecursionError): return dict(WITHHELD)

    def _terminal(self,c,m,request,state,reason,now,trial=None):
        require(request['state']=='pending','terminal-transition')
        self._event(c,m,request,'disposition',{'from':'pending','to':state,'reason':reason,'tryEventId':trial},now)
        request['state']=state; self._save(c,request)

    def lookup(self,key,actor,now):
        try:
            slot=self._slot(actor,key)
            with self._tx(now) as (c,m):
                request=self._get(c,slot)
                if not request: return dict(WITHHELD)
                return self._out(c,request,bool(matching_rules(self._policy(c,m),request['intent'],'read',now)))
        except (ValueError,sqlite3.Error,KeyError,TypeError,IndexError,AttributeError,OverflowError,RecursionError): return dict(WITHHELD)

    def cancel(self,key,actor,now):
        try:
            slot=self._slot(actor,key)
            with self._tx(now) as (c,m):
                r=self._get(c,slot)
                if not r: return dict(WITHHELD)
                policy=self._policy(c,m); readable=bool(matching_rules(policy,r['intent'],'read',now))
                if r['keyRetired']: return self._out(c,r,readable)
                matches=matching_rules(policy,r['intent'],'cancel',now)
                if not matches and not readable: return dict(WITHHELD)
                trial=self._event(c,m,r,'try',{'decision':{'action':'cancel','policyRevision':m['policy_revision'],'allowed':bool(matches),'matchedRuleDigests':matches,'definitionAvailable':self._definition(c,r['intent'],now)[1]}},now)
                if not matches: return self._out(c,r,readable,'current-cancellation-denied')
                if r['state']=='pending':
                    state='expired' if now>=r['intent']['expiresAt'] else 'cancelled'
                    self._terminal(c,m,r,state,'deadline' if state=='expired' else 'authorized-cancellation',now,trial['eventId'])
                return self._out(c,r,readable)
        except (ValueError,sqlite3.Error,KeyError,TypeError,IndexError,AttributeError,OverflowError,RecursionError): return dict(WITHHELD)

    def observe(self,key,actor,now,claim,reason,corrects=None):
        try:
            slot=self._slot(actor,key)
            with self._tx(now) as (c,m):
                r=self._get(c,slot)
                if not r: return dict(WITHHELD)
                policy=self._policy(c,m); readable=bool(matching_rules(policy,r['intent'],'read',now))
                matches=matching_rules(policy,r['intent'],'observe',now)
                if not readable or not matches or r['keyRetired']: return dict(WITHHELD)
                if corrects:
                    old=c.execute('SELECT body FROM events WHERE id=?',(corrects,)).fetchone()
                    previous=json.loads(old[0]) if old else None
                    require(previous and previous['kind']=='observation' and previous['requestId']==r['requestId'] and previous['payload']['observerId']==actor,'observation-predecessor')
                    observations=[json.loads(x[0]) for x in c.execute('SELECT body FROM events')]
                    require(not any(x['kind']=='observation' and x['payload']['correctsEventId']==corrects for x in observations),'observation-already-corrected')
                trial=self._event(c,m,r,'try',{'decision':{'action':'observe','policyRevision':m['policy_revision'],'allowed':True,'matchedRuleDigests':matches,'definitionAvailable':self._definition(c,r['intent'],now)[1]}},now)
                e=self._event(c,m,r,'observation',{'observerId':actor,'claim':claim,'reason':reason,'correctsEventId':corrects,'tryEventId':trial['eventId']},now)
                return {'status':'recorded','event':e}
        except (ValueError,sqlite3.Error,KeyError,TypeError,IndexError,AttributeError,OverflowError,RecursionError): return dict(WITHHELD)

    def retire_key(self,key,actor,now):
        """TRUSTED retention administration: retain immutable intent/receipt forever here."""
        with self._tx(now) as (c,m):
            r=self._get(c,self._slot(actor,key)); require(r and r['state']!='pending','retire-terminal-only')
            if not r['keyRetired']:
                self._event(c,m,r,'key-retirement',{'retained':True},now)
                r['keyRetired']=True; self._save(c,r)

    def snapshot(self,now):
        """Privileged evidence export. NEVER expose this method as a caller endpoint."""
        with self._tx(now) as (c,m):
            m['clock']=now
            return {'format':'enterprise-action-snapshot/0.1.0','meta':m,
                'definitions':[dict(x) for x in c.execute('SELECT * FROM definitions ORDER BY ordinal')],
                'policies':[dict(x) for x in c.execute('SELECT * FROM policies ORDER BY revision')],
                'resources':[dict(x) for x in c.execute('SELECT * FROM resources ORDER BY id,revision')],
                'requests':[json.loads(x[0]) for x in c.execute('SELECT body FROM requests ORDER BY id')],
                'events':[json.loads(x[0]) for x in c.execute('SELECT body FROM events ORDER BY sequence')]}
