import unittest,copy,json,hashlib,sys,platform
from pathlib import Path
from decimal import Decimal,localcontext,ROUND_HALF_EVEN,ROUND_HALF_UP,ROUND_DOWN,ROUND_FLOOR,ROUND_CEILING
from fractions import Fraction
import monetary as m
P=Path(__file__).parent
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
        modes={'half-even':ROUND_HALF_EVEN,'half-away-from-zero':ROUND_HALF_UP,'toward-zero':ROUND_DOWN,'floor':ROUND_FLOOR,'ceiling':ROUND_CEILING}
        for mode,oracle in modes.items():
            for token in ('-2.55','-2.5','-1.025','-0.001','0','0.005','1.025','2.5','2.55','999999999999999999.99999'):
                for inc in ('0.01','0.05','2','0.000001'):
                    q=fixture();q['inputs']=q['inputs'][:1];q['inputs'][0]['amount']=token;q['inputs'][0]['declaredScale']=m.scale(token);q['policy'].update(mode=mode,increment=inc)
                    actual=m.issue(q)['result']['roundedTotal']
                    with localcontext() as ctx:
                        ctx.prec=100;expected=(Decimal(token)/Decimal(inc)).quantize(Decimal('1'),rounding=oracle)*Decimal(inc)
                    self.assertEqual(Fraction(actual),Fraction(expected),(mode,token,inc))
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
        opts={'dimension':q['dimension'],'allowed_issuers':{q['issuer']}}
        records=m.import_receipts([],[r,n],**opts);self.assertEqual(m.import_receipts(records,[n],**opts),records);self.assertEqual(records[0],r)
        fork=copy.deepcopy(self.q);fork['policy']['stage']='after-sum'
        with self.assertRaises(m.Rejected):m.import_receipts(records,[m.issue(fork)],**opts)
        with self.assertRaises(m.Rejected):m.import_receipts([],[n],**opts)
    def test_wrong_dimension_issuer(self):
        r=m.issue(self.q)
        for dimension,issuers in [('urn:wrong',{self.q['issuer']}),(self.q['dimension'],set())]:
            with self.assertRaises(m.Rejected):m.import_receipts([],[r],dimension=dimension,allowed_issuers=issuers)
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
        r=m.issue(q);self.assertEqual(Fraction(r['result']['roundedTotal']),Fraction('9'*36)*256)
        q['inputs'].append(copy.deepcopy(q['inputs'][0]));self.refused(q)
    def test_no_input_mutation(self):
        old=copy.deepcopy(self.q);m.issue(self.q);self.assertEqual(old,self.q)
    def test_three_profiles(self):
        for name in ('startup','matrix','ai'):self.assertEqual(m.validate(m.issue(fixture(name))),m.issue(fixture(name)))
if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests);r=unittest.TextTestRunner(verbosity=1).run(suite)
    (P/'examples').mkdir(exist_ok=True)
    for name in ('startup','matrix','ai'):(P/'examples'/f'{name}.json').write_bytes(m.canonical(m.issue(fixture(name)))+b'\n')
    report={'passed':r.wasSuccessful(),'testsRun':r.testsRun,'failures':len(r.failures),'errors':len(r.errors),'oracleCases':200,'python':platform.python_version(),'scope':'Local exact arithmetic, immutable merge, errors and synthetic scenarios; no external resolution or permissions.','files':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ('monetary.py','monetary.schema.json','test_monetary.py')}}
    (P/'test-results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');sys.exit(not r.wasSuccessful())
