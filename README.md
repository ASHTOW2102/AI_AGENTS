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

## Getting started

Clone the repository, choose an agent directory, and follow that agent's README.

```bash
git clone https://github.com/ASHTOW2102/AI_AGENTS.git
cd AI_AGENTS
```

Each agent keeps its own dependencies and environment example. Never commit a populated .env file.
