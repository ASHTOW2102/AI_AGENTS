# APIBulkExportThrottleAudit

Checks bulk data export endpoints for throttling that prevents full-dataset exfiltration in a single request.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
