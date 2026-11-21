import unittest
from agent import audit


class SearchQueryCostBudgetAuditTests(unittest.TestCase):

    def test_no_estimation(self):
        self.assertTrue(audit({"cost_estimation_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"cost_estimation_enabled": True, "estimated_cost": 100, "max_acceptable_cost": 1000, "rejected": False}))
