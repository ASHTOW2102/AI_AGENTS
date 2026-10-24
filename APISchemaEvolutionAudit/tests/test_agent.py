import unittest
from agent import audit


class APISchemaEvolutionAuditTests(unittest.TestCase):
    def test_removed_field(self):
        self.assertIn("email", audit({"removed_fields": ["email"]})[0]["issue"])

    def test_nonbreaking_change(self):
        self.assertEqual([], audit({"removed_fields": [], "required_fields_added": [], "enum_values_removed": []}))


if __name__ == "__main__":
    unittest.main()
