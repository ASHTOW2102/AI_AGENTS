import unittest
from agent import audit


class ThirdPartyStatusAuditTests(unittest.TestCase):
    def test_critical_vendor_requires_sla(self):
        self.assertTrue(any("SLA" in f["issue"] for f in audit({"criticality": "high"})))

    def test_review_interval(self):
        self.assertEqual(1, len(audit({"status_page_url": "https://status.invalid", "incident_contact": "ops",
                                       "last_continuity_review_days": 500, "max_review_interval_days": 365})))


if __name__ == "__main__":
    unittest.main()
