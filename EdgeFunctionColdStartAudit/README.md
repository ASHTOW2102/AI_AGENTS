# EdgeFunctionColdStartAudit

Flags edge/serverless functions with heavy initialization work on every cold start (large dependency graphs, synchronous remote config fetches) with no warm-pool or provisioned-concurrency mitigation.

## What it checks

Checks edge/serverless function configuration for cold-start latency mitigations and synchronous remote-config fetches during init.

## Usage

```python
from agent import audit

findings = audit({...})
for f in findings:
    print(f["severity"], f["issue"])
```

## Running tests

```bash
python -m unittest discover -s tests
```
