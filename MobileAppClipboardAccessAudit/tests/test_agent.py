import unittest
from agent import audit


class MobileAppClipboardAccessAuditTests(unittest.TestCase):

    def test_triggered(self):
        self.assertTrue(audit({"copies_sensitive_data_to_clipboard": True, "clears_clipboard_after_timeout": False}))

    def test_ok(self):
        self.assertFalse(audit({"copies_sensitive_data_to_clipboard": True, "clears_clipboard_after_timeout": True}))
