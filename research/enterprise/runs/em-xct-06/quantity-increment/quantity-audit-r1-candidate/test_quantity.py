import copy,json,hashlib,unittest,sys,argparse
from pathlib import Path
from fractions import Fraction
from decimal import Decimal,localcontext
import quantity as q
HERE=Path(__file__).parent
def pin(name,rev='1'):
    return {'uri':'urn:synthetic:'+name,'revision':rev,'sha256':hashlib.sha256((name+'@'+rev).encode()).hexdigest()}
def unit(code,kind,dim,a=(1,1),b=(0,1),roles=('scalar',),rev='1'):
    return {'reference':pin('unit:'+code,rev),'code':code,'kind':pin('kind:'+kind),'dimension':dim,'anchor':pin('anchor:'+kind),'roles':list(roles),'formula':'anchor=a*x+b','exactness':'definition-exact','a':{'n':str(a[0]),'d':str(a[1])},'b':{'n':str(b[0]),'d':str(b[1])},'authority':pin('definition-policy:'+code,rev)}
def fixture(name):
    if name=='startup':u=unit('h','service-duration',[0,0,1,0,0,0,0],(3600,1));t=unit('min','service-duration',[0,0,1,0,0,0,0],(60,1));lex='1.250';role='scalar'
    elif name=='matrix':u=unit('km','route-length',[1,0,0,0,0,0,0],(1000,1));t=unit('m','route-length',[1,0,0,0,0,0,0]);lex='12.50';role='scalar'
    else:u=unit('[degF]','temperature',[0,0,0,0,1,0,0],(5,9),(45967,180),('point','difference'));t=unit('Cel','temperature',[0,0,0,0,1,0,0],(1,1),(5463,20),('point','difference'));lex='32.0';role='point'
    value={'unit':u,'role':role,'context':pin('context:'+name),'source':pin('source:'+name),'magnitude':{'state':'known','lexical':lex,'scale':len(lex.split('.')[1]),'precisionMeaning':'reported-digits'}}
    admitted={'definitions':{q.digest(u),q.digest(t)},'contexts':{q.digest(value['context'])},'sources':{q.digest(value['source'])}}
    return value,t,admitted
def document(value):return {'format':'vercy-embedded-quantity','version':'0.1.0','quantity':value}
class Cases(unittest.TestCase):
    def setUp(self):self.v,self.t,self.a=fixture('ai')
    def reject(self,reason,fn,*args,**kw):
        with self.assertRaises(q.Rejected) as c:fn(*args,**kw)
        self.assertEqual(str(c.exception),reason)
    def check(self):return q.validate(document(self.v),admitted=self.a)
    def test_three_golden_examples(self):
        for n,want in [('startup',{'n':'75','d':'1'}),('matrix',{'n':'12500','d':'1'}),('ai',{'n':'0','d':'1'})]:
            v,t,a=fixture(n);got=q.convert(v,t,admitted=a);self.assertEqual(got['result'],want);self.assertEqual(got['quantity'],v)
    def test_signed_zero_preserved(self):
        self.v['magnitude'].update(lexical='-0.00',scale=2);self.assertEqual(self.check()['quantity']['magnitude']['lexical'],'-0.00');self.v['role']='difference';self.assertEqual(q.convert(self.v,self.t,admitted=self.a)['result'],{'n':'0','d':'1'})
    def test_unknown_not_zero(self):
        self.v['magnitude']={'state':'unknown','reason':'Not measured'};self.check();self.reject('non-numeric',q.convert,self.v,self.t,admitted=self.a)
    def test_other_absence_states(self):
        for state in ['withheld','not-applicable']:
            self.v['magnitude']={'state':state,'reason':'Host decision'};self.check()
    def test_missing_unit_not_one(self):
        del self.v['unit'];self.reject('schema',self.check)
    def test_explicit_unit_one(self):
        self.v['unit']=unit('1','count-of-tests',[0]*7);self.v['role']='scalar';self.a['definitions'].add(q.digest(self.v['unit']));self.check()
    def test_missing_kind(self):
        del self.v['unit']['kind'];self.reject('schema',self.check)
    def test_same_dimension_wrong_kind(self):
        self.t['kind']=pin('kind:unrelated');self.a['definitions'].add(q.digest(self.t));self.reject('kind-mismatch',q.convert,self.v,self.t,admitted=self.a)
    def test_energy_torque_not_equivalent(self):
        v,t,a=fixture('matrix');v['unit']=unit('J','energy',[2,1,-2,0,0,0,0]);t=unit('N.m','torque',[2,1,-2,0,0,0,0]);a['definitions']={q.digest(v['unit']),q.digest(t)};self.reject('kind-mismatch',q.convert,v,t,admitted=a)
    def test_dimension_mismatch(self):
        self.t['dimension'][0]=1;self.a['definitions'].add(q.digest(self.t));self.reject('dimension-mismatch',q.convert,self.v,self.t,admitted=self.a)
    def test_anchor_mismatch(self):
        self.t['anchor']=pin('anchor:other');self.a['definitions'].add(q.digest(self.t));self.reject('anchor-mismatch',q.convert,self.v,self.t,admitted=self.a)
    def test_source_revision_drift(self):
        self.v['source']['revision']='2';self.reject('source-not-admitted',self.check)
    def test_definition_revision_drift(self):
        self.v['unit']['reference']['revision']='2';self.reject('definition-not-admitted',self.check)
    def test_admitted_exact_revision_change(self):
        self.v['unit']['reference']['revision']='2';self.a['definitions'].add(q.digest(self.v['unit']));self.check()
    def test_context_not_admitted(self):
        self.a['contexts']=set();self.reject('context-not-admitted',self.check)
    def test_admission_not_string_list(self):
        for invalid in [next(iter(self.a['sources'])),list(self.a['sources']),None]:
            a=copy.deepcopy(self.a);a['sources']=invalid;self.reject('admission-set',q.validate,document(self.v),admitted=a)
    def test_float(self):
        self.v['magnitude']['lexical']=1.25;self.reject('unsupported-number-or-type',self.check)
    def test_decimal_bounds(self):
        self.v['magnitude'].update(lexical='9'*37,scale=0);self.reject('decimal-bounds',self.check)
    def test_scale(self):
        self.v['magnitude']['scale']=0;self.reject('scale',self.check)
    def test_decimal_lexical(self):
        for s in ['+1','01','1e2','1,00','1.','NaN',' 1']:
            self.v['magnitude']['lexical']=s;self.reject('schema',self.check)
    def test_control_unicode(self):
        for s in ['1\n','\u0661','1\u202e']:
            self.v['magnitude']['lexical']=s;self.reject('ascii-string',self.check)
    def test_versions_unknown_fields(self):
        d=document(self.v);d['version']='0.2.0';self.reject('schema',q.validate,d,admitted=self.a);d['version']='0.1.0';d['id']='second-identity';self.reject('schema',q.validate,d,admitted=self.a)
    def test_nonlinear_and_approximate(self):
        for key,val in [('formula','log(x)'),('exactness','approximate')]:
            v=copy.deepcopy(self.v);v['unit'][key]=val;self.reject('schema',q.validate,document(v),admitted=self.a)
    def test_bad_factors(self):
        for a,reason in [({'n':'0','d':'1'},'positive-factor'),({'n':'-1','d':'1'},'positive-factor'),({'n':'2','d':'4'},'noncanonical-rational'),({'n':'1','d':'0'},'schema')]:
            v=copy.deepcopy(self.v);v['unit']['a']=a;self.reject(reason,q.validate,document(v),admitted=self.a)
    def test_wrong_qudt_offset_mapping_unadmitted(self):
        self.v['unit']['b']={'n':'45967','d':'100'};self.reject('definition-not-admitted',self.check)
    def test_finite_factor_not_silently_exact(self):
        # This is an external-policy refusal, not inference that any rational is physically wrong.
        self.v['unit']['a']={'n':'1388888888888888888888888888888889','d':'2500000000000000000000000000000000'};self.reject('definition-not-admitted',self.check)
    def test_difference_suppresses_offsets(self):
        self.v['role']='difference';self.v['magnitude'].update(lexical='18.0',scale=1);self.assertEqual(q.convert(self.v,self.t,admitted=self.a)['result'],{'n':'10','d':'1'})
    def test_scalar_with_offset(self):
        self.v['unit']['roles']=['scalar'];self.v['role']='scalar';self.reject('scalar-offset',self.check)
    def test_role_not_admitted(self):
        self.v['role']='scalar';self.reject('role-not-admitted',self.check)
    def test_target_role(self):
        self.t['roles']=['difference'];self.a['definitions'].add(q.digest(self.t));self.reject('target-role',q.convert,self.v,self.t,admitted=self.a)
    def test_comparison(self):
        other=copy.deepcopy(self.v);other['unit']=self.t;other['magnitude'].update(lexical='0.0',scale=1);self.assertEqual(q.compare(self.v,other,admitted=self.a),0)
        other['magnitude']['lexical']='1.0';self.assertEqual(q.compare(self.v,other,admitted=self.a),-1)
    def test_comparison_context_role(self):
        other=copy.deepcopy(self.v);other['context']=pin('context:other');self.a['contexts'].add(q.digest(other['context']));self.reject('context-mismatch',q.compare,self.v,other,admitted=self.a)
        other=copy.deepcopy(self.v);other['role']='difference';self.reject('role-mismatch',q.compare,self.v,other,admitted=self.a)
    def test_tampered_result(self):
        d=q.convert(self.v,self.t,admitted=self.a);d['result']['n']='1';self.reject('replay-mismatch',q.validate,d,admitted=self.a)
    def test_load_roundtrip_and_repeat(self):
        d=q.convert(self.v,self.t,admitted=self.a);raw=q.canonical(d);self.assertEqual(q.canonical(q.validate(q.load(raw),admitted=self.a)),raw);self.assertEqual(q.validate(d,admitted=self.a),q.validate(d,admitted=self.a))
    def test_wire(self):
        for raw,reason in [(b'{"a":1,"a":2}','duplicate-key'),(b'1e999','wire-float'),(b'NaN','wire-float'),(b'100000','wire-integer'),(b' '*262145,'wire-bytes')]:self.reject(reason,q.load,raw)
    def test_canonical_known_vectors(self):
        self.assertEqual(q.canonical({'z':True,'a':'"\\','n':None,'i':-2}),b'{"a":"\\"\\\\","i":-2,"n":null,"z":true}')
        self.assertEqual(q.digest({}),hashlib.sha256(b'{}').hexdigest())
    def test_resource_depth(self):
        d=0
        for i in range(26):d=[d]
        self.reject('depth',q.canonical,d)
    def test_numeric_oracle(self):
        # Decimal separately evaluates UCUM's pre-offset formula, not production normal form.
        with localcontext() as ctx:
            ctx.prec=120
            for i in range(-100,101):
                v,t,a=fixture('ai');v['magnitude'].update(lexical=str(i),scale=0);got=q.rational(q.convert(v,t,admitted=a)['result'])
                oracle=(Decimal(i)+Decimal('459.67'))*Decimal(5)/Decimal(9)-Decimal('273.15')
                self.assertLess(abs(Decimal(got.numerator)/Decimal(got.denominator)-oracle),Decimal('1e-110'))
    def test_dimension_integer_only(self):
        self.v['unit']['dimension'][0]='1/2';self.reject('schema',self.check)
    def test_preserve_source_copy(self):
        got=q.convert(self.v,self.t,admitted=self.a);got['quantity']['magnitude']['lexical']='3';self.assertEqual(self.v['magnitude']['lexical'],'32.0')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--report',required=True);a=ap.parse_args();suite=unittest.defaultTestLoader.loadTestsFromTestCase(Cases);r=unittest.TextTestRunner(verbosity=1).run(suite)
    report={'passed':r.wasSuccessful(),'testsRun':r.testsRun,'oracleCases':201,'oracle':'Independent Decimal pre-offset Fahrenheit formula, 120-digit arithmetic; comparison tolerance 1e-110. Not physical measurement verification.','python':sys.version.split()[0],'sourceDigests':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ['quantity.py','quantity.schema.json','test_quantity.py']}}
    Path(a.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');sys.exit(0 if r.wasSuccessful() else 1)
