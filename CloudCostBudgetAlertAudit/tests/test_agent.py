import unittest
from agent import audit


class CloudCostBudgetAlertAuditTests(unittest.TestCase):

    def test_no_thresholds(self):
        self.assertTrue(audit({"alert_thresholds": None}))

    def test_ok(self):
        self.assertFalse(audit({"alert_thresholds": [50, 90], "alert_recipients": ["team"], "forecasted_overspend": False}))
