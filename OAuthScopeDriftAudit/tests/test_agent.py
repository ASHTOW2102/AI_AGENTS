import unittest
from agent import audit


class OAuthScopeDriftAuditTests(unittest.TestCase):
    def test_unapproved_grant(self):
        self.assertIn("admin", audit({"granted_scopes": ["read", "admin"], "approved_scopes": ["read"]})[0]["issue"])

    def test_compliant_client(self):
        client = {"granted_scopes": ["read"], "approved_scopes": ["read"], "sensitive_scopes": False,
                  "redirect_uri_exact_match": True}
        self.assertEqual([], audit(client))


if __name__ == "__main__":
    unittest.main()
