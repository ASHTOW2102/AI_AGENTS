# DatabaseConnectionPoolExhaustionAudit

Flags database connection pools running near exhaustion with no queueing or backpressure for new requests.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
