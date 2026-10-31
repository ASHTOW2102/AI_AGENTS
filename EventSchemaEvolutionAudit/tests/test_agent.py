import unittest
from agent import audit


class EventSchemaEvolutionAuditTests(unittest.TestCase):
    def test_type_change(self):
        self.assertIn("type changed", audit({"field_type_changed": True})[0]["issue"])

    def test_compatible_extension(self):
        change = {"required_field_added": False, "field_type_changed": False,
                  "enum_value_removed": False, "breaking_change": False}
        self.assertEqual([], audit(change))


if __name__ == "__main__":
    unittest.main()
