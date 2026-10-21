# AnalyticsEventPrivacyAudit

Reviews analytics event definitions for unapproved properties, direct identifiers, missing consent gates, and retention beyond the approved period.

## Usage

```python
from agent import audit
print(audit({"properties": {"campaign": "spring"}, "retention_days": 30, "approved_retention_days": 30}, {"campaign"}))
```

Provide an event dictionary and the set of approved property names. Results contain severity and a concise issue description. Runs offline without credentials.
