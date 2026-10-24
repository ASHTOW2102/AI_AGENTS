# DataPipelineBackfillAudit

Checks large data backfills for chunking, resumable checkpoints, idempotency, and post-run validation. Pass a backfill plan dictionary to `audit()`; it does not launch jobs.
