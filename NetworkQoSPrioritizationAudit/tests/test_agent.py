import unittest
from agent import audit


class NetworkQoSPrioritizationAuditTests(unittest.TestCase):

    def test_no_qos(self):
        self.assertTrue(audit({"carries_latency_sensitive_traffic": True, "carries_bulk_traffic": True, "qos_prioritization_configured": False}))

    def test_ok(self):
        self.assertFalse(audit({"carries_latency_sensitive_traffic": True, "carries_bulk_traffic": True, "qos_prioritization_configured": True, "qos_policy_tested_under_load": True}))
