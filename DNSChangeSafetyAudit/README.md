# DNSChangeSafetyAudit

Checks DNS change plans for rollback, TTL preparation, registrar consistency, and DNSSEC DS coordination. Pass a change record to `audit()`; it does not query or modify DNS.
