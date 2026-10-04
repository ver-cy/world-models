import json
from pathlib import Path
p=Path(__file__).parent
c=json.loads((p/'candidate.json').read_text(encoding='utf-8'))
f=json.loads((p/'fixtures.json').read_text(encoding='utf-8'))
assert c['modelId']=='WM-SFT-010' and c['registryId']=='vr.wm-sft-010'
required={'RuntimeEnvironment','InfrastructureResource','RuntimeOccupantRecord','HostingRelation','ConfigurationItemDesignation','StateAssertion','StatusAssertion','SuccessionRelation','AssetResourceEvidenceLink','CorrectionRecord'}
assert required <= set(c['objects']) and 'DeployedInstance' not in c['objects']
assert len(c['invariants'])>=27 and len(c['relations'])>=4
assert set(c['hostingRelationKinds'])==set(c['hostingEndpointRules'])
assert 'contained-in' in c['hostingRelationKinds']
assert c['objects']['InfrastructureResource']['required'] == ['resourceKind','providerRef']
assert 'parentResourceRef' not in c['objects']['InfrastructureResource'].get('optional',[])
assert all(x['required'] for x in c['relations'] if x['target'] in {'WM-SFT-009','WM-XCT-039'})
assert c['assetEvidenceContract']['carrier']=='AssetResourceEvidenceLink'
assert len(f['cases'])>=28 and all('expectRule' in x for x in f['cases'])
needed={'recycled-runtime-key','conflicting-simultaneous-hosting','cross-environment-hosting','occupant-without-deployment','retired-without-close-time'}
assert needed <= {x['id'] for x in f['cases']}
print(f"candidate-ok: WM-SFT-010, {len(c['invariants'])} invariants, {len(c['relations'])} external boundaries, {len(f['cases'])} fixtures")
