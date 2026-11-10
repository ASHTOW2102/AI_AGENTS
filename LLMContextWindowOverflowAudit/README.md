# LLMContextWindowOverflowAudit

Flags LLM requests that silently truncate context when the input exceeds the model's context window.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
