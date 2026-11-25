# StorageBucketPublicACLAudit

Flags cloud storage buckets with a public-read ACL, at high severity when the bucket is also known to contain sensitive data.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
