# CloudStorageBucketVersioningAudit

Checks cloud storage buckets for disabled versioning that would prevent recovery from accidental overwrite or deletion.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
