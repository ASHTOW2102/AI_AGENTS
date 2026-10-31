import unittest
from agent import audit


class SFTPKeyAuthAuditTests(unittest.TestCase):
    def test_missing_host_key_pin(self):
        self.assertIn("not pinned", audit({"host_key_pinned": False})[0]["issue"])

    def test_key_auth_configured(self):
        endpoint = {"password_auth_enabled": False, "host_key_pinned": True,
                    "shared_private_key": False, "key_rotation_schedule": "annual"}
        self.assertEqual([], audit(endpoint))


if __name__ == "__main__":
    unittest.main()
