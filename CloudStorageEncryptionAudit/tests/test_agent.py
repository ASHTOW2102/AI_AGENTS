import unittest
from agent import audit


class CloudStorageEncryptionAuditTests(unittest.TestCase):
    def test_encryption_disabled(self):
        self.assertEqual("critical", audit({"encryption_at_rest_enabled": False})[0]["severity"])

    def test_compliant_storage(self):
        storage = {"encryption_at_rest_enabled": True, "customer_managed_key_required": True,
                   "customer_managed_key_configured": True, "key_rotation_days": 90,
                   "max_key_rotation_days": 365, "unencrypted_object_count": 0}
        self.assertEqual([], audit(storage))


if __name__ == "__main__":
    unittest.main()
