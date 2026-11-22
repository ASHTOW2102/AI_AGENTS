# DatabaseReplicationLagAudit

Flags read replicas with no replication-lag monitoring or alert threshold, allowing stale reads to silently serve outdated data after a lag spike.

## What it checks

Checks database read replica configuration for replication-lag monitoring and an alert threshold.

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
