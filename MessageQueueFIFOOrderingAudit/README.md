# MessageQueueFIFOOrderingAudit

Flags workloads that require strict message ordering but run on a standard (non-FIFO) queue, which offers no ordering guarantee.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
