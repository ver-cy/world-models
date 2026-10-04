"""Trusted synthetic new-Dimension composition, admission and snapshot checks."""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from datetime import datetime,timedelta,timezone
from pathlib import Path
import provenance as p
HERE=Path(__file__).resolve().parent
PROFILE_ID='vr.profile.enterprise-assertion-provenance'
SLUG='enterprise-assertion-provenance'
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
                binding={'id':'urn:vercy:binding:enterprise-assertion-provenance','version':'0.1.0','forSpecificationDigest':ds['digest'],'runtime':descriptor(folder,'runtime-model.reference.json',HERE/'runtime-model.reference.json',base+'runtime-model.reference.json'),'instanceSchema':descriptor(folder,'provenance.schema.json',HERE/'provenance.schema.json',base+'provenance.schema.json'),'companionValidator':descriptor(folder,'provenance.py',HERE/'provenance.py',base+'provenance.py'),'scope':'Own companion namespace/specification; no parent subtype. Explicit nested validation and admission required.'}
            return {'modelId':mid,'version':version,'namespace':'urn:vercy:model:'+mid,'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','requires':[],'references':[],'specification':ds,'agents':da,'installationMode':'native-binding' if native else 'semantic-only','binding':binding,'semanticFingerprint':None,'compatibility':{'decision':'accepted','reviewer':'urn:synthetic:reviewer:authority','evidence':'urn:synthetic:acceptance:authority','observedAt':at,'scope':'Synthetic candidate-installation exercise, not global parent ratification; publication and research assurance are separate.'}}
        parent='wm-xct-012-provenance';up=HERE/'upstream'/parent
        semantic=release('vr.wm-xct-012','0.3.0-research.1',parent,up/'spec.yaml',up/'AGENTS.md','https://ver.cy/models/enterprise-assertion-provenance/versions/0.1.0/upstream/'+parent+'/',False)
        companion=release(PROFILE_ID,'0.1.0',SLUG,HERE/'spec.json',HERE/'AGENTS.md','https://ver.cy/models/enterprise-assertion-provenance/versions/0.1.0/',True)
        companion['references']=[{'modelId':semantic['modelId'],'version':semantic['version']}];releases=[semantic,companion]
        for name in ['startup','group','ai-team']:
            config=p.load(HERE/('examples/'+name+'.config.json'));fixture=p.load(HERE/('examples/'+name+'.json'));target=root/name;stage=root/(name+'-stage');pp=root/(name+'-policy.json');lp=root/(name+'-lock.json');planp=root/(name+'-plan.json');dimension=config['dimension']
            policy={'format':'vercy-composition-policy','version':1,'id':'urn:synthetic:composition-policy:authority','dimensionId':dimension,'owner':'urn:synthetic:owner:installation','allowInstall':True,'actors':['urn:synthetic:actor:composer'],'purposes':['Synthetic assertion provenance reference'],'allowedModelIds':[r['modelId'] for r in releases],'allowedOrigins':['https://ver.cy'],'reviewers':['urn:synthetic:reviewer:authority'],'allowReviewableDrafts':True,'validFrom':at,'validUntil':expires}
            pp.write_bytes(c.encode(policy));lp.write_bytes(c.encode({'models':[]}))
            plan={'format':'vercy-composition-plan','schemaVersion':'1.0.0','planId':'urn:synthetic:composition:authority:'+name,'revision':1,'supersedes':None,'algorithm':'exact-closure-v1','dimensionId':dimension,'createdAt':at,'validUntil':expires,'baseLockDigest':c.digest(lp.read_bytes()),'roots':[{'modelId':r['modelId'],'version':r['version']} for r in releases],'releases':releases,'authority':{'actor':policy['actors'][0],'allowReviewableDrafts':True,'allowedModelIds':policy['allowedModelIds'],'decision':'allow','owner':policy['owner'],'policyDigest':c.digest(pp.read_bytes()),'policyRef':policy['id'],'purpose':policy['purposes'][0]},'provenance':{'classification':'public-synthetic','evidenceKind':'proposal','masterSystem':'urn:synthetic:reference','recordedAt':at,'source':'urn:synthetic:fixture:'+name}}
            planp.write_bytes(c.encode(plan));c.stage(planp,assets,pp,lp,stage);bootstrap(stage,pp,lp,skill,target,'Synthetic provenance '+name,dimension)
            installed=target/'models/composed'/SLUG/'provenance.py';p.require(c.digest(installed.read_bytes())==companion['binding']['companionValidator']['digest'],'Code differs');p.require(c.digest((installed.parent/'provenance.schema.json').read_bytes())==companion['binding']['instanceSchema']['digest'],'Schema differs')
            ms=importlib.util.spec_from_file_location('installed_authority_'+name,installed);module=importlib.util.module_from_spec(ms);ms.loader.exec_module(module)
            ledger={'format':'vercy-assertion-provenance','version':'0.1.0','dimension':dimension,'records':[]}
            initial=copy.deepcopy(ledger)
            for row in fixture['records']:ledger=module.admit(ledger,row,config,row['writer'],row['recordedAt'])
            p.require(ledger==fixture,'Fixture admission differs');module.validate_extension(initial,ledger,config)
            correction=copy.deepcopy(ledger['records'][0]);correction.update(revision=2,previousDigest=module.digest(correction),change='correct',recordedAt='2026-09-21T10:01:00Z',integrity='mismatched',reason='Synthetic later integrity check')
            updated=module.admit(ledger,correction,config,correction['writer'],correction['recordedAt']);module.validate_extension(ledger,updated,config)
            oid=dimension+':provenance-register';operator='urn:synthetic:register-operator';register='urn:synthetic:governance-register'
            obj={'recordType':'object','schemaVersion':'1.0.0','recordId':oid+':object-r1','objectId':oid,'objectType':PROFILE_ID+':provenance-register','name':'Synthetic provenance register','description':'Own companion namespace, not a ControlRecord or Company','recordedAt':at,'previousRecordId':None,'state':'active','provenance':{'source':register,'synthetic':True},'accessClass':'synthetic-private'}
            path=root/(name+'-object.json');path.write_bytes(p.encode(obj));append(target,'object',path);facts=[]
            for i,snapshot in enumerate([ledger,updated],1):
                fact={'recordType':'fact','schemaVersion':'1.0.0','factId':oid+':snapshot-r'+str(i),'subjectId':oid,'path':'provenance.register.snapshot','value':snapshot,'unit':None,'validFrom':at,'validTo':None,'recordedAt':at,'supersedes':[] if i==1 else [oid+':snapshot-r1'],'status':'asserted','provenance':{'source':register,'synthetic':True,'snapshotDigest':p.digest(snapshot),'previousSnapshotDigest':None if i==1 else p.digest(ledger)},'authority':{'source':operator,'rank':0},'masterSystem':register,'accessClass':'synthetic-private'}
                path=root/(name+'-fact'+str(i)+'.json');path.write_bytes(p.encode(fact));result=append(target,'fact',path);facts.append(target/result['written'])
            stored=[p.load(x)['value'] for x in facts];p.require(stored==[ledger,updated],'Stored round-trip differs');module.validate_extension(stored[0],stored[1],config)
            first,second=[p.load(x) for x in facts];module.validate_snapshot(first,config,now='2026-09-21T12:00:00Z');module.validate_snapshot(second,config,first,now='2026-09-21T12:00:00Z')
            bad_pin=copy.deepcopy(second);bad_pin['provenance']['snapshotDigest']='sha256:'+'0'*64
            pin_rejected=False
            try:module.validate_snapshot(bad_pin,config,first,now='2026-09-21T12:00:00Z')
            except module.Invalid:pin_rejected=True
            p.require(pin_rejected,'Native snapshot digest mismatch was accepted')
            def evaluate(snapshot):return module.view(snapshot,config,actor='urn:synthetic:reader',purpose='research',claim=fixture['records'][2]['claim'],knownAt='2026-09-21T12:00:00Z',now='2026-09-21T12:00:00Z')
            decisions=[evaluate(x) for x in stored]
            p.require(decisions[0]['truth']=='not-evaluated' and decisions[1]['impacts'][0]['requiresReview'],'Stored provenance outcomes differ')
            native=native_validate(target);p.require(native['valid'],'Native validation failed');victim=facts[-1];original=victim.read_bytes();bad=p.load(victim);bad['value']['records'][0]['representationDigest']='invalid';victim.write_bytes(p.encode(bad));negative=native_validate(target);rejected=False
            try:module.validate_ledger(p.load(victim)['value'],config)
            except module.Invalid:rejected=True
            finally:victim.write_bytes(original)
            p.require(negative['valid'] and rejected,'Native/companion distinction missing')
            truncated=p.load(victim);truncated['value']=copy.deepcopy(stored[0]);truncated['value']['records'].pop();victim.write_bytes(p.encode(truncated));truncation_rejected=False
            try:module.validate_extension(stored[0],p.load(victim)['value'],config)
            except module.Invalid:truncation_rejected=True
            finally:victim.write_bytes(original)
            p.require(truncation_rejected,'Snapshot truncation was accepted');native.pop('dimension',None);negative.pop('dimension',None)
            reports.append({'profile':name,'dimension':dimension,'objects':1,'facts':2,'native':native,'roundTripEqualsInput':True,'admissionReplayedThroughInstalledCompanion':True,'snapshotTruncationRejected':True,'snapshotDigestMismatchRejected':pin_rejected,'storedDecisions':decisions,'invalidNestedSnapshot':{'native':negative,'companionRejected':rejected},'envelopeOperator':operator,'envelopeAuthorityMeaning':'Snapshot storage only; never domain fact precedence','pins':[{'id':r['modelId'],'version':r['version'],'digest':r['specification']['digest'],'mode':r['installationMode']} for r in releases]})
    return {'format':'vercy-provenance-profile-acceptance','executedAt':c.now(),'passed':len(reports),'failed':0,'profiles':reports,'sourceDigests':{str(x.relative_to(HERE)):hashlib.sha256(x.read_bytes()).hexdigest() for x in [Path(__file__),HERE/'provenance.py',HERE/'provenance.schema.json',HERE/'spec.json',HERE/'tool-pins.json',*sorted((HERE/'examples').glob('*.json'))]},'limits':'Synthetic new Dimensions; semantic-only parent plus separately identified companion. Candidate-installation metadata anticipates publication. No IAM, source truth, durable concurrency or existing-Dimension migration proof.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True);args=ap.parse_args();report=run(args.composer,args.skill);Path(args.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':report['passed'],'failed':report['failed']}))
