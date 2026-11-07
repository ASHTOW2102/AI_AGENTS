# CloudCostAnomalyAudit

Detects anomalous cloud spend spikes relative to historical baselines.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
