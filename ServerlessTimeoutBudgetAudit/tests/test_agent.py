import unittest
from agent import audit


class ServerlessTimeoutBudgetAuditTests(unittest.TestCase):

    def test_budget_exceeded(self):
        self.assertTrue(audit({"sum_downstream_timeout_ms": 5000, "function_timeout_ms": 3000}))

    def test_ok(self):
        self.assertFalse(audit({"sum_downstream_timeout_ms": 1000, "function_timeout_ms": 3000, "max_approved_timeout_ms": 5000, "cold_start_ms": 100}))
