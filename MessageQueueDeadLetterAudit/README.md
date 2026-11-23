# MessageQueueDeadLetterAudit

Flags message queues with no dead-letter queue configured, so poison messages are retried forever or silently dropped instead of being surfaced.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
