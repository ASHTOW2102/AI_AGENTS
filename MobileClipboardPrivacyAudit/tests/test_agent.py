import unittest
from agent import audit


class MobileClipboardPrivacyAuditTests(unittest.TestCase):
    def test_clipboard_content_logged(self):
        self.assertEqual("critical", audit({"clipboard_access_logged": True, "clipboard_content_logged": True})[0]["severity"])

    def test_restricted_clipboard(self):
        app = {"sensitive_fields_copyable": False, "auth_secrets_copyable": False,
               "clipboard_access_logged": False, "clipboard_content_logged": False}
        self.assertEqual([], audit(app))


if __name__ == "__main__":
    unittest.main()
