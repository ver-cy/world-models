import json
from pathlib import Path
p=Path(__file__).parent
c=json.loads((p/"candidate.json").read_text(encoding="utf-8")); f=json.loads((p/"fixtures.json").read_text(encoding="utf-8"))
assert c["modelId"]=="WM-SFT-018" and c["version"]=="0.1.0-candidate.2"
assert {"NetworkEndpoint","AddressBinding","ConnectivityRelation","ExposureAssertion","ZoneMembership"} <= set(c["objects"])
assert len(c["invariants"])>=13 and all("id" in x and "rule" in x for x in c["invariants"])
assert all(("satisfies" in x) if x["kind"]=="positive" else ("violates" in x) for x in f["cases"])
print(f"candidate-ok: WM-SFT-018, {len(c['invariants'])} invariants, {len(f['cases'])} fixtures")
