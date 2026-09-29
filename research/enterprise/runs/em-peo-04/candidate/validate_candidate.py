import json, pathlib, sys
p=pathlib.Path(__file__).parent
objs=[json.loads((p/n).read_text(encoding="utf-8")) for n in ["candidate.json","candidacy-candidate.json","enterprise-recruitment-profile.json","fixtures.json"]]
assert objs[0]["modelId"] is None and objs[1]["modelId"] is None
assert objs[0]["candidateRevision"]==3 and objs[1]["candidateRevision"]==3
assert objs[2]["canonicalPublishable"] is False and objs[3]["executable"] is False
all_rules={r["id"] for o in objs[:2] for r in o["invariantRules"]}
covered={rid for s in objs[3]["sets"] for c in s["cases"] for rid in c.get("rules",[])}
assert all_rules <= covered
print(json.dumps({"ok":True,"rules":len(all_rules),"fixtures":sum(len(s["cases"]) for s in objs[3]["sets"])},indent=2))
