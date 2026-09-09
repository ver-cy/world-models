# WM-ACT-040 bounded external research focus

Produce one complete schema-valid result for `WM-ACT-040 Onboarding / Offboarding`.

Treat it as one governed worker-transition case aggregate with a mandatory
profile: join or onboard, internal move or role change, leave or offboard, or
rejoin. Cover identity, trigger, authority, employment and role bindings,
plans, tasks and dependencies, notices and obligations, identity proofing,
accounts, access and credentials, workspaces and facilities, devices and other
assets, licences, data custody and transfer, knowledge handover, induction and
training, benefits and administrative steps, communications and support,
returns and revocation, exit evidence, continuing obligations, lifecycle,
metrics, exceptions, provenance, interoperability, privacy, retention and safe
agents.

Keep Person, Employment, Role Assignment, Organization, Account, Credential,
Access Grant, Device, Asset, Licence, Workspace, Training, Competency,
Agreement, Benefit, Dataset, Record, Communication and Audit masters separate.
Never infer employment from onboarding, active work from account activation,
authority from group membership, completion from checked tasks, revocation
from a disable request or data deletion from access loss.

Target 6 bundles, 12 layers, 24 findings, 72 questions, 24 artifacts and 10
functions. Prefer NIST SP 800-53 Rev. 5, CIS Controls v8, IETF SCIM RFCs 7643
and 7644, OPM onboarding guidance, CISA separation guidance, NCSC joiner mover
leaver guidance, ISO 30414, GDPR, W3C PROV and WCAG, NIST Privacy Framework,
records guidance and RFC 3339. Preserve source, regional, relation and external
provider limitations as visible holds.
