import unittest
from agent import audit


class PasswordResetAbuseAuditTests(unittest.TestCase):
    def test_reusable_token(self):
        self.assertIn("reused", audit({"token_single_use": False})[0]["issue"])

    def test_safe_flow(self):
        flow = {"same_response_for_known_and_unknown_users": True, "request_rate_limited": True,
                "token_single_use": True, "token_ttl_minutes": 15, "max_token_ttl_minutes": 60}
        self.assertEqual([], audit(flow))


if __name__ == "__main__":
    unittest.main()
