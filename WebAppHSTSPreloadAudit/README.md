# WebAppHSTSPreloadAudit

Flags sites with no HSTS header, or whose HSTS max-age is shorter than a year, weakening protection against TLS-stripping downgrade attacks.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
