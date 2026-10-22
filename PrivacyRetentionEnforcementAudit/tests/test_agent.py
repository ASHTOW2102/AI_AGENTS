import unittest
from agent import audit


class PrivacyRetentionEnforcementAuditTests(unittest.TestCase):
    def test_retention_exceeds_policy(self):
        self.assertIn("policy maximum", audit({"retention_days": 900, "policy_max_days": 365})[0]["issue"])

    def test_policy_compliant(self):
        record = {"retention_days": 30, "policy_max_days": 90, "deletion_job_enabled": True,
                  "deletion_evidence_retained": True, "deletion_due": False}
        self.assertEqual([], audit(record))


if __name__ == "__main__":
    unittest.main()
