# APIDeprecatedCipherSuiteAudit

Flags API endpoints that still negotiate deprecated or weak TLS cipher suites.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
