import unittest
from agent import audit


class KubernetesConfigMapDriftAuditTests(unittest.TestCase):

    def test_drift(self):
        self.assertTrue(audit({"live_values": {"a": "1"}, "declared_values": {"a": "2"}}))

    def test_ok(self):
        self.assertFalse(audit({"live_values": {"a": "1"}, "declared_values": {"a": "1"}, "contains_secret_like_values": False}))
