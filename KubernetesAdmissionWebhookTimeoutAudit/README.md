# KubernetesAdmissionWebhookTimeoutAudit

Flags Kubernetes admission webhooks with timeout or failure policy settings that risk cluster-wide blocking.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
