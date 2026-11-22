import unittest
from agent import audit


class DatabaseReplicationLagAuditTests(unittest.TestCase):

    def test_no_monitoring(self):
        self.assertTrue(audit({"monitors_replication_lag": False}))

    def test_ok(self):
        self.assertFalse(audit({"monitors_replication_lag": True, "alert_threshold_seconds": 30}))
