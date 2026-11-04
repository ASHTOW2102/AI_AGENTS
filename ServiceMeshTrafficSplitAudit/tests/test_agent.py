import unittest
from agent import audit


class ServiceMeshTrafficSplitAuditTests(unittest.TestCase):

    def test_bad_weights(self):
        self.assertTrue(audit({"weights": {"v1": 50, "v2": 40}}))

    def test_ok(self):
        self.assertFalse(audit({"weights": {"v1": 90, "v2": 10}, "canary_weight": 10, "automatic_rollback_configured": True}))
