# DataShareExternalPartyAudit

Flags data shared with external parties that lacks a signed data processing agreement or an expiry date.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
