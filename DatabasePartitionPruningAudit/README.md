# DatabasePartitionPruningAudit

Flags database queries on partitioned tables that scan all partitions instead of pruning to relevant ones.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
