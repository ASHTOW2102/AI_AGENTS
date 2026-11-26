# CloudCDNOriginExposureAudit

Flags CDN-fronted origins that remain publicly reachable directly, letting attackers bypass the CDN's WAF and caching entirely.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
