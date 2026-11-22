import unittest
from agent import audit


class CrossRegionFailoverAuditTests(unittest.TestCase):

    def test_no_automated_failover(self):
        self.assertTrue(audit({"has_automated_failover": False, "last_failover_test_days_ago": None}))

    def test_ok(self):
        self.assertFalse(audit({"has_automated_failover": True, "last_failover_test_days_ago": 30}))
