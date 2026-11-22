# APIVersionDeprecationAudit

Flags API endpoints still serving a deprecated version with no sunset header or migration deadline communicated to clients, risking an abrupt breaking removal.

## What it checks

Checks deprecated API endpoints for Sunset header and communicated sunset date to avoid abrupt breaking removals.

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
