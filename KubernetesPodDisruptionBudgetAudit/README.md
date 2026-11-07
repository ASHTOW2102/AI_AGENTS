# KubernetesPodDisruptionBudgetAudit

Checks Kubernetes workloads for missing or misconfigured PodDisruptionBudgets.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
