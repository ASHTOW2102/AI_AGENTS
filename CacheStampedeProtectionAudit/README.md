# CacheStampedeProtectionAudit

Flags caching layers with no stampede protection (lock, early recomputation, or request coalescing), where a cache-key expiry under high concurrency causes a thundering herd of simultaneous origin requests.

## What it checks

Checks cache configurations for stampede protection (recompute locks or jittered early expiry) under high expected concurrency.

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
