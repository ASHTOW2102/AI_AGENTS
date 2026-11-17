import unittest
from agent import audit


class NetworkAnycastFailoverAuditTests(unittest.TestCase):

    def test_unverified(self):
        self.assertTrue(audit({"failover_path_verified": False}))

    def test_ok(self):
        self.assertFalse(audit({"failover_path_verified": True, "failover_time_seconds": 5, "max_acceptable_failover_seconds": 30}))
