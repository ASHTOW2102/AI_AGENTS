import unittest
from agent import audit


class CloudBillingAlertCoverageAuditTests(unittest.TestCase):

    def test_uncovered(self):
        self.assertTrue(audit({"active_cost_centers": ["eng"], "cost_centers_with_alerts": []}))

    def test_ok(self):
        self.assertFalse(audit({"active_cost_centers": ["eng"], "cost_centers_with_alerts": ["eng"], "org_level_anomaly_detection_enabled": True}))
