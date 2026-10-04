# WM-LIV-021 canonical preflight

- Sequence: 179
- Registry identity: `vr.wm-liv-021`
- Model identity: `WM-LIV-021`
- Registered name: `Disease / Biological Condition`
- Registry-plane kind: `standalone-mm`
- Candidate subject kind: `aggregate`
- Navigation: `NAV.PHY.LIV.HLT`
- Domain: `PHY.LIV.HLT`
- Registered parent: `WM-LIV-002 Organism Individual`
- Registered incoming relation: `WM-ACT-049 Care Plan / Episode REFERENCE`
- Registered purpose: condition is not the same object as a care encounter

## Frozen boundary

The root is one condition occurrence concerning an organism plus immutable,
source-qualified assertions about that occurrence. A disease concept,
classification code and diagnostic criterion are external terminology or rule
masters. A diagnosis is an epistemic assertion about the occurrence, not the
occurrence itself. Symptoms, measurements, specimens, encounters, care plans,
procedures and outcomes retain external identities and lifecycles.

Clinical status, verification status and record status are independent. Onset,
first manifestation, first observation, diagnosis, recording, remission,
relapse, recurrence, resolution and death are not interchangeable clocks.
Severity, stage, course, body site, morphology, etiology and consequences are
source-qualified assertions with method, profile, effective interval and
evidence rather than timeless intrinsic truth.

The model must support human and non-human conditions while keeping
human-clinical, public-health, rare-disease, cancer, infectious, genetic and
veterinary profiles explicit. It never infers a condition from a code alone or
clinical action from a condition assertion.
