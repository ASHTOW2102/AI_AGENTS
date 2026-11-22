# SearchIndexStalenessAudit

Flags search indexes with no freshness SLA or staleness monitoring, allowing the index to silently drift out of sync with the source of truth after an indexing pipeline failure.

## What it checks

Checks search index configuration for staleness monitoring and a defined freshness SLA.

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
