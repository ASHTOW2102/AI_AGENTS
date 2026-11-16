import unittest
from agent import audit


class MobileAppDeepLinkValidationAuditTests(unittest.TestCase):

    def test_unvalidated(self):
        self.assertTrue(audit({"handles_deep_links": True, "deep_link_origin_validated": False}))

    def test_ok(self):
        self.assertFalse(audit({"handles_deep_links": True, "deep_link_origin_validated": True, "deep_link_can_trigger_sensitive_action": True, "confirmation_required": True}))
