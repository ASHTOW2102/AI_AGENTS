# BatchIdempotencyAudit

Checks batch-job retries for stable idempotency keys, bounded attempts, external-write deduplication, and adequate record lifetime. Provide job metadata to `audit()`; it does not execute jobs or access external systems.
