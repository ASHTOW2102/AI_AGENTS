import unittest
from agent import audit


class CloudBillingAlertThresholdAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"has_budget_alert": False}))

    def test_ok(self):
        self.assertFalse(audit({"has_budget_alert": True}))
