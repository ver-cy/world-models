import json
from pathlib import Path
p=Path(__file__).parent
c=json.loads((p/"candidate.json").read_text(encoding="utf-8")); f=json.loads((p/"fixtures.json").read_text(encoding="utf-8"))
assert c["modelId"]=="WM-SFT-003" and c["version"]=="0.1.0-candidate.2"
assert {"InterfaceContract","ContractRevision","ConsumerPin","RevisionResolutionRecord","RevisionExposure","CompatibilityAssessment"} <= set(c["objects"])
assert len(c["invariants"])>=20 and all("id" in x and "rule" in x for x in c["invariants"])
assert all(("satisfies" in x) if x["kind"]=="positive" else ("violates" in x) for x in f["cases"])
assert not any("integrationRef" in json.dumps(x) for x in c["objects"].values())
print(f"candidate-ok: WM-SFT-003, {len(c['invariants'])} invariants, {len(f['cases'])} fixtures")
