"""Trusted synthetic new-Dimension composition, admission and snapshot checks."""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from datetime import datetime,timedelta,timezone
from pathlib import Path
import authority as p
HERE=Path(__file__).resolve().parent
PROFILE_ID='vr.profile.enterprise-fact-authority'
SLUG='enterprise-fact-authority'
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
                binding={'id':'urn:vercy:binding:enterprise-fact-authority','version':'0.1.0','forSpecificationDigest':ds['digest'],'runtime':descriptor(folder,'runtime-model.reference.json',HERE/'runtime-model.reference.json',base+'runtime-model.reference.json'),'instanceSchema':descriptor(folder,'authority.schema.json',HERE/'authority.schema.json',base+'authority.schema.json'),'companionValidator':descriptor(folder,'authority.py',HERE/'authority.py',base+'authority.py'),'scope':'Own companion namespace/specification; no parent subtype. Explicit nested validation and admission required.'}
            return {'modelId':mid,'version':version,'namespace':'urn:vercy:model:'+mid,'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','requires':[],'references':[],'specification':ds,'agents':da,'installationMode':'native-binding' if native else 'semantic-only','binding':binding,'semanticFingerprint':None,'compatibility':{'decision':'accepted','reviewer':'urn:synthetic:reviewer:authority','evidence':'urn:synthetic:acceptance:authority','observedAt':at,'scope':'Synthetic candidate-installation exercise, not global parent ratification; publication and research assurance are separate.'}}
        parent='wm-xct-001-ownership-stewardship';up=HERE/'upstream'/parent
        semantic=release('vr.wm-xct-001','0.3.0-research.1',parent,up/'spec.yaml',up/'AGENTS.md','https://ver.cy/models/'+parent+'/versions/0.3.0-research.1/',False)
        companion=release(PROFILE_ID,'0.1.0',SLUG,HERE/'spec.json',HERE/'AGENTS.md','https://ver.cy/models/'+parent+'/profiles/enterprise-fact-authority/0.1.0/',True)
        companion['references']=[{'modelId':semantic['modelId'],'version':semantic['version']}];releases=[semantic,companion]
        for name in ['startup','group','ai-team']:
            config=p.load(HERE/('examples/'+name+'.config.json'));fixture=p.load(HERE/('examples/'+name+'.json'));target=root/name;stage=root/(name+'-stage');pp=root/(name+'-policy.json');lp=root/(name+'-lock.json');planp=root/(name+'-plan.json');dimension=config['dimension']
            policy={'format':'vercy-composition-policy','version':1,'id':'urn:synthetic:composition-policy:authority','dimensionId':dimension,'owner':'urn:synthetic:owner:installation','allowInstall':True,'actors':['urn:synthetic:actor:composer'],'purposes':['Synthetic fact authority reference'],'allowedModelIds':[r['modelId'] for r in releases],'allowedOrigins':['https://ver.cy'],'reviewers':['urn:synthetic:reviewer:authority'],'allowReviewableDrafts':True,'validFrom':at,'validUntil':expires}
            pp.write_bytes(c.encode(policy));lp.write_bytes(c.encode({'models':[]}))
            plan={'format':'vercy-composition-plan','schemaVersion':'1.0.0','planId':'urn:synthetic:composition:authority:'+name,'revision':1,'supersedes':None,'algorithm':'exact-closure-v1','dimensionId':dimension,'createdAt':at,'validUntil':expires,'baseLockDigest':c.digest(lp.read_bytes()),'roots':[{'modelId':r['modelId'],'version':r['version']} for r in releases],'releases':releases,'authority':{'actor':policy['actors'][0],'allowReviewableDrafts':True,'allowedModelIds':policy['allowedModelIds'],'decision':'allow','owner':policy['owner'],'policyDigest':c.digest(pp.read_bytes()),'policyRef':policy['id'],'purpose':policy['purposes'][0]},'provenance':{'classification':'public-synthetic','evidenceKind':'proposal','masterSystem':'urn:synthetic:reference','recordedAt':at,'source':'urn:synthetic:fixture:'+name}}
            planp.write_bytes(c.encode(plan));c.stage(planp,assets,pp,lp,stage);bootstrap(stage,pp,lp,skill,target,'Synthetic authority '+name,dimension)
            installed=target/'models/composed'/SLUG/'authority.py';p.require(c.digest(installed.read_bytes())==companion['binding']['companionValidator']['digest'],'Code differs');p.require(c.digest((installed.parent/'authority.schema.json').read_bytes())==companion['binding']['instanceSchema']['digest'],'Schema differs')
            ms=importlib.util.spec_from_file_location('installed_authority_'+name,installed);module=importlib.util.module_from_spec(ms);ms.loader.exec_module(module)
            ledger=module.empty(dimension)
            entries=sorted([(x,'authority') for x in fixture['authorities']]+[(x,'observation') for x in fixture['observations']],key=lambda item:item[0]['recordedAt'])
            for row,kind in entries:ledger=module.admit(ledger,row,kind,config,row['issuedBy'] if kind=='authority' else row['writer'],row['recordedAt'])
            p.require(ledger==fixture,'Fixture admission differs');module.validate_extension(module.empty(dimension),ledger,config)
            correction=copy.deepcopy(ledger['observations'][-1]);correction.update(revision=2,previousDigest=module.digest(correction),change='correction',recordedAt='2026-09-21T10:01:00Z',value=copy.deepcopy(ledger['observations'][0]['value']))
            updated=module.admit(ledger,correction,'observation',config,correction['writer'],correction['recordedAt']);module.validate_extension(ledger,updated,config)
            oid=dimension+':authority-register';operator='urn:synthetic:register-operator';register='urn:synthetic:governance-register'
            p.require(all(operator!=a['accountable'] and all(operator!=s['party'] for s in a['stewardships']) for a in updated['authorities']),'Envelope operator is not a steward/accountable role')
            obj={'recordType':'object','schemaVersion':'1.0.0','recordId':oid+':object-r1','objectId':oid,'objectType':PROFILE_ID+':authority-register','name':'Synthetic authority register','description':'Own companion namespace, not a ControlRecord or Company','recordedAt':at,'previousRecordId':None,'state':'active','provenance':{'source':register,'synthetic':True},'accessClass':'synthetic-private'}
            path=root/(name+'-object.json');path.write_bytes(p.encode(obj));append(target,'object',path);facts=[]
            for i,snapshot in enumerate([ledger,updated],1):
                fact={'recordType':'fact','schemaVersion':'1.0.0','factId':oid+':snapshot-r'+str(i),'subjectId':oid,'path':'authority.register.snapshot','value':snapshot,'unit':None,'validFrom':at,'validTo':None,'recordedAt':at,'supersedes':[] if i==1 else [oid+':snapshot-r1'],'status':'asserted','provenance':{'source':register,'synthetic':True,'snapshotDigest':p.digest(snapshot),'previousSnapshotDigest':None if i==1 else p.digest(ledger)},'authority':{'source':operator,'rank':0},'masterSystem':register,'accessClass':'synthetic-private'}
                path=root/(name+'-fact'+str(i)+'.json');path.write_bytes(p.encode(fact));result=append(target,'fact',path);facts.append(target/result['written'])
            stored=[p.load(x)['value'] for x in facts];p.require(stored==[ledger,updated],'Stored round-trip differs');module.validate_extension(stored[0],stored[1],config)
            def evaluate(snapshot):return module.evaluate(snapshot,config,actor='urn:synthetic:reader',purpose='governance-review',scope='urn:synthetic:scope',predicate='urn:synthetic:predicate',subject='urn:synthetic:subject',validAt='2026-09-21T12:00:00Z',knownAt='2026-09-21T12:00:00Z',now='2026-09-21T12:00:00Z')
            decisions=[evaluate(x) for x in stored];p.require(decisions[0]['status']==('contested' if name=='startup' else 'preferred') and decisions[1]['status']=='preferred','Stored outcomes differ')
            native=native_validate(target);p.require(native['valid'],'Native validation failed');victim=facts[-1];original=victim.read_bytes();bad=p.load(victim);bad['value']['authorities'][0]['rules'][0]['priority']=-1;victim.write_bytes(p.encode(bad));negative=native_validate(target);rejected=False
            try:module.validate_ledger(p.load(victim)['value'],config)
            except module.Invalid:rejected=True
            finally:victim.write_bytes(original)
            p.require(negative['valid'] and rejected,'Native/companion distinction missing')
            truncated=p.load(victim);truncated['value']=copy.deepcopy(stored[0]);truncated['value']['observations'].pop();victim.write_bytes(p.encode(truncated));truncation_rejected=False
            try:module.validate_extension(stored[0],p.load(victim)['value'],config)
            except module.Invalid:truncation_rejected=True
            finally:victim.write_bytes(original)
            p.require(truncation_rejected,'Snapshot truncation was accepted');native.pop('dimension',None);negative.pop('dimension',None)
            reports.append({'profile':name,'objects':1,'facts':2,'native':native,'roundTripEqualsInput':True,'admissionReplayedThroughInstalledCompanion':True,'snapshotTruncationRejected':True,'storedDecisions':decisions,'invalidNestedSnapshot':{'native':negative,'companionRejected':rejected},'envelopeOperator':operator,'envelopeAuthorityMeaning':'Snapshot storage only; never domain fact precedence','pins':[{'id':r['modelId'],'version':r['version'],'digest':r['specification']['digest'],'mode':r['installationMode']} for r in releases]})
    return {'format':'vercy-authority-profile-acceptance','executedAt':c.now(),'passed':len(reports),'failed':0,'profiles':reports,'sourceDigests':{str(x.relative_to(HERE)):hashlib.sha256(x.read_bytes()).hexdigest() for x in [Path(__file__),HERE/'authority.py',HERE/'authority.schema.json',HERE/'spec.json',HERE/'tool-pins.json',*sorted((HERE/'examples').glob('*.json'))]},'limits':'Synthetic new Dimensions; semantic-only parent plus separately identified companion. Candidate-installation metadata anticipates publication. No IAM, source truth, durable concurrency or existing-Dimension migration proof.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True);args=ap.parse_args();report=run(args.composer,args.skill);Path(args.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':report['passed'],'failed':report['failed']}))
