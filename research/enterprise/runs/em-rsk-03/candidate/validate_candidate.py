import json, pathlib
p=pathlib.Path(__file__).parent
c=json.loads((p/"authorization-domain-access-grant.json").read_text(encoding="utf-8"))
f=json.loads((p/"fixtures.json").read_text(encoding="utf-8"))
assert c["modelId"] is None and c["registryId"] is None and c["allocationState"]=="unassigned" and not c["canonicalPublishable"]
ids=[r["id"] for r in c["invariantRules"]]; assert len(ids)==len(set(ids))==24
assert len(f["cases"])==25 and not f["canonicalPublishable"] and not f["executable"]
known=set(ids)
for x in f["cases"]:
 assert x["input"] and x["expect"] and set(x["rules"])<=known
print("EM-RSK-03 candidate valid: 24 rules, 25 fixtures, no identifiers")
