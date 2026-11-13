import unittest
from agent import audit


class KubernetesAdmissionWebhookTimeoutAuditTests(unittest.TestCase):

    def test_long_timeout(self):
        self.assertTrue(audit({"timeout_seconds": 30, "max_acceptable_timeout_seconds": 10}))

    def test_ok(self):
        self.assertFalse(audit({"timeout_seconds": 5, "max_acceptable_timeout_seconds": 10, "failure_policy": "Fail", "high_availability_configured": True}))
