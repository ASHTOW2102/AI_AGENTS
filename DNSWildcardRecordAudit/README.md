# DNSWildcardRecordAudit

Flags DNS zones with a wildcard record whose target has not been verified, letting an attacker claim an unclaimed subdomain target and hijack arbitrary subdomains.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
