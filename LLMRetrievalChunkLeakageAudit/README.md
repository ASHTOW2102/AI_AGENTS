# LLMRetrievalChunkLeakageAudit

Flags RAG pipelines whose retrieval step can return document chunks the requesting user is not authorized to view.

## Usage

```python
from agent import audit

findings = audit({...})
```

Each finding is a dict with `severity` and `issue` keys.
