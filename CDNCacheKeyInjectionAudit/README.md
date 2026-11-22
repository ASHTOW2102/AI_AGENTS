# CDNCacheKeyInjectionAudit

Flags CDN configurations that include unvalidated headers or query parameters in the cache key, allowing an attacker to poison the shared cache with a malicious response for other users.

## What it checks

Checks CDN cache key configuration for unvalidated headers or unbounded query parameters that enable cache poisoning.

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
