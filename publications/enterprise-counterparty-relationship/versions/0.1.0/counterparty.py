from __future__ import annotations
import re
from datetime import datetime, timezone

class Invalid(ValueError): pass
DIGEST=re.compile(r"^sha256:(?!0{64}$)[0-9a-f]{64}$")
RFC3339=re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$")
ROLE_MODEL={"customer":"WM-ORG-014","supplier":"WM-ORG-015","partner":"WM-ORG-015"}
FORBIDDEN_CONTACT={"value","contactValue","channel","normalizedValue","verification","consent","consentRef","reachable"}
SET_FIELDS={"kind","setId","partyRef","observerDimensionRef","createdAt","displayCache"}
ROLE_FIELDS={"kind","bindingId","setRef","role","upstreamModel","upstreamRecordRef","upstreamVersion","upstreamDigest","sourceMasterRef","validFrom","validTo","supersededByRef"}
SCOPE_FIELDS={"kind","scopeBindingId","setRef","scopeKind","targetRef","sourceMasterRef","validFrom","validTo"}
CONTACT_FIELDS={"kind","assignmentId","setRef","endpointRef","endpointModel","purpose","roleBindingRef","scopeBindingRef","validFrom","validTo"}
SEGMENT_FIELDS={"kind","assertionId","setRef","code","schemeRef","schemeVersion","sourceRef","method","assertedAt","validFrom","validTo","supersedesRef","reasonCode"}

def _ref(v,n):
    if not isinstance(v,str) or not v.strip(): raise Invalid(f"{n} is required")
    return v
def _digest(v,n):
    if not isinstance(v,str) or not DIGEST.fullmatch(v): raise Invalid(f"{n} must be non-zero sha256")
    return v
def _time(v,n):
    _ref(v,n)
    if not RFC3339.fullmatch(v): raise Invalid(f"{n} must be strict RFC3339")
    try: x=datetime.fromisoformat(v.replace("Z","+00:00"))
    except ValueError as e: raise Invalid(f"{n} invalid") from e
    return x.astimezone(timezone.utc)
def _interval(x):
    start=_time(x.get("validFrom"),"validFrom"); end=_time(x["validTo"],"validTo") if x.get("validTo") else None
    if end and end <= start: raise Invalid("validTo must be after validFrom")
    return start,end
def _active(x,t):
    a,b=_interval(x); return a <= t and (b is None or t < b)

def validate_profile(sets,roles,scopes,contacts,segments,as_at):
    t=_time(as_at,"asAt")
    for name,items in (("sets",sets),("roles",roles),("scopes",scopes),("contacts",contacts),("segments",segments)):
        if not isinstance(items,list) or any(not isinstance(x,dict) for x in items): raise Invalid(f"{name} must be a list of records")
    ids=set(); keys=set(); set_by_id={}
    for s in sets:
        if s.get("kind")!="CounterpartyRelationshipSet": raise Invalid("invalid set kind")
        if set(s)-SET_FIELDS: raise Invalid("unknown set fields")
        sid=_ref(s.get("setId"),"setId"); key=(_ref(s.get("partyRef"),"partyRef"),_ref(s.get("observerDimensionRef"),"observerDimensionRef"))
        if sid in ids or key in keys: raise Invalid("duplicate set identity")
        ids.add(sid); keys.add(key); set_by_id[sid]=s; _time(s.get("createdAt"),"createdAt")
        if "displayCache" in s:
            cache=s["displayCache"]
            if not isinstance(cache,dict) or cache.get("authoritative") is not False or not isinstance(cache.get("values"),dict) or set(cache)-{"authoritative","values"} or any(not isinstance(v,str) for v in cache["values"].values()): raise Invalid("display cache must be an explicitly non-authoritative string map")
    role_by_id={}
    for r in roles:
        if r.get("kind")!="CommercialRoleBinding": raise Invalid("invalid role kind")
        if set(r)-ROLE_FIELDS: raise Invalid("unknown role fields")
        rid=_ref(r.get("bindingId"),"bindingId")
        if rid in role_by_id: raise Invalid("duplicate bindingId")
        if r.get("setRef") not in set_by_id: raise Invalid("dangling role setRef")
        role=_ref(r.get("role"),"role")
        if role not in ROLE_MODEL or r.get("upstreamModel")!=ROLE_MODEL[role]: raise Invalid("role-to-authority mismatch")
        _ref(r.get("upstreamRecordRef"),"upstreamRecordRef"); _ref(r.get("upstreamVersion"),"upstreamVersion"); _digest(r.get("upstreamDigest"),"upstreamDigest"); _ref(r.get("sourceMasterRef"),"sourceMasterRef"); _interval(r)
        if any(k in r for k in ("relationshipState","qualificationStatus","approvalStatus","risk","performance")): raise Invalid("upstream lifecycle copied into role binding")
        role_by_id[rid]=r
    for rid,r in role_by_id.items():
        target=r.get("supersededByRef")
        if target and (target==rid or target not in role_by_id or role_by_id[target]["setRef"]!=r["setRef"]): raise Invalid("invalid role supersession")
    scope_by_id={}
    for s in scopes:
        if s.get("kind")!="AccountScopeBinding": raise Invalid("invalid scope kind")
        if set(s)-SCOPE_FIELDS: raise Invalid("unknown scope fields")
        sid=_ref(s.get("scopeBindingId"),"scopeBindingId")
        if sid in scope_by_id: raise Invalid("duplicate scopeBindingId")
        if s.get("setRef") not in set_by_id: raise Invalid("dangling scope setRef")
        if s.get("scopeKind") not in {"seller","buyer","legal-entity","group"}: raise Invalid("invalid scopeKind")
        _ref(s.get("targetRef"),"targetRef"); _ref(s.get("sourceMasterRef"),"sourceMasterRef"); _interval(s); scope_by_id[sid]=s
    contact_by_id={}
    for c in contacts:
        if c.get("kind")!="ContactAssignment": raise Invalid("invalid contact kind")
        if set(c)-CONTACT_FIELDS: raise Invalid("unknown contact fields")
        cid=_ref(c.get("assignmentId"),"assignmentId")
        if cid in contact_by_id: raise Invalid("duplicate assignmentId")
        if c.get("setRef") not in set_by_id: raise Invalid("dangling contact setRef")
        if c.get("endpointModel")!="WM-PER-010": raise Invalid("party endpoints resolve through WM-PER-010")
        if FORBIDDEN_CONTACT & set(c): raise Invalid("contact assignment owns forbidden endpoint or consent data")
        _ref(c.get("endpointRef"),"endpointRef"); _ref(c.get("purpose"),"purpose")
        if c.get("roleBindingRef") not in role_by_id: raise Invalid("dangling contact role")
        if c.get("scopeBindingRef") not in scope_by_id: raise Invalid("dangling contact scope")
        if role_by_id[c["roleBindingRef"]]["setRef"]!=c["setRef"] or scope_by_id[c["scopeBindingRef"]]["setRef"]!=c["setRef"]: raise Invalid("cross-set contact assignment")
        _interval(c); contact_by_id[cid]=c
    segment_by_id={}
    for s in segments:
        if s.get("kind")!="SegmentationAssertion": raise Invalid("invalid segment kind")
        if set(s)-SEGMENT_FIELDS: raise Invalid("unknown segment fields")
        sid=_ref(s.get("assertionId"),"assertionId")
        if sid in segment_by_id: raise Invalid("duplicate assertionId")
        if s.get("setRef") not in set_by_id: raise Invalid("dangling segment setRef")
        for field in ("code","schemeRef","schemeVersion","sourceRef","method"): _ref(s.get(field),field)
        if s["method"] not in {"declared","derived","purchased","observed"}: raise Invalid("invalid segment method")
        _time(s.get("assertedAt"),"assertedAt"); _interval(s)
        segment_by_id[sid]=s
    for sid,s in segment_by_id.items():
        target=s.get("supersedesRef")
        if target and (target==sid or target not in segment_by_id or segment_by_id[target]["setRef"]!=s["setRef"]): raise Invalid("invalid segment supersession")
    return {"sets":set_by_id,"roles":role_by_id,"scopes":scope_by_id,"contacts":contact_by_id,"segments":segment_by_id,"asAt":t}

def project_current(sets,roles,scopes,contacts,segments,set_ref,as_at,purpose=None):
    state=validate_profile(sets,roles,scopes,contacts,segments,as_at); t=state["asAt"]
    if set_ref not in state["sets"]: raise Invalid("projection setRef is missing")
    anchor=state["sets"][set_ref]
    active_roles={k:v for k,v in state["roles"].items() if v["setRef"]==set_ref and _active(v,t) and not v.get("supersededByRef")}
    active_scopes={k:v for k,v in state["scopes"].items() if v["setRef"]==set_ref and _active(v,t)}
    active_contacts=[v for v in state["contacts"].values() if v["setRef"]==set_ref and _active(v,t) and v["roleBindingRef"] in active_roles and v["scopeBindingRef"] in active_scopes and (purpose is None or v["purpose"]==purpose)]
    superseded={x.get("supersedesRef") for x in state["segments"].values() if x.get("supersedesRef") and _time(x["assertedAt"],"assertedAt")<=t}
    active_segments=[v for k,v in state["segments"].items() if v["setRef"]==set_ref and k not in superseded and _active(v,t) and _time(v["assertedAt"],"assertedAt")<=t]
    return {"rolesAt":[{"bindingId":k,"role":v["role"],"upstreamRecordRef":v["upstreamRecordRef"],"upstreamVersion":v["upstreamVersion"],"upstreamDigest":v["upstreamDigest"],"sourceMasterRef":v["sourceMasterRef"]} for k,v in sorted(active_roles.items())],"contactsFor":[{"assignmentId":v["assignmentId"],"endpointRef":v["endpointRef"],"endpointModel":v["endpointModel"],"purpose":v["purpose"],"roleBindingRef":v["roleBindingRef"],"scopeBindingRef":v["scopeBindingRef"]} for v in sorted(active_contacts,key=lambda x:x["assignmentId"])],"segmentsAt":[{"assertionId":v["assertionId"],"code":v["code"],"schemeRef":v["schemeRef"],"schemeVersion":v["schemeVersion"],"sourceRef":v["sourceRef"],"method":v["method"],"assertedAt":v["assertedAt"]} for v in sorted(active_segments,key=lambda x:x["assertionId"])],"provenance":{"profile":"EM-COM-01","profileVersion":"0.1.0","setRef":set_ref,"partyRef":anchor["partyRef"],"observerDimensionRef":anchor["observerDimensionRef"],"asAt":t.isoformat().replace("+00:00","Z")}}
