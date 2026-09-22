"""Install exact candidate bytes in three new synthetic Vercy Dimensions."""
import argparse,copy,hashlib,importlib.util,json,sys,tempfile
from datetime import datetime,timedelta,timezone
from pathlib import Path
import classification_review as r
HERE=Path(__file__).resolve().parent
SLUG='enterprise-classification-review'

def run(composer,skill):
    composer=Path(composer).resolve();skill=Path(skill).resolve();pins=json.loads((HERE/'tool-pins.json').read_text(encoding='utf-8'))
    for field,root in [('composerFiles',composer),('skillFiles',skill),('upstreamFiles',HERE/'upstream')]:
        for n,h in pins[field].items():r.require(hashlib.sha256((root/n).read_bytes()).hexdigest()==h,'Unexpected trusted asset: '+n)
    sys.path.insert(0,str(composer));import composition as c
    from bootstrap_dimension import bootstrap
    sys.path.insert(0,str(skill/'scripts'));from write_record import append,VercyError
    from validate_dimension import validate as native_validate
    at=c.now();expires=(datetime.now(timezone.utc)+timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ');reports=[]
    with tempfile.TemporaryDirectory(prefix='vercy-classification-acceptance-') as tmp:
        root=Path(tmp).resolve();assets=root/'assets';assets.mkdir()
        def descriptor(folder,name,source,base):
            raw=source.read_bytes();dest=assets/folder/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
            media='application/json' if name.endswith('.json') else 'text/x-python' if name.endswith('.py') else 'text/markdown' if name.endswith('.md') else 'application/yaml'
            return {'path':folder+'/'+name,'digest':c.digest(raw),'size':len(raw),'mediaType':media,'sourceUrl':base+name}
        def release(mid,version,folder,source,base,native):
            specname='spec.json' if native else 'spec.yaml';ds=descriptor(folder,specname,source/specname,base);binding=None
            if native:
                binding={'id':'urn:vercy:binding:'+SLUG,'version':'0.1.0','forSpecificationDigest':ds['digest'],'runtime':descriptor(folder,'runtime-model.reference.json',source/'runtime-model.reference.json',base),'instanceSchema':descriptor(folder,'classification.schema.json',source/'classification.schema.json',base),'companionValidator':descriptor(folder,'classification_review.py',source/'classification_review.py',base),'scope':'Own restricted Assessment object; outer native checks plus separately executed installed nested consistency evaluator; host authority remains external.'}
            return {'modelId':mid,'version':version,'namespace':'urn:vercy:model:'+mid,'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','requires':[],'references':[],'specification':ds,'agents':descriptor(folder,'AGENTS.md',source/'AGENTS.md',base),'installationMode':'native-binding' if native else 'semantic-only','binding':binding,'semanticFingerprint':None,'compatibility':{'decision':'accepted','reviewer':'urn:synthetic:reviewer:classification','evidence':'urn:synthetic:acceptance:classification','observedAt':at,'scope':'Synthetic candidate installation only, not proof of production publication, source truth or parent conformance.'}}
        base='https://ver.cy/models/'+SLUG+'/versions/0.1.0/'
        releases=[]
        for slug,mid in [('wm-knw-018-taxonomy-classification-scheme','vr.wm-knw-018'),('wm-xct-020-classification-binding','vr.wm-xct-020')]:
            releases.append(release(mid,'0.3.0-research.1',slug,HERE/'upstream'/slug,'https://ver.cy/models/'+slug+'/',False))
        companion=release(r.MODEL,'0.1.0',SLUG,HERE,base,True);companion['references']=[{'modelId':x['modelId'],'version':x['version']} for x in releases];releases.append(companion)
        for name in ('startup','international','ai-team'):
            f=r.decode((HERE/'examples'/(name+'.json')).read_bytes());dimension=f['packet']['dimensionId'];target=root/name;stage=root/(name+'-stage');pp=root/(name+'-policy.json');lp=root/(name+'-lock.json');planp=root/(name+'-plan.json')
            r.require(target.resolve().is_relative_to(root) and stage.resolve().is_relative_to(root),'Target escaped owned temporary directory')
            policy={'format':'vercy-composition-policy','version':1,'id':'urn:synthetic:composition-policy:classification','dimensionId':dimension,'owner':f['packet']['owner'],'allowInstall':True,'actors':['urn:synthetic:actor:composer'],'purposes':['Synthetic classification acceptance'],'allowedModelIds':[x['modelId'] for x in releases],'allowedOrigins':['https://ver.cy'],'reviewers':['urn:synthetic:reviewer:classification'],'allowReviewableDrafts':True,'validFrom':at,'validUntil':expires}
            pp.write_bytes(c.encode(policy));lp.write_bytes(c.encode({'models':[]}))
            plan={'format':'vercy-composition-plan','schemaVersion':'1.0.0','planId':'urn:synthetic:composition:classification:'+name,'revision':1,'supersedes':None,'algorithm':'exact-closure-v1','dimensionId':dimension,'createdAt':at,'validUntil':expires,'baseLockDigest':c.digest(lp.read_bytes()),'roots':[{'modelId':x['modelId'],'version':x['version']} for x in releases],'releases':releases,'authority':{'actor':policy['actors'][0],'allowReviewableDrafts':True,'allowedModelIds':policy['allowedModelIds'],'decision':'allow','owner':policy['owner'],'policyDigest':c.digest(pp.read_bytes()),'policyRef':policy['id'],'purpose':policy['purposes'][0]},'provenance':{'classification':'public-synthetic','evidenceKind':'proposal','masterSystem':'urn:synthetic:reference','recordedAt':at,'source':'urn:synthetic:fixture:'+name}}
            planp.write_bytes(c.encode(plan));c.stage(planp,assets,pp,lp,stage);bootstrap(stage,pp,lp,skill,target,'Synthetic classification '+name,dimension)
            installed=target/'models/composed'/SLUG/'classification_review.py'
            for n,key in [('classification_review.py','companionValidator'),('classification.schema.json','instanceSchema')]:r.require(c.digest((installed.parent/n).read_bytes())==companion['binding'][key]['digest'],'Installed bytes differ')
            ms=importlib.util.spec_from_file_location('installed_classification_'+name,installed);module=importlib.util.module_from_spec(ms);ms.loader.exec_module(module)
            # Host authority is issued independently for this test invocation, not inferred from fixture scores.
            host=copy.deepcopy(f['host']);host.update(validFrom=at,validUntil=expires)
            assessment=module.review(f['packet'],host,host['actor'],host['purpose'],at)
            for key,wanted in f['expected'].items():r.require(assessment[key]==wanted,'Installed disposition differs')
            value={'packet':f['packet'],'assessment':assessment};obj,fact=module.native_records(value,at)
            r.require(module.build_id()==r.build_id(),'Installed build differs')
            paths=[]
            for i,(kind,record) in enumerate([('object',obj),('fact',fact)]):
                path=root/(name+'-'+str(i)+'.json');path.write_bytes(module.encode(record));out=append(target,kind,path);paths.append(target/out['written'])
            stored=[module.decode(p.read_bytes()) for p in paths];r.require(module.encode(stored)==module.encode([obj,fact]),'Native stored bytes changed')
            nested=module.validate_native_fact(stored[1]);native=native_validate(target);r.require(native['valid'],'Native validation failed')
            duplicate=False;stored_fact_bytes=paths[1].read_bytes()
            try:append(target,'fact',root/(name+'-1.json'))
            except VercyError as exc:duplicate='already exists' in str(exc)
            r.require(duplicate and paths[1].read_bytes()==stored_fact_bytes,'Duplicate recording changed data')
            original=paths[1].read_bytes();bad=copy.deepcopy(fact);bad['value']['assessment']['outcome']='candidate-only' if assessment['outcome']!='candidate-only' else 'human-review-required';paths[1].write_bytes(module.encode(bad))
            outer=native_validate(target);rejected=False
            try:module.validate_native_fact(bad)
            except module.Invalid:rejected=True
            finally:paths[1].write_bytes(original)
            r.require(outer['valid'] and rejected,'Outer/nested distinction not demonstrated')
            native.pop('dimension',None);outer.pop('dimension',None)
            reports.append({'profile':name,'objects':1,'facts':1,'expected':f['expected'],'observed':{k:assessment[k] for k in f['expected']},'native':native,'nested':nested,'duplicateIdRejectedWithoutMutation':duplicate,'nativeRoundTripExact':True,'invalidNestedSnapshot':{'outerNative':outer,'companionRejected':rejected},'buildId':module.build_id(),'pins':[{'id':x['modelId'],'version':x['version'],'digest':x['specification']['digest'],'mode':x['installationMode']} for x in releases]})
    names=['acceptance.py','classification_review.py','classification.schema.json','spec.json','tool-pins.json',*['examples/'+n+'.json' for n in ('startup','international','ai-team')]]
    return {'format':'vercy-classification-native-acceptance','executedAt':c.now(),'passed':len(reports),'failed':0,'profiles':reports,'sourceDigests':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in names},'limits':'Three NEW synthetic Dimensions; exact generic composition and separately run installed evaluator. No production IAM, source authenticity, classifier quality, standard certification or existing-Dimension migration.'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--composer',required=True);ap.add_argument('--skill',required=True);ap.add_argument('--report',required=True);args=ap.parse_args();report=run(args.composer,args.skill);Path(args.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({'passed':report['passed'],'failed':report['failed']}))
