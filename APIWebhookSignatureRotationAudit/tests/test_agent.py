import unittest
from agent import audit


class APIWebhookSignatureRotationAuditTests(unittest.TestCase):
    def test_stale_signing_secret(self):
        self.assertIn("exceeds", audit({"signing_enabled": True, "secret_age_days": 500,
                                        "max_secret_age_days": 365})[0]["issue"])

    def test_rotatable_secret(self):
        endpoint = {"signing_enabled": True, "secret_age_days": 30, "max_secret_age_days": 365,
                    "rotation_in_progress": True, "old_new_overlap_supported": True,
                    "signature_version_tagged": True, "verification_failure_alert": True}
        self.assertEqual([], audit(endpoint))


if __name__ == "__main__":
    unittest.main()
