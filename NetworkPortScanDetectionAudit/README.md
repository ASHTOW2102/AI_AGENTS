# NetworkPortScanDetectionAudit

Flags networks with no detection in place for sequential port-scanning activity against internal hosts.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
