# CloudFunctionColdPathAudit

Flags cloud functions on rarely-exercised error paths that are untested and likely to fail silently under cold invocation.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
