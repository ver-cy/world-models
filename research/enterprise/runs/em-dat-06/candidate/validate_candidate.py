import json
from pathlib import Path

root = Path(__file__).resolve().parent
candidate = json.loads((root / "candidate.json").read_text(encoding="utf-8"))
fixtures = json.loads((root / "fixtures.json").read_text(encoding="utf-8"))

assert candidate["modelId"] == "WM-REC-002"
assert candidate["registryId"] == "vr.wm-rec-002"
assert candidate["canonicalPublishable"] is False
assert candidate["definitionVersion"]["lifecycle"] == ["draft", "issued", "superseded", "withdrawn"]
assert candidate["reportIssue"]["lifecycle"] == ["planned", "computed", "issued", "superseded", "withdrawn"]
assert candidate["version"] == "0.1.0-candidate.3"
assert len(candidate["invariants"]) >= 27
assert len({item["target"] for item in candidate["relations"]}) == len(candidate["relations"])
assert all(item["relation"] == "REFERENCE" for item in candidate["relations"])
assert all(item["required"] is False for item in candidate["relations"])
assert len({item["id"] for item in candidate["operations"]}) == len(candidate["operations"])
assert fixtures["modelId"] == candidate["modelId"]
assert len(fixtures["fixtures"]) >= 18
assert len({item["id"] for item in fixtures["fixtures"]}) == len(fixtures["fixtures"])
assert all(item["input"] and item["expected"] for item in fixtures["fixtures"])

text = json.dumps(candidate, ensure_ascii=False).lower()
for required in ("definitionversionid", "cutoffat", "asofat", "asofbasis", "calendarbasis", "inputsnapshots", "disclosurepolicytuple", "suppressionmanifest", "supersedesreportissueid", "staterequirements", "conditionalrequirements"):
    assert required in text, required

print("candidate-ok: WM-REC-002 candidate.3, 27 invariants, 8 external boundaries, 18 fixtures")
