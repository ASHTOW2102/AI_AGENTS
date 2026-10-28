import unittest
from agent import audit


class EmailUnsubscribePropagationAuditTests(unittest.TestCase):
    def test_missing_sender_update(self):
        self.assertIn("crm", audit({"sender_systems": ["crm"], "systems_updated": []})[0]["issue"])

    def test_propagated_request(self):
        request = {"sender_systems": ["crm"], "systems_updated": ["crm"],
                   "propagation_minutes": 5, "max_propagation_minutes": 60,
                   "suppression_list_shared": True, "confirmation_recorded": True}
        self.assertEqual([], audit(request))


if __name__ == "__main__":
    unittest.main()
