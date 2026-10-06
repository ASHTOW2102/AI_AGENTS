# CronGuard

CronGuard audits interval-based scheduled-job metadata before overlapping runs or retry storms create an outage.

It detects duplicate names, runtime and timeout overlap, retry spillover into the next interval, same-slot workload collisions, invalid offsets, and invalid IANA time zones.

The deterministic audit works without credentials. With OPENAI_API_KEY, the agent explains only sanitized timing findings.

## Setup

~~~bash
cd CronGuard
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
~~~

Copy .env.example to .env only for optional AI explanations. Never commit .env.

## Usage

~~~bash
python cli.py example_schedule.json --no-model
python cli.py schedule.json
~~~

Input is a JSON array describing job intervals, offsets, timezone, expected runtime, timeout, retries, and singleton protection. The CLI exits 0 for a clean schedule, 2 for findings, or with an argparse error for malformed input.

## Tests

~~~bash
pip install -r requirements-dev.txt
python -m pytest -q
~~~

## Scope

CronGuard models fixed intervals, not full cron expressions, daylight-saving execution semantics, scheduler guarantees, distributed locks, or real resource capacity. Validate final schedules in the production scheduler.
