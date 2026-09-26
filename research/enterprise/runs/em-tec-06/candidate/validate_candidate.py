import json
from pathlib import Path
p=Path(__file__).parent
c=json.loads((p/'candidate.json').read_text(encoding='utf-8'))
f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert c['modelId']=='WM-SFT-016' and c['registryId']=='vr.wm-sft-016'
assert {'SLISpecification','SLOPolicy','SLOEvaluation','ErrorBudgetPolicy','ObservabilityBinding'} <= set(c['objects'])
assert len(c['invariants'])>=12 and len(c['relations'])>=4
assert {'met','not-met','unknown-insufficient-coverage','no-eligible-traffic','indeterminate'}==set(c['verdictVocabulary'])
assert len(f['cases'])>=7 and {'positive','negative'} <= {x['kind'] for x in f['cases']}
assert any(x['id']=='three-service-journey-gap' for x in f['cases'])
print(f"candidate-ok: WM-SFT-016, {len(c['invariants'])} invariants, {len(c['relations'])} external boundaries, {len(f['cases'])} fixtures")
