import unittest
from agent import audit


class DataContractCompatibilityAuditTests(unittest.TestCase):
    def test_missing_required_field(self):
        self.assertIn("account_id", audit({"consumer_required_fields": ["account_id"], "producer_fields": []})[0]["issue"])

    def test_compatible_contract(self):
        self.assertEqual([], audit({"consumer_required_fields": ["id"], "producer_fields": ["id", "name"],
                                    "incompatible_type_changes": [], "breaking_change": False}))


if __name__ == "__main__":
    unittest.main()
