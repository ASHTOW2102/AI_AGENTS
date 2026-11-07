# APISchemaVersionSkewAudit

Detects schema version skew between API producers and consumers.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
