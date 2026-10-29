import unittest
from agent import audit


class WebAuthnChallengeAuditTests(unittest.TestCase):
    def test_reusable_challenge(self):
        self.assertIn("reused", audit({"challenge_single_use": False})[0]["issue"])

    def test_validated_challenge(self):
        policy = {"challenge_ttl_seconds": 60, "max_challenge_ttl_seconds": 300,
                  "challenge_single_use": True, "origin_validation": True, "rp_id_validation": True}
        self.assertEqual([], audit(policy))


if __name__ == "__main__":
    unittest.main()
