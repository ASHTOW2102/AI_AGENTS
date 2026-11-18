import unittest
from agent import audit


class DatabaseStatisticsStalenessAuditTests(unittest.TestCase):

    def test_stale_stats(self):
        self.assertTrue(audit({"rows_changed_since_analyze": 50000, "row_count": 100000, "max_acceptable_change_fraction": 0.1}))

    def test_ok(self):
        self.assertFalse(audit({"rows_changed_since_analyze": 100, "row_count": 100000, "max_acceptable_change_fraction": 0.1, "auto_analyze_enabled": True}))
