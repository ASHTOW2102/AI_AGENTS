import unittest
from agent import audit


class FeatureFlagDefaultValueAuditTests(unittest.TestCase):

    def test_risky_fallback(self):
        self.assertTrue(audit({"fallback_value": True, "safe_default_value": False}))

    def test_ok(self):
        self.assertFalse(audit({"fallback_value": False, "safe_default_value": False, "fallback_behavior_tested": True}))
