# CrossRegionFailoverAudit

Flags multi-region services with no tested, automated failover procedure, relying instead on manual intervention during a regional outage.

## What it checks

Checks multi-region services for automated failover and a recently tested failover procedure.

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
