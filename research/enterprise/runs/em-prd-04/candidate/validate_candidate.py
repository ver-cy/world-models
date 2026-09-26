import json
from pathlib import Path
p=Path(__file__).parent
c=json.loads((p/'candidate.json').read_text(encoding='utf-8'))
f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert c['modelId']=='WM-ACT-022' and c['registryId']=='vr.wm-act-022'
assert {'ExperimentRun','RunManifest','ExperimentAttempt','RunDeviation'} <= set(c['objects'])
assert len(c['invariants'])>=12 and len(c['relations'])>=6
assert len(f['cases'])>=7 and {'positive','negative'} <= {x['kind'] for x in f['cases']}
assert any(x['id']=='contradictory-runs' for x in f['cases'])
assert any(x['id']=='delete-failed-run' for x in f['cases'])
print(f"candidate-ok: WM-ACT-022, {len(c['invariants'])} invariants, {len(c['relations'])} external boundaries, {len(f['cases'])} fixtures")
