import json
from pathlib import Path
root=Path(__file__).resolve().parent
c=json.loads((root/"candidate.json").read_text(encoding="utf-8"))
f=json.loads((root/"fixtures.json").read_text(encoding="utf-8"))
assert c["modelId"]=="WM-DAT-007" and c["registryId"]=="vr.wm-dat-007"
assert c["canonicalPublishable"] is False and c["entryKind"]=="aggregate"
assert set(c["denominatorStates"])=={"exact","estimated","unknown"}
assert len(c["relations"])==6 and all(x["relation"]=="REFERENCE" for x in c["relations"])
assert len(c["invariants"])>=20
assert set(c["dimensionContracts"])=={"completeness","accuracy","validity","freshness","coverage"}
assert f["modelId"]==c["modelId"] and len(f["fixtures"])>=7
assert len({x["id"] for x in f["fixtures"]})==len(f["fixtures"])
assert c["assessmentKinds"]["coverage"]
assert len(f["fixtures"])>=24
print("candidate-ok: WM-DAT-007, audited reserved candidate, 24 fixtures")
