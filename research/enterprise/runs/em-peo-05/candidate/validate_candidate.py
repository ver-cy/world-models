import json,pathlib
p=pathlib.Path(__file__).parent
names=["learning-program","enrollment","learning-result","career-path","succession-plan"]
roots=[json.loads((p/f"{n}.json").read_text()) for n in names]
profile=json.loads((p/"enterprise-learning-development-profile.json").read_text())
fx=json.loads((p/"fixtures.json").read_text())
assert all(x["modelId"] is None and x["registryId"] is None and x["candidateRevision"]==3 and not x["canonicalPublishable"] for x in roots)
assert not profile["canonicalPublishable"] and not fx["executable"]
rules={r["id"] for x in roots for r in x["invariantRules"]}; covered={q for s in fx["sets"] for c in s["cases"] for q in c.get("rules",[])}
assert rules<=covered
print(json.dumps({"ok":True,"roots":5,"rules":len(rules),"fixtures":sum(len(s["cases"]) for s in fx["sets"])},indent=2))
