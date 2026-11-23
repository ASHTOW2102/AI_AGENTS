# DataRetentionPolicyAudit

Flags datasets containing PII with no defined retention policy, risking indefinite storage of personal data past its lawful purpose.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
