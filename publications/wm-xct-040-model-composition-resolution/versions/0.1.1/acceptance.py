"""Reproduce three synthetic new-Dimension trials against a trusted Vercy skill.
Usage: python acceptance.py --skill /trusted/vercy/skills/vercy --report result.json
Never uses real company data or changes an existing Dimension.
"""
from pathlib import Path
import argparse,copy,importlib.util,json,sys,tempfile,subprocess,shutil
from unittest.mock import patch
import bootstrap_dimension as bd
import composition as c
from bootstrap_dimension import bootstrap

def run(skill):
    if not __debug__:raise RuntimeError('Acceptance checks require Python without -O')
    skill=Path(skill).resolve();examples=Path(__file__).resolve().parent/'examples'
    sys.path.insert(0,str(skill/'scripts'))
    from write_record import append
    from validate_dimension import validate as native_validate
    reports=[];failure_checks=[]
    with tempfile.TemporaryDirectory(prefix='vercy-composition-acceptance-') as tmp:
        root=Path(tmp)
        for name in ['startup','group','ai-team']:
            src=examples/name;plan=c.load(src/'plan.json');stage=root/(name+'-stage');target=root/name
            c.stage(src/'plan.json',examples/'assets',src/'policy.json',src/'current.lock',stage)
            result=bootstrap(stage,src/'policy.json',src/'current.lock',skill,target,'Synthetic '+name,plan['dimensionId'])
            assert c.load(target/'dimension.yaml')['id']==plan['dimensionId']
            obj={'recordType':'object','schemaVersion':'1.0.0','recordId':'urn:synthetic:org:'+name+':r1','objectId':'urn:synthetic:org:'+name,'objectType':'vr.wm-org-001:organization','name':'Synthetic '+name,'description':'Public fictional acceptance fixture','recordedAt':c.now(),'previousRecordId':None,'state':'active','provenance':{'source':'urn:synthetic:reference','synthetic':True},'accessClass':'synthetic-private'}
            # Start from the current runtime fact template, retaining its exact temporal/provenance shape.
            template=c.load(examples/'native-fact.reference.json')
            fact={**template,'factId':'urn:synthetic:org:'+name+':name:r1','subjectId':obj['objectId'],'path':'organization.reference.name','value':obj['name'],'unit':None}
            for kind,value in [('object',obj),('fact',fact)]:
                f=root/(name+'-'+kind+'.json');f.write_bytes(c.encode(value));append(target,kind,f)
            nested=None
            if name=='ai-team':
                vf=target/'models/composed/wm-org-017-performance-objective-review/validate_examples.py'
                validator_digest=c.digest(vf.read_bytes());assert validator_digest==next(r for r in plan['releases'] if r['modelId']=='vr.wm-org-017')['binding']['companionValidator']['digest']
                module_spec=importlib.util.spec_from_file_location('trusted_performance_reference',vf);module=importlib.util.module_from_spec(module_spec);module_spec.loader.exec_module(module)
                actual_fact=c.load(examples/'native-fact.reference.json');good=actual_fact['value'];assert good==c.load(examples/'example-founder-draft.json')
                bad=copy.deepcopy(good);bad['policy']['automatic_employment_decisions']=True
                assert not module.errors(good) and module.errors(bad)
                append(target,'object',examples/'native-object.reference.json')
                bad_target=root/'ai-team-negative-copy';shutil.copytree(target,bad_target)
                bad_fact=copy.deepcopy(actual_fact);bad_fact['value']=bad;bad_file=root/'bad-performance-fact.json';bad_file.write_bytes(c.encode(bad_fact))
                bad_written=append(bad_target,'fact',bad_file);negative_native=native_validate(bad_target);assert negative_native['valid'];negative_native.pop('dimension',None)
                actual_bad=c.load(bad_target/bad_written['written']);assert module.errors(actual_bad['value'])
                good_written=append(target,'fact',examples/'native-fact.reference.json');assert not module.errors(c.load(target/good_written['written'])['value'])
                nested={'positiveStoredFactPassed':True,'negativeStoredFactPassedV3':True,'negativeStoredFactRejectedByCompanion':True,'executedInstalledValidatorDigest':validator_digest,'negativeNativeReport':negative_native,'rule':'No automatic employment decisions','execution':'Explicit trusted acceptance harness only; composer never executes package code.'}
            validation=native_validate(target);assert validation['valid'],validation
            # A second bootstrap must refuse, preserving all bytes.
            before={str(p.relative_to(target)):c.digest(p.read_bytes()) for p in target.rglob('*') if p.is_file()}
            try:bootstrap(stage,src/'policy.json',src/'current.lock',skill,target,'Synthetic '+name,plan['dimensionId'])
            except c.Invalid:pass
            else:raise AssertionError('existing Dimension was not refused')
            assert before=={str(p.relative_to(target)):c.digest(p.read_bytes()) for p in target.rglob('*') if p.is_file()}
            validation.pop('dimension',None)
            reports.append({'profile':name,'passed':True,'nativeModels':result['nativeBoundModels'],'semanticOnlyModels':result['semanticOnlyModels'],'nativeValidation':validation,'nestedValidation':nested,'existingDimensionPreserved':True})
        src=examples/'startup';stage=root/'startup-stage';plan=c.load(src/'plan.json')
        def invoke(target,namespace=plan['dimensionId']):return bootstrap(stage,src/'policy.json',src/'current.lock',skill,target,'Synthetic startup',namespace)
        target=root/'wrong-dimension'
        try:invoke(target,'urn:dimension:other')
        except c.Invalid as e:assert str(e).startswith('OWNER:')
        else:raise AssertionError('namespace mismatch allowed')
        assert not target.exists();failure_checks.append('authorized Dimension identity enforced')
        target=root/'native-invalid';real_run=bd.subprocess.run
        def invalid_native(cmd,**kwargs):
            if str(skill/'scripts/vercy.py') in cmd:return subprocess.CompletedProcess(cmd,1,json.dumps({'valid':False,'errors':['injected acceptance failure']}),'')
            return real_run(cmd,**kwargs)
        with patch.object(bd.subprocess,'run',side_effect=invalid_native):
            try:invoke(target)
            except c.Invalid as e:assert str(e).startswith('NATIVE:')
            else:raise AssertionError('native failure activated')
        assert not target.exists() and not list(root.glob('.native-invalid.*'));failure_checks.append('failed native validation never activates')
        target=root/'rename-invalid'
        with patch.object(c.os,'rename',side_effect=OSError('injected rename failure')):
            try:invoke(target)
            except OSError:pass
            else:raise AssertionError('rename failure ignored')
        assert not target.exists() and not list(root.glob('.rename-invalid.*'));failure_checks.append('failed activation cleans only own temporary state')
    return {'format':'vercy-composition-acceptance','executedAt':c.now(),'passed':len(reports),'failed':0,'scope':'Synthetic limited bindings, not startup/group/AI-enterprise domain completeness; no real company data.','profiles':reports,'bootstrapFailureChecks':failure_checks}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--skill',required=True);p.add_argument('--report',required=True);a=p.parse_args();report=run(a.skill);Path(a.report).write_bytes(c.encode(report));print(json.dumps(report,indent=2))
