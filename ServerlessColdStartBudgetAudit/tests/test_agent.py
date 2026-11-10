import unittest
from agent import audit


class ServerlessColdStartBudgetAuditTests(unittest.TestCase):

    def test_slow_cold_start(self):
        self.assertTrue(audit({"cold_start_ms": 3000, "max_acceptable_cold_start_ms": 1000}))

    def test_ok(self):
        self.assertFalse(audit({"cold_start_ms": 200, "max_acceptable_cold_start_ms": 1000, "on_critical_path": True, "provisioned_concurrency_enabled": True}))
