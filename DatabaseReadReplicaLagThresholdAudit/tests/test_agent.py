import unittest
from agent import audit


class DatabaseReadReplicaLagThresholdAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"current_lag_seconds": 60, "max_acceptable_lag_seconds": 10}))

    def test_ok(self):
        self.assertFalse(audit({"current_lag_seconds": 5, "max_acceptable_lag_seconds": 10}))
