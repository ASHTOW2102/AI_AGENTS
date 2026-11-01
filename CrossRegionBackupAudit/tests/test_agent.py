import unittest
from agent import audit


class CrossRegionBackupAuditTests(unittest.TestCase):

    def test_no_cross_region(self):
        self.assertTrue(audit({"cross_region_copy_exists": False}))

    def test_ok(self):
        self.assertFalse(audit({"cross_region_copy_exists": True, "replication_lag_hours": 1, "cross_region_restore_tested": True}))
