"""Build the closed D2 reference shapes. Does not execute or authorize actions."""
from pathlib import Path
import json

def obj(properties, required=None):
    return {'type':'object','properties':properties,'required':list(properties) if required is None else required,'additionalProperties':False}
def array(item, maximum=128, minimum=0, unique=False):
    return {'type':'array','items':item,'minItems':minimum,'maxItems':maximum,**({'uniqueItems':True} if unique else {})}
def enum(*values): return {'enum':list(values)}
def ref(name): return {'$ref':'#/$defs/'+name}
def nullable(value): return {'anyOf':[value,{'type':'null'}]}
ID={'type':'string','pattern':'^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$'}
TEXT={'type':'string','minLength':1,'maxLength':2048}
TOKEN={'type':'string','pattern':'^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$'}
HASH={'type':'string','pattern':'^[a-f0-9]{64}$'}
TIME={'type':'integer','minimum':946684800,'maximum':4102444800}
REV={'type':'integer','minimum':0,'maximum':9007199254740991}
LABELS=array({'type':'string','maxLength':200},32)
PIN=obj({'uri':{'type':'string','pattern':'^(urn:|https://)[!-~]+$','maxLength':512},'revision':TOKEN,'sha256':HASH})
DEFREF=obj({'definitionId':ID,'version':TOKEN,'sha256':HASH})
SCOPE=obj({'dimensionId':ID,'definition':DEFREF,'resourceId':ID,'purpose':TOKEN,'audience':ID,
           'actions':array(enum('submit','execute','read','cancel','observe'),5,0,True),'validFrom':TIME,'validUntil':TIME})
RULE=obj({'actorId':ID,'principalId':ID,'mode':enum('self','direct-representation'),
          'issuerId':ID,'issuerStanding':PIN,'basis':PIN,'principalScope':SCOPE,'delegateScope':SCOPE})
DEFINITION=obj({'format':enum('enterprise-action-definition/0.1.0'),'definitionId':ID,'version':TOKEN,
 'name':TEXT,'description':TEXT,'mode':enum('synthetic-executable','descriptive-only'),
 'parameterContract':{'anyOf':[enum('ordered-label-list/1'),PIN]},'targetType':ID,'precondition':TEXT,
 'effectBoundary':TEXT,'adapter':enum('local-sqlite-ordered-labels/1','none'),
 'validFrom':TIME,'validUntil':TIME,'purposes':array(TOKEN,16,1,True),
 'authorityRequirement':enum('current-exact-principal-and-actor-scope'),
 'compensation':enum('new-request-restores-before-labels-at-exact-after-revision','external-unspecified'),
 'stewardId':ID,'masterId':ID,'legacyCrosswalk':nullable(PIN)})
INTENT=obj({'format':enum('enterprise-action-intent/0.1.0'),'dimensionId':ID,'definition':DEFREF,
 'resourceId':ID,'expectedRevision':REV,'parameters':obj({'labels':LABELS}),
 'actorId':ID,'principalId':ID,'purpose':TOKEN,'audience':ID,'expiresAt':TIME,'compensatesReceiptId':nullable(ID)})
REQUEST=obj({'requestId':ID,'keyHash':HASH,'intentDigest':HASH,'intent':INTENT,'submittedAt':TIME,'submissionEventId':ID,
 'state':enum('pending','committed','cancelled','expired','rejected-precondition'),'receiptId':nullable(ID),'keyRetired':{'type':'boolean'}})
DECISION=obj({'action':enum('execute','cancel','observe'),'policyRevision':REV,'allowed':{'type':'boolean'},
              'matchedRuleDigests':array(HASH,128,0,True),'definitionAvailable':{'type':'boolean'}})
PAYLOADS={
 'submission':obj({'intentDigest':HASH}),
 'delivery':obj({'intentDigest':HASH}),
 'try':obj({'decision':DECISION}),
 'receipt':obj({'definition':DEFREF,'resourceId':ID,'beforeRevision':REV,'afterRevision':REV,'beforeLabels':LABELS,'afterLabels':LABELS,'compensatesReceiptId':nullable(ID),'tryEventId':ID}),
 'disposition':obj({'from':enum('pending'),'to':enum('cancelled','expired','rejected-precondition'),'reason':TOKEN,'tryEventId':nullable(ID)}),
 'observation':obj({'observerId':ID,'claim':enum('caller-unknown','caller-observed-success','caller-observed-failure'),'reason':TEXT,'correctsEventId':nullable(ID),'tryEventId':ID}),
 'key-retirement':obj({'retained':enum(True)})}
EVENTS=[obj({'eventId':ID,'sequence':REV,'controlSequence':REV,'kind':enum(kind),'requestId':ID,'recordedAt':TIME,'issuerId':ID,'payload':payload}) for kind,payload in PAYLOADS.items()]
SCHEMA={'$schema':'https://json-schema.org/draft/2020-12/schema','$id':'urn:vercy:enterprise-action-requests:0.1.0:reference-shapes',
 'oneOf':[ref(name) for name in ('ActionDefinition','Intent','ActionRequestSnapshot','Event','Policy')],
 '$defs':{'Pin':PIN,'DefinitionRef':DEFREF,'Scope':SCOPE,'Rule':RULE,'Policy':array(RULE),
 'ActionDefinition':DEFINITION,'Intent':INTENT,'ActionRequestSnapshot':REQUEST,'Event':{'oneOf':EVENTS},
 'Labels':LABELS}}
if __name__=='__main__':
    Path(__file__).with_name('action.schema.json').write_text(json.dumps(SCHEMA,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
