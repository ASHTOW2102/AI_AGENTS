import unittest
from agent import audit


class DatabaseReplicationLagAlertAuditTests(unittest.TestCase):

    def test_high_lag(self):
        self.assertTrue(audit({"current_lag_seconds": 120, "max_acceptable_lag_seconds": 30}))

    def test_ok(self):
        self.assertFalse(audit({"lag_alert_configured": True, "current_lag_seconds": 2, "max_acceptable_lag_seconds": 30}))
