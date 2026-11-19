# CloudBillingAlertCoverageAudit

Flags cloud accounts with no billing anomaly alert covering one or more active cost centers.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
