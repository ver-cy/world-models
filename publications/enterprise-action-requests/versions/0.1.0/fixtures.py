"""Invented company profiles; no claims about any real organization."""
from copy import deepcopy
from action import Executor, definition_ref, digest

NOW=1789990000
ALL=['submit','execute','read','cancel','observe']

def pin(name):
    return {'uri':'urn:synthetic:evidence:'+name,'revision':'1','sha256':digest({'syntheticEvidence':name})}

def fixture(path,profile='startup',executor_type=Executor):
    dimension='urn:synthetic:dimension:'+profile
    actor='urn:synthetic:actor:'+profile
    principal=actor if profile=='startup' else 'urn:synthetic:principal:'+profile
    issuer='urn:synthetic:host:'+profile
    executor=executor_type.create(path,dimension,issuer,NOW)
    definition={'format':'enterprise-action-definition/0.1.0','definitionId':'urn:synthetic:action:replace-labels','version':'1',
        'name':'Replace ordered labels','description':'Replace all labels in one synthetic SQLite resource; duplicate labels and order are meaningful.',
        'mode':'synthetic-executable','parameterContract':'ordered-label-list/1','targetType':'urn:vercy:synthetic:OrderedLabelResource',
        'precondition':'resource-revision-and-retained-compensation-v1',
        'effectBoundary':'local-atomic-ordered-label-replacement-v1',
        'adapter':'local-sqlite-ordered-labels/1','validFrom':NOW-10,'validUntil':NOW+10000,'purposes':['synthetic-label-management'],
        'authorityRequirement':'current-exact-principal-and-actor-scope',
        'compensation':'new-request-restores-before-labels-at-exact-after-revision','stewardId':principal,'masterId':issuer,'legacyCrosswalk':None}
    executor.add_definition(definition,NOW)
    intent={'format':'enterprise-action-intent/0.1.0','dimensionId':dimension,'definition':definition_ref(definition),
        'resourceId':'urn:synthetic:resource:'+profile,'expectedRevision':0,'parameters':{'labels':['alpha','beta','alpha']},
        'actorId':actor,'principalId':principal,'purpose':'synthetic-label-management','audience':issuer,'expiresAt':NOW+100,'compensatesReceiptId':None}
    scope={k:deepcopy(intent[k]) for k in ('dimensionId','definition','resourceId','purpose','audience')}
    scope.update(actions=list(ALL),validFrom=NOW-10,validUntil=NOW+10000)
    rule={'actorId':actor,'principalId':principal,'mode':'self' if actor==principal else 'direct-representation',
          'issuerId':issuer,'issuerStanding':pin('issuer-standing-'+profile),'basis':pin('direct-basis-'+profile),
          'principalScope':deepcopy(scope),'delegateScope':deepcopy(scope)}
    executor.set_policy([rule],NOW)
    executor.add_resource(intent['resourceId'],['draft'],NOW)
    return executor,intent,[rule],definition

def descriptive(definition):
    d=deepcopy(definition); d.update(definitionId='urn:synthetic:action:external-onboarding',name='Describe external onboarding',mode='descriptive-only',
        parameterContract=pin('external-parameter-document'),targetType='urn:synthetic:ExternalService',adapter='none',
        effectBoundary='External host; no execution binding in this release.',precondition='External host governance.',compensation='external-unspecified')
    return d
