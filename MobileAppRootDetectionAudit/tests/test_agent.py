import unittest
from agent import audit


class MobileAppRootDetectionAuditTests(unittest.TestCase):

    def test_no_detection(self):
        self.assertTrue(audit({"handles_sensitive_operations": True, "root_detection_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"handles_sensitive_operations": True, "root_detection_enabled": True, "response_on_detection": "restrict_features"}))
