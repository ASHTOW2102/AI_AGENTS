import unittest
from agent import audit


class MobileCertificateTransparencyAuditTests(unittest.TestCase):
    def test_fail_open_is_risky(self):
        self.assertTrue(any("falls open" in f["issue"] for f in audit({"ct_enforcement_enabled": True, "failure_behavior": "fail_open"})))

    def test_enforced_policy(self):
        app = {"ct_enforcement_enabled": True, "failure_behavior": "fail_closed", "required_scts": 3,
               "minimum_scts": 2, "ct_policy_tested": True}
        self.assertEqual([], audit(app))


if __name__ == "__main__":
    unittest.main()
