# LLMAgentLoopDetectionAudit

Flags autonomous LLM agents with no detection for repeating the same tool call in a loop, risking runaway cost or action spam.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
