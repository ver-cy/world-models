# EM-FAC-01 provider comparison

Claude and Grok agree on the composition: reuse the existing Place, Site, Facility and Building masters; complete reserved WM-BLT-002 as the single Premises / Spatial Unit authority; retire WM-PLC-009 as a standalone duplicate while preserving Indoor Topology as a WM-BLT-002 profile; treat office as an effective-dated use designation; and retain Workplace Allocation as an identifier-unassigned **NEW MODEL** relationship.

Grok corrects the containment language. Place locates Site by reference and is not its container. Site-to-Facility and Facility-to-Building are optional intermediate layers; a facility may lack a site and a building may lack a facility. Premises still resolve to their building shell, while client-site, home-jurisdiction and mobile workplace loci need not create premises records.

The reconciled candidates keep lease, ownership, access, booking, employment, establishment and legal-branch authority external. Remote-home allocations store only approved jurisdiction granularity, never residential addresses. Allocation identity survives booking changes and records successor versions when endpoint meaning changes.

Both providers reject assigning a numeric Workplace Allocation identifier before registry review. WM-PLC-009 retirement, relation retargeting, source-pinned built-environment crosswalks, non-US privacy and employment-law review, the frozen audit, package conversion and live verification remain holds.
