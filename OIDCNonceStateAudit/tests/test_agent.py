import unittest
from agent import audit


class OIDCNonceStateAuditTests(unittest.TestCase):
    def test_missing_nonce_validation(self):
        self.assertIn("nonce", audit({"openid_connect": True, "nonce_validated": False})[0]["issue"])

    def test_secure_flow(self):
        client = {"authorization_code_flow": True, "state_generated_and_validated": True,
                  "openid_connect": True, "nonce_validated": True,
                  "state_bound_to_user_agent_session": True, "pkce_used": True,
                  "pkce_verifier_reused": False}
        self.assertEqual([], audit(client))


if __name__ == "__main__":
    unittest.main()
