import unittest
from agent import audit


class MobileAppRootDetectionBypassAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"handles_sensitive_data": True, "checks_root_status": False}))

    def test_ok(self):
        self.assertFalse(audit({"handles_sensitive_data": True, "checks_root_status": True, "root_check_is_client_side_only": False}))
