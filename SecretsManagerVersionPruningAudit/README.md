# SecretsManagerVersionPruningAudit

Flags secrets retaining far more old versions than their own configured maximum, needlessly widening the window in which a leaked old version stays valid-looking.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
