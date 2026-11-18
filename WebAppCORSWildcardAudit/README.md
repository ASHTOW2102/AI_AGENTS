# WebAppCORSWildcardAudit

Flags web API endpoints that respond with Access-Control-Allow-Origin: * while also allowing credentialed requests.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
