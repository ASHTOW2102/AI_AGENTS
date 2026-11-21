# TokenStorageClientSideAudit

Flags web apps storing authentication tokens in localStorage, where they're readable by any injected script, instead of an HttpOnly cookie.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
