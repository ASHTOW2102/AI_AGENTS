import unittest
from agent import audit


class ServiceMeshCanaryRollbackAuditTests(unittest.TestCase):

    def test_no_rollback(self):
        self.assertTrue(audit({"uses_canary_traffic_split": True, "automated_rollback_on_metric_regression": False}))

    def test_ok(self):
        self.assertFalse(audit({"uses_canary_traffic_split": True, "automated_rollback_on_metric_regression": True, "rollback_tested": True}))
