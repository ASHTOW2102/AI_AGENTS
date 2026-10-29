import unittest
from agent import audit


class APISunsetNoticeAuditTests(unittest.TestCase):
    def test_sunset_without_notice(self):
        self.assertIn("notified", audit({"sunset_date": "2027-01-01", "consumer_notice_sent": False})[0]["issue"])

    def test_communicated_deprecation(self):
        endpoint = {"deprecated": True, "deprecation_date": "2026-01-01", "successor_documented": True,
                    "sunset_date": "2027-01-01", "consumer_notice_sent": True,
                    "days_until_sunset": 180, "minimum_notice_days": 90}
        self.assertEqual([], audit(endpoint))


if __name__ == "__main__":
    unittest.main()
