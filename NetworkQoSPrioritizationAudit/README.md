# NetworkQoSPrioritizationAudit

Flags networks carrying latency-sensitive and bulk traffic on the same queue with no QoS prioritization configured.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
