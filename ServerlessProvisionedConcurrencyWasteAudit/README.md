# ServerlessProvisionedConcurrencyWasteAudit

Flags serverless functions paying for provisioned concurrency far above their observed peak invocation rate.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
