# QueueMessageVisibilityTimeoutAudit

Flags message queues whose visibility timeout is shorter than the worker's actual processing time, causing in-flight messages to be redelivered and processed twice.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
