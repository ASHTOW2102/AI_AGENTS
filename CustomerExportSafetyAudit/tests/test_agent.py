import unittest
from agent import audit


class CustomerExportSafetyAuditTests(unittest.TestCase):
    def test_unencrypted_delivery(self):
        self.assertIn("not confirmed encrypted", audit({"delivery_channel_encrypted": False})[0]["issue"])

    def test_safe_export(self):
        export = {"requester_authorized": True, "includes_sensitive_fields": False,
                  "delivery_channel_encrypted": True, "temporary_copy_created": False}
        self.assertEqual([], audit(export))


if __name__ == "__main__":
    unittest.main()
