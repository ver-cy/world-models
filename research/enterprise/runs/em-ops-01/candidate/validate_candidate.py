import json
from pathlib import Path
p=Path(__file__).parent
a=json.loads((p/'wm-act-003.candidate.json').read_text(encoding='utf-8'))
b=json.loads((p/'wm-act-009.candidate.json').read_text(encoding='utf-8'))
f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert a['modelId']=='WM-ACT-003' and b['modelId']=='WM-ACT-009'
assert len(a['invariants'])>=12 and len(b['invariants'])>=10
assert 'WorkItem' in a['objects'] and 'StepExecution' in a['objects']
assert 'Edition' in b['objects'] and 'AdoptionRecord' in b['objects']
assert any(r['target']=='WM-ACT-009' for r in a['relations'])
assert len(f['cases'])>=8 and {'positive','negative'} <= {x['kind'] for x in f['cases']}
assert any(x['id']=='retroactive-instruction-update' for x in f['cases'])
print(f"candidate-ok: WM-ACT-003 {len(a['invariants'])} invariants; WM-ACT-009 {len(b['invariants'])} invariants; {len(f['cases'])} fixtures")
