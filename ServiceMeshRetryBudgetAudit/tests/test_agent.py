import unittest
from agent import audit


class ServiceMeshRetryBudgetAuditTests(unittest.TestCase):

    def test_unbounded(self):
        self.assertTrue(audit({"retries_enabled": True, "retry_budget_percent": None}))

    def test_ok(self):
        self.assertFalse(audit({"retries_enabled": True, "retry_budget_percent": 10, "method": "GET", "max_retries": 2}))
