import unittest
from agent import audit


class DataSchemaNullabilityAuditTests(unittest.TestCase):
    def test_required_field_relaxed(self):
        self.assertIn("email", audit({"required_non_null_fields": ["email"],
                                       "newly_nullable_fields": ["email"]})[0]["issue"])

    def test_compatible_nullability(self):
        self.assertEqual([], audit({"required_non_null_fields": ["id"], "newly_nullable_fields": [],
                                    "nullable_field_count": 2, "max_nullable_field_count": 5}))


if __name__ == "__main__":
    unittest.main()
