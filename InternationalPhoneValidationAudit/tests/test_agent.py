import unittest
from agent import audit


class InternationalPhoneValidationAuditTests(unittest.TestCase):
    def test_unverified_sensitive_flow(self):
        self.assertIn("before sensitive", audit({"verification_required": True,
                                                  "verification_before_sensitive_action": False})[0]["issue"])

    def test_compliant_form(self):
        form = {"country_code_supported": True, "e164_normalization": True, "verification_required": True,
                "verification_before_sensitive_action": True}
        self.assertEqual([], audit(form))


if __name__ == "__main__":
    unittest.main()
