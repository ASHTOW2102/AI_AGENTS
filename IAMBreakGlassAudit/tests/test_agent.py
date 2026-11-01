import unittest
from agent import audit


class IAMBreakGlassAuditTests(unittest.TestCase):

    def test_no_alerting(self):
        self.assertTrue(audit({"usage_alerting_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"usage_alerting_enabled": True, "credential_expiry_enforced": True}))
