# KubernetesCRDVersionSkewAudit

Flags Kubernetes custom resources still on a deprecated CRD schema version with no migration path defined.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
