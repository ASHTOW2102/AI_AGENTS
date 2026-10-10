# 🤖 AI_AGENTS

A growing collection of practical, self-contained AI agents built with Python.

## Agent catalog

| Agent | Purpose | Runs without an API key |
|---|---|---:|
| [DocBrief](DocBrief/) | Summarizes uploaded documents | No |
| [HealthPlanner](HealthPlanner/) | Creates personalized health plans | No |
| [SpeakScore](SpeakScore/) | Transcribes and scores speaking practice | No |
| [UK Housing Agent](uk-housing-agent/) | Explains UK housing costs and guidance | Partly |
| [IncidentTriage](IncidentTriage/) | Converts incident reports into secret-safe action plans | Yes |
| [PromptShield](PromptShield/) | Detects prompt injection and unsafe tool-use requests | Yes |
| [SchemaScout](SchemaScout/) | Profiles CSV data and detects schema drift | Yes |
| [MailSift](MailSift/) | Privately triages email urgency and phishing signals | Yes |
| [PlanGraph](PlanGraph/) | Finds critical paths and dependency risks in project plans | Yes |
| [EnvDoctor](EnvDoctor/) | Audits environment configuration without exposing values | Yes |
| [OpenAPISentry](OpenAPISentry/) | Audits OpenAPI quality and authentication coverage | Yes |
| [A11yScout](A11yScout/) | Audits static HTML accessibility basics | Yes |
| [ChangeScribe](ChangeScribe/) | Generates release notes from Conventional Commits | Yes |
| [LocaleLens](LocaleLens/) | Checks translation catalogs for structural drift | Yes |
| [RetryRight](RetryRight/) | Audits HTTP retry traces for resilience and idempotency risks | Yes |
| [HookSentry](HookSentry/) | Audits webhook delivery security, replay, and ordering risks | Yes |
| [ADRGuard](ADRGuard/) | Audits architecture decision records for completeness and lifecycle hygiene | Yes |
| [CoverageCompass](CoverageCompass/) | Prioritizes risky test gaps from coverage.py JSON | Yes |
| [UKBillCheck](UKBillCheck/) | Recalculates UK household energy bills and flags mismatches | Yes |
| [MeetingPulse](MeetingPulse/) | Audits meeting participation, decisions, and action ownership | Yes |
| [BackupBeacon](BackupBeacon/) | Audits backup freshness, protection, and restore-test evidence | Yes |
| [CacheGuard](CacheGuard/) | Audits HTTP response caching for privacy and correctness risks | Yes |
| [FlagDoctor](FlagDoctor/) | Audits feature-flag ownership, expiry, rollout, and cleanup hygiene | Yes |
| [CronGuard](CronGuard/) | Audits scheduled jobs for overlap, retry, and collision risks | Yes |
| [PIIGuard](PIIGuard/) | Detects and masks likely personal data before files are shared | Yes |
| [LogSentry](LogSentry/) | Audits structured application logs for operational warning signals | Yes |
| [CookieCheck](CookieCheck/) | Audits web cookie settings for common security weaknesses | Yes |
| [QueueWatch](QueueWatch/) | Audits message queues for backlog and consumer risks | Yes |
| [SLAWatch](SLAWatch/) | Audits support tickets for SLA and ownership risks | Yes |
| [ConfigDiff](ConfigDiff/) | Finds risky drift between baseline and current configuration | Yes |
| [CertWatch](CertWatch/) | Audits TLS certificate inventory before outages occur | Yes |
| [CostPulse](CostPulse/) | Audits cloud cost snapshots for budget and tagging risks | Yes |
| [HeaderHawk](HeaderHawk/) | Audits HTTP security headers and browser protections | Yes |
| [RedirectRadar](RedirectRadar/) | Finds unsafe or inefficient HTTP redirect chains | Yes |
| [FormGuard](FormGuard/) | Audits web form definitions for privacy and security risks | Yes |
| [SecretLease](SecretLease/) | Audits secret inventories for rotation and ownership risks | Yes |
| [RetentionCheck](RetentionCheck/) | Audits data-retention rules for privacy and deletion gaps | Yes |
| [QuotaSentry](QuotaSentry/) | Audits API quotas and rate-limit configurations | Yes |
| [AccessReview](AccessReview/) | Audits user access exports for stale and excessive privileges | Yes |
| [ReleaseReady](ReleaseReady/) | Audits software releases for rollout and rollback readiness | Yes |
| [DNSGuard](DNSGuard/) | Audits DNS records for mail and domain-security gaps | Yes |
| [InvoiceAudit](InvoiceAudit/) | Recalculates invoices and flags payment-data inconsistencies | Yes |
| [ConsentLedger](ConsentLedger/) | Audits consent records for evidence and expiry gaps | Yes |
| [SessionSentry](SessionSentry/) | Audits application session policies for account risks | Yes |
| [RobotsGuard](RobotsGuard/) | Audits robots.txt rules for accidental exposure and blocking | Yes |
| [VendorWatch](VendorWatch/) | Audits third-party vendors for assurance and ownership gaps | Yes |
| [ChangeWindow](ChangeWindow/) | Audits production changes for timing and coordination risks | Yes |
| [TokenScope](TokenScope/) | Audits API token metadata for excessive permissions | Yes |
| [LicenseLens](LicenseLens/) | Audits dependency licenses for policy and attribution risks | Yes |
| [DomainExpiry](DomainExpiry/) | Audits domain portfolios for renewal and ownership risks | Yes |
| [StorageGuard](StorageGuard/) | Audits object-storage buckets for exposure and protection gaps | Yes |
| [BranchShield](BranchShield/) | Audits repository branch-protection configurations | Yes |
| [MFAWatch](MFAWatch/) | Audits account inventories for multi-factor authentication gaps | Yes |

## Getting started

Clone the repository, choose an agent directory, and follow that agent's README.

```bash
git clone https://github.com/ASHTOW2102/AI_AGENTS.git
cd AI_AGENTS
```

Each agent keeps its own dependencies and environment example. Never commit a populated .env file.
