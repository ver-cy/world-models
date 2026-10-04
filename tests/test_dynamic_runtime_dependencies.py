import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT=Path(__file__).resolve().parents[1]/'tools/site/build_runtime_index.py'

class RuntimeDependencies(unittest.TestCase):
    def test_required_dependencies_are_enforced(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); models=root/'models'; models.mkdir()
            (root/'tools/server').mkdir(parents=True)
            def write(path,value): path.write_text(json.dumps(value),encoding='utf-8')
            rows=[]
            for name in ('base','aggregate'):
                folder=models/name;folder.mkdir()
                (folder/'AGENTS.md').write_text('Instructions',encoding='utf-8')
                write(folder/'spec.yaml',{'composition':[{'target':'vr.base','required':True}] if name=='aggregate' else []})
                write(folder/'publication.json',{'runtime_requires':['vr.base'] if name=='aggregate' else []})
                rows.append({'registry_id':'vr.'+name,'model_id':name,'name':name,'code':name,'page_url':'/models/'+name+'/','status':'published','spec_available':True,'version':'1.0.0'})
            write(models/'catalog-index.json',[]);write(models/'composer-index.json',{'models':[]})
            write(root/'tools/server/vercy-catalog-import.json',{'models':rows})
            spec=importlib.util.spec_from_file_location('runtime_test',SCRIPT)
            module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
            module.ROOT=root;module.MODELS=models
            module.main()
            result={m['id']:m for m in json.loads((models/'runtime-index.json').read_text())['models']}
            self.assertEqual(result['vr.aggregate']['requires'],['vr.base'])
            self.assertTrue(result['vr.aggregate']['installable'])
            rows[0]['status']='todo'
            write(root/'tools/server/vercy-catalog-import.json',{'models':rows})
            module.main()
            result={m['id']:m for m in json.loads((models/'runtime-index.json').read_text())['models']}
            self.assertFalse(result['vr.aggregate']['installable'])
            write(models/'aggregate/publication.json',{'runtime_requires':[]})
            with self.assertRaisesRegex(ValueError,'dependency mismatch'):
                module.main()

if __name__=='__main__': unittest.main()
