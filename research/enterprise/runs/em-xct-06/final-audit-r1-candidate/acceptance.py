"""Three new synthetic Dimensions; native envelopes AND installed companion validation."""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from datetime import datetime,timedelta,timezone
from pathlib import Path
import monetary as m
from test_monetary import fixture
HERE=Path(__file__).resolve().parent;SLUG='enterprise-monetary-calculation';MID=m.MID
MASTER='urn:synthetic:monetary-register';WRITER='urn:synthetic:storage-writer'
def require(ok,s):
    if not ok:raise RuntimeError(s)
def read(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def native_pair(r,at):
    rid=r['request']['id'];obj={'recordType':'object','schemaVersion':'1.0.0','recordId':'urn:vercy:monetary-object:'+hashlib.sha256(m.canonical({'dimension':r['request']['dimension'],'id':rid})).hexdigest(),'objectId':rid,'objectType':MID+':MonetaryCalculationReceipt','name':'Synthetic calculation receipt','description':'An immutable calculation, not an authorization','recordedAt':at,'previousRecordId':None,'state':'active','provenance':{'source':MASTER,'synthetic':True},'accessClass':'restricted'}
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
            installed=target/'models/composed'/SLUG/'monetary.py';require(c.digest(installed.read_bytes())==release['binding']['companionValidator']['digest'],'Installed code differs')
            ms=importlib.util.spec_from_file_location('installed_money_'+name,installed);module=importlib.util.module_from_spec(ms);ms.loader.exec_module(module)
            first=module.issue(q);q2=copy.deepcopy(q);q2['id']+='-corrected';q2['computedAt']='2026-09-21T10:02:00Z';q2['supersedes']=module.pin(first);q2['correctionReason']='Declared alternative rounding stage';q2['policy']['stage']='after-sum';second=module.issue(q2)
            opts={'dimension':dimension,'allowed_issuers':{q['issuer']}};register=module.import_receipts([],[first,second],**opts)
            stored=[];pairs=[];paths=[]
            for i,r in enumerate(register):
                obj,fact=native_pair(r,at);pairs.append((obj,fact))
                op=root/(name+'-object-'+str(i)+'.json');op.write_bytes(m.canonical(obj));append(target,'object',op)
                fp=root/(name+'-fact-'+str(i)+'.json');fp.write_bytes(m.canonical(fact));result=append(target,'fact',fp);actual=target/result['written'];paths.append(actual)
                saved=read(actual);stored.append(module.validate_native(saved,obj,master=MASTER,writer=WRITER,**opts))
            require(module.import_receipts([],stored,**opts)==register,'Stored register differs');require(module.import_receipts(register,[second],**opts)==register,'Replay differs')
            native=native_validate(target);require(native['valid'],'Native validation failed')
            negatives=[];obj,fact=pairs[0]
            for k,val in [('path','monetary.wrong'),('subjectId','urn:synthetic:wrong'),('factId','urn:synthetic:wrong'),('masterSystem','urn:synthetic:wrong'),('accessClass','public'),('validFrom','2026-09-21T10:00:00Z'),('unit','EUR'),('supersedes',['urn:synthetic:wrong'])]:
                f=copy.deepcopy(fact);f[k]=val
                try:module.validate_native(f,obj,master=MASTER,writer=WRITER,**opts)
                except module.Rejected:negatives.append(k)
                else:raise RuntimeError('Accepted '+k)
            bad=copy.deepcopy(fact);bad['value']['result']['roundedTotal']='999';bad['value']['digest']=module.digest({k:v for k,v in bad['value'].items() if k!='digest'});bad['provenance']['recordDigest']=bad['value']['digest']
            old=paths[0].read_bytes();paths[0].write_bytes(m.canonical(bad))
            try:outer=native_validate(target);require(outer['valid'],'Bad nested fixture must isolate arithmetic')
            finally:paths[0].write_bytes(old)
            try:module.validate_native(bad,obj,master=MASTER,writer=WRITER,**opts)
            except module.Rejected:negatives.append('rehashed-invalid-nested-result')
            else:raise RuntimeError('Nested arithmetic accepted')
            native.pop('dimension',None);outer.pop('dimension',None)
            reports.append({'profile':name,'dimension':dimension,'objects':2,'immutableReceiptFacts':2,'native':native,'installedReplayAndImmutableImport':True,'firstResult':first['result']['roundedTotal'],'correctedResult':second['result']['roundedTotal'],'negativeCasesRejected':negatives,'outerAloneAcceptsBadArithmetic':outer['valid'],'specDigest':sd['digest']})
    return {'format':'vercy-monetary-native-acceptance','executedAt':at,'passed':len(reports),'failed':0,'profiles':reports,'sourceDigests':{n:sha(HERE/n) for n in ['monetary.py','monetary.schema.json','test_monetary.py','acceptance.py','spec.json','runtime-model.reference.json','tool-pins.json']},'limits':'Three new synthetic Dimensions. Explicit companion calls, no automatic hook; source truth/rights, production scale, current selector and existing-Dimension migration unimplemented.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True);a=ap.parse_args();r=run(a.composer,a.skill);Path(a.report).write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':r['passed'],'failed':r['failed']}))
