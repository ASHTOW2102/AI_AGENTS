# GraphQLDepthLimitAudit

Flags GraphQL endpoints that accept arbitrarily deep or recursive queries without a configured maximum query depth, enabling resource-exhaustion attacks.

## What it checks

Checks GraphQL endpoint configuration for a maximum query depth limit and fragment-cycle detection, flagging configurations that permit unbounded query nesting.

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
