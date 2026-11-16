# ServerlessDeadLetterQueueAudit

Flags serverless functions with no dead-letter queue configured for failed asynchronous invocations.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
