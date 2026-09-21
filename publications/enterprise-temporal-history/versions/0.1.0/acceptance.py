"""Trusted synthetic new-Dimension composition, admission and snapshot checks."""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from datetime import datetime,timedelta,timezone
from pathlib import Path
import temporal as p
from test_temporal import fixture,T1,T2,NOW
HERE=Path(__file__).resolve().parent
PROFILE_ID='vr.profile.enterprise-temporal-history'
SLUG='enterprise-temporal-history'
def run(composer,skill):
    p.require(__debug__,'Run without -O');composer=Path(composer).resolve();skill=Path(skill).resolve();pins=p.load(HERE/'tool-pins.json')
    for field,root in [('composerFiles',composer),('skillFiles',skill),('upstreamFiles',HERE/'upstream')]:
        for n,h in pins[field].items():p.require(hashlib.sha256((root/n).read_bytes()).hexdigest()==h,'Unexpected trusted asset: '+n)
    sys.path.insert(0,str(composer));import composition as c
    from bootstrap_dimension import bootstrap
    sys.path.insert(0,str(skill/'scripts'));from write_record import append
    from validate_dimension import validate as native_validate
    reports=[];at=c.now();expires=(datetime.now(timezone.utc)+timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    with tempfile.TemporaryDirectory(prefix='vercy-authority-acceptance-') as tmp:
        root=Path(tmp);assets=root/'assets';assets.mkdir()
        def descriptor(folder,name,source,url):
            raw=source.read_bytes();dest=assets/folder/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
            return {'path':folder+'/'+name,'digest':c.digest(raw),'size':len(raw),'mediaType':'application/json' if name.endswith('.json') else 'text/x-python' if name.endswith('.py') else 'text/markdown' if name.endswith('.md') else 'application/yaml','sourceUrl':url}
        def release(mid,version,folder,spec,agents,base,native):
            ds=descriptor(folder,spec.name,spec,base+spec.name);da=descriptor(folder,'AGENTS.md',agents,base+'AGENTS.md');binding=None
            if native:
                binding={'id':'urn:vercy:binding:enterprise-temporal-history','version':'0.1.0','forSpecificationDigest':ds['digest'],'runtime':descriptor(folder,'runtime-model.reference.json',HERE/'runtime-model.reference.json',base+'runtime-model.reference.json'),'instanceSchema':descriptor(folder,'temporal.schema.json',HERE/'temporal.schema.json',base+'temporal.schema.json'),'companionValidator':descriptor(folder,'temporal.py',HERE/'temporal.py',base+'temporal.py'),'scope':'Own companion namespace/specification; no parent subtype. Explicit nested validation and admission required.'}
            return {'modelId':mid,'version':version,'namespace':'urn:vercy:model:'+mid,'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','requires':[],'references':[],'specification':ds,'agents':da,'installationMode':'native-binding' if native else 'semantic-only','binding':binding,'semanticFingerprint':None,'compatibility':{'decision':'accepted','reviewer':'urn:synthetic:reviewer:authority','evidence':'urn:synthetic:acceptance:authority','observedAt':at,'scope':'Synthetic candidate-installation exercise, not global parent ratification; publication and research assurance are separate.'}}
        parent='wm-xct-009-time-calendar';up=HERE/'upstream'/parent
        semantic=release('vr.wm-xct-009','0.3.0-research.1',parent,up/'spec.yaml',up/'AGENTS.md','https://ver.cy/models/enterprise-temporal-history/versions/0.1.0/upstream/'+parent+'/',False)
        companion=release(PROFILE_ID,'0.1.0',SLUG,HERE/'spec.json',HERE/'AGENTS.md','https://ver.cy/models/enterprise-temporal-history/versions/0.1.0/',True)
        companion['references']=[{'modelId':semantic['modelId'],'version':semantic['version']}];releases=[semantic,companion]
        for name in ['startup','group','ai-team']:
            config,initial,first,second,q1,q2=fixture(name);target=root/name;stage=root/(name+'-stage');pp=root/(name+'-policy.json');lp=root/(name+'-lock.json');planp=root/(name+'-plan.json');dimension=config['dimension']
            policy={'format':'vercy-composition-policy','version':1,'id':'urn:synthetic:composition-policy:temporal','dimensionId':dimension,'owner':'urn:synthetic:owner:installation','allowInstall':True,'actors':['urn:synthetic:actor:composer'],'purposes':['Synthetic temporal reference'],'allowedModelIds':[r['modelId'] for r in releases],'allowedOrigins':['https://ver.cy'],'reviewers':['urn:synthetic:reviewer:authority'],'allowReviewableDrafts':True,'validFrom':at,'validUntil':expires}
            pp.write_bytes(c.encode(policy));lp.write_bytes(c.encode({'models':[]}))
            plan={'format':'vercy-composition-plan','schemaVersion':'1.0.0','planId':'urn:synthetic:composition:temporal:'+name,'revision':1,'supersedes':None,'algorithm':'exact-closure-v1','dimensionId':dimension,'createdAt':at,'validUntil':expires,'baseLockDigest':c.digest(lp.read_bytes()),'roots':[{'modelId':r['modelId'],'version':r['version']} for r in releases],'releases':releases,'authority':{'actor':policy['actors'][0],'allowReviewableDrafts':True,'allowedModelIds':policy['allowedModelIds'],'decision':'allow','owner':policy['owner'],'policyDigest':c.digest(pp.read_bytes()),'policyRef':policy['id'],'purpose':policy['purposes'][0]},'provenance':{'classification':'public-synthetic','evidenceKind':'proposal','masterSystem':'urn:synthetic:reference','recordedAt':at,'source':'urn:synthetic:fixture:'+name}}
            planp.write_bytes(c.encode(plan));c.stage(planp,assets,pp,lp,stage);bootstrap(stage,pp,lp,skill,target,'Synthetic temporal '+name,dimension)
            installed=target/'models/composed'/SLUG/'temporal.py';p.require(c.digest(installed.read_bytes())==companion['binding']['companionValidator']['digest'],'Code differs');p.require(c.digest((installed.parent/'temporal.schema.json').read_bytes())==companion['binding']['instanceSchema']['digest'],'Schema differs')
            ms=importlib.util.spec_from_file_location('installed_temporal_'+name,installed);module=importlib.util.module_from_spec(ms);ms.loader.exec_module(module)
            replay1=module.admit(initial,q1,config,actor=config['writer'],now=T1);replay2=module.admit(replay1,q2,config,actor=config['writer'],now=T2)
            p.require(replay1==first and replay2==second,'Admission differs');checkAt=max(at,NOW);oid=config['timeline'];operator='urn:synthetic:timeline-operator';register='urn:synthetic:governance-register'
            obj={'recordType':'object','schemaVersion':'1.0.0','recordId':oid+':object-r1','objectId':oid,'objectType':PROFILE_ID+':timeline','name':'Synthetic temporal timeline','description':'Own companion namespace, not a domain state-machine subtype','recordedAt':at,'previousRecordId':None,'state':'active','provenance':{'source':register,'synthetic':True},'accessClass':'synthetic-private'}
            path=root/(name+'-object.json');path.write_bytes(p.encode(obj));append(target,'object',path);facts=[]
            for i,snapshot in enumerate([first,second],1):
                fact={'recordType':'fact','schemaVersion':'1.0.0','factId':oid+':snapshot-r'+str(i),'subjectId':oid,'path':'temporal.timeline.snapshot','value':snapshot,'unit':None,'validFrom':at,'validTo':None,'recordedAt':at,'supersedes':[] if i==1 else [oid+':snapshot-r1'],'status':'asserted','provenance':{'source':register,'synthetic':True,'snapshotDigest':p.digest(snapshot),'previousSnapshotDigest':None if i==1 else p.digest(first)},'authority':{'source':operator,'rank':0},'masterSystem':register,'accessClass':'synthetic-private'}
                path=root/(name+'-fact'+str(i)+'.json');path.write_bytes(p.encode(fact));result=append(target,'fact',path);facts.append(target/result['written'])
            f1,f2=[p.load(x) for x in facts];p.require([f1['value'],f2['value']]==[first,second],'Stored roundtrip differs')
            module.validate_snapshot(f1,dimension=dimension,now=checkAt);module.validate_snapshot(f2,dimension=dimension,now=checkAt,previous=f1)
            def query(k):return module.resolve(f2['value'],config,actor=config['readers'][0],purpose='research',validAt='2026-02-01T00:00:00Z',knownAt=k,now=NOW)
            before,after=query('2026-01-31T00:00:00Z'),query('2026-02-11T00:00:00Z')
            p.require(before['segment']['value']==q1['segments'][0]['value'] and after['segment']['value']==q2['segments'][1]['value'],'Bitemporal stored answers differ')
            native=native_validate(target);p.require(native['valid'],'Native validation failed')
            original=facts[-1].read_bytes();bad=copy.deepcopy(f2);bad['value']['commits'][0]['request']['segments'][0]['validFrom']='not-an-instant';facts[-1].write_bytes(p.encode(bad));outer=native_validate(target);nested=False
            try:module.validate_snapshot(bad,dimension=dimension,now=checkAt,previous=f1)
            except module.Invalid:nested=True
            finally:facts[-1].write_bytes(original)
            p.require(outer['valid'] and nested,'Native/companion distinction missing')
            negatives=[]
            for label,mutator in [('truncation',lambda x:x['value']['commits'].clear()),('digest',lambda x:x['provenance'].update(snapshotDigest='sha256:'+'0'*64)),('subject',lambda x:x.update(subjectId='urn:synthetic:wrong')),('predecessor',lambda x:x.update(supersedes=[]))]:
                bad=copy.deepcopy(f2);mutator(bad);failed=False
                if label=='truncation':bad['provenance']['snapshotDigest']=p.digest(bad['value'])
                try:module.validate_snapshot(bad,dimension=dimension,now=checkAt,previous=f1)
                except module.Invalid:failed=True
                p.require(failed,'Accepted '+label);negatives.append(label)
            cross_rejected=False
            try:module.validate_snapshot(f1,dimension='urn:synthetic:other-dimension',now=checkAt)
            except module.Invalid:cross_rejected=True
            p.require(cross_rejected,'Cross-Dimension snapshot admitted');negatives.append('cross-Dimension')
            native.pop('dimension',None);outer.pop('dimension',None)
            reports.append({'profile':name,'dimension':dimension,'objects':1,'facts':2,'native':native,'roundTripEqualsInput':True,'admissionReplayedThroughInstalledCompanion':True,'negativeCasesRejected':negatives,'storedAnswers':[before,after],'invalidNestedSnapshot':{'native':outer,'companionRejected':nested},'envelopeAuthorityMeaning':'Later native storage of synthetic pre-existing host history; inner receipts do not establish earlier native Dimension existence or domain fact priority','pins':[{'id':r['modelId'],'version':r['version'],'digest':r['specification']['digest'],'mode':r['installationMode']} for r in releases]})
    return {'format':'vercy-temporal-profile-acceptance','executedAt':c.now(),'passed':len(reports),'failed':0,'profiles':reports,'sourceDigests':{str(x.relative_to(HERE)):hashlib.sha256(x.read_bytes()).hexdigest() for x in [Path(__file__),HERE/'temporal.py',HERE/'temporal.schema.json',HERE/'spec.json',HERE/'tool-pins.json',HERE/'test_temporal.py']},'limits':'Three synthetic new Dimensions; own companion plus optional semantic-only parent. No IAM, domain truth/transition, durable concurrency, production capacity or existing-Dimension migration proof.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True);args=ap.parse_args();report=run(args.composer,args.skill);Path(args.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':report['passed'],'failed':report['failed']}))
