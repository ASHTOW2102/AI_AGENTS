# APIBatchRequestLimitAudit

Flags batch API endpoints with no cap on the number of operations per batch request.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
