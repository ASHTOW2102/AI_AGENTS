# WebAppSubresourceIntegrityAudit

Flags web pages that load third-party scripts without Subresource Integrity hashes.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
