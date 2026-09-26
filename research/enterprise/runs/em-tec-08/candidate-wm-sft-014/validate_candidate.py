import json,hashlib
from pathlib import Path
p=Path(__file__).parent
c=json.loads((p/'candidate.json').read_text(encoding='utf-8'))
f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
s=json.loads((p/'source-spec.json').read_text(encoding='utf-8'))
assert c['modelId']=='WM-SFT-014' and c['registryId']=='vr.wm-sft-014'
assert c['sourceSpecSha256']==hashlib.sha256((p/'source-spec.json').read_bytes()).hexdigest()
assert s['metaModel']['id']=='WM-SFT-014' and s['statistics']['sources']>=16
assert {'Defect','AffectedScopeAssertion','SeverityAssertion','ResolutionAssertion','VerificationAssertion'} <= set(c['objects'])
assert len(c['invariants'])>=12 and len(c['relations'])>=5
assert all(x['relation']=='REFERENCE' for x in c['relations'])
assert len(f['cases'])>=7 and {'positive','negative'} <= {x['kind'] for x in f['cases']}
assert any(x['id']=='same-build-green' for x in f['cases'])
print(f"candidate-ok: WM-SFT-014, {len(c['invariants'])} invariants, {len(c['relations'])} external boundaries, {len(f['cases'])} fixtures, {s['statistics']['sources']} frozen sources")
