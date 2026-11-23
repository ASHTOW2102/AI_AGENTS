# GraphQLIntrospectionExposureAudit

Flags GraphQL schemas with introspection enabled in production, letting attackers enumerate the full API surface including unreleased fields.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
