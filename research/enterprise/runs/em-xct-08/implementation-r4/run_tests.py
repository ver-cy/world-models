"""Execute source tests and retain a portable exact-input evidence report."""
import hashlib,json,platform,sqlite3,unittest
from datetime import datetime,timezone
from pathlib import Path
import test_sync
HERE=Path(__file__).resolve().parent
class Results(unittest.TextTestResult):
    def startTest(self,test):
        self.names.append(test.id());super().startTest(test)
    def __init__(self,*args,**kwargs):super().__init__(*args,**kwargs);self.names=[]
if __name__=='__main__':
    result=unittest.TextTestRunner(verbosity=2,resultclass=Results).run(unittest.defaultTestLoader.loadTestsFromModule(test_sync))
    report={'format':'vercy-source-sync-tests','executedAt':datetime.now(timezone.utc).isoformat(),'passed':result.wasSuccessful(),'testsRun':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'tests':result.names,'python':platform.python_version(),'sqlite':sqlite3.sqlite_version,'sourceDigests':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ('run_tests.py','test_sync.py','fault_worker.py','fixtures.py','sync_register.py','sync.schema.json')},'limits':'Synthetic local reference. Two real subprocess crash cuts and a two-process writer race; no hardware/power-loss, remote connector or production-scale certification.'}
    (HERE/'test-results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');raise SystemExit(0 if result.wasSuccessful() else 1)
