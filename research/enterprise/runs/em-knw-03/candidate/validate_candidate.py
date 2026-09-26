import json
from pathlib import Path
root=Path(__file__).resolve().parent
c=json.loads((root/"candidate.json").read_text(encoding="utf-8"))
f=json.loads((root/"fixtures.json").read_text(encoding="utf-8"))
assert c["modelId"]=="WM-REC-012" and c["registryId"]=="vr.wm-rec-012"
assert c["canonicalPublishable"] is False and c["entryKind"]=="aggregate"
assert c["recordWorks"]["rule"].startswith("Minutes and transcript are separate works")
assert len(c["relations"])==7 and all(x["relation"]=="REFERENCE" for x in c["relations"])
assert len(c["invariants"])>=14
assert f["modelId"]==c["modelId"] and len(f["fixtures"])>=7
assert len({x["id"] for x in f["fixtures"]})==len(f["fixtures"])
print("candidate-ok: WM-REC-012, 14 invariants, 7 external boundaries, 7 fixtures")
