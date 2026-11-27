# CloudBillingAlertThresholdAudit

Flags cloud accounts with no budget alert configured, so a cost spike (runaway resource, abuse, misconfiguration) goes unnoticed until the invoice arrives.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
