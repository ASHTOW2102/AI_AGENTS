import unittest
from agent import audit


class MobileAppClipboardLeakAuditTests(unittest.TestCase):

    def test_no_expiry(self):
        self.assertTrue(audit({"copies_sensitive_data_to_clipboard": True, "clipboard_auto_expire_enabled": False}))

    def test_ok(self):
        self.assertFalse(audit({"copies_sensitive_data_to_clipboard": True, "clipboard_auto_expire_enabled": True, "excluded_from_clipboard_history": True}))
