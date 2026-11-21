import unittest
from agent import audit


class ServiceMeshRateLimitPropagationAuditTests(unittest.TestCase):

    def test_not_propagated(self):
        self.assertTrue(audit({"edge_rate_limited": True, "rate_limit_decision_propagated_internally": False}))

    def test_ok(self):
        self.assertFalse(audit({"edge_rate_limited": True, "rate_limit_decision_propagated_internally": True, "internal_retries_enabled": True}))
