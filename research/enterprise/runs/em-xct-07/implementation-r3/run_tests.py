"""Reproducible unit-suite report. --bundle routes ALL component imports to bundle."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,importlib.util,io,json,sqlite3,sys,unittest
HERE=Path(__file__).parent
def run(bundle=False):
    if bundle:
        ms=importlib.util.spec_from_file_location('action_bundle_under_test',HERE/'action_bundle.py'); module=importlib.util.module_from_spec(ms);ms.loader.exec_module(module)
        for name in ('action','history','native'):sys.modules[name]=module
    import test_action
    suite=unittest.defaultTestLoader.loadTestsFromModule(test_action)
    ids=[t.id() for group in suite for t in group]
    output=io.StringIO();result=unittest.TextTestRunner(stream=output,verbosity=2).run(suite)
    files=['action_bundle.py','action.schema.json','action.py','history.py','native.py','fixtures.py','test_action.py','run_tests.py']
    report={'format':'enterprise-action-unit-tests','executedAt':datetime.now(timezone.utc).isoformat(),'mode':'standalone-bundle' if bundle else 'source-modules',
       'python':sys.version.split()[0],'sqlite':sqlite3.sqlite_version,'testsRun':result.testsRun,'failed':len(result.failures),'errors':len(result.errors),'passed':result.wasSuccessful(),'testIds':ids,
       'sourceDigests':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in files},'limits':'Synthetic in-process exceptions and independent SQLite connections; no hardware fault, production authentication or external continuity guarantee.'}
    return report,output.getvalue()
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--bundle',action='store_true');ap.add_argument('--report',required=True);args=ap.parse_args()
    report,log=run(args.bundle);Path(args.report).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8'); print(log);sys.exit(0 if report['passed'] else 1)
