# MessageQueuePoisonMessageAudit

Flags message queue consumers with no dead-letter queue or max-retry limit, where a single malformed 'poison' message is redelivered indefinitely and blocks the queue.

## What it checks

Checks message queue consumer configuration for a dead-letter queue and a maximum delivery attempt limit to contain poison messages.

## Usage

```python
from agent import audit

findings = audit({...})
for f in findings:
    print(f["severity"], f["issue"])
```

## Running tests

```bash
python -m unittest discover -s tests
```
