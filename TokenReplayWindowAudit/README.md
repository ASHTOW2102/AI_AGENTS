# TokenReplayWindowAudit

Flags short-lived authentication tokens with a replay window too large relative to their validity period.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
