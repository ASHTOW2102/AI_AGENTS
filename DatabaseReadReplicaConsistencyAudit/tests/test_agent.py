import unittest
from agent import audit


class DatabaseReadReplicaConsistencyAuditTests(unittest.TestCase):

    def test_high_lag(self):
        self.assertTrue(audit({"lag_ms": 5000, "max_tolerable_lag_ms": 1000}))

    def test_ok(self):
        self.assertFalse(audit({"lag_ms": 100, "max_tolerable_lag_ms": 1000, "lag_monitoring_enabled": True}))
