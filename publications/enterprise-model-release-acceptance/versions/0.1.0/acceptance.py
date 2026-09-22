from __future__ import annotations

import re
from datetime import datetime, timezone


class Invalid(ValueError):
    pass


SEMVER = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$")
DIGEST = re.compile(r"^sha256:(?!0{64}$)[0-9a-f]{64}$")
RFC3339 = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$")
MUTABLE = re.compile(r"(^|[/:@?&=_.-])(main|master|head|latest|tbd)([/:@?&=_.-]|$)|[*?]|\[[^]]*\]", re.I)


def _digest(value, field):
    if not isinstance(value, str) or not DIGEST.fullmatch(value) or value == "sha256:" + "0" * 64:
        raise Invalid(f"{field} must be a non-zero sha256 digest")
    return value


def _ref(value, field):
    if not isinstance(value, str) or not value.strip():
        raise Invalid(f"{field} is required")
    return value


def _instant(value, field):
    _ref(value, field)
    if not RFC3339.fullmatch(value):
        raise Invalid(f"{field} must be strict RFC3339")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise Invalid(f"{field} must be RFC3339") from exc
    if parsed.tzinfo is None:
        raise Invalid(f"{field} needs an offset")
    return parsed.astimezone(timezone.utc)


def _not_mutable(value, field):
    _ref(value, field)
    if MUTABLE.search(value):
        raise Invalid(f"{field} is mutable")


def validate_release(release, registered=None):
    if release.get("kind") != "ModelRelease":
        raise Invalid("invalid ModelRelease kind")
    required = ("releaseId", "modelId", "version", "packageByteDigest", "immutableLocator", "registryEntryRef", "lockSetRef", "resolutionReceiptRef", "createdAt")
    for field in required:
        _ref(release.get(field), field)
    if not SEMVER.fullmatch(release["version"]):
        raise Invalid("version must be SemVer 2.0.0")
    _digest(release["packageByteDigest"], "packageByteDigest")
    if release["immutableLocator"] != "urn:sha256:" + release["packageByteDigest"].split(":", 1)[1]:
        raise Invalid("immutableLocator must exactly bind packageByteDigest")
    _not_mutable(release["lockSetRef"], "lockSetRef")
    _not_mutable(release["resolutionReceiptRef"], "resolutionReceiptRef")
    _instant(release["createdAt"], "createdAt")
    fp = release.get("semanticFingerprint")
    if fp is not None:
        _digest(fp, "semanticFingerprint")
        if fp == release["packageByteDigest"]:
            raise Invalid("semanticFingerprint cannot equal packageByteDigest")
        _ref(release.get("canonicalizationProfileRef"), "canonicalizationProfileRef")
        _digest(release.get("canonicalizationProfileDigest"), "canonicalizationProfileDigest")
    if registered:
        coordinate = (release["modelId"], release["version"])
        old = registered.get(coordinate)
        if old is not None and old != release["packageByteDigest"]:
            raise Invalid("same model/version cannot be republished with different bytes")
    return True


def validate_receipt(receipt, release, target_context):
    _ref(receipt.get("receiptId"), "receiptId")
    _digest(receipt.get("subjectDigest"), "receipt.subjectDigest")
    _digest(receipt.get("closureDigest"), "receipt.closureDigest")
    if receipt["subjectDigest"] != release["packageByteDigest"]:
        raise Invalid("receipt is for different bytes")
    if receipt.get("targetContext") != target_context:
        raise Invalid("receipt is for different target context")
    if receipt.get("resolutionReceiptRef") != release["resolutionReceiptRef"]:
        raise Invalid("receipt reference mismatch")
    if receipt.get("lockSetRef") != release["lockSetRef"]:
        raise Invalid("receipt lock-set mismatch")
    if not receipt.get("resolved") or not receipt.get("staged") or not receipt.get("mandatoryClosureComplete"):
        return False
    members = receipt.get("members", [])
    if receipt.get("memberCount") != len(members):
        raise Invalid("receipt member count mismatch")
    for member in members:
        _digest(member.get("digest"), "closure member digest")
        if member.get("locator") != "urn:sha256:" + member["digest"].split(":", 1)[1]:
            raise Invalid("closure member locator must exactly bind digest")
        if member.get("available") is not True:
            return False
    return True


def validate_assessment(assessment, release, evidence, profile, as_at):
    if assessment.get("kind") != "AcceptanceAssessment":
        raise Invalid("invalid AcceptanceAssessment kind")
    for field in ("assessmentId", "subjectReleaseRef", "profileRef", "fixtureSetRef", "assessorRef"):
        _ref(assessment.get(field), field)
    if assessment["subjectReleaseRef"] != release["releaseId"]:
        raise Invalid("assessment release mismatch")
    _digest(assessment.get("subjectDigest"), "assessment.subjectDigest")
    if assessment["subjectDigest"] != release["packageByteDigest"]:
        raise Invalid("assessment cannot transfer across package digests")
    _digest(assessment.get("profileDigest"), "profileDigest")
    _digest(assessment.get("fixtureSetDigest"), "fixtureSetDigest")
    _not_mutable(assessment["profileRef"], "profileRef")
    _not_mutable(assessment["fixtureSetRef"], "fixtureSetRef")
    assessed = _instant(assessment.get("assessedAt"), "assessedAt")
    effective = _instant(assessment.get("effectiveAt"), "effectiveAt")
    if effective < assessed:
        raise Invalid("assessment cannot be effective before assessedAt")
    pins = assessment.get("toolPins") or []
    if not pins:
        raise Invalid("toolPins are required")
    for pin in pins:
        _ref(pin.get("name"), "tool name")
        if not SEMVER.fullmatch(pin.get("version", "")):
            raise Invalid("tool version must be SemVer")
        _digest(pin.get("artifactDigest"), "tool artifactDigest")
    tool_digests = {p["artifactDigest"] for p in pins}
    refs = set(assessment.get("evidenceRefs") or [])
    if not refs:
        raise Invalid("evidenceRefs are required")
    evidence_ids = [item.get("evidenceId") for item in evidence]
    if len(evidence_ids) != len(set(evidence_ids)):
        raise Invalid("duplicate evidenceId")
    by_id = {item.get("evidenceId"): item for item in evidence}
    if not refs.issubset(by_id):
        raise Invalid("assessment references missing evidence")
    kinds = set()
    for ref in refs:
        item = by_id[ref]
        if item.get("kind") != "ConformanceEvidenceRef": raise Invalid("invalid evidence kind")
        if item.get("assessmentRef") != assessment["assessmentId"]:
            raise Invalid("evidence assessment mismatch")
        if item.get("subjectDigest") != release["packageByteDigest"]:
            raise Invalid("evidence subject mismatch")
        _digest(item.get("contentDigest"), "evidence contentDigest")
        _digest(item.get("producingToolDigest"), "evidence producingToolDigest")
        if item["producingToolDigest"] not in tool_digests: raise Invalid("evidence tool is not pinned")
        if item.get("locator") != "urn:sha256:" + item["contentDigest"].split(":", 1)[1]:
            raise Invalid("evidence locator must exactly bind content digest")
        if item.get("retentionClass") not in {"release-lifetime", "longer"}:
            raise Invalid("evidence retention is too short")
        kinds.add(item.get("evidenceType"))
    if assessment.get("profileRef") != profile.get("profileRef") or assessment.get("profileDigest") != profile.get("profileDigest"):
        raise Invalid("assessment profile does not match gate profile")
    required_kinds = set(profile.get("requiredEvidenceKinds") or [])
    mandatory = set(profile.get("mandatoryCriteria") or [])
    negative = set(profile.get("negativeCriteria") or [])
    if not required_kinds or not mandatory or not negative: raise Invalid("gate profile is incomplete")
    if not required_kinds.issubset(kinds):
        return False
    criteria = assessment.get("criterionResults") or []
    criterion_ids = [x.get("criterion") for x in criteria]
    if len(criterion_ids) != len(set(criterion_ids)): raise Invalid("duplicate criterion result")
    results = {x.get("criterion"): x.get("result") for x in criteria}
    active = effective <= as_at
    return active and assessment.get("outcome") == "pass" and assessment.get("fixtureResult") == "pass" and (mandatory | negative).issubset(results) and all(results[x] == "pass" for x in mandatory | negative)


def validate_holds(holds, release, as_at):
    open_blocking = set()
    seen = set()
    for hold in holds:
        hid = _ref(hold.get("holdId"), "holdId")
        if hid in seen:
            raise Invalid("duplicate holdId")
        seen.add(hid)
        if hold.get("kind") != "PublicationHoldDisposition": raise Invalid("invalid hold kind")
        if hold.get("subjectReleaseRef") != release["releaseId"]:
            raise Invalid("hold release mismatch")
        scopes = set(hold.get("scopes") or [])
        if not scopes or not scopes.issubset({"canonical", "new-install", "discovery"}):
            raise Invalid("invalid hold scopes")
        state, severity = hold.get("state"), hold.get("severity")
        if state not in {"open","resolved","waived","superseded"}: raise Invalid("invalid hold state")
        if severity not in {"blocking","advisory"}: raise Invalid("invalid hold severity")
        opened = _instant(hold.get("openedAt"), "openedAt")
        closed = _instant(hold["closedAt"], "closedAt") if hold.get("closedAt") else None
        if state == "open" and closed: raise Invalid("open hold cannot have closedAt")
        if state != "open":
            if not closed or closed < opened: raise Invalid("closed hold needs valid closedAt")
            _ref(hold.get("authorityRef"), "hold authorityRef")
            _digest(hold.get("dispositionEvidenceDigest"), "hold disposition evidence")
        active = opened <= as_at and (closed is None or as_at < closed)
        if active and severity == "blocking":
            open_blocking |= scopes
    return open_blocking


def validate_withdrawals(notices, release, as_at):
    if isinstance(notices, dict): notices = [notices]
    active_scopes = set()
    for notice in notices or []:
      if notice.get("kind") != "WithdrawalNotice": raise Invalid("invalid withdrawal kind")
      for field in ("noticeId", "registryWithdrawalActRef", "authorityRef", "reasonCode"):
        _ref(notice.get(field), field)
      if notice.get("subjectReleaseRef") != release["releaseId"]:
        raise Invalid("withdrawal release mismatch")
      if not notice.get("registryWithdrawalActRef", "").startswith("vr.wm-xct-013:act:"):
        raise Invalid("withdrawal must reference WM-XCT-013 act")
      for field in ("retainsReleaseBytes", "retainsEvidence", "retainsPriorLockResolution", "retainsTransitiveClosure"):
        if notice.get(field) is not True:
            raise Invalid(f"destructive withdrawal: {field}")
      scopes = set(notice.get("scopes") or [])
      if not scopes or not scopes.issubset({"new-install", "discovery"}):
        raise Invalid("invalid withdrawal scopes")
      if _instant(notice.get("effectiveAt"), "effectiveAt") <= as_at: active_scopes |= scopes
    return active_scopes


def derive_status(release, receipt, assessments, evidence, holds, withdrawals, target_context, as_at, profile=None, registry=None, projection=None):
    profile = profile or {"profileRef":"urn:vercy:profile:em-xct-10:0.1.0","profileDigest":"sha256:"+"6"*64,"requiredEvidenceKinds":["fixture-log"],"mandatoryCriteria":["schema"],"negativeCriteria":["negative-fixtures"]}
    registry = registry or {(release.get("modelId"),release.get("version")):release.get("packageByteDigest")}
    validate_release(release, registry)
    now = _instant(as_at, "asAt")
    installable = validate_receipt(receipt, release, target_context)
    ids=[x.get("assessmentId") for x in assessments]
    if len(ids)!=len(set(ids)): raise Invalid("duplicate assessmentId")
    by_assessment={x.get("assessmentId"):x for x in assessments}
    for item in assessments:
        parent=item.get("supersedesRef")
        if parent and parent not in by_assessment: raise Invalid("supersedesRef points to missing assessment")
        seen=set(); cursor=item
        while cursor.get("supersedesRef"):
            nxt=cursor["supersedesRef"]
            if nxt in seen or nxt == item.get("assessmentId"): raise Invalid("assessment supersession cycle")
            seen.add(nxt); cursor=by_assessment[nxt]
    superseded={x["supersedesRef"] for x in assessments if x.get("supersedesRef") and _instant(x.get("effectiveAt"),"effectiveAt") <= now}
    current=[x for x in assessments if x.get("assessmentId") not in superseded]
    results=[validate_assessment(item, release, evidence, profile, now) for item in current]
    assured = any(results)
    blocking = validate_holds(holds, release, now)
    withdrawal_scopes = validate_withdrawals(withdrawals, release, now)
    dependency_withdrawn = any(m.get("withdrawnForNewUse") is True for m in receipt.get("members", []))
    fingerprint_ready = bool(release.get("semanticFingerprint") and release.get("canonicalizationProfileRef") and release.get("canonicalizationProfileDigest"))
    withdrawn = bool(withdrawal_scopes)
    canonical = installable and assured and fingerprint_ready and "canonical" not in blocking and not withdrawn and not dependency_withdrawn
    eligible = installable and "new-install" not in blocking and "new-install" not in withdrawal_scopes and not dependency_withdrawn
    discoverable = "discovery" not in blocking and "discovery" not in withdrawal_scopes
    result={"exists": True, "installable": installable, "assured": assured, "canonical": canonical, "eligibleForNewInstall": eligible, "discoverableForNewConsumers": discoverable, "blockingScopes": sorted(blocking), "withdrawn": withdrawn}
    if projection is not None:
        keys=("installable","canonical","eligibleForNewInstall","discoverableForNewConsumers")
        result["projectionMismatches"]=[k for k in keys if projection.get(k)!=result[k]]
        result["projectionConsistent"]=not result["projectionMismatches"]
    return result
