"""Three new synthetic Dimensions; native envelopes AND installed companion validation."""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from datetime import datetime,timedelta,timezone
from pathlib import Path
import monetary as m
from test_monetary import fixture
HERE=Path(__file__).resolve().parent;SLUG='enterprise-monetary-calculation';MID=m.MID
MASTER='urn:synthetic:monetary-receipt-register';WRITER='urn:synthetic:storage-writer'
def require(ok,s):
    if not ok:raise RuntimeError(s)
def read(p):return m.load(Path(p).read_bytes())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def native_pair(r,at):
    rid=r['request']['id'];obj={'recordType':'object','schemaVersion':'1.0.0','recordId':m.native_object_record_id(r),'objectId':rid,'objectType':MID+':MonetaryCalculationReceipt','name':'Synthetic calculation receipt','description':'An immutable calculation, not an authorization','recordedAt':at,'previousRecordId':None,'state':'active','provenance':{'source':MASTER,'synthetic':True},'accessClass':'restricted'}
    fact={'recordType':'fact','schemaVersion':'1.0.0','factId':m.native_fact_id(r),'subjectId':rid,'path':m.PATH,'value':r,'unit':None,'validFrom':at,'validTo':None,'recordedAt':at,'supersedes':[],'status':'asserted','provenance':{'source':MASTER,'synthetic':True,'recordDigest':r['digest']},'authority':{'source':WRITER,'rank':0},'masterSystem':MASTER,'accessClass':'restricted'}
    return obj,fact
def run(composer,skill):
    composer=Path(composer).resolve();skill=Path(skill).resolve();pins=read(HERE/'tool-pins.json')
    for key,root in [('composerFiles',composer),('skillFiles',skill)]:
        for n,h in pins[key].items():require(sha(root/n)==h,'Changed tool '+n)
    sys.path.insert(0,str(composer));import composition as c
    from bootstrap_dimension import bootstrap
    sys.path.insert(0,str(skill/'scripts'));from write_record import append
    from validate_dimension import validate as native_validate
    at=c.now();until=(datetime.now(timezone.utc)+timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ');reports=[]
    with tempfile.TemporaryDirectory(prefix='vercy-money-acceptance-') as tmp:
        root=Path(tmp);assets=root/'assets';assets.mkdir()
        def desc(n):
            raw=(HERE/n).read_bytes();dst=assets/SLUG/n;dst.parent.mkdir(exist_ok=True);dst.write_bytes(raw)
            return {'path':SLUG+'/'+n,'digest':c.digest(raw),'size':len(raw),'mediaType':'application/json' if n.endswith('.json') else 'text/x-python' if n.endswith('.py') else 'text/markdown','sourceUrl':'https://ver.cy/models/'+SLUG+'/versions/0.1.0/'+n}
        sd=desc('spec.json')
        release={'modelId':MID,'version':'0.1.0','namespace':'urn:vercy:model:'+MID,'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','requires':[],'references':[],'specification':sd,'agents':desc('AGENTS.md'),'installationMode':'native-binding','binding':{'id':'urn:vercy:binding:enterprise-monetary-calculation','version':'0.1.0','forSpecificationDigest':sd['digest'],'runtime':desc('runtime-model.reference.json'),'instanceSchema':desc('monetary.schema.json'),'companionValidator':desc('monetary.py'),'scope':'Bounded optional calculation receipts. Explicit nested and full-register validation required. Read complete pinned documentation separately.'},'semanticFingerprint':None,'compatibility':{'decision':'accepted','reviewer':'urn:synthetic:reviewer:installation','evidence':'urn:synthetic:acceptance:monetary','observedAt':at,'scope':'Synthetic candidate installation only. Published fixture state is not a claim of live deployment.'}}
        for name in ('startup','matrix','ai'):
            q=fixture(name);dimension=q['dimension'];target=root/name;stage=root/(name+'-stage');policy_path=root/(name+'-policy.json');lock=root/(name+'-lock.json');plan_path=root/(name+'-plan.json')
            policy={'format':'vercy-composition-policy','version':1,'id':'urn:synthetic:policy:monetary-installation','dimensionId':dimension,'owner':'urn:synthetic:owner:installation','allowInstall':True,'actors':['urn:synthetic:actor:composer'],'purposes':['Synthetic monetary installation'],'allowedModelIds':[MID],'allowedOrigins':['https://ver.cy'],'reviewers':['urn:synthetic:reviewer:installation'],'allowReviewableDrafts':True,'validFrom':at,'validUntil':until}
            policy_path.write_bytes(c.encode(policy));lock.write_bytes(c.encode({'models':[]}))
            plan={'format':'vercy-composition-plan','schemaVersion':'1.0.0','planId':'urn:synthetic:composition:monetary:'+name,'revision':1,'supersedes':None,'algorithm':'exact-closure-v1','dimensionId':dimension,'createdAt':at,'validUntil':until,'baseLockDigest':c.digest(lock.read_bytes()),'roots':[{'modelId':MID,'version':'0.1.0'}],'releases':[release],'authority':{'actor':policy['actors'][0],'allowReviewableDrafts':True,'allowedModelIds':[MID],'decision':'allow','owner':policy['owner'],'policyDigest':c.digest(policy_path.read_bytes()),'policyRef':policy['id'],'purpose':policy['purposes'][0]},'provenance':{'classification':'public-synthetic','evidenceKind':'proposal','masterSystem':MASTER,'recordedAt':at,'source':'urn:synthetic:fixture:'+name}}
            plan_path.write_bytes(c.encode(plan));c.stage(plan_path,assets,policy_path,lock,stage);bootstrap(stage,policy_path,lock,skill,target,'Synthetic monetary '+name,dimension)
            installed=target/'models/composed'/SLUG/'monetary.py'
            installed_checks={}
            for descriptor in (release['specification'],release['agents'],release['binding']['runtime'],release['binding']['instanceSchema'],release['binding']['companionValidator']):
                asset=target/'models/composed'/descriptor['path'];ok=c.digest(asset.read_bytes())==descriptor['digest'] and asset.stat().st_size==descriptor['size'];require(ok,'Installed asset differs '+descriptor['path']);installed_checks[descriptor['path']]=ok
            ms=importlib.util.spec_from_file_location('installed_money_'+name,installed);module=importlib.util.module_from_spec(ms);ms.loader.exec_module(module)
            first=module.issue(q);q2=copy.deepcopy(q);q2['id']+='-corrected';q2['computedAt']='2026-09-21T10:02:00Z';q2['supersedes']=module.pin(first);q2['correctionReason']='Declared alternative rounding stage';q2['policy']['stage']='after-sum';second=module.issue(q2)
            opts={'dimension':dimension,'allowed_issuers':{'urn:synthetic:issuer:'+name}};imports={'dimension':dimension,'admitted_existing_issuers':opts['allowed_issuers'],'admitted_incoming_issuers':opts['allowed_issuers']};register=module.import_receipts([],[first,second],**imports)
            stored=[];pairs=[];paths=[]
            for i,r in enumerate(register):
                obj,fact=native_pair(r,at);pairs.append((obj,fact))
                op=root/(name+'-object-'+str(i)+'.json');op.write_bytes(m.canonical(obj));written_object=append(target,'object',op);obj=read(target/written_object['written']);pairs[-1]=(obj,fact)
                fp=root/(name+'-fact-'+str(i)+'.json');fp.write_bytes(m.canonical(fact));result=append(target,'fact',fp);actual=target/result['written'];paths.append(actual)
                saved=read(actual);stored.append(module.validate_native(saved,obj,master=MASTER,writer=WRITER,**opts))
            stored_facts=[read(p) for p in (target/'data/facts').rglob('*.json') if read(p).get('path')==module.PATH]
            require(len(stored_facts)==len(stored) and {f['factId'] for f in stored_facts}=={f['factId'] for _,f in pairs},'Fixture enumeration differs')
            replay_ok=module.import_receipts([],stored,**imports)==register and module.import_receipts(register,[second],**imports)==register;require(replay_ok,'Stored register or replay differs')
            native=native_validate(target);require(native['valid'],'Native validation failed')
            negatives=[];obj,fact=pairs[0]
            for k,val,expected in [('schemaVersion','2.0.0','native-version'),('provenance',None,'native-provenance'),('provenance','invalid','native-provenance'),('path','monetary.wrong','native-binding'),('subjectId','urn:synthetic:wrong','native-binding'),('factId','urn:synthetic:wrong','native-binding'),('masterSystem','urn:synthetic:wrong','native-master'),('accessClass','public','native-disclosure-digest'),('validFrom','2026-09-21T10:00:00Z','native-storage-time'),('unit','EUR','native-shape'),('supersedes',['urn:synthetic:wrong'],'native-shape'),('authority',{'source':'urn:synthetic:wrong','rank':0},'native-master'),('status','retracted','native-shape'),('validTo',at,'native-shape'),('provenance',{'recordDigest':'sha256:'+'0'*64},'native-disclosure-digest')]:
                f=copy.deepcopy(fact);f[k]=val
                try:module.validate_native(f,obj,master=MASTER,writer=WRITER,**opts)
                except module.Rejected as e:require(str(e)==expected,'Wrong failure '+k+': '+str(e));negatives.append('fact-'+k)
                else:raise RuntimeError('Accepted '+k)
            for k,val,expected in [('schemaVersion','2.0.0','native-version'),('provenance',None,'native-provenance'),('objectType','urn:wrong','native-object'),('recordId','urn:wrong','native-object-record'),('previousRecordId','urn:wrong','native-object-record'),('recordedAt','2026-09-21T10:00:00Z','native-object-time'),('state','retired','native-object-state'),('accessClass','public','native-object-state')]:
                ob=copy.deepcopy(obj);ob[k]=val
                try:module.validate_native(fact,ob,master=MASTER,writer=WRITER,**opts)
                except module.Rejected as e:require(str(e)==expected,'Wrong object failure '+k);negatives.append('object-'+k)
                else:raise RuntimeError('Accepted object '+k)
            for param,value in [('dimension','urn:synthetic:wrong'),('allowed_issuers',set())]:
                opt=copy.deepcopy(opts);opt[param]=value
                try:module.validate_native(fact,obj,master=MASTER,writer=WRITER,**opt)
                except module.Rejected as e:require(str(e)=='native-host-scope','Wrong scope failure');negatives.append(param)
                else:raise RuntimeError('Accepted scope')
            for bad in (q['issuer']+'-admin',[q['issuer']],None):
                opt=dict(opts,allowed_issuers=bad)
                try:module.validate_native(fact,obj,master=MASTER,writer=WRITER,**opt)
                except module.Rejected as e:require(str(e)=='host-issuer-set','Wrong admission type failure');negatives.append('issuer-type-'+type(bad).__name__)
                else:raise RuntimeError('Accepted malformed admission')
            ob=copy.deepcopy(obj);f=copy.deepcopy(fact);ob['recordedAt']=f['recordedAt']=f['validFrom']='2026-09-21T09:00:00Z'
            try:module.validate_native(f,ob,master=MASTER,writer=WRITER,**opts)
            except module.Rejected as e:require(str(e)=='native-recorded-before-computed','Wrong time failure');negatives.append('recorded-before-computed')
            else:raise RuntimeError('Accepted early storage')
            bad=copy.deepcopy(fact);bad['value']['result']['roundedTotal']='999';bad['value']['digest']=module.digest({k:v for k,v in bad['value'].items() if k!='digest'});bad['provenance']['recordDigest']=bad['value']['digest'];bad['factId']=module.native_fact_id(bad['value'])
            old=paths[0].read_bytes();paths[0].write_bytes(m.canonical(bad))
            try:outer=native_validate(target);require(outer['valid'],'Bad nested fixture must isolate arithmetic')
            finally:paths[0].write_bytes(old)
            try:module.validate_native(bad,obj,master=MASTER,writer=WRITER,**opts)
            except module.Rejected as e:require(str(e)=='replay-mismatch','Nested negative did not isolate replay');negatives.append('rehashed-invalid-nested-result')
            else:raise RuntimeError('Nested arithmetic accepted')
            native.pop('dimension',None);outer.pop('dimension',None)
            reports.append({'profile':name,'dimension':dimension,'objects':len(pairs),'immutableReceiptFacts':len(stored_facts),'native':native,'installedReplayAndImmutableImport':replay_ok,'installedAssets':installed_checks,'firstResult':first['result']['roundedTotal'],'correctedResult':second['result']['roundedTotal'],'negativeCasesRejected':negatives,'outerAloneAcceptsBadArithmetic':outer['valid'],'specDigest':sd['digest']})
    return {'format':'vercy-monetary-native-acceptance','reportMode':'fail-stop: any failed assertion aborts without writing a success report','executedAt':at,'passed':len(reports),'failed':0,'profiles':reports,'sourceDigests':{n:sha(HERE/n) for n in ['monetary.py','monetary.schema.json','test_monetary.py','acceptance.py','spec.json','runtime-model.reference.json','tool-pins.json']},'limits':'Three new synthetic Dimensions. Explicit companion calls, no automatic hook; source truth/rights, production scale, current selector and existing-Dimension migration unimplemented.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True);a=ap.parse_args();r=run(a.composer,a.skill);Path(a.report).write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':r['passed'],'failed':r['failed']}))
