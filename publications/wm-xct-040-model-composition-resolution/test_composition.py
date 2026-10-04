"""Behavioral tests, including adversarial semantic and state-change cases."""
from pathlib import Path
import copy, json, tempfile, unittest, datetime as dt
from unittest.mock import patch
import composition as c

class CompositionTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);self.assets=self.root/'assets';self.assets.mkdir()
        self.when=c.now();self.future=(dt.datetime.now(dt.timezone.utc)+dt.timedelta(days=1)).isoformat(timespec='seconds')
        self.policy={'format':'vercy-composition-policy','version':1,'id':'urn:policy:fixture','dimensionId':'urn:dimension:fixture','owner':'urn:owner:fixture','actors':['urn:actor:fixture'],'purposes':['Assemble synthetic company'],'allowInstall':True,'allowedModelIds':['test.company','test.unit','test.ai'],'allowReviewableDrafts':True,'reviewers':['urn:reviewer:fixture'],'allowedOrigins':['https://example.test'],'validFrom':'2026-01-01T00:00:00Z','validUntil':'2100-01-01T00:00:00Z'}
        self.policy_raw=c.encode(self.policy);self.lock_raw=c.encode(c.EMPTY_LOCK)
        self.plan={'format':'vercy-composition-plan','schemaVersion':'1.0.0','planId':'urn:plan:fixture','revision':1,'supersedes':None,'dimensionId':'urn:dimension:fixture','createdAt':self.when,'validUntil':self.future,'baseLockDigest':c.digest(self.lock_raw),'algorithm':'exact-closure-v1','authority':{'owner':'urn:owner:fixture','actor':'urn:actor:fixture','purpose':'Assemble synthetic company','policyRef':self.policy['id'],'policyDigest':c.digest(self.policy_raw),'decision':'allow','allowedModelIds':self.policy['allowedModelIds'],'allowReviewableDrafts':True},'roots':[{'modelId':'test.company','version':'1.0.0'}],'releases':[self.release('test.company')],'provenance':{'source':'urn:fixture:source','masterSystem':'urn:fixture:control-plane','recordedAt':self.when,'classification':'public-synthetic','evidenceKind':'proposal'}}
    def asset(self,path,value,media='application/json'):
        raw=c.encode(value) if not isinstance(value,bytes) else value
        p=self.assets/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
        return {'path':path,'digest':c.digest(raw),'size':len(raw),'mediaType':media,'sourceUrl':'https://example.test/'+path}
    def release(self,mid,native=False,nested=False):
        r={'modelId':mid,'version':'1.0.0','namespace':'urn:namespace:'+mid,'role':'core','publicationStatus':'published','researchAssurance':'reviewable-draft','semanticFingerprint':None,'specification':self.asset(mid+'/spec.yaml',{'metaModel':{'registryId':mid,'version':'1.0.0'}},'application/yaml'),'agents':self.asset(mid+'/AGENTS.md',b'# Synthetic fixture model\n','text/markdown'),'requires':[],'references':[],'installationMode':'semantic-only','binding':None,'compatibility':{'decision':'accepted','evidence':'urn:fixture:compatibility','reviewer':'urn:reviewer:fixture','observedAt':self.when,'scope':'Synthetic offline reference tests only'}}
        if native:
            r['installationMode']='native-binding';r['binding']={'id':'urn:binding:'+mid,'version':'1.0.0','forSpecificationDigest':r['specification']['digest'],'runtime':self.asset(mid+'/runtime.json',{'format':'vercy-runtime-model-schema','schemaVersion':'1.0.0','modelId':mid,'paths':{mid+'.snapshot':{'valueTypes':['object' if nested else 'string'],'units':[None]}}}),'instanceSchema':None,'companionValidator':None,'scope':'Fixture snapshot, not general domain conformance'}
            if nested:
                r['binding']['instanceSchema']=self.asset(mid+'/instance.schema.json',{'$schema':c.DIALECT,'type':'object','required':['name'],'properties':{'name':{'type':'string','minLength':1}},'additionalProperties':False})
                r['binding']['companionValidator']=self.asset(mid+'/validator.py',b'# Fixture only; never executed by composer\n','text/x-python')
        return r
    def runplan(self,plan=None):return c.validate(plan or self.plan,self.assets,self.policy_raw,self.lock_raw)
    def rejects(self,code):
        with self.assertRaisesRegex(c.Invalid,'^'+code+':'):self.runplan()
    def replaceasset(self,r,field,value):
        d=r['binding'][field];r['binding'][field]=self.asset(d['path'],value,d['mediaType'])
    def files(self):
        p=self.root/'plan.json';p.write_bytes(c.encode(self.plan));pol=self.root/'policy.json';pol.write_bytes(self.policy_raw);lock=self.root/'current.lock';lock.write_bytes(self.lock_raw);return p,pol,lock
    def test_startup_semantic_only(self):self.assertTrue(self.runplan()['valid'])
    def test_group_two_independent_roots(self):
        self.plan['releases'].append(self.release('test.unit',True));self.plan['roots'].append({'modelId':'test.unit','version':'1.0.0'});self.assertEqual(self.runplan()['modelCount'],2)
    def test_ai_structured_binding(self):
        self.plan['releases']=[self.release('test.company',True,True)];self.assertTrue(self.runplan()['valid'])
    def test_required_dependency_closure(self):
        self.plan['releases'][0]['requires']=[{'modelId':'test.unit','version':'1.0.0'}];self.plan['releases'].append(self.release('test.unit'));self.assertTrue(self.runplan()['valid'])
    def test_optional_reference_does_not_import_packages(self):
        self.plan['releases'][0]['references']=[{'modelId':'test.unit','version':'1.0.0'}];self.assertEqual(self.runplan()['modelCount'],1)
    def test_round_trip(self):self.assertEqual(self.runplan(),self.runplan(json.loads(c.encode(self.plan))))
    def test_correction_revision(self):self.plan.update(revision=2,supersedes='urn:plan:previous');self.assertTrue(self.runplan()['valid'])
    def test_unknown_top_level_field(self):self.plan['approvedByAi']=True;self.rejects('SCHEMA')
    def test_missing_runtime_binding(self):self.plan['releases'][0]['installationMode']='native-binding';self.rejects('READINESS')
    def test_hidden_binding(self):self.plan['releases']=[self.release('test.company',True)];self.plan['releases'][0]['installationMode']='semantic-only';self.rejects('READINESS')
    def test_empty_runtime(self):
        self.plan['releases']=[self.release('test.company',True)];r=self.plan['releases'][0];v=c.load(self.assets/r['binding']['runtime']['path']);v['paths']={};self.replaceasset(r,'runtime',v);self.rejects('BINDING')
    def test_nested_without_companion(self):
        self.plan['releases']=[self.release('test.company',True,True)];self.plan['releases'][0]['binding']['companionValidator']=None;self.rejects('NESTED')
    def test_external_schema_reference(self):
        self.plan['releases']=[self.release('test.company',True,True)];r=self.plan['releases'][0];s=c.load(self.assets/r['binding']['instanceSchema']['path']);s['properties']['name']={'$ref':'https://evil.test/schema'};self.replaceasset(r,'instanceSchema',s);self.rejects('SCHEMA-REF')
    def test_unresolved_internal_reference(self):
        self.plan['releases']=[self.release('test.company',True,True)];r=self.plan['releases'][0];s=c.load(self.assets/r['binding']['instanceSchema']['path']);s['properties']['name']={'$ref':'#/$defs/missing'};self.replaceasset(r,'instanceSchema',s);self.rejects('SCHEMA-REF')
    def test_unknown_schema_dialect(self):
        self.plan['releases']=[self.release('test.company',True,True)];r=self.plan['releases'][0];s=c.load(self.assets/r['binding']['instanceSchema']['path']);s['$schema']='https://example.test/dialect';self.replaceasset(r,'instanceSchema',s);self.rejects('DIALECT')
    def test_permissive_nested_schema(self):
        self.plan['releases']=[self.release('test.company',True,True)];r=self.plan['releases'][0];self.replaceasset(r,'instanceSchema',{'$schema':c.DIALECT});self.rejects('NESTED')
    def test_binding_spec_mismatch(self):
        self.plan['releases']=[self.release('test.company',True)];self.plan['releases'][0]['binding']['forSpecificationDigest']='sha256:'+'0'*64;self.rejects('BINDING')
    def test_spec_identity_mismatch(self):
        r=self.plan['releases'][0];r['specification']=self.asset('test.company/spec.yaml',{'metaModel':{'registryId':'wrong.company','version':'1.0.0'}},'application/yaml');self.rejects('SPEC')
    def test_digest_tampering(self):(self.assets/'test.company/AGENTS.md').write_bytes(b'injected');self.rejects('DIGEST')
    def test_path_escape(self):self.plan['releases'][0]['agents']['path']='x/../../escape.md';self.rejects('PATH')
    def test_windows_reserved_name(self):self.plan['releases'][0]['agents']['path']='CON.md';self.rejects('PATH')
    def test_alias_path_collision(self):self.plan['releases'][0]['agents']=copy.deepcopy(self.plan['releases'][0]['specification']);self.rejects('COLLISION')
    def test_untrusted_origin(self):self.plan['releases'][0]['agents']['sourceUrl']='https://evil.test/a';self.rejects('ORIGIN')
    def test_credential_in_source_url(self):self.plan['releases'][0]['agents']['sourceUrl']='https://user:pass@example.test/a';self.rejects('ORIGIN')
    def test_policy_denied(self):self.plan['authority']['decision']='deny';self.rejects('DENIED')
    def test_forged_policy(self):self.plan['authority']['policyDigest']='sha256:'+'0'*64;self.rejects('POLICY-DIGEST')
    def test_undeclared_actor(self):self.plan['authority']['actor']='urn:actor:evil';self.rejects('AUTHORITY')
    def test_other_dimension(self):self.plan['dimensionId']='urn:dimension:other';self.rejects('OWNER')
    def test_stale_lock(self):self.plan['baseLockDigest']='sha256:'+'0'*64;self.rejects('STALE')
    def test_expired_plan(self):self.plan['validUntil']='2026-01-01T00:00:00Z';self.rejects('TIME')
    def test_naive_time(self):self.plan['createdAt']='2026-09-21T00:00:00';self.rejects('SCHEMA')
    def test_same_identity_two_versions(self):
        self.plan['releases'].append(copy.deepcopy(self.plan['releases'][0]));self.plan['releases'][1]['version']='2.0.0';self.rejects('VERSION')
    def test_unknown_dependency(self):self.plan['releases'][0]['requires']=[{'modelId':'test.unit','version':'1.0.0'}];self.rejects('CLOSURE')
    def test_cycle(self):self.plan['releases'][0]['requires']=[{'modelId':'test.company','version':'1.0.0'}];self.rejects('CYCLE')
    def test_extraneous_dependency(self):self.plan['releases'].append(self.release('test.unit'));self.rejects('MINIMAL')
    def test_kernel_domain_import(self):r=self.plan['releases'][0];r['role']='kernel';r['requires']=[{'modelId':'test.unit','version':'1.0.0'}];self.rejects('KERNEL')
    def test_draft_release(self):self.plan['releases'][0]['publicationStatus']='draft';self.rejects('LIFECYCLE')
    def test_unresolved_compatibility(self):self.plan['releases'][0]['compatibility']['decision']='unknown';self.rejects('COMPATIBILITY')
    def test_namespace_collision(self):
        self.plan['releases'].append(self.release('test.unit'));self.plan['releases'][1]['namespace']=self.plan['releases'][0]['namespace'];self.rejects('NAMESPACE')
    def test_revision_without_parent(self):self.plan['revision']=2;self.rejects('REVISION')
    def test_implicit_upgrade_refused(self):
        self.lock_raw=c.encode({'models':[{'id':'test.company','version':'0.9.0','digest':self.plan['releases'][0]['specification']['digest']}]});self.plan['baseLockDigest']=c.digest(self.lock_raw);self.rejects('MIGRATION')
    def test_repeat_staging_is_idempotent(self):
        p,pol,lock=self.files();target=self.root/'staged';first=c.stage(p,self.assets,pol,lock,target);second=c.stage(p,self.assets,pol,lock,target);self.assertTrue(first['changed']);self.assertFalse(second['changed']);self.assertFalse(first['receipt']['nativeRuntimeValidated'])
    def test_existing_target_preserved(self):
        p,pol,lock=self.files();target=self.root/'existing';target.mkdir();(target/'keep').write_text('unchanged');
        with self.assertRaisesRegex(c.Invalid,'TARGET:'):c.stage(p,self.assets,pol,lock,target)
        self.assertEqual((target/'keep').read_text(),'unchanged')
    def test_competing_writer(self):
        p,pol,lock=self.files();(self.root/'.staged.composition-write.lock').mkdir()
        with self.assertRaisesRegex(c.Invalid,'BUSY:'):c.stage(p,self.assets,pol,lock,self.root/'staged')
    def test_failed_commit_leaves_no_target(self):
        p,pol,lock=self.files();target=self.root/'staged'
        with patch.object(c.os,'rename',side_effect=OSError('simulated rename failure')):
            with self.assertRaises(OSError):c.stage(p,self.assets,pol,lock,target)
        self.assertFalse(target.exists());self.assertFalse((self.root/'.staged.composition-write.lock').exists());self.assertFalse(list(self.root.glob('.staged.stage-*')))
    def test_library_historical_write_refused(self):
        p,pol,lock=self.files()
        with self.assertRaisesRegex(c.Invalid,'TIME:'):c.stage(p,self.assets,pol,lock,self.root/'staged',at=self.when)
        self.assertFalse((self.root/'staged').exists())
    def test_same_version_changed_bytes_refused(self):
        self.lock_raw=c.encode({'models':[{'id':'test.company','version':'1.0.0','digest':'sha256:'+'f'*64}]});self.plan['baseLockDigest']=c.digest(self.lock_raw);self.rejects('MIGRATION')
    def test_real_yaml_profile_refused(self):
        self.plan['releases'][0]['specification']=self.asset('test.company/spec.yaml',b'metaModel:\n  registryId: test.company\n  version: 1.0.0\n','application/yaml');self.rejects('SPEC')
    def test_nested_open_object_refused(self):
        self.plan['releases']=[self.release('test.company',True,True)];r=self.plan['releases'][0];s=c.load(self.assets/r['binding']['instanceSchema']['path']);s['properties']['snapshot']={'type':'object'};self.replaceasset(r,'instanceSchema',s);self.rejects('NESTED')
    def test_internal_ref_resolves(self):
        self.plan['releases']=[self.release('test.company',True,True)];r=self.plan['releases'][0];s=c.load(self.assets/r['binding']['instanceSchema']['path']);s['$defs']={'name':s['properties']['name']};s['properties']['name']={'$ref':'#/$defs/name'};self.replaceasset(r,'instanceSchema',s);self.assertTrue(self.runplan()['valid'])
    def test_draft_assurance_not_authorized(self):self.plan['authority']['allowReviewableDrafts']=False;self.rejects('ASSURANCE')
    def test_empty_agents(self):self.plan['releases'][0]['agents']=self.asset('test.company/AGENTS.md',b' \n','text/markdown');self.rejects('AGENTS')
    def test_shared_native_path_refused(self):
        self.plan['releases']=[self.release('test.company',True),self.release('test.unit',True)];r=self.plan['releases'][1];self.plan['roots'].append({'modelId':'test.unit','version':'1.0.0'});s=c.load(self.assets/r['binding']['runtime']['path']);s['paths']={'test.company.snapshot':{'valueTypes':['string'],'units':[None]}};self.replaceasset(r,'runtime',s);self.rejects('FACT-PATH')
    def test_kernel_leaf_allowed(self):self.plan['releases'][0]['role']='kernel';self.assertTrue(self.runplan()['valid'])
    def test_policy_change_before_staging_commit(self):
        p,pol,lock=self.files();original=c.tempfile.mkdtemp
        def mutate(*args,**kwargs):
            out=original(*args,**kwargs);pol.write_bytes(b'{}');return out
        with patch.object(c.tempfile,'mkdtemp',side_effect=mutate):
            with self.assertRaisesRegex(c.Invalid,'STALE:'):c.stage(p,self.assets,pol,lock,self.root/'staged')
        self.assertFalse((self.root/'staged').exists())
    def test_pattern_properties_reopens_root_refused(self):
        self.plan['releases']=[self.release('test.company',True,True)];r=self.plan['releases'][0];s=c.load(self.assets/r['binding']['instanceSchema']['path']);s['patternProperties']={'^':{}};self.replaceasset(r,'instanceSchema',s);self.rejects('NESTED')
    def test_list_typed_open_object_refused(self):
        self.plan['releases']=[self.release('test.company',True,True)];r=self.plan['releases'][0];s=c.load(self.assets/r['binding']['instanceSchema']['path']);s['properties']['snapshot']={'type':['object','null']};self.replaceasset(r,'instanceSchema',s);self.rejects('NESTED')
    def test_expired_policy(self):
        self.policy['validUntil']='2026-01-01T00:00:00Z';self.policy_raw=c.encode(self.policy);self.plan['authority']['policyDigest']=c.digest(self.policy_raw);self.rejects('POLICY')
    def test_unapproved_reviewer(self):self.plan['releases'][0]['compatibility']['reviewer']='urn:reviewer:other';self.rejects('COMPATIBILITY')
    def test_expanded_allowlist(self):self.plan['authority']['allowedModelIds'].append('test.forbidden');self.rejects('AUTHORITY')
    def test_future_provenance(self):self.plan['provenance']['recordedAt']='2100-01-01T00:00:00Z';self.rejects('TIME')
    def test_overlapping_dependency_kinds(self):
        r=self.plan['releases'][0];r['requires']=r['references']=[{'modelId':'test.unit','version':'1.0.0'}];self.rejects('EDGE')
    def test_duplicate_dependency(self):
        self.plan['releases'][0]['requires']=[{'modelId':'test.unit','version':'1.0.0'}]*2;self.rejects('EDGE')
    def test_malformed_lock(self):self.lock_raw=c.encode({'models':['wrong']});self.plan['baseLockDigest']=c.digest(self.lock_raw);self.rejects('LOCK')
    def test_non_object_spec(self):self.plan['releases'][0]['specification']=self.asset('test.company/spec.yaml',[],'application/yaml');self.rejects('SPEC')
    def test_invalid_date(self):self.plan['createdAt']='2026-13-01T00:00:00Z';self.assertRaises(c.Invalid,self.runplan)
    def test_case_insensitive_asset_collision(self):
        r=self.plan['releases'][0];d=copy.deepcopy(r['specification']);d['path']='Test.Company/SPEC.yaml';p=self.assets/d['path'];p.parent.mkdir(exist_ok=True);p.write_bytes((self.assets/r['specification']['path']).read_bytes());r['agents']=d;self.rejects('COLLISION')
    def test_corrupt_staged_plan_refused(self):
        p,pol,lock=self.files();target=self.root/'staged';c.stage(p,self.assets,pol,lock,target);(target/'composition-plan.json').write_bytes(b'{}')
        with self.assertRaisesRegex(c.Invalid,'TARGET:'):c.stage(p,self.assets,pol,lock,target)

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Reference tests require Python without -O')
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(CompositionTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    report={'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'passed':result.wasSuccessful(),'scope':'Offline exact closure, trusted policy, descriptor integrity, readiness, historical correction, idempotency and staged-commit failure. Synthetic assets; native runtime acceptance is a separate test.'}
    (Path(__file__).parent/'test-results.json').write_bytes(c.encode(report))
    raise SystemExit(0 if result.wasSuccessful() else 1)
