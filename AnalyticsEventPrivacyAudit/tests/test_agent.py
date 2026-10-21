import unittest

from agent import audit


class AnalyticsEventPrivacyAuditTests(unittest.TestCase):
    def test_reports_unapproved_and_personal_data(self):
        findings = audit({"properties": {"email": "a@example.test"}, "contains_direct_identifiers": True}, set())
        self.assertEqual(2, len(findings))

    def test_clean_event(self):
        self.assertEqual([], audit({"properties": {"source": "web"}, "retention_days": 30,
                                    "approved_retention_days": 30}, {"source"}))


if __name__ == "__main__":
    unittest.main()
