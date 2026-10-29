import unittest
from agent import audit


class OAuthPKCEConfigAuditTests(unittest.TestCase):
    def test_public_client_requires_pkce(self):
        self.assertIn("require PKCE", audit({"public_client": True})[0]["issue"])

    def test_secure_client(self):
        client = {"public_client": True, "pkce_required": True, "pkce_method": "S256",
                  "redirect_uri_exact_match": True, "implicit_flow_enabled": False}
        self.assertEqual([], audit(client))


if __name__ == "__main__":
    unittest.main()
