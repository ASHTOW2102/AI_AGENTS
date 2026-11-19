# TokenClockSkewToleranceAudit

Flags token validators with clock skew tolerance set so loosely that it meaningfully extends a token's effective lifetime past expiry.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
