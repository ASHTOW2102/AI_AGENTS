import unittest
from agent import audit


class DataWarehouseCostAuditTests(unittest.TestCase):

    def test_idle_no_autosuspend(self):
        self.assertTrue(audit({"idle_hours_per_day": 10, "max_idle_hours_per_day": 6, "auto_suspend_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"idle_hours_per_day": 1, "full_table_scan_query_count": 0}))
