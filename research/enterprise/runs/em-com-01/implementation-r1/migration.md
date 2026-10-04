# Migration

Deduplicate candidate records by authoritative Party reference before creating profile sets. Convert customer/supplier/partner rows into upstream record references, not local subject identities. Move contact values to the endpoint authority and retain only assignment context. Convert bare segments only when scheme, version, source and time can be reconstructed; otherwise create a hold.
