# CloudKMSGrantExpiryAudit

Flags cloud KMS key grants that have no expiry set, leaving indefinite decrypt or sign access.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
