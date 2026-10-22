# TLSCertificateRenewalAudit

Reviews certificate expiry, renewal start, renewal ownership, and hostname matching using inventory fields. ISO dates are expected; pass `today` to `audit()` to make checks deterministic. No certificate is fetched.
