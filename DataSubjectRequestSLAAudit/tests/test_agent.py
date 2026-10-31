import unittest
from agent import audit


class DataSubjectRequestSLAAuditTests(unittest.TestCase):
    def test_overdue_request(self):
        self.assertIn("exceeds completion SLA", audit({"age_days": 45, "completion_sla_days": 30})[0]["issue"])

    def test_on_time_request(self):
        request = {"age_days": 2, "completion_sla_days": 30, "days_until_due": 28,
                   "owner_assigned": True, "identity_verification_required": False, "closed": False}
        self.assertEqual([], audit(request))


if __name__ == "__main__":
    unittest.main()
