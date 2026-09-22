"""D1 request-shape and native-envelope experiment; no execution or authority."""
from pathlib import Path
import argparse, copy, datetime, hashlib, json, sys
from jsonschema import Draft202012Validator, FormatChecker

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--native-schema-dir',type=Path,required=True)
parser.add_argument('--output',type=Path,default=Path(__file__).parent/'request-shape-experiment')
args=parser.parse_args()
W=args.output;W.mkdir(parents=True,exist_ok=True)
S=args.native_schema_dir

def encoded(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode('utf-8')
def sha(x):return hashlib.sha256(encoded(x)).hexdigest()
def save(n,x):
    p=W/n;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def obj(properties):return {'type':'object','properties':properties,'required':list(properties),'additionalProperties':False}
def ref(n):return {'$ref':'#/$defs/'+n}
def nullable(n):return {'anyOf':[ref(n),{'type':'null'}]}

ident={'type':'string','minLength':3,'maxLength':120,'pattern':'^[A-Za-z0-9][A-Za-z0-9._:-]{2,119}$'}
uri={'type':'string','minLength':3,'maxLength':500,'format':'uri'}
timestamp={'type':'string','pattern':r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$','format':'date-time'}
pin={'type':'string','pattern':'^[0-9a-f]{64}$'}
versioned=obj({'id':ref('uri'),'revision':{'type':'string','minLength':1,'maxLength':100},'sha256':pin})
labels={'type':'array','maxItems':20,'items':{'type':'string','maxLength':200}}
intent=obj({'requestId':ref('nativeId'),'dimensionId':ref('uri'),'executorId':ref('uri'),'executorEpoch':ref('nativeId'),'retryKey':ref('nativeId'),'definitionRef':ref('versionedRef'),'actorId':ref('uri'),'principalId':ref('uri'),'purpose':{'type':'string','minLength':1,'maxLength':100},'resourceId':ref('nativeId'),'expectedRevision':{'type':'integer','minimum':0,'maximum':9007199254740991},'expiresAt':ref('timestamp'),'parameters':obj({'labels':labels}),'basisRef':nullable('versionedRef'),'proposalEventId':nullable('nativeId'),'compensatesReceiptId':nullable('nativeId')})
admission=obj({'submittedAt':ref('timestamp'),'submittedBy':ref('uri'),'admittedDefinitionRef':ref('versionedRef'),'intentDigest':pin,'submissionEventId':ref('nativeId')})
schema={'$schema':'https://json-schema.org/draft/2020-12/schema','$id':'urn:vercy:research:em-xct-07:request:D1','title':'Provisional D1 ActionRequest; no authorization or execution','$defs':{'nativeId':ident,'uri':uri,'timestamp':timestamp,'versionedRef':versioned},**obj({'schemaVersion':{'const':'D1'},'intent':intent,'admission':admission})}
Draft202012Validator.check_schema(schema)
validator=Draft202012Validator(schema,format_checker=FormatChecker())
save('request.schema.json',schema)

definition={'id':'urn:vercy:synthetic:ordered-label-replacement','revision':'D1','operation':'replace-ordered-labels','parameters':obj({'labels':labels}),'effectBoundary':'one synthetic resource in one local transaction; not implemented by this shape experiment'}
definition_ref={'id':definition['id'],'revision':'D1','sha256':sha(definition)}
# Exact published artifact bytes are canonical here, matching the definition pin.
(W/'definition.json').write_bytes(encoded(definition))

def validate(x):
    validator.validate(x)
    i=x['intent'];a=x['admission']
    if type(i['expectedRevision']) is not int:raise ValueError('integer encoding required')
    raw=encoded(i) # Rejects unpaired surrogates during UTF-8 encoding.
    if hashlib.sha256(raw).hexdigest()!=a['intentDigest']:raise ValueError('intent digest')
    if i['definitionRef']!=definition_ref or a['admittedDefinitionRef']!=definition_ref:raise ValueError('definition pin')
    if a['submittedBy']!=i['actorId']:raise ValueError('first-adapter submitter restriction')
    if a['submittedAt']>=i['expiresAt']:raise ValueError('admission after deadline')
    return raw

outer={kind:Draft202012Validator(json.loads((S/(kind+'.schema.json')).read_text(encoding='utf-8')),format_checker=FormatChecker()) for kind in ['object','event']}
results=[];fixtures={}
for profile in ['startup','matrix','ai-service']:
    actor='urn:synthetic:'+('founder' if profile=='startup' else 'employee' if profile=='matrix' else 'ai-proposer')
    principal=actor if profile=='startup' else 'urn:synthetic:matrix-unit' if profile=='matrix' else 'urn:synthetic:service-owner'
    req={'schemaVersion':'D1','intent':{'requestId':'urn:synthetic:'+profile+':request:1','dimensionId':'urn:synthetic:'+profile+':dimension','executorId':'urn:synthetic:'+profile+':executor','executorEpoch':'urn:synthetic:'+profile+':epoch:1','retryKey':'urn:synthetic:'+profile+':key:1','definitionRef':copy.deepcopy(definition_ref),'actorId':actor,'principalId':principal,'purpose':'synthetic-label-demo','resourceId':'urn:synthetic:'+profile+':workspace','expectedRevision':0,'expiresAt':'2026-09-23T00:00:00Z','parameters':{'labels':['alpha','beta']},'basisRef':None,'proposalEventId':None,'compensatesReceiptId':None},'admission':{'submittedAt':'2026-09-22T00:00:00Z','submittedBy':actor,'admittedDefinitionRef':copy.deepcopy(definition_ref),'intentDigest':'','submissionEventId':'urn:synthetic:'+profile+':submitted:1'}}
    req['admission']['intentDigest']=sha(req['intent']);validate(req)
    native={'recordType':'object','schemaVersion':'1.0.0','recordId':req['intent']['requestId']+':r1','objectId':req['intent']['requestId'],'objectType':'urn:vercy:research:ActionRequest:D1','name':'Synthetic '+profile+' action request','recordedAt':req['admission']['submittedAt'],'previousRecordId':None,'state':'active','facets':{'enterprise-action-request-draft':req},'provenance':{'source':'urn:synthetic:draft-harness','assurance':'synthetic-shape-fixture-not-authorized'}}
    event={'recordType':'event','schemaVersion':'1.0.0','eventId':req['admission']['submissionEventId'],'eventType':'urn:vercy:research:ActionSubmitted:D1','subjectIds':[req['intent']['requestId']],'occurredAt':req['admission']['submittedAt'],'recordedAt':req['admission']['submittedAt'],'actorId':req['intent']['executorId'],'payload':{'requestId':req['intent']['requestId'],'intentDigest':req['admission']['intentDigest'],'admittedDefinitionRef':definition_ref},'provenance':{'source':'urn:synthetic:draft-harness','assurance':'synthetic-shape-fixture-not-authorized'}}
    outer['object'].validate(native);outer['event'].validate(event)
    assert native['objectId']==event['subjectIds'][0]==event['payload']['requestId']
    assert event['eventId']==req['admission']['submissionEventId']
    save(profile+'/request.json',req);save(profile+'/object.json',native);save(profile+'/submission-event.json',event)
    fixtures[profile]=req
    results.append({'profile':profile,'nestedRequest':'pass','nativeObjectEnvelope':'pass','nativeSubmissionEnvelope':'pass','explicitPairReferences':'pass','authorizationChecked':False,'installedDimension':False})

base=fixtures['startup'];negative=[]
def reject(name,mutate,repin=False):
    x=copy.deepcopy(base);mutate(x)
    if repin:x['admission']['intentDigest']=sha(x['intent'])
    try:validate(x)
    except Exception as e:negative.append({'case':name,'outcome':'rejected','exceptionType':type(e).__name__})
    else:raise AssertionError('unexpected acceptance: '+name)
reject('unknown intent field',lambda x:x['intent'].update(execute=True),True)
reject('boolean revision',lambda x:x['intent'].update(expectedRevision=True),True)
reject('floating-point integer encoding',lambda x:x['intent'].update(expectedRevision=1.0),True)
reject('reordered labels without new pin',lambda x:x['intent']['parameters']['labels'].reverse())
reject('changed purpose without new pin',lambda x:x['intent'].update(purpose='publish'))
reject('wrong definition digest',lambda x:x['intent']['definitionRef'].update(sha256='0'*64),True)
reject('invented extra parameter',lambda x:x['intent']['parameters'].update(shell='ignored'),True)
reject('wrong native request ID',lambda x:x['intent'].update(requestId='https://example.invalid/request'),True)
reject('admission submitter differs',lambda x:x['admission'].update(submittedBy='urn:synthetic:other'))
reject('admission at exclusive deadline',lambda x:x['admission'].update(submittedAt=x['intent']['expiresAt']))
reject('invalid calendar date',lambda x:x['intent'].update(expiresAt='2026-02-30T00:00:00Z'),True)
reject('unpaired surrogate',lambda x:x['intent']['parameters'].update(labels=['\ud800']))
reject('unsupported draft version',lambda x:x.update(schemaVersion='0.1.0'))
reject('missing explicit optional field',lambda x:x['intent'].pop('basisRef'),True)

report={'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'draft shape experiment passed','python':sys.version.split()[0],'schemaSha256':hashlib.sha256((W/'request.schema.json').read_bytes()).hexdigest(),'definitionExactSha256':definition_ref['sha256'],'nativeSchemas':{kind:hashlib.sha256((S/(kind+'.schema.json')).read_bytes()).hexdigest() for kind in outer},'fixtures':results,'negativeCases':negative,'limits':['No execution, policy evaluation, authentication, complete event history, archive admission, cancellation or compensation is implemented.','No Dimension installation, runtime registration, independent audit or model publication occurred.','Selected digest/pin/reference checks supplement JSON Schema; they do not prove authority, latest history or atomic effects.','The supplied synthetic admission records are fixture claims, not production admissions.']}
save('validation-results.json',report)
print(json.dumps({'profiles':len(results),'negativeCasesRejected':len(negative),'nativeEnvelopes':6,'installedDimensions':0,'modelPublished':False}))
