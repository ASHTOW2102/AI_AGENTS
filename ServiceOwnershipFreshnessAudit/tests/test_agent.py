import unittest
from agent import audit


class ServiceOwnershipFreshnessAuditTests(unittest.TestCase):
    def test_missing_technical_owner(self):
        self.assertIn("no technical owner", audit({})[0]["issue"])

    def test_current_ownership(self):
        service = {"technical_owner": "platform", "business_owner": "operations",
                   "owner_review_age_days": 20, "max_owner_review_age_days": 365,
                   "on_call_required": True, "on_call_route_verified": True}
        self.assertEqual([], audit(service))


if __name__ == "__main__":
    unittest.main()
