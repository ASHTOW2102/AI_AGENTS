# CloudFailoverReadinessAudit

Assesses regional failover readiness using region count, measured RTO, replication lag, recovery-region dependencies, and exercise recency.

## Usage

```python
from agent import audit
print(audit({"regions": 2, "target_rto_minutes": 60, "measured_rto_minutes": 45,
             "max_replication_lag_minutes": 5, "replication_lag_minutes": 1,
             "days_since_failover_exercise": 90}))
```

Supply service recovery metrics as a dictionary. The agent returns actionable findings and works offline.
