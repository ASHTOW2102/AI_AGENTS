# WebAppCDNScriptIntegrityAudit

Flags pages that load third-party scripts without a Subresource Integrity hash, letting a compromised CDN inject arbitrary code.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
