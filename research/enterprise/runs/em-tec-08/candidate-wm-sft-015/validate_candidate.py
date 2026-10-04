import json,hashlib
from pathlib import Path
p=Path(__file__).parent;c=json.loads((p/"candidate.json").read_text(encoding="utf-8"));f=json.loads((p/"fixtures.json").read_text(encoding="utf-8"))
assert c["modelId"]=="WM-SFT-015" and c["registryId"]=="vr.wm-sft-015" and c["version"]=="0.1.0-candidate.2"
assert c["sourceSpecSha256"]==hashlib.sha256((p/"source-spec.json").read_bytes()).hexdigest()
assert {"TestCaseDefinition","TestExecution","ObservedOutcome","ResultAdjudication","AttemptSet","EvidenceManifest"}<=set(c["objects"])
assert "WM-SFT-010" not in {x["target"] for x in c["relations"]};assert len(c["invariants"])>=20 and len(f["cases"])>=15
print(f"candidate-ok: WM-SFT-015, {len(c['invariants'])} invariants, {len(f['cases'])} fixtures")
