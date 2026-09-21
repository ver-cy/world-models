"""Three synthetic native installations, explicit storage and nested validation."""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from datetime import datetime,timedelta,timezone
from pathlib import Path
import disclosure as d
from test_disclosure import fixture
HERE=Path(__file__).resolve().parent
MID='vr.profile.enterprise-disclosure-review';SLUG='enterprise-disclosure-review'
MASTER='urn:synthetic:disclosure-register';WRITER='urn:synthetic:storage-writer'
def require(ok,message):
    if not ok:raise RuntimeError(message)
def read(path):return json.loads(Path(path).read_text(encoding='utf-8'))
def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def native_pair(record,at):
    object_record_id='urn:vercy:disclosure-object:'+hashlib.sha256(d.canonical({'dimension':record['dimension'],'id':record['id']})).hexdigest()
    obj={'recordType':'object','schemaVersion':'1.0.0','recordId':object_record_id,'objectId':record['id'],'objectType':MID+':'+record['type'],'name':'Synthetic '+record['type'],'description':'Independent information record; active storage does not mean review applicability','recordedAt':at,'previousRecordId':None,'state':'active','provenance':{'source':MASTER,'synthetic':True},'accessClass':'restricted'}
    fact={'recordType':'fact','schemaVersion':'1.0.0','factId':d.native_fact_id(record),'subjectId':record['id'],'path':'disclosure.'+record['type']+'.revision','value':record,'unit':None,'validFrom':at,'validTo':None,'recordedAt':at,'supersedes':[],'status':'asserted','provenance':{'source':MASTER,'synthetic':True,'recordDigest':record['digest']},'authority':{'source':WRITER,'rank':0},'masterSystem':MASTER,'accessClass':'restricted'}
    return obj,fact
def run(composer,skill):
    composer=Path(composer).resolve();skill=Path(skill).resolve();pins=read(HERE/'tool-pins.json')
    for key,root in [('composerFiles',composer),('skillFiles',skill)]:
        for name,sha in pins[key].items():require(digest(root/name)==sha,'Changed trusted tool '+name)
    sys.path.insert(0,str(composer));import composition as c
    from bootstrap_dimension import bootstrap
    sys.path.insert(0,str(skill/'scripts'));from write_record import append
    from validate_dimension import validate as native_validate
    at=c.now();until=(datetime.now(timezone.utc)+timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ');reports=[]
    with tempfile.TemporaryDirectory(prefix='vercy-disclosure-acceptance-') as tmp:
        root=Path(tmp);assets=root/'assets';assets.mkdir()
        def desc(name):
            raw=(HERE/name).read_bytes();dst=assets/SLUG/name;dst.parent.mkdir(exist_ok=True);dst.write_bytes(raw)
            return {'path':SLUG+'/'+name,'digest':c.digest(raw),'size':len(raw),'mediaType':'application/json' if name.endswith('.json') else 'text/x-python' if name.endswith('.py') else 'text/markdown','sourceUrl':'https://ver.cy/models/'+SLUG+'/versions/0.1.0/'+name}
        sd=desc('spec.json')
        release={'modelId':MID,'version':'0.1.0','namespace':'urn:vercy:model:'+MID,'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','requires':[],'references':[],'specification':sd,'agents':desc('AGENTS.md'),'installationMode':'native-binding','binding':{'id':'urn:vercy:binding:enterprise-disclosure-review','version':'0.1.0','forSpecificationDigest':sd['digest'],'runtime':desc('runtime-model.reference.json'),'instanceSchema':desc('disclosure.schema.json'),'companionValidator':desc('disclosure.py'),'scope':'Own original metadata contract. Separate V3 envelope, explicit validate_native, full register import and inspect are mandatory; no automatic hook.'},'semanticFingerprint':None,'compatibility':{'decision':'accepted','reviewer':'urn:synthetic:reviewer:installation','evidence':'urn:synthetic:acceptance:disclosure','observedAt':at,'scope':'Synthetic candidate exercise only. Published is a catalogue lifecycle value in the fixture, not a claim the candidate is live.'}}
        for name in ('startup','matrix','ai'):
            proposal,review,snapshot,capability=fixture(name);dimension=proposal['dimension'];target=root/name;stage=root/(name+'-stage');policy_path=root/(name+'-policy.json');lock=root/(name+'-lock.json');plan_path=root/(name+'-plan.json')
            policy={'format':'vercy-composition-policy','version':1,'id':'urn:synthetic:policy:disclosure-installation','dimensionId':dimension,'owner':'urn:synthetic:owner:installation','allowInstall':True,'actors':['urn:synthetic:actor:composer'],'purposes':['Synthetic disclosure installation'],'allowedModelIds':[MID],'allowedOrigins':['https://ver.cy'],'reviewers':['urn:synthetic:reviewer:installation'],'allowReviewableDrafts':True,'validFrom':at,'validUntil':until}
            policy_path.write_bytes(c.encode(policy));lock.write_bytes(c.encode({'models':[]}))
            plan={'format':'vercy-composition-plan','schemaVersion':'1.0.0','planId':'urn:synthetic:composition:disclosure:'+name,'revision':1,'supersedes':None,'algorithm':'exact-closure-v1','dimensionId':dimension,'createdAt':at,'validUntil':until,'baseLockDigest':c.digest(lock.read_bytes()),'roots':[{'modelId':MID,'version':'0.1.0'}],'releases':[release],'authority':{'actor':policy['actors'][0],'allowReviewableDrafts':True,'allowedModelIds':[MID],'decision':'allow','owner':policy['owner'],'policyDigest':c.digest(policy_path.read_bytes()),'policyRef':policy['id'],'purpose':policy['purposes'][0]},'provenance':{'classification':'public-synthetic','evidenceKind':'proposal','masterSystem':MASTER,'recordedAt':at,'source':'urn:synthetic:fixture:'+name}}
            plan_path.write_bytes(c.encode(plan));c.stage(plan_path,assets,policy_path,lock,stage);bootstrap(stage,policy_path,lock,skill,target,'Synthetic disclosure '+name,dimension)
            installed=target/'models/composed'/SLUG/'disclosure.py'
            require(c.digest(installed.read_bytes())==release['binding']['companionValidator']['digest'],'Installed code differs')
            require(c.digest((installed.parent/'disclosure.schema.json').read_bytes())==release['binding']['instanceSchema']['digest'],'Installed schema differs')
            module_spec=importlib.util.spec_from_file_location('installed_disclosure_'+name,installed);module=importlib.util.module_from_spec(module_spec);module_spec.loader.exec_module(module)
            corrected=copy.deepcopy(review);corrected['revision']='2';corrected['body']['reviewedAt']='2026-09-21T10:02:00Z';corrected['body']['validFrom']='2026-09-21T10:02:00Z';corrected['body']['supersedes']=module.pin(review);corrected['body']['residualRisk']+=' Corrected explanation; no changed serving authority.';corrected=module.seal(corrected)
            records=module.import_records([],[proposal,review,corrected],dimension,capability)
            require(module.import_records(records,[corrected],dimension,capability)==records,'Import replay differs')
            objects={};stored=[];paths=[]
            def nested(f,o):return module.validate_native(f,o,dimension=dimension,capability=capability,now=at,master=MASTER,writer=WRITER)
            for i,record in enumerate(records):
                obj,fact=native_pair(record,at)
                if record['id'] not in objects:
                    p=root/(name+'-object-'+str(i)+'.json');p.write_bytes(d.canonical(obj));append(target,'object',p);objects[record['id']]=obj
                p=root/(name+'-fact-'+str(i)+'.json');p.write_bytes(d.canonical(fact));result=append(target,'fact',p);actual=target/result['written'];paths.append(actual);saved=read(actual)
                require(nested(saved,objects[record['id']])==record,'Nested roundtrip differs');stored.append(saved['value'])
            require(module.import_records([],stored,dimension,capability)==records,'Stored register differs')
            historical=copy.deepcopy(snapshot);historical['asOf']='2026-09-21T10:01:30Z'
            old_answer=module.inspect(stored[0],[stored[1]],historical,capability,historical['asOf'])
            current=copy.deepcopy(snapshot);current['activeReviews']=[module.pin(corrected)];current['withdrawnReviews']=[module.pin(review)]
            answer=module.inspect(stored[0],[stored[2]],current,capability,current['asOf']);expected='rejected' if name=='matrix' else 'applicable-review'
            require(old_answer['status']==answer['status']==expected,'Stored assessments differ');require(answer['notServingAuthorization'] is True,'Serving boundary lost')
            native=native_validate(target);require(native['valid'],'Native envelope validation failed')
            fact=read(paths[-1]);obj=objects[fact['subjectId']];negatives=[]
            mutations=[('subject',lambda f:f.update(subjectId='urn:synthetic:wrong')),('path',lambda f:f.update(path='disclosure.proposal.revision')),('revision-storage-key',lambda f:f.update(factId='urn:synthetic:wrong')),('digest',lambda f:f['provenance'].update(recordDigest='sha256:'+'0'*64)),('public-access',lambda f:f.update(accessClass='public')),('master',lambda f:f.update(masterSystem='urn:synthetic:wrong')),('storage-authority',lambda f:f['authority'].update(rank=1)),('boolean-authority-rank',lambda f:f['authority'].update(rank=False)),('validity-receipt-mismatch',lambda f:f.update(validFrom='2026-09-21T10:00:00Z')),('unit',lambda f:f.update(unit='items')),('validTo',lambda f:f.update(validTo=at)),('status',lambda f:f.update(status='retracted')),('provenance-source',lambda f:f['provenance'].update(source='urn:synthetic:wrong')),('native-supersession',lambda f:f.update(supersedes=['urn:synthetic:old'])),('storage-before-assessment',lambda f:f.update(recordedAt='2020-01-01T00:00:00Z',validFrom='2020-01-01T00:00:00Z')),('storage-future',lambda f:f.update(recordedAt='2999-01-01T00:00:00Z',validFrom='2999-01-01T00:00:00Z')),('nested-invalid',lambda f:f['value']['body'].update(verdict='grant-access'))]
            for label,mutate in mutations:
                bad=copy.deepcopy(fact);mutate(bad);rejected=False
                try:nested(bad,obj)
                except module.Invalid:rejected=True
                require(rejected,'Accepted native '+label);negatives.append(label)
            # Isolate assessment <= receipt: object <= receipt and receipt <= now
            # remain true; the corrected review was assessed at 10:02:00.
            earlier=copy.deepcopy(fact);earlier.update(recordedAt='2026-09-21T10:01:30Z',validFrom='2026-09-21T10:01:30Z')
            earlier_obj=copy.deepcopy(obj);earlier_obj['recordedAt']='2026-09-21T10:01:30Z'
            try:nested(earlier,earlier_obj)
            except module.Invalid as e:
                require(str(e)=='native storage time','Wrong isolated assessment failure');negatives.append('isolated-receipt-before-assessment')
            else:raise RuntimeError('Accepted receipt before assessment')
            for key,value in [('state','retired'),('accessClass','public')]:
                wrong_obj=copy.deepcopy(obj);wrong_obj[key]=value
                try:nested(fact,wrong_obj)
                except module.Invalid:negatives.append('object-'+key)
                else:raise RuntimeError('Accepted wrong object '+key)
            bad=copy.deepcopy(fact);bad['value']['body']['verdict']='grant-access';original=paths[-1].read_bytes();paths[-1].write_bytes(d.canonical(bad))
            try:
                outer=native_validate(target);require(outer['valid'],'Fixture must isolate nested semantic validation')
                companion_rejected=False
                try:nested(read(paths[-1]),obj)
                except module.Invalid:companion_rejected=True
                require(companion_rejected,'Companion accepted the actual stored invalid nested fact')
            finally:paths[-1].write_bytes(original)
            wrong=copy.deepcopy(obj);wrong['objectType']=MID+':proposal'
            try:nested(fact,wrong)
            except module.Invalid:negatives.append('object-type')
            else:raise RuntimeError('Accepted wrong object type')
            try:module.validate_native(fact,obj,dimension='urn:synthetic:other',capability={'dimension':'urn:synthetic:other','inspect':True},now=at,master=MASTER,writer=WRITER)
            except module.Invalid:negatives.append('cross-Dimension')
            else:raise RuntimeError('Accepted cross-Dimension')
            native.pop('dimension',None);outer.pop('dimension',None)
            reports.append({'profile':name,'dimension':dimension,'objects':2,'immutableRevisionFacts':3,'native':native,'sameVersionRoundtrip':True,'installedCompanionImportReplay':True,'historicalAndCurrentAnswers':[old_answer,answer],'negativeCasesRejected':negatives,'invalidNestedFact':{'native':outer,'companionRejected':companion_rejected},'installationPin':{'id':MID,'version':'0.1.0','specDigest':sd['digest']},'clockMeaning':'Current native storage of synthetic records; two constructed time-indexed snapshots (10:01:30 and 12:00:00 UTC) exercise an earlier assessment and later correction. Neither snapshot is preserved real history or a current serving decision.'})
    names=['disclosure.py','disclosure.schema.json','acceptance.py','test_disclosure.py','spec.json','runtime-model.reference.json','tool-pins.json']
    return {'format':'vercy-disclosure-native-acceptance','executedAt':c.now(),'passed':len(reports),'failed':0,'profiles':reports,'sourceDigests':{n:digest(HERE/n) for n in names},'limits':'Three new synthetic Dimensions, explicit installed companion calls. No automatic dispatch, production source/policy/IAM/custody integration, concurrency, existing-Dimension migration or inferred privacy assurance.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True);a=ap.parse_args();report=run(a.composer,a.skill);Path(a.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({'passed':report['passed'],'failed':report['failed']}))
