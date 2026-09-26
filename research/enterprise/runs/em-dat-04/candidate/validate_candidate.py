import json
from pathlib import Path
root=Path(__file__).resolve().parent
c=json.loads((root/"candidate.json").read_text(encoding="utf-8"))
f=json.loads((root/"fixtures.json").read_text(encoding="utf-8"))
assert c["modelId"]=="WM-DAT-007" and c["registryId"]=="vr.wm-dat-007"
assert c["canonicalPublishable"] is False and c["entryKind"]=="aggregate"
assert set(c["denominatorStates"])=={"known-exact","estimated","unknown"}
assert len(c["relations"])==6 and all(x["relation"]=="REFERENCE" for x in c["relations"])
assert len(c["invariants"])>=14
assert set(c["dimensionContracts"])=={"completeness","accuracy","validity","freshness","coverage"}
assert f["modelId"]==c["modelId"] and len(f["fixtures"])>=7
assert len({x["id"] for x in f["fixtures"]})==len(f["fixtures"])
print("candidate-ok: WM-DAT-007, 14 invariants, 6 external boundaries, 7 fixtures")
