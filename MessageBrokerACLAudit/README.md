# MessageBrokerACLAudit

Flags message brokers whose default ACL allows any client to publish or subscribe to any topic.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
