# DataRetentionPolicyEnforcementAudit

Flags datasets with a defined retention policy that is not actually enforced by automated deletion.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
