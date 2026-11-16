# KubernetesHorizontalAutoscalerThrashAudit

Flags Kubernetes HorizontalPodAutoscalers with scaling thresholds too tight, causing rapid scale up/down thrashing.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
