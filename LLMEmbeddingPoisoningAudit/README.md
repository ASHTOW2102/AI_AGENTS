# LLMEmbeddingPoisoningAudit

Flags retrieval-augmented pipelines that index unvetted user-submitted content into the same embedding store queried for trusted context.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
