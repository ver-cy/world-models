import unittest,copy,json,hashlib,sys,platform,argparse,tempfile,importlib.util
from pathlib import Path
from decimal import Decimal,localcontext,ROUND_HALF_EVEN,ROUND_HALF_UP,ROUND_DOWN,ROUND_FLOOR,ROUND_CEILING
from fractions import Fraction
import monetary as m
P=Path(__file__).parent
ORACLE_COMPARISONS=0
GOLDEN_DIGESTS={'startup': 'f124f732774850c00b4a7ceb8dc0936304bba467e3b10d66777f2d0b312652bd', 'matrix': '6e55f11bf2b82d9bb71bc651c438bfcb4592fad0ba1d3bd863f248a1cd248e3a', 'ai': '553ae660182a557094833770ff9f0216f7e3ed653099f0ffa47b99a4a719829a'}
def pin(s):return {'id':'urn:synthetic:'+s,'revision':'1','digest':'sha256:'+hashlib.sha256(s.encode()).hexdigest()}
def fixture(profile='startup'):
    currency={'catalogue':'urn:synthetic:currency-catalogue','edition':'fixture-1','snapshotDigest':pin('currency')['digest'],'code':'EUR','resolution':'host-admitted'}
    context={'basis':pin('estimate-basis'),'valuationAt':'2026-09-21T10:00:00Z','amountRole':'synthetic-estimate'}
    values={'startup':['0.495','0.495','0.495'],'matrix':['-1.025','2.075'],'ai':['1000000000000000.000001','0.000001']}[profile]
    return {'schemaVersion':m.VERSION,'id':'urn:synthetic:receipt:'+profile,'dimension':'urn:synthetic:dimension:'+profile,'subject':'urn:synthetic:estimate:'+profile,'issuer':'urn:synthetic:issuer:'+profile,'computedAt':'2026-09-21T10:01:00Z','purpose':'estimate','inputs':[{'key':'item-'+str(i),'source':pin(profile+'-slot-'+str(i)),'amount':s,'declaredScale':m.scale(s),'currency':copy.deepcopy(currency),'context':copy.deepcopy(context),'state':'exact'} for i,s in enumerate(values)],'policy':{'authority':pin('rounding-authority'),'currency':copy.deepcopy(currency),'increment':'0.01','mode':'half-even','stage':'per-item'},'supersedes':None,'correctionReason':None}
class Tests(unittest.TestCase):
    def setUp(self):self.q=fixture()
    def refused(self,q):
        with self.assertRaises(m.Rejected):m.issue(q)
    def test_line_sum_and_ties(self):
        self.assertEqual(m.issue(self.q)['result']['roundedTotal'],'1.50')
        self.q['policy']['stage']='after-sum';self.assertEqual(m.issue(self.q)['result']['roundedTotal'],'1.48')
        self.q['policy']['mode']='half-away-from-zero';self.assertEqual(m.issue(self.q)['result']['roundedTotal'],'1.49')
    def test_independent_decimal_oracle(self):
        global ORACLE_COMPARISONS
        modes={'half-even':ROUND_HALF_EVEN,'half-away-from-zero':ROUND_HALF_UP,'toward-zero':ROUND_DOWN,'floor':ROUND_FLOOR,'ceiling':ROUND_CEILING}
        for mode,oracle in modes.items():
            for token in ('-2.55','-2.5','-1.025','-0.001','0','0.005','1.025','2.5','2.55','999999999999999999.99999'):
                for inc in ('0.01','0.05','2','0.000001'):
                    q=fixture();q['inputs']=q['inputs'][:1];q['inputs'][0]['amount']=token;q['inputs'][0]['declaredScale']=m.scale(token);q['policy'].update(mode=mode,increment=inc)
                    actual=m.issue(q)['result']['roundedTotal']
                    with localcontext() as ctx:
                        ctx.prec=100;expected=(Decimal(token)/Decimal(inc)).quantize(Decimal('1'),rounding=oracle)*Decimal(inc)
                    self.assertEqual(Fraction(actual),Fraction(expected),(mode,token,inc))
                    self.assertEqual(actual,format(expected,f".{m.scale(inc)}f").lstrip("-") if expected==0 else format(expected,f".{m.scale(inc)}f"))
                    ORACLE_COMPARISONS+=1
    def test_cancelled_residuals_still_inexact(self):
        q=fixture('matrix');q['inputs'][0]['amount']='-0.004';q['inputs'][1]['amount']='0.004'
        for i in q['inputs']:i['declaredScale']=3
        r=m.issue(q)['result'];self.assertEqual(r['residual']['numerator'],'0');self.assertTrue(r['inexact'])
    def test_lexical_roundtrip(self):
        q=self.q;q['inputs'][0].update(amount='0.4950',declaredScale=4);r=m.issue(q)
        self.assertEqual(m.validate(m.load(m.canonical(r))),r);self.assertEqual(r['request']['inputs'][0]['amount'],'0.4950')
    def test_currency_edition_and_basis_refusal(self):
        for key,value in [('code','USD'),('edition','fixture-2'),('catalogue','urn:synthetic:other'),('snapshotDigest',pin('other')['digest'])]:
            q=copy.deepcopy(self.q);q['inputs'][1]['currency'][key]=value;self.refused(q)
        q=copy.deepcopy(self.q);q['inputs'][1]['context']['valuationAt']='2026-09-22T10:00:00Z';self.refused(q)
        q=copy.deepcopy(self.q);q['inputs'][1]['context']['basis']=pin('other');self.refused(q)
    def test_unknown_interval_float_forbidden(self):
        for value in (None,0,0.495,True,'NaN','Infinity','1e2','01.20','+1','1,50','١.٢','-0.00','1.2345678901234567890','9'*37):
            q=copy.deepcopy(self.q);q['inputs'][0]['amount']=value;self.refused(q)
        q=copy.deepcopy(self.q);q['inputs'][0]['state']='unknown';self.refused(q)
    def test_context_and_policy_required(self):
        for key in ('increment','mode','stage','authority','currency'):
            q=copy.deepcopy(self.q);del q['policy'][key];self.refused(q)
        for val in ('0','-0.01'):
            q=copy.deepcopy(self.q);q['policy']['increment']=val;self.refused(q)
    def test_dates_and_scale(self):
        q=copy.deepcopy(self.q);q['computedAt']='2026-02-30T10:00:00Z';self.refused(q)
        q=copy.deepcopy(self.q)
        for x in q['inputs']:x['context']['valuationAt']='2026-02-30T10:00:00Z'
        self.refused(q)
        q=copy.deepcopy(self.q);q['inputs'][0]['declaredScale']=2;self.refused(q)
    def test_duplicate_slots_and_keys(self):
        q=copy.deepcopy(self.q);q['inputs'][1]['source']=q['inputs'][0]['source'];self.refused(q)
        q=copy.deepcopy(self.q);q['inputs'][1]['key']=q['inputs'][0]['key'];self.refused(q)
    def test_replay_and_digest_tamper(self):
        r=m.issue(self.q);r['result']['roundedTotal']='1.49'
        with self.assertRaises(m.Rejected):m.validate(r)
        r['digest']=m.digest({k:v for k,v in r.items() if k!='digest'})
        with self.assertRaises(m.Rejected):m.validate(r)
    def test_immutable_import_and_correction(self):
        r=m.issue(self.q);q=copy.deepcopy(self.q);q['id']+='-correction';q['supersedes']=m.pin(r);q['correctionReason']='Explicit alternate stage';q['policy']['stage']='after-sum';n=m.issue(q)
        opts={'dimension':q['dimension'],'admitted_existing_issuers':{q['issuer']},'admitted_incoming_issuers':{q['issuer']}}
        records=m.import_receipts([],[r,n],**opts);self.assertEqual(m.import_receipts(records,[n],**opts),records);self.assertEqual(records[0],r)
        fork=copy.deepcopy(self.q);fork['policy']['stage']='after-sum'
        with self.assertRaises(m.Rejected):m.import_receipts(records,[m.issue(fork)],**opts)
        with self.assertRaises(m.Rejected):m.import_receipts([],[n],**opts)
    def test_wrong_dimension_issuer(self):
        r=m.issue(self.q)
        for dimension,issuers in [('urn:wrong',{self.q['issuer']}),(self.q['dimension'],set())]:
            with self.assertRaises(m.Rejected):m.import_receipts([],[r],dimension=dimension,admitted_existing_issuers=issuers,admitted_incoming_issuers=issuers)
    def test_correction_reason_and_identity(self):
        q=copy.deepcopy(self.q);q['correctionReason']='spurious';self.refused(q)
        q=copy.deepcopy(self.q);q['supersedes']={'id':q['id'],'digest':pin('wrong')['digest']};q['correctionReason']='self';self.refused(q)
    def test_new_version_refused(self):
        q=copy.deepcopy(self.q);q['schemaVersion']='0.2.0';self.refused(q)
    def test_json_and_unknown_fields(self):
        for raw in ('{"a":1,"a":2}','{"a":NaN}'):
            with self.assertRaises(m.Rejected):m.load(raw)
        q=copy.deepcopy(self.q);q['executePayment']=True;self.refused(q)
        q=copy.deepcopy(self.q);q['inputs'][0]['currency']['minorUnit']=2;self.refused(q)
    def test_boundaries(self):
        q=copy.deepcopy(self.q);q['inputs']=[copy.deepcopy(q['inputs'][0]) for _ in range(256)]
        for i,x in enumerate(q['inputs']):x['key']='i'+str(i);x['source']=pin('slot-'+str(i));x['amount']='9'*36;x['declaredScale']=0
        q['policy']['increment']='0.000000000000000001';r=m.issue(q);self.assertEqual(Fraction(r['result']['roundedTotal']),Fraction('9'*36)*256);self.assertEqual(len(r['result']['roundedTotal'].replace('.','')),57)
        q['inputs'].append(copy.deepcopy(q['inputs'][0]));self.refused(q)
    def test_no_input_mutation(self):
        old=copy.deepcopy(self.q);m.issue(self.q);self.assertEqual(old,self.q)
    def test_three_profiles(self):
        for name in ('startup','matrix','ai'):self.assertEqual(m.validate(m.issue(fixture(name))),m.issue(fixture(name)))
    def test_strict_grammar_aliases(self):
        paths=[('id',),('inputs',0,'source','id'),('inputs',0,'source','digest'),('inputs',0,'key'),('inputs',0,'currency','code')]
        for path in paths:
            q=copy.deepcopy(self.q);cursor=q
            for key in path[:-1]:cursor=cursor[key]
            cursor[path[-1]]+='\n';self.refused(q)
        q=copy.deepcopy(self.q);q['computedAt']='٢٠٢٦-09-21T10:01:00Z';self.refused(q)
    def test_historical_issuer_does_not_authorize_new(self):
        first=m.issue(self.q);q=copy.deepcopy(self.q);q['id']+='-new';new=m.issue(q)
        opts={'dimension':q['dimension'],'admitted_existing_issuers':{q['issuer']},'admitted_incoming_issuers':set()}
        self.assertEqual(m.import_receipts([first],[],**opts),[first])
        with self.assertRaisesRegex(m.Rejected,'issuer-not-admitted'):m.import_receipts([first],[new],**opts)
        with self.assertRaisesRegex(m.Rejected,'issuer-not-admitted'):m.import_receipts([first],[first],**opts)
    def test_correction_branches_and_guards(self):
        old=m.issue(self.q);q=copy.deepcopy(self.q);q.update(id=q['id']+'-b',supersedes=m.pin(old),correctionReason='Correction')
        first=m.issue(q);q['id']+='-branch';second=m.issue(q)
        opts={'dimension':q['dimension'],'admitted_existing_issuers':{q['issuer'],'urn:synthetic:other'},'admitted_incoming_issuers':{q['issuer'],'urn:synthetic:other'}}
        self.assertEqual(len(m.import_receipts([],[old,first,second],**opts)),3)
        for field,value in [('issuer','urn:synthetic:other'),('subject','urn:synthetic:other'),('computedAt','2026-09-21T09:00:00Z')]:
            changed=copy.deepcopy(q);changed[field]=value
            with self.assertRaises(m.Rejected):m.import_receipts([],[old,m.issue(changed)],**opts)
    def test_transitive_missing_pin_typed_refusal(self):
        q=copy.deepcopy(self.q);q['id']+='-b';q['supersedes']={'id':'urn:synthetic:absent','digest':pin('absent')['digest']};q['correctionReason']='Missing predecessor';b=m.issue(q)
        q['id']+='-a';q['supersedes']=m.pin(b);a=m.issue(q)
        with self.assertRaisesRegex(m.Rejected,'supersedes-unresolved'):m.import_receipts([],[a,b],dimension=q['dimension'],admitted_existing_issuers={q['issuer']},admitted_incoming_issuers={q['issuer']})
    def test_golden_examples(self):
        for name in ('startup','matrix','ai'):
            raw=(P/'examples'/f'{name}.json').read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(),GOLDEN_DIGESTS[name])
            self.assertEqual(raw,m.canonical(m.issue(fixture(name)))+b'\n')
            saved=m.load(raw);self.assertEqual(m.validate(saved),saved)
    def test_utf8_wire_only(self):
        for raw in (b'\xef\xbb\xbf{}','{}'.encode('utf-16'),'\ud800'):
            with self.assertRaises(m.Rejected):m.load(raw)
    def test_full_register_replay_and_new_capacity(self):
        full=[]
        for i in range(256):
            q=copy.deepcopy(self.q);q['id']='urn:synthetic:full:'+str(i);full.append(m.issue(q))
        opts={'dimension':self.q['dimension'],'admitted_existing_issuers':{self.q['issuer']},'admitted_incoming_issuers':{self.q['issuer']}}
        self.assertEqual(m.import_receipts(full,[full[0]],**opts),full)
        with self.assertRaisesRegex(m.Rejected,'register-bound'):m.import_receipts(full,[m.issue(self.q)],**opts)
    def test_minor_stage_context_and_pin_edges(self):
        q=copy.deepcopy(self.q);q['inputs'][1]['context']['amountRole']='other';self.refused(q)
        for mode,expected in [('floor','1.47'),('ceiling','1.50'),('toward-zero','1.47')]:
            q=copy.deepcopy(self.q);q['policy']['mode']=mode;self.assertEqual(m.issue(q)['result']['roundedTotal'],expected)
        q=copy.deepcopy(self.q);q['policy']['increment']='0.10';a=m.issue(q);q['policy']['increment']='0.1';b=m.issue(q)
        self.assertEqual(Fraction(a['result']['roundedTotal']),Fraction(b['result']['roundedTotal']));self.assertNotEqual(a['result']['roundedTotal'],b['result']['roundedTotal'])
        old=m.issue(self.q);q['id']+='-corrected';q['supersedes']={'id':old['request']['id'],'digest':pin('wrong')['digest']};q['correctionReason']='Bad digest'
        with self.assertRaisesRegex(m.Rejected,'supersedes-unresolved'):m.import_receipts([old],[m.issue(q)],dimension=q['dimension'],admitted_existing_issuers={q['issuer']},admitted_incoming_issuers={q['issuer']})
    def test_schema_integrity(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);(root/'monetary.py').write_bytes((P/'monetary.py').read_bytes())
            schema=copy.deepcopy(m.SCHEMA);schema['$defs']['Request']['additionalProperties']=True
            (root/'monetary.schema.json').write_bytes(m.canonical(schema))
            spec=importlib.util.spec_from_file_location('tampered_money',root/'monetary.py');module=importlib.util.module_from_spec(spec)
            with self.assertRaisesRegex(ValueError,'^schema-integrity$'):spec.loader.exec_module(module)
    def test_load_typed_errors(self):
        for raw,code in [('{"x":1,"x":2}','duplicate-json-key'),('{"x":NaN}','nonfinite-json'),('{','invalid-wire-json')]:
            with self.assertRaisesRegex(m.Rejected,'^'+code+'$'):m.load(raw)
    def test_native_host_types_and_envelopes(self):
        from acceptance import native_pair,MASTER,WRITER
        r=m.issue(self.q);obj,fact=native_pair(r,'2026-09-21T10:03:00Z')
        opts=dict(dimension=self.q['dimension'],master=MASTER,writer=WRITER,allowed_issuers={self.q['issuer']})
        self.assertEqual(m.validate_native(fact,obj,**opts),r)
        for bad in (self.q['issuer']+'-admin',[self.q['issuer']],None,{1}):
            altered=dict(opts,allowed_issuers=bad)
            with self.assertRaisesRegex(m.Rejected,'^host-issuer-set$'):m.validate_native(fact,obj,**altered)
        self.assertEqual(m.validate_native(fact,obj,**dict(opts,allowed_issuers=frozenset(opts['allowed_issuers']))),r)
        for key in ('dimension','master','writer'):
            for bad in ('',None,4):
                with self.assertRaisesRegex(m.Rejected,'^host-string$'):m.validate_native(fact,obj,**dict(opts,**{key:bad}))
        for target in ('fact','object'):
            for field,value,code in [('schemaVersion','2.0.0','native-version'),('provenance',None,'native-provenance'),('provenance','invalid','native-provenance')]:
                ob,f=copy.deepcopy(obj),copy.deepcopy(fact);(f if target=='fact' else ob)[field]=value
                with self.assertRaisesRegex(m.Rejected,'^'+code+'$'):m.validate_native(f,ob,**opts)
    def test_multi_input_oracle(self):
        global ORACLE_COMPARISONS
        for stage in ('per-item','after-sum'):
            q=fixture('matrix');q['policy'].update(increment='0.01',mode='half-even',stage=stage)
            with localcontext() as ctx:
                ctx.prec=100;values=[Decimal(i['amount']) for i in q['inputs']]
                expected=sum(v.quantize(Decimal('0.01'),rounding=ROUND_HALF_EVEN) for v in values) if stage=='per-item' else sum(values).quantize(Decimal('0.01'),rounding=ROUND_HALF_EVEN)
            self.assertEqual(m.issue(q)['result']['roundedTotal'],format(expected,'.2f'));ORACLE_COMPARISONS+=1
    def test_whitespace_reason(self):
        q=copy.deepcopy(self.q);q.update(id=q['id']+'-new',supersedes=m.pin(m.issue(self.q)),correctionReason='   ')
        with self.assertRaisesRegex(m.Rejected,'^correction-reason$'):m.issue(q)
    def test_partition_cannot_prove_global_uniqueness(self):
        a=m.issue(self.q);q=copy.deepcopy(self.q);q['policy']['stage']='after-sum';b=m.issue(q)
        opts=dict(dimension=q['dimension'],admitted_existing_issuers={q['issuer']},admitted_incoming_issuers={q['issuer']})
        self.assertEqual(m.import_receipts([],[a],**opts),[a]);self.assertEqual(m.import_receipts([],[b],**opts),[b])
        with self.assertRaisesRegex(m.Rejected,'^immutable-identity-conflict$'):m.import_receipts([a],[b],**opts)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--report',help='Optional explicit report output; tests never regenerate examples');a=ap.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests);r=unittest.TextTestRunner(verbosity=1).run(suite)
    report={'passed':r.wasSuccessful(),'testsRun':r.testsRun,'failures':len(r.failures),'errors':len(r.errors),'oracleCases':ORACLE_COMPARISONS,'python':platform.python_version(),'scope':'Local exact arithmetic, immutable merge, typed errors and synthetic scenarios; no external resolution or permissions. Golden examples are immutable and verified by exact bytes and digest.','files':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ('monetary.py','monetary.schema.json','test_monetary.py')}}
    if a.report:Path(a.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    sys.exit(not r.wasSuccessful())
