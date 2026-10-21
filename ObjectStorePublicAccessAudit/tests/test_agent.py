import unittest
from agent import audit


class ObjectStorePublicAccessAuditTests(unittest.TestCase):
    def test_public_bucket_is_critical(self):
        self.assertEqual("critical", audit({"public_access": True})[0]["severity"])

    def test_private_encrypted_bucket(self):
        self.assertEqual([], audit({"public_access": False, "policy_principal": "service-role",
                                    "sensitive_data": True, "access_logging": True, "encryption": True}))


if __name__ == "__main__":
    unittest.main()
