import unittest
from agent import audit


class OpenRedirectAuditTests(unittest.TestCase):
    def test_unvalidated_user_redirect(self):
        self.assertIn("allowlist", audit({"user_controlled_redirect": True})[0]["issue"])

    def test_allowlisted_redirects(self):
        policy = {"user_controlled_redirect": True, "destination_allowlist": ["example.test"],
                  "https_only": True, "relative_redirects_only": True, "redirect_chain_max": 3}
        self.assertEqual([], audit(policy))


if __name__ == "__main__":
    unittest.main()
