# DatabaseShardRebalancingAudit

Flags sharded database clusters with significant data skew across shards and no automated rebalancing in place.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
