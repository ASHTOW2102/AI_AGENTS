# APIConsumerVersionSkewAudit

Flags API consumers still pinned to deprecated client library versions well past the recommended upgrade window.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
