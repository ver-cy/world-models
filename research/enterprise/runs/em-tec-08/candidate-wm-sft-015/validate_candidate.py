import json,hashlib
from pathlib import Path
p=Path(__file__).parent
c=json.loads((p/'candidate.json').read_text(encoding='utf-8'))
f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
s=json.loads((p/'source-spec.json').read_text(encoding='utf-8'))
assert c['modelId']=='WM-SFT-015' and c['registryId']=='vr.wm-sft-015'
assert c['sourceSpecSha256']==hashlib.sha256((p/'source-spec.json').read_bytes()).hexdigest()
assert s['metaModel']['id']=='WM-SFT-015' and s['statistics']['sources']>=33
assert {'TestCaseDefinition','TestExecution','ObservedOutcome','ResultAdjudication','EvidenceManifest'} <= set(c['objects'])
assert set(c['verdicts'])=={'passed','failed','inconclusive','blocked','not-executed'}
assert len(c['invariants'])>=12 and len(c['relations'])>=5 and len(f['cases'])>=7
assert {'positive','negative'} <= {x['kind'] for x in f['cases']}
print(f"candidate-ok: WM-SFT-015, {len(c['invariants'])} invariants, {len(c['relations'])} external boundaries, {len(f['cases'])} fixtures, {s['statistics']['sources']} frozen sources")
