# SearchRelevanceFeedbackLoopAudit

Flags search ranking systems that train directly on raw click data without correcting for position bias.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
