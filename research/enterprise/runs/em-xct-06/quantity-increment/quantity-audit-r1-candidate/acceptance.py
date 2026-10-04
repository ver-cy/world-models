"""Install five pinned assets into three synthetic V3 Dimensions, read stored facts."""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from datetime import datetime,timedelta,timezone
from pathlib import Path
import quantity as q
from test_quantity import fixture,pin
HERE=Path(__file__).parent;SLUG='enterprise-quantity-values';MID=q.MID
MASTER='urn:synthetic:quantity-capture';WRITER='urn:synthetic:writer'
def require(ok,s):
    if not ok:raise RuntimeError(s)
def read(p):return q.load(Path(p).read_bytes())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(composer,skill):
    composer=Path(composer).resolve();skill=Path(skill).resolve();pins=json.loads((HERE/'tool-pins.json').read_text(encoding='utf-8'))
    for key,root in [('composerFiles',composer),('skillFiles',skill)]:
        for n,h in pins[key].items():require(sha(root/n)==h,'Changed tool '+n)
    sys.path.insert(0,str(composer));import composition as c
    from bootstrap_dimension import bootstrap
    sys.path.insert(0,str(skill/'scripts'));from write_record import append
    from validate_dimension import validate as outer_validate
    at=c.now();until=(datetime.now(timezone.utc)+timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ');reports=[]
    with tempfile.TemporaryDirectory(prefix='vercy-quantity-acceptance-') as tmp:
        root=Path(tmp);assets=root/'assets';assets.mkdir()
        def desc(n):
            raw=(HERE/n).read_bytes();dst=assets/SLUG/n;dst.parent.mkdir(exist_ok=True);dst.write_bytes(raw)
            return {'path':SLUG+'/'+n,'digest':c.digest(raw),'size':len(raw),'mediaType':'application/json' if n.endswith('.json') else 'text/x-python' if n.endswith('.py') else 'text/markdown','sourceUrl':'https://ver.cy/models/'+SLUG+'/versions/0.1.0/'+n}
        sd=desc('spec.json')
        release={'modelId':MID,'version':'0.1.0','namespace':'urn:vercy:model:'+MID,'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','requires':[],'references':[],'specification':sd,'agents':desc('AGENTS.md'),'installationMode':'native-binding','binding':{'id':'urn:vercy:binding:enterprise-quantity-values','version':'0.1.0','forSpecificationDigest':sd['digest'],'runtime':desc('runtime-model.reference.json'),'instanceSchema':desc('quantity.schema.json'),'companionValidator':desc('quantity.py'),'scope':'Embedded values on existing host objects. Explicit nested validation and trusted definition/source/context admission required. No independent quantity identity.'},'semanticFingerprint':None,'compatibility':{'decision':'accepted','reviewer':'urn:synthetic:reviewer:installation','evidence':'urn:synthetic:acceptance:quantity','observedAt':at,'scope':'Synthetic new Dimension installation; fixture declarations do not prove live publication.'}}
        for name in ('startup','matrix','ai'):
            v,t,admitted=fixture(name);dimension='urn:synthetic:dimension:quantity:'+name;subject='urn:synthetic:host:'+name
            target=root/name;stage=root/(name+'-stage');policy_path=root/(name+'-policy.json');lock=root/(name+'-lock.json');plan_path=root/(name+'-plan.json')
            policy={'format':'vercy-composition-policy','version':1,'id':'urn:synthetic:policy:quantity-installation','dimensionId':dimension,'owner':'urn:synthetic:owner:installation','allowInstall':True,'actors':['urn:synthetic:actor:composer'],'purposes':['Synthetic quantity installation'],'allowedModelIds':[MID],'allowedOrigins':['https://ver.cy'],'reviewers':['urn:synthetic:reviewer:installation'],'allowReviewableDrafts':True,'validFrom':at,'validUntil':until}
            policy_path.write_bytes(c.encode(policy));lock.write_bytes(c.encode({'models':[]}))
            plan={'format':'vercy-composition-plan','schemaVersion':'1.0.0','planId':'urn:synthetic:composition:quantity:'+name,'revision':1,'supersedes':None,'algorithm':'exact-closure-v1','dimensionId':dimension,'createdAt':at,'validUntil':until,'baseLockDigest':c.digest(lock.read_bytes()),'roots':[{'modelId':MID,'version':'0.1.0'}],'releases':[release],'authority':{'actor':policy['actors'][0],'allowReviewableDrafts':True,'allowedModelIds':[MID],'decision':'allow','owner':policy['owner'],'policyDigest':c.digest(policy_path.read_bytes()),'policyRef':policy['id'],'purpose':policy['purposes'][0]},'provenance':{'classification':'public-synthetic','evidenceKind':'proposal','masterSystem':MASTER,'recordedAt':at,'source':'urn:synthetic:fixture:'+name}}
            plan_path.write_bytes(c.encode(plan));c.stage(plan_path,assets,policy_path,lock,stage);bootstrap(stage,policy_path,lock,skill,target,'Synthetic quantity '+name,dimension)
            installed=target/'models/composed'/SLUG/'quantity.py';checks={}
            for d in (release['specification'],release['agents'],release['binding']['runtime'],release['binding']['instanceSchema'],release['binding']['companionValidator']):
                p=target/'models/composed'/d['path'];checks[d['path']]=c.digest(p.read_bytes())==d['digest'] and p.stat().st_size==d['size'];require(checks[d['path']],'Installed asset differs')
            ms=importlib.util.spec_from_file_location('installed_quantity_'+name,installed);module=importlib.util.module_from_spec(ms);ms.loader.exec_module(module)
            obj={'recordType':'object','schemaVersion':'1.0.0','recordId':subject+':record:1','objectId':subject,'objectType':'urn:synthetic:type:'+{'startup':'ServiceEstimate','matrix':'RoutePlan','ai':'ThermalSample'}[name],'name':'Synthetic host '+name,'recordedAt':at,'previousRecordId':None,'state':'active','provenance':{'source':MASTER,'synthetic':True},'accessClass':'restricted'}
            op=root/(name+'-object.json');op.write_bytes(q.canonical(obj));ob=append(target,'object',op);obj=read(target/ob['written'])
            opts={'subject':subject,'master':MASTER,'writer':WRITER,'access':'restricted','admitted':admitted}
            first=module.convert(v,t,admitted=admitted);v2=copy.deepcopy(v);v2['magnitude'].update(lexical='2.00',scale=2);v2['source']=pin('source:'+name,'2');admitted['sources'].add(q.digest(v2['source']));second=module.convert(v2,t,admitted=admitted)
            facts=[];paths=[]
            for i,value in enumerate((first,second)):
                f={'recordType':'fact','schemaVersion':'1.0.0','factId':subject+':quantity:'+str(i),'subjectId':subject,'path':'quantity.conversion','value':value,'unit':None,'validFrom':'2026-09-20T10:00:00Z','validTo':None,'recordedAt':at,'supersedes':[] if i==0 else [facts[0]['factId']],'status':'asserted','provenance':{'source':MASTER,'synthetic':True,**({'correctionReason':'Corrected source revision'} if i else {})},'authority':{'source':WRITER,'rank':0},'masterSystem':MASTER,'accessClass':'restricted'}
                module.validate_native(f,obj,**opts);fp=root/(name+'-fact-'+str(i)+'.json');fp.write_bytes(q.canonical(f));written=append(target,'fact',fp);paths.append(target/written['written']);facts.append(read(paths[-1]));module.validate_native(facts[-1],obj,**opts)
            original=paths[0].read_bytes();module.validate_correction(facts[0],facts[1],obj,**opts);require(paths[0].read_bytes()==original,'Original changed')
            negative=[]
            # A repeat V3 append rejects the duplicate ID; no adapter silently rewrites it.
            try:append(target,'fact',fp)
            except Exception as e:
                require('already exists' in str(e) or 'duplicate' in str(e).lower(),'Unexpected duplicate refusal: '+str(e));negative.append('duplicate-native-append')
            else:raise RuntimeError('Duplicate append accepted')
            for key,val,reason in [('path','quantity.value','native-path'),('subjectId','urn:synthetic:wrong','native-subject'),('masterSystem','urn:synthetic:wrong','native-master'),('authority',{'source':'urn:synthetic:wrong','rank':0},'native-master'),('accessClass','public','native-access'),('unit','Cel','native-state'),('validTo',at,'native-state'),('status','retracted','native-state'),('recordedAt','invalid','native-time')]:
                bad=copy.deepcopy(facts[0]);bad[key]=val
                try:module.validate_native(bad,obj,**opts)
                except module.Rejected as e:require(str(e)==reason,'Wrong native failure '+key+': '+str(e));negative.append(key)
                else:raise RuntimeError('Accepted wrong '+key)
            for key,val,reason in [('supersedes',[],'correction-link'),('recordedAt','2026-01-01T00:00:00Z','correction-time'),('path','quantity.value','native-path')]:
                bad=copy.deepcopy(facts[1]);bad[key]=val
                try:module.validate_correction(facts[0],bad,obj,**opts)
                except module.Rejected as e:require(str(e)==reason,'Wrong correction failure '+key);negative.append('correction-'+key)
                else:raise RuntimeError('Accepted correction '+key)
            bad=copy.deepcopy(facts[1]);bad['provenance'].pop('correctionReason')
            try:module.validate_correction(facts[0],bad,obj,**opts)
            except module.Rejected as e:require(str(e)=='correction-reason','Wrong correction reason failure');negative.append('correction-reason')
            else:raise RuntimeError('Correction reason accepted')
            native=outer_validate(target);require(native['valid'],'Outer dimension invalid')
            # Write tampered nested result to actual storage, read it, restore exact original bytes.
            bad=copy.deepcopy(facts[0]);bad['value']['result']={'n':'999999','d':'1'};paths[0].write_bytes(q.canonical(bad))
            try:
                outer=outer_validate(target);require(outer['valid'],'Must isolate nested arithmetic')
                try:module.validate_native(read(paths[0]),obj,**opts)
                except module.Rejected as e:require(str(e)=='replay-mismatch','Wrong nested failure');negative.append('stored-invalid-result')
                else:raise RuntimeError('Stored invalid arithmetic accepted')
            finally:paths[0].write_bytes(original)
            require(paths[0].read_bytes()==original,'Original restoration failed')
            native.pop('dimension',None);outer.pop('dimension',None)
            reports.append({'profile':name,'dimension':dimension,'hostObjects':1,'independentQuantityObjects':0,'facts':2,'installedAssets':checks,'native':native,'storedCorrectionValidated':True,'originalBytesPreserved':True,'negativeCasesRejected':negative,'outerAloneAcceptsInvalidNestedResult':outer['valid'],'firstResult':first['result'],'secondResult':second['result']})
    return {'format':'vercy-quantity-native-acceptance','reportMode':'fail-stop; no success report on assertion failure','executedAt':at,'passed':len(reports),'failed':0,'profiles':reports,'sourceDigests':{n:sha(HERE/n) for n in ['quantity.py','quantity.schema.json','test_quantity.py','acceptance.py','spec.json','runtime-model.reference.json','tool-pins.json']},'limits':'Three new synthetic Dimensions, explicit companion invocation. Most negatives mutate in-memory readbacks; arithmetic negative is read from tampered stored fact. Host object identity, current access, head resolution, definition authority and source truth remain external.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True);a=ap.parse_args();r=run(a.composer,a.skill);Path(a.report).write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':r['passed'],'failed':r['failed']}))
