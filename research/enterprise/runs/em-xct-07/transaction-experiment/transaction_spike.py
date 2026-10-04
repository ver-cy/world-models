"""Research-only synthetic transaction experiment; NOT a Vercy model or auth service.

All state is an invented workspace in one local SQLite file. Sessions, policies,
time and IDs are trusted TEST INPUTS. No real identity verification or remote
effect exists. Callers with file/code access control this entire experiment.
"""
from contextlib import contextmanager, closing
from pathlib import Path
import hashlib, json, sqlite3, uuid

class Refused(Exception): pass
class ResponseLost(Exception): pass

FIELDS={'dimension','executor','epoch','key','definition','resource','revision',
        'actor','principal','purpose','expires','value','mode'}
def encoded(value):
    return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode('utf-8')
def digest(value): return hashlib.sha256(encoded(value)).hexdigest()
def validate(req):
    if type(req)!=dict or set(req)!=FIELDS: raise Refused('shape')
    for k in FIELDS-{'revision','expires','value'}:
        if type(req[k])!=str or not 1<=len(req[k])<=200: raise Refused('shape')
    if type(req['revision'])!=int or req['revision']<0 or type(req['expires'])!=int: raise Refused('shape')
    if req['mode']!='request': raise Refused('proposal-not-execution')
    if type(req['value'])!=list or len(req['value'])>20 or any(type(x)!=str or len(x)>200 for x in req['value']): raise Refused('shape')
    try: raw=encoded(req)
    except (UnicodeError,ValueError): raise Refused('encoding') from None
    return raw

def create_fixture(path,profile='startup'):
    path=Path(path)
    if path.exists(): raise Refused('fixture-already-exists')
    actor='urn:demo:'+('founder' if profile=='startup' else 'employee' if profile=='matrix' else 'ai-service')
    principal=actor if profile=='startup' else 'urn:demo:unit' if profile=='matrix' else 'urn:demo:service-owner'
    cfg={'dimension':'urn:demo:dimension:'+profile,'executor':'urn:demo:executor:'+profile,'epoch':uuid.uuid4().hex,'definition':'urn:demo:labels-set:v1','resource':'urn:demo:workspace:'+profile}
    policy={'actor':actor,'principal':principal,'purpose':'demo-labels','execute':True,'read':True,'until':1000,'revision':1,'delegated':profile!='startup','owner':'urn:demo:accountable-owner'}
    with closing(sqlite3.connect(path)) as c, c:
        c.executescript('''PRAGMA journal_mode=DELETE; PRAGMA synchronous=FULL;
        CREATE TABLE metadata (k TEXT PRIMARY KEY, value TEXT NOT NULL);
        CREATE TABLE policies (id INTEGER PRIMARY KEY CHECK(id=1), body TEXT NOT NULL);
        CREATE TABLE resource (id INTEGER PRIMARY KEY CHECK(id=1), revision INTEGER NOT NULL, body TEXT NOT NULL);
        CREATE TABLE requests (key TEXT PRIMARY KEY, digest TEXT NOT NULL, body BLOB NOT NULL, request_id TEXT NOT NULL, receipt TEXT, retired INTEGER NOT NULL DEFAULT 0);
        CREATE TABLE effects (id TEXT PRIMARY KEY, request_id TEXT UNIQUE NOT NULL, before_value TEXT NOT NULL, after_value TEXT NOT NULL);
        CREATE TABLE attempts (id TEXT PRIMARY KEY, request_id TEXT NOT NULL, observed_at INTEGER NOT NULL, policy_revision INTEGER NOT NULL, replay INTEGER NOT NULL);
        ''')
        c.executemany('INSERT INTO metadata VALUES (?,?)',cfg.items())
        c.execute('INSERT INTO policies VALUES(1,?)',(json.dumps(policy),))
        c.execute('INSERT INTO resource VALUES(1,0,?)',(json.dumps(['draft']),))
    return {**cfg,'key':'retry-1','revision':0,'actor':actor,'principal':principal,'purpose':'demo-labels','expires':900,'value':['alpha','beta'],'mode':'request'}

@contextmanager
def transaction(path):
    # mode=rw refuses to invent an empty history if the database was lost.
    c=sqlite3.connect(Path(path).resolve().as_uri()+'?mode=rw',uri=True,timeout=10,isolation_level=None)
    try:
        c.execute('PRAGMA synchronous=FULL')
        c.execute('BEGIN IMMEDIATE')
        yield c
        c.execute('COMMIT')
    except BaseException:
        if c.in_transaction: c.execute('ROLLBACK')
        raise
    finally: c.close()

def policy_change(path,**changes):
    """Trusted fixture administration only, serialized with execution and reads."""
    with transaction(path) as c:
        p=json.loads(c.execute('SELECT body FROM policies').fetchone()[0])
        p.update(changes);p['revision']+=1
        c.execute('UPDATE policies SET body=?',(json.dumps(p),))

def authorize(c,req,session,now,operation):
    p=json.loads(c.execute('SELECT body FROM policies').fetchone()[0])
    ok=(session==req['actor']==p['actor'] and req['principal']==p['principal']
        and req['purpose']==p['purpose'] and type(now)==int and now<p['until']
        and p[operation] is True and (req['actor']==req['principal'] or p['delegated'] is True))
    if not ok: raise Refused('not-authorized')
    return p

def locate(c,req):
    cfg=dict(c.execute('SELECT k,value FROM metadata'))
    if any(req[k]!=v for k,v in cfg.items()): raise Refused('scope')
    return c.execute('SELECT digest,body,request_id,receipt,retired FROM requests WHERE key=?',(req['key'],)).fetchone()

def submit(path,req,session,now,failpoint=None):
    """Set an invented ordered label list; receipt and effect commit together.

    Every submit, including retry, requires current execute authority. Return of
    its result additionally requires current read authority. Different current
    policy versions are observations, not immutable-intent fields.
    """
    raw=validate(req);fp=hashlib.sha256(raw).hexdigest()
    with transaction(path) as c:
        # Authorization first: denied caller cannot probe retry state or scope.
        p=authorize(c,req,session,now,'execute')
        prior=locate(c,req)
        if prior:
            if prior[4]: raise Refused('retired-key')
            if prior[0]!=fp or bytes(prior[1])!=raw: raise Refused('key-conflict')
            rid=prior[2];receipt=json.loads(prior[3]);replay=True
        else:
            if now>=req['expires']: raise Refused('expired-request')
            revision,old=c.execute('SELECT revision,body FROM resource').fetchone()
            if revision!=req['revision']: raise Refused('stale-resource')
            rid='urn:demo:request:'+uuid.uuid4().hex;effect='urn:demo:effect:'+uuid.uuid4().hex
            receipt={'requestId':rid,'effectId':effect,'resourceRevision':revision+1,'value':req['value']}
            c.execute('UPDATE resource SET revision=?,body=?',(revision+1,json.dumps(req['value'])))
            if failpoint=='between-effect-and-receipt': raise RuntimeError('injected-before-commit')
            c.execute('INSERT INTO effects VALUES(?,?,?,?)',(effect,rid,old,json.dumps(req['value'])))
            c.execute('INSERT INTO requests(key,digest,body,request_id,receipt) VALUES(?,?,?,?,?)',(req['key'],fp,raw,rid,json.dumps(receipt)))
            replay=False
        c.execute('INSERT INTO attempts VALUES(?,?,?,?,?)',('urn:demo:attempt:'+uuid.uuid4().hex,rid,now,p['revision'],int(replay)))
        # A denial affects disclosure, not whether the effect already committed.
        try: authorize(c,req,session,now,'read')
        except Refused: result={'outcome':'withheld'}
        else: result={'outcome':'observed','receipt':receipt,'replay':replay}
    if failpoint=='after-commit-before-response': raise ResponseLost('caller-outcome-unknown; reconcile')
    return result

def read_result(path,req,session,now):
    raw=validate(req)
    with transaction(path) as c:
        authorize(c,req,session,now,'read')
        prior=locate(c,req)
        if not prior: return {'outcome':'not-found-in-current-retained-store'}
        if prior[4]: raise Refused('retired-key')
        if prior[0]!=hashlib.sha256(raw).hexdigest() or bytes(prior[1])!=raw: raise Refused('key-conflict')
        return {'outcome':'observed','receipt':json.loads(prior[3])}

def retire_key(path,key):
    """Trusted fixture administration: keep key and intent pin; no silent reuse."""
    with transaction(path) as c:
        c.execute('UPDATE requests SET retired=1,receipt=NULL WHERE key=?',(key,))

def inspect_fixture(path):
    """Privileged test inspection, not an end-user disclosure endpoint."""
    with transaction(path) as c:
        rev,value=c.execute('SELECT revision,body FROM resource').fetchone()
        return {'revision':rev,'value':json.loads(value),**{n:c.execute('SELECT COUNT(*) FROM '+n).fetchone()[0] for n in ['requests','effects','attempts']}}
