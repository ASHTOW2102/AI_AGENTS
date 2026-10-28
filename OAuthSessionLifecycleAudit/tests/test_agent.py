import unittest
from agent import audit


class OAuthSessionLifecycleAuditTests(unittest.TestCase):
    def test_rotation_without_reuse_detection(self):
        self.assertTrue(any("reuse" in f["issue"] for f in audit({"refresh_token_rotation": True})))

    def test_short_lived_tokens(self):
        client = {"refresh_token_enabled": True, "refresh_token_rotation": True, "reuse_detection": True,
                  "logout_supported": True, "server_side_revocation": True,
                  "access_token_ttl_minutes": 15, "max_access_token_ttl_minutes": 60}
        self.assertEqual([], audit(client))


if __name__ == "__main__":
    unittest.main()
