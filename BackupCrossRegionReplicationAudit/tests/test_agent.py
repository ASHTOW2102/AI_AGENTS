import unittest
from agent import audit


class BackupCrossRegionReplicationAuditTests(unittest.TestCase):

    def test_not_replicated(self):
        self.assertTrue(audit({"cross_region_replicated": False}))

    def test_ok(self):
        self.assertFalse(audit({"cross_region_replicated": True, "replication_lag_hours": 1, "max_acceptable_lag_hours": 24}))
