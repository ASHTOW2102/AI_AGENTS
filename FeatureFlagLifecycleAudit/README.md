# FeatureFlagLifecycleAudit

Checks feature flags for overdue expiry, missing ownership, and production rollout without a rollback plan. Dates use ISO `YYYY-MM-DD`; pass an optional `today` date to `audit()` for deterministic reviews. No API key required.
