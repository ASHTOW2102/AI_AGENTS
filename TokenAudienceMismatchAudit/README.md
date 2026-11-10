# TokenAudienceMismatchAudit

Flags tokens accepted by a service whose audience claim does not match that service's identifier.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
