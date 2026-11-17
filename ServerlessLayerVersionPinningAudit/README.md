# ServerlessLayerVersionPinningAudit

Flags serverless functions that reference a shared layer by a mutable alias instead of a pinned version.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
