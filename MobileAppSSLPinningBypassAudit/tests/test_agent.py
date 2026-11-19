import unittest
from agent import audit


class MobileAppSSLPinningBypassAuditTests(unittest.TestCase):

    def test_leaf_only(self):
        self.assertTrue(audit({"certificate_pinning_enabled": True, "pinning_scope": "leaf_only"}))

    def test_ok(self):
        self.assertFalse(audit({"certificate_pinning_enabled": True, "pinning_scope": "public_key", "handles_sensitive_data": True}))
