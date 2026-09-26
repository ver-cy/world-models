import json
from pathlib import Path
root=Path(__file__).resolve().parent
c=json.loads((root/"candidate.json").read_text(encoding="utf-8"))
f=json.loads((root/"fixtures.json").read_text(encoding="utf-8"))
assert c["modelId"]=="WM-DAT-008" and c["registryId"]=="vr.wm-dat-008"
assert c["canonicalPublishable"] is False and c["entryKind"]=="aggregate"
assert len(c["relations"])==6 and all(x["relation"]=="REFERENCE" for x in c["relations"])
assert len(c["invariants"])>=14
assert len(c["productVersion"]["required"])>=12
assert c["consumerEntitlementBinding"]["classification"].startswith("dependent relation")
assert f["modelId"]==c["modelId"] and len(f["fixtures"])>=7
assert len({x["id"] for x in f["fixtures"]})==len(f["fixtures"])
print("candidate-ok: WM-DAT-008, 14 invariants, 6 external boundaries, 7 fixtures")
