import unittest
from agent import audit


class SAMLAssertionAuditTests(unittest.TestCase):
    def test_missing_signature_validation(self):
        self.assertEqual("critical", audit({"signature_validation": False})[0]["severity"])

    def test_validated_assertion_policy(self):
        sp = {"signature_validation": True, "audience_validation": True,
              "recipient_validation": True, "assertion_replay_cache": True}
        self.assertEqual([], audit(sp))


if __name__ == "__main__":
    unittest.main()
