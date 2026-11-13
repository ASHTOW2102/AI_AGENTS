# NetworkASNReputationAudit

Flags inbound connections originating from ASNs with poor reputation scores that bypass blocking rules.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
