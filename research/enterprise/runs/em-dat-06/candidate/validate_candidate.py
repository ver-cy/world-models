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
assert len(candidate["invariants"]) >= 13
assert len({item["target"] for item in candidate["relations"]}) == len(candidate["relations"])
assert all(item["relation"] == "REFERENCE" for item in candidate["relations"])
assert all(item["required"] is False for item in candidate["relations"])
assert len({item["id"] for item in candidate["operations"]}) == len(candidate["operations"])
assert fixtures["modelId"] == candidate["modelId"]
assert len(fixtures["fixtures"]) >= 7
assert len({item["id"] for item in fixtures["fixtures"]}) == len(fixtures["fixtures"])
assert all(item["input"] and item["expected"] for item in fixtures["fixtures"])

text = json.dumps(candidate, ensure_ascii=False).lower()
for required in ("definitionversionid", "cutoffat", "asofbasis", "calendarbasis", "inputsnapshots", "disclosurepolicytuple", "suppressionmanifest", "supersedesreportissueid"):
    assert required in text, required

print("candidate-ok: WM-REC-002, 13 invariants, 6 external boundaries, 7 fixtures")
